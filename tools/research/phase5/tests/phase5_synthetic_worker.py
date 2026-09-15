"""Fresh-process, offline synthetic harness. No benchmark inputs accepted."""
import json
import os
from pathlib import Path
import sys
from phase5_test_support import ROOT, Client, Pipeline, responses
from phase5_ablation_runner import RuntimeConfig, produce, runtime_allowlist
from phase5_common import digest, exclusive_json


def main():
    root = Path(sys.argv[1])
    rows = [{'query_id': 'synthetic-1', 'query': 'Synthetic registration question?'}]
    query_input = root / 'queries.json'
    exclusive_json(query_input, rows)
    for alias in ('R2', 'A1', 'A2'):
        output = root / alias
        output.mkdir()
        guard = runtime_allowlist(output, query_input, root / 'cache')
        # No test directory allowlist: fixtures are already loaded synthetic objects.
        p, c = Pipeline(), Client(responses(alias, incomplete=True))
        with guard:
            projected = json.loads(query_input.read_text())
            produce(projected, RuntimeConfig(alias), p, c, output, expected_hash=digest(rows), expected_count=1)
        exclusive_json(root / (alias + '-audit.json'), {'prompts': c.prompts, 'retrieval': p.calls, 'reads': guard.reads})
    print(json.dumps({'producer_pid': os.getpid(), 'network_calls': 0}))


if __name__ == '__main__':
    main()
