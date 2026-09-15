from __future__ import annotations

import unittest

from legal_rag.retrieval.pipeline import RetrievalPipeline, retrieval_config
from legal_rag.retrieval.reranker import RerankerRetriever, rank_candidates, union_candidates


def chunk(chunk_id: str) -> dict:
    return {
        "chunk_id": chunk_id,
        "document_id": "DOC",
        "document_number": "01/2026",
        "document_title": "Luật mẫu",
        "article": "1",
        "clause": "2",
        "point": "a",
        "text": f"body {chunk_id}",
        "retrieval_text": f"retrieval {chunk_id}",
        "official_source_url": "https://example.invalid/law",
    }


class FixedRetriever:
    def __init__(self, rows):
        self.rows = rows

    def search(self, query, top_k):
        return self.rows[:top_k]


class FixedReranker:
    def rerank(self, query, candidates, top_k):
        scores = {"dense": 3.0, "shared": 2.0, "sparse": 1.0}
        return rank_candidates(
            [scores[item.chunk["chunk_id"]] for item in candidates], candidates, top_k
        )


class PipelineTests(unittest.TestCase):
    def test_candidate_union_reranking_top_k_and_evidence_compatibility(self) -> None:
        retriever = RerankerRetriever.__new__(RerankerRetriever)
        retriever.bm25 = FixedRetriever([
            {"rank": 1, "score": 4.0, "chunk": chunk("shared")},
            {"rank": 2, "score": 3.0, "chunk": chunk("sparse")},
        ])
        retriever.dense = FixedRetriever([
            {"rank": 1, "score": 0.9, "chunk": chunk("dense")},
            {"rank": 2, "score": 0.8, "chunk": chunk("shared")},
        ])
        retriever.reranker = FixedReranker()
        pipeline = RetrievalPipeline(retriever=retriever)
        evidence = pipeline.retrieve("question", top_k=2)
        self.assertEqual([item.chunk_id for item in evidence], ["dense", "shared"])
        value = evidence[0].to_dict()
        for key in ("evidence_id", "chunk_id", "article_id", "clause_id", "point_id", "source_url", "retrieval_text"):
            self.assertIn(key, value)
        self.assertEqual(value["article_id"], "DOC_dieu-1")
        self.assertEqual(value["clause_id"], "DOC_dieu-1_khoan-2")

    def test_config_explicitly_excludes_rrf(self) -> None:
        config = retrieval_config()
        self.assertEqual(config["bm25_depth"], 20)
        self.assertEqual(config["dense_depth"], 20)
        self.assertIsNone(config["fusion"])
        self.assertEqual(config["top_k"], 5)


if __name__ == "__main__":
    unittest.main()
