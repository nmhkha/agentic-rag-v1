from __future__ import annotations

import json

import pytest

from legal_rag.evaluation.pipelines import PIPELINES, get_pipeline, load_records


def test_registry_has_all_six_supported_systems() -> None:
    assert set(PIPELINES) == {
        "bm25", "dense", "hybrid-rrf", "reranker", "standard-rag", "agentic-v1"
    }
    assert {PIPELINES[name].kind for name in list(PIPELINES)[:4]} == {"retrieval"}


def test_retrieval_adapter_normalizes_csv_numbers() -> None:
    rows = get_pipeline("bm25").normalize([{"hit_at_1": "1", "query_id": "q"}])
    assert rows == [{"hit_at_1": 1.0, "query_id": "q"}]


def test_load_records_jsonl_and_unknown_pipeline(tmp_path) -> None:
    path = tmp_path / "results.jsonl"
    path.write_text(json.dumps({"query_id": "q"}) + "\n", encoding="utf-8")
    assert load_records(path) == [{"query_id": "q"}]
    with pytest.raises(ValueError, match="unknown pipeline"):
        get_pipeline("nope")
