#!/usr/bin/env python3
"""Equal-weight reciprocal-rank fusion of the frozen BM25 and Dense baselines."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from ..paths import CORPUS_VERSION_DIR
from .dense import DEFAULT_INDEX_DIR, DenseRetriever
from .sparse import BM25Retriever, read_chunks

RETRIEVER_NAME = "hybrid-rrf-v0"
CORPUS_PATH = CORPUS_VERSION_DIR / "chunks.jsonl"
BM25_CANDIDATE_DEPTH = 20
DENSE_CANDIDATE_DEPTH = 20
RRF_K = 60


@dataclass(frozen=True)
class Candidate:
    chunk: dict[str, Any]
    bm25_rank: int | None = None
    bm25_score: float | None = None
    dense_rank: int | None = None
    dense_score: float | None = None


def _missing_last(rank: int | None) -> int:
    return rank if rank is not None else BM25_CANDIDATE_DEPTH + DENSE_CANDIDATE_DEPTH + 1


def fuse_rankings(
    bm25_results: list[dict[str, Any]], dense_results: list[dict[str, Any]], top_k: int
) -> list[dict[str, Any]]:
    """Fuse rankings with the experiment's fixed score and deterministic tie-break."""
    merged: dict[str, Candidate] = {}
    for result in bm25_results:
        chunk = result["chunk"]
        merged[chunk["chunk_id"]] = Candidate(
            chunk=chunk, bm25_rank=result["rank"], bm25_score=result["score"]
        )
    for result in dense_results:
        chunk = result["chunk"]
        old = merged.get(chunk["chunk_id"])
        merged[chunk["chunk_id"]] = Candidate(
            chunk=chunk,
            bm25_rank=old.bm25_rank if old else None,
            bm25_score=old.bm25_score if old else None,
            dense_rank=result["rank"],
            dense_score=result["score"],
        )

    scored: list[tuple[float, Candidate]] = []
    for candidate in merged.values():
        score = 0.0
        if candidate.bm25_rank is not None:
            score += 1.0 / (RRF_K + candidate.bm25_rank)
        if candidate.dense_rank is not None:
            score += 1.0 / (RRF_K + candidate.dense_rank)
        scored.append((score, candidate))

    scored.sort(
        key=lambda item: (
            -item[0],
            min(_missing_last(item[1].bm25_rank), _missing_last(item[1].dense_rank)),
            _missing_last(item[1].bm25_rank),
            _missing_last(item[1].dense_rank),
            item[1].chunk["chunk_id"],
        )
    )
    return [
        {
            "rank": rank,
            "rrf_score": score,
            "score": score,
            "chunk": candidate.chunk,
            "bm25_rank": candidate.bm25_rank,
            "bm25_score": candidate.bm25_score,
            "dense_rank": candidate.dense_rank,
            "dense_score": candidate.dense_score,
        }
        for rank, (score, candidate) in enumerate(scored[:top_k], 1)
    ]


class HybridRRFRetriever:
    def __init__(self, corpus_path: Path = CORPUS_PATH, index_dir: Path = DEFAULT_INDEX_DIR) -> None:
        chunks = read_chunks(corpus_path)
        self.bm25 = BM25Retriever(chunks)
        self.dense = DenseRetriever(corpus_path, index_dir)

    def search_with_candidates(self, query: str, top_k: int = 10):
        bm25 = self.bm25.search(query, BM25_CANDIDATE_DEPTH)
        dense = self.dense.search(query, DENSE_CANDIDATE_DEPTH)
        return fuse_rankings(bm25, dense, top_k), bm25, dense

    def search(self, query: str, top_k: int = 10) -> list[dict[str, Any]]:
        return self.search_with_candidates(query, top_k)[0]
