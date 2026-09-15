#!/usr/bin/env python3
"""Trusted post-seal evaluator wiring. CLI verifies seals only in Phase 5B.1."""
from __future__ import annotations
import argparse
import copy
import json
import os
from pathlib import Path
from phase5_common import exclusive_json, file_hash


def verify_seal(directory, *, separate_process=True):
    directory = Path(directory)
    seal = json.loads((directory / 'production_seal.json').read_text())
    if seal.get('schema') != 'phase5-production-seal-v0':
        raise ValueError('unsupported production seal')
    if separate_process and seal['producer_pid'] == os.getpid():
        raise RuntimeError('evaluation must use a separate process')
    for relative, expected in seal['files'].items():
        path = directory / relative
        if path.is_symlink() or not path.resolve().is_relative_to(directory.resolve()):
            raise ValueError('escaped seal path')
        if file_hash(path) != expected:
            raise ValueError('production seal hash mismatch: ' + relative)
    for qid in seal['query_ids']:
        for relative in (f'outputs/{qid}.json', f'attempts/{qid}/started.json', f'attempts/{qid}/terminal.json', f'{qid}.json', f'observations/{qid}.json'):
            if relative not in seal['files']:
                raise ValueError('incomplete production seal')
    return seal


def verify_primary_seals(directories):
    if set(directories) != {'R2', 'A1', 'A2'}:
        raise ValueError('all three primary productions must be sealed first')
    seals = {alias: verify_seal(path) for alias, path in directories.items()}
    from phase5_ablation_runner import CONFIG_HASHES
    for alias, seal in seals.items():
        if seal['variant'] != alias or seal['config_hash'] != CONFIG_HASHES[alias]:
            raise ValueError('variant seal mismatch')
    if len({s['query_hash'] for s in seals.values()}) != 1:
        raise ValueError('primary query sets differ')
    return seals


class DurableJudgeClient:
    """Preserve the existing evaluator's 3-call ceiling across process crashes.

    A cached successful response is replayed into the SAME frozen parser, in
    order. Invalid responses are replayed too and consume their original slot.
    An ambiguous request becomes an exception, never another transport attempt.
    """
    def __init__(self, client, directory):
        self.client, self.directory = client, Path(directory)
        self.index = 0

    def generate(self, prompt):
        from phase5_common import digest
        self.index += 1
        if self.index > 3:
            raise RuntimeError('total evaluator attempt ceiling reached')
        path = self.directory / str(self.index)
        request = path / 'request.json'
        response = path / 'response.json'
        if request.exists():
            if json.loads(request.read_text())['prompt_hash'] != digest(prompt):
                raise ValueError('evaluator prompt drift')
            if not response.exists():
                raise RuntimeError('ambiguous prior evaluator attempt')
            cached = json.loads(response.read_text())
            if cached['status'] == 'error':
                raise RuntimeError('prior evaluator transport error')
            return cached['raw']
        exclusive_json(request, {'prompt_hash': digest(prompt), 'status': 'started'})
        try:
            raw = self.client.generate(prompt)
        except Exception as exc:
            exclusive_json(response, {'status': 'error', 'type': type(exc).__name__})
            raise
        exclusive_json(response, {'status': 'completed', 'raw': raw})
        return raw


def evaluate_sealed(directories, alias, items, client, output):
    """Library wiring for 5B.2; caller loads trusted items only after seals verify."""
    seals = verify_primary_seals(directories)
    seal = seals[alias]
    if [i['query_id'] for i in items] != seal['query_ids']:
        raise ValueError('join order mismatch')
    from phase5_common import digest
    if digest([{'query_id': i['query_id'], 'query': i['query']} for i in items]) != seal['query_hash']:
        raise ValueError('join query text mismatch')
    from evaluate_agentic_rag import evaluate_record
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    # Serialize evaluator resumes so two processes cannot consume one slot twice.
    import fcntl
    with (output / 'evaluator.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        for item in items:
            target = output / (item['query_id'] + '.json')
            if target.exists():
                json.loads(target.read_text())  # malformed/partial results fail closed
                continue
            record = json.loads((Path(directories[alias]) / 'outputs' / target.name).read_text())
            if record['generation_error'] is not None:
                record.update(evaluation_error=None, answer_completeness=0.0, citation_completeness=0.0,
                              citation_correctness=None, groundedness=None, unsupported_claim_rate=None)
            else:
                judge = DurableJudgeClient(client, output / 'attempts' / item['query_id'])
                record = evaluate_record(item, copy.deepcopy(record), judge)
            exclusive_json(target, record)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verify-seals', nargs=3, type=Path, required=True, metavar=('R2', 'A1', 'A2'))
    args = parser.parse_args()
    verify_primary_seals(dict(zip(('R2', 'A1', 'A2'), args.verify_seals)))
    print('All primary production seals verified. No semantic evaluation executed.')


if __name__ == '__main__':
    main()
