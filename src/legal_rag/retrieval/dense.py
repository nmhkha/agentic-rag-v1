#!/usr/bin/env python3
"""Dense-only retrieval with jinaai/jina-embeddings-v3."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np

from ..paths import CORPUS_VERSION_DIR, INDEX_DIR

RETRIEVER_NAME = "dense-jina-v3-v0"
MODEL_ID = "jinaai/jina-embeddings-v3"
DEFAULT_CORPUS_PATH = CORPUS_VERSION_DIR / "chunks.jsonl"
DEFAULT_INDEX_DIR = INDEX_DIR / RETRIEVER_NAME
QUERY_TASK = "retrieval.query"
EXPECTED_DIMENSION = 1024
PASSAGE_TASK = "retrieval.passage"
EXPECTED_COUNT = 737
DENSE_MODEL_REVISION = "ab036b023d30b4d1138c4c3bfa9f0c445ab455d6"


def read_chunks(path: Path) -> list[dict[str, Any]]:
    chunks: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            chunk = json.loads(line)
            if not str(chunk.get("chunk_id", "")).strip():
                raise ValueError(f"Line {line_number}: missing chunk_id")
            if not isinstance(chunk.get("retrieval_text"), str) or not chunk["retrieval_text"]:
                raise ValueError(f"Line {line_number}: missing retrieval_text")
            chunks.append(chunk)
    if not chunks:
        raise ValueError(f"Empty corpus: {path}")
    return chunks


def select_device() -> str:
    import torch
    return "cuda" if torch.cuda.is_available() else "cpu"


def load_model(model_id: str, revision: str | None, device: str):
    from transformers import AutoModel
    model = AutoModel.from_pretrained(
        model_id,
        revision=revision,
        trust_remote_code=True,
    )
    model.to(device)
    model.eval()
    return model


def encode(model: Any, texts: list[str], task: str, batch_size: int) -> np.ndarray:
    vectors = model.encode(
        texts,
        task=task,
        batch_size=batch_size,
        truncate_dim=EXPECTED_DIMENSION,
    )
    vectors = np.asarray(vectors, dtype=np.float32)
    if vectors.ndim == 1:
        vectors = vectors.reshape(1, -1)
    norms = np.linalg.norm(vectors, axis=1, keepdims=True)
    if np.any(norms == 0) or not np.isfinite(vectors).all():
        raise ValueError("Embedding contains a zero norm, NaN, or Inf")
    vectors /= norms
    if not np.isfinite(vectors).all():
        raise ValueError("Normalized embedding contains NaN or Inf")
    return vectors.astype(np.float32, copy=False)


class DenseRetriever:
    def __init__(self, corpus_path: Path = DEFAULT_CORPUS_PATH,
                 index_dir: Path = DEFAULT_INDEX_DIR, batch_size: int | None = None) -> None:
        self.chunks = read_chunks(corpus_path)
        self.embeddings = np.load(index_dir / "embeddings.npy", allow_pickle=False)
        self.chunk_ids = json.loads((index_dir / "chunk_ids.json").read_text(encoding="utf-8"))
        self.manifest = json.loads((index_dir / "index_manifest.json").read_text(encoding="utf-8"))
        corpus_ids = [chunk["chunk_id"] for chunk in self.chunks]
        expected_shape = (len(self.chunks), EXPECTED_DIMENSION)
        if self.embeddings.shape != expected_shape:
            raise ValueError(f"Index shape {self.embeddings.shape}, expected {expected_shape}")
        if self.embeddings.dtype != np.float32 or not np.isfinite(self.embeddings).all():
            raise ValueError("Index must contain finite float32 values")
        if self.chunk_ids != corpus_ids:
            raise ValueError("chunk_ids.json ordering does not match corpus ordering")
        if not np.allclose(np.linalg.norm(self.embeddings, axis=1), 1.0, atol=1e-5):
            raise ValueError("Index vectors are not L2-normalized")
        if self.manifest.get("query_task") != QUERY_TASK or not self.manifest.get("normalized"):
            raise ValueError("Index manifest retrieval configuration is incompatible")
        self.device = select_device()
        self.batch_size = batch_size or (32 if self.device == "cuda" else 4)
        self.model = load_model(
            self.manifest["model_id"], self.manifest.get("resolved_model_revision"), self.device
        )

    def search(self, query: str, top_k: int = 5) -> list[dict[str, Any]]:
        if not query.strip():
            return []
        query_vector = encode(self.model, [query], QUERY_TASK, self.batch_size)[0]
        scores = self.embeddings @ query_vector
        indices = np.argsort(-scores, kind="stable")[:min(top_k, len(scores))]
        return [{"rank": rank, "score": float(scores[index]), "chunk": self.chunks[index]}
                for rank, index in enumerate(indices, 1)]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def build_dense_index(
    corpus_path: Path = DEFAULT_CORPUS_PATH,
    output_dir: Path = DEFAULT_INDEX_DIR,
    *,
    model_id: str = MODEL_ID,
    revision: str = DENSE_MODEL_REVISION,
    batch_size: int | None = None,
) -> dict[str, Any]:
    """Build the legacy dense index at an explicit location."""
    chunks = read_chunks(corpus_path)
    if len(chunks) != EXPECTED_COUNT:
        raise ValueError(f"Expected {EXPECTED_COUNT} chunks, found {len(chunks)}")
    chunk_ids = [str(chunk["chunk_id"]) for chunk in chunks]
    if len(set(chunk_ids)) != len(chunk_ids):
        raise ValueError("Duplicate chunk_id in corpus")

    device = select_device()
    resolved_batch_size = batch_size or (32 if device == "cuda" else 4)
    model = load_model(model_id, revision, device)
    embeddings = encode(
        model,
        [str(chunk["retrieval_text"]) for chunk in chunks],
        PASSAGE_TASK,
        resolved_batch_size,
    )
    if embeddings.shape != (EXPECTED_COUNT, EXPECTED_DIMENSION):
        raise ValueError(f"Unexpected embedding shape: {embeddings.shape}")

    output_dir.mkdir(parents=True, exist_ok=True)
    np.save(output_dir / "embeddings.npy", embeddings, allow_pickle=False)
    (output_dir / "chunk_ids.json").write_text(
        json.dumps(chunk_ids, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    try:
        corpus_label = str(corpus_path.relative_to(PROJECT_ROOT))
    except ValueError:
        corpus_label = str(corpus_path)
    manifest = {
        "retriever_name": RETRIEVER_NAME,
        "model_id": model_id,
        "resolved_model_revision": revision,
        "trust_remote_code": True,
        "embedding_dimension": EXPECTED_DIMENSION,
        "corpus_version": "corpus-v0.1",
        "corpus_path": corpus_label,
        "corpus_chunk_count": len(chunks),
        "input_field": "retrieval_text",
        "passage_task": PASSAGE_TASK,
        "query_task": QUERY_TASK,
        "similarity": "cosine (normalized dot product)",
        "normalized": True,
        "dtype": "float32",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "chunks_file_sha256": sha256(corpus_path),
        "device_used": device,
        "batch_size": resolved_batch_size,
    }
    (output_dir / "index_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return manifest
