from __future__ import annotations

import tempfile
import unittest
import zipfile
from pathlib import Path

from legal_rag.ingestion.extractors import extract_document


DOCUMENT_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:body>
    <w:p><w:r><w:t>QUỐC HỘI</w:t></w:r></w:p>
    <w:p/>
    <w:tbl>
      <w:tr><w:tc><w:p><w:r><w:t>Điều 1.</w:t></w:r></w:p></w:tc><w:tc><w:p><w:r><w:t>Phạm vi</w:t></w:r></w:p></w:tc></w:tr>
      <w:tr><w:tc><w:p/></w:tc><w:tc><w:p/></w:tc></w:tr>
    </w:tbl>
    <w:p><w:r><w:t>1. Nội dung</w:t></w:r></w:p>
  </w:body>
</w:document>"""


class ExtractorTests(unittest.TestCase):
    def test_paragraph_and_table_order_and_counts(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "legal.docx"
            with zipfile.ZipFile(path, "w") as archive:
                archive.writestr("word/document.xml", DOCUMENT_XML)
            text, paragraphs, tables = extract_document(path)
        self.assertEqual(
            text, "QUỐC HỘI\n\nĐiều 1. | Phạm vi\n\n1. Nội dung"
        )
        self.assertEqual(paragraphs, 2)
        self.assertEqual(tables, 1)

    def test_existing_corpus_matches_preserved_raw_artifact(self) -> None:
        root = Path(__file__).parents[2]
        docx = root / "data/raw/docx/05-2026-TT-BKHCN.docx"
        expected = root / "data/extracted/05-2026-TT-BKHCN.raw.txt"
        actual, _, _ = extract_document(docx)
        self.assertEqual(actual.encode(), expected.read_bytes())


if __name__ == "__main__":
    unittest.main()
