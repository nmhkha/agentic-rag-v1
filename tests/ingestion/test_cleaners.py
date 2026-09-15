from __future__ import annotations

import unicodedata
import unittest

from legal_rag.ingestion.cleaners import clean_text, normalize_single_line


class CleanerTests(unittest.TestCase):
    def test_nfc_nbsp_horizontal_space_line_endings_and_blank_lines(self) -> None:
        decomposed = "A\u0301p"
        raw = f"  {decomposed}\u00a0 dụng\t  luật  \r\n\r\n\r\nĐiều 1.  Tên\r"
        cleaned, removed = clean_text(raw, set())
        self.assertEqual(cleaned, "Áp dụng luật\n\nĐiều 1. Tên")
        self.assertEqual(unicodedata.normalize("NFC", cleaned), cleaned)
        self.assertEqual(removed, [])

    def test_only_exact_normalized_boilerplate_is_removed(self) -> None:
        cleaned, removed = clean_text(
            "Đầu\n  Tải về tại ví dụ.vn  \nTải về tại ví dụ.vn!\nCuối",
            {normalize_single_line("Tải về tại ví dụ.vn")},
        )
        self.assertEqual(cleaned, "Đầu\nTải về tại ví dụ.vn!\nCuối")
        self.assertEqual(removed, ["Tải về tại ví dụ.vn"])

    def test_representative_cleaning_contract(self) -> None:
        raw = "e\u0301\u00a0  x\r\n\r\n\r\nREMOVE\nĐiều 1. Giữ nguyên"
        self.assertEqual(clean_text(raw, {"REMOVE"}), ("é x\n\nĐiều 1. Giữ nguyên", ["REMOVE"]))


if __name__ == "__main__":
    unittest.main()
