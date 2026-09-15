from __future__ import annotations

import ast
import json
from pathlib import Path

import pytest

from legal_rag.evaluation.runner import run_evaluation
from legal_rag.evaluation.validation import dataset_integrity


ROOT = Path(__file__).resolve().parents[2]
RESULTS = ROOT / "experiments/reference/retrieval"
GENERATION = ROOT / "experiments/reference/generation"


@pytest.mark.parametrize(
    ("pipeline", "stem"),
    [
        ("bm25", "bm25-simple-v0"),
        ("dense", "dense-jina-v3-v0"),
        ("hybrid-rrf", "hybrid-rrf-v0"),
        ("reranker", "bge-reranker-v2-m3-v0"),
    ],
)
def test_all_historical_retrieval_metrics_reproduce(pipeline, stem) -> None:
    legacy = json.loads((RESULTS / stem / f"{stem}_metrics.json").read_text(encoding="utf-8"))
    current = run_evaluation(
        pipeline=pipeline,
        results=RESULTS / stem / f"{stem}_per_query.csv",
        score_only=True,
    )["metrics"]
    assert current["query_count"] == legacy["query_count"] == 31
    for level in ("chunk_level", "article_level"):
        for key, expected in legacy[level].items():
            assert current[level][key] == pytest.approx(expected, abs=2e-10)


def test_reranker_reference_values() -> None:
    current = run_evaluation(
        pipeline="reranker",
        results=RESULTS / "bge-reranker-v2-m3-v0/bge-reranker-v2-m3-v0_per_query.csv",
        score_only=True,
    )["metrics"]
    assert current["chunk_level"] == pytest.approx({
        "hit_at_1": 0.5161290322580645,
        "hit_at_3": 0.7419354838709677,
        "hit_at_5": 0.9354838709677419,
        "recall_at_5": 0.6239119303635433,
        "recall_at_10": 0.7659498207885305,
        "mrr_at_10": 0.6664362519201228,
    }, abs=2e-10)
    assert current["article_level"] == pytest.approx({
        "hit_at_1": 0.6451612903225806,
        "hit_at_3": 0.9354838709677419,
        "hit_at_5": 0.967741935483871,
        "mrr_at_10": 0.7967741935483871,
    }, abs=2e-10)


def test_standard_rag_historical_metrics_reproduce() -> None:
    legacy = json.loads(
        (GENERATION / "standard-rag-v0/standard_rag_metrics_v0.json").read_text(encoding="utf-8")
    )
    current = run_evaluation(
        pipeline="standard-rag",
        results=GENERATION / "standard-rag-v0/standard_rag_eval_v0.jsonl",
        score_only=True,
    )["metrics"]
    assert current["query_count"] == legacy["query_count"] == 31
    assert current["required_point_count"] == legacy["required_point_count"] == 102
    assert current["supported_point_count"] == legacy["supported_point_count"] == 60
    for key in ("answer_completeness", "citation_completeness",
                "citation_correctness", "groundedness", "unsupported_claim_rate"):
        assert current[key]["macro"] == legacy[key]["macro"]
    assert current["answer_completeness"]["micro"] == legacy["answer_completeness"]["micro"]
    assert current["citation_syntax_validity"] == legacy["citation_syntax_validity"]


def test_agentic_v1_historical_macro_and_pooled_metrics_reproduce() -> None:
    legacy = json.loads(
        (GENERATION / "agentic-rag-v1/agentic_rag_metrics_v1_agentic-v1.json").read_text(encoding="utf-8")
    )["metrics"]
    current = run_evaluation(
        pipeline="agentic-v1",
        results=GENERATION / "agentic-rag-v1/agentic_rag_eval_v1_agentic-v1.jsonl",
        score_only=True,
    )["metrics"]
    assert current["required_point_count"] == 102
    assert current["supported_point_count"] == 65
    assert current["answer_completeness"]["macro"] == legacy["answer_completeness"]
    assert current["answer_completeness"]["micro"] == pytest.approx(65 / 102)
    for key in ("citation_completeness", "citation_correctness",
                "groundedness", "unsupported_claim_rate"):
        assert current[key]["macro"] == legacy[key]
    assert current["groundedness"]["numerator"] == 93
    assert current["groundedness"]["denominator"] == 97
    assert current["groundedness"]["pooled"] == pytest.approx(93 / 97)
    assert current["unsupported_claim_rate"]["numerator"] == 4
    assert current["unsupported_claim_rate"]["pooled"] == pytest.approx(4 / 97)
    for key, value in current["agentic_usage"].items():
        assert value == legacy[key]


def test_generation_gold_integrity_is_31_queries_102_points() -> None:
    dataset = json.loads(
        (ROOT / "eval-sets/generation/generation_eval_v1_verified.json").read_text(encoding="utf-8")
    )
    assert dataset_integrity(dataset) == {
        "query_count": 31, "required_point_count": 102
    }


def test_runtime_packages_do_not_import_evaluation_or_gold_loaders() -> None:
    runtime_paths = [
        ROOT / "src/legal_rag/retrieval",
        ROOT / "src/legal_rag/generation",
        ROOT / "src/legal_rag/agentic",
    ]
    files = [path for directory in runtime_paths for path in directory.rglob("*.py")]
    files.append(ROOT / "src/legal_rag/llm_client.py")
    forbidden = {"legal_rag.evaluation", "evaluate_standard_rag", "evaluate_agentic_rag"}
    for path in files:
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        imports = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imports.extend(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imports.append(node.module)
        assert not any(
            name in forbidden or name.startswith("legal_rag.evaluation.")
            for name in imports
        ), path
