from __future__ import annotations

import unittest

from legal_rag.ingestion.validators import (
    ValidationCollector,
    parse_iso_date,
    validate_articles,
    validate_chunks,
)


class ValidatorTests(unittest.TestCase):
    def test_date_and_article_identity_rules(self) -> None:
        collector = ValidationCollector()
        self.assertIsNone(
            parse_iso_date(
                "2026/01/01",
                field_name="issued_date",
                context="row",
                collector=collector,
                required=True,
            )
        )
        registry = {"DOC": {}}
        articles = [{
            "_jsonl_line": 1,
            "article_id": "wrong",
            "document_id": "DOC",
            "document_number": "01/2026",
            "document_title": "Luật mẫu",
            "article": "1",
            "article_title": "Tên",
            "start_line": 1,
            "end_line": 2,
            "clauses": [{"clause": "1", "points": []}, {"clause": "1", "points": []}],
            "direct_points": [],
        }]
        validate_articles(articles, registry, collector)
        joined = "\n".join(collector.errors)
        self.assertIn("issued_date không đúng YYYY-MM-DD", joined)
        self.assertIn("article_id không khớp", joined)
        self.assertIn("khoản trùng", joined)

    def test_chunk_duplicate_and_retrieval_containment_rules(self) -> None:
        collector = ValidationCollector()
        registry = {"DOC": {key: "" for key in (
            "document_number", "document_title", "document_type",
            "issuing_authority", "issued_date", "effective_from", "effective_to",
            "status", "corpus_layer", "official_source_url", "official_pdf_path",
            "working_docx_path", "extraction_method", "verification_status",
        )}}
        article = {"article_id": "DOC_dieu-1"}
        base = {
            "_jsonl_line": 1, "chunk_id": "same", "document_id": "DOC",
            "article": "1", "clause": "", "point": "", "chunk_level": "article",
            "text": "Nội dung đủ dài để kiểm tra", "retrieval_text": "không chứa",
            "structure_path_text": "Điều 1", "corpus_version": "v1",
            "segment_index": 1, "segment_count": 1,
        }
        validate_chunks([base, {**base, "_jsonl_line": 2}], registry, {"DOC_dieu-1": article}, collector)
        joined = "\n".join(collector.errors)
        self.assertIn("chunk_id trùng", joined)
        self.assertIn("retrieval_text không chứa nguyên text", joined)


if __name__ == "__main__":
    unittest.main()
