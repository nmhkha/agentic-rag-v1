from __future__ import annotations

import pytest

from legal_rag.evaluation.metrics import (
    aggregate_retrieval,
    retrieval_query_metrics,
)


def score(chunks, articles, gold_chunks=("g",), gold_articles=("ga",)):
    return retrieval_query_metrics(
        gold_chunk_ids=gold_chunks,
        gold_article_ids=gold_articles,
        retrieved_chunk_ids=chunks,
        retrieved_article_ids=articles,
    )


def test_no_gold_retrieved_is_zero() -> None:
    row = score(["x", "y"], ["xa", "ya"])
    assert row["hit_at_5"] == 0
    assert row["recall_at_10"] == 0
    assert row["reciprocal_rank"] == 0


def test_one_gold_and_one_based_rank() -> None:
    row = score(["x", "g"], ["xa", "ga"])
    assert row["first_gold_chunk_rank"] == 2
    assert row["hit_at_1"] == 0
    assert row["hit_at_3"] == 1
    assert row["reciprocal_rank"] == 0.5


def test_multiple_gold_recall_uses_gold_denominator() -> None:
    row = score(
        ["g1", "x", "g2"], ["ga", "xa", "ga"],
        gold_chunks=("g1", "g2", "g3"), gold_articles=("ga",),
    )
    assert row["recall_at_5"] == pytest.approx(2 / 3)


def test_duplicate_chunk_does_not_inflate_recall() -> None:
    row = score(
        ["g1", "g1", "x"], ["ga", "ga", "xa"],
        gold_chunks=("g1", "g2"), gold_articles=("ga",),
    )
    assert row["recall_at_5"] == 0.5


def test_fewer_than_k_and_rank_boundary() -> None:
    at_five = score(["a", "b", "c", "d", "g"], ["x"] * 4 + ["ga"])
    after_five = score(["a", "b", "c", "d", "e", "g"], ["x"] * 5 + ["ga"])
    assert at_five["hit_at_5"] == 1
    assert after_five["hit_at_5"] == 0
    assert after_five["recall_at_10"] == 1


def test_article_ranking_is_deduplicated_but_chunk_ranking_is_not() -> None:
    row = score(["x1", "x2", "g"], ["xa", "xa", "ga"])
    assert row["first_gold_chunk_rank"] == 3
    assert row["first_gold_article_rank"] == 2


def test_empty_gold_is_rejected_like_verified_loader() -> None:
    with pytest.raises(ValueError):
        score([], [], gold_chunks=(), gold_articles=())


def test_aggregate_is_macro_query_average() -> None:
    rows = [score(["g"], ["ga"]), score([], [])]
    result = aggregate_retrieval(rows)
    assert result["query_count"] == 2
    assert result["chunk_level"]["hit_at_1"] == 0.5
    assert result["chunk_level"]["recall_at_5"] == 0.5
