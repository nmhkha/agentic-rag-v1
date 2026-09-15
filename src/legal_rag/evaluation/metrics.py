"""Pure metric definitions shared by retrieval and generation evaluation.

The formulas in this module intentionally follow the historical evaluators.
They do not execute a pipeline and never load evaluation data themselves.
"""

from __future__ import annotations

from collections import Counter
from statistics import mean
from typing import Any, Iterable, Mapping, Sequence


def _mean(values: Sequence[float]) -> float:
    return sum(values) / len(values)


def first_gold_rank(
    ranking: Sequence[str], gold: Iterable[str], limit: int = 10
) -> int | None:
    """Return the historical one-based rank of the first gold item."""
    gold_set = set(gold)
    return next(
        (rank for rank, item in enumerate(ranking[:limit], 1) if item in gold_set),
        None,
    )


def unique_ranking(items: Iterable[str]) -> list[str]:
    """Deduplicate while retaining first occurrence (used for articles only)."""
    seen: set[str] = set()
    output: list[str] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            output.append(item)
    return output


def retrieval_query_metrics(
    *,
    gold_chunk_ids: Iterable[str],
    gold_article_ids: Iterable[str],
    retrieved_chunk_ids: Sequence[str],
    retrieved_article_ids: Sequence[str],
) -> dict[str, float | int | None]:
    """Score one ranking with the exact M0 retrieval definitions.

    Chunk duplicates retain their ranks but cannot increase recall because the
    legacy evaluator used set intersection. Article rankings are deduplicated.
    """
    gold_chunks = set(gold_chunk_ids)
    gold_articles = set(gold_article_ids)
    if not gold_chunks or not gold_articles:
        raise ValueError("retrieval gold chunk and article IDs must be non-empty")
    article_ranking = unique_ranking(retrieved_article_ids)
    chunk_rank = first_gold_rank(retrieved_chunk_ids, gold_chunks)
    article_rank = first_gold_rank(article_ranking, gold_articles)
    found_5 = len(gold_chunks.intersection(retrieved_chunk_ids[:5]))
    found_10 = len(gold_chunks.intersection(retrieved_chunk_ids[:10]))
    return {
        "first_gold_chunk_rank": chunk_rank,
        "first_gold_article_rank": article_rank,
        "hit_at_1": int(chunk_rank == 1),
        "hit_at_3": int(chunk_rank is not None and chunk_rank <= 3),
        "hit_at_5": int(chunk_rank is not None and chunk_rank <= 5),
        "recall_at_5": found_5 / len(gold_chunks),
        "recall_at_10": found_10 / len(gold_chunks),
        "reciprocal_rank": 1 / chunk_rank if chunk_rank else 0.0,
        "article_hit_at_1": int(article_rank == 1),
        "article_hit_at_3": int(article_rank is not None and article_rank <= 3),
        "article_hit_at_5": int(article_rank is not None and article_rank <= 5),
        "article_reciprocal_rank": 1 / article_rank if article_rank else 0.0,
    }


