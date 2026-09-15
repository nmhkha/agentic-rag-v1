from __future__ import annotations

from legal_rag.evaluation.validation import (
    dataset_integrity,
    validate_generation_dataset,
)


def test_pure_generation_validation_accepts_valid_minimal_dataset() -> None:
    dataset = {"items": [{
        "query_id": "q1",
        "required_points": [{"point_id": "P1", "supporting_chunk_ids": ["c1"]}],
    }]}
    assert validate_generation_dataset(dataset) == []
    assert dataset_integrity(dataset) == {"query_count": 1, "required_point_count": 1}


def test_pure_generation_validation_reports_duplicates() -> None:
    point = {"point_id": "P1", "supporting_chunk_ids": ["c1", "c1"]}
    dataset = {"items": [
        {"query_id": "q1", "required_points": [point, point]},
        {"query_id": "q1", "required_points": []},
    ]}
    errors = validate_generation_dataset(dataset)
    assert any("duplicate query_id" in error for error in errors)
    assert any("duplicate point_id" in error for error in errors)
    assert any("duplicate supporting chunk ID" in error for error in errors)
