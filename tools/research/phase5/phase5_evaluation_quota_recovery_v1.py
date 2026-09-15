"""Versioned quota recovery infrastructure. CLI is strictly offline; never judges."""
from __future__ import annotations
import argparse
import copy
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
import fcntl
import hashlib
import json
import math
import os
from pathlib import Path
import re
import sys
import time
import urllib.error
import urllib.request

from phase5_common import canonical, digest, exclusive_json, exclusive_bytes, file_hash
from phase5_durable_seal_v1 import read_json, require, safe_path
from phase5_isolation import ReadGuard

ROOT = Path(__file__).resolve().parents[1]
BASE = 'data/evaluation/generation/phase5'
V0 = BASE + '/phase5b2e_v0'
VERSION = 'phase5b2e-quota-recovery-v1'
MANIFEST = BASE + '/phase5b2er1_quota_recovery_manifest_v0.json'
SPEC = BASE + '/phase5b2er1_quota_recovery_spec_v0.md'
TESTS = BASE + '/phase5b2er1_quota_recovery_tests_v0.json'
INTEGRITY = BASE + '/phase5b2er1_integrity_v0.json'
REPORT = BASE + '/phase5b2er1_console_v0.txt'
RECOVERY_ROOT = BASE + '/phase5b2er2_v1'
PRODUCTION_ANCHOR = '60f2c25b82082e41d466439afa0d93106484ca8fb4cdd41bbdb35cd1f83282bc'
V0_ANCHOR = '073e6a5ed1b1759d11afce596dce7af4bf6dec5390f693a089a354e2be9ca53c'
VARIANTS = {'R2':'full-agentic-replication','A1':'agentic-v1-no-answer-revision',
            'A2':'agentic-v1-no-evidence-expansion'}
EXPECTED = {'R2':['eval021','eval022','eval023','eval024','eval025','eval026','eval027','eval028'],
            'A1':['eval014','eval016','eval019','eval020','eval022','eval023','eval024','eval025','eval026'],
            'A2':['eval015','eval016','eval017','eval018','eval019','eval020','eval022','eval023','eval024','eval025','eval026','eval027']}
MAX_RECOVERY_ATTEMPTS_PER_ELIGIBLE_SLOT = 3
FROZEN_SOURCES = ['scripts/evaluate_agentic_rag.py','scripts/evaluate_standard_rag.py',
    'scripts/citation_validator.py','scripts/llm_client.py','scripts/evidence_formatter.py',
    'scripts/phase5_analyze.py']
NEW_SOURCES = ['scripts/phase5_evaluation_quota_recovery_v1.py','tests/test_phase5_evaluation_quota_recovery.py']

def offline_guard(event,args):
    if event.startswith('socket.') or event in ('urllib.Request','http.client.connect','http.client.send'):
        raise RuntimeError('Phase 5B.2-E-R1 forbids network/API activity')

def utc(epoch=None):
    return datetime.fromtimestamp(time.time() if epoch is None else epoch,timezone.utc).isoformat()

def jsonl(path):
    return [json.loads(line) for line in Path(path).read_text().splitlines() if line]

def finite_delay(value):
    try:
        result=float(value)
        return result if math.isfinite(result) and result>0 else None
    except (ValueError,TypeError):
        return None

