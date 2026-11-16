from __future__ import annotations

import json
from pathlib import Path

from legal_rag.document_scoped_search import (
    DOCUMENT_SCOPED_SEARCH,
    NO_RELEVANT_RESULTS,
    NOT_DOCUMENT_SCOPED_SEARCH,
    detect_document_scoped_search,
    try_document_scoped_search,
)
from legal_rag.navigation import (
    DOCUMENT_AMBIGUOUS,
    DOCUMENT_NOT_FOUND,
    SUCCESS,
    DocumentNavigator,
)
from legal_rag.practical import run_practical_rag
from legal_rag.retrieval.pipeline import Evidence


ROOT = Path(__file__).parents[1]
CHUNKS = ROOT / "data/versions/corpus-v0.2/chunks/chunks.jsonl"


def _corpus_rows() -> dict[str, dict]:
    wanted = {
        "91-2025-QH15_dieu-30_khoan-1",
        "91-2025-QH15_dieu-30_khoan-4",
        "91-2025-QH15_dieu-26_khoan-1_diem-a",
        "91-2025-QH15_dieu-31_khoan-1",
        "356-2025-ND-CP_dieu-12_khoan-1",
    }
    rows = {}
    with CHUNKS.open(encoding="utf-8") as handle:
        for line in handle:
            row = json.loads(line)
            if row.get("chunk_id") in wanted:
                rows[row["chunk_id"]] = row
    assert set(rows) == wanted
    return rows


ROWS = _corpus_rows()


def _evidence(chunk_id: str, rank: int) -> Evidence:
    row = ROWS[chunk_id]
    return Evidence(
        rank=rank,
        evidence_id=f"E{rank}",
        chunk_id=chunk_id,
        document_id=row["document_id"],
        document_number=row["document_number"],
        document_title=row["document_title"],
        article_id=row["article_id"],
        article=row["article"],
        article_label=f"Điều {row['article']}",
        clause=row.get("clause"),
        clause_label=f"Khoản {row['clause']}" if row.get("clause") else None,
        point=row.get("point"),
        point_label=f"Điểm {row['point']}" if row.get("point") else None,
        text=row["text"],
        retrieval_text=row["retrieval_text"],
        official_source_url=row.get("official_source_url"),
        reranker_score=float(10 - rank),
        bm25_rank=rank,
        dense_rank=rank,
    )


class CorpusBackedFakePipeline:
    """Returns verified corpus rows while asserting pre-retrieval document scope."""

    def __init__(self) -> None:
        self.calls: list[tuple[str, int, str | None]] = []

    def retrieve(self, query, top_k, *, document_id=None):
        self.calls.append((query, top_k, document_id))
        by_query = {
            "trí tuệ nhân tạo": [
                "91-2025-QH15_dieu-30_khoan-1",
                "91-2025-QH15_dieu-30_khoan-4",
            ],
            "dữ liệu sức khỏe": ["91-2025-QH15_dieu-26_khoan-1_diem-a"],
            "dữ liệu vị trí": ["91-2025-QH15_dieu-31_khoan-1"],
            "điện toán đám mây": ["356-2025-ND-CP_dieu-12_khoan-1"],
        }
        ids = [
            chunk_id for chunk_id in by_query.get(query, [])
            if ROWS[chunk_id]["document_id"] == document_id
        ]
        return [_evidence(chunk_id, rank) for rank, chunk_id in enumerate(ids[:top_k], 1)]


def test_ai_search_is_isolated_and_aggregated_by_article() -> None:
    pipeline = CorpusBackedFakePipeline()
    result = try_document_scoped_search(
        "Trong Luật Bảo vệ dữ liệu cá nhân có những điều nào liên quan đến trí tuệ nhân tạo?",
        pipeline,
    )

    assert result.handled is True
    assert result.route == DOCUMENT_SCOPED_SEARCH
    assert result.status == SUCCESS
    assert result.document_id == "91-2025-QH15"
    assert result.scoped_query == "trí tuệ nhân tạo"
    assert {item.document_id for item in result.results} == {"91-2025-QH15"}
    assert [item.article_id for item in result.results] == [
        "91-2025-QH15_dieu-30", "91-2025-QH15_dieu-30"
    ]
    assert [item.clause for item in result.provisions[0].matches] == ["1", "4"]
    assert len(result.provisions) == 1
    assert result.retrieval_call_count == 1
    assert result.llm_call_count == 0
    assert pipeline.calls == [("trí tuệ nhân tạo", 5, "91-2025-QH15")]


def test_health_data_uses_verified_health_provision_without_leakage() -> None:
    result = try_document_scoped_search(
        "Tìm các quy định về dữ liệu sức khỏe trong Luật Bảo vệ dữ liệu cá nhân",
        CorpusBackedFakePipeline(),
    )

    assert result.document_id == "91-2025-QH15"
    assert result.results[0].article_id == "91-2025-QH15_dieu-26"
    assert "sức khỏe" in result.provisions[0].article_title.casefold()
    assert all(item.document_id == "91-2025-QH15" for item in result.results)


