"""High-level orchestration for online execution or pure offline scoring."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Callable, Mapping, Sequence

from .metrics import (
    agentic_usage_metrics,
    aggregate_generation,
    aggregate_retrieval,
    retrieval_query_metrics,
)
from .pipelines import get_pipeline, load_records
from .reporting import write_outputs


def _load_eval_set(path: Path | None) -> list[dict[str, Any]]:
    if path is None:
        return []
    if path.suffix.lower() == ".jsonl":
        return [
            json.loads(line)
            for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
    payload = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(payload, list):
        return payload
    if isinstance(payload.get("items"), list):
        return payload["items"]
    raise ValueError(f"evaluation set has no items array: {path}")


def _article_from_chunk_id(chunk_id: str) -> str:
    marker = "_dieu-"
    if marker not in chunk_id:
        raise ValueError(f"cannot derive article ID from chunk ID: {chunk_id}")
    document, rest = chunk_id.split(marker, 1)
    article = rest.split("_", 1)[0]
    return f"{document}{marker}{article}"


def _score_raw_retrieval(
    records: Sequence[Mapping[str, Any]], eval_items: Sequence[Mapping[str, Any]]
) -> list[dict[str, Any]]:
    gold_by_id = {str(item["query_id"]): item for item in eval_items}
    if not gold_by_id:
        raise ValueError("raw rankings require --eval-set with gold labels")
    output: list[dict[str, Any]] = []
    for record in records:
        query_id = str(record["query_id"])
        if query_id not in gold_by_id:
            raise ValueError(f"result query is absent from evaluation set: {query_id}")
        gold = gold_by_id[query_id]
        chunks = list(record.get("retrieved_chunk_ids", record.get("ranking", [])))
        articles = list(record.get("retrieved_article_ids", []))
        if not articles:
            articles = [_article_from_chunk_id(chunk_id) for chunk_id in chunks]
        scores = retrieval_query_metrics(
            gold_chunk_ids=gold["gold_chunk_ids"],
            gold_article_ids=gold["gold_article_ids"],
            retrieved_chunk_ids=chunks,
            retrieved_article_ids=articles,
        )
        output.append({
            "query_id": query_id,
            "query": record.get("query", gold.get("query", "")),
            "query_type": gold.get("query_type", ""),
            "difficulty": gold.get("difficulty", ""),
            **scores,
        })
    return output


def _retrieval_rows(
    records: list[dict[str, Any]], eval_items: Sequence[Mapping[str, Any]]
) -> list[dict[str, Any]]:
    required = {
        "hit_at_1", "hit_at_3", "hit_at_5", "recall_at_5", "recall_at_10",
        "reciprocal_rank", "article_hit_at_1", "article_hit_at_3",
        "article_hit_at_5", "article_reciprocal_rank",
    }
    if records and required.issubset(records[0]):
        return records
    return _score_raw_retrieval(records, eval_items)


def run_evaluation(
    *,
    pipeline: str,
    eval_set: Path | None = None,
    results: Path | None = None,
    output_dir: Path | None = None,
    score_only: bool = False,
    executor: Callable[[str], Mapping[str, Any]] | None = None,
) -> dict[str, Any]:
    """Run or score a registered system.

    In score-only mode no executor is accepted or called. In execution mode the
    external adapter receives only query text, never the evaluation gold.
    """
    adapter = get_pipeline(pipeline)
    eval_items = _load_eval_set(eval_set)
    if score_only:
        if results is None:
            raise ValueError("score-only mode requires a stored --results artifact")
        if executor is not None:
            raise ValueError("score-only mode does not accept an executor")
        source_records = load_records(results)
    else:
        if executor is None:
            raise ValueError("execution mode requires a pipeline executor")
        if not eval_items:
            raise ValueError("execution mode requires an evaluation set")
        source_records = []
        for item in eval_items:
            result = dict(executor(str(item["query"])))
            result.setdefault("query_id", item["query_id"])
            source_records.append(result)

    records = adapter.normalize(source_records)
    if adapter.kind == "retrieval":
        per_query = _retrieval_rows(records, eval_items)
        metrics = aggregate_retrieval(per_query)
    else:
        benchmark = "agentic-rag-eval-v1" if pipeline == "agentic-v1" else "standard-rag-eval-v0"
        metrics = aggregate_generation(
            records,
            benchmark_version=benchmark,
            point_scope="judged" if pipeline == "agentic-v1" else "all",
        )
        if pipeline == "agentic-v1":
            metrics["agentic_usage"] = agentic_usage_metrics(records)
        per_query = metrics.pop("per_query")

    paths: dict[str, Path] = {}
    if output_dir is not None:
        paths = write_outputs(
            output_dir,
            pipeline=pipeline,
            kind=adapter.kind,
            metrics=metrics,
            per_query=per_query,
        )
    return {
        "pipeline": pipeline,
        "kind": adapter.kind,
        "score_only": score_only,
        "metrics": metrics,
        "per_query": per_query,
        "outputs": paths,
    }
