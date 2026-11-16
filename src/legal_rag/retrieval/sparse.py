from __future__ import annotations

import argparse
import hashlib
import json
import re
import unicodedata
from pathlib import Path
from typing import Any

from rank_bm25 import BM25Okapi

from ..paths import CORPUS_VERSION_DIR

DEFAULT_CORPUS_PATH = CORPUS_VERSION_DIR / "chunks.jsonl"
RETRIEVER_NAME = "BM25-simple-v0"
BM25_K1 = 1.5
BM25_B = 0.75
BM25_EPSILON = 0.25


def normalize_text(text: str) -> str:
    text = unicodedata.normalize("NFC", text)
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def tokenize(text: str) -> list[str]:
    text = normalize_text(text)
    return re.findall(
        r"[0-9]+|[a-zà-ỹđ]+",
        text,
        flags=re.IGNORECASE,
    )


def read_chunks(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        raise FileNotFoundError(f"Không tìm thấy corpus: {path}")

    chunks: list[dict[str, Any]] = []

    with path.open("r", encoding="utf-8") as file:
        for line_number, raw_line in enumerate(file, start=1):
            line = raw_line.strip()
            if not line:
                continue

            try:
                chunk = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(
                    f"JSON lỗi tại dòng {line_number}: {exc}"
                ) from exc

            chunk_id = str(chunk.get("chunk_id", "")).strip()
            retrieval_text = str(
                chunk.get("retrieval_text", "")
            ).strip()

            if not chunk_id:
                raise ValueError(
                    f"Dòng {line_number}: thiếu chunk_id"
                )

            if not retrieval_text:
                raise ValueError(
                    f"Dòng {line_number} ({chunk_id}): "
                    "thiếu retrieval_text"
                )

            chunks.append(chunk)

    if not chunks:
        raise ValueError("Corpus không có chunk nào")

    return chunks


class BM25Retriever:
    def __init__(self, chunks: list[dict[str, Any]]) -> None:
        self.chunks = chunks
        tokenized_corpus = [
            tokenize(str(chunk["retrieval_text"]))
            for chunk in chunks
        ]
        self.bm25 = BM25Okapi(
            tokenized_corpus,
            k1=BM25_K1,
            b=BM25_B,
            epsilon=BM25_EPSILON,
        )

    def search(
        self,
        query: str,
        top_k: int = 5,
        *,
        document_id: str | None = None,
    ) -> list[dict[str, Any]]:
        query_tokens = tokenize(query)

        if not query_tokens:
            return []

        scores = self.bm25.get_scores(query_tokens)

        eligible_indices = (
            range(len(scores))
            if document_id is None
            else (
                index for index, chunk in enumerate(self.chunks)
                if str(chunk.get("document_id", "")) == document_id
            )
        )
        ranked_indices = sorted(
            eligible_indices,
            key=lambda index: scores[index],
            reverse=True,
        )[:top_k]

        results = []

        for rank, index in enumerate(ranked_indices, start=1):
            results.append(
                {
                    "rank": rank,
                    "score": float(scores[index]),
                    "chunk": self.chunks[index],
                }
            )

        return results


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def build_sparse_index(chunks: list[dict[str, Any]], output_path: Path) -> dict[str, Any]:
    """Persist the canonical BM25 inputs without changing their corpus order."""
    chunk_ids = [str(chunk["chunk_id"]) for chunk in chunks]
    if len(set(chunk_ids)) != len(chunk_ids):
        raise ValueError("Duplicate chunk_id in corpus")
    tokenized_corpus = [tokenize(str(chunk["retrieval_text"])) for chunk in chunks]
    if any(not tokens for tokens in tokenized_corpus):
        raise ValueError("Sparse index contains an empty tokenized document")
    payload = {
        "index_version": "1",
        "retriever_name": RETRIEVER_NAME,
        "input_field": "retrieval_text",
        "parameters": {"b": BM25_B, "epsilon": BM25_EPSILON, "k1": BM25_K1},
        "chunk_ids": chunk_ids,
        "tokenized_corpus": tokenized_corpus,
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n",
        encoding="utf-8",
    )
    return {
        "document_count": len(chunk_ids),
        "unique_chunk_ids": len(set(chunk_ids)),
        "vocabulary_size": len({token for row in tokenized_corpus for token in row}),
        "artifact_sha256": sha256(output_path),
    }


class PersistentBM25Retriever(BM25Retriever):
    """Load a persisted canonical BM25 index and enforce corpus binding."""

    def __init__(
        self,
        corpus_path: Path,
        index_path: Path,
        manifest_path: Path,
        *,
        corpus_fingerprint: str,
    ) -> None:
        chunks = read_chunks(corpus_path)
        payload = json.loads(index_path.read_text(encoding="utf-8"))
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        chunk_ids = [str(chunk["chunk_id"]) for chunk in chunks]
        if payload.get("retriever_name") != RETRIEVER_NAME:
            raise ValueError("Sparse retrieval configuration is incompatible")
        if payload.get("parameters") != {
            "b": BM25_B, "epsilon": BM25_EPSILON, "k1": BM25_K1
        }:
            raise ValueError("Sparse BM25 parameters are incompatible")
        if payload.get("chunk_ids") != chunk_ids:
            raise ValueError("Sparse index ordering does not match corpus ordering")
        if manifest.get("corpus_fingerprint_sha256") != corpus_fingerprint:
            raise ValueError("Sparse index corpus fingerprint mismatch")
        tokenized_corpus = payload.get("tokenized_corpus")
        expected_tokens = [tokenize(str(chunk["retrieval_text"])) for chunk in chunks]
        if tokenized_corpus != expected_tokens:
            raise ValueError("Sparse index inputs do not match corpus retrieval_text")
        self.chunks = chunks
        self.bm25 = BM25Okapi(
            tokenized_corpus,
            k1=BM25_K1,
            b=BM25_B,
            epsilon=BM25_EPSILON,
        )
