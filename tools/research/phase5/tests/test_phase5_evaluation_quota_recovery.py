"""Offline quota-recovery controls. No real judge, HTTP, retrieval, or bootstrap."""
from __future__ import annotations
import copy
from datetime import datetime,timezone
import io
import json
from pathlib import Path
import socket
import sys
import tempfile
import unittest
from unittest.mock import patch
import urllib.error

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import phase5_evaluation_quota_recovery_v1 as q
from phase5_common import canonical,digest,exclusive_json,file_hash
from llm_client import OpenAICompatibleClient
from evaluate_standard_rag import judge_prompt,parse_judge
from citation_validator import validate_citations

NETWORK_BLOCKS=[]
def deny_network(event,args):
    if event.startswith('socket.') or event in ('urllib.Request','http.client.connect','http.client.send'):
        NETWORK_BLOCKS.append(event)
        raise RuntimeError('offline synthetic tests: network blocked')
sys.addaudithook(deny_network)

def slot(alias='R2',qid='eval021',complete=False):
    return dict(alias=alias,variant_id=q.VARIANTS[alias],query_id=qid,
        completion='LOCKED_VALID_V0' if complete else 'ELIGIBLE_EXHAUSTED_429',
        production_output_path='production.json',production_output_hash='a'*64,
        gold_query_binding_hash='b'*64,gold_sha256='c'*64,gold_item_sha256='d'*64,
        query_sha256='e'*64,prompt_sha256='f'*64,v0_evaluation_status='JUDGED' if complete else 'FAILED',
        v0_attempt_count=1 if complete else 3,v0_record_path='v0.json',v0_record_sha256='0'*64)

def quota(delay=None,*,header=None,message=None):
    details=[] if delay is None else [{'@type':'type.googleapis.com/google.rpc.RetryInfo','retryDelay':str(delay)+'s'}]
    error=dict(code=429,status='RESOURCE_EXHAUSTED',message=message or 'Synthetic quota failure',details=details)
    return q.quota_metadata(429,json.dumps({'error':error}),{'Retry-After':header} if header else {},1000)

def quota_outcome(delay=None):
    return dict(transport_status='provider_error',http_status=429,quota_metadata=quota(delay),
        response_hash='a'*64,parse_status='not_attempted',final_recovery_status='QUOTA_BLOCKED')

def invalid_outcome():
    return dict(transport_status='completed',http_status=200,quota_metadata=None,response_hash='b'*64,
                parse_status='invalid',final_recovery_status='TRANSPORT_ERROR',error_type='ValueError')

def successful_outcome(path):
    exclusive_json(path/'evaluation_record.json',{'synthetic_completion':True})
    return dict(transport_status='completed',http_status=200,quota_metadata=None,response_hash='c'*64,
                parse_status='valid',final_recovery_status='VALID_JUDGMENT',result_hash=file_hash(path/'evaluation_record.json'))

def synthetic_inputs(qid='eval021'):
    item=dict(query_id=qid,query='What synthetic registration condition applies?',answerability='answerable',
        required_points=[dict(point_id='P1',description='Synthetic registration is required.',importance='essential',supporting_chunk_ids=['synthetic-1'])])
    evidence=[dict(evidence_id='E1',chunk_id='synthetic-1',text='Synthetic registration is required.')]
    record=dict(query_id=qid,query=item['query'],generation_error=None,status='success',
        trace=dict(final_evidence=evidence,final_answer='Synthetic registration is required. [E1]',
                   citation_check=dict(cited_evidence_ids=['E1'])))
    raw=json.dumps(dict(points=[dict(point_id='P1',supported=True,citation_supported=True,supporting_evidence_ids=['E1'],reason='Synthetic match')],
        claim_count=1,grounded_claim_count=1,unsupported_claim_count=0,cited_claim_count=1,correctly_cited_claim_count=1,
        abstention_correct=None,abstention_hallucinated=False))
    s=slot(qid=qid)
    validation=validate_citations(record['trace']['final_answer'],{'E1':evidence[0]},['E1'])
    prompt=judge_prompt(item['query'],record['trace']['final_answer'],evidence,item['required_points'],validation.cited_evidence_ids,item['answerability'])
    s['prompt_sha256']=digest(prompt)
    return s,item,record,raw,prompt

