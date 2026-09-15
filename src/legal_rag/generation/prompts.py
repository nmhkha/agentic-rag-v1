"""Exact loading and construction of the frozen legal RAG prompt."""

from __future__ import annotations

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_PROMPT_PATH = PROJECT_ROOT / "prompts" / "legal_rag_v0.txt"


def load_prompt(path: str | Path = DEFAULT_PROMPT_PATH) -> str:
    """Load prompt text without normalization or mutation."""
    return Path(path).read_text(encoding="utf-8")


def build_prompt(
    query: str,
    evidence_context: str,
    *,
    path: str | Path = DEFAULT_PROMPT_PATH,
) -> str:
    """Perform the same two ordered replacements as the legacy runtime."""
    template = load_prompt(path)
    return template.replace("{query}", query).replace(
        "{evidence_context}", evidence_context
    )
