#!/usr/bin/env python3
"""Unified frozen retrieval interface for legal-rag-v0."""

from __future__ import annotations

from dataclasses import asdict, dataclass, replace
from typing import TYPE_CHECKING, Any

# Keep the evaluated configuration importable for lightweight formatting and
# unit tests. The heavyweight reranker (and its torch dependency) is loaded
# only when a real default retriever is requested.
BM25_DEPTH = 20
DENSE_DEPTH = 20
MODEL_ID = "BAAI/bge-reranker-v2-m3"

if TYPE_CHECKING:
    from .reranker import RerankerRetriever

RETRIEVAL_PIPELINE = "BM25-simple-v0@20 + dense-jina-v3-v0@20 union -> BAAI/bge-reranker-v2-m3"
DEFAULT_TOP_K = 5


@dataclass(frozen=True)
class Evidence:
    rank: int
    evidence_id: str
    chunk_id: str
    document_id: str | None
    document_number: str | None
    document_title: str | None
    article_id: str | None
    article: str | None
    article_label: str | None
    clause: str | None
    clause_label: str | None
    point: str | None
    point_label: str | None
    text: str
    retrieval_text: str
    official_source_url: str | None
    reranker_score: float
    bm25_rank: int | None
    dense_rank: int | None
    # These fields make the object self-describing for Agentic RAG traces while
    # retaining the constructor used by the v0 runtime and its tests.
    retrieval_source: str = RETRIEVAL_PIPELINE
    retrieval_rank: int | None = None

    @property
    def source_url(self) -> str | None:
        return self.official_source_url

    @property
    def clause_id(self) -> str | None:
        if self.clause in (None, "") or not self.article_id:
            return None
        return f"{self.article_id}_khoan-{self.clause}"

    @property
    def point_id(self) -> str | None:
        if self.point in (None, "") or not self.clause_id:
            return None
        return f"{self.clause_id}_diem-{self.point}"

    def to_dict(self) -> dict[str, Any]:
        value = asdict(self)
        # Keep the original v0 keys and expose the v1 names as well. This is
        # useful when traces are consumed by tools that only know the spec.
        value.update({
            "source_url": self.source_url,
            "clause_id": self.clause_id,
            "point_id": self.point_id,
        })
        return value


def _label(prefix: str, value: Any) -> str | None:
    return f"{prefix} {value}" if value not in (None, "") else None


def evidence_from_result(result: dict[str, Any], rank: int) -> Evidence:
    chunk = result["chunk"]
    document_id = chunk.get("document_id")
    article = chunk.get("article")
    article_id = chunk.get("article_id")
    if not article_id and document_id not in (None, "") and article not in (None, ""):
        article_id = f"{document_id}_dieu-{article}"
    return Evidence(
        rank=rank,
        evidence_id=f"E{rank}",
        chunk_id=str(chunk["chunk_id"]),
        document_id=document_id,
        document_number=chunk.get("document_number"),
        document_title=chunk.get("document_title"),
        article_id=article_id,
        article=article,
        article_label=_label("Điều", article),
        clause=chunk.get("clause"),
        clause_label=_label("Khoản", chunk.get("clause")),
        point=chunk.get("point"),
        point_label=_label("Điểm", chunk.get("point")),
        text=str(chunk.get("text", "")),
        retrieval_text=str(chunk.get("retrieval_text", "")),
        official_source_url=chunk.get("official_source_url"),
        reranker_score=float(result["reranker_score"]),
        bm25_rank=result.get("bm25_rank"),
        dense_rank=result.get("dense_rank"),
        retrieval_rank=result.get("rank", rank),
    )


