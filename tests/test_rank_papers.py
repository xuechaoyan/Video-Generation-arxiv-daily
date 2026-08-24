import datetime as dt
import unittest

from rank_papers import (
    _extract_json_object,
    collect_recent_ids,
    enforce_reading_budget,
    heuristic_assessment,
    render_markdown,
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

        self.assertIn("未配置模型 API Key", output)
        self.assertIn("快速浏览", output)


if __name__ == "__main__":
    unittest.main()
