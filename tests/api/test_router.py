from __future__ import annotations

from fastapi.testclient import TestClient

from legal_rag.agentic.v1.state import AgentState
from legal_rag.api.app import create_app
from legal_rag.api.service import CitationResult, RAGServiceError, ServiceResult


class FakeService:
    def __init__(self, *, fail: bool = False) -> None:
        self.fail = fail
        self.queries: list[str] = []

    def answer(self, query: str) -> ServiceResult:
        self.queries.append(query)
        if self.fail:
            raise RAGServiceError("failed-run", "failed-trace.json")
        state = AgentState(
            query=query,
            run_id="run-1",
            final_answer="Kết luận [E1]",
            final_status="success",
        )
        return ServiceResult(
            state=state,
            citations=[CitationResult(
                evidence_id="E1",
                chunk_id="chunk-1",
                document_title="Luật",
                document_number="1/2026",
                article="1",
                clause=None,
                point=None,
                source_url="https://example.test/source",
            )],
            rag_latency_ms=12.5,
            trace_id="trace.json",
        )


def test_answer_endpoint_returns_contract_and_normalizes_query() -> None:
    service = FakeService()
    with TestClient(create_app(service=service)) as client:
        response = client.post("/api/v1/answers", json={"query": "  Câu hỏi?  "})

    assert response.status_code == 200
    assert service.queries == ["Câu hỏi?"]
    assert response.json() == {
        "run_id": "run-1",
        "answer": "Kết luận [E1]",
        "status": "success",
        "citations": [{
            "evidence_id": "E1",
            "chunk_id": "chunk-1",
            "document_title": "Luật",
            "document_number": "1/2026",
            "article": "1",
            "clause": None,
            "point": None,
            "source_url": "https://example.test/source",
        }],
        "rag_latency_ms": 12.5,
        "trace_id": "trace.json",
    }


def test_empty_query_is_rejected_before_service_call() -> None:
    service = FakeService()
    with TestClient(create_app(service=service)) as client:
        response = client.post("/api/v1/answers", json={"query": "   "})

    assert response.status_code == 422
    assert service.queries == []


def test_service_error_returns_safe_response_with_trace_identity() -> None:
    with TestClient(create_app(service=FakeService(fail=True))) as client:
        response = client.post("/api/v1/answers", json={"query": "Câu hỏi?"})

    assert response.status_code == 500
    assert response.json() == {
        "detail": "RAG execution failed",
        "run_id": "failed-run",
        "trace_id": "failed-trace.json",
    }


def test_health_reports_ready_without_loading_production_dependencies() -> None:
    with TestClient(create_app(service=FakeService())) as client:
        response = client.get("/api/v1/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ready"}


def test_static_frontend_is_served() -> None:
    with TestClient(create_app(service=FakeService())) as client:
        index = client.get("/")
        script = client.get("/static/app.js")

    assert index.status_code == 200
    assert "Hỏi đáp pháp luật Việt Nam" in index.text
    assert script.status_code == 200
    assert "HTTP end-to-end" in script.text
