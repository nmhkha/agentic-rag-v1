from __future__ import annotations

import pytest

from legal_rag.evaluation.metrics import (
    aggregate_generation,
    generation_query_metrics,
)


def record(required, supported, cited, *, claims=1, grounded=1, unsupported=0,
           cited_claims=1, correct=1, valid=True):
    return {
        "query_id": "q",
        "required_point_ids": required,
        "supported_point_ids": supported,
        "citation_supported_point_ids": cited,
        "judge_claim_count": claims,
        "judge_grounded_claim_count": grounded,
        "judge_unsupported_claim_count": unsupported,
        "judge_cited_claim_count": cited_claims,
        "judge_correctly_cited_claim_count": correct,
        "citation_valid": valid,
        "generation_error": None,
        "evaluation_error": None,
    }


@pytest.mark.parametrize(
    ("supported", "expected"), [(["p1", "p2"], 1.0), (["p1"], 0.5), ([], 0.0)]
)
def test_answer_completeness_all_partial_zero(supported, expected) -> None:
    row = generation_query_metrics(record(["p1", "p2"], supported, []))
    assert row["answer_completeness"] == expected


def test_valid_wrong_and_missing_citation() -> None:
    valid = generation_query_metrics(record(["p"], ["p"], ["p"]))
    wrong = generation_query_metrics(
        record(["p"], ["p"], [], cited_claims=1, correct=0, valid=True)
    )
    missing = generation_query_metrics(
        record(["p"], ["p"], [], cited_claims=0, correct=0, valid=False)
    )
    assert valid["citation_completeness"] == 1
    assert wrong["citation_correctness"] == 0
    assert missing["citation_correctness"] is None
    assert missing["citation_valid"] is False


def test_unsupported_claim_metrics() -> None:
    row = generation_query_metrics(
        record(["p"], ["p"], ["p"], claims=3, grounded=2, unsupported=1)
    )
    assert row["groundedness"] == pytest.approx(2 / 3)
    assert row["unsupported_claim_rate"] == pytest.approx(1 / 3)


def test_zero_claim_is_none_and_excluded_from_macro() -> None:
    zero = record(["p"], ["p"], ["p"], claims=0, grounded=0, unsupported=0,
                  cited_claims=0, correct=0)
    scored = generation_query_metrics(zero)
    assert scored["groundedness"] is None
    metrics = aggregate_generation([zero])
    assert metrics["groundedness"]["macro"] is None
    assert metrics["groundedness"]["pooled"] is None


def test_macro_micro_and_pooled_remain_distinct() -> None:
    first = record(["a"], ["a"], ["a"], claims=1, grounded=1, unsupported=0)
    second = record(
        ["a", "b", "c"], [], [], claims=3, grounded=1, unsupported=2,
        cited_claims=3, correct=1,
    )
    metrics = aggregate_generation([first, second])
    assert metrics["answer_completeness"]["macro"] == 0.5
    assert metrics["answer_completeness"]["micro"] == 0.25
    assert metrics["groundedness"]["macro"] == pytest.approx(2 / 3)
    assert metrics["groundedness"]["pooled"] == 0.5
    assert metrics["unsupported_claim_rate"]["pooled"] == 0.5
