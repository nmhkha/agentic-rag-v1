from __future__ import annotations

import unittest

from legal_rag.retrieval.reranker import Candidate, rank_candidates, union_candidates


def result(chunk_id: str, rank: int, score: float) -> dict:
    return {
        "rank": rank,
        "score": score,
        "chunk": {"chunk_id": chunk_id, "retrieval_text": f"text {chunk_id}"},
    }


class RerankerTests(unittest.TestCase):
    def test_union_deduplicates_without_using_component_scores(self) -> None:
        candidates = union_candidates(
            [result("shared", 1, 4.0), result("sparse", 2, 3.0)],
            [result("dense", 1, 0.9), result("shared", 2, 0.8)],
        )
        self.assertEqual([item.chunk["chunk_id"] for item in candidates], ["shared", "sparse", "dense"])
        self.assertEqual((candidates[0].bm25_rank, candidates[0].dense_rank), (1, 2))

    def test_ranking_uses_score_then_lexical_chunk_id_and_top_k(self) -> None:
        candidates = [
            Candidate({"chunk_id": "z", "retrieval_text": "z"}),
            Candidate({"chunk_id": "a", "retrieval_text": "a"}),
            Candidate({"chunk_id": "low", "retrieval_text": "low"}),
        ]
        rows = rank_candidates([2.0, 2.0, -1.0], candidates, 2)
        self.assertEqual([row["chunk"]["chunk_id"] for row in rows], ["a", "z"])
        self.assertEqual([row["reranker_score"] for row in rows], [2.0, 2.0])


if __name__ == "__main__":
    unittest.main()
