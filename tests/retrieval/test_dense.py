from __future__ import annotations

import json
import unittest
from pathlib import Path
from unittest.mock import patch

import numpy as np

from legal_rag.retrieval.dense import (
    DENSE_MODEL_REVISION,
    DenseRetriever,
)


class FakeModel:
    def encode(self, texts, **kwargs):
        return np.asarray([[1.0, 0.0] for _ in texts], dtype=np.float32)


class DenseTests(unittest.TestCase):
    def test_frozen_metadata_and_chunk_alignment_load(self) -> None:
        root = Path(__file__).parents[2]
        manifest = json.loads(
            (root / "experiments/indexes/dense-jina-v3-v0/index_manifest.json").read_text()
        )
        self.assertEqual(manifest["resolved_model_revision"], DENSE_MODEL_REVISION)
        with patch("legal_rag.retrieval.dense.select_device", return_value="cpu"), patch(
            "legal_rag.retrieval.dense.load_model", return_value=FakeModel()
        ):
            retriever = DenseRetriever(
                root / "data/versions/corpus-v0.1/chunks.jsonl",
                root / "experiments/indexes/dense-jina-v3-v0",
            )
        self.assertEqual(len(retriever.chunk_ids), len(retriever.chunks))
        self.assertEqual(
            retriever.chunk_ids,
            [chunk["chunk_id"] for chunk in retriever.chunks],
        )

    def test_similarity_ranking_is_descending_and_stable_for_ties(self) -> None:
        retriever = DenseRetriever.__new__(DenseRetriever)
        retriever.chunks = [
            {"chunk_id": "a"}, {"chunk_id": "b"}, {"chunk_id": "c"}
        ]
        retriever.embeddings = np.asarray(
            [[0.0, 1.0], [1.0, 0.0], [1.0, 0.0]], dtype=np.float32
        )
        retriever.model = FakeModel()
        retriever.batch_size = 2
        rows = retriever.search("query", top_k=3)
        self.assertEqual([row["chunk"]["chunk_id"] for row in rows], ["b", "c", "a"])
        self.assertEqual([row["rank"] for row in rows], [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
