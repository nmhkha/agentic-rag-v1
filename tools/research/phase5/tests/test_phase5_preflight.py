import copy
import json
from pathlib import Path
import tempfile
import unittest
from phase5_test_support import *
from phase5_common import canonical, digest, validate_queries
from phase5_preflight import load_design, resolve_variant, validate_variant, materialize_variants, prepare_queries, integrity
from phase5_assets import inspect_snapshot, validate_environment
from phase5_ablation_runner import CONFIG_HASHES, RuntimeConfig


class ConfigTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.design = load_design()

    def test_design_hashes_and_integrity(self):
        self.assertEqual(len(integrity(self.design)), 248)

    def test_exact_variants_flags_hashes_and_materialization(self):
        with tempfile.TemporaryDirectory() as tmp:
            materialize_variants(tmp, self.design)
            for alias in CONFIG_HASHES:
                config = resolve_variant(alias)
                self.assertEqual(config, self.design['variant_manifests'][alias])
                self.assertEqual(config['ablation_flags'], RuntimeConfig(alias).flags)
                self.assertEqual(digest(config), CONFIG_HASHES[alias])
                self.assertEqual((Path(tmp) / alias / 'variant_manifest.json').read_bytes(), canonical(config))
            with self.assertRaises(FileExistsError):
                materialize_variants(tmp, self.design)

    def test_config_drift_rejected(self):
        for alias in CONFIG_HASHES:
            for key, value in {'top_k': 6, 'prompt_hash': 'wrong', 'llm_model': 'other', 'dense_depth': 21,
                'dense_batch_size': 5, 'max_llm_calls': 7, 'dense_revision': 'wrong', 'extra': True,
                'created_at': 'changed', 'llm_temperature': False}.items():
                with self.subTest(alias=alias, key=key):
                    config = resolve_variant(alias)
                    config[key] = value
                    with self.assertRaises(ValueError):
                        validate_variant(self.design, alias, config)
            config = resolve_variant(alias); config.pop('top_k')
            with self.assertRaises(ValueError):
                validate_variant(self.design, alias, config)
        for alias, flag in [('A1', 'enable_answer_revision'), ('A2', 'enable_expansion')]:
            config = resolve_variant(alias); config['ablation_flags'][flag] = True
            with self.assertRaises(ValueError):
                validate_variant(self.design, alias, config)
            config = resolve_variant(alias); config['ablation_flags']['enable_citation_revision'] = 1
            with self.assertRaises(ValueError):
                validate_variant(self.design, alias, config)

    def test_real_projection_deterministic_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / 'queries.json'
            result = prepare_queries(target)
            self.assertEqual(result['count'], 31)
            self.assertEqual(result['canonical_sha256'], self.design['query_input_schema']['canonical_sha256'])
            self.assertEqual([r['query_id'] for r in json.loads(target.read_text())], self.design['query_order'])
            prepare_queries(target)

    def test_l2_schema_duplicate_nested_modified_order(self):
        rows = [{'query_id': f's{i}', 'query': f'synthetic question {i}'} for i in range(31)]
        expected = digest(rows)
        validate_queries(rows, expected)
        variants = []
        bad = copy.deepcopy(rows); bad[0]['gold_chunk_ids'] = ['x']; variants.append(bad)
        bad = copy.deepcopy(rows); bad[0]['query'] = {'required_point_ids': ['x']}; variants.append(bad)
        bad = copy.deepcopy(rows); bad[0]['query'] = 'changed'; variants.append(bad)
        bad = copy.deepcopy(rows); bad[0].pop('query'); variants.append(bad)
        bad = copy.deepcopy(rows); bad[1] = bad[0]; variants.append(bad)
        bad = copy.deepcopy(rows); bad[1]['query'] = bad[0]['query']; variants.append(bad)
        variants += [rows[:-1], rows[::-1], {'items': rows}]
        for bad in variants:
            with self.assertRaises(ValueError):
                validate_queries(bad, expected)

    def test_environment_config_types(self):
        config = resolve_variant('R2')
        validate_environment(config)
        for key, value in [('device', 'cuda'), ('dense_dtype', 'float16'), ('reranker_dtype', 'float16'), ('reranker_batch_size', 8), ('dense_batch_size', 32), ('llm_model', 'other'), ('production_max_transport_attempts', 3), ('llm_timeout_seconds', 60.0)]:
            bad = copy.deepcopy(config); bad[key] = value
            with self.assertRaises(ValueError):
                validate_environment(bad)


class SnapshotTests(unittest.TestCase):
    def fixture(self, root):
        repo = Path(root) / 'models--synthetic--model'
        snap = repo / 'snapshots' / ('a' * 40)
        snap.mkdir(parents=True)
        for name in ('config.json', 'tokenizer_config.json', 'tokenizer.json', 'special_tokens_map.json'):
            (snap / name).write_text('{}')
        (snap / 'model.safetensors').write_bytes(b'synthetic weights')
        (repo / 'refs').mkdir(); (repo / 'refs/main').write_text('a' * 40)
        return snap, repo

    def test_model_and_tokenizer_snapshot_revision(self):
        with tempfile.TemporaryDirectory() as tmp:
            snap, repo = self.fixture(tmp)
            good = inspect_snapshot(tmp, 'synthetic/model', 'a'*40, require_main=True)
            self.assertTrue(good['model_pass']); self.assertTrue(good['tokenizer_pass'])
            self.assertFalse(inspect_snapshot(tmp, 'synthetic/model', 'b'*40)['model_pass'])
            (repo / 'refs/main').write_text('b'*40)
            self.assertFalse(inspect_snapshot(tmp, 'synthetic/model', 'a'*40, require_main=True)['model_pass'])

    def test_missing_tokenizer_or_weights_or_symlink_escape(self):
        for filename in ('tokenizer.json', 'model.safetensors'):
            with tempfile.TemporaryDirectory() as tmp:
                snap, repo = self.fixture(tmp)
                (snap / filename).unlink()
                result = inspect_snapshot(tmp, 'synthetic/model', 'a'*40)
                self.assertFalse(result['model_pass'])
                if filename == 'tokenizer.json':
                    self.assertFalse(result['tokenizer_pass'])
                outside = Path(tmp) / 'outside'; outside.write_bytes(b'synthetic')
                (snap / filename).symlink_to(outside)
                self.assertFalse(inspect_snapshot(tmp, 'synthetic/model', 'a'*40)['model_pass'])
