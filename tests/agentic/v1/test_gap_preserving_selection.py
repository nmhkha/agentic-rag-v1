from __future__ import annotations

from dataclasses import replace

from legal_rag.agentic.v1.controller import AgenticRAGController
from legal_rag.agentic.v1.evidence_selection import (
    GAP_PRESERVING_V1_PRACTICAL_V1,
    HISTORICAL_V1,
    MAX_RESERVED_EXPANSION_SLOTS,
)
from legal_rag.agentic.v1.trace import trace_for_state
from tests.agentic.v1.support import STRAIGHT, ScriptedClient, make_evidence, model_answer


HEALTH_GAP = "specific personal-data rules for medical/health applications"
SECURITY_GAP = "security and data-protection requirements"


def _evidence(chunk_id: str, rank: int, text: str, *, article: str = "1"):
    return replace(
        make_evidence(rank),
        chunk_id=chunk_id,
        evidence_id=f"E{rank}",
        article_id=f"91-2025-QH15_dieu-{article}",
        article=article,
        text=text,
        retrieval_text=text,
    )


class PolicyPipeline:
    """Offline ranked retrieval fixture; no corpus or network access."""

    def __init__(self, initial, by_gap, global_order=None):
        self.initial = list(initial)
        self.by_gap = by_gap
        self.global_order = list(global_order or [])
        self.calls = []
        self.rerank_calls = []

    def retrieve_with_audit(self, query, top_k=5, *, all_candidates=False):
        self.calls.append((query, all_candidates))
        values = self.initial if len(self.calls) == 1 else next(
            (rows for gap, rows in self.by_gap.items() if query.startswith(gap)), []
        )
        audit = {
            "query": query,
            "candidate_chunk_ids": [item.chunk_id for item in values if hasattr(item, "chunk_id")],
            "candidate_count": len(values),
            "reranker_ranks": [],
            "top5_chunk_ids": [item.chunk_id for item in values[:5] if hasattr(item, "chunk_id")],
            "candidate_ranks": [],
        }
        return list(values), audit

    def rerank_evidence_pool(self, query, evidence_pool, top_k=5):
        self.rerank_calls.append((query, top_k, len(evidence_pool)))
        unique = {item.chunk_id: item for item in evidence_pool}
        order = [chunk_id for chunk_id in self.global_order if chunk_id in unique]
        order.extend(chunk_id for chunk_id in unique if chunk_id not in set(order))
        return [replace(unique[chunk_id], rank=rank, reranker_score=50 - rank)
                for rank, chunk_id in enumerate(order[:top_k], 1)]


def _coverage(*gaps):
    import json
    return json.dumps({"sufficient": False, "missing_aspects": list(gaps), "reason": "fixture"})


def _state(pipeline, gaps, *, policy=GAP_PRESERVING_V1_PRACTICAL_V1,
           answer="Nội dung 1 [E1]", used=("E1",)):
    responses = [_coverage(*gaps), model_answer(answer, list(used)), STRAIGHT[2]]
    return AgenticRAGController(
        pipeline,
        ScriptedClient(responses),
        enable_answer_revision=False,
        enable_citation_revision=False,
        final_evidence_policy=policy,
    ).run("q", run_id="fixture")


def test_no_expansion_keeps_the_historical_final_top5():
    initial = [make_evidence(i) for i in range(1, 6)]
    historical = _state(PolicyPipeline(initial, {}), (), policy=HISTORICAL_V1)
    practical = _state(PolicyPipeline(initial, {}), ())

    assert practical.final_top5 == historical.final_top5
    assert practical.final_evidence_policy == GAP_PRESERVING_V1_PRACTICAL_V1
    assert practical.expansion_reservations == []
    assert all(item["selection_origin"] == "INITIAL_GLOBAL"
               for item in practical.final_evidence_selection)


def test_one_targeted_gap_reserves_its_best_local_rank_and_keeps_top5():
    initial = [make_evidence(i) for i in range(1, 6)]
    targeted = [replace(make_evidence(i), rank=9 - i) for i in range(6, 9)]
    pipeline = PolicyPipeline(initial, {HEALTH_GAP: targeted})
    state = _state(pipeline, (HEALTH_GAP,))

    best_targeted = targeted[2]
    assert state.final_top5[0] == best_targeted.chunk_id
    assert state.final_top5 == [best_targeted.chunk_id, *[item.chunk_id for item in initial[:4]]]
    assert len(state.current_evidence) == 5
    assert state.expansion_reservations[0]["targeted_rank"] == 1
    assert state.final_evidence_selection[0]["selection_origin"] == "EXPANSION_RESERVED"


