from __future__ import annotations

from legal_rag.evaluation.reporting import render_report, write_outputs


def generation_metrics():
    ratio = {"macro": 0.75, "pooled": 0.5, "numerator": 1, "denominator": 2}
    return {
        "query_count": 1,
        "answer_completeness": {"macro": 1.0, "micro": 0.5},
        "citation_completeness": {"macro": 1.0, "micro": 0.5},
        "citation_correctness": ratio,
        "groundedness": ratio,
        "unsupported_claim_rate": ratio,
        "citation_syntax_validity": {"valid_count": 1, "query_count": 1},
    }


def test_report_explicitly_labels_macro_and_pooled() -> None:
    report = render_report("agentic-v1", "generation", generation_metrics())
    assert "Groundedness macro" in report
    assert "Groundedness pooled" in report
    assert "Micro/pooled" in report


def test_writers_create_three_generic_outputs(tmp_path) -> None:
    paths = write_outputs(
        tmp_path, pipeline="agentic-v1", kind="generation",
        metrics=generation_metrics(), per_query=[{"query_id": "q", "failures": []}],
    )
    assert {path.name for path in paths.values()} == {
        "metrics.json", "per_query.csv", "report.md"
    }
