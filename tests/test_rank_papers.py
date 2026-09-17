import datetime as dt
import tempfile
import unittest
from pathlib import Path

from cursor_summarize import select_papers_for_summary
from rank_papers import (
    _extract_json_object,
    collect_recent_ids,
    enforce_reading_budget,
    heuristic_assessment,
    paper_note_filename,
    render_markdown,
    write_must_read_notes,
)


class RankPapersTests(unittest.TestCase):
    def test_collect_recent_ids_deduplicates_topics(self):
        database = {
            "World Models": {
                "2408.00001": "|**2026-08-23**|**Paper**|A et.al.|[id](url)|null|\n"
            },
            "Efficient Video Diffusion": {
                "2408.00001": "|**2026-08-23**|**Paper**|A et.al.|[id](url)|null|\n",
                "2401.00002": "|**2026-01-01**|**Old**|B et.al.|[id](url)|null|\n",
            },
        }

        result = collect_recent_ids(
            database, lookback_days=7, today=dt.date(2026, 8, 24)
        )

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["id"], "2408.00001")
        self.assertEqual(
            result[0]["topics"], ["World Models", "Efficient Video Diffusion"]
        )

    def test_heuristic_prioritizes_core_research_terms(self):
        paper = {
            "id": "2408.00001",
            "date": "2026-08-23",
            "topics": ["World Models", "Efficient Video Diffusion"],
            "title": "Real-Time Action-Conditioned Video World Models",
            "abstract": (
                "We introduce a closed-loop world model with sparse attention. "
                "Experiments outperform prior work on a driving benchmark. "
                "Code is available."
            ),
            "comment": "",
            "authors": ["A. Author"],
            "url": "https://arxiv.org/abs/2408.00001",
            "categories": ["cs.CV"],
        }

        assessed = heuristic_assessment(paper)

        self.assertGreaterEqual(assessed["score"], 72)
        self.assertEqual(assessed["priority"], "must-read")
        self.assertIn("world model", assessed["relevance_cn"])

    def test_reading_budget_caps_must_read_items(self):
        papers = [
            {"id": "1", "score": 95, "priority": "must-read"},
            {"id": "2", "score": 90, "priority": "must-read"},
            {"id": "3", "score": 85, "priority": "must-read"},
        ]

        result = enforce_reading_budget(papers, must_read_count=2)

        self.assertEqual(
            [paper["priority"] for paper in result],
            ["must-read", "must-read", "skim"],
        )

    def test_nonvisual_world_model_paper_is_penalized(self):
        paper = {
            "id": "2408.00002",
            "date": "2026-08-23",
            "topics": ["World Models"],
            "title": "World-Model-Grounded Language Planning",
            "abstract": (
                "We propose a world model for language-based route planning. "
                "The planner predicts symbolic robot commands."
            ),
            "comment": "",
            "authors": ["A. Author"],
            "url": "https://arxiv.org/abs/2408.00002",
            "categories": ["cs.RO"],
        }

        assessed = heuristic_assessment(paper)

        self.assertLess(assessed["score"], 48)
        self.assertEqual(assessed["priority"], "archive")

    def test_extracts_json_from_fenced_response(self):
        parsed = _extract_json_object('```json\n{"papers": []}\n```')
        self.assertEqual(parsed, {"papers": []})

    def test_digest_warns_when_llm_is_not_configured(self):
        paper = {
            "id": "1",
            "score": 60,
            "priority": "skim",
            "title": "A Paper",
            "url": "https://arxiv.org/abs/1",
            "authors": ["A"],
            "topics": ["Video Generation"],
            "summary_cn": "Summary.",
            "contribution_cn": "Contribution.",
            "relevance_cn": "Relevant.",
            "limitations_cn": "Unknown.",
        }

        output = render_markdown(
            [paper], "2026-08-24T00:00:00+00:00", used_llm=False
        )

        self.assertIn("未配置 Cursor API Key", output)
        self.assertIn("快速浏览", output)
        self.assertIn("一句话", output)
        self.assertNotIn("核心贡献", output)

    def test_digest_keeps_must_read_short_and_links_notes(self):
        paper = {
            "id": "2609.11548",
            "score": 80,
            "priority": "must-read",
            "title": "World in World",
            "url": "https://arxiv.org/abs/2609.11548",
            "authors": ["A"],
            "topics": ["World Models"],
            "abstract_cn": "很长的中文摘要不应出现在 digest 里。",
            "summary_cn": "全文总结。",
            "contribution_cn": "贡献。",
            "relevance_cn": "相关。",
            "limitations_cn": "局限。",
            "assessment_source": "cursor:gpt-5.6-luna",
            "note_path": "2026-09-16/2609.11548-world-in-world.md",
        }

        output = render_markdown(
            [paper], "2026-09-16T00:00:00+00:00", used_llm=True
        )

        self.assertIn("Cursor 全文阅读", output)
        self.assertIn("精读笔记", output)
        self.assertIn("../notes/2026-09-16/2609.11548-world-in-world.md", output)
        self.assertNotIn("很长的中文摘要不应出现在 digest 里", output)
        self.assertNotIn("核心贡献", output)

    def test_writes_one_note_file_per_must_read_paper_by_date(self):
        papers = [
            {
                "id": "2609.11548",
                "score": 80,
                "priority": "must-read",
                "title": "World in World",
                "url": "https://arxiv.org/abs/2609.11548",
                "authors": ["A"],
                "topics": ["World Models"],
                "abstract_cn": "中文摘要。",
                "summary_cn": "全文总结。",
                "contribution_cn": "贡献。",
                "relevance_cn": "相关。",
                "limitations_cn": "局限。",
                "assessment_source": "cursor:gpt-5.6-luna",
            },
            {
                "id": "x",
                "score": 60,
                "priority": "skim",
                "title": "Skim Paper",
                "url": "https://arxiv.org/abs/x",
                "authors": ["B"],
                "topics": ["Video Generation"],
                "summary_cn": "Skim.",
                "contribution_cn": "C",
                "relevance_cn": "R",
                "limitations_cn": "L",
            },
        ]

        with tempfile.TemporaryDirectory() as tmp:
            notes_dir = Path(tmp)
            written = write_must_read_notes(
                papers, notes_dir, "2026-09-16T00:00:00+00:00"
            )
            note_path = notes_dir / "2026-09-16" / paper_note_filename(papers[0])
            self.assertEqual(len(written), 1)
            self.assertTrue(note_path.exists())
            self.assertTrue((notes_dir / "index.md").exists())
            self.assertTrue((notes_dir / "2026-09-16" / "index.md").exists())
            content = note_path.read_text(encoding="utf-8")
            self.assertIn("中文摘要。", content)
            self.assertIn("全文总结。", content)
            self.assertNotIn("Skim Paper", content)

    def test_summary_selection_prefers_must_read_papers(self):
        papers = [
            {"id": "skim", "priority": "skim"},
            {"id": "must-2", "priority": "must-read"},
            {"id": "must-1", "priority": "must-read"},
            {"id": "must-3", "priority": "must-read"},
        ]

        selected = select_papers_for_summary(papers, max_papers=3)

        self.assertEqual(
            [paper["id"] for paper in selected],
            ["must-2", "must-1", "must-3"],
        )


if __name__ == "__main__":
    unittest.main()
