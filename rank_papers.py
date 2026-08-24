"""Rank recent arXiv papers and build a compact research digest.

The script works without an LLM. When LLM_API_KEY is available it calls an
OpenAI-compatible chat completions endpoint for Chinese summaries and a second
relevance assessment.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import logging
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

import arxiv
import requests
import yaml
from bs4 import BeautifulSoup


LOGGER = logging.getLogger("paper-digest")
DATE_PATTERN = re.compile(r"^\|\*\*(\d{4}-\d{2}-\d{2})\*\*\|")
SENTENCE_PATTERN = re.compile(r"(?<=[.!?])\s+")

TRACK_RULES: dict[str, dict[str, int]] = {
    "world model": {
        "world model": 18,
        "video world model": 8,
        "action-conditioned": 14,
        "interactive": 6,
        "closed-loop": 12,
        "driving": 7,
        "simulation": 5,
        "embodied": 5,
    },
    "streaming video": {
        "autoregressive": 12,
        "causal video": 14,
        "streaming": 10,
        "self-forcing": 15,
        "diffusion forcing": 15,
        "long video": 7,
        "temporal consistency": 6,
    },
    "efficient generation": {
        "real-time": 13,
        "acceleration": 9,
        "few-step": 12,
        "distillation": 10,
        "sparse attention": 9,
        "cache": 8,
        "kv cache": 8,
        "efficient": 5,
    },
    "video generation": {
        "video generation": 9,
        "text-to-video": 8,
        "image-to-video": 8,
        "video diffusion": 7,
        "video synthesis": 6,
    },
}

EVIDENCE_CUES = (
    "outperform",
    "state-of-the-art",
    "benchmark",
    "evaluation",
    "experiment",
    "ablation",
)
REPRODUCIBILITY_CUES = ("github", "open-source", "open source", "code is available")
VISUAL_CUES = (
    "video",
    "visual",
    "image",
    "frame",
    "pixel",
    "render",
    "camera",
    "diffusion",
)
SURVEY_CUES = ("survey", "review", "taxonomy")
MAJOR_ORG_CUES = {
    "NVIDIA": ("nvidia", "nvidia research"),
    "MiniMax": ("minimax", "hailuo"),
    "ByteDance / Seedance": ("bytedance", "seedance", "seed ai", "seed research"),
    "Alibaba / Qwen": ("alibaba", "qwen", "tongyi"),
    "Google / DeepMind": ("google deepmind", "deepmind", "google research"),
    "OpenAI": ("openai",),
    "Meta": ("meta ai", "facebook ai research"),
    "Microsoft": ("microsoft research",),
    "Adobe": ("adobe research",),
    "Amazon": ("amazon", "aws ai labs"),
    "Baidu": ("baidu",),
    "Huawei": ("huawei", "noah's ark lab"),
    "Tencent": ("tencent",),
    "Kuaishou": ("kuaishou", "快手"),
    "Stability AI": ("stability ai",),
    "Luma AI": ("luma ai",),
    "Moonshot AI": ("moonshot ai",),
    "Zhipu AI": ("zhipu ai", "zhipu.ai"),
    "Pika": ("pika labs",),
    "Runway": ("runway",),
    "Waymo": ("waymo",),
    "Tesla": ("tesla",),
}


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def detect_major_orgs(text: str) -> list[str]:
    normalized = " ".join(text.lower().split())
    return [
        organization
        for organization, cues in MAJOR_ORG_CUES.items()
        if any(cue in normalized for cue in cues)
    ]


def fetch_arxiv_affiliations(paper_id: str) -> str:
    """Read author affiliations from arXiv HTML without downloading the PDF."""
    response = requests.get(
        f"https://arxiv.org/html/{paper_id}",
        headers={"User-Agent": "paper-lab/1.0"},
        timeout=20,
    )
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    nodes = soup.select(
        ".ltx_role_affiliation, .ltx_affiliation, "
        ".ltx_authors .ltx_personname, .ltx_authors"
    )
    return " ".join(node.get_text(" ", strip=True) for node in nodes)


def enrich_major_orgs(
    papers: list[dict[str, Any]], scan_limit: int, bonus: int
) -> list[dict[str, Any]]:
    """Apply a bounded institution bonus using author affiliation metadata."""
    selected = sorted(papers, key=lambda item: item["score"], reverse=True)[
        :scan_limit
    ]
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = {
            executor.submit(fetch_arxiv_affiliations, paper["id"]): paper
            for paper in selected
        }
        for future in as_completed(futures):
            paper = futures[future]
            try:
                affiliations = future.result()
            except requests.RequestException as exc:
                LOGGER.info("Affiliation lookup skipped for %s: %s", paper["id"], exc)
                continue

            major_orgs = detect_major_orgs(affiliations)
            if not major_orgs:
                continue
            paper["major_orgs"] = major_orgs
            paper["score"] = min(100, paper["score"] + bonus)
            if paper["score"] >= 72:
                paper["priority"] = "must-read"
            elif paper["score"] >= 48:
                paper["priority"] = "skim"
            else:
                paper["priority"] = "archive"
            paper["relevance_cn"] += (
                f"；大厂/重点实验室：{', '.join(major_orgs)}"
                "（机构加分，不替代内容相关性）"
            )
    return papers


def collect_recent_ids(
    database: dict[str, dict[str, str]],
    lookback_days: int,
    today: dt.date | None = None,
) -> list[dict[str, Any]]:
    """Collect recent paper IDs while preserving all matching source topics."""
    today = today or dt.date.today()
    cutoff = today - dt.timedelta(days=lookback_days)
    papers: dict[str, dict[str, Any]] = {}

    for topic, entries in database.items():
        for paper_id, row in entries.items():
            match = DATE_PATTERN.match(row)
            if not match:
                continue
            paper_date = dt.date.fromisoformat(match.group(1))
            if paper_date < cutoff:
                continue
            item = papers.setdefault(
                paper_id,
                {"id": paper_id, "date": paper_date.isoformat(), "topics": []},
            )
            if topic not in item["topics"]:
                item["topics"].append(topic)

    return sorted(
        papers.values(),
        key=lambda item: (item["date"], item["id"]),
        reverse=True,
    )


def fetch_metadata(candidates: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Fetch titles and abstracts only for IDs selected from the existing feed."""
    if not candidates:
        return []

    by_id = {item["id"]: item for item in candidates}
    search = arxiv.Search(id_list=list(by_id), max_results=len(by_id))
    client = arxiv.Client(page_size=min(100, len(by_id)), delay_seconds=3)
    papers: list[dict[str, Any]] = []

    for result in client.results(search):
        paper_id = re.sub(r"v\d+$", "", result.get_short_id())
        candidate = by_id.get(paper_id)
        if candidate is None:
            continue
        papers.append(
            {
                **candidate,
                "title": " ".join(result.title.split()),
                "abstract": " ".join(result.summary.split()),
                "authors": [str(author) for author in result.authors],
                "url": result.entry_id,
                "categories": list(result.categories),
                "comment": result.comment or "",
            }
        )
    return papers


