#!/usr/bin/env python3
"""Fixed cross-encoder baseline over BM25@20 union Dense@20 candidates."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

try:
    import torch
    from transformers import AutoModelForSequenceClassification, AutoTokenizer
except ImportError:
    torch = None  # type: ignore[assignment]
    AutoModelForSequenceClassification = None  # type: ignore[assignment]
    AutoTokenizer = None  # type: ignore[assignment]

from ..paths import CORPUS_VERSION_DIR
from .dense import DEFAULT_INDEX_DIR, DenseRetriever
from .sparse import BM25Retriever, PersistentBM25Retriever, read_chunks

EXPERIMENT = "bge-reranker-v2-m3-v0"
MODEL_ID = "BAAI/bge-reranker-v2-m3"
RERANKER_MODEL_REVISION = "953dc6f6f85a1b2dbfca4c34a2796e7dde08d41e"
CORPUS_PATH = CORPUS_VERSION_DIR / "chunks.jsonl"
BM25_DEPTH = 20
DENSE_DEPTH = 20
MAX_LENGTH = 8192
FINAL_DEPTH = 10


@dataclass
class Candidate:
    chunk: dict[str, Any]
    bm25_rank: int | None = None
    bm25_score: float | None = None
    dense_rank: int | None = None
    dense_score: float | None = None


def rank_candidates(
    scores: list[float], candidates: list[Candidate], top_k: int
) -> list[dict[str, Any]]:
    """Apply the frozen score ordering and lexical tie-break."""
    scored = list(zip(scores, candidates))
    scored.sort(key=lambda item: (-item[0], item[1].chunk["chunk_id"]))
    return [{
        "rank": rank, "score": score, "reranker_score": score,
        "chunk": candidate.chunk,
        "bm25_rank": candidate.bm25_rank, "bm25_score": candidate.bm25_score,
        "dense_rank": candidate.dense_rank, "dense_score": candidate.dense_score,
    } for rank, (score, candidate) in enumerate(scored[:top_k], 1)]


def union_candidates(
    bm25_results: list[dict[str, Any]], dense_results: list[dict[str, Any]]
) -> list[Candidate]:
    """Union by chunk_id; component ranks are metadata, never fusion signals."""
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
    return list(merged.values())


class BGEReranker:
    def __init__(self, model_id: str = MODEL_ID, revision: str | None = None,
                 max_length: int = MAX_LENGTH, batch_size: int | None = None) -> None:
        torch.manual_seed(0)
        if torch.cuda.is_available(): torch.cuda.manual_seed_all(0)
        torch.use_deterministic_algorithms(True)
        self.model_id = model_id
        self.max_length = max_length
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.dtype = "float16" if self.device == "cuda" else "float32"
        self.batch_size = batch_size or (8 if self.device == "cuda" else 1)
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(
                model_id, revision=revision, local_files_only=True
            )
        except Exception:
            self.tokenizer = AutoTokenizer.from_pretrained(model_id, revision=revision)
        kwargs: dict[str, Any] = {"revision": revision}
        if self.device == "cuda":
            kwargs["torch_dtype"] = torch.float16
        try:
            self.model = AutoModelForSequenceClassification.from_pretrained(
                model_id, local_files_only=True, **kwargs
            )
        except Exception:
            self.model = AutoModelForSequenceClassification.from_pretrained(model_id, **kwargs)
        self.model.to(self.device)
        self.model.eval()
        self.resolved_revision = str(self.model.config._commit_hash)

    def score(self, query: str, passages: list[str]) -> list[float]:
        scores: list[float] = []
        with torch.inference_mode():
            for start in range(0, len(passages), self.batch_size):
                batch = passages[start:start + self.batch_size]
                encoded = self.tokenizer(
                    [query] * len(batch), batch, padding=True, truncation=True,
                    max_length=self.max_length, return_tensors="pt",
                ).to(self.device)
                logits = self.model(**encoded, return_dict=True).logits.reshape(-1)
                scores.extend(float(value) for value in logits.float().cpu().tolist())
        return scores

    def rerank(self, query: str, candidates: list[Candidate], top_k: int) -> list[dict[str, Any]]:
        """Rank only by reranker score descending, then lexical chunk_id."""
        passages = [contextual_passage(candidate.chunk) for candidate in candidates]
        return rank_candidates(self.score(query, passages), candidates, top_k)


def extract_vertical_leads(
    parent_context: str | None, body_text: str = ""
) -> tuple[str | None, str | None]:
    """Extract (article_intro, clause_lead) from parent_context when not redundant."""
    if not parent_context:
        return None, None
    article_intro: str | None = None
    clause_lead: str | None = None
    norm_body = body_text.strip()
    for raw_line in parent_context.splitlines():
        line = raw_line.strip()
        if line.startswith("Mở đầu điều:"):
            val = line[len("Mở đầu điều:") :].strip()
            if val and val != norm_body:
                article_intro = val
        elif line.startswith("Nội dung dẫn của khoản:"):
            val = line[len("Nội dung dẫn của khoản:") :].strip()
            if val and val != norm_body:
                clause_lead = val
    return article_intro, clause_lead


def contextual_passage(chunk: dict[str, Any]) -> str:
    """Build reranker passage with vertical parent lead overlap when available."""
    base = str(chunk.get("retrieval_text", ""))
    article_intro, clause_lead = extract_vertical_leads(
        chunk.get("parent_context"), str(chunk.get("text", ""))
    )
    if not article_intro and not clause_lead:
        return base

    lines = base.splitlines()
    enriched: list[str] = []
    inserted_intro = not bool(article_intro and article_intro not in base)
    inserted_clause = not bool(clause_lead and clause_lead not in base)

    for line in lines:
        enriched.append(line)
        stripped = line.strip()
        if not inserted_intro and stripped.startswith("Điều "):
            enriched.append(article_intro)  # type: ignore[arg-type]
            inserted_intro = True
        elif not inserted_clause and stripped.startswith("Khoản "):
            enriched.append(clause_lead)  # type: ignore[arg-type]
            inserted_clause = True

    return "\n".join(enriched)


def rerank(query: str, candidates: list[Candidate], top_k: int,
           scorer: BGEReranker | None = None) -> list[dict[str, Any]]:
    """Public fixed-baseline reranking entry point."""
    return (scorer or BGEReranker()).rerank(query, candidates, top_k)


class RerankerRetriever:
    def __init__(self, corpus_path: Path = CORPUS_PATH, index_dir: Path = DEFAULT_INDEX_DIR,
                 batch_size: int | None = None) -> None:
        sparse_index = index_dir.parent / "sparse" / "sparse_index.json"
        sparse_manifest = index_dir.parent / "manifests" / "sparse_manifest.json"
        corpus_fingerprint: str | None = None
        if sparse_index.is_file() and sparse_manifest.is_file():
            manifest = json.loads(sparse_manifest.read_text(encoding="utf-8"))
            corpus_fingerprint = manifest.get("corpus_fingerprint_sha256")
            self.bm25: BM25Retriever = PersistentBM25Retriever(
                corpus_path,
                sparse_index,
                sparse_manifest,
                corpus_fingerprint=corpus_fingerprint or "",
            )
        else:
            chunks = read_chunks(corpus_path)
            self.bm25 = BM25Retriever(chunks)
        self.dense = DenseRetriever(
            corpus_path,
            index_dir,
            batch_size=batch_size,
            corpus_fingerprint=corpus_fingerprint,
        )
        self.reranker = BGEReranker(
            revision=RERANKER_MODEL_REVISION,
            batch_size=batch_size,
        )

    def search_with_candidates(
        self, query: str, top_k: int = FINAL_DEPTH, *, document_id: str | None = None
    ):
        if document_id is None:
            bm25 = self.bm25.search(query, BM25_DEPTH)
            dense = self.dense.search(query, DENSE_DEPTH)
        else:
            bm25 = self.bm25.search(query, BM25_DEPTH, document_id=document_id)
            dense = self.dense.search(query, DENSE_DEPTH, document_id=document_id)
        candidates = union_candidates(bm25, dense)
        return self.reranker.rerank(query, candidates, top_k), candidates

    def search(
        self, query: str, top_k: int = FINAL_DEPTH, *, document_id: str | None = None
    ) -> list[dict[str, Any]]:
        return self.search_with_candidates(query, top_k, document_id=document_id)[0]
