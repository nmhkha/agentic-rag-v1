#!/usr/bin/env python3
"""Parse internal model JSON and render the user-visible legal answer."""

from __future__ import annotations

import json
import re
from typing import Any


def parse_model_output(raw: str) -> dict[str, Any]:
    text = raw.strip()
    fenced = re.fullmatch(r"```(?:json)?\s*(.*?)\s*```", text, re.IGNORECASE | re.DOTALL)
    if fenced:
        text = fenced.group(1).strip()
    try:
        value = json.loads(text)
    except json.JSONDecodeError:
        start, end = text.find("{"), text.rfind("}")
        if start < 0 or end <= start:
            raise ValueError("LLM response does not contain a JSON object")
        try:
            value = json.loads(text[start:end + 1])
        except json.JSONDecodeError as exc:
            raise ValueError(f"Invalid JSON from LLM: {exc}") from exc
    if not isinstance(value, dict) or not isinstance(value.get("answer"), str):
        raise ValueError("LLM JSON must be an object containing string field 'answer'")
    used = value.get("used_evidence_ids", [])
    missing = value.get("missing_information", [])
    if not isinstance(used, list) or not all(isinstance(item, str) for item in used):
        raise ValueError("used_evidence_ids must be a string array")
    if not isinstance(missing, list) or not all(isinstance(item, str) for item in missing):
        raise ValueError("missing_information must be a string array")
    return {
        "answer": value["answer"].strip(),
        "used_evidence_ids": used,
        "insufficient_evidence": bool(value.get("insufficient_evidence", False)),
        "missing_information": missing,
    }


def format_final_response(answer: str, cited_ids: list[str],
                          citation_map: dict[str, dict[str, Any]]) -> str:
    lines = [answer]
    sources: list[str] = []
    for evidence_id in cited_ids:
        source = citation_map[evidence_id]
        location = [source.get("document_number")]
        location.extend(f"{label} {source[key]}" for label, key in
                        (("Điều", "article"), ("Khoản", "clause"), ("Điểm", "point"))
                        if source.get(key))
        sources.append(f"[{evidence_id}] " + ", ".join(item for item in location if item))
        if source.get("official_source_url"):
            sources.append(f"Official source: {source['official_source_url']}")
    if sources:
        lines.extend(["", "Nguồn tham chiếu:", "", *sources])
    return "\n".join(lines)
