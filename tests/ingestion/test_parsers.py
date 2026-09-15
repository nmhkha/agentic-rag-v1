from __future__ import annotations

import unittest

from legal_rag.ingestion.parsers import parse_legal_structure


LEGAL_TEXT = """Phần thứ NHẤT
QUY ĐỊNH CHUNG
Chương I
NGUYÊN TẮC
Mục 1
PHẠM VI
Tiểu mục 1
QUY ĐỊNH CHI TIẾT
Điều 1. Phạm vi điều chỉnh
Lời mở đầu.
1. Khoản thứ nhất
a) Điểm A
Nội dung tiếp.
Điều 2.
Tên điều thứ hai
đ) Điểm trực tiếp
Phụ lục I
Điều 1. Không được parse
1. Nội dung phụ lục"""


class ParserTests(unittest.TestCase):
    def test_full_hierarchy_clause_point_and_appendix_exclusion(self) -> None:
        articles = parse_legal_structure(
            LEGAL_TEXT,
            document_id="DOC",
            document_number="01/2026",
            document_title="Luật mẫu",
        )
        self.assertEqual([article.number for article in articles], ["1", "2"])
        first = articles[0].to_dict()
        self.assertEqual(first["part"], "NHẤT")
        self.assertEqual(first["chapter"], "I")
        self.assertEqual(first["section"], "1")
        self.assertEqual(first["subsection"], "1")
        self.assertEqual(first["clauses"][0]["clause"], "1")
        self.assertEqual(first["clauses"][0]["points"][0]["point"], "a")
        self.assertEqual(articles[1].direct_points[0].number.lower(), "đ")

    def test_parser_is_deterministic(self) -> None:
        first = [
            article.to_dict()
            for article in parse_legal_structure(
                LEGAL_TEXT,
                document_id="DOC",
                document_number="01/2026",
                document_title="Luật mẫu",
            )
        ]
        second = [
            article.to_dict()
            for article in parse_legal_structure(
                LEGAL_TEXT,
                document_id="DOC",
                document_number="01/2026",
                document_title="Luật mẫu",
            )
        ]
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
