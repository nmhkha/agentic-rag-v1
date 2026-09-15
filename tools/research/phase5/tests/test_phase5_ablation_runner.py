import copy
import json
from pathlib import Path
import tempfile
import unittest
from phase5_test_support import *
from agentic_rag import AgentState, AgenticRAGController, MAX_LLM_CALLS, record_execution_error, trace_for_state
from phase5_ablation_runner import AttemptLedger, CONFIG_HASHES, RuntimeConfig, produce, run_query
from phase5_common import digest, exclusive_json
from phase5_observer import Observer, ObservedClient


class BehaviorTests(unittest.TestCase):
    def run_variant(self, alias, **kwargs):
        p, c = Pipeline(), Client(responses(alias, **kwargs))
        s, trace, side = run_query('Synthetic registration question?', RuntimeConfig(alias), p, c)
        return s, trace, side, p, c

    def test_r2_direct_parity_all_paths(self):
        for kwargs in ({}, {'expansion': True}, {'incomplete': True}, {'invalid': True}, {'semantic': True}, {'expansion': True, 'incomplete': True, 'invalid': True}):
            with self.subTest(kwargs=kwargs):
                p, c = Pipeline(), Client(responses(**kwargs))
                direct = AgenticRAGController(p, c).run('Synthetic registration question?')
                state, trace, _, wp, wc = self.run_variant('R2', **kwargs)
                self.assertEqual(normalize(trace_for_state(direct, c)), normalize(trace))
                self.assertEqual(c.prompts, wc.prompts)
                self.assertEqual((p.calls, p.merges), (wp.calls, wp.merges))
                self.assertEqual(normalize(direct.to_dict()), normalize(state.to_dict()))

    def test_r2_error_parity(self):
        for rs in ([RuntimeError('synthetic')], ['bad json'], [coverage(), answer(), 'bad json'], [coverage(), answer(), completeness(False), RuntimeError('synthetic')]):
            p, c = Pipeline(), Client(rs)
            state = AgentState(query='synthetic')
            try:
                AgenticRAGController(p, c).run('synthetic', state=state)
            except Exception as exc:
                record_execution_error(state, exc)
            ws, trace, side = run_query('synthetic', RuntimeConfig('R2'), Pipeline(), Client(rs))
            self.assertEqual(normalize(trace_for_state(state, c)), normalize(trace))

    def test_a1_no_answer_revision_no_compensation_citation_preserved(self):
        full = self.run_variant('R2', incomplete=True, invalid=True)
        s, _, side, p, c = self.run_variant('A1', incomplete=True, invalid=True)
        stages = [call['stage'] for call in s.llm_calls]
        self.assertEqual(stages, ['coverage_check', 'answer_generation', 'completeness_check', 'citation_revision'])
        self.assertIn('citation_check', s.transitions)
        self.assertIn('citation_recheck', s.transitions)
        self.assertTrue(s.citation_revision_used)
        self.assertIn(s.draft_answer, c.prompts[-1])
        self.assertEqual(len(full[4].prompts) - len(c.prompts), 2)
        self.assertEqual(p.calls, full[3].calls)
        self.assertTrue(side['metadata']['answer_revision_would_have_triggered'])
        self.assertTrue(side['metadata']['answer_revision_blocked_by_ablation'])
        self.assertFalse(full[2]['metadata']['first_completeness_check']['complete'])
        self.assertTrue(full[0].completeness_check.complete)

    def test_a2_no_expansion_no_compensation_revision_preserved(self):
        full = self.run_variant('R2', expansion=True, incomplete=True)
        s, _, side, p, c = self.run_variant('A2', expansion=True, incomplete=True)
        self.assertEqual(p.calls, [['Synthetic registration question?', 5, True]])
        self.assertEqual(p.merges, [])
        self.assertEqual(s.sub_queries, [])
        self.assertEqual(s.current_evidence, s.initial_evidence)
        self.assertEqual(len(s.current_evidence), 5)
        self.assertTrue(s.missing_aspects)
        self.assertTrue(s.revision_used)
        self.assertEqual(len(full[3].calls), 2)
        self.assertEqual(len(full[3].merges), 1)
        self.assertTrue(side['metadata']['expansion_would_have_triggered'])
        self.assertTrue(side['metadata']['expansion_blocked_by_ablation'])

    def test_empty_missing_aspects(self):
        for alias in CONFIG_HASHES:
            s, _, side = run_query('synthetic', RuntimeConfig(alias), Pipeline(), Client([coverage(False), answer(), completeness()]))
            self.assertFalse(side['metadata']['expansion_would_have_triggered'])
            self.assertEqual(side['metadata']['expansion_reason'], 'missing_aspects_empty')
            self.assertEqual(s.final_status, 'insufficient_evidence')

    def test_citation_semantic_gate_and_budget_all_variants(self):
        for alias in CONFIG_HASHES:
            s, _, side, p, c = self.run_variant(alias, semantic=True)
            self.assertTrue(s.citation_check.alignment_checked)
            self.assertTrue(s.citation_revision_used)
            self.assertEqual(s.citation_check.alignment_method, 'structured_llm_with_revision')
            self.assertEqual(len(c.prompts), 4)
            s, trace, side, _, c = self.run_variant(alias, expansion=True, incomplete=True, invalid=True)
            self.assertLessEqual(len(c.prompts), 6)
            self.assertEqual(trace['budgets']['max_llm_calls'], 6)
            self.assertEqual(len([e for e in side['events'] if e['logical_call_type'] == 'llm']), len(c.prompts))
        self.assertEqual(MAX_LLM_CALLS, 6)

    def test_null_on_unreached_or_failed_check(self):
        for rs, fail in (([], True), ([RuntimeError('synthetic')], False), (['malformed'], False), ([coverage(), answer(), 'bad completeness'], False)):
            s, _, side = run_query('synthetic', RuntimeConfig('A1'), Pipeline(fail), Client(rs))
            self.assertIsNone(side['metadata']['answer_revision_would_have_triggered'])
            if len(rs) < 3:
                self.assertIsNone(side['metadata']['expansion_would_have_triggered'])
            self.assertEqual(s.final_status, 'execution_error')
        self.assertEqual(side['events'][-1]['status'], 'success')  # transport success, parser failure retained in metadata
        self.assertEqual(side['metadata']['error_type'], 'ValueError')

    def test_observer_identity_error_no_retries_redaction(self):
        state = AgentState(query='synthetic')
        state.transitions.append('coverage_check')
        raw = 'Authorization: Bearer secret-token api_key="secret-key"'
        c = Client([raw, RuntimeError('Authorization: private')])
        observer = Observer(state, secrets=('secret-token', 'secret-key'))
        client = ObservedClient(c, observer)
        self.assertIs(client.generate('prompt'), raw)
        with self.assertRaises(RuntimeError):
            client.generate('prompt')
        logged = json.dumps(observer.events)
        for secret in ('secret-token', 'secret-key', 'private'):
            self.assertNotIn(secret, logged)
        self.assertEqual(len(c.prompts), 2)
        self.assertEqual(observer.events[0]['response_hash'], digest(raw))
        self.assertEqual(observer.events[1]['status'], 'error')
        self.assertEqual(observer.events[0]['provider_internal_retries'], 'unknown')

    def test_controller_input_rejects_design_and_records(self):
        with self.assertRaises(TypeError):
            run_query({'query': 'synthetic'}, RuntimeConfig('R2'), Pipeline(), Client([]))
        with self.assertRaises(TypeError):
            run_query('synthetic', {'ablation_flags': {}}, Pipeline(), Client([]))