def test_two_targeted_gaps_are_both_reserved_with_a_two_slot_cap():
    initial = [make_evidence(i) for i in range(1, 6)]
    health = replace(make_evidence(6), rank=1)
    security = replace(make_evidence(7), rank=1)
    pipeline = PolicyPipeline(
        initial,
        {HEALTH_GAP: [health], SECURITY_GAP: [security]},
    )
    state = _state(
        pipeline,
        (HEALTH_GAP, SECURITY_GAP),
        answer="Nội dung 6 [E6]",
        used=("E6",),
    )

    assert state.final_top5[:2] == [health.chunk_id, security.chunk_id]
    assert len(state.expansion_reservations) == 2
    assert len(state.expansion_reservations) <= MAX_RESERVED_EXPANSION_SLOTS
    assert len(state.current_evidence) == 5


def test_global_top5_duplicate_satisfies_gap_without_duplicate_or_reservation():
    initial = [make_evidence(i) for i in range(1, 6)]
    next_best = make_evidence(6)
    pipeline = PolicyPipeline(
        initial,
        {HEALTH_GAP: [initial[0], next_best]},
    )
    state = _state(pipeline, (HEALTH_GAP,))

    assert state.expansion_reservations == []
    assert state.final_top5 == [item.chunk_id for item in initial]
    assert len(set(state.final_top5)) == 5
    assert state.expansion_gap_results[0]["status"] == "already_in_global_top_k"


def test_one_chunk_satisfying_two_gaps_is_reserved_once():
    initial = [make_evidence(i) for i in range(1, 6)]
    shared = make_evidence(6)
    pipeline = PolicyPipeline(
        initial,
        {HEALTH_GAP: [shared], SECURITY_GAP: [replace(shared, rank=1)]},
    )
    state = _state(
        pipeline,
        (HEALTH_GAP, SECURITY_GAP),
        answer="Nội dung 6 [E6]",
        used=("E6",),
    )

    assert state.final_top5.count(shared.chunk_id) == 1
    assert len(state.expansion_reservations) == 1
    assert state.expansion_gap_results[1]["status"] == "already_selected"
    trace_item = next(item for item in state.final_evidence_selection
                      if item["chunk_id"] == shared.chunk_id)
    assert [item["target_gap"] for item in trace_item["target_gaps"]] == [
        HEALTH_GAP, SECURITY_GAP
    ]


def test_empty_or_malformed_expansion_fills_from_global_candidates():
    initial = [make_evidence(i) for i in range(1, 6)]
    malformed = replace(make_evidence(6), chunk_id=" ", text="", retrieval_text="")
    pipeline = PolicyPipeline(
        initial,
        {HEALTH_GAP: [None, malformed]},
    )
    state = _state(pipeline, (HEALTH_GAP,))

    assert state.final_top5 == [item.chunk_id for item in initial]
    assert state.expansion_reservations == []
    assert state.expansion_gap_results[0]["status"] == "no_valid_evidence"
    assert len(pipeline.calls) == 2


def test_failed_expansion_call_does_not_fail_the_practical_query():
    class OneExpansionFails(PolicyPipeline):
        def retrieve_with_audit(self, query, top_k=5, *, all_candidates=False):
            if query.startswith(SECURITY_GAP):
                self.calls.append((query, all_candidates))
                raise RuntimeError("fixture retrieval failure")
            return super().retrieve_with_audit(
                query, top_k, all_candidates=all_candidates
            )

    initial = [make_evidence(i) for i in range(1, 6)]
    health = replace(make_evidence(6), rank=1)
    pipeline = OneExpansionFails(initial, {HEALTH_GAP: [health]})
    state = _state(pipeline, (HEALTH_GAP, SECURITY_GAP))

    assert state.final_top5[0] == health.chunk_id
    assert len(state.current_evidence) == 5
    assert len(state.retrieval_calls) == 3
    assert state.retrieval_calls[-1]["error"]["message"] == "fixture retrieval failure"


def test_three_gaps_never_reserve_more_than_two_slots():
    initial = [make_evidence(i) for i in range(1, 6)]
    gaps = (HEALTH_GAP, SECURITY_GAP, "third gap")
    targeted = {gap: [make_evidence(index + 6)] for index, gap in enumerate(gaps)}
    pipeline = PolicyPipeline(initial, targeted)
    state = _state(pipeline, gaps)

    assert len(state.expansion_reservations) == MAX_RESERVED_EXPANSION_SLOTS
    assert state.expansion_gap_results[2]["status"] == "reservation_cap_reached"
    assert len(state.current_evidence) == 5


