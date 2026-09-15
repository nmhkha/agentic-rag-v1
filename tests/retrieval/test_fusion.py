from __future__ import annotations

import unittest

from legal_rag.retrieval.fusion import RRF_K, fuse_rankings


def result(chunk_id: str, rank: int, score: float) -> dict:
    return {"rank": rank, "score": score, "chunk": {"chunk_id": chunk_id}}


class FusionTests(unittest.TestCase):
    def test_rrf_math_duplicates_order_and_ties(self) -> None:
        rows = fuse_rankings(
            [result("shared", 1, 9.0), result("bm25", 2, 8.0)],
            [result("shared", 2, 0.9), result("dense", 1, 0.8)],
            3,
        )
        self.assertEqual([row["chunk"]["chunk_id"] for row in rows], ["shared", "dense", "bm25"])
        self.assertAlmostEqual(rows[0]["rrf_score"], 1 / (RRF_K + 1) + 1 / (RRF_K + 2))
        self.assertEqual(rows[0]["bm25_rank"], 1)
        self.assertEqual(rows[0]["dense_rank"], 2)

    def test_final_tie_break_is_lexical_chunk_id(self) -> None:
        rows = fuse_rankings(
            [result("z", 1, 1.0), result("a", 1, 1.0)], [], 2
        )
        self.assertEqual([row["chunk"]["chunk_id"] for row in rows], ["a", "z"])


if __name__ == "__main__":
    unittest.main()
