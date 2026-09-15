from __future__ import annotations

import json
import unittest
from pathlib import Path

from legal_rag.agentic.v1.controller import AgenticRAGController
from legal_rag.agentic.v1.trace import trace_for_state
from legal_rag.retrieval.pipeline import Evidence
from tests.agentic.v1.support import FakePipeline, STRAIGHT, ScriptedClient


class FrozenTraceCompatibilityTests(unittest.TestCase):
    def test_all_31_stored_initial_top5_are_reproduced(self) -> None:
        root = Path(__file__).parents[3]
        fields = set(Evidence.__dataclass_fields__)
        paths = sorted((root / "experiments/traces/agentic-rag-v1/agentic-v1").glob("eval*.json"))
        self.assertEqual(len(paths), 31)
        for path in paths:
            stored = json.loads(path.read_text(encoding="utf-8"))
            evidences = [Evidence(**{key: value for key, value in item.items() if key in fields})
                         for item in stored["state"]["initial_evidence"]]
            audit = stored["retrieval_calls"][0]
            client = ScriptedClient(list(STRAIGHT) + [
                '{"valid":true,"errors":[],"reason":"được hỗ trợ","revised_answer":null}'
            ])
            state = AgenticRAGController(FakePipeline(evidences, audit), client).run(
                stored["query"], run_id=stored["run_id"]
            )
            self.assertEqual(state.initial_top5, stored["initial_top5"], path.name)
            trace = trace_for_state(state, client)
            self.assertEqual(trace["initial_candidate_count"], stored["initial_candidate_count"], path.name)


if __name__ == "__main__":
    unittest.main()
