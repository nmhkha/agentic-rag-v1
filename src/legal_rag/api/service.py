"""Transport-independent service around the frozen Agentic RAG runtime."""

from __future__ import annotations

import time
import uuid
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from ..agentic.v1.controller import AgenticRAGController
from ..agentic.v1.state import AgentState
from ..agentic.v1.trace import record_execution_error, trace_for_state, write_trace
from ..document_scoped_search import DocumentScopedSearchResult
from ..exact_lookup import ExactLookupResult
from ..llm_client import LLMClient
from ..navigation import DocumentNavigator, NavigationResult
from ..practical import run_practical_rag


@dataclass(frozen=True)
class CitationResult:
    evidence_id: str
    chunk_id: str
    document_title: str | None
    document_number: str | None
    article: str | None
    clause: str | None
    point: str | None
    source_url: str | None


@dataclass(frozen=True)
class ServiceResult:
    state: AgentState
    citations: list[CitationResult]
    rag_latency_ms: float
    trace_id: str
    route: str = "V1_RAG"


class RAGServiceError(RuntimeError):
    """Safe error surfaced to the HTTP adapter after an execution trace is written."""

    def __init__(self, run_id: str, trace_id: str) -> None:
        super().__init__("RAG execution failed")
        self.run_id = run_id
        self.trace_id = trace_id


TraceWriter = Callable[[dict[str, Any]], Path]
Clock = Callable[[], float]


