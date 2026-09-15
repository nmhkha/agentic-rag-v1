from __future__ import annotations

import unittest

from legal_rag.generation.answerer import generate_answer
from legal_rag.generation.prompts import build_prompt


class FakeClient:
    def __init__(self) -> None:
        self.prompts: list[str] = []

    def generate(self, prompt: str) -> str:
        self.prompts.append(prompt)
        return '{"answer":"A [E1]","used_evidence_ids":["E1"]}'


class AnswererTests(unittest.TestCase):
    def test_only_builds_prompt_and_delegates_generation(self) -> None:
        client = FakeClient()
        prompt, raw = generate_answer("Q?", "[E1]\nText", client)
        self.assertEqual(prompt, build_prompt("Q?", "[E1]\nText"))
        self.assertEqual(client.prompts, [prompt])
        self.assertEqual(raw, '{"answer":"A [E1]","used_evidence_ids":["E1"]}')


if __name__ == "__main__":
    unittest.main()