def quota_metadata(status, body, headers=None, received_at=None, *, legacy=False):
    """Extract supplied evidence only. No quota-tier/window inference."""
    received_at=time.time() if received_at is None else received_at
    headers={k.lower():v for k,v in (headers or {}).items() if k.lower() in ('retry-after','date')}
    try:
        parsed=json.loads(body)
        if isinstance(parsed,list):
            parsed=parsed[0] if len(parsed)==1 else {}
        error=parsed.get('error',{}) if isinstance(parsed,dict) else {}
    except (ValueError,TypeError):
        error={}
    def scalar(pattern):
        match=re.search(pattern,body)
        return match.group(1) if match else None
    message=error.get('message')
    if not isinstance(message,str):
        token=scalar(r'"message"\s*:\s*("(?:[^"\\]|\\.)*")')
        message=json.loads(token) if token else None
    code=error.get('code')
    if code is None:
        value=scalar(r'"code"\s*:\s*(\d+)')
        code=int(value) if value else None
    provider_status=error.get('status') or scalar(r'"status"\s*:\s*"([A-Z_]+)"')
    violations=[]; retry_info=[]; candidates=[]
    details=error.get('details',[])
    for detail in details if isinstance(details,list) else []:
        if not isinstance(detail,dict):
            continue
        if detail.get('@type','').endswith('google.rpc.QuotaFailure'):
            for v in detail.get('violations',[]):
                if isinstance(v,dict):
                    violations.append({k:v.get(k) for k in ('quotaMetric','quotaId','quotaDimensions','quotaValue','subject','description')})
        if detail.get('@type','').endswith('google.rpc.RetryInfo'):
            value=detail.get('retryDelay')
            retry_info.append(value)
            match=re.fullmatch(r'(\d+(?:\.\d+)?)s',value) if isinstance(value,str) else None
            delay=finite_delay(match.group(1)) if match else None
            if delay is not None:
                candidates.append(dict(source='RetryInfo.retryDelay',seconds=delay))
    retry_after=headers.get('retry-after')
    if retry_after is not None:
        delay=finite_delay(retry_after) if re.fullmatch(r'\d+',retry_after.strip()) else None
        if delay is None:
            try:
                date=parsedate_to_datetime(retry_after)
                require(date.tzinfo is not None,'Retry-After date without timezone')
                if 'date' in headers:
                    server_date=parsedate_to_datetime(headers['date'])
                    require(server_date.tzinfo is not None,'Response Date without timezone')
                    baseline=server_date.timestamp()
                else:
                    baseline=received_at
                delay=finite_delay(date.timestamp()-baseline)
            except (ValueError,TypeError,KeyError,OverflowError):
                delay=None
        if delay is not None:
            candidates.append(dict(source='Retry-After',seconds=delay))
    retry_message=None
    if message:
        match=re.search(r'Please retry in (\d+(?:\.\d+)?)s\.',message)
        if match:
            retry_message=finite_delay(match.group(1))
            if retry_message is not None:
                candidates.append(dict(source='explicit provider message',seconds=retry_message))
    # For 429 only; unrelated body strings can never enable quota retries.
    reliable=max((x['seconds'] for x in candidates),default=None) if status==429 else None
    metric_match=re.search(r'Quota exceeded for metric:\s*([^,\s]+)',message or '')
    model_match=re.search(r'model:\s*([^\s\\]+)',message or '')
    limit_match=re.search(r'limit:\s*(\d+)',message or '')
    return dict(http_status=status,provider_error_code=code,provider_status=provider_status,
        quota_violations=violations,quota_metric_from_message=metric_match.group(1) if metric_match else None,
        reported_limit_from_message=int(limit_match.group(1)) if limit_match else None,
        reported_model_from_message=model_match.group(1) if model_match else None,
        quota_window=None,quota_window_inferred=False,retry_after=retry_after,retry_info=retry_info,
        message_retry_delay_seconds=retry_message,provider_message=message,
        reliable_retry_delay_seconds=reliable,retry_delay_evidence=candidates,
        received_at=utc(received_at),legacy_truncated_body=legacy,
        missing_metadata=['Retry-After header','structured RetryInfo','quota ID/dimensions'] if legacy else [])

def classify_v0(envelope, attempts, responses):
    """Completion/transport state only; no quality metric is consulted."""
    require(envelope.get('generation_error') is None,'production error')
    require(len(attempts)==len(responses)==envelope['evaluation_attempts'],'v0 attempt count mismatch')
    require([a['attempt'] for a in attempts]==list(range(1,len(attempts)+1)), 'v0 attempt order mismatch')
    require(all(not a['replay'] for a in attempts),'unexpected v0 replay')
    accepted=[i for i,a in enumerate(attempts) if a['status']=='valid_parsed_judgment']
    if envelope.get('evaluation_error') is None or envelope.get('evaluation_status')=='JUDGED' or 'judge' in envelope:
        require(envelope.get('evaluation_error') is None and envelope.get('evaluation_status')=='JUDGED'
                and isinstance(envelope.get('judge'),dict) and accepted==[len(attempts)-1]
                and responses[-1].get('status')=='completed','inconsistent completed v0 judgment; never recover')
        return 'LOCKED_VALID_V0'
    require(envelope.get('evaluation_status')=='FAILED' and envelope.get('evaluation_error')
            and not accepted and len(attempts)==3,'v0 not exhausted failure')
    for a,r in zip(attempts,responses):
        require(a['status']=='transport_error' and a.get('error_type')=='RuntimeError'
                and r=={'status':'error','type':'RuntimeError'},'non-transport v0 failure')
        msg=a.get('error','')
        require(msg.startswith('LLM HTTP 429: '),'non-429 v0 failure')
        metadata=quota_metadata(429,msg.removeprefix('LLM HTTP 429: '),received_at=0,legacy=True)
        require(metadata['provider_error_code']==429 and metadata['provider_status']=='RESOURCE_EXHAUSTED',
                'unknown v0 provider failure class')
    return 'ELIGIBLE_EXHAUSTED_429'

