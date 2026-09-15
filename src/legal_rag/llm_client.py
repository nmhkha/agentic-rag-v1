#!/usr/bin/env python3
"""Provider-neutral generation interface with an OpenAI-compatible HTTP client."""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Protocol


class LLMClient(Protocol):
    def generate(self, prompt: str) -> str: ...


@dataclass
class OpenAICompatibleClient:
    model: str
    base_url: str
    api_key: str
    timeout: float = 120.0

    def generate(self, prompt: str) -> str:
        endpoint = self.base_url.rstrip("/")
        if not endpoint.endswith("/chat/completions"):
            endpoint += "/chat/completions"
        body = json.dumps({
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0,
            "response_format": {"type": "json_object"},
        }).encode("utf-8")
        request = urllib.request.Request(endpoint, data=body, method="POST", headers={
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        })
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                payload = json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")[:500]
            raise RuntimeError(f"LLM HTTP {exc.code}: {detail}") from exc
        return str(payload["choices"][0]["message"]["content"])


def client_from_env() -> OpenAICompatibleClient:
    model = os.getenv("RAG_LLM_MODEL", "").strip()
    base_url = os.getenv("RAG_LLM_BASE_URL", "").strip()
    api_key = os.getenv("RAG_LLM_API_KEY", "").strip()
    missing = [name for name, value in (("RAG_LLM_MODEL", model),
               ("RAG_LLM_BASE_URL", base_url), ("RAG_LLM_API_KEY", api_key)) if not value]
    if missing:
        raise RuntimeError("Missing LLM configuration: " + ", ".join(missing))
    return OpenAICompatibleClient(model, base_url, api_key)