class RetrievalPipeline:
    """Loads the evaluated retrievers once and exposes stable Evidence objects."""

    def __init__(self, retriever: "RerankerRetriever | None" = None, batch_size: int | None = None):
        if retriever is None:
            from .reranker import RerankerRetriever
            retriever = RerankerRetriever(batch_size=batch_size)
        self.retriever = retriever

    def retrieve(self, query: str, top_k: int = DEFAULT_TOP_K) -> list[Evidence]:
        if top_k < 1:
            raise ValueError("top_k must be >= 1")
        results = self.retriever.search(query, top_k)
        seen: set[str] = set()
        evidences: list[Evidence] = []
        for result in results:
            chunk_id = str(result["chunk"]["chunk_id"])
            if chunk_id in seen:
                continue
            seen.add(chunk_id)
            evidences.append(evidence_from_result(result, len(evidences) + 1))
        return evidences

    def retrieve_with_audit(
        self, query: str, top_k: int = DEFAULT_TOP_K, *, all_candidates: bool = False
    ) -> tuple[list[Evidence], dict[str, Any]]:
        """Run the frozen pipeline and return evidence plus retrieval metadata.

        ``search_with_candidates`` is part of the evaluated reranker runtime,
        so this method records its intermediate results without introducing a
        second retrieval implementation. Lightweight test doubles that only
        implement ``search`` remain supported.
        """
        if top_k < 1:
            raise ValueError("top_k must be >= 1")
        search_with_candidates = getattr(self.retriever, "search_with_candidates", None)
        search_k = BM25_DEPTH + DENSE_DEPTH if all_candidates else top_k
        if search_with_candidates is None:
            results = self.retriever.search(query, top_k)
            candidates = []
        else:
            results, candidates = search_with_candidates(query, search_k)
        seen: set[str] = set()
        evidences: list[Evidence] = []
        for result in results:
            chunk_id = str(result["chunk"]["chunk_id"])
            if chunk_id in seen:
                continue
            seen.add(chunk_id)
            evidences.append(evidence_from_result(result, len(evidences) + 1))
        if candidates:
            candidate_ids = [str(item.chunk["chunk_id"]) for item in candidates]
        else:
            candidate_ids = [item.chunk_id for item in evidences]
        audit = {
            "query": query,
            "bm25_depth": BM25_DEPTH,
            "dense_depth": DENSE_DEPTH,
            "candidate_chunk_ids": candidate_ids,
            "candidate_count": len(candidate_ids),
            "reranker_ranks": [
                {"chunk_id": item.chunk_id, "rank": item.rank,
                 "reranker_score": item.reranker_score}
                for item in evidences
            ],
            "top5_chunk_ids": [item.chunk_id for item in evidences[:DEFAULT_TOP_K]],
            "candidate_ranks": ([
                {"chunk_id": str(item.chunk["chunk_id"]),
                 "bm25_rank": item.bm25_rank, "dense_rank": item.dense_rank}
                for item in candidates
            ] if candidates else [
                {"chunk_id": item.chunk_id, "bm25_rank": item.bm25_rank,
                 "dense_rank": item.dense_rank}
                for item in evidences
            ]),
        }
        return evidences, audit

    def rerank_evidence_pool(
        self, query: str, evidence_pool: list[Evidence], top_k: int = DEFAULT_TOP_K
    ) -> list[Evidence]:
        """Rerank a merged evidence pool with the baseline BGE reranker.

        No fusion signal is introduced here: candidates are scored only by the
        same cross-encoder used by the baseline. A small deterministic fallback
        keeps injected test retrievers usable when they do not expose a BGE
        scorer.
        """
        if top_k < 1:
            raise ValueError("top_k must be >= 1")
        unique: dict[str, Evidence] = {}
        for item in evidence_pool:
            unique.setdefault(item.chunk_id, item)
        pool = list(unique.values())
        reranker = getattr(getattr(self, "retriever", None), "reranker", None)
        if reranker is None or not hasattr(reranker, "rerank"):
            ranked = sorted(pool, key=lambda item: (-item.reranker_score, item.chunk_id))
            return [replace(item, rank=index) for index, item in enumerate(ranked[:top_k], 1)]

        # Import lazily so the light-weight v0 wrapper does not import torch.
        from .reranker import Candidate

        candidates = [Candidate(
            chunk=self._chunk_dict(item),
            bm25_rank=item.bm25_rank,
            dense_rank=item.dense_rank,
        ) for item in pool]
        results = reranker.rerank(query, candidates, top_k)
        by_chunk_id = {item.chunk_id: item for item in pool}
        final: list[Evidence] = []
        for index, result in enumerate(results, 1):
            rescored = evidence_from_result(result, index)
            original = by_chunk_id[rescored.chunk_id]
            final.append(Evidence(
                rank=index, evidence_id=original.evidence_id,
                chunk_id=rescored.chunk_id, document_id=rescored.document_id,
                document_number=rescored.document_number,
                document_title=rescored.document_title,
                article_id=rescored.article_id, article=rescored.article,
                article_label=rescored.article_label, clause=rescored.clause,
                clause_label=rescored.clause_label, point=rescored.point,
                point_label=rescored.point_label, text=rescored.text,
                retrieval_text=rescored.retrieval_text,
                official_source_url=rescored.official_source_url,
                reranker_score=rescored.reranker_score,
                bm25_rank=original.bm25_rank, dense_rank=original.dense_rank,
                retrieval_source=original.retrieval_source,
                retrieval_rank=original.retrieval_rank,
            ))
        return final

    @staticmethod
    def _chunk_dict(item: Evidence) -> dict[str, Any]:
        return {
            "chunk_id": item.chunk_id,
            "document_id": item.document_id,
            "document_number": item.document_number,
            "document_title": item.document_title,
            "article_id": item.article_id,
            "article": item.article,
            "clause": item.clause,
            "point": item.point,
            "text": item.text,
            "retrieval_text": item.retrieval_text or item.text,
            "official_source_url": item.official_source_url,
        }

_default_pipeline: RetrievalPipeline | None = None


def retrieve(query: str, top_k: int = DEFAULT_TOP_K) -> list[Evidence]:
    global _default_pipeline
    if _default_pipeline is None:
        _default_pipeline = RetrievalPipeline()
    return _default_pipeline.retrieve(query, top_k)


def retrieval_config() -> dict[str, Any]:
    return {
        "bm25": "BM25-simple-v0",
        "bm25_depth": BM25_DEPTH,
        "dense": "dense-jina-v3-v0",
        "dense_depth": DENSE_DEPTH,
        "candidate_merge": "union_deduplicate_by_chunk_id",
        "fusion": None,
        "reranker": MODEL_ID,
        "top_k": DEFAULT_TOP_K,
    }