def heuristic_assessment(paper: dict[str, Any]) -> dict[str, Any]:
    """Produce a deterministic relevance score and fallback summary."""
    text = " ".join(
        [
            paper.get("title", ""),
            paper.get("abstract", ""),
            paper.get("comment", ""),
        ]
    ).lower()
    major_orgs: list[str] = []
    matched: list[str] = []
    track_scores: dict[str, int] = {}

    for track, rules in TRACK_RULES.items():
        score = 0
        for phrase, weight in rules.items():
            if phrase in text:
                score += weight
                matched.append(phrase)
        if score:
            track_scores[track] = score

    score = 18 + min(52, sum(track_scores.values()))
    score += min(10, sum(2 for cue in EVIDENCE_CUES if cue in text))
    score += min(8, sum(4 for cue in REPRODUCIBILITY_CUES if cue in text))
    score += min(6, max(0, len(paper.get("topics", [])) - 1) * 3)
    if not any(cue in text for cue in VISUAL_CUES):
        score -= 18
    if any(cue in text for cue in SURVEY_CUES):
        score -= 10
    score = min(100, score)
    score = max(0, score)

    best_tracks = [
        name
        for name, _ in sorted(
            track_scores.items(), key=lambda item: item[1], reverse=True
        )[:2]
    ]
    sentences = SENTENCE_PATTERN.split(paper.get("abstract", ""))
    fallback_summary = sentences[0].strip() if sentences else ""
    if len(fallback_summary) > 520:
        fallback_summary = fallback_summary[:517].rstrip() + "..."
    contribution = next(
        (
            sentence.strip()
            for sentence in sentences
            if re.search(
                r"\b(we (?:propose|present|introduce|develop)|this (?:paper|work) "
                r"(?:proposes|presents|introduces))\b",
                sentence,
                flags=re.IGNORECASE,
            )
        ),
        "请快速查看方法图和主要实验表确认具体贡献。",
    )
    if len(contribution) > 520:
        contribution = contribution[:517].rstrip() + "..."

    if score >= 72:
        priority = "must-read"
    elif score >= 48:
        priority = "skim"
    else:
        priority = "archive"

    unique_matches = list(dict.fromkeys(matched))[:6]
    relation = (
        f"匹配研究线：{', '.join(best_tracks)}；关键词：{', '.join(unique_matches)}"
        if best_tracks
        else "仅与通用视频生成主题弱相关，建议先归档。"
    )
    return {
        **paper,
        "score": score,
        "priority": priority,
        "summary_cn": fallback_summary or "摘要不可用。",
        "contribution_cn": contribution,
        "relevance_cn": relation,
        "limitations_cn": "规则模式无法可靠判断实验质量与论文局限。",
        "assessment_source": "heuristic",
        "major_orgs": major_orgs,
    }


