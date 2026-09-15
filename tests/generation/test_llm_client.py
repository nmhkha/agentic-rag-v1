from __future__ import annotations

import json
import os
import unittest
from unittest.mock import patch

from legal_rag.llm_client import OpenAICompatibleClient, client_from_env


class FakeResponse:
    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

    def read(self):
        return b'{"choices":[{"message":{"content":"result"}}]}'


class LLMClientTests(unittest.TestCase):
    def _request(self, client):
        captured = []
        def fake(request, timeout):
            captured.append((request, timeout))
            return FakeResponse()
        with patch("urllib.request.urlopen", side_effect=fake):
            output = client.generate("prompt")
        request, timeout = captured[0]
        return output, request.full_url, request.data, dict(request.header_items()), timeout

    def test_request_and_response_semantics_without_network(self) -> None:
        args = ("model", "https://example.invalid/v1/", "secret", 7.5)
        output, url, data, headers, timeout = self._request(OpenAICompatibleClient(*args))
        self.assertEqual(output, "result")
        self.assertEqual(url, "https://example.invalid/v1/chat/completions")
        self.assertEqual(timeout, 7.5)
        self.assertEqual(headers["Authorization"], "Bearer secret")
        body = json.loads(data)
        self.assertEqual(body["temperature"], 0)
        self.assertEqual(body["response_format"], {"type": "json_object"})

    def test_environment_resolution_and_missing_error(self) -> None:
        values = {
            "RAG_LLM_MODEL": "gemini-3.5-flash-lite",
            "RAG_LLM_BASE_URL": "https://example.invalid/v1",
            "RAG_LLM_API_KEY": "not-real",
        }
        with patch.dict(os.environ, values, clear=True):
            client = client_from_env()
            self.assertEqual((client.model, client.base_url, client.api_key), tuple(values.values()))
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaisesRegex(RuntimeError, "Missing LLM configuration"):
                client_from_env()


if __name__ == "__main__":
    unittest.main()
