from __future__ import annotations

from legal_rag.exact_lookup import (
    EXACT_ARTICLE_LOOKUP,
    EXACT_CLAUSE_LOOKUP,
    EXACT_LEGAL_LOOKUP,
    EXACT_POINT_LOOKUP,
    NOT_EXACT_LOOKUP,
    POINT_NOT_FOUND,
    try_exact_lookup,
)
from legal_rag.navigation import (
    ARTICLE_NOT_FOUND,
    CLAUSE_NOT_FOUND,
    DOCUMENT_AMBIGUOUS,
    DOCUMENT_NOT_FOUND,
    SUCCESS,
)
from legal_rag.practical import run_practical_rag


def test_article_14_is_reconstructed_completely_without_model_calls() -> None:
    result = try_exact_lookup(
        "Điều 14 Luật Bảo vệ dữ liệu cá nhân quy định gì?"
    )

    assert result.handled is True
    assert result.route == EXACT_LEGAL_LOOKUP
    assert result.intent == EXACT_ARTICLE_LOOKUP
    assert result.status == SUCCESS
    assert result.document_number == "91/2025/QH15"
    assert result.article == "14"
    assert [f"Khoản {number}." in result.content for number in range(1, 7)] == [True] * 6
    assert "a) Chủ thể dữ liệu cá nhân có yêu cầu" in result.content
    assert "đ) Thực hiện theo thỏa thuận;" in result.content
    assert result.retrieval_call_count == 0
    assert result.llm_call_count == 0


def test_document_number_article_lookup_returns_same_article() -> None:
    by_title = try_exact_lookup(
        "Điều 14 Luật Bảo vệ dữ liệu cá nhân quy định gì?"
    )
    by_number = try_exact_lookup("Cho tôi nội dung Điều 14 của 91/2025/QH15")

    assert by_number.status == SUCCESS
    assert by_number.document_id == "91-2025-QH15"
    assert by_number.content == by_title.content


def test_clause_lookup_contains_only_requested_clause_and_children() -> None:
    result = try_exact_lookup(
        "Khoản 2 Điều 14 Luật Bảo vệ dữ liệu cá nhân quy định gì?"
    )

    assert result.intent == EXACT_CLAUSE_LOOKUP
    assert result.status == SUCCESS
    assert result.clause == "2"
    assert "Khoản 2." in result.content
    assert "Điều 19 của Luật này" in result.content
    assert "Khoản 1." not in result.content
    assert "Khoản 3." not in result.content


def test_point_lookup_returns_only_exact_point_with_minimal_context() -> None:
    result = try_exact_lookup(
        "Điểm a khoản 1 Điều 14 Luật Bảo vệ dữ liệu cá nhân quy định gì?"
    )

    assert result.intent == EXACT_POINT_LOOKUP
    assert result.status == SUCCESS
    assert result.point == "a"
    assert "Điểm a khoản 1 Điều 14" in result.content
    assert "a) Chủ thể dữ liệu cá nhân có yêu cầu" in result.content
    assert "b) Đã hoàn thành mục đích" not in result.content


def test_vietnamese_d_stroke_point_is_not_normalized_to_ascii_d() -> None:
    d_ascii = try_exact_lookup(
        "Điểm d khoản 1 Điều 14 Luật Bảo vệ dữ liệu cá nhân quy định gì?"
    )
    d_stroke = try_exact_lookup(
        "Cho tôi điểm đ khoản 1 Điều 14 của 91/2025/QH15"
    )

    assert d_ascii.status == d_stroke.status == SUCCESS
    assert "quyết định của cơ quan nhà nước" in d_ascii.content
    assert "thỏa thuận" not in d_ascii.content
    assert d_stroke.point == "đ"
    assert "đ) Thực hiện theo thỏa thuận;" in d_stroke.content
    assert "quyết định của cơ quan nhà nước" not in d_stroke.content


