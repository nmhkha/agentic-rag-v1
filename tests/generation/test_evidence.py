from __future__ import annotations

import unittest

from legal_rag.generation.evidence import format_evidence
from legal_rag.retrieval.pipeline import Evidence


def evidence(rank: int, *, missing: bool = False) -> Evidence:
    return Evidence(
        rank=rank, evidence_id=f"E{rank}", chunk_id=f"chunk-{rank}",
        document_id="doc", document_number=None if missing else "1/2026/QH",
        document_title="Luật mẫu", article_id="doc_dieu-2", article="2",
        article_label="Điều 2", clause=None if missing else "1",
        clause_label=None if missing else "Khoản 1", point=None, point_label=None,
        text=f"Nội dung {rank}.", retrieval_text=f"metadata\nNội dung {rank}.",
        official_source_url=None if missing else "https://example.test/law",
        reranker_score=1.0, bm25_rank=rank, dense_rank=None,
    )


class EvidenceTests(unittest.TestCase):
    def test_format_order_separators_and_missing_metadata(self) -> None:
        values = [evidence(1), evidence(2, missing=True)]
        context, mapping = format_evidence(values)
        self.assertTrue(context.startswith("[E1]\nVăn bản: Luật mẫu\nSố văn bản: 1/2026/QH"))
        self.assertIn("\n\n[E2]\n", context)
        self.assertNotIn("metadata\n", context)
        self.assertEqual(list(mapping), ["E1", "E2"])

    def test_empty_input(self) -> None:
        self.assertEqual(format_evidence([]), ("", {}))

    def test_format_includes_vertical_overlap_parent_leads(self) -> None:
        item = Evidence(
            rank=1, evidence_id="E1", chunk_id="134-2025-QH15_dieu-6_khoan-2_diem-a",
            document_id="134-2025-QH15", document_number="134/2025/QH15",
            document_title="Luật Trí tuệ nhân tạo", article_id="134-2025-QH15_dieu-6",
            article="6", article_label="Điều 6", clause="2", clause_label="Khoản 2",
            point="a", point_label="Điểm a",
            text="Lĩnh vực y tế: bảo đảm an toàn cho người bệnh;",
            retrieval_text="Luật Trí tuệ nhân tạo\nĐiều 6\nKhoản 2\nĐiểm a)\nLĩnh vực y tế: bảo đảm an toàn cho người bệnh;",
            official_source_url="https://example.test/law",
            reranker_score=1.0, bm25_rank=1, dense_rank=1,
            parent_context=(
                "Văn bản: Luật Trí tuệ nhân tạo (134/2025/QH15)\n"
                "Điều 6: Ứng dụng trí tuệ nhân tạo\n"
                "Khoản 2\n"
                "Nội dung dẫn của khoản: Đối với các lĩnh vực thiết yếu phải quản lý rủi ro chặt chẽ hơn:"
            ),
        )
        context, _ = format_evidence([item])
        self.assertIn(
            "Nội dung dẫn của khoản: Đối với các lĩnh vực thiết yếu phải quản lý rủi ro chặt chẽ hơn:",
            context,
        )


if __name__ == "__main__":
    unittest.main()
