"""Pure validation helpers for generation evaluation sets."""

from __future__ import annotations

from typing import Any, Mapping


def validate_generation_dataset(dataset: Mapping[str, Any]) -> list[str]:
    """Validate reusable record/point invariants without loading external files."""
    errors: list[str] = []
    items = dataset.get("items")
    if not isinstance(items, list):
        return ["items must be a list"]
    seen: set[str] = set()
    for index, item in enumerate(items, 1):
        if not isinstance(item, dict):
            errors.append(f"item {index}: record must be an object")
            continue
        query_id = item.get("query_id")
        prefix = f"item {index} ({query_id or '<missing>'})"
        if not isinstance(query_id, str) or not query_id.strip():
            errors.append(f"{prefix}: query_id is empty")
        elif query_id in seen:
            errors.append(f"{prefix}: duplicate query_id")
        else:
            seen.add(query_id)
        points = item.get("required_points")
        if not isinstance(points, list):
            errors.append(f"{prefix}: required_points must be a list")
            continue
        point_ids: set[str] = set()
        for point_index, point in enumerate(points, 1):
            point_prefix = f"{prefix} point {point_index}"
            if not isinstance(point, dict):
                errors.append(f"{point_prefix}: must be an object")
                continue
            point_id = point.get("point_id")
            if not isinstance(point_id, str) or not point_id.strip():
                errors.append(f"{point_prefix}: point_id is empty")
            elif point_id in point_ids:
                errors.append(f"{point_prefix}: duplicate point_id")
            else:
                point_ids.add(point_id)
            support = point.get("supporting_chunk_ids")
            if not isinstance(support, list) or not support:
                errors.append(
                    f"{point_prefix}: supporting_chunk_ids must be a non-empty list"
                )
            elif len(support) != len(set(support)):
                errors.append(f"{point_prefix}: duplicate supporting chunk ID")
    return errors


def dataset_integrity(dataset: Mapping[str, Any]) -> dict[str, int]:
    items = dataset.get("items", [])
    if not isinstance(items, list):
        raise ValueError("items must be a list")
    return {
        "query_count": len(items),
        "required_point_count": sum(
            len(item.get("required_points", []))
            for item in items
            if isinstance(item, dict)
        ),
    }
