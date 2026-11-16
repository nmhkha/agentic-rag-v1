from __future__ import annotations

import unittest

from legal_rag.ingestion.parsers import LegalStructureParser, parse_legal_structure


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

    def test_consolidated_certification_and_quoted_articles_are_suffix(self) -> None:
        text = """VĂN BẢN HỢP NHẤT
Điều 1. Phạm vi điều chỉnh
Nội dung chính.
Điều 2. Hiệu lực thi hành
Văn bản này có hiệu lực.
Số: 01/VBHN | XÁC THỰC VĂN BẢN HỢP NHẤT
CHỦ NHIỆM
[1] Luật sửa đổi có quy định như sau:
“Điều 7. Hiệu lực thi hành
Điều 8. Điều khoản chuyển tiếp”"""
        parser = LegalStructureParser("VBHN", "01/VBHN", "Văn bản mẫu")

        articles = parser.parse(text)

        self.assertEqual([article.number for article in articles], ["1", "2"])
        self.assertEqual(parser.suffix_start_line, 6)
        self.assertEqual(parser.suffix_excluded_line_count, 5)
        self.assertEqual(articles[-1].end_line, 5)

    def test_terminal_publication_block_is_not_part_of_last_article(self) -> None:
        text = """Điều 1. Điều khoản thi hành
1. Nội dung quy phạm cuối cùng.
Nơi nhận:
- Cơ quan liên quan;
PHỤ LỤC I
Điều 1. Điều trong biểu mẫu"""
        parser = LegalStructureParser("DOC", "01/2026", "Văn bản mẫu")

        articles = parser.parse(text)

        self.assertEqual([article.number for article in articles], ["1"])
        self.assertEqual(articles[-1].end_line, 2)
        self.assertEqual(parser.suffix_start_line, 3)
        self.assertEqual(parser.appendix_start_line, 5)

    def test_law_certification_is_not_part_of_last_article(self) -> None:
        text = """Điều 1. Điều khoản chuyển tiếp
Nội dung quy phạm.
Luật này được Quốc hội nước Cộng hòa xã hội chủ nghĩa Việt Nam thông qua.
CHỦ TỊCH QUỐC HỘI
Nguyễn Văn A"""
        parser = LegalStructureParser("DOC", "01/2026", "Luật mẫu")

        articles = parser.parse(text)

        self.assertEqual(articles[-1].end_line, 2)
        self.assertEqual(parser.suffix_start_line, 3)


if __name__ == "__main__":
    unittest.main()
