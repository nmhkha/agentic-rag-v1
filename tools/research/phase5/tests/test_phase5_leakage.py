import ast
import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
from phase5_test_support import *
from phase5_isolation import ReadGuard
from phase5_analyze import verify_seal, verify_primary_seals, evaluate_sealed, DurableJudgeClient
from phase5_common import exclusive_json

SENTINEL = 'PHASE5_GOLD_SENTINEL_DO_NOT_LEAK'
FORBIDDEN = ('generation_eval_v1_verified', 'generation_eval_v1.json', 'retrieval_eval',
             'required_point_ids', 'gold_chunk_ids', 'failure_analysis', 'agentic_trace_analysis')


class LeakageTests(unittest.TestCase):
    def test_l1_recursive_production_source_import_closure(self):
        queue = ['phase5_ablation_runner']; seen = set()
        while queue:
            module = queue.pop()
            if module in seen:
                continue
            seen.add(module)
            self.assertFalse(module.startswith(('evaluate_', 'validate_generation_eval', 'phase5_preflight', 'phase5_analyze')))
            source = (ROOT / 'scripts' / (module + '.py')).read_text()
            for marker in FORBIDDEN:
                self.assertNotIn(marker, source, module)
            for node in ast.walk(ast.parse(source)):
                names = [node.module] if isinstance(node, ast.ImportFrom) else [a.name for a in node.names] if isinstance(node, ast.Import) else []
                for name in names:
                    if name and (ROOT / 'scripts' / (name.split('.')[0] + '.py')).is_file():
                        queue.append(name.split('.')[0])
        self.assertIn('agentic_rag', seen)
        self.assertIn('dense_baseline', seen)
        self.assertIn('phase5_observer', seen)

    def test_l3_direct_symlink_pathlib_builtin_os_open(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); allowed = root / 'allowed'; allowed.mkdir()
            forbidden = root / 'private'; forbidden.mkdir()
            targets = ['generation_eval_v1_verified.json', 'generation_eval_v1.json', 'retrieval_eval.jsonl',
                       'failure_analysis_points.jsonl', 'agentic_trace_analysis_v0.jsonl',
                       'standard_rag_eval_v0.jsonl', 'agentic_rag_eval_v1.jsonl', 'R1_trace.json']
            paths = []
            for name in targets:
                p = forbidden / name; p.write_text(SENTINEL)
                alias = allowed / name; alias.symlink_to(p)
                paths.extend([p, alias])
            safe = allowed / 'safe'; safe.write_text('synthetic')
            guard = ReadGuard(directories=[allowed])
            with guard:
                self.assertEqual(safe.read_text(), 'synthetic')
                for path in paths:
                    for reader in (lambda p: p.read_text(), lambda p: open(p).read(), lambda p: os.open(p, os.O_RDONLY)):
                        with self.assertRaises(PermissionError):
                            reader(path)
                with self.assertRaises(PermissionError):
                    import evaluate_hybrid

    def synthetic_process(self, root):
        env = {k: os.environ[k] for k in ('PATH', 'LANG') if k in os.environ}
        env.update(PYTHONDONTWRITEBYTECODE='1', HF_HUB_OFFLINE='1', TRANSFORMERS_OFFLINE='1')
        run = subprocess.run([sys.executable, '-B', str(ROOT / 'tests/phase5_synthetic_worker.py'), str(root)],
                             env=env, stdin=subprocess.DEVNULL, close_fds=True, capture_output=True, text=True)
        self.assertEqual(run.returncode, 0, run.stderr)
        return json.loads(run.stdout)

    def test_l4_sentinel_and_l5_without_gold_separate_evaluator(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            gold = root / 'unavailable-gold.json'; gold.write_text(SENTINEL)
            # The worker's allowlist cannot see this path; it is not in its argv/env.
            gold.chmod(0)
            run = self.synthetic_process(root)
            self.assertNotEqual(run['producer_pid'], os.getpid())
            for path in root.rglob('*.json'):
                if path != gold:
                    self.assertNotIn(SENTINEL, path.read_text())
            paths = {a: root / a for a in ('R2', 'A1', 'A2')}
            seals = verify_primary_seals(paths)
            self.assertEqual(set(seals), {'R2', 'A1', 'A2'})
            # Only now make evaluator references available, after all seals verify.
            gold.chmod(0o600)
            items = [{'query_id': 'synthetic-1', 'query': 'Synthetic registration question?',
                      'required_points': [{'point_id': 'synthetic-point', 'text': 'Synthetic registration rule 1', 'supporting_chunk_ids': ['synthetic-1']}]}]
            calls = []
            def fake_evaluate(item, record, judge):
                calls.append(item['required_points'][0]['point_id'])
                record['evaluation_error'] = None
                return record
            with patch('evaluate_agentic_rag.evaluate_record', fake_evaluate):
                evaluate_sealed(paths, 'R2', items, Client([]), root / 'evaluation')
                evaluate_sealed(paths, 'R2', items, Client([]), root / 'evaluation')
            self.assertEqual(calls, ['synthetic-point'])
            # Mutation invalidates the seal before any evaluator call.
            (root / 'R2/outputs/synthetic-1.json').write_text('{}')
            with self.assertRaises(ValueError):
                verify_primary_seals(paths)

    def test_unsealed_and_same_process_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(FileNotFoundError):
                verify_seal(tmp)
            exclusive_json(Path(tmp) / 'production_seal.json', {'schema': 'phase5-production-seal-v0', 'producer_pid': os.getpid()})
            with self.assertRaises(RuntimeError):
                verify_seal(tmp)
            with self.assertRaises(ValueError):
                verify_primary_seals({'R2': tmp})

    def test_evaluator_reuses_frozen_functions(self):
        import evaluate_agentic_rag as agentic
        import evaluate_standard_rag as standard
        import citation_validator
        for name in ('judge_prompt', 'parse_judge', 'point_audit'):
            self.assertIs(getattr(agentic, name), getattr(standard, name))
        self.assertIs(agentic.validate_citations, citation_validator.validate_citations)
        self.assertEqual(agentic.MAX_EVALUATION_ATTEMPTS, 3)

    def test_durable_evaluator_attempt_ceiling_and_replay(self):
        with tempfile.TemporaryDirectory() as tmp:
            client = Client(['invalid', RuntimeError('synthetic'), 'valid'])
            first = DurableJudgeClient(client, tmp)
            self.assertEqual(first.generate('prompt'), 'invalid')
            with self.assertRaises(RuntimeError): first.generate('prompt')
            self.assertEqual(first.generate('prompt'), 'valid')
            resumed = DurableJudgeClient(Client([]), tmp)
            self.assertEqual(resumed.generate('prompt'), 'invalid')
            with self.assertRaises(RuntimeError): resumed.generate('prompt')
            self.assertEqual(resumed.generate('prompt'), 'valid')
            with self.assertRaises(RuntimeError): resumed.generate('prompt')
            self.assertEqual(len(client.prompts), 3)

    def test_real_frozen_evaluator_wiring_with_synthetic_judge(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.synthetic_process(root)
            paths = {a: root / a for a in ('R2', 'A1', 'A2')}
            items = [{'query_id': 'synthetic-1', 'query': 'Synthetic registration question?',
                      'required_points': [{'point_id': 'synthetic-point', 'description': 'Synthetic registration rule 1',
                                           'importance': 'required', 'supporting_chunk_ids': ['synthetic-1']}]}]
            raw = json.dumps(dict(points=[dict(point_id='synthetic-point', supported=True, citation_supported=True,
                supporting_evidence_ids=['E1'], reason='synthetic')], claim_count=1, grounded_claim_count=1,
                unsupported_claim_count=0, cited_claim_count=1, correctly_cited_claim_count=1,
                abstention_correct=None, abstention_hallucinated=False))
            client = Client(['bad json', raw])
            evaluate_sealed(paths, 'R2', items, client, root / 'evaluation')
            row = json.loads((root / 'evaluation/synthetic-1.json').read_text())
            self.assertIsNone(row['evaluation_error'])
            self.assertEqual(row['evaluation_attempts'], 2)
            self.assertEqual(row['answer_completeness'], 1.0)
            self.assertEqual(client.prompts[0], client.prompts[1])
            evaluate_sealed(paths, 'R2', items, client, root / 'evaluation')
            self.assertEqual(len(client.prompts), 2)

    def test_preloaded_unapproved_module_rejected(self):
        from phase5_ablation_runner import runtime_allowlist
        import evaluate_agentic_rag
        with tempfile.TemporaryDirectory() as tmp:
            guard = runtime_allowlist(tmp, Path(tmp) / 'query.json', Path(tmp) / 'cache')
            with self.assertRaisesRegex(PermissionError, 'already imported'):
                with guard:
                    pass

    def test_worker_rejects_full_design_path_before_read(self):
        from phase5_ablation_runner import worker, VARIANT_IDS
        with patch('phase5_ablation_runner.file_hash') as reader:
            with self.assertRaises(ValueError):
                worker('R2', ROOT / 'data/evaluation/generation/phase5/query_inputs_v0.json',
                       ROOT / 'data/rag/traces/phase5' / VARIANT_IDS['R2'],
                       ROOT / 'data/evaluation/generation/phase5/phase5a_ablation_manifest_v0.json', 'fake')
            reader.assert_not_called()

    def test_network_socket_http_gemini_fail_immediately(self):
        import urllib.request
        from llm_client import OpenAICompatibleClient
        before = NETWORK['blocked_network_attempts']
        with self.assertRaises(PermissionError):
            with socket.socket() as s:
                s.connect(('127.0.0.1', 9))
        with self.assertRaises(PermissionError):
            urllib.request.urlopen('https://synthetic.invalid')
        with self.assertRaises(PermissionError):
            OpenAICompatibleClient('gemini-3.5-flash-lite', 'https://synthetic.invalid', 'synthetic-key').generate('synthetic guard probe')
        # This workspace may deny socket creation before a connect audit event.
        self.assertGreaterEqual(NETWORK['blocked_network_attempts'] - before, 2)
        self.assertEqual(NETWORK['network_calls'], 0)

    def test_hub_download_blocked_offline(self):
        from huggingface_hub import hf_hub_download
        from huggingface_hub.errors import LocalEntryNotFoundError
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(LocalEntryNotFoundError):
                hf_hub_download('synthetic-unavailable/phase5-test', 'config.json', cache_dir=tmp)