def build_inventory(root=ROOT, *, check_report=True):
    """Trusted offline projector. Scheduler only receives sanitized completion slots."""
    root=Path(root)
    require(file_hash(root/V0/'provenance.json')==V0_ANCHOR,'v0 provenance trust anchor mismatch')
    provenance=read_json(root/V0/'provenance.json')
    for name,expected in provenance['evaluation_artifacts'].items():
        require(file_hash(root/name)==expected,'v0 evidence changed: '+name)
    projection=read_json(root/BASE/'query_inputs_v0.json')
    gold_path='data/evaluation/generation/generation_eval_v1_verified.json'
    gold_hash=file_hash(root/gold_path)
    require(gold_hash==provenance['gold_sha256'],'gold drift')
    items=read_json(root/gold_path)['items']
    require([{'query_id':i['query_id'],'query':i['query']} for i in items]==projection,'gold/query binding mismatch')
    source_hashes={p:file_hash(root/p) for p in FROZEN_SOURCES}
    require(source_hashes==provenance['evaluator_sources'],'frozen evaluator source mismatch')
    slots=[]; evidence=[]; summary={}
    for alias,variant in VARIANTS.items():
        directory=root/V0/variant
        ledger=jsonl(directory/'evaluation_attempts.jsonl')
        envelopes=jsonl(directory/'evaluation.jsonl')
        require(len(envelopes)==31 and [e['query_id'] for e in envelopes]==[q['query_id'] for q in projection],'v0 envelope order/count')
        actual=[]; locked=0
        for item,envelope in zip(items,envelopes):
            qid=item['query_id']
            require(envelope['query']==item['query'],'v0 query text mismatch')
            record_path=directory/'records'/(qid+'.json')
            require(read_json(record_path)==envelope,'v0 envelope/record disagreement')
            attempts=[a for a in ledger if a['query_id']==qid]
            responses=[]
            for a in attempts:
                path=directory/'attempts'/qid/str(a['attempt'])
                request=read_json(path/'request.json')
                require(a['variant']==alias and request['prompt_hash']==a['prompt_sha256'],'v0 prompt binding mismatch')
                response=read_json(path/'response.json'); responses.append(response)
                if a['status']=='transport_error':
                    md=quota_metadata(429,a['error'].removeprefix('LLM HTTP 429: '),
                                      received_at=datetime.fromisoformat(a['ended_utc']).timestamp(),legacy=True)
                    evidence.append(dict(alias=alias,variant_id=variant,query_id=qid,v0_attempt_index=a['attempt'],
                        ledger_path=str((directory/'evaluation_attempts.jsonl').relative_to(root)),
                        error_text_sha256=digest(a['error']),metadata=md))
            require(len({a['prompt_sha256'] for a in attempts})==1,'v0 prompt drift between retries')
            status=classify_v0(envelope,attempts,responses)
            production_path='data/rag/traces/phase5/'+variant+'/outputs/'+qid+'.json'
            production=read_json(root/production_path)
            production_hash=file_hash(root/production_path)
            require(production_hash==provenance['production_outputs'][alias][qid]
                    and production['generation_error'] is None and production['trace']==envelope['trace'], 'production output drift')
            binding=dict(gold_sha256=gold_hash,query_id=qid,query_sha256=digest(item['query']),
                         gold_item_sha256=digest(item),production_output_sha256=production_hash)
            slots.append(dict(alias=alias,variant_id=variant,query_id=qid,completion=status,
                production_output_path=production_path,production_output_hash=production_hash,
                gold_query_binding_hash=digest(binding),gold_sha256=gold_hash,gold_item_sha256=digest(item),
                query_sha256=digest(item['query']),prompt_sha256=attempts[0]['prompt_sha256'],
                v0_evaluation_status=envelope['evaluation_status'],v0_attempt_count=len(attempts),
                v0_record_path=str(record_path.relative_to(root)),v0_record_sha256=file_hash(record_path)))
            if status=='LOCKED_VALID_V0':
                locked+=1
            else:
                actual.append(qid)
        require(actual==EXPECTED[alias], 'eligible slot mismatch: '+alias)
        summary[alias]=dict(completed=locked,eligible=len(actual),v0_attempt_count=len(ledger))
    require([summary[a]['completed'] for a in VARIANTS]==[23,22,19],'completed count mismatch')
    if check_report:
        report=(root/BASE/'phase5b_evaluation_report_v0.md').read_text()
        for alias in VARIANTS:
            match=re.search(r'^- '+alias+r' failed query IDs: (.+)$',report,re.M)
            require(match is not None and re.findall(r'`(eval\w+)`',match.group(1))==EXPECTED[alias], 'historical report/ledger ID mismatch')
            require(re.search(r'\| '+alias+r' \| '+str(summary[alias]['completed'])+r'/31 \| '+str(len(EXPECTED[alias]))+r' \|',report) is not None,'historical report/ledger count mismatch')
    return dict(slots=slots,summary=summary,stored_429_evidence=evidence,
                original_evaluation_artifact_hashes={**provenance['evaluation_artifacts'],
                    V0+'/provenance.json':V0_ANCHOR},frozen_evaluator_hashes=source_hashes,gold_sha256=gold_hash,
                frozen_endpoint=read_json(root/BASE/'phase5b1_preflight_manifest_v0.json')['endpoint'])

SLOT_KEYS={'alias','variant_id','query_id','completion','production_output_path','production_output_hash',
    'gold_query_binding_hash','gold_sha256','gold_item_sha256','query_sha256','prompt_sha256',
    'v0_evaluation_status','v0_attempt_count','v0_record_path','v0_record_sha256'}

