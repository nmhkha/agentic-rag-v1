"""Evaluation adapters and registry; no retrieval/generation algorithms live here."""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Iterable, Mapping


RETRIEVAL_NUMERIC_FIELDS = {
    "hit_at_1", "hit_at_3", "hit_at_5", "recall_at_5", "recall_at_10",
    "reciprocal_rank", "article_hit_at_1", "article_hit_at_3",
    "article_hit_at_5", "article_reciprocal_rank",
}


@dataclass(frozen=True)
class PipelineAdapter:
    name: str
    kind: str
    normalizer: Callable[[Iterable[Mapping[str, Any]]], list[dict[str, Any]]]

    def normalize(self, records: Iterable[Mapping[str, Any]]) -> list[dict[str, Any]]:
        return self.normalizer(records)


def normalize_retrieval_records(
    records: Iterable[Mapping[str, Any]],
) -> list[dict[str, Any]]:
    output: list[dict[str, Any]] = []
    for source in records:
        row = dict(source)
        for field in RETRIEVAL_NUMERIC_FIELDS:
            if field in row and row[field] not in (None, ""):
                row[field] = float(row[field])
        output.append(row)
    return output


def normalize_generation_records(
    records: Iterable[Mapping[str, Any]],
) -> list[dict[str, Any]]:
    return [dict(record) for record in records]


PIPELINES: dict[str, PipelineAdapter] = {
    name: PipelineAdapter(name, "retrieval", normalize_retrieval_records)
    for name in ("bm25", "dense", "hybrid-rrf", "reranker")
}
PIPELINES.update({
    name: PipelineAdapter(name, "generation", normalize_generation_records)
    for name in ("standard-rag", "agentic-v1")
})


def get_pipeline(name: str) -> PipelineAdapter:
    try:
        return PIPELINES[name]
    except KeyError as exc:
        raise ValueError(
            f"unknown pipeline {name!r}; choose one of {', '.join(PIPELINES)}"
        ) from exc


def load_records(path: Path) -> list[dict[str, Any]]:
    """Load a CSV, JSONL, or JSON stored-output artifact."""
    suffix = path.suffix.lower()
    if suffix == ".csv":
        with path.open(encoding="utf-8", newline="") as handle:
            return [dict(row) for row in csv.DictReader(handle)]
    if suffix == ".jsonl":
        return [
            json.loads(line)
            for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
    if suffix == ".json":
        payload = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(payload, list):
            return [dict(row) for row in payload]
        for key in ("results", "records", "items"):
            if isinstance(payload.get(key), list):
                return [dict(row) for row in payload[key]]
        raise ValueError(f"JSON result artifact has no records array: {path}")
    raise ValueError(f"unsupported result format: {path}")
