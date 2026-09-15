#!/usr/bin/env python3
"""Deterministically validate generation-evaluation annotations."""

from __future__ import annotations

import hashlib
import json
import argparse
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from legal_rag.evaluation.validation import validate_generation_dataset

DEFAULT_DATASET = ROOT / "eval-sets/generation/generation_eval_v1_verified.json"
DEFAULT_RETRIEVAL_EVAL = ROOT / "eval-sets/retrieval/retrieval_eval.jsonl"
DEFAULT_CORPUS = ROOT / "data/versions/corpus-v0.1/chunks.jsonl"
ANSWERABILITY = {"answerable", "insufficient_evidence"}
IMPORTANCE = {"required", "important"}
STATUSES = {"template", "draft", "verified"}
CONFIDENCE = {"high", "medium", "low"}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def validate(dataset_path: Path = DEFAULT_DATASET, retrieval_path: Path = DEFAULT_RETRIEVAL_EVAL,
             corpus_path: Path = DEFAULT_CORPUS) -> list[str]:
    errors: list[str] = []
    try:
        data = json.loads(dataset_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"Cannot parse generation dataset: {exc}"]
    version = data.get("evaluation_version")
    if version not in {"generation-eval-v0", "generation-eval-v1"}:
        errors.append("invalid or missing evaluation_version")
    if data.get("dataset_status") not in {"template", "draft", "verified"}:
        errors.append("invalid or missing dataset_status")
    items = data.get("items")
    if not isinstance(items, list):
        return errors + ["items must be a list"]
    errors.extend(validate_generation_dataset(data))
    try:
        retrieval_items = load_jsonl(retrieval_path)
        corpus_chunks = {row["chunk_id"] for row in load_jsonl(corpus_path)}
    except (OSError, json.JSONDecodeError, KeyError) as exc:
        return errors + [f"Cannot load source artifacts: {exc}"]
    retrieval_by_id = {row["query_id"]: row for row in retrieval_items}
    if data.get("source_retrieval_eval_sha256") != sha256(retrieval_path):
        errors.append("source_retrieval_eval_sha256 does not match frozen retrieval benchmark")
    seen: set[str] = set()
    if version == "generation-eval-v1":
        if len(items) != 31:
            errors.append("v1 must contain exactly 31 queries")
        if data.get("dataset_status") not in {"draft", "verified"}:
            errors.append("v1 dataset_status must be draft or verified")

    for index, item in enumerate(items, 1):
        if not isinstance(item, dict):
            continue
        prefix = f"item {index} ({item.get('query_id', '<missing>')})"
        qid = item.get("query_id")
        if isinstance(qid, str) and qid.strip(): seen.add(qid)
        benchmark = retrieval_by_id.get(qid)
        if not benchmark: errors.append(f"{prefix}: query_id is absent from retrieval benchmark")
        elif item.get("query") != benchmark["query"]: errors.append(f"{prefix}: query differs from frozen retrieval benchmark")
        if item.get("split") != "eval": errors.append(f"{prefix}: split must be eval")
        if item.get("answerability") not in ANSWERABILITY: errors.append(f"{prefix}: invalid answerability")
        status = item.get("annotation_status")
        if status not in STATUSES: errors.append(f"{prefix}: invalid annotation_status")
        if version == "generation-eval-v1" and status != data.get("dataset_status"):
            errors.append(f"{prefix}: annotation_status must match v1 dataset_status")
        points = item.get("required_points")
        if not isinstance(points, list): continue
        if not isinstance(item.get("reference_answer"), str): errors.append(f"{prefix}: reference_answer must be a string")
        if version == "generation-eval-v1" and item.get("answerability") == "answerable" and not item.get("reference_answer", "").strip():
            errors.append(f"{prefix}: answerable records require a non-empty reference_answer")
        if not str(item.get("annotation_notes", "")).strip(): errors.append(f"{prefix}: annotation_notes is empty")
        if item.get("annotation_confidence") not in CONFIDENCE:
            errors.append(f"{prefix}: invalid or missing annotation_confidence")
        if status == "template" and (points or item.get("reference_answer", "").strip()):
            errors.append(f"{prefix}: template records must not contain annotation content")
        if status == "verified" and (not points or not item.get("reference_answer", "").strip()):
            errors.append(f"{prefix}: verified records require points and a reference answer")
        gold = set(benchmark.get("gold_chunk_ids", [])) if benchmark else set()
        for point_index, point in enumerate(points, 1):
            point_prefix = f"{prefix} point {point_index}"
            if not isinstance(point, dict): continue
            if not str(point.get("description", "")).strip(): errors.append(f"{point_prefix}: description is empty")
            if point.get("importance") not in IMPORTANCE: errors.append(f"{point_prefix}: invalid importance")
            support = point.get("supporting_chunk_ids")
            if not isinstance(support, list) or not support: continue
            for chunk_id in support:
                if chunk_id not in corpus_chunks: errors.append(f"{point_prefix}: nonexistent corpus chunk {chunk_id}")
                elif chunk_id not in gold: errors.append(f"{point_prefix}: supporting chunk is not retrieval gold: {chunk_id}")
            variants = point.get("acceptable_variants")
            if variants is not None and (not isinstance(variants, list) or not all(isinstance(x, str) and x.strip() for x in variants)):
                errors.append(f"{point_prefix}: acceptable_variants must be non-empty strings")
    if seen != set(retrieval_by_id):
        errors.append("generation dataset query IDs do not exactly match frozen retrieval benchmark")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", type=Path, default=DEFAULT_DATASET)
    parser.add_argument("--retrieval", type=Path, default=DEFAULT_RETRIEVAL_EVAL)
    parser.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS)
    args = parser.parse_args()
    errors = validate(args.dataset, args.retrieval, args.corpus)
    print(f"Validation errors: {len(errors)}")
    for error in errors: print(f"ERROR: {error}")
    print("Validation: PASSED" if not errors else "Validation: FAILED")
    raise SystemExit(bool(errors))


if __name__ == "__main__":
    main()