class RecoveryLedger:
    """Exclusive, fsynced numbered records; existing events are never rewritten."""
    def __init__(self,directory,slots,protocol_hash):
        self.directory=Path(directory).absolute()
        self.slots_hash=digest(slots)
        self.slot_bindings={(s['alias'],s['query_id']):digest(s) for s in slots}
        require(self.directory.resolve()==self.directory,'symlink recovery root')
        self.directory.mkdir(parents=True,exist_ok=True)
        binding=dict(protocol=VERSION,protocol_sha256=protocol_hash,slots_sha256=digest(slots),max_attempts=3)
        path=self.directory/'protocol_binding.json'
        if path.exists():
            require(read_json(path)==binding,'recovery ledger binding changed')
        else:
            require(not list(self.directory.iterdir()),'unbound/nonempty recovery directory')
            exclusive_json(path,binding)

    def guard(self):
        return ReadGuard(directories=[self.directory],writable=[self.directory])

    def slot_dir(self,slot):
        require(self.slot_bindings.get((slot['alias'],slot['query_id']))==digest(slot),'slot not authorized by immutable ledger binding')
        return safe_path(self.directory,slot['alias']+'/'+slot['query_id'])

    def state(self,slot):
        path=self.slot_dir(slot)
        if not path.exists():
            return [],None
        entries=sorted(path.iterdir(),key=lambda p:p.name)
        require(all(p.is_dir() and p.name in ('1','2','3') and not p.is_symlink() for p in entries), 'unknown recovery attempt or attempt 4')
        require([p.name for p in entries]==[str(i) for i in range(1,len(entries)+1)], 'recovery counter gap/reset')
        history=[]
        for p in entries:
            start=read_json(p/'started.json')
            require(start['slot_binding']==digest(slot) and start['recovery_attempt_index']==int(p.name),'attempt slot mismatch')
            receipt=read_json(p/'receipt.json') if (p/'receipt.json').exists() else None
            require(receipt is not None or p==entries[-1],'unfinished request before later attempt')
            if receipt:
                require(receipt['started_record_hash']==file_hash(p/'started.json'),'receipt binding mismatch')
                require(receipt['recovery_attempt_index']==int(p.name),'receipt index mismatch')
                if receipt.get('wire_record_hash'):
                    require(file_hash(p/'wire_response.json')==receipt['wire_record_hash'],'saved transport response changed')
                if receipt.get('result_hash'):
                    require(file_hash(p/'evaluation_record.json')==receipt['result_hash'],'valid recovery judgment changed')
                if receipt['parse_status']=='valid':
                    require(p==entries[-1], 'request after a valid recovery judgment')
            history.append((p,start,receipt))
        return history,(history[-1][2] if history else None)

    def start(self,slot,index,now):
        require(slot['completion']=='ELIGIBLE_EXHAUSTED_429','valid v0 judgment cannot start recovery')
        history,last=self.state(slot)
        require(not history or last is not None,'pending attempt must be resolved before another reservation')
        require(not last or last['parse_status']!='valid','valid recovery judgment protected')
        require(index==len(history)+1 and 1<=index<=3,'recovery attempt budget/counter violation')
        path=self.slot_dir(slot)/str(index)
        exclusive_json(path/'started.json',dict(protocol=VERSION,slot_binding=digest(slot),variant_id=slot['variant_id'],
            query_id=slot['query_id'],production_output_hash=slot['production_output_hash'],
            gold_query_binding_hash=slot['gold_query_binding_hash'],v0_evaluation_status=slot['v0_evaluation_status'],
            v0_attempt_count=slot['v0_attempt_count'],recovery_attempt_index=index,started_at=utc(now),
            final_recovery_status='STARTED'))
        return path

    def finish(self,path,index,outcome,now):
        allowed={'transport_status','http_status','quota_metadata','response_hash','parse_status','error_type','error_message',
                 'result_hash','final_recovery_status','ambiguous_transport','wire_record_hash'}
        require(set(outcome)<=allowed,'quality/unrecognized field returned to scheduler')
        require(outcome['final_recovery_status'] in ('VALID_JUDGMENT','QUOTA_BLOCKED','TRANSPORT_ERROR'), 'invalid attempt outcome')
        require(outcome['parse_status'] in ('valid','invalid','not_attempted'),'invalid parse status')
        require((outcome['final_recovery_status']=='VALID_JUDGMENT') == (outcome['parse_status']=='valid' and bool(outcome.get('result_hash'))), 'completion receipt inconsistency')
        value=dict(outcome,recovery_attempt_index=index,ended_at=utc(now),started_record_hash=file_hash(path/'started.json'),
            slot_status_after_attempt='RECOVERY_EXHAUSTED' if index==3 and outcome['parse_status']!='valid'
                                      else outcome['final_recovery_status'])
        exclusive_json(path/'receipt.json',value)
        return value

    def blocks(self):
        return sorted(p for p in self.directory.glob('quota_stop_*.json') if re.fullmatch(r'quota_stop_\d{4}\.json',p.name))

    def stop_quota(self,receipt,now):
        md=receipt.get('quota_metadata') or {}
        delay=md.get('reliable_retry_delay_seconds')
        # Deadline is based on receipt handling time, conservatively after response arrival.
        exclusive_json(self.directory/f'quota_stop_{len(self.blocks())+1:04d}.json',dict(
            final_recovery_status='QUOTA_BLOCKED',received_at=utc(now),receipt_sha256=digest(receipt),
            not_before_epoch=math.nextafter(now+delay,math.inf) if delay is not None else None,
            retry_delay_seconds=delay,requires_external_resume_authorization=delay is None))

