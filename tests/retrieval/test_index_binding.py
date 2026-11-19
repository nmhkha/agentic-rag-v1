from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

import numpy as np

from legal_rag.retrieval.dense import (
    DENSE_MODEL_REVISION,
    MODEL_ID,
    DenseRetriever,
    load_model,
)
from legal_rag.retrieval.sparse import PersistentBM25Retriever, build_sparse_index


FINGERPRINT = "a" * 64


def write_corpus(path: Path) -> list[dict]:
    rows = [
        {"chunk_id": "one", "retrieval_text": "Điều một"},
        {"chunk_id": "two", "retrieval_text": "Điều hai"},
    ]
    path.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows))
    return rows


class IndexBindingTests(unittest.TestCase):
    def test_sparse_loader_enforces_fingerprint_and_mapping(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            corpus = root / "chunks.jsonl"
            rows = write_corpus(corpus)
            index = root / "sparse.json"
            build_sparse_index(rows, index)
            manifest = root / "manifest.json"
            manifest.write_text(json.dumps({"corpus_fingerprint_sha256": FINGERPRINT}))
            loaded = PersistentBM25Retriever(
                corpus, index, manifest, corpus_fingerprint=FINGERPRINT
            )
            self.assertEqual(len(loaded.chunks), 2)
            with self.assertRaisesRegex(ValueError, "fingerprint mismatch"):
                PersistentBM25Retriever(
                    corpus, index, manifest, corpus_fingerprint="b" * 64
                )

    def test_dense_metadata_loader_enforces_fingerprint_and_revision(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            corpus = root / "chunks.jsonl"
            rows = write_corpus(corpus)
            index = root / "dense"
            index.mkdir()
            vectors = np.zeros((2, 1024), dtype=np.float32)
            vectors[:, 0] = 1.0
            np.save(index / "embeddings.npy", vectors, allow_pickle=False)
            (index / "chunk_ids.json").write_text(json.dumps([row["chunk_id"] for row in rows]))
            (index / "index_manifest.json").write_text(json.dumps({
                "model_id": MODEL_ID,
                "resolved_model_revision": DENSE_MODEL_REVISION,
                "query_task": "retrieval.query",
                "normalized": True,
                "corpus_fingerprint_sha256": FINGERPRINT,
            }))
            loaded = DenseRetriever(
                corpus, index, corpus_fingerprint=FINGERPRINT, load_encoder=False
            )
            self.assertEqual(loaded.embeddings.shape, (2, 1024))
            with self.assertRaisesRegex(ValueError, "fingerprint mismatch"):
                DenseRetriever(
                    corpus, index, corpus_fingerprint="b" * 64, load_encoder=False
                )

    def test_dense_model_loading_is_local_only(self) -> None:
        fake = MagicMock()
        with patch("transformers.AutoModel.from_pretrained", return_value=fake) as loader:
            load_model(MODEL_ID, DENSE_MODEL_REVISION, "cpu")
        self.assertTrue(loader.call_args.kwargs["local_files_only"])


if __name__ == "__main__":
    unittest.main()