class Clock:
    value=1000.
    def __call__(self):return self.value

class RecoveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Trusted offline inventory validation only, not semantic evaluation.
        cls.inventory=q.build_inventory()
        cls.before={p:file_hash(ROOT/p) for p in cls.inventory['original_evaluation_artifact_hashes']}

    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='phase5-quota-test-',dir='/tmp')
        self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name); self.clock=Clock(); self.calls=[]

    def scheduler(self,slots=None,outcomes=None,worker=None,verify=None):
        slots=[slot()] if slots is None else slots
        outcomes=iter([None] if outcomes is None else outcomes)
        def fake(s,path,*,resume=False):
            self.calls.append((s['alias'],s['query_id'],int(path.name),resume,self.clock()))
            value=next(outcomes)
            return successful_outcome(path) if value is None else value
        ledger=q.RecoveryLedger(self.root/'ledger',slots,'a'*64)
        return q.RecoveryScheduler(slots,ledger,worker or fake,verify or (lambda s:None),self.clock)

    def test_Q1_all_64_v0_valid_judgments_issue_zero_calls(self):
        slots=[s for s in self.inventory['slots'] if s['completion']=='LOCKED_VALID_V0']
        self.assertEqual(len(slots),64)
        scheduler=self.scheduler(slots=slots)
        scheduler.run(); scheduler.run()
        self.assertEqual(self.calls,[])
        with self.assertRaisesRegex(ValueError,'valid v0'):
            scheduler.ledger.start(slots[0],1,self.clock())

    def test_Q2_exact_29_eligible_transport_failures(self):
        eligible=[s for s in self.inventory['slots'] if s['completion']=='ELIGIBLE_EXHAUSTED_429']
        self.assertEqual(len(eligible),29)
        for a in q.VARIANTS:
            self.assertEqual([s['query_id'] for s in eligible if s['alias']==a],q.EXPECTED[a])
        self.assertTrue(all(s['v0_attempt_count']==3 for s in eligible))

    def test_Q3_first_valid_recovery_stops_all_further_attempts(self):
        scheduler=self.scheduler(outcomes=[invalid_outcome(),None])
        self.assertEqual(scheduler.run()['status'],'VALID_JUDGMENT')
        self.assertEqual([c[2] for c in self.calls],[1,2])
        self.scheduler().run()
        self.assertEqual(len(self.calls),2)

    def test_Q4_retry_info_blocks_immediate_retry_and_other_slots(self):
        slots=[slot(),slot(qid='eval022')]
        first=self.scheduler(slots,outcomes=[quota_outcome(10)])
        self.assertEqual(first.run()['status'],'QUOTA_BLOCKED')
        self.assertEqual(len(self.calls),1)
        self.assertFalse((self.root/'ledger/R2/eval022').exists())
        self.assertEqual(self.scheduler(slots).run()['status'],'QUOTA_BLOCKED')
        self.clock.value=1009.99
        self.assertEqual(self.scheduler(slots).run()['status'],'QUOTA_BLOCKED')
        self.assertEqual(len(self.calls),1)
        self.clock.value=1011
        self.assertEqual(self.scheduler(slots,outcomes=[None,None]).run()['status'],'VALID_JUDGMENT')
        self.assertEqual([c[2] for c in self.calls],[1,2,1])

    def test_Q5_no_retry_information_stops_entire_session(self):
        slots=[slot(),slot(qid='eval022')]
        self.scheduler(slots,outcomes=[quota_outcome()]).run()
        self.clock.value=999999
        self.assertEqual(self.scheduler(slots).run()['status'],'QUOTA_BLOCKED')
        self.assertEqual(len(self.calls),1)
        self.assertFalse((self.root/'ledger/R2/eval022').exists())

    def test_Q6_resume_never_resets_attempt_counter(self):
        failure=dict(transport_status='transport_error',http_status=None,quota_metadata=None,response_hash=None,
                     parse_status='not_attempted',final_recovery_status='TRANSPORT_ERROR')
        self.scheduler(outcomes=[failure]).run()
        self.scheduler().run()
        self.assertEqual([c[2] for c in self.calls],[1,2])
        self.assertTrue((self.root/'ledger/R2/eval021/1/receipt.json').exists())

    def test_Q7_attempt_four_rejected(self):
        scheduler=self.scheduler(outcomes=[invalid_outcome()]*3)
        self.assertEqual(scheduler.run()['status'],'RECOVERY_EXHAUSTED')
        self.assertEqual(self.scheduler().run()['status'],'RECOVERY_EXHAUSTED')
        self.assertEqual(len(self.calls),3)
        self.assertEqual(scheduler.ledger.state(slot())[1]['slot_status_after_attempt'],'RECOVERY_EXHAUSTED')
        with self.assertRaises(ValueError):scheduler.ledger.start(slot(),4,self.clock())

    def test_Q8_changed_production_output_hash_rejected(self):
        path=self.root/'production.json'; path.write_text('original')
        s=slot(); s['production_output_hash']=file_hash(path)
        path.write_text('changed')
        def verify(s):q.require(file_hash(path)==s['production_output_hash'],'production output hash changed')
        with self.assertRaisesRegex(ValueError,'production output hash'):
            self.scheduler([s],verify=verify).run()
        self.assertEqual(self.calls,[])

    def test_Q9_non429_and_unknown_v0_failure_rejected(self):
        variant=q.VARIANTS['R2']; directory=ROOT/q.V0/variant
        record=q.read_json(directory/'records/eval021.json')
        attempts=[a for a in q.jsonl(directory/'evaluation_attempts.jsonl') if a['query_id']=='eval021']
        responses=[{'status':'error','type':'RuntimeError'}]*3
        for message in ('LLM HTTP 503: unavailable','unknown failure','LLM HTTP 429: {"code":429}'):
            altered=copy.deepcopy(attempts); altered[0]['error']=message
            with self.assertRaises(ValueError):q.classify_v0(record,altered,responses)

    def test_Q10_frozen_order_and_reorder_rejection(self):
        slots=[s for s in self.inventory['slots'] if s['completion']=='ELIGIBLE_EXHAUSTED_429']
        self.scheduler(slots,outcomes=[None]*29).run()
        self.assertEqual([(a,qid) for a,qid,*_ in self.calls],[(a,qid) for a in q.VARIANTS for qid in q.EXPECTED[a]])
        with self.assertRaisesRegex(ValueError,'order'):
            q.RecoveryScheduler(list(reversed(slots)),q.RecoveryLedger(self.root/'other',list(reversed(slots)),'b'*64),None,None)

    def test_Q11_quality_files_and_metric_fields_cannot_influence_scheduler(self):
        quality=self.root/'contrast_R2_A1.json'; quality.write_text('{"answer_completeness":0.99}')
        scheduler=self.scheduler()
        original=scheduler.ledger.state
        def attempted_quality_read(s):
            quality.read_text()
            return original(s)
        with patch.object(scheduler.ledger,'state',attempted_quality_read),self.assertRaises(PermissionError):
            scheduler.run()
        self.assertEqual(self.calls,[])
        bad=slot(); bad['answer_completeness']=.9
        with self.assertRaisesRegex(ValueError,'completion-only'):
            q.RecoveryScheduler([bad],scheduler.ledger,None,None)

    def test_Q12_transport_request_matches_frozen_payload_bytes(self):
        client=OpenAICompatibleClient('gemini-3.5-flash-lite','https://synthetic.invalid/v1/','synthetic-only-secret')
        captured=[]
        class Response:
            def __enter__(self):return self
            def __exit__(self,*args):pass
            def read(self):return b'{"choices":[{"message":{"content":"synthetic raw"}}]}'
        def opener(request,timeout):
            captured.append((request.full_url,request.data,request.get_method(),dict(request.header_items()),timeout))
            return Response()
        prompt='Synthetic Unicode query: điều kiện\nReturn JSON.'
        with patch('urllib.request.urlopen',opener):client.generate(prompt)
        q.QuotaTransport(client,digest(client.base_url.strip()),opener=opener).generate(prompt)
        self.assertEqual(captured[0],captured[1])
        payload=json.loads(captured[1][1])
        self.assertEqual(payload['temperature'],0)
        self.assertEqual(set(payload),{'model','messages','temperature','response_format'})

    def test_Q13_frozen_parser_receives_response_unchanged(self):
        s,item,record,raw,prompt=synthetic_inputs()
        raw='```json\n'+raw+'\n```'
        calls=[]
        class Transport:
            def generate(self,p):calls.append(p); return raw
        worker=q.FrozenAttemptEvaluator(lambda slot:(item,record),Transport())
        parser_inputs=[]
        def parser(value,point_ids):parser_inputs.append(value); return parse_judge(value,point_ids)
        with patch('evaluate_agentic_rag.parse_judge',parser):
            self.scheduler([s],worker=worker).run()
        self.assertEqual(parser_inputs,[raw]); self.assertEqual(calls,[prompt])
        result=q.read_json(self.root/'ledger/R2/eval021/1/evaluation_record.json')
        self.assertEqual(result['trace'],record['trace'])

    def test_Q14_v0_paths_and_valid_judgments_cannot_be_overwritten(self):
        old=self.root/'old-v0'; old.mkdir(); (old/'evaluation.jsonl').write_text('existing valid judgment')
        before=(old/'evaluation.jsonl').read_bytes()
        with self.assertRaisesRegex(ValueError,'unbound/nonempty'):
            q.RecoveryLedger(old,[slot()],'a'*64)
        self.assertEqual((old/'evaluation.jsonl').read_bytes(),before)
        scheduler=self.scheduler(); scheduler.run()
        result=self.root/'ledger/R2/eval021/1/evaluation_record.json'
        with self.assertRaises(FileExistsError):exclusive_json(result,{'changed':True})
        self.assertEqual(len(self.calls),1)

    def test_Q15_original_v0_ledgers_and_artifacts_unchanged(self):
        for path,before in self.before.items():self.assertEqual(file_hash(ROOT/path),before,path)

    def test_Q16_crash_after_429_receipt_rebuilds_global_barrier(self):
        scheduler=self.scheduler(outcomes=[quota_outcome(20)])
        def crash(*args):raise RuntimeError('synthetic crash')
        with patch.object(scheduler.ledger,'stop_quota',crash),self.assertRaises(RuntimeError):scheduler.run()
        self.assertEqual(len(self.calls),1)
        self.assertEqual(self.scheduler().run()['status'],'QUOTA_BLOCKED')
        self.assertEqual(self.scheduler().run()['status'],'QUOTA_BLOCKED')
        self.assertEqual(len(self.calls),1)

    def test_Q17_ambiguous_started_attempt_never_resubmitted(self):
        s,item,record,raw,prompt=synthetic_inputs()
        class Transport:
            def generate(self,p):raise AssertionError('must never submit')
        scheduler=self.scheduler([s],worker=q.FrozenAttemptEvaluator(lambda slot:(item,record),Transport()))
        scheduler.ledger.start(s,1,self.clock())
        self.assertEqual(scheduler.run()['status'],'TRANSPORT_ERROR')
        self.assertEqual(scheduler.run()['status'],'TRANSPORT_ERROR')
        self.assertEqual(len(scheduler.ledger.state(s)[0]),1)

    def test_Q18_saved_valid_response_replayed_after_crash_without_call(self):
        s,item,record,raw,prompt=synthetic_inputs()
        class Transport:
            def generate(self,p):raise AssertionError('must replay persisted text')
        scheduler=self.scheduler([s],worker=q.FrozenAttemptEvaluator(lambda slot:(item,record),Transport()))
        path=scheduler.ledger.start(s,1,self.clock())
        exclusive_json(path/'wire_response.json',dict(transport_status='completed',raw=raw,response_hash=digest(raw),http_status=200,
            started_record_hash=file_hash(path/'started.json'),prompt_sha256=s['prompt_sha256']))
        self.assertEqual(scheduler.run()['status'],'VALID_JUDGMENT')
        self.assertEqual(scheduler.run()['status'],'VALID_JUDGMENT')
        self.assertEqual(len(scheduler.ledger.state(s)[0]),1)

    def test_Q19_explicit_retry_sources_maximum_and_no_guessed_window(self):
        body=json.dumps({'error':{'code':429,'status':'RESOURCE_EXHAUSTED','message':'Please retry in 3.5s.',
            'details':[{'@type':'type.googleapis.com/google.rpc.RetryInfo','retryDelay':'4s'},
                       {'@type':'type.googleapis.com/google.rpc.QuotaFailure','violations':[{
                           'quotaMetric':'synthetic_metric','quotaId':'synthetic_id','quotaDimensions':{'model':'synthetic'}}]}]}})
        m=q.quota_metadata(429,body,{'Retry-After':'5'},1000)
        self.assertEqual(m['reliable_retry_delay_seconds'],5)
        self.assertIsNone(m['quota_window']); self.assertEqual(len(m['retry_delay_evidence']),3)
        self.assertEqual(m['quota_violations'][0]['quotaId'],'synthetic_id')
        self.assertIsNone(quota(0)['reliable_retry_delay_seconds'])
        self.assertIsNone(quota(message='quota limit: 15')['reliable_retry_delay_seconds'])

    def test_Q20_unknown_delay_requires_bound_external_resume(self):
        self.scheduler(outcomes=[quota_outcome()]).run()
        block=self.root/'ledger/quota_stop_0001.json'
        with self.assertRaises(ValueError):self.scheduler().run(explicit_resume={'blocked_record_sha256':'bad','review_reference':'review'})
        auth={'blocked_record_sha256':file_hash(block),'review_reference':'synthetic external review'}
        self.assertEqual(self.scheduler().run(explicit_resume=auth)['status'],'VALID_JUDGMENT')
        self.assertEqual(self.scheduler().run()['status'],'VALID_JUDGMENT')
        self.assertEqual([x[2] for x in self.calls],[1,2])

    def test_Q21_synthetic_http429_metadata_no_credentials(self):
        client=OpenAICompatibleClient('gemini-3.5-flash-lite','https://synthetic.invalid/v1','secret-test-only')
        def opener(request,timeout):
            body=json.dumps({'error':{'code':429,'status':'RESOURCE_EXHAUSTED','message':'secret-test-only Please retry in 7s.'}}).encode()
            raise urllib.error.HTTPError(request.full_url,429,'quota',{'Retry-After':'9','Authorization':'never log'},io.BytesIO(body))
        with self.assertRaises(q.ProviderFailure) as caught:
            q.QuotaTransport(client,digest(client.base_url),opener=opener).generate('synthetic')
        serialized=json.dumps(caught.exception.metadata)
        self.assertNotIn(client.api_key,serialized); self.assertNotIn('Authorization',serialized)
        self.assertEqual(caught.exception.metadata['reliable_retry_delay_seconds'],9)

    def test_Q22_network_and_live_transport_guards(self):
        with self.assertRaisesRegex(RuntimeError,'network blocked'):socket.socket()
        client=OpenAICompatibleClient('gemini-3.5-flash-lite','https://synthetic.invalid/v1','synthetic')
        with self.assertRaisesRegex(ValueError,'later external execution authorization'):
            q.QuotaTransport(client,digest(client.base_url)).generate('synthetic')

    def test_Q23_endpoint_and_model_changes_rejected(self):
        client=OpenAICompatibleClient('gemini-3.5-flash-lite','https://synthetic.invalid/v1','synthetic')
        with self.assertRaises(ValueError):q.QuotaTransport(client,'bad')
        client.model='changed-model'
        with self.assertRaises(ValueError):q.QuotaTransport(client,digest(client.base_url))

    def test_Q24_frozen_invalid_parser_retries_only_in_recovery_budget(self):
        s,item,record,raw,prompt=synthetic_inputs(); responses=iter(['invalid JSON',raw]); sent=[]
        class Transport:
            def generate(self,p):sent.append(p); return next(responses)
        scheduler=self.scheduler([s],worker=q.FrozenAttemptEvaluator(lambda slot:(item,record),Transport()))
        self.assertEqual(scheduler.run()['status'],'VALID_JUDGMENT')
        self.assertEqual(len(sent),2)
        history,_=scheduler.ledger.state(s)
        self.assertEqual([h[2]['parse_status'] for h in history],['invalid','valid'])

    def test_Q25_ledger_counter_binding_and_symlink_rejected(self):
        scheduler=self.scheduler()
        with self.assertRaises(ValueError):q.RecoveryLedger(self.root/'ledger',[slot(qid='eval022')],'a'*64)
        target=self.root/'elsewhere'; target.mkdir()
        (self.root/'link').symlink_to(target)
        with self.assertRaises(ValueError):q.RecoveryLedger(self.root/'link',[slot()],'a'*64)
        bad=slot(qid='../escape')
        with self.assertRaises(ValueError):scheduler.ledger.start(bad,1,self.clock())

    def test_Q26_http_date_retry_after_honored(self):
        metadata=q.quota_metadata(429,'{}',{'Retry-After':'Wed, 09 Sep 2026 00:00:20 GMT',
            'Date':'Wed, 09 Sep 2026 00:00:00 GMT'},0)
        self.assertEqual(metadata['reliable_retry_delay_seconds'],20)

    def test_Q27_trusted_input_loader_checks_full_binding(self):
        s,item,record,raw,prompt=synthetic_inputs()
        exclusive_json(self.root/'production.json',record)
        exclusive_json(self.root/'v0.json',{'evaluation_status':'FAILED'})
        gold=self.root/'data/evaluation/generation/generation_eval_v1_verified.json'
        exclusive_json(gold,{'items':[item]})
        s.update(production_output_hash=file_hash(self.root/'production.json'),v0_record_sha256=file_hash(self.root/'v0.json'),
            gold_sha256=file_hash(gold),gold_item_sha256=digest(item),query_sha256=digest(item['query']))
        s['gold_query_binding_hash']=digest(dict(gold_sha256=s['gold_sha256'],query_id=s['query_id'],
            query_sha256=s['query_sha256'],gold_item_sha256=s['gold_item_sha256'],production_output_sha256=s['production_output_hash']))
        self.assertEqual(q.load_bound_inputs(self.root,s),(item,record))
        (self.root/'production.json').write_bytes(canonical(dict(record,query='changed')))
        with self.assertRaisesRegex(ValueError,'production output hash changed'):q.load_bound_inputs(self.root,s)

    def test_Q28_transport_mutation_rejected_before_submission(self):
        client=OpenAICompatibleClient('gemini-3.5-flash-lite','https://synthetic.invalid/v1','synthetic')
        transport=q.QuotaTransport(client,digest(client.base_url),opener=lambda *a,**kw:self.fail('must not send'))
        client.model='changed-after-construction'
        with self.assertRaisesRegex(ValueError,'settings changed'):transport.generate('synthetic')

    def test_Q29_direct_adapter_rejects_v0_success(self):
        worker=q.FrozenAttemptEvaluator(lambda s:self.fail('must not load inputs'),None)
        with self.assertRaisesRegex(ValueError,'locked v0 judgment'):
            worker(slot(complete=True),self.root/'attempt')

    def test_Q30_ledger_rejects_added_slots_and_unresolved_attempt_skip(self):
        scheduler=self.scheduler()
        with self.assertRaisesRegex(ValueError,'not authorized'):
            scheduler.ledger.start(slot(qid='eval022'),1,self.clock())
        scheduler.ledger.start(slot(),1,self.clock())
        with self.assertRaisesRegex(ValueError,'pending attempt'):
            scheduler.ledger.start(slot(),2,self.clock())
        with self.assertRaisesRegex(ValueError,'differs from durable ledger'):
            q.RecoveryScheduler([slot(qid='eval022')],scheduler.ledger,None,None)

    def test_Q31_unbound_existing_resume_ack_cannot_release_quota_stop(self):
        self.scheduler(outcomes=[quota_outcome()]).run()
        exclusive_json(self.root/'ledger/quota_stop_0001_resume_authorization.json',{'review_reference':'unbound'})
        with self.assertRaisesRegex(ValueError,'invalid durable external resume authorization'):
            self.scheduler().run()
        self.assertEqual(len(self.calls),1)

if __name__=='__main__':
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(RecoveryTests)
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    report=dict(status='PASS' if result.wasSuccessful() else 'FAIL',tests_run=result.testsRun,
        failures=len(result.failures),errors=len(result.errors),network_calls=0,gemini_api_calls=0,
        production_calls=0,real_semantic_evaluator_calls=0,synthetic_adapter_exercises=True,
        prevented_network_attempts=len(NETWORK_BLOCKS),network_guard_events=NETWORK_BLOCKS,
        source_hashes={p:file_hash(ROOT/p) for p in q.NEW_SOURCES})
    target=Path('/tmp/phase5b2er1-tests.json')
    target.write_bytes(canonical(report))
    print(json.dumps(report))
    sys.exit(0 if result.wasSuccessful() else 1)