class RecoveryScheduler:
    """Quality-blind control component: sanitized slots and completion receipts only."""
    def __init__(self,slots,ledger,worker,verify_slot,clock=time.time):
        require(all(set(s)==SLOT_KEYS for s in slots),'scheduler accepts completion-only slot schema')
        require(digest(slots)==ledger.slots_hash,'scheduler plan differs from durable ledger binding')
        require(len({(s['alias'],s['query_id']) for s in slots})==len(slots),'duplicate recovery slots')
        require(all(s['alias'] in VARIANTS and s['variant_id']==VARIANTS[s['alias']]
                    and s['completion'] in ('LOCKED_VALID_V0','ELIGIBLE_EXHAUSTED_429') for s in slots),'unknown slot state/variant')
        order=[(list(VARIANTS).index(s['alias']),s['query_id']) for s in slots]
        require(order==sorted(order),'recovery order must match variant and original query order')
        self.slots=copy.deepcopy(slots); self.ledger=ledger; self.worker=worker
        self.verify_slot=verify_slot; self.clock=clock

    def run(self, *, explicit_resume=None):
        """429 always ends a session; a later invocation must satisfy the global barrier."""
        with (self.ledger.directory/'session.lock').open('a') as lock:
            fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
            with self.ledger.guard():
                # Recover a crash between a 429 receipt and its global stop event.
                bound={read_json(p)['receipt_sha256'] for p in self.ledger.blocks()}
                for slot in self.slots:
                    if slot['completion']!='ELIGIBLE_EXHAUSTED_429':
                        continue
                    history,_=self.ledger.state(slot)
                    for _,_,receipt in history:
                        if receipt and receipt['final_recovery_status']=='QUOTA_BLOCKED' and digest(receipt) not in bound:
                            self.ledger.stop_quota(receipt,self.clock())
                            return dict(status='QUOTA_BLOCKED',reason='Recovered global quota barrier after interrupted receipt commit')
                blocks=self.ledger.blocks()
                if blocks:
                    path=blocks[-1]; block=read_json(path)
                    deadline=block['not_before_epoch']
                    if deadline is not None and self.clock()<deadline:
                        return dict(status='QUOTA_BLOCKED',not_before_epoch=deadline)
                    if deadline is None:
                        ack=path.with_name(path.stem+'_resume_authorization.json')
                        if not ack.exists():
                            if not explicit_resume:
                                return dict(status='QUOTA_BLOCKED',reason='No reliable delay; explicit external resume authorization required')
                            require(set(explicit_resume)=={'blocked_record_sha256','review_reference'} and
                                    explicit_resume['blocked_record_sha256']==file_hash(path) and
                                    isinstance(explicit_resume['review_reference'],str) and explicit_resume['review_reference'].strip(),
                                    'resume authorization must bind exact quota stop and external review')
                            exclusive_json(ack,dict(explicit_resume,authorized_at=utc(self.clock())))
                        recorded=read_json(ack)
                        require(recorded.get('blocked_record_sha256')==file_hash(path)
                                and isinstance(recorded.get('review_reference'),str) and recorded['review_reference'].strip()
                                and isinstance(recorded.get('authorized_at'),str),'invalid durable external resume authorization')
                todo=[s for s in self.slots if s['completion']=='ELIGIBLE_EXHAUSTED_429']
            exhausted=[]
            for slot in todo:
                # Trusted verifier/worker run outside the scheduler read allowlist.
                self.verify_slot(slot)
                while True:
                    with self.ledger.guard():
                        history,last=self.ledger.state(slot)
                        if last and last['parse_status']=='valid':
                            if last['final_recovery_status']!='VALID_JUDGMENT':
                                return dict(status='TRANSPORT_ERROR',reason='Valid response requires offline finalization; never request again')
                            break
                        if last and last.get('ambiguous_transport'):
                            return dict(status='TRANSPORT_ERROR',reason='Ambiguous prior request; no automatic resubmission')
                        pending=bool(history and last is None)
                        if not pending and len(history)>=3:
                            exhausted.append((slot['variant_id'],slot['query_id']))
                            break
                        index=len(history) if pending else len(history)+1
                        path=history[-1][0] if pending else self.ledger.start(slot,index,self.clock())
                    outcome=self.worker(slot,path,resume=pending)
                    with self.ledger.guard():
                        receipt=self.ledger.finish(path,index,outcome,self.clock())
                        if receipt['final_recovery_status']=='QUOTA_BLOCKED':
                            self.ledger.stop_quota(receipt,self.clock())
                            return dict(status='QUOTA_BLOCKED',slot=[slot['variant_id'],slot['query_id']],attempt=index)
                        if receipt['final_recovery_status']=='TRANSPORT_ERROR' and receipt['parse_status']!='invalid':
                            return dict(status='TRANSPORT_ERROR',slot=[slot['variant_id'],slot['query_id']],attempt=index)
            return dict(status='RECOVERY_EXHAUSTED' if exhausted else 'VALID_JUDGMENT',exhausted_slots=exhausted)

class ProviderFailure(Exception):
    def __init__(self,metadata,response_hash,error_type='HTTPError'):
        self.metadata=metadata; self.response_hash=response_hash; self.error_type=error_type
        super().__init__('Provider transport failure')

