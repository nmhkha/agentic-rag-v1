from __future__ import annotations

import unittest

from legal_rag.generation.verifier import validate_citations


class VerifierTests(unittest.TestCase):
    def test_valid_unknown_malformed_repeated_and_declared_sets(self) -> None:
        mapping = {"E1": {}, "E2": {}}
        cases = [
            ("Claim [E1][E2]", None),
            ("Unknown [E9]", None),
            ("Bad [E01] [e2] [E]", None),
            ("Repeat [E1]. Again [E1].", ["E1"]),
            ("Mismatch [E1]", ["E2"]),
            ("Order [E1][E2]", ["E2", "E1"]),
        ]
        for answer, used in cases:
            result = validate_citations(answer, mapping, used)
            self.assertIsInstance(result.valid, bool)
            self.assertEqual(result.cited_evidence_ids, list(dict.fromkeys(result.cited_evidence_ids)))
        self.assertTrue(validate_citations("Claim [E1][E2]", mapping).valid)
        self.assertFalse(validate_citations("Unknown [E9]", mapping).valid)


if __name__ == "__main__":
    unittest.main()
