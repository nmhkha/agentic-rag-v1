from __future__ import annotations

import csv
import json
import unittest
from pathlib import Path

from legal_rag.ingestion.chunking import build_chunks, serialize_chunks


class ChunkingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.root = Path(__file__).parents[2]
        with (cls.root / "data/source_registry/documents.csv").open(
            encoding="utf-8-sig", newline=""
        ) as handle:
            rows = list(csv.DictReader(handle))
        cls.registry = {
            row["document_id"].strip(): {
                key: (value or "").strip() for key, value in row.items()
            }
            for row in rows
        }
        cls.articles = [
            json.loads(line)
            for line in (cls.root / "data/processed/articles.jsonl")
            .read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]

    def test_current_corpus_is_byte_and_semantically_equivalent(self) -> None:
        chunks = build_chunks(self.articles, self.registry)
        frozen = self.root / "data/processed/chunks.jsonl"
        self.assertEqual(len(chunks), 737)
        self.assertEqual(serialize_chunks(chunks), frozen.read_bytes())

    def test_chunk_ids_are_unique_and_order_is_deterministic(self) -> None:
        first = build_chunks(self.articles, self.registry)
        second = build_chunks(self.articles, self.registry)
        ids = [row["chunk_id"] for row in first]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
