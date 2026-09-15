from __future__ import annotations

import unittest

from legal_rag.generation.formatter import format_final_response, parse_model_output


class FormatterTests(unittest.TestCase):
    def test_parse_valid_fenced_embedded_and_invalid_contract(self) -> None:
        fenced = parse_model_output('```json\n{"answer":" A [E1] ","used_evidence_ids":["E1"]}\n```')
        embedded = parse_model_output('prefix {"answer":" B ","used_evidence_ids":[],"missing_information":[]} suffix')
        self.assertEqual(fenced["answer"], "A [E1]")
        self.assertEqual(embedded["answer"], "B")
        for raw in ("not json", '{"answer": 1}'):
            with self.subTest(raw=raw), self.assertRaises(ValueError):
                parse_model_output(raw)

    def test_final_serialization_contract(self) -> None:
        mapping = {"E1": {
            "document_number": "1/2026/QH", "article": "2", "clause": "1",
            "point": None, "official_source_url": "https://example.test/law",
        }}
        self.assertEqual(format_final_response("Trả lời [E1]", ["E1"], mapping),
                         "Trả lời [E1]\n\nNguồn tham chiếu:\n\n[E1] 1/2026/QH, Điều 2, Khoản 1\nOfficial source: https://example.test/law")


if __name__ == "__main__":
    unittest.main()
