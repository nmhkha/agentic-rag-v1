from __future__ import annotations

import unittest
from pathlib import Path

from legal_rag.generation.prompts import build_prompt, load_prompt


class PromptTests(unittest.TestCase):
    def test_load_preserves_prompt_bytes_as_text(self) -> None:
        root = Path(__file__).parents[2]
        path = root / "prompts/legal_rag_v0.txt"
        self.assertEqual(load_prompt(path), path.read_text(encoding="utf-8"))

    def test_construction_replaces_query_then_evidence(self) -> None:
        query = "Quy định {evidence_context} có áp dụng?"
        context = "[E1]\nNội dung nguyên văn"
        result = build_prompt(query, context)
        self.assertIn("Quy định [E1]\nNội dung nguyên văn có áp dụng?", result)
        self.assertIn(context, result)


if __name__ == "__main__":
    unittest.main()
