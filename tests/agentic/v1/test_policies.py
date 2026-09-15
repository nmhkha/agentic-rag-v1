from __future__ import annotations

import itertools
import unittest

from legal_rag.agentic.v1.policies import (
    MAX_ANSWER_REVISIONS, MAX_CITATION_REVISIONS, MAX_LLM_CALLS,
    MAX_RETRIEVAL_EXPANSIONS, MAX_SUB_QUERIES, answer_revision_allowed,
    citation_revision_allowed, determine_final_status, expansion_allowed,
    llm_call_allowed,
)


class PolicyTests(unittest.TestCase):
    def test_budgets_match_legacy(self) -> None:
        self.assertEqual((MAX_SUB_QUERIES, MAX_RETRIEVAL_EXPANSIONS,
                          MAX_ANSWER_REVISIONS, MAX_CITATION_REVISIONS,
                          MAX_LLM_CALLS), (3, 1, 1, 1, 6))

    def test_transition_predicate_truth_tables_match_legacy_expressions(self) -> None:
        for enabled, flag, count in itertools.product((False, True), (False, True), range(3)):
            self.assertEqual(
                answer_revision_allowed(enabled, flag, count),
                (not flag and enabled and count < 1),
            )
            self.assertEqual(
                citation_revision_allowed(enabled, flag, count),
                (not flag and enabled and count < 1),
            )
        for enabled, sufficient, has_missing in itertools.product((False, True), repeat=3):
            missing = ["x"] if has_missing else []
            self.assertEqual(
                expansion_allowed(enabled, sufficient, missing),
                bool(enabled and not sufficient and missing and 1 > 0),
            )
        for count in range(9):
            self.assertEqual(llm_call_allowed(count), count < 6)

    def test_final_status_exhaustive_truth_table_matches_legacy_chain(self) -> None:
        for values in itertools.product((False, True), repeat=5):
            citation, coverage, complete, expanded, declares = values
            if not citation: expected = "citation_check_failed"
            elif not coverage and not complete: expected = "insufficient_evidence"
            elif not complete: expected = "incomplete_answer"
            elif not coverage and not expanded: expected = "insufficient_evidence"
            elif declares and not coverage: expected = "insufficient_evidence"
            else: expected = "success"
            self.assertEqual(determine_final_status(
                citation_valid=citation, coverage_sufficient=coverage,
                completeness_complete=complete, expansion_used=expanded,
                answer_declares_insufficient=declares,
            ), expected)


if __name__ == "__main__":
    unittest.main()