class QuotaTransport:
    """Frozen request bytes; extra response metadata, no hidden retries or pacing."""
    def __init__(self,client,endpoint_hash,*,opener=None,real_requests_authorized=False):
        require(client.model=='gemini-3.5-flash-lite' and client.timeout==120.0,'frozen client setting drift')
        require(digest(client.base_url.strip())==endpoint_hash,'frozen endpoint drift')
        self.client=client; self.opener=opener; self.real_requests_authorized=real_requests_authorized
        self.endpoint_hash=endpoint_hash

    def generate(self,prompt):
        require(self.client.model=='gemini-3.5-flash-lite' and self.client.timeout==120.0
                and digest(self.client.base_url.strip())==self.endpoint_hash,'frozen transport settings changed')
        if self.opener is None:
            require(self.real_requests_authorized,'Real recovery requests require later external execution authorization')
        endpoint=self.client.base_url.rstrip('/')
        if not endpoint.endswith('/chat/completions'):
            endpoint+='/chat/completions'
        body=json.dumps({'model':self.client.model,'messages':[{'role':'user','content':prompt}],
                         'temperature':0,'response_format':{'type':'json_object'}}).encode('utf-8')
        request=urllib.request.Request(endpoint,data=body,method='POST',headers={
            'Authorization':f'Bearer {self.client.api_key}','Content-Type':'application/json'})
        try:
            with (self.opener or urllib.request.urlopen)(request,timeout=self.client.timeout) as response:
                payload=json.loads(response.read().decode('utf-8'))
        except urllib.error.HTTPError as exc:
            data=exc.read(); text=data.decode('utf-8',errors='replace').replace(self.client.api_key,'[REDACTED]')
            metadata=quota_metadata(exc.code,text,dict(exc.headers or {}))
            raise ProviderFailure(metadata,hashlib.sha256(data).hexdigest()) from None
        return str(payload['choices'][0]['message']['content'])

class AttemptBoundary(BaseException):
    """Escapes the unchanged evaluator's immediate retry loop; no scoring override."""

class FrozenAttemptEvaluator:
    """Trusted worker, deliberately separate from quality-blind scheduling.

    The unchanged evaluate_record sees exactly one transport response per durable
    attempt. Its next generate (only after a frozen failure) yields control back
    to the transport scheduler. Stored responses replay without another request.
    """
    def __init__(self,load_inputs,transport):
        self.load_inputs=load_inputs; self.transport=transport

    def __call__(self,slot,path,*,resume=False):
        require(slot['completion']=='ELIGIBLE_EXHAUSTED_429','locked v0 judgment cannot enter recovery evaluator')
        from evaluate_agentic_rag import evaluate_record
        from evaluate_standard_rag import parse_judge
        item,production=self.load_inputs(slot)
        wire=path/'wire_response.json'
        if resume and not wire.exists():
            return dict(transport_status='ambiguous',http_status=None,quota_metadata=None,response_hash=None,
                        parse_status='not_attempted',final_recovery_status='TRANSPORT_ERROR',ambiguous_transport=True)
        state={'calls':0,'raw':None,'parsed':False,'parse_error':None,'wire':None}
        def generate(prompt):
            require(digest(prompt)==slot['prompt_sha256'],'frozen judge prompt drift')
            state['calls']+=1
            if state['calls']>1:
                raise AttemptBoundary()
            if wire.exists():
                value=read_json(wire)
                require(value['started_record_hash']==file_hash(path/'started.json') and
                        value['prompt_sha256']==slot['prompt_sha256'],'saved response belongs to different attempt/prompt')
                if value['transport_status']=='completed':
                    require(digest(value['raw'])==value['response_hash'],'cached response text changed')
            else:
                try:
                    raw=self.transport.generate(prompt)
                    value=dict(transport_status='completed',raw=raw,response_hash=digest(raw),http_status=200)
                except ProviderFailure as exc:
                    value=dict(transport_status='provider_error',quota_metadata=exc.metadata,
                               response_hash=exc.response_hash,http_status=exc.metadata['http_status'])
                except Exception as exc:
                    # No arbitrary exception body/credential serialization.
                    value=dict(transport_status='transport_error',http_status=None,response_hash=None,error_type=type(exc).__name__)
                value.update(started_record_hash=file_hash(path/'started.json'),prompt_sha256=slot['prompt_sha256'])
                exclusive_json(wire,value)
            state['wire']=value
            if value['transport_status']!='completed':
                raise AttemptBoundary()
            raw=value['raw']; state['raw']=raw
            try:
                parse_judge(raw,[p['point_id'] for p in item['required_points']])
                state['parsed']=True
            except Exception as exc:
                state['parse_error']=type(exc).__name__
            return raw
        client=type('OneDurableResponse',(),{'generate':staticmethod(generate)})()
        result=None
        try:
            result=evaluate_record(item,copy.deepcopy(production),client)
        except AttemptBoundary:
            pass
        value=state['wire']
        require(value is not None,'failure before any bound evaluator request')
        outcome=dict(transport_status=value['transport_status'],http_status=value['http_status'],
            quota_metadata=value.get('quota_metadata'),response_hash=value['response_hash'],
            wire_record_hash=file_hash(wire),
            parse_status='valid' if state['parsed'] else 'invalid' if state['raw'] is not None else 'not_attempted',
            final_recovery_status='TRANSPORT_ERROR')
        if value['http_status']==429:
            outcome['final_recovery_status']='QUOTA_BLOCKED'
        elif result and result.get('evaluation_error') is None:
            target=path/'evaluation_record.json'
            if target.exists():
                require(read_json(target)==result,'cached recovery judgment cannot change')
            else:
                exclusive_json(target,result)
            outcome.update(final_recovery_status='VALID_JUDGMENT',result_hash=file_hash(target))
        elif state['parse_error']:
            outcome['error_type']=state['parse_error']
        else:
            outcome['error_type']=value.get('error_type') or 'EvaluationFinalizationError'
        return outcome