def test_missing_article_clause_point_and_document_do_not_guess() -> None:
    missing_article = try_exact_lookup(
        "Điều 999 Luật Bảo vệ dữ liệu cá nhân quy định gì?"
    )
    missing_clause = try_exact_lookup(
        "Khoản 999 Điều 14 Luật Bảo vệ dữ liệu cá nhân quy định gì?"
    )
    missing_point = try_exact_lookup(
        "Điểm z khoản 1 Điều 14 Luật Bảo vệ dữ liệu cá nhân quy định gì?"
    )
    missing_document = try_exact_lookup(
        "Điều 14 Luật Không Hề Tồn Tại quy định gì?"
    )

    assert missing_article.status == ARTICLE_NOT_FOUND
    assert missing_clause.status == CLAUSE_NOT_FOUND
    assert missing_point.status == POINT_NOT_FOUND
    assert missing_document.status == DOCUMENT_NOT_FOUND
    assert not missing_article.content
    assert not missing_clause.content
    assert not missing_point.content
    assert not missing_document.content


def test_ambiguous_document_reference_returns_candidates_without_guessing() -> None:
    result = try_exact_lookup(
        "Điều 14 Bảo vệ dữ liệu cá nhân quy định gì?"
    )

    assert result.handled is True
    assert result.status == DOCUMENT_AMBIGUOUS
    assert len(result.candidates) > 1
    assert result.document_id is None
    assert not result.content


def test_navigation_has_precedence_over_exact_lookup() -> None:
    class FailIfCalled:
        def __getattr__(self, name: str):
            raise AssertionError(f"unexpected dependency access: {name}")

    result = run_practical_rag(
        "Liệt kê các khoản của Điều 14 Luật Bảo vệ dữ liệu cá nhân",
        FailIfCalled(),
        FailIfCalled(),
    )

    assert result.intent == "ARTICLE_CLAUSE_LIST"
    assert result.status == SUCCESS


def test_exact_lookup_short_circuits_retrieval_and_llm() -> None:
    class FailIfCalled:
        def __getattr__(self, name: str):
            raise AssertionError(f"unexpected dependency access: {name}")

    result = run_practical_rag(
        "Điều 14 Luật Bảo vệ dữ liệu cá nhân quy định gì?",
        FailIfCalled(),
        FailIfCalled(),
    )

    assert result.route == EXACT_LEGAL_LOOKUP
    assert result.retrieval_call_count == result.llm_call_count == 0


def test_broad_qa_is_not_exact_lookup_and_falls_through_to_v1(monkeypatch) -> None:
    query = "Quy định về xóa dữ liệu cá nhân là gì?"
    detected = try_exact_lookup(query)
    expected = object()
    calls = []

    def fake_v1(received_query, pipeline, client, **kwargs):
        calls.append((received_query, pipeline, client, kwargs))
        return expected

    monkeypatch.setattr("legal_rag.practical.run_agentic_rag", fake_v1)
    result = run_practical_rag(query, "pipeline", "client")

    assert detected.handled is False
    assert detected.intent == NOT_EXACT_LOOKUP
    assert result is expected
    assert calls == [(query, "pipeline", "client", {
        "final_evidence_policy": "GAP_PRESERVING_V1_PRACTICAL_V1",
    })]


def test_semantic_article_question_is_not_exact_lookup() -> None:
    result = try_exact_lookup("Điều 14 có áp dụng cho app của tôi không?")

    assert result.handled is False
    assert result.status == NOT_EXACT_LOOKUP


def test_health_app_query_still_falls_through_to_v1(monkeypatch) -> None:
    query = (
        "Tôi muốn xây một app về sức khỏe cho người tiêu dùng sử dụng, "
        "tôi có cần lưu ý gì không?"
    )
    expected = object()
    monkeypatch.setattr(
        "legal_rag.practical.run_agentic_rag", lambda *args, **kwargs: expected
    )

    assert run_practical_rag(query, object(), object()) is expected
