import sys, os, json, hashlib, time
from pathlib import Path
ROOT=Path('/home/minhkha/kk/TTTN/legal-agentic-rag')
BASE=ROOT/'data/evaluation/generation/phase5'
OUT=BASE/'phase5b2f_v0'
sys.dont_write_bytecode=True
sys.path.insert(0,str(ROOT/'scripts'))
COUNTS={'network_calls':0,'blocked_network_attempts':0,'production_calls':0,'evaluator_calls':0}
def guard(event,args):
    if event.startswith('socket.') or event in ('urllib.Request','http.client.connect','http.client.send','subprocess.Popen','os.system','os.posix_spawn'):
        COUNTS['blocked_network_attempts']+=1
        raise RuntimeError('Offline analysis prohibits transport and child processes')
sys.addaudithook(guard)
def sha(p):
    with Path(p).open('rb') as f: return hashlib.file_digest(f,'sha256').hexdigest()
def read(p): return json.loads(Path(p).read_text())
def snapshot():
    result={}
    for parent,dirs,files in os.walk(ROOT):
        dirs[:]=sorted(d for d in dirs if d not in ('.venv','.git','.agents','.codex') and Path(parent)/d!=OUT)
        for name in sorted(files):
            p=Path(parent)/name
            result[str(p.relative_to(ROOT))]=sha(p)
    return result
if __name__=='__main__':
    assert not OUT.exists(),'additive target already exists'
    before=snapshot()
    external={}
    env=read(BASE/'execution_environment_v0.json')
    for name,expected in env['runtime_lock']['asset_files'].items():
        if Path(name).is_absolute():
            external[name]=sha(name); assert external[name]==expected,name
    Path('/tmp/phase5b2f_before.json').write_text(json.dumps({'project':before,'external_assets':external},sort_keys=True))
    print('Before snapshot:',len(before),'project files;',len(external),'external assets',flush=True)
    from phase5_evaluation_quota_recovery_v1 import verify_manifest,RecoveryLedger,digest
    anchor='8e74013cab6df4564dd33f17cd6901e968152b631d82bbc0c523e680c4a999ee'
    manifest=verify_manifest(ROOT,anchor)
    ledger=RecoveryLedger(BASE/'phase5b2er2_v1',manifest['slots'],anchor)
    records=[]; attempts=[]; counts={a:{'v0':0,'v1':0} for a in ('R2','A1','A2')}
    expected_dirs=set()
    for slot in manifest['slots']:
        alias,qid=slot['alias'],slot['query_id']
        history,last=ledger.state(slot)
        if slot['completion']=='LOCKED_VALID_V0':
            assert not history,'recovery competed with accepted v0'
            source=ROOT/slot['v0_record_path']; kind='v0'
        else:
            assert slot['completion']=='ELIGIBLE_EXHAUSTED_429'
            assert last and last['final_recovery_status']==last['slot_status_after_attempt']=='VALID_JUDGMENT',f'unresolved {alias}/{qid}'
            assert sum(bool(h[2] and h[2]['final_recovery_status']=='VALID_JUDGMENT') for h in history)==1
            for path,start,receipt in history:
                assert receipt is not None,'unresolved STARTED'
                assert receipt['final_recovery_status'] not in ('RECOVERY_EXHAUSTED','AMBIGUOUS')
                assert start['production_output_hash']==slot['production_output_hash']
                assert start['gold_query_binding_hash']==slot['gold_query_binding_hash']
                wire=read(path/'wire_response.json')
                assert wire['started_record_hash']==sha(path/'started.json')
                assert wire['prompt_sha256']==slot['prompt_sha256']
                if wire.get('raw') is not None: assert digest(wire['raw'])==wire['response_hash']==receipt['response_hash']
                expected_dirs.add(str(path.relative_to(BASE/'phase5b2er2_v1')))
                attempts.append({'alias':alias,'query_id':qid,'attempt':start['recovery_attempt_index'],'status':receipt['final_recovery_status'],'receipt_path':str((path/'receipt.json').relative_to(ROOT)),'receipt_sha256':sha(path/'receipt.json')})
            source=history[-1][0]/'evaluation_record.json'; kind='v1'
            assert sha(source)==last['result_hash'],'unsealed judgment'
        counts[alias][kind]+=1
        records.append({'alias':alias,'query_id':qid,'source':str(source.relative_to(ROOT)),'source_sha256':sha(source),'kind':kind})
    actual={str(p.parent.relative_to(BASE/'phase5b2er2_v1')) for p in (BASE/'phase5b2er2_v1').glob('*/*/*/started.json')}
    assert actual==expected_dirs,'unknown recovery attempts'
    judgments=list((BASE/'phase5b2er2_v1').glob('*/*/*/evaluation_record.json'))
    assert len(judgments)==29 and {str(p.relative_to(ROOT)) for p in judgments}=={r['source'] for r in records if r['kind']=='v1'}
    assert sum(c['v0'] for c in counts.values())==64 and sum(c['v1'] for c in counts.values())==29
    assert all(sum(c.values())==31 for c in counts.values())
    result={'status':'PASS','anchor':anchor,'counts':counts,'valid_total':93,'remaining_slots':0,'attempts':attempts,'sources':records,'calls':COUNTS}
    Path('/tmp/phase5b2f_gate.json').write_text(json.dumps(result,indent=2))
    print(json.dumps({k:v for k,v in result.items() if k not in ('sources','attempts')},indent=2),flush=True)