def enforce_reading_budget(
    papers: list[dict[str, Any]], must_read_count: int
) -> list[dict[str, Any]]:
    """Do not label more papers must-read than a human can reasonably process."""
    ordered = sorted(papers, key=lambda item: item["score"], reverse=True)
    used = 0
    for paper in ordered:
        if paper["priority"] == "must-read":
            if used < must_read_count:
                used += 1
            else:
                paper["priority"] = "skim"
    return ordered


def markdown_escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ").strip()


def render_markdown(
    papers: list[dict[str, Any]], generated_at: str, used_llm: bool
) -> str:
    groups = [
        ("must-read", "优先精读"),
        ("skim", "快速浏览"),
        ("archive", "低优先级 / 归档"),
    ]
    mode = "规则评分 + Cursor 全文阅读" if used_llm else "规则评分（未配置 Cursor API Key）"
    lines = [
        "# Generation Research Daily Digest",
        "",
        f"> 生成时间：{generated_at} · 筛选方式：{mode}",
        "> 建议先读“优先精读”，快速浏览只看摘要、方法图和主实验表。",
        "",
    ]

    for key, heading in groups:
        selected = [paper for paper in papers if paper["priority"] == key]
        if not selected:
            continue
        lines.extend([f"## {heading}", ""])
        for index, paper in enumerate(selected, start=1):
            authors = ", ".join(paper["authors"][:3])
            if len(paper["authors"]) > 3:
                authors += " et al."
            abstract_cn = paper.get("abstract_cn", "")
            lines.extend(
                [
                    f"### {index}. [{markdown_escape(paper['title'])}]({paper['url']})",
                    "",
                    f"- **评分**：{paper['score']}/100",
                    f"- **作者**：{markdown_escape(authors)}",
                    f"- **方向**：{markdown_escape(', '.join(paper['topics']))}",
                ]
            )
            if abstract_cn:
                lines.extend(
                    [
                        f"- **Abstract 中文翻译**：{markdown_escape(abstract_cn)}",
                        f"- **全文总结**：{markdown_escape(paper['summary_cn'])}",
                    ]
                )
            else:
                lines.append(
                    f"- **Abstract 摘录**：{markdown_escape(paper['summary_cn'])}"
                )
            lines.extend(
                [
                    f"- **核心贡献**：{markdown_escape(paper['contribution_cn'])}",
                    f"- **与你课题的关系**：{markdown_escape(paper['relevance_cn'])}",
                    f"- **局限 / 待核实**：{markdown_escape(paper['limitations_cn'])}",
                    "",
                ]
            )
    return "\n".join(lines).rstrip() + "\n"


def write_outputs(
    papers: list[dict[str, Any]],
    output_dir: Path,
    generated_at: str,
    used_llm: bool,
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    markdown = render_markdown(papers, generated_at, used_llm)
    date_name = generated_at[:10] + ".md"
    (output_dir / date_name).write_text(markdown, encoding="utf-8")
    payload = {
        "generated_at": generated_at,
        "assessment_mode": "llm+heuristic" if used_llm else "heuristic",
        "papers": papers,
    }
    (output_dir / f"{generated_at[:10]}.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    dated_files = sorted(output_dir.glob("????-??-??.md"), reverse=True)
    index_lines = [
        "# Generation Research Digests",
        "",
        "> 每天一份独立文件；历史精选不会被后续运行覆盖。",
        "",
    ]
    index_lines.extend(f"- [{file.stem}]({file.name})" for file in dated_files)
    (output_dir / "index.md").write_text(
        "\n".join(index_lines) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="config.yaml")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    config = load_yaml(Path(args.config))
    digest = config.get("digest", {})
    source_path = Path(config["json_readme_path"])
    output_dir = Path(digest.get("output_dir", "docs/digests"))
    lookback_days = int(digest.get("lookback_days", 7))
    candidate_limit = int(digest.get("candidate_limit", 60))
    top_n = int(digest.get("top_n", 10))
    must_read_count = int(digest.get("must_read_count", 3))
    affiliation_scan_limit = int(digest.get("affiliation_scan_limit", 30))
    major_org_bonus = int(digest.get("major_org_bonus", 10))

    candidates = collect_recent_ids(load_json(source_path), lookback_days)
    candidates = candidates[:candidate_limit]
    LOGGER.info("Fetching metadata for %d recent papers", len(candidates))
    papers = [heuristic_assessment(paper) for paper in fetch_metadata(candidates)]
    papers = enrich_major_orgs(
        papers,
        scan_limit=affiliation_scan_limit,
        bonus=major_org_bonus,
    )
    papers = enforce_reading_budget(papers, must_read_count)[:top_n]
    generated_at = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
    write_outputs(papers, output_dir, generated_at, used_llm=False)
    LOGGER.info("Wrote digest with %d papers to %s", len(papers), output_dir)


if __name__ == "__main__":
    main()
