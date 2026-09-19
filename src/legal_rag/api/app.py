"""FastAPI application factory and production dependency lifecycle."""

from __future__ import annotations

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from ..agentic.v1.controller import AgenticRAGController
from ..agentic.v1.trace import require_expected_model
from ..llm_client import client_from_env
from ..retrieval.pipeline import RetrievalPipeline
from .router import router
from .service import RAGService

STATIC_DIR = Path(__file__).with_name("static")


def build_service() -> RAGService:
    client = client_from_env()
    require_expected_model(client)
    pipeline = RetrievalPipeline()
    controller = AgenticRAGController(pipeline, client)
    return RAGService(controller, client)


def create_app(service: RAGService | None = None) -> FastAPI:
    @asynccontextmanager
    async def lifespan(app: FastAPI) -> AsyncIterator[None]:
        app.state.rag_service = service if service is not None else build_service()
        yield

    application = FastAPI(
        title="Vietnamese Legal Agentic RAG API",
        version="0.1.0",
        lifespan=lifespan,
    )
    application.include_router(router)
    application.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

    @application.get("/", include_in_schema=False)
    def index() -> FileResponse:
        return FileResponse(STATIC_DIR / "index.html")

    return application


app = create_app()
