"""Final evidence selection policies for Agentic RAG v1.

The historical policy is intentionally implemented by the controller's
existing Top-K path. The practical policy in this module is an opt-in wrapper
around the same merged, original-query rerank.
"""

from __future__ import annotations

from collections.abc import Sequence as SequenceABC
from dataclasses import dataclass, replace
from typing import Any, Sequence

from ...retrieval.pipeline import DEFAULT_TOP_K, Evidence

HISTORICAL_V1 = "HISTORICAL_V1"
GAP_PRESERVING_V1_PRACTICAL_V1 = "GAP_PRESERVING_V1_PRACTICAL_V1"
MAX_RESERVED_EXPANSION_SLOTS = 2


@dataclass(frozen=True)
class ExpansionResult:
    """Ranked evidence returned by one targeted query for one coverage gap."""

    target_gap: str
    sub_query: str
    evidences: Sequence[Evidence]


def valid_expansion_evidence(item: Any) -> bool:
    """Return whether an expansion result has a usable identity and content."""
    if not isinstance(item, Evidence):
        return False
    if not isinstance(item.rank, int) or isinstance(item.rank, bool) or item.rank < 1:
        return False
    if not isinstance(item.chunk_id, str) or not item.chunk_id.strip():
        return False
    return bool(
        (isinstance(item.text, str) and item.text.strip())
        or (isinstance(item.retrieval_text, str) and item.retrieval_text.strip())
    )


def _unique_evidence(items: Sequence[Evidence]) -> list[Evidence]:
    seen: set[str] = set()
    result: list[Evidence] = []
    for item in items:
        if not isinstance(item, Evidence) or not isinstance(item.chunk_id, str):
            continue
        chunk_id = item.chunk_id.strip()
        if not chunk_id or chunk_id in seen:
            continue
        seen.add(chunk_id)
        result.append(item)
    return result


def _gap_entry(gap: ExpansionResult, *, chunk_id: str | None,
               status: str) -> dict[str, Any]:
    return {
        "target_gap": gap.target_gap,
        "sub_query": gap.sub_query,
        "chunk_id": chunk_id,
        "status": status,
    }


def select_gap_preserving_evidence(
    global_ranked: Sequence[Evidence],
    initial_evidence: Sequence[Evidence],
    expansion_results: Sequence[ExpansionResult],
    *,
    top_k: int = DEFAULT_TOP_K,
) -> tuple[
    list[Evidence], list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]
]:
    """Reserve up to two targeted results, then fill from the global ranking.

    Each target result list is already ordered by its local retrieval rank.
    Scores from those calls are deliberately ignored because each was produced
    against a different query. A targeted result already present in global
    Top-K satisfies that gap without consuming a reservation slot. If an
    earlier gap reserved a chunk, that same chunk also satisfies later gaps;
    the next candidate is not reserved for the later gap.
    """
    if top_k < 1:
        raise ValueError("top_k must be >= 1")

    global_unique = _unique_evidence(global_ranked)
    global_by_id = {item.chunk_id: item for item in global_unique}
    global_top_ids = {item.chunk_id for item in global_unique[:top_k]}
    global_ranks = {item.chunk_id: rank for rank, item in enumerate(global_unique, 1)}
    initial_ids = {item.chunk_id for item in _unique_evidence(initial_evidence)}
    reserved_evidence: list[Evidence] = []
    reserved_ids: set[str] = set()
    protected_global_ids: set[str] = set()
    reservations: list[dict[str, Any]] = []
    gap_results: list[dict[str, Any]] = []
    selected_gaps: dict[str, list[dict[str, Any]]] = {}

    # Invalid/missing expansion calls degrade to an empty call. Valid calls
    # still proceed, so one malformed result cannot break the query.
    for gap in expansion_results:
        if not isinstance(gap, ExpansionResult):
            continue
        candidates = gap.evidences
        if not isinstance(candidates, SequenceABC) or isinstance(candidates, (str, bytes)):
            candidates = ()
        ranked_targets = _unique_evidence([
            item for item in candidates if valid_expansion_evidence(item)
        ])
        ranked_targets.sort(key=lambda item: item.rank)
        if not ranked_targets:
            gap_results.append(_gap_entry(gap, chunk_id=None, status="no_valid_evidence"))
            continue

        best = ranked_targets[0]
        chunk_id = best.chunk_id.strip()
        globally_ranked_item = global_by_id.get(chunk_id)
        if globally_ranked_item is None:
            gap_results.append(_gap_entry(
                gap, chunk_id=None, status="missing_from_global_rerank"
            ))
            continue
        selected_gaps.setdefault(chunk_id, []).append({
            "target_gap": gap.target_gap,
            "sub_query": gap.sub_query,
            "targeted_rank": best.rank,
        })
        if chunk_id in global_top_ids:
            if (chunk_id not in protected_global_ids
                    and len(reserved_evidence) + len(protected_global_ids) < top_k):
                protected_global_ids.add(chunk_id)
            gap_results.append(_gap_entry(
                gap, chunk_id=chunk_id, status="already_in_global_top_k"
            ))
            continue
        if chunk_id in reserved_ids or chunk_id in protected_global_ids:
            gap_results.append(_gap_entry(gap, chunk_id=chunk_id, status="already_selected"))
            continue
        if len(reservations) >= min(MAX_RESERVED_EXPANSION_SLOTS, top_k):
            gap_results.append(_gap_entry(
                gap, chunk_id=None, status="reservation_cap_reached"
            ))
            continue

        # Keep final evidence scores on the original-query rerank scale.
        # The targeted rank is carried separately in the trace.
        reserved_evidence.append(globally_ranked_item)
        reserved_ids.add(chunk_id)
        reservations.append({
            "target_gap": gap.target_gap,
            "sub_query": gap.sub_query,
            "chunk_id": chunk_id,
            "targeted_rank": best.rank,
        })
        gap_results.append(_gap_entry(gap, chunk_id=chunk_id, status="reserved"))

    selected = list(reserved_evidence)
    selected_ids = set(reserved_ids)
    # Keep global-Top-K expansion matches in the final list even when newly
    # reserved items would otherwise push a lower-ranked match past Top-K.
    for item in global_unique:
        if item.chunk_id in protected_global_ids and item.chunk_id not in selected_ids:
            selected.append(item)
            selected_ids.add(item.chunk_id)
    for item in global_unique:
        if len(selected) >= top_k:
            break
        if item.chunk_id in selected_ids:
            continue
        selected.append(item)
        selected_ids.add(item.chunk_id)

    selected = [replace(item, rank=index) for index, item in enumerate(selected[:top_k], 1)]
    selection_trace: list[dict[str, Any]] = []
    for item in selected:
        gaps = selected_gaps.get(item.chunk_id, [])
        if any(entry["chunk_id"] == item.chunk_id for entry in reservations):
            origin = "EXPANSION_RESERVED"
        elif item.chunk_id in initial_ids:
            origin = "INITIAL_GLOBAL"
        else:
            origin = "GLOBAL_FILL"
        selection_trace.append({
            "rank": item.rank,
            "evidence_id": item.evidence_id,
            "chunk_id": item.chunk_id,
            "global_rank": global_ranks.get(item.chunk_id),
            "targeted_rank": gaps[0]["targeted_rank"] if gaps else None,
            "selection_origin": origin,
            "target_gap": gaps[0]["target_gap"] if gaps else None,
            "sub_query": gaps[0]["sub_query"] if gaps else None,
            "target_gaps": gaps,
        })
    return selected, reservations, gap_results, selection_trace
