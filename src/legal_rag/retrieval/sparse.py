from __future__ import annotations

import argparse
import json
import re
import unicodedata
from pathlib import Path
from typing import Any

from rank_bm25 import BM25Okapi

from ..paths import CORPUS_VERSION_DIR

DEFAULT_CORPUS_PATH = CORPUS_VERSION_DIR / "chunks.jsonl"


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
        self.bm25 = BM25Okapi(tokenized_corpus)

    def search(
        self,
        query: str,
        top_k: int = 5,
    ) -> list[dict[str, Any]]:
        query_tokens = tokenize(query)

        if not query_tokens:
            return []

        scores = self.bm25.get_scores(query_tokens)

        ranked_indices = sorted(
            range(len(scores)),
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