def load_bound_inputs(root,slot):
    root=Path(root)
    require(slot['completion']=='ELIGIBLE_EXHAUSTED_429','locked v0 judgment cannot load for recovery')
    path=root/slot['production_output_path']
    require(file_hash(path)==slot['production_output_hash'],'production output hash changed')
    require(file_hash(root/slot['v0_record_path'])==slot['v0_record_sha256'],'v0 completion evidence changed')
    gold=root/'data/evaluation/generation/generation_eval_v1_verified.json'
    require(file_hash(gold)==slot['gold_sha256'],'gold changed')
    items=[i for i in read_json(gold)['items'] if i['query_id']==slot['query_id']]
    require(len(items)==1 and digest(items[0])==slot['gold_item_sha256'],'gold item binding mismatch')
    item=items[0]; production=read_json(path)
    require(production['generation_error'] is None and production['query']==item['query']
            and production['query_id']==item['query_id'] and digest(item['query'])==slot['query_sha256'],'production query binding mismatch')
    binding=dict(gold_sha256=slot['gold_sha256'],query_id=slot['query_id'],query_sha256=slot['query_sha256'],
                 gold_item_sha256=slot['gold_item_sha256'],production_output_sha256=slot['production_output_hash'])
    require(digest(binding)==slot['gold_query_binding_hash'],'gold/query/production binding changed')
    return item,production

def verify_manifest(root,manifest_hash):
    root=Path(root)
    require(file_hash(root/MANIFEST)==manifest_hash,'quota recovery manifest trust anchor mismatch')
    manifest=read_json(root/MANIFEST)
    for group in ('historical_file_hashes','infrastructure_hashes','artifact_hashes'):
        for name,expected in manifest[group].items():
            require(file_hash(root/name)==expected,'frozen amendment drift: '+name)
    from phase5_seal_recovery_v1 import verify
    verify(root,PRODUCTION_ANCHOR)
    inventory=build_inventory(root)
    require(inventory['slots']==manifest['slots'],'frozen quota slot inventory changed')
    require(manifest['eligible_slot_count']==29 and manifest['completed_v0_judgment_count']==64
            and manifest['recovery_protocol_version']==VERSION,'invalid frozen quota plan')
    return manifest

def make_reviewed_session(root,manifest_hash,*,transport,external_review_reference):
    """Future Phase 5B.2-E-R2 library entry; intentionally absent from R1 CLI."""
    require(isinstance(external_review_reference,str) and external_review_reference.strip(),'external R2 review required')
    manifest=verify_manifest(root,manifest_hash)
    require(isinstance(transport,QuotaTransport) and transport.opener is None
            and transport.real_requests_authorized and transport.endpoint_hash==manifest['frozen_endpoint']['base_url_canonical_sha256'],
            'reviewed live session requires explicitly authorized frozen quota transport')
    root=Path(root)
    ledger=RecoveryLedger(root/RECOVERY_ROOT,manifest['slots'],manifest_hash)
    loader=lambda slot:load_bound_inputs(root,slot)
    worker=FrozenAttemptEvaluator(loader,transport)
    return RecoveryScheduler(manifest['slots'],ledger,worker,lambda slot:loader(slot))

