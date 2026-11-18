from __future__ import annotations

import argparse
import hashlib
import json
import re
import unicodedata
from pathlib import Path
from typing import Any

try:
    from rank_bm25 import BM25Okapi
except ImportError:
    import math

    class BM25Okapi:  # type: ignore[no-redef]
        def __init__(
            self,
            corpus: list[list[str]],
            k1: float = 1.5,
            b: float = 0.75,
            epsilon: float = 0.25,
        ) -> None:
            self.k1 = k1
            self.b = b
            self.epsilon = epsilon
            self.corpus_size = len(corpus)
            self.doc_freqs: list[dict[str, int]] = []
            self.idf: dict[str, float] = {}
            self.doc_len: list[int] = []
            nd: dict[str, int] = {}
            num_doc = 0
            for document in corpus:
                self.doc_len.append(len(document))
                num_doc += len(document)
                frequencies: dict[str, int] = {}
                for word in document:
                    frequencies[word] = frequencies.get(word, 0) + 1
                self.doc_freqs.append(frequencies)
                for word in frequencies:
                    nd[word] = nd.get(word, 0) + 1
            self.avgdl = num_doc / self.corpus_size if self.corpus_size else 0.0
            idf_sum = 0.0
            negative_idfs: list[str] = []
            for word, freq in nd.items():
                idf = math.log(self.corpus_size - freq + 0.5) - math.log(freq + 0.5)
                self.idf[word] = idf
                idf_sum += idf
                if idf < 0:
                    negative_idfs.append(word)
            self.average_idf = idf_sum / len(self.idf) if self.idf else 0.0
            eps = self.epsilon * self.average_idf
            for word in negative_idfs:
                self.idf[word] = eps

        def get_scores(self, query: list[str]) -> list[float]:
            scores = [0.0] * self.corpus_size
            for q in query:
                q_idf = self.idf.get(q)
                if q_idf is None:
                    continue
                for i, doc_freq in enumerate(self.doc_freqs):
                    f = doc_freq.get(q, 0)
                    if f:
                        dl = self.doc_len[i]
                        scores[i] += q_idf * (f * (self.k1 + 1)) / (
                            f + self.k1 * (1 - self.b + self.b * dl / self.avgdl)
                        )
            return scores

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


def bm25_input_text(chunk: dict[str, Any]) -> str:
    """Return retrieval_text enriched with vertical parent leads when present."""
    base = str(chunk.get("retrieval_text", ""))
    parent_ctx = chunk.get("parent_context")
    if not isinstance(parent_ctx, str) or not parent_ctx.strip():
        return base
    norm_body = str(chunk.get("text", "")).strip()
    leads: list[str] = []
    for raw_line in parent_ctx.splitlines():
        line = raw_line.strip()
        if line.startswith("Mở đầu điều:"):
            val = line[len("Mở đầu điều:") :].strip()
            if val and val != norm_body and val not in base:
                leads.append(val)
        elif line.startswith("Nội dung dẫn của khoản:"):
            val = line[len("Nội dung dẫn của khoản:") :].strip()
            if val and val != norm_body and val not in base:
                leads.append(val)
    if not leads:
        return base
    return base + "\n" + "\n".join(leads)


class BM25Retriever:
    def __init__(self, chunks: list[dict[str, Any]]) -> None:
        self.chunks = chunks
        tokenized_corpus = [
            tokenize(bm25_input_text(chunk))
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
