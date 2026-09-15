from __future__ import annotations

import unittest

from legal_rag.agentic.v1.nodes import (
    _json_object, answer_revision_prompt, citation_revision_prompt,
    claims_needing_semantic_alignment, completeness_prompt, coverage_prompt,
    parse_completeness_response, parse_coverage_response, semantic_citation_prompt,
)
from tests.agentic.v1.support import make_evidence


class NodeTests(unittest.TestCase):
    def test_all_agentic_prompts_and_alignment_gate_contract(self) -> None:
        ev = [make_evidence(1)]
        prompts = [coverage_prompt("q", ev), completeness_prompt("q", "a", ev),
                   answer_revision_prompt("q", "a", ["x"], ev),
                   citation_revision_prompt("a", ["bad"], ev),
                   semantic_citation_prompt("a", ["claim"], ev, allow_revision=True)]
        for prompt in prompts:
            self.assertIsInstance(prompt, str)
            self.assertTrue(prompt.strip())
        answer = "Nội dung 1 [E1]. Khác hẳn [E1]"
        self.assertEqual(claims_needing_semantic_alignment(answer, ev), ["Khác hẳn [E1]"])

    def test_controller_json_and_structured_parse_fallbacks(self) -> None:
        self.assertEqual(_json_object('```json\n{"x":1}\n```'), {"x": 1})
        coverage = parse_coverage_response('{"sufficient":false,"missing_aspects":[" a ","","b","c","d"],"reason":"r"}')
        self.assertEqual(coverage.missing_aspects, ["a", "b", "c"])
        complete = parse_completeness_response('{"complete":false,"missing_points":["x"],"reason":"r"}')
        self.assertEqual(complete.missing_points, ["x"])
        with self.assertRaisesRegex(ValueError, "must be empty"):
            parse_coverage_response('{"sufficient":true,"missing_aspects":["x"]}')


if __name__ == "__main__":
    unittest.main()