def test_global_top5_gap_match_stays_after_two_other_reservations():
    initial = [make_evidence(i) for i in range(1, 6)]
    third_gap = "third gap already covered globally"
    pipeline = PolicyPipeline(
        initial,
        {
            HEALTH_GAP: [replace(make_evidence(6), rank=1)],
            SECURITY_GAP: [replace(make_evidence(7), rank=1)],
            third_gap: [initial[4]],
        },
    )
    state = _state(pipeline, (HEALTH_GAP, SECURITY_GAP, third_gap))

    assert len(state.expansion_reservations) == 2
    assert initial[4].chunk_id in state.final_top5
    assert state.expansion_gap_results[2]["status"] == "already_in_global_top_k"
    assert len(state.final_top5) == len(set(state.final_top5)) == 5


def test_health_app_non_live_fixture_preserves_article_26_and_article_37_gaps():
    """The broad original-query ranking excludes both targeted legal items."""
    initial = [
        _evidence("91-2025-QH15_dieu-14_khoan-1", 1, "Quyền của chủ thể dữ liệu cá nhân"),
        _evidence("91-2025-QH15_dieu-15_khoan-1", 2, "Cung cấp dữ liệu cá nhân"),
        _evidence("91-2025-QH15_dieu-18_khoan-1", 3, "Lưu trữ dữ liệu cá nhân"),
        _evidence("91-2025-QH15_dieu-23_khoan-1", 4, "Thông báo vi phạm dữ liệu cá nhân"),
        _evidence("91-2025-QH15_dieu-29_khoan-1", 5, "Thông báo dữ liệu thu thập khi dùng dịch vụ trực tuyến"),
    ]
    health_rule = _evidence(
        "91-2025-QH15_dieu-26_khoan-3", 1,
        "Tổ chức, cá nhân phát triển ứng dụng về y tế ... phải tuân thủ đầy đủ quy định về bảo vệ dữ liệu cá nhân.",
        article="26",
    )
    security_rule = _evidence(
        "91-2025-QH15_dieu-37_khoan-1_diem-c", 1,
        "Thực hiện biện pháp quản lý, kỹ thuật phù hợp để bảo vệ dữ liệu cá nhân.",
        article="37",
    )
    global_order = [item.chunk_id for item in initial] + [
        health_rule.chunk_id, security_rule.chunk_id,
    ]
    pipeline = PolicyPipeline(
        initial,
        {
            HEALTH_GAP: [health_rule],
            SECURITY_GAP: [security_rule],
        },
        global_order=global_order,
    )
    state = _state(
        pipeline,
        (HEALTH_GAP, SECURITY_GAP),
        answer="Ứng dụng y tế phải tuân thủ bảo vệ dữ liệu cá nhân [E6]",
        used=("E6",),
    )

    assert "91-2025-QH15_dieu-26_khoan-3" in state.final_top5
    assert "91-2025-QH15_dieu-37_khoan-1_diem-c" in state.final_top5
    assert health_rule.chunk_id not in global_order[:5]
    assert security_rule.chunk_id not in global_order[:5]
    assert state.final_top5[:2] == [health_rule.chunk_id, security_rule.chunk_id]
    assert state.current_evidence[0].reranker_score == 44
    assert state.current_evidence[1].reranker_score == 43
    assert len(pipeline.calls) == 3  # one initial plus the two existing expansion calls
    assert len(pipeline.rerank_calls) == 1
    assert len(state.llm_calls) == 3
    assert pipeline.rerank_calls[0][1] == pipeline.rerank_calls[0][2]

    trace = trace_for_state(state, None)
    assert trace["final_evidence_policy"] == GAP_PRESERVING_V1_PRACTICAL_V1
    assert trace["reserved_expansion_count"] == 2
    assert all(item["selection_origin"] == "EXPANSION_RESERVED"
               for item in trace["final_evidence_selection"][:2])


def test_historical_expansion_keeps_the_existing_rerank_top5_policy():
    initial = [make_evidence(i) for i in range(1, 6)]
    pipeline = PolicyPipeline(initial, {HEALTH_GAP: [make_evidence(6)]})
    expected_pipeline = PolicyPipeline(initial, {HEALTH_GAP: [make_evidence(6)]})
    expanded = [replace(make_evidence(6), evidence_id="E6")]
    expected = expected_pipeline.rerank_evidence_pool("q", initial + expanded, 5)

    state = _state(pipeline, (HEALTH_GAP,), policy=HISTORICAL_V1)

    assert state.final_evidence_policy == HISTORICAL_V1
    assert state.final_top5 == [item.chunk_id for item in expected]
    assert state.expansion_reservations == []
