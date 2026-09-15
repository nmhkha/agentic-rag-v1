#!/usr/bin/env python3
"""Run only offline Phase 5 acceptance tests and emit a durable test certificate."""
import argparse
import json
from pathlib import Path
import sys
import unittest
from phase5_test_support import ROOT, NETWORK
from phase5_common import exclusive_json, file_hash


def implementation_hashes():
    paths = sorted((ROOT / 'scripts').glob('phase5*.py')) + sorted((ROOT / 'tests').glob('*phase5*.py'))
    return {str(p.relative_to(ROOT)): file_hash(p) for p in paths}


class Result(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.successes = []

    def addSuccess(self, test):
        super().addSuccess(test)
        self.successes.append(test.id())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    before = implementation_hashes()
    suite = unittest.defaultTestLoader.discover(str(ROOT / 'tests'), pattern='test_phase5_*.py')
    result = unittest.TextTestRunner(verbosity=2, resultclass=Result).run(suite)
    after = implementation_hashes()
    data = dict(passed=result.wasSuccessful() and before == after, tests_run=result.testsRun,
                successes=result.successes, failures=[(t.id(), e) for t, e in result.failures + result.errors],
                implementation_hashes=after, implementation_unchanged=before == after,
                network_calls=NETWORK['network_calls'], blocked_network_probe_attempts=NETWORK['blocked_network_attempts'],
                gemini_api_calls=0, real_benchmark_production_queries=0, real_semantic_evaluations=0)
    exclusive_json(args.output, data)
    raise SystemExit(0 if data['passed'] else 1)


if __name__ == '__main__':
    main()