def test_document_number_resolves_before_location_search() -> None:
    result = try_document_scoped_search(
        "Trong 91/2025/QH15 có quy định nào về dữ liệu vị trí?",
        CorpusBackedFakePipeline(),
    )

    assert result.route == DOCUMENT_SCOPED_SEARCH
    assert result.document_number == "91/2025/QH15"
    assert result.results[0].article_id == "91-2025-QH15_dieu-31"


def test_decree_cloud_search_returns_only_decree_chunks() -> None:
    result = try_document_scoped_search(
        "Nghị định 356/2025/NĐ-CP quy định gì về điện toán đám mây?",
        CorpusBackedFakePipeline(),
    )

    assert result.document_id == "356-2025-ND-CP"
    assert result.results[0].article_id == "356-2025-ND-CP_dieu-12"
    assert all(item.document_id == "356-2025-ND-CP" for item in result.results)


def test_existing_deterministic_routes_keep_precedence() -> None:
    fail = object()
    navigation = run_practical_rag(
        "Liệt kê các điều khoản của Luật Bảo vệ dữ liệu cá nhân", fail, fail
    )
    exact = run_practical_rag(
        "Điều 14 Luật Bảo vệ dữ liệu cá nhân quy định gì?", fail, fail
    )

    assert navigation.intent == "DOCUMENT_ARTICLE_LIST"
    assert exact.route == "EXACT_LEGAL_LOOKUP"


def test_broad_product_and_reasoning_queries_fall_through_unchanged(monkeypatch) -> None:
    queries = [
        "Quy định về dữ liệu sức khỏe là gì?",
        "Tôi muốn xây một app về sức khỏe cho người tiêu dùng sử dụng, tôi có cần lưu ý gì không?",
        "Điều 14 Luật Bảo vệ dữ liệu cá nhân có áp dụng cho app của tôi không?",
    ]
    calls = []
    sentinel = object()

    def fake_v1(query, pipeline, client, **kwargs):
        calls.append((query, pipeline, client, kwargs))
        return sentinel

    monkeypatch.setattr("legal_rag.practical.run_agentic_rag", fake_v1)
    for query in queries:
        assert detect_document_scoped_search(query).intent == NOT_DOCUMENT_SCOPED_SEARCH
        assert run_practical_rag(query, "pipeline", "client") is sentinel

    assert [call[0] for call in calls] == queries


def test_foreign_evidence_is_rejected_instead_of_silently_filtered() -> None:
    class BrokenPipeline:
        def retrieve(self, query, top_k, *, document_id=None):
            return [_evidence("356-2025-ND-CP_dieu-12_khoan-1", 1)]

    try:
        try_document_scoped_search(
            "Trong Luật Bảo vệ dữ liệu cá nhân có những điều nào liên quan đến trí tuệ nhân tạo?",
            BrokenPipeline(),
        )
    except RuntimeError as exc:
        assert "foreign chunks" in str(exc)
    else:
        raise AssertionError("foreign-document evidence was accepted")


def test_unknown_explicit_document_returns_not_found_without_retrieval() -> None:
    pipeline = CorpusBackedFakePipeline()
    result = try_document_scoped_search(
        "Tìm các quy định về AI trong Luật Không Hề Tồn Tại", pipeline
    )

    assert result.handled is True
    assert result.status == DOCUMENT_NOT_FOUND
    assert result.retrieval_call_count == 0
    assert pipeline.calls == []


def test_ambiguous_explicit_document_returns_candidates_without_retrieval() -> None:
    documents = [
        {"document_id": "A", "document_number": "1/2026/QH", "title": "Luật Mẫu"},
        {"document_id": "B", "document_number": "2/2026/QH", "title": "Luật Mẫu"},
    ]
    pipeline = CorpusBackedFakePipeline()
    result = try_document_scoped_search(
        "Tìm các quy định về AI trong Luật Mẫu",
        pipeline,
        navigator=DocumentNavigator(documents, []),
    )

    assert result.status == DOCUMENT_AMBIGUOUS
    assert [item.document_id for item in result.candidates] == ["A", "B"]
    assert result.retrieval_call_count == 0
    assert pipeline.calls == []


def test_empty_scoped_candidates_return_no_relevant_results() -> None:
    pipeline = CorpusBackedFakePipeline()
    result = try_document_scoped_search(
        "Tìm các quy định về chủ đề không có trong Luật Bảo vệ dữ liệu cá nhân",
        pipeline,
    )

    assert result.status == NO_RELEVANT_RESULTS
    assert result.results == result.provisions == ()
    assert result.retrieval_call_count == 1
    assert result.llm_call_count == 0
