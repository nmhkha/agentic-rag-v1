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
from ..llm_client import LLMClient


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
        trace_writer: TraceWriter = write_trace,
        clock: Clock = time.perf_counter,
    ) -> None:
        self.controller = controller
        self.client = client
        self.trace_writer = trace_writer
        self.clock = clock

    def answer(self, query: str) -> ServiceResult:
        normalized_query = query.strip()
        state = AgentState(query=normalized_query, run_id=uuid.uuid4().hex)
        started = self.clock()
        try:
            state = self.controller.run(
                normalized_query,
                run_id=state.run_id,
                state=state,
            )
        except Exception as exc:
            record_execution_error(state, exc)
            trace_path = self.trace_writer(trace_for_state(state, self.client))
            raise RAGServiceError(state.run_id, trace_path.name) from exc
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
        )
