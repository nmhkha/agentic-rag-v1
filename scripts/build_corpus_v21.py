#!/usr/bin/env python3
"""Build corpus-v2.1 (with Vertical Overlap in retrieval_text) and its Sparse & Dense indexes.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from legal_rag.retrieval.reranker import contextual_passage
from legal_rag.retrieval.sparse import (
    BM25_B,
    BM25_EPSILON,
    BM25_K1,
    RETRIEVER_NAME as SPARSE_RETRIEVER_NAME,
    build_sparse_index,
    read_chunks,
)

V02_DIR = ROOT / "data/versions/corpus-v0.2"
V21_DIR = ROOT / "data/versions/corpus-v2.1"
V02_INDEX_DIR = ROOT / "experiments/indexes/corpus-v0.2"
V21_INDEX_DIR = ROOT / "experiments/indexes/corpus-v2.1"

CORPUS_VERSION = "corpus-v2.1"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_path(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def canonical_hash(value: Any) -> str:
    encoded = json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return sha256_bytes(encoded)


def build_corpus_v21() -> tuple[list[dict[str, Any]], str, str]:
    print("1. Reading frozen corpus-v0.2 chunks (read-only)...", flush=True)
    v02_chunks_path = V02_DIR / "chunks/chunks.jsonl"
    v02_manifest = json.loads((V02_DIR / "corpus_manifest.json").read_text(encoding="utf-8"))
    raw_chunks = [
        json.loads(line)
        for line in v02_chunks_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]

    v21_chunks: list[dict[str, Any]] = []
    by_doc: dict[str, list[dict[str, Any]]] = defaultdict(list)
    enriched_count = 0

    for row in raw_chunks:
        new_row = dict(row)
        new_row["corpus_version"] = CORPUS_VERSION
        old_rt = str(row["retrieval_text"])
        new_rt = contextual_passage(row)
        if new_rt != old_rt:
            enriched_count += 1
        new_row["retrieval_text"] = new_rt
        v21_chunks.append(new_row)
        by_doc[str(new_row["document_id"])].append(new_row)

    print(
        f"   Processed {len(v21_chunks)} chunks ({enriched_count} chunks enriched with Vertical Overlap).",
        flush=True,
    )

    chunks_dir = V21_DIR / "chunks"
    by_doc_dir = chunks_dir / "by_document"
    by_doc_dir.mkdir(parents=True, exist_ok=True)

    per_doc_sha: dict[str, str] = {}
    for doc_id, doc_rows in sorted(by_doc.items()):
        payload = "".join(
            json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in doc_rows
        ).encode("utf-8")
        doc_path = by_doc_dir / f"{doc_id}.jsonl"
        doc_path.write_bytes(payload)
        per_doc_sha[doc_id] = sha256_bytes(payload)

    combined_payload = "".join(
        json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in v21_chunks
    ).encode("utf-8")
    combined_path = chunks_dir / "chunks.jsonl"
    combined_path.write_bytes(combined_payload)
    chunks_sha = sha256_bytes(combined_payload)

    manifest = dict(v02_manifest)
    manifest["corpus_version"] = CORPUS_VERSION
    manifest["parent_corpus_version"] = "corpus-v0.2"
    manifest["parent_chunks_sha256"] = v02_manifest["chunks_sha256"]
    manifest["vertical_overlap_enabled"] = True
    manifest["vertical_overlap_enriched_chunks"] = enriched_count
    manifest["chunks_sha256"] = chunks_sha
    manifest["per_document_chunk_sha256"] = per_doc_sha
    manifest.pop("corpus_fingerprint_sha256", None)
    fingerprint = canonical_hash(manifest)
    manifest["corpus_fingerprint_sha256"] = fingerprint

    manifest_path = V21_DIR / "corpus_manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"   Saved {combined_path} (sha256={chunks_sha[:16]}...)", flush=True)
    print(f"   Saved {manifest_path} (fingerprint={fingerprint[:16]}...)", flush=True)
    return v21_chunks, chunks_sha, fingerprint


def build_sparse_v21(chunks: list[dict[str, Any]], chunks_sha: str, fingerprint: str) -> None:
    print("2. Building sparse index for corpus-v2.1...", flush=True)
    sparse_dir = V21_INDEX_DIR / "sparse"
    manifest_dir = V21_INDEX_DIR / "manifests"
    sparse_dir.mkdir(parents=True, exist_ok=True)
    manifest_dir.mkdir(parents=True, exist_ok=True)

    mapping_path = manifest_dir / "chunk_mapping.jsonl"
    mapping_rows = [
        json.dumps(
            {
                "row_index": idx,
                "chunk_id": str(c["chunk_id"]),
                "article_id": str(c["article_id"]),
                "source_uid": str(c["source_uid"]),
                "document_id": str(c["document_id"]),
            },
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        for idx, c in enumerate(chunks)
    ]
    mapping_path.write_text("\n".join(mapping_rows) + "\n", encoding="utf-8")
    mapping_hash = sha256_path(mapping_path)

    sparse_index_path = sparse_dir / "sparse_index.json"
    stats = build_sparse_index(chunks, sparse_index_path)

    sparse_manifest = {
        "index_id": f"{SPARSE_RETRIEVER_NAME}-corpus-v2.1",
        "index_type": "sparse",
        "index_version": "1",
        "corpus_version": CORPUS_VERSION,
        "corpus_fingerprint_sha256": fingerprint,
        "chunks_sha256": chunks_sha,
        "retrieval_method": SPARSE_RETRIEVER_NAME,
        "effective_parameters": {"b": BM25_B, "epsilon": BM25_EPSILON, "k1": BM25_K1},
        "input_field": "retrieval_text",
        "chunk_mapping_sha256": mapping_hash,
        "index_artifact_sha256": stats["artifact_sha256"],
        "chunk_count": len(chunks),
        "indexed_documents": stats["document_count"],
        "unique_indexed_chunk_ids": stats["unique_chunk_ids"],
        "vocabulary_size": stats["vocabulary_size"],
    }
    sparse_fp = canonical_hash(sparse_manifest)
    sparse_manifest["index_fingerprint_sha256"] = sparse_fp
    (manifest_dir / "sparse_manifest.json").write_text(
        json.dumps(sparse_manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (sparse_dir / "fingerprint.sha256").write_text(sparse_fp + "\n", encoding="ascii")
    print(
        f"   Sparse index built: {stats['document_count']} chunks, vocab={stats['vocabulary_size']}",
        flush=True,
    )


def build_dense_v21(
    chunks: list[dict[str, Any]],
    chunks_sha: str,
    fingerprint: str,
    *,
    fast_reuse: bool = False,
) -> None:
    print("3. Building dense index (jinaai/jina-embeddings-v3) for corpus-v2.1...", flush=True)
    import shutil
    from legal_rag.retrieval.dense import (
        DENSE_MODEL_REVISION,
        EXPECTED_DIMENSION,
        MODEL_ID,
        PASSAGE_TASK,
        QUERY_TASK,
    )

    dense_dir = V21_INDEX_DIR / "dense"
    manifest_dir = V21_INDEX_DIR / "manifests"
    dense_dir.mkdir(parents=True, exist_ok=True)
    manifest_dir.mkdir(parents=True, exist_ok=True)

    embeddings_path = dense_dir / "embeddings.npy"
    chunk_ids_path = dense_dir / "chunk_ids.json"
    index_manifest_path = dense_dir / "index_manifest.json"

    if fast_reuse:
        shutil.copy2(V02_INDEX_DIR / "dense/embeddings.npy", embeddings_path)
        print(f"   Copied {len(chunks)} dense vectors to {embeddings_path}", flush=True)
    else:
        import numpy as np
        from legal_rag.retrieval.dense import encode, load_model, select_device

        os.environ["HF_HUB_OFFLINE"] = "1"
        os.environ["TRANSFORMERS_OFFLINE"] = "1"

        v02_chunks = read_chunks(V02_DIR / "chunks/chunks.jsonl")
        v02_embeddings = np.load(V02_INDEX_DIR / "dense/embeddings.npy", allow_pickle=False)

        changed_indices: list[int] = []
        changed_texts: list[str] = []
        embeddings = np.array(v02_embeddings, dtype=np.float32, copy=True)

        for idx, (old_c, new_c) in enumerate(zip(v02_chunks, chunks)):
            if old_c["chunk_id"] != new_c["chunk_id"]:
                raise RuntimeError(f"Chunk alignment mismatch at row {idx}")
            if old_c["retrieval_text"] != new_c["retrieval_text"]:
                changed_indices.append(idx)
                changed_texts.append(str(new_c["retrieval_text"]))

        print(
            f"   Reusing {len(chunks) - len(changed_indices)} unchanged vectors from corpus-v0.2; "
            f"encoding {len(changed_indices)} Vertical-Overlap enriched chunks...",
            flush=True,
        )
        t0 = time.time()
        device = select_device()
        batch_size = 16 if device == "cuda" else 8
        print(f"   Loading {MODEL_ID} on {device}...", flush=True)
        model = load_model(MODEL_ID, DENSE_MODEL_REVISION, device)
        print(f"   Model ready. Encoding {len(changed_indices)} chunks in batches...", flush=True)

        step = 200
        for start_idx in range(0, len(changed_texts), step):
            end_idx = min(start_idx + step, len(changed_texts))
            sub_texts = changed_texts[start_idx:end_idx]
            sub_vecs = encode(model, sub_texts, PASSAGE_TASK, batch_size)
            for j, v in enumerate(sub_vecs):
                embeddings[changed_indices[start_idx + j]] = v
            elapsed = time.time() - t0
            pct = (end_idx / len(changed_texts)) * 100
            print(f"   [{end_idx:4d}/{len(changed_texts)}] ({pct:5.1f}%) encoded in {elapsed:.1f}s", flush=True)

        np.save(embeddings_path, embeddings, allow_pickle=False)
        print(f"   Finished encoding {len(changed_indices)} chunks on {device} in {time.time() - t0:.2f}s", flush=True)

    resolved_rev = DENSE_MODEL_REVISION
    chunk_ids = [str(c["chunk_id"]) for c in chunks]
    chunk_ids_path.write_text(
        json.dumps(chunk_ids, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    index_manifest = {
        "retriever_name": "dense-jina-v3-v0",
        "model_id": MODEL_ID,
        "requested_model_revision": DENSE_MODEL_REVISION,
        "resolved_model_revision": resolved_rev,
        "corpus_path": "data/versions/corpus-v2.1/chunks/chunks.jsonl",
        "corpus_version": CORPUS_VERSION,
        "corpus_sha256": chunks_sha,
        "corpus_fingerprint_sha256": fingerprint,
        "input_field": "retrieval_text",
        "passage_task": PASSAGE_TASK,
        "query_task": QUERY_TASK,
        "dimension": EXPECTED_DIMENSION,
        "dtype": "float32",
        "normalized": True,
        "count": len(chunks),
        "embeddings_sha256": sha256_path(embeddings_path),
        "chunk_ids_sha256": sha256_path(chunk_ids_path),
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    index_manifest_path.write_text(
        json.dumps(index_manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (manifest_dir / "dense_manifest.json").write_text(
        json.dumps(index_manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"   Saved dense index to {dense_dir}", flush=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip-dense", action="store_true")
    parser.add_argument("--fast-dense", action="store_true")
    args = parser.parse_args()

    chunks, chunks_sha, fingerprint = build_corpus_v21()
    build_sparse_v21(chunks, chunks_sha, fingerprint)
    if not args.skip_dense:
        build_dense_v21(chunks, chunks_sha, fingerprint, fast_reuse=args.fast_dense)


if __name__ == "__main__":
    main()
