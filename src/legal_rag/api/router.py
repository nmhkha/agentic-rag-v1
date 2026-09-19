"""HTTP routes for the legal RAG service."""

from __future__ import annotations

from dataclasses import asdict

from fastapi import APIRouter, Depends, Request
from fastapi.concurrency import run_in_threadpool
from fastapi.responses import JSONResponse

from .schemas import (
    AnswerRequest,
    AnswerResponse,
    CitationResponse,
    ErrorResponse,
    HealthResponse,
)
from .service import RAGService, RAGServiceError


router = APIRouter(prefix="/api/v1")


def get_rag_service(request: Request) -> RAGService:
    return request.app.state.rag_service


@router.get("/health", response_model=HealthResponse)
def health(_: RAGService = Depends(get_rag_service)) -> HealthResponse:
    return HealthResponse()


@router.post(
    "/answers",
    response_model=AnswerResponse,
    responses={500: {"model": ErrorResponse}},
)
async def answer(
    payload: AnswerRequest,
    service: RAGService = Depends(get_rag_service),
) -> AnswerResponse | JSONResponse:
    try:
        result = await run_in_threadpool(service.answer, payload.query)
    except RAGServiceError as exc:
        error = ErrorResponse(
            detail=str(exc),
            run_id=exc.run_id,
            trace_id=exc.trace_id,
        )
        return JSONResponse(status_code=500, content=error.model_dump())

    return AnswerResponse(
        run_id=result.state.run_id,
        answer=result.state.final_answer or "",
        status=result.state.final_status,
        citations=[CitationResponse(**asdict(item)) for item in result.citations],
        rag_latency_ms=result.rag_latency_ms,
        trace_id=result.trace_id,
    )