class LedgerTests(unittest.TestCase):
    def test_lifecycle_exclusive_and_ambiguous(self):
        with tempfile.TemporaryDirectory() as tmp:
            ledger = AttemptLedger(tmp)
            self.assertEqual(ledger.status('q1'), 'never_started')
            ledger.start('q1')
            self.assertEqual(ledger.status('q1'), 'ambiguous')
            with self.assertRaises(FileExistsError):
                ledger.start('q1')
            ledger.finish('q1', 'completed', 'hash')
            self.assertEqual(ledger.status('q1'), 'completed')
            with self.assertRaises(FileExistsError):
                ledger.finish('q1', 'error', 'hash')
            ledger.start('q2'); ledger.finish('q2', 'error', 'hash')
            self.assertEqual(ledger.status('q2'), 'error')
            ledger.path('q3').mkdir()
            self.assertEqual(ledger.status('q3'), 'ambiguous')

    def test_resume_never_started_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp)
            rows = [{'query_id': 'q1', 'query': 'synthetic one'}, {'query_id': 'q2', 'query': 'synthetic two'}]
            # Simulate an interrupted worker after a durable error result for q1.
            ledger = AttemptLedger(out / 'attempts')
            ledger.start('q1')
            exclusive_json(out / 'outputs/q1.json', {'status': 'execution_error'})
            exclusive_json(out / 'q1.json', {'status': 'execution_error'})
            exclusive_json(out / 'observations/q1.json', {'events': []})
            from phase5_common import file_hash
            ledger.finish('q1', 'error', file_hash(out / 'outputs/q1.json'))
            c = Client(responses())
            produce(rows, RuntimeConfig('R2'), Pipeline(), c, out, expected_hash=digest(rows), expected_count=2)
            self.assertEqual(len(c.prompts), 3)
            self.assertTrue(all('synthetic one' not in p for p in c.prompts))
            with self.assertRaises(FileExistsError):
                produce(rows, RuntimeConfig('R2'), Pipeline(), c, out, expected_hash=digest(rows), expected_count=2)

    def test_ambiguous_resume_rejected_before_calls(self):
        with tempfile.TemporaryDirectory() as tmp:
            rows = [{'query_id': 'q1', 'query': 'synthetic'}]
            AttemptLedger(Path(tmp) / 'attempts').start('q1')
            c = Client([])
            with self.assertRaisesRegex(RuntimeError, 'ambiguous'):
                produce(rows, RuntimeConfig('R2'), Pipeline(), c, tmp, expected_hash=digest(rows), expected_count=1)
            self.assertEqual(c.prompts, [])