def freeze(root,before_path,test_path):
    root=Path(root)
    before=read_json(before_path)
    for name,expected in before.items():
        require(file_hash(root/name)==expected,'historical drift: '+name)
    from phase5_seal_recovery_v1 import verify
    verify(root,PRODUCTION_ANCHOR)
    inventory=build_inventory(root)
    tests=read_json(test_path)
    require(tests['status']=='PASS' and tests['tests_run']>=15 and tests['failures']==tests['errors']==0,'offline tests failed')
    require(tests['source_hashes']=={p:file_hash(root/p) for p in NEW_SOURCES},'source changed since tests')
    targets=[MANIFEST,TESTS,INTEGRITY,REPORT]
    require(all(not (root/p).exists() for p in targets),'quota amendment already frozen; never overwrite')
    require((root/SPEC).is_file(),'specification missing')
    exclusive_json(root/TESTS,tests)
    after={p:file_hash(root/p) for p in before}
    require(after==before,'historical files modified')
    exclusive_json(root/INTEGRITY,dict(status='PASS',file_count=len(before),
        files={p:dict(before_sha256=h,after_sha256=after[p]) for p,h in before.items()},
        production_seals='PASS',v0_evaluator_evidence='PASS',gold_runtime_prompt_evaluator='PASS'))
    console='\n'.join(['Phase 5B.2-E-R1 status: PASS','','Existing valid judgments:','64/93','','Recovery eligible:',
        '29/93','','R2 eligible:','8','','A1 eligible:','9','','A2 eligible:','12','','Semantic methodology:',
        'UNCHANGED','','Recovery max attempts/slot:','3','','HTTP 429 policy:',
        'Stop the session. Persist a global not-before deadline from explicit provider retry evidence; no automatic retry before it.',
        'Without a reliable delay: QUOTA_BLOCKED, no further request; a future session requires explicit externally reviewed resume authorization.',
        'No inferred quota window, guessed interval, hidden retries, or quality-dependent pacing.',
        '','Valid judgments protected:','PASS','','Quality-blind scheduler:','PASS','','Resume ledger:','PASS','',
        'Synthetic tests:',f"{tests['tests_run']}/{tests['tests_run']} PASS",'',
        'Frozen integrity:','PASS','','Network calls:','0','','Gemini/API calls:','0','','Production calls:','0','',
        'Semantic evaluator calls:','0 (real benchmark); synthetic-only adapter exercises recorded in tests','',
        'Ready for Phase 5B.2-E-R2:','YES','','STOP. Await external review. No recovery execution authorized by this freeze.',''])
    exclusive_bytes(root/REPORT,console.encode())
    eligible=[dict(variant_id=s['variant_id'],query_id=s['query_id']) for s in inventory['slots'] if s['completion']=='ELIGIBLE_EXHAUSTED_429']
    manifest=dict(schema='phase5b2er1-quota-recovery-manifest-v0',status='PASS',created_at=utc(),
        recovery_protocol_version=VERSION,eligible_slot_count=29,completed_v0_judgment_count=64,
        max_recovery_attempts_per_slot=3,v0_attempt_budget_unchanged=True,
        recovery_order=eligible,eligible_slots=eligible,slots=inventory['slots'],counts=inventory['summary'],
        initial_recovery_states=[dict(s,status='NOT_STARTED') for s in eligible],
        quota_429_behavior=dict(session_status='QUOTA_BLOCKED',explicit_delay='Persist global deadline; stop session; future resume cannot request before deadline',
            reliable_sources=['RetryInfo.retryDelay','Retry-After delta/date','exact explicit provider retry message'],
            multiple_delays='Honor maximum positive finite delay',missing_delay='Stop entire session; require externally reviewed resume bound to quota-stop hash',
            zero_invalid_delay='Unreliable; stop',minimum_inter_request_interval=None,quota_window_inferred=False,
            non429_transport_failure='Stop session; consume only started attempt; explicit resume retains remaining budget',
            ambiguous_attempt='Consume reserved slot; block automatically; never resubmit unknown request',
            parse_failure='Existing frozen parser failure; next separate recovery attempt allowed up to three',
            historical_delays='Evidence only; never reuse an old response delay as a new quota interval'),
        stored_429_evidence=inventory['stored_429_evidence'],
        frozen_evaluator_hashes=inventory['frozen_evaluator_hashes'],frozen_model='gemini-3.5-flash-lite',temperature=0,
        frozen_endpoint=inventory['frozen_endpoint'],gold_hash=inventory['gold_sha256'],
        production_hashes={s['production_output_path']:s['production_output_hash'] for s in inventory['slots']},
        original_evaluation_artifact_hashes=inventory['original_evaluation_artifact_hashes'],
        original_production_recovery_anchor=PRODUCTION_ANCHOR,original_evaluation_provenance_anchor=V0_ANCHOR,
        historical_file_hashes=before,infrastructure_hashes={p:file_hash(root/p) for p in NEW_SOURCES},
        artifact_hashes={p:file_hash(root/p) for p in (SPEC,TESTS,INTEGRITY,REPORT)},
        recovery_ledger_root=RECOVERY_ROOT,recovery_attempts_created=0,semantic_evaluation_authorized=False,
        network_calls=0,gemini_api_calls=0,production_calls=0,semantic_evaluator_calls=0,
        tests_run=tests['tests_run'],ready_for_phase5b2e_r2=True,stop='Await external review')
    exclusive_json(root/MANIFEST,manifest)
    print(console,flush=True)
    print('Quota recovery manifest SHA-256: '+file_hash(root/MANIFEST),flush=True)

def main():
    sys.addaudithook(offline_guard)
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest='command',required=True)
    make=sub.add_parser('freeze'); make.add_argument('--before-snapshot',type=Path,required=True)
    make.add_argument('--test-results',type=Path,required=True)
    check=sub.add_parser('verify'); check.add_argument('--manifest-sha256',required=True)
    args=parser.parse_args()
    if args.command=='freeze':
        freeze(ROOT,args.before_snapshot,args.test_results)
    else:
        m=verify_manifest(ROOT,args.manifest_sha256)
        print(json.dumps(dict(status='PASS',locked=64,eligible=29,network_calls=0,semantic_evaluations=0,
                              manifest_sha256=args.manifest_sha256)))

if __name__=='__main__':
    main()
