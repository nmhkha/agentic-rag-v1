from __future__ import annotations

import json

import pytest

from legal_rag.evaluation.runner import run_evaluation


def test_score_only_never_accepts_or_calls_executor(tmp_path) -> None:
    results = tmp_path / "rows.jsonl"
    results.write_text("{}\n", encoding="utf-8")
    with pytest.raises(ValueError, match="does not accept an executor"):
        run_evaluation(
            pipeline="standard-rag", results=results, score_only=True,
            executor=lambda _: (_ for _ in ()).throw(AssertionError("called")),
        )


def test_score_only_requires_results() -> None:
    with pytest.raises(ValueError, match="requires a stored"):
        run_evaluation(pipeline="bm25", score_only=True)


def test_raw_retrieval_results_are_joined_with_gold_after_execution(tmp_path) -> None:
    evaluation = tmp_path / "eval.jsonl"
    evaluation.write_text(json.dumps({
        "query_id": "q1", "query": "secret gold query", "gold_chunk_ids": ["d_dieu-1_khoan-1"],
        "gold_article_ids": ["d_dieu-1"], "query_type": "x", "difficulty": "easy",
    }) + "\n", encoding="utf-8")
    seen = []
    run = run_evaluation(
        pipeline="bm25", eval_set=evaluation,
        executor=lambda query: seen.append(query) or {"ranking": ["d_dieu-1_khoan-1"]},
    )
    assert seen == ["secret gold query"]
    assert run["metrics"]["chunk_level"]["hit_at_1"] == 1


def test_score_only_writes_only_requested_temp_outputs(tmp_path) -> None:
    results = tmp_path / "generation.jsonl"
    results.write_text(json.dumps({
        "query_id": "q", "required_point_ids": ["p"], "supported_point_ids": ["p"],
        "citation_supported_point_ids": ["p"], "citation_valid": True,
        "judge_claim_count": 1, "judge_grounded_claim_count": 1,
        "judge_unsupported_claim_count": 0, "judge_cited_claim_count": 1,
        "judge_correctly_cited_claim_count": 1, "generation_error": None,
        "evaluation_error": None,
    }) + "\n", encoding="utf-8")
    output = tmp_path / "out"
    run = run_evaluation(
        pipeline="standard-rag", results=results, score_only=True, output_dir=output
    )
    assert set(run["outputs"]) == {"metrics", "per_query", "report"}
    assert all(path.exists() for path in run["outputs"].values())