def aggregate_retrieval(rows: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    """Macro-average historical per-query retrieval metrics."""
    if not rows:
        raise ValueError("cannot aggregate an empty retrieval result set")

    def avg(field: str) -> float:
        return sum(float(row[field]) for row in rows) / len(rows)

    return {
        "query_count": len(rows),
        "chunk_level": {
            "hit_at_1": avg("hit_at_1"),
            "hit_at_3": avg("hit_at_3"),
            "hit_at_5": avg("hit_at_5"),
            "recall_at_5": avg("recall_at_5"),
            "recall_at_10": avg("recall_at_10"),
            "mrr_at_10": avg("reciprocal_rank"),
        },
        "article_level": {
            "hit_at_1": avg("article_hit_at_1"),
            "hit_at_3": avg("article_hit_at_3"),
            "hit_at_5": avg("article_hit_at_5"),
            "mrr_at_10": avg("article_reciprocal_rank"),
        },
    }


def coverage_ratio(supported: int, required: int) -> float:
    """Legacy required-point denominator behavior (zero points -> 0.0)."""
    return supported / required if required else 0.0


def optional_ratio(numerator: int, denominator: int) -> float | None:
    """Legacy claim denominator behavior (zero claims -> excluded/None)."""
    return numerator / denominator if denominator else None


def generation_query_metrics(record: Mapping[str, Any]) -> dict[str, Any]:
    """Normalize stored Standard/Agentic judge output into one query score."""
    required = list(record.get("required_point_ids", []))
    supported = list(record.get("supported_point_ids", []))
    cited_supported = list(record.get("citation_supported_point_ids", []))
    judge = record.get("judge") or {}

    def count(standard_key: str, judge_key: str) -> int:
        return int(record.get(standard_key, judge.get(judge_key, 0)) or 0)

    claims = count("judge_claim_count", "claim_count")
    grounded = count("judge_grounded_claim_count", "grounded_claim_count")
    unsupported = count("judge_unsupported_claim_count", "unsupported_claim_count")
    cited_claims = count("judge_cited_claim_count", "cited_claim_count")
    correctly_cited = count(
        "judge_correctly_cited_claim_count", "correctly_cited_claim_count"
    )
    return {
        "query_id": record.get("query_id"),
        "required_point_count": len(required),
        "supported_point_count": len(supported),
        "citation_supported_point_count": len(cited_supported),
        "answer_completeness": coverage_ratio(len(supported), len(required)),
        "citation_completeness": coverage_ratio(len(cited_supported), len(required)),
        "citation_correctness": optional_ratio(correctly_cited, cited_claims),
        "groundedness": optional_ratio(grounded, claims),
        "unsupported_claim_rate": optional_ratio(unsupported, claims),
        "citation_valid": bool(record.get("citation_valid", False)),
        "claim_count": claims,
        "grounded_claim_count": grounded,
        "unsupported_claim_count": unsupported,
        "cited_claim_count": cited_claims,
        "correctly_cited_claim_count": correctly_cited,
        "generation_error": record.get("generation_error"),
        "evaluation_error": record.get("evaluation_error"),
    }


def _summary(
    rows: Sequence[Mapping[str, Any]],
    key: str,
    numerator_key: str,
    denominator_key: str,
) -> dict[str, Any]:
    macro_values = [float(row[key]) for row in rows if row[key] is not None]
    numerator = sum(int(row[numerator_key]) for row in rows)
    denominator = sum(int(row[denominator_key]) for row in rows)
    return {
        "macro": mean(macro_values) if macro_values else None,
        "pooled": optional_ratio(numerator, denominator),
        "numerator": numerator,
        "denominator": denominator,
        "judged_query_count": len(macro_values),
    }


def aggregate_generation(
    records: Sequence[Mapping[str, Any]], *, benchmark_version: str | None = None,
    point_scope: str = "all",
) -> dict[str, Any]:
    """Aggregate shared generation metrics, retaining macro and pooled views."""
    if point_scope not in {"all", "judged"}:
        raise ValueError("point_scope must be 'all' or 'judged'")
    rows = [generation_query_metrics(record) for record in records]
    judged = [
        row
        for row in rows
        if row["generation_error"] is None and row["evaluation_error"] is None
    ]
    # Standard RAG historically assigned failed rows point score 0; Agentic v1
    # historically excluded them. The formulas remain shared, while the
    # evaluator-specific eligibility rule is explicit here.
    point_rows = rows if point_scope == "all" else judged
    required_total = sum(int(row["required_point_count"]) for row in point_rows)
    supported_total = sum(int(row["supported_point_count"]) for row in point_rows)
    citation_supported_total = sum(
        int(row["citation_supported_point_count"]) for row in point_rows
    )
    answer_values = [float(row["answer_completeness"]) for row in point_rows]
    citation_values = [float(row["citation_completeness"]) for row in point_rows]
    valid_count = sum(int(row["citation_valid"]) for row in rows)
    output = {
        "benchmark_version": benchmark_version,
        "query_count": len(rows),
        "completed_query_count": sum(
            row["generation_error"] is None for row in rows
        ),
        "judged_query_count": len(judged),
        "generation_error_count": sum(
            row["generation_error"] is not None for row in rows
        ),
        "evaluation_error_count": sum(
            row["evaluation_error"] is not None for row in rows
        ),
        "required_point_count": required_total,
        "supported_point_count": supported_total,
        "answer_completeness": {
            "macro": mean(answer_values) if answer_values else 0.0,
            "micro": coverage_ratio(supported_total, required_total),
        },
        "citation_completeness": {
            "macro": mean(citation_values) if citation_values else 0.0,
            "micro": coverage_ratio(citation_supported_total, required_total),
            "numerator": citation_supported_total,
            "denominator": required_total,
        },
        "citation_syntax_validity": {
            "valid_count": valid_count,
            "query_count": len(rows),
            "rate": coverage_ratio(valid_count, len(rows)),
        },
        "citation_correctness": _summary(
            judged,
            "citation_correctness",
            "correctly_cited_claim_count",
            "cited_claim_count",
        ),
        "groundedness": _summary(
            judged, "groundedness", "grounded_claim_count", "claim_count"
        ),
        "unsupported_claim_rate": _summary(
            judged,
            "unsupported_claim_rate",
            "unsupported_claim_count",
            "claim_count",
        ),
        "per_query": rows,
    }
    return output


def agentic_usage_metrics(records: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    """Generic summary of controller mechanisms stored in Agentic traces."""
    generated = [row for row in records if row.get("generation_error") is None]
    traces = [row["trace"] for row in generated if isinstance(row.get("trace"), dict)]
    statuses = Counter(str(row.get("status")) for row in records)
    return {
        "average_retrieval_calls": mean(
            [len(trace.get("retrieval_calls", [])) for trace in traces]
        ) if traces else 0.0,
        "average_llm_calls": mean(
            [len(trace.get("llm_calls", [])) for trace in traces]
        ) if traces else 0.0,
        "expansion_rate": mean(
            [bool(trace.get("expansion_used")) for trace in traces]
        ) if traces else 0.0,
        "revision_rate": mean(
            [bool(trace.get("revision_used")) for trace in traces]
        ) if traces else 0.0,
        "citation_revision_rate": mean(
            [bool(trace.get("citation_revision_used")) for trace in traces]
        ) if traces else 0.0,
        "semantic_citation_check_rate": mean(
            [bool((trace.get("citation_check") or {}).get("alignment_checked"))
             for trace in traces]
        ) if traces else 0.0,
        "status_counts": dict(sorted(statuses.items())),
    }
