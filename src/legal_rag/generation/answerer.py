"""Single-shot generation over already-formatted evidence."""

from __future__ import annotations

from pathlib import Path

from ..llm_client import LLMClient
from .prompts import DEFAULT_PROMPT_PATH, build_prompt


def generate_answer(
    query: str,
    evidence_context: str,
    client: LLMClient,
    *,
    prompt_path: str | Path = DEFAULT_PROMPT_PATH,
) -> tuple[str, str]:
    """Build the frozen prompt and return it with the client's raw response."""
    prompt = build_prompt(query, evidence_context, path=prompt_path)
    return prompt, client.generate(prompt)
