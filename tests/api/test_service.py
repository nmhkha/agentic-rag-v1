from __future__ import annotations

from pathlib import Path

import pytest

from legal_rag.agentic.v1.controller import AgenticRAGController
from legal_rag.api.service import RAGService, RAGServiceError
from tests.agentic.v1.support import FakePipeline, STRAIGHT, ScriptedClient


def test_answer_returns_structured_result_and_writes_success_trace() -> None:
    traces = []
    client = ScriptedClient(list(STRAIGHT))
    service = RAGService(
        AgenticRAGController(FakePipeline(), client),
        client,
        trace_writer=lambda trace: traces.append(trace) or Path("success.json"),
        clock=iter([10.0, 10.125]).__next__,
    )

    result = service.answer("  Câu hỏi?  ")

    assert result.state.query == "Câu hỏi?"
    assert result.state.final_status == "success"
    assert result.rag_latency_ms == 125.0
    assert result.trace_id == "success.json"
    assert [citation.evidence_id for citation in result.citations] == ["E1"]
    assert traces[0]["final_status"] == "success"


def test_answer_writes_execution_error_trace_without_exposing_raw_error() -> None:
    traces = []
    client = ScriptedClient(["not-json"])
    service = RAGService(
        AgenticRAGController(FakePipeline(), client),
        client,
        trace_writer=lambda trace: traces.append(trace) or Path("error.json"),
    )

    with pytest.raises(RAGServiceError) as caught:
        service.answer("Câu hỏi?")

    assert str(caught.value) == "RAG execution failed"
    assert caught.value.trace_id == "error.json"
    assert traces[0]["final_status"] == "execution_error"
    assert traces[0]["state"]["execution_error"]["type"] == "ValueError"


def test_answer_exact_lookup_route_returns_citations_and_route() -> None:
    traces = []
    service = RAGService(
        AgenticRAGController(FakePipeline(), ScriptedClient([])),
        ScriptedClient([]),
        trace_writer=lambda trace: traces.append(trace) or Path("exact.json"),
        clock=iter([1.0, 1.05]).__next__,
    )

    result = service.answer("Điều 14 Luật Bảo vệ dữ liệu cá nhân quy định gì?")

    assert result.route == "EXACT_LEGAL_LOOKUP"
    assert result.state.final_status == "success"
    assert result.rag_latency_ms == pytest.approx(50.0)
    assert result.trace_id == "exact.json"
    assert len(result.citations) == 1
    citation = result.citations[0]
    assert citation.document_title == "Luật Bảo vệ dữ liệu cá nhân"
    assert citation.article == "14"
    assert "Điều 14" in (result.state.final_answer or "")
    assert traces[0]["route"] == "EXACT_LEGAL_LOOKUP"
    assert traces[0]["final_status"] == "success"


def test_answer_navigation_route_returns_structured_result() -> None:
    traces = []
    service = RAGService(
        AgenticRAGController(FakePipeline(), ScriptedClient([])),
        ScriptedClient([]),
        trace_writer=lambda trace: traces.append(trace) or Path("nav.json"),
        clock=iter([2.0, 2.02]).__next__,
    )

    result = service.answer("Liệt kê các khoản của Điều 14 Luật Bảo vệ dữ liệu cá nhân")

    assert result.route == "DOCUMENT_NAVIGATION"
    assert result.state.final_status == "success"
    assert result.rag_latency_ms == pytest.approx(20.0)
    assert result.trace_id == "nav.json"
    assert len(result.citations) == 1
    assert "Khoản" in (result.state.final_answer or "")
    assert traces[0]["route"] == "DOCUMENT_NAVIGATION"
    assert traces[0]["final_status"] == "success"

