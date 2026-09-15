"""Offline corruption tests on disposable copies; never display answer content."""
from __future__ import annotations

import copy
import json
from pathlib import Path
import shutil
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from phase5_common import canonical, exclusive_json, file_hash
import phase5_durable_seal_v1 as durable
from phase5_seal_recovery_v1 import BASE, TRACE, VARIANTS, SOURCE_FILES, anchor_for, deny_network


class RecoveryCorruptionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.before = {alias: (ROOT / TRACE / variant / 'production_seal.json').read_bytes()
                      for alias, variant in VARIANTS.items()}
        cls.queries = durable.read_json(ROOT / BASE / 'query_inputs_v0.json')
        cls.baseline = {}
        for p in (ROOT / BASE).rglob('*'):
            if p.is_file():
                cls.baseline[p.relative_to(ROOT).as_posix()] = file_hash(p)

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='phase5b2r-test-', dir='/tmp')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.anchor = anchor_for(ROOT, 'R2', self.baseline)
        self.directory = self.root / self.anchor['directory']
        shutil.copytree(ROOT / self.anchor['directory'], self.directory,
                        ignore=shutil.ignore_patterns(durable.SUPPLEMENT))
        for entry in self.anchor['provenance_artifacts']:
            path = self.root / entry['path']
            path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / entry['path'], path)
        self.protocol_hash = 'a' * 64
        self.original_bytes = (self.directory / 'production_seal.json').read_bytes()
        self.seal = durable.build_supplement(self.directory, self.queries, self.anchor,
                                            self.protocol_hash, project_root=self.root)
        exclusive_json(self.directory / durable.SUPPLEMENT, self.seal)

    def verify(self):
        return durable.verify_pair(self.directory, self.queries, self.anchor,
                                   self.protocol_hash, project_root=self.root)

    def reject(self):
        with self.assertRaises((ValueError, OSError)):
            self.verify()

    def rewrite_copy_original(self, update):
        path = self.directory / 'production_seal.json'
        original = durable.read_json(path)
        update(original)
        path.write_bytes(canonical(original))
        self.anchor['original_seal_sha256'] = file_hash(path)
        return original

    def test_T1_deleted_output_journal_fails(self):
        (self.directory / 'production_outputs.jsonl').unlink()
        self.reject()

    def test_T2_changed_answer_byte_fails(self):
        path = self.directory / 'production_outputs.jsonl'
        data = path.read_bytes()
        marker = b'"final_answer":"'
        position = data.index(marker) + len(marker)
        # Exactly one byte of an answer string changes, without displaying it.
        changed = data[:position] + (b'X' if data[position:position + 1] != b'X' else b'Y') + data[position + 1:]
        self.assertEqual(sum(a != b for a, b in zip(data, changed)), 1)
        path.write_bytes(changed)
        self.reject()

    def test_T3_deleted_trace_fails(self):
        (self.directory / 'eval001.json').unlink()
        self.reject()

    def test_T4_deleted_observer_fails(self):
        (self.directory / 'observations/eval001.json').unlink()
        self.reject()

    def test_T5_changed_variant_manifest_fails(self):
        path = self.root / BASE / VARIANTS['R2'] / 'variant_manifest.json'
        path.write_bytes(path.read_bytes() + b' ')
        self.reject()

    def test_T6_arbitrary_missing_cache_file_fails_even_if_declared(self):
        relative = 'runtime_cache/tmpabcdefgh/important_model.bin'
        self.rewrite_copy_original(lambda seal: seal['files'].update({relative: durable.EPHEMERAL_SHA256}))
        self.reject()
        forged = dict(original_path=relative, original_expected_sha256=durable.EPHEMERAL_SHA256,
                      classification=durable.CLASSIFICATION, reason=durable.REASON)
        self.anchor['ephemeral_exclusions'] = [forged]
        self.reject()

    def test_T7_symlink_and_traversal_exclusions_fail(self):
        relative = self.anchor['ephemeral_exclusions'][0]['original_path']
        parent = (self.directory / relative).parent
        # A dangling symlink must fail even though the excluded file is missing.
        parent.symlink_to(self.root / 'nonexistent', target_is_directory=True)
        self.reject()
        parent.unlink()
        for unsafe in ('runtime_cache/../runtime_cache/tmpabcdefgh/_remote_module_non_scriptable.py',
                       '/runtime_cache/tmpabcdefgh/_remote_module_non_scriptable.py',
                       'runtime_cache//tmpabcdefgh/_remote_module_non_scriptable.py',
                       'runtime_cache/tmp*/_remote_module_non_scriptable.py'):
            with self.subTest(path=unsafe), self.assertRaises(ValueError):
                durable.exclusion(self.directory, unsafe, durable.EPHEMERAL_SHA256)
        parent.mkdir()
        (self.directory / relative).symlink_to(self.root / 'missing-target')
        self.reject()

    def test_T8_known_disappearance_requires_exact_declaration(self):
        self.assertEqual(self.verify()['completed'], 31)
        original = copy.deepcopy(self.seal)
        for key, value in [('classification', 'cache'), ('reason', 'ignore all cache'),
                           ('original_expected_sha256', '0' * 64), ('original_path', 'runtime_cache/**')]:
            forged = copy.deepcopy(original)
            forged['ephemeral_exclusions'][0][key] = value
            (self.directory / durable.SUPPLEMENT).write_bytes(canonical(forged))
            self.reject()
        forged = copy.deepcopy(original)
        forged['ephemeral_exclusions'] = []
        (self.directory / durable.SUPPLEMENT).write_bytes(canonical(forged))
        self.reject()

    def test_T9_original_seals_remain_byte_identical(self):
        self.verify()
        self.assertEqual((self.directory / 'production_seal.json').read_bytes(), self.original_bytes)
        for alias, original in self.before.items():
            self.assertEqual((ROOT / TRACE / VARIANTS[alias] / 'production_seal.json').read_bytes(), original)

    def test_changed_ledger_and_run_manifest_fail(self):
        for path in (self.directory / 'production_attempts.jsonl',
                     self.root / BASE / VARIANTS['R2'] / 'run_manifest.json'):
            original = path.read_bytes()
            path.write_bytes(original + b' ')
            self.reject()
            path.write_bytes(original)

    def test_changed_original_seal_fails(self):
        path = self.directory / 'production_seal.json'
        path.write_bytes(path.read_bytes() + b' ')
        self.reject()

    def test_second_missing_approved_pattern_is_not_silently_excluded(self):
        relative = 'runtime_cache/tmpabcdefgh/_remote_module_non_scriptable.py'
        self.rewrite_copy_original(lambda seal: seal['files'].update({relative: durable.EPHEMERAL_SHA256}))
        self.reject()

    def test_invalid_anchor_classification_and_hash_fail(self):
        original = copy.deepcopy(self.anchor)
        for key, value in [('classification', 'cache'), ('original_expected_sha256', '0' * 64)]:
            self.anchor = copy.deepcopy(original)
            self.anchor['ephemeral_exclusions'][0][key] = value
            self.reject()

    def test_unsealed_file_fails(self):
        (self.directory / 'runtime_cache/unlisted.bin').write_bytes(b'unknown artifact')
        self.reject()

    def test_surviving_cache_source_is_durable(self):
        path = self.directory / 'runtime_cache/modules/__init__.py'
        path.unlink()
        self.reject()

    def test_journal_reconciliation_independent_of_hashes(self):
        path = self.directory / 'production_outputs.jsonl'
        lines = path.read_bytes().splitlines(keepends=True)
        lines[0], lines[1] = lines[1], lines[0]
        path.write_bytes(b''.join(lines))
        original = self.rewrite_copy_original(lambda seal: seal['files'].update({path.name: file_hash(path)}))
        with self.assertRaisesRegex(ValueError, 'journal mismatch'):
            durable.reconcile(self.directory, original, self.queries)

    def test_observer_reconciliation_independent_of_hashes(self):
        path = self.directory / 'observations/eval001.json'
        observer = durable.read_json(path)
        observer['events'] = [e for e in observer['events'] if e['logical_call_type'] != 'llm']
        path.write_bytes(canonical(observer))
        original = durable.read_json(self.directory / 'production_seal.json')
        with self.assertRaisesRegex(ValueError, 'observer/trace LLM count mismatch'):
            durable.reconcile(self.directory, original, self.queries)

    def test_query_order_and_config_mismatch_fail(self):
        self.queries = list(reversed(type(self).queries))
        self.reject()
        self.queries = type(self).queries
        self.anchor['config_sha256'] = '0' * 64
        self.reject()

    def test_future_sealer_refuses_historical_run(self):
        with self.assertRaisesRegex(ValueError, 'existing/historical'):
            durable.seal_production_v1(self.directory, self.queries, SimpleNamespace(alias='R2'))
        self.assertEqual((self.directory / 'production_seal.json').read_bytes(), self.original_bytes)

    def prepare_future_copy(self):
        # Only remove seals from a disposable COPY; originals stay untouched.
        (self.directory / 'production_seal.json').unlink()
        (self.directory / durable.SUPPLEMENT).unlink()

    def test_future_sealer_roundtrip_and_unknown_cache_corruption(self):
        self.prepare_future_copy()
        cache = self.directory / 'runtime_cache/durable_cache.bin'
        cache.write_bytes(b'durable cache data')
        durable.seal_production_v1(self.directory, self.queries, SimpleNamespace(alias='R2'))
        result = durable.verify_future_seal(self.directory, self.queries, separate_process=False)
        self.assertEqual(result['completed'], 31)
        cache.unlink()
        with self.assertRaises((ValueError, OSError)):
            durable.verify_future_seal(self.directory, self.queries, separate_process=False)

    def test_future_ephemeral_provenance_survives_disappearance(self):
        self.prepare_future_copy()
        relative = self.anchor['ephemeral_exclusions'][0]['original_path']
        real_inventory, real_hash = durable.inventory, durable.file_hash
        # Simulate a process-live inventory entry through mocks. Never create,
        # reconstruct or import the missing PyTorch module, even in tests.
        def inventory(directory):
            return real_inventory(directory) | {relative}
        def hashed(path):
            return durable.EPHEMERAL_SHA256 if Path(path) == self.directory / relative else real_hash(path)
        with patch.object(durable, 'inventory', inventory), patch.object(durable, 'file_hash', hashed):
            durable.seal_production_v1(self.directory, self.queries, SimpleNamespace(alias='R2'))
        result = durable.verify_future_seal(self.directory, self.queries, separate_process=False)
        self.assertEqual(result['completed'], 31)
        seal = durable.read_json(self.directory / 'production_seal_v1.json')
        self.assertNotIn(relative, seal['files'])
        provenance = durable.read_json(self.directory / 'execution_cache_provenance_v1.json')
        self.assertEqual(provenance['ephemeral_artifacts'], self.anchor['ephemeral_exclusions'])


if __name__ == '__main__':
    sys.addaudithook(deny_network)
    destination = Path(sys.argv[1]) if len(sys.argv) == 2 else None
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(RecoveryCorruptionTests)
    names = [test.id() for test in suite]
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    evidence = dict(status='PASS' if result.wasSuccessful() else 'FAIL', tests_run=result.testsRun,
                    failures=len(result.failures), errors=len(result.errors), tests=names,
                    test_source_sha256=file_hash(__file__), synthetic_copies_only=True,
                    infrastructure_source_sha256={p: file_hash(ROOT / p) for p in SOURCE_FILES[:2]},
                    missing_module_recreated=False, network_calls=0, model_inference_calls=0,
                    production_reruns=0, semantic_evaluations=0)
    if destination:
        exclusive_json(destination, evidence)
    sys.exit(0 if result.wasSuccessful() else 1)
