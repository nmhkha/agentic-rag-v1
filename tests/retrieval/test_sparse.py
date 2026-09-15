from __future__ import annotations

import unittest

from legal_rag.retrieval.sparse import BM25Retriever, normalize_text, tokenize


class SparseTests(unittest.TestCase):
    def test_normalization_and_tokenization_contract(self) -> None:
        text = "  HỆ\u00a0THỐNG AI-2026, Điều 9!  "
        self.assertEqual(normalize_text(text), "hệ thống ai-2026, điều 9!")
        self.assertEqual(tokenize(text), ["hệ", "thống", "ai", "2026", "điều", "9"])

    def test_score_ranking_top_k_and_empty_query_contract(self) -> None:
        chunks = [
            {"chunk_id": "first", "retrieval_text": "alpha common"},
            {"chunk_id": "second", "retrieval_text": "beta common"},
            {"chunk_id": "third", "retrieval_text": "alpha alpha"},
        ]
        retriever = BM25Retriever(chunks)
        rows = retriever.search("alpha", 2)
        self.assertEqual([row["chunk"]["chunk_id"] for row in rows], ["second", "first"])
        self.assertEqual([row["rank"] for row in rows], [1, 2])
        self.assertEqual(retriever.search("", 2), [])


if __name__ == "__main__":
    unittest.main()
