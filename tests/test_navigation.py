from __future__ import annotations

from legal_rag.navigation import (
    ARTICLE_CLAUSE_LIST,
    CLAUSE_POINT_LIST,
    DOCUMENT_AMBIGUOUS,
    DOCUMENT_ARTICLE_COUNT,
    DOCUMENT_ARTICLE_LIST,
    DOCUMENT_NOT_FOUND,
    NOT_NAVIGATION,
    SUCCESS,
    DocumentNavigator,
    frozen_document_navigator,
    try_document_navigation,
)
from legal_rag.practical import run_practical_rag


def test_personal_data_law_article_enumeration_is_complete_and_ordered() -> None:
    result = try_document_navigation(
        "Liệt kê các điều khoản của Luật Bảo vệ dữ liệu cá nhân"
    )

    assert result.handled is True
    assert result.intent == DOCUMENT_ARTICLE_LIST
    assert result.status == SUCCESS
    assert result.document_number == "91/2025/QH15"
    assert result.document_id == "91-2025-QH15"
    assert result.count == 39
    assert len({item.canonical_id for item in result.items}) == result.count
    assert [item.number for item in result.items[:3]] == ["1", "2", "3"]
    assert [item.number for item in result.items[8:11]] == ["9", "10", "11"]
    assert "356/2025/NĐ-CP" not in result.message


def test_navigation_short_circuits_retrieval_and_llm() -> None:
    class FailIfCalled:
        def __getattr__(self, name: str):
            raise AssertionError(f"unexpected dependency access: {name}")

    result = run_practical_rag(
        "Liệt kê các điều khoản của Luật Bảo vệ dữ liệu cá nhân",
        FailIfCalled(),
        FailIfCalled(),
    )

    assert result.status == SUCCESS
    assert result.document_number == "91/2025/QH15"


def test_personal_data_law_article_count_comes_from_corpus() -> None:
    result = try_document_navigation(
        "Luật Bảo vệ dữ liệu cá nhân có bao nhiêu điều?"
    )

    assert result.intent == DOCUMENT_ARTICLE_COUNT
    assert result.status == SUCCESS
    assert result.count == 39
    assert result.message == "Luật Bảo vệ dữ liệu cá nhân (91/2025/QH15) có 39 điều."


def test_article_14_clause_list_returns_only_its_clauses() -> None:
    result = try_document_navigation(
        "Liệt kê các khoản của Điều 14 Luật Bảo vệ dữ liệu cá nhân"
    )

    assert result.intent == ARTICLE_CLAUSE_LIST
    assert result.status == SUCCESS
    assert result.article == "14"
    assert [item.number for item in result.items] == ["1", "2", "3", "4", "5", "6"]
    assert all("dieu-14_khoan-" in item.canonical_id for item in result.items)


def test_article_14_clause_1_point_list_returns_only_its_points() -> None:
    result = try_document_navigation(
        "Liệt kê các điểm của khoản 1 Điều 14 Luật Bảo vệ dữ liệu cá nhân"
    )

    assert result.intent == CLAUSE_POINT_LIST
    assert result.status == SUCCESS
    assert result.article == "14"
    assert result.clause == "1"
    assert [item.number for item in result.items] == ["a", "b", "c", "d", "đ", "e"]
    assert all("dieu-14_khoan-1_diem-" in item.canonical_id for item in result.items)


def test_document_number_format_resolves_exactly() -> None:
    result = try_document_navigation("Liệt kê các điều của 91-2025-QH15")

    assert result.status == SUCCESS
    assert result.document_number == "91/2025/QH15"
    assert result.count == 39


def test_product_question_is_not_navigation() -> None:
    result = try_document_navigation(
        "Tôi muốn xây một app về sức khỏe cho người tiêu dùng sử dụng, tôi có cần lưu ý gì không?"
    )

    assert result.handled is False
    assert result.intent == NOT_NAVIGATION
    assert result.status == NOT_NAVIGATION


def test_product_question_falls_through_to_unchanged_v1(monkeypatch) -> None:
    pipeline = object()
    client = object()
    expected = object()
    calls = []

    def fake_v1(query, received_pipeline, received_client, **kwargs):
        calls.append((query, received_pipeline, received_client, kwargs))
        return expected

    monkeypatch.setattr("legal_rag.practical.run_agentic_rag", fake_v1)
    query = (
        "Tôi muốn xây một app về sức khỏe cho người tiêu dùng sử dụng, "
        "tôi có cần lưu ý gì không?"
    )

    result = run_practical_rag(
        query, pipeline, client, run_id="same-v1-argument"
    )

    assert result is expected
    assert calls == [(query, pipeline, client, {
        "run_id": "same-v1-argument",
        "final_evidence_policy": "GAP_PRESERVING_V1_PRACTICAL_V1",
    })]


def test_missing_document_does_not_guess() -> None:
    result = try_document_navigation("Liệt kê các điều của Luật Không Hề Tồn Tại")

    assert result.handled is True
    assert result.status == DOCUMENT_NOT_FOUND
    assert not result.items


def test_ambiguous_document_returns_structured_candidates() -> None:
    result = try_document_navigation("Liệt kê các điều của Bảo vệ dữ liệu cá nhân")

    assert result.handled is True
    assert result.status == DOCUMENT_AMBIGUOUS
    assert len(result.candidates) > 1
    assert not result.items


def test_second_supported_clause_question_form() -> None:
    result = try_document_navigation(
        "Điều 14 của 91/2025/QH15 có những khoản nào?"
    )

    assert result.status == SUCCESS
    assert result.intent == ARTICLE_CLAUSE_LIST
    assert result.count == 6


def test_synthetic_duplicate_metadata_is_deduplicated_by_canonical_identity() -> None:
    source = {
        "document_id": "1-2026-QH",
        "document_number": "1/2026/QH",
        "title": "Luật Mẫu",
    }
    article = {
        "document_id": source["document_id"],
        "article_id": "1-2026-QH_dieu-2",
        "article_number": "2",
        "article_title": "Hai",
        "clauses": [],
    }
    navigator = DocumentNavigator(
        [source],
        [
            {**article, "article_id": "1-2026-QH_dieu-10", "article_number": "10"},
            article,
            article,
        ],
    )

    result = navigator.navigate("Liệt kê các điều của Luật Mẫu")

    assert [item.number for item in result.items] == ["2", "10"]
    assert result.count == 2


def test_frozen_navigator_identity_is_cached() -> None:
    assert frozen_document_navigator() is frozen_document_navigator()