class RAGService:
    def __init__(
        self,
        controller: AgenticRAGController,
        client: LLMClient,
        *,
        navigator: DocumentNavigator | None = None,
        trace_writer: TraceWriter = write_trace,
        clock: Clock = time.perf_counter,
    ) -> None:
        self.controller = controller
        self.client = client
        self.navigator = navigator
        self.trace_writer = trace_writer
        self.clock = clock

    def answer(self, query: str) -> ServiceResult:
        normalized_query = query.strip()
        state = AgentState(query=normalized_query, run_id=uuid.uuid4().hex)
        started = self.clock()
        try:
            route_result = run_practical_rag(
                normalized_query,
                self.controller.pipeline,
                self.client,
                controller=self.controller,
                navigator=self.navigator,
                run_id=state.run_id,
                state=state,
            )
        except Exception as exc:
            record_execution_error(state, exc)
            trace_path = self.trace_writer(trace_for_state(state, self.client))
            raise RAGServiceError(state.run_id, trace_path.name) from exc

        if isinstance(route_result, NavigationResult):
            return self._handle_navigation(route_result, state, started)
        elif isinstance(route_result, ExactLookupResult):
            return self._handle_exact_lookup(route_result, state, started)
        elif isinstance(route_result, DocumentScopedSearchResult):
            return self._handle_scoped_search(route_result, state, started)
        else:
            return self._handle_agentic_state(route_result, started)

    def _handle_navigation(
        self, result: NavigationResult, state: AgentState, started: float
    ) -> ServiceResult:
        final_status = "success" if result.status == "SUCCESS" else "insufficient_evidence"
        state.final_answer = result.message
        state.final_status = final_status
        state.transitions.extend(["route:document_navigation", f"final:{final_status}"])
        citations: list[CitationResult] = []
        if result.status == "SUCCESS" and result.document_id:
            citations.append(
                CitationResult(
                    evidence_id="E1",
                    chunk_id=result.document_id,
                    document_title=result.document_title,
                    document_number=result.document_number,
                    article=result.article,
                    clause=result.clause,
                    point=None,
                    source_url=None,
                )
            )
        rag_latency_ms = (self.clock() - started) * 1000
        trace = trace_for_state(state, self.client)
        trace.update({
            "route": "DOCUMENT_NAVIGATION",
            "intent": result.intent,
            "status": result.status,
            "document_id": result.document_id,
            "document_number": result.document_number,
            "document_title": result.document_title,
            "article": result.article,
            "clause": result.clause,
            "count": result.count,
        })
        trace_path = self.trace_writer(trace)
        return ServiceResult(
            state=state,
            citations=citations,
            rag_latency_ms=rag_latency_ms,
            trace_id=trace_path.name,
            route="DOCUMENT_NAVIGATION",
        )

    def _handle_exact_lookup(
        self, result: ExactLookupResult, state: AgentState, started: float
    ) -> ServiceResult:
        final_status = "success" if result.status == "SUCCESS" else "insufficient_evidence"
        answer = result.message or result.content
        state.final_answer = answer
        state.final_status = final_status
        state.transitions.extend(["route:exact_legal_lookup", f"final:{final_status}"])
        citations: list[CitationResult] = []
        if result.status == "SUCCESS" and result.document_id:
            article_suffix = f"_dieu-{result.article}" if result.article else ""
            clause_suffix = f"_khoan-{result.clause}" if result.clause else ""
            point_suffix = f"_diem-{result.point}" if result.point else ""
            chunk_id = f"{result.document_id}{article_suffix}{clause_suffix}{point_suffix}"
            citations.append(
                CitationResult(
                    evidence_id="E1",
                    chunk_id=chunk_id,
                    document_title=result.document_title,
                    document_number=result.document_number,
                    article=result.article,
                    clause=result.clause,
                    point=result.point,
                    source_url=None,
                )
            )
        rag_latency_ms = (self.clock() - started) * 1000
        trace = trace_for_state(state, self.client)
        trace.update({
            "route": result.route,
            "intent": result.intent,
            "status": result.status,
            "document_id": result.document_id,
            "document_number": result.document_number,
            "document_title": result.document_title,
            "article": result.article,
            "clause": result.clause,
            "point": result.point,
        })
        trace_path = self.trace_writer(trace)
        return ServiceResult(
            state=state,
            citations=citations,
            rag_latency_ms=rag_latency_ms,
            trace_id=trace_path.name,
            route=result.route,
        )

    def _handle_scoped_search(
        self, result: DocumentScopedSearchResult, state: AgentState, started: float
    ) -> ServiceResult:
        final_status = "success" if result.status == "SUCCESS" else "insufficient_evidence"
        state.final_answer = result.message
        state.final_status = final_status
        state.transitions.extend(["route:document_scoped_search", f"final:{final_status}"])
        if result.results:
            state.current_evidence = [item.evidence for item in result.results]
            state.final_top5 = [item.chunk_id for item in result.results]
        citations = [
            CitationResult(
                evidence_id=f"E{item.rank}",
                chunk_id=item.chunk_id,
                document_title=item.document_title,
                document_number=item.document_number,
                article=item.article,
                clause=item.clause,
                point=item.point,
                source_url=getattr(item.evidence, "source_url", None),
            )
            for item in result.results
        ]
        rag_latency_ms = (self.clock() - started) * 1000
        trace = trace_for_state(state, self.client)
        trace.update({
            "route": result.route,
            "intent": result.intent,
            "status": result.status,
            "document_id": result.document_id,
            "document_number": result.document_number,
            "document_title": result.document_title,
            "scoped_query": result.scoped_query,
            "result_count": len(result.results),
        })
        trace_path = self.trace_writer(trace)
        return ServiceResult(
            state=state,
            citations=citations,
            rag_latency_ms=rag_latency_ms,
            trace_id=trace_path.name,
            route=result.route,
        )

    def _handle_agentic_state(
        self, state: AgentState, started: float
    ) -> ServiceResult:
        rag_latency_ms = (self.clock() - started) * 1000
        trace_path = self.trace_writer(trace_for_state(state, self.client))
        evidence_by_id = {
            evidence.evidence_id: evidence for evidence in state.current_evidence
        }
        citations = [
            CitationResult(
                evidence_id=evidence_id,
                chunk_id=evidence.chunk_id,
                document_title=evidence.document_title,
                document_number=evidence.document_number,
                article=evidence.article,
                clause=evidence.clause,
                point=evidence.point,
                source_url=evidence.source_url,
            )
            for evidence_id in state.citation_check.cited_evidence_ids
            if (evidence := evidence_by_id.get(evidence_id)) is not None
        ]
        return ServiceResult(
            state=state,
            citations=citations,
            rag_latency_ms=rag_latency_ms,
            trace_id=trace_path.name,
            route="V1_RAG",
        )

