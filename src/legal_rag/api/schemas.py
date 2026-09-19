"""Pydantic contracts exposed by the HTTP API."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator


FinalStatus = Literal[
    "success",
    "insufficient_evidence",
    "incomplete_answer",
    "citation_check_failed",
]


class AnswerRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    query: str = Field(min_length=1)

    @field_validator("query")
    @classmethod
    def normalize_query(cls, value: str) -> str:
        normalized = value.strip()
        if not normalized:
            raise ValueError("query must not be empty")
        return normalized


class CitationResponse(BaseModel):
    evidence_id: str
    chunk_id: str
    document_title: str | None = None
    document_number: str | None = None
    article: str | None = None
    clause: str | None = None
    point: str | None = None
    source_url: str | None = None


class AnswerResponse(BaseModel):
    run_id: str
    answer: str
    status: FinalStatus
    citations: list[CitationResponse]
    rag_latency_ms: float = Field(ge=0)
    trace_id: str


class ErrorResponse(BaseModel):
    detail: str
    run_id: str | None = None
    trace_id: str | None = None


class HealthResponse(BaseModel):
    status: Literal["ready"] = "ready"