class EdgeGateTests(unittest.TestCase):
    def test_observer_redacts_structured_auth(self):
        from phase5_observer import redact
        raw = json.dumps({'Authorization': 'Bearer hidden-auth', 'api_key': 'hidden-key',
                          'nested': {'password': 'hidden-password'}})
        output = redact(raw)
        for value in ('hidden-auth', 'hidden-key', 'hidden-password'):
            self.assertNotIn(value, output)

    def test_actual_http_attempt_event_is_separate_from_logical_call(self):
        # Emit the audited submission event without constructing a request or socket.
        # A standalone child has only the observer hook; the suite blocks transport.
        import subprocess, sys
        source = '''
import sys
from agentic_rag import AgentState
from phase5_observer import Observer
state=AgentState(query='synthetic')
o=Observer(state)
def fake_submission():
    sys.audit('urllib.Request', 'synthetic', None, {}, 'POST')
    return 'synthetic response'
o.call('llm', 'synthetic prompt', fake_submission)
assert len(o.events)==1 and o.events[0]['observable_http_attempts']==1
assert o.events[0]['provider_internal_retries']=='unknown'
'''
        # No transport exists in the child; no-network hook installs after observer
        # so the probe is observable and still immediately rejected.
        source = source.replace("o.call('llm', 'synthetic prompt', fake_submission)", "from phase5_isolation import block_network\nblock_network()\ntry:\n    o.call('llm', 'synthetic prompt', fake_submission)\nexcept PermissionError:\n    pass")
        run = subprocess.run([sys.executable, '-B', '-c', source], env={'PYTHONPATH': str(ROOT / 'scripts'),
            'PYTHONDONTWRITEBYTECODE': '1'}, capture_output=True, text=True, stdin=subprocess.DEVNULL, close_fds=True)
        self.assertEqual(run.returncode, 0, run.stderr)

    def test_failed_revision_retains_eligibility_but_zero_completed_count(self):
        s, _, side = run_query('synthetic', RuntimeConfig('R2'), Pipeline(),
            Client([coverage(), answer(), completeness(False), RuntimeError('synthetic')]))
        self.assertTrue(side['metadata']['answer_revision_would_have_triggered'])
        self.assertTrue(side['metadata']['revision_attempted'])
        self.assertEqual(side['metadata']['revision_count'], 0)
        self.assertEqual(side['events'][-1]['status'], 'error')
        self.assertEqual(len(s.llm_calls), 4)

    def test_r2_six_call_budget_no_extra_semantic_call(self):
        rs = [coverage(), answer(), completeness(False), answer(), completeness(),
              json.dumps(dict(valid=True, errors=[], reason='synthetic', revised_answer=None))]
        # The sixth call is the unchanged semantic gate after answer revision.
        rs[3] = answer('Unrelated astronomy assertion [E1]')
        s, _, side = run_query('synthetic', RuntimeConfig('R2'), Pipeline(), Client(rs))
        self.assertEqual(len(s.llm_calls), 6)
        self.assertTrue(side['metadata']['llm_budget_exhausted'])
        self.assertEqual(s.llm_calls[-1]['stage'], 'semantic_citation_alignment')

    def test_resume_rejects_variant_or_query_drift_and_orphan_outputs(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp)
            rows = [{'query_id': 'q1', 'query': 'synthetic'}]
            exclusive_json(out / 'run_binding.json', {'variant': 'R2', 'config_hash': CONFIG_HASHES['R2'], 'query_hash': digest(rows)})
            with self.assertRaises(ValueError):
                produce(rows, RuntimeConfig('A1'), Pipeline(), Client([]), out, expected_hash=digest(rows), expected_count=1)
            exclusive_json(out / 'outputs/q1.json', {})
            with self.assertRaisesRegex(RuntimeError, 'orphan'):
                produce(rows, RuntimeConfig('R2'), Pipeline(), Client([]), out, expected_hash=digest(rows), expected_count=1)
