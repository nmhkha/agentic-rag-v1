"""Offline protocol validation and additive provenance, not adjudication."""
from pathlib import Path
import datetime
import hashlib
import json
import os
import re
import stat
import sys

OUT=Path(__file__).resolve().parent
BASE=OUT.parent
ROOT=BASE.parents[4]
NAMES=['phase5c4_resource_constrained_amendment_v0.md','phase5c4_research_claim_boundaries_v0.md',
       'phase5c4_adjudicator_c_protocol_v0.md','phase5c4_selection_rules_v0.json',
       'phase5c4_amendment_manifest_v0.json','phase5c4_amendment_validation_v0.json',
       'integrity_before_after_v0.json','phase5c4_amendment_console_v0.txt',
       'integrity_baseline_v0.json','finalize_amendment_v0.py','artifact_hashes_v0.json']

def require(ok,code):
    if not ok:raise RuntimeError(code)
def read(p):return json.loads(p.read_bytes())
def raw(x):return (json.dumps(x,ensure_ascii=False,indent=2)+'\n').encode('utf-8')
def sha(b):return hashlib.sha256(b).hexdigest()
def rel(p):return p.relative_to(ROOT).as_posix()
def filehash(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1048576),b''):h.update(b)
    return h.hexdigest()
def write(name,data):
    payload=data.encode('utf-8') if isinstance(data,str) else raw(data)
    with os.fdopen(os.open(OUT/name,os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o600),'wb') as f:f.write(payload)

def snapshot():
    entries={};count=0
    for base,dirs,files in os.walk(ROOT,followlinks=False):
        for name in sorted(dirs+files):
            p=Path(base)/name;s=p.lstat();k=rel(p)
            if stat.S_ISLNK(s.st_mode):entries[k]={'kind':'symlink','target':os.readlink(p),'mode':stat.S_IMODE(s.st_mode)}
            elif stat.S_ISREG(s.st_mode):
                entries[k]={'kind':'file','sha256':filehash(p),'size_bytes':s.st_size,'mode':stat.S_IMODE(s.st_mode)}
                count+=1
                if count%5000==0:print('Integrity sweep: '+str(count)+' regular files hashed; no content printed.',flush=True)
            else:require(stat.S_ISDIR(s.st_mode),'UNSUPPORTED_ENTRY')
    return dict(sorted(entries.items()))

def protocol_checks():
    rules=read(OUT/NAMES[3]);docs={name:(OUT/name).read_text() for name in NAMES[:3]}
    main=docs[NAMES[0]];claims=docs[NAMES[1]];c=docs[NAMES[2]];checks=[]
    def check(ok,code):require(ok,code);checks.append({'check':code,'status':'PASS'})
    check(rules['target']=={'retained':36,'DEV':12,'HOLDOUT_TEST':24},'TARGET_36_12_24')
    check(rules['target']['retained']==rules['target']['DEV']+rules['target']['HOLDOUT_TEST'],'TARGET_ARITHMETIC')
    check('graduation/internship' in main and 'cannot fund' in main and '503' in main,'RESOURCE_RATIONALE_EXPLICIT')
    check(rules['benchmark_track']=='RESOURCE-CONSTRAINED MODEL-ADJUDICATED CHALLENGE BENCHMARK' and rules['benchmark_track'] in main and rules['benchmark_track'] in claims,'HONEST_TRACK_LABEL')
    check(rules['adjudicator']['human_legal_validation']=='NOT COMPLETED' and 'NOT COMPLETED' in c and 'not independently validated' in claims,'NO_FALSE_HUMAN_VALIDATION')
    check(rules['adjudicator']=={'role':'MODEL_BASED_ADJUDICATOR_C','independent_context_required':True,'authorized_passes':1,'authorized':True,'started':False,'human_legal_validation':'NOT COMPLETED'},'INDEPENDENT_C_AUTHORIZED_NOT_STARTED')
    check('fresh context' in c and 'did not author Annotation A, Annotation B or C1' in c,'INDEPENDENCE_FROM_A_B_C1')
    check('Proposal X' in c and 'Proposal Y' in c and 'disagreement registry' in c and 'complete original corpus-v0.1' in c,'C_INPUTS_DEFINED')
    check(len(rules['allowed_selection_criteria'])==10 and len(rules['hard_retention_gates'])==8,'SELECTION_CRITERIA_AND_GATES_COMPLETE')
    check(all(any(term in v for v in rules['forbidden_selection_inputs']) for term in ['Standard','v1','v2','retrieval','model answer quality','evaluator','mechanism','expected system difficulty']),'NO_SYSTEM_OUTCOME_SELECTION')
    check('A/B agreement' in rules['disagreement_use']['forbidden'] and 'annotation-quality' in rules['disagreement_use']['allowed'],'NO_AGREEMENT_ONLY_SELECTION')
    check(rules['ambiguous_case_retention']=='FORBIDDEN' and set(rules['failed_gate_disposition'])=={'RESERVE','EXCLUDE'},'UNRESOLVED_AMBIGUITY_NOT_RETAINED')
    check('Every substantive supported assertion' in c and 'scoped whole-corpus audit' in c and 'failed keyword search is not proof' in c,'SUPPORT_AND_ABSENCE_GATES')
    check('complete issue-to-decision crosswalk' in main and 'normalization rationale' in c and 'mechanically take union' in c,'MATERIAL_ADJUDICATION_AND_NORMALIZATION_PROTOCOL')
    check(len(rules['family_coverage']['families'])==4 and rules['family_coverage']['all_four_in_retained_cohort']=='REQUIRED','FOUR_TASK_FAMILIES')
    check(rules['dimension_coverage']['dimensions']==['D1','D2','D3','D4','D5','D7','D8','D9','D10'] and rules['dimension_coverage']['exact_quotas'] is None,'DIMENSION_COVERAGE_WITHOUT_FORCED_QUOTAS')
    check(rules['dimension_coverage']['D6']['value'] is None and rules['dimension_coverage']['D6']['status']=='EMPIRICAL_UNVERIFIED' and rules['dimension_coverage']['D6']['selection_input'] is False,'D6_UNMEASURED_UNUSED')
    check(rules['cluster_rules']['whole_scenario_template_proposition_clusters_one_split'] and rules['cluster_rules']['exposed_DEV_or_DEV_reserve_to_TEST']=='FORBIDDEN','WHOLE_CLUSTERS_AND_DEV_EXPOSURE_PRESERVED')
    check(rules['force_target_by_weakening_gates'] is False and 'shortfall' in main,'NO_FORCED_TARGET')
    check(rules['holdout_blindness']=='REQUIRED' and rules['holdout_storage_isolation']=='NOT_YET_ENFORCED','HOLDOUT_BLINDNESS_NOT_RELAXED')
    check(rules['implementation_safe_workspace']['required_before_implementation'] and rules['implementation_safe_workspace']['verify_from_actual_implementation_identity'] and not rules['implementation_safe_workspace']['ignore_file_or_shared_owner_modes_sufficient'],'VALIDATED_ACCESS_BOUNDARY_REQUIRED')
    check(set(rules['implementation_safe_workspace']['must_deny'])=={'TEST query plaintext','TEST gold','TEST dimensions','TEST answerability','TEST scores'},'TEST_ACCESS_DENIAL_COMPLETE')
    check(rules['historical_benchmark']['queries']==31 and rules['historical_benchmark']['points']==102 and rules['historical_benchmark']['pool_with_challenge_denominators'] is False,'HISTORICAL_BENCHMARK_SEPARATE')
    check(rules['acceptance_margins']['status']=='PROVISIONAL' and rules['acceptance_margins']['final_values'] is None,'NO_FINAL_ACCEPTANCE_MARGINS')
    check(not rules['selection_executed'] and rules['actual_final_retained_count'] is None and not rules['dataset_frozen'] and not rules['implementation_started'],'PROTOCOL_ONLY_NO_SELECTION_OR_IMPLEMENTATION')
    check(rules['future_v2_implementation_in_current_custodian_context']=='FORBIDDEN','EXPOSED_CONTEXT_IMPLEMENTATION_FORBIDDEN')
    check('Explicit amendment precedence' in main and 'inherited challenge' in main and 'All old artifacts' in main,'VERSIONED_OVERRIDE_DOMAINS_EXPLICIT')
    # Exercise hard-gate conjunction using synthetic booleans, not candidates.
    def eligible(gates,ambiguity):return len(gates)==8 and all(v is True for v in gates) and not ambiguity
    check(eligible([True]*8,False),'CONTROL_ALL_HARD_GATES_CAN_PASS')
    for i in range(8):
        g=[True]*8;g[i]=False;check(not eligible(g,False),'CONTROL_EACH_FAILED_GATE_BLOCKS_'+str(i))
    check(not eligible([True]*8,True),'CONTROL_AMBIGUITY_BLOCKS_RETENTION')
    check(not eligible([True]*7,False),'CONTROL_MISSING_GATE_BLOCKS_RETENTION')
    return rules,checks

def main():
    os.umask(0o077);require(ROOT==Path.cwd().resolve(),'RUN_FROM_PROJECT_ROOT')
    require(not (OUT/NAMES[4]).exists(),'AMENDMENT_ALREADY_FINALIZED')
    for p in OUT.iterdir():
        require(p.name in NAMES,'UNEXPECTED_OUTPUT_FILE')
        if p.is_file():p.chmod(0o600)
    before=read(OUT/'integrity_baseline_v0.json')['entries'];rules,checks=protocol_checks()
    bindings=[]
    for registry,key in [(BASE.parent/'phase5c3_v0/phase5c3_freeze_manifest_v0.json','artifact_hashes'),(BASE/'comparison_c1/final_artifact_hashes_v0.json','artifacts')]:
        for name,v in read(registry)[key].items():
            p=registry.parent/name if key=='artifact_hashes' else ROOT/name
            require(before[rel(p)]['sha256']==v['sha256'],'AUTHORITATIVE_BINDING_MISMATCH')
            bindings.append({'registry':rel(registry),'path':rel(p),'sha256':v['sha256'],'match':True})
    f=read(BASE.parent/'phase5c3_v0/phase5c3_freeze_manifest_v0.json')
    require(f['phase_status']=='PASS' and f['phase5c3_freeze_status']=='FROZEN','FROZEN_DESIGN_STATUS')
    design=BASE.parent/'phase5c3_v0/phase5c3_frozen_design_spec_v0.md'
    require('36 retained (12/24)' in design.read_text(),'RESOURCE_ALTERNATIVE_NOT_IN_FROZEN_DESIGN')
    cv=read(BASE/'comparison_c1/phase5c4c1_validation_v0.json');cs=read(BASE/'comparison_c1/phase5c4c1_disagreement_summary_v0.json')
    cm=read(BASE/'comparison_c1/phase5c4c1_agreement_metrics_v0.json')
    require(cv['phase_status']=='PASS' and cs['unresolved_issue_count']==503 and cm['candidates_with_full_substantive_agreement']==0,'C1_CONTEXT_MISMATCH')
    require(cs['candidate_priority_distribution']=={'LOW':0,'MEDIUM':14,'HIGH':41,'CRITICAL_REVIEW':5},'C1_PRIORITY_MISMATCH')
    print('Protocol validation PASS; checking all preexisting file hashes after amendment writes.',flush=True)
    after=snapshot();changed=[k for k,v in before.items() if after.get(k)!=v];additions=sorted(after.keys()-before.keys())
    require(not changed,'PREEXISTING_ARTIFACT_CHANGED')
    require(all((ROOT/k).parent==OUT and (ROOT/k).name in NAMES for k in additions),'ADDITION_OUTSIDE_AMENDMENT')
    integrity={'status':'PASS','preexisting_regular_files':sum(x['kind']=='file' for x in before.values()),
               'preexisting_symlinks':sum(x['kind']=='symlink' for x in before.values()),
               'all_preexisting_files_byte_identical':True,'preexisting_modes_and_symlink_targets_unchanged':True,
               'before_inventory_sha256':sha(raw(before)),'after_preexisting_inventory_sha256':sha(raw({k:after[k] for k in before})),
               'baseline_file':'integrity_baseline_v0.json','baseline_sha256':filehash(OUT/'integrity_baseline_v0.json'),
               'changed_or_missing':changed,'new_paths_outside_namespace':[],
               'additions_at_integrity_sweep':additions,'allowed_final_files':NAMES,
               'scope':'All preexisting project regular files hashed before and after; symlink targets/modes preserved; opaque binary hashing, not substantive system-output inspection. Remaining manifest/validation/console/hash files are additive in this namespace.'}
    write('integrity_before_after_v0.json',integrity)
    request=Path('/home/minhkha/.codex/attachments/c50f3e00-bbec-4954-872d-f9922e611cb5/pasted-text.txt')
    source_paths=[design,BASE.parent/'phase5c3_v0/phase5c3_design_amendments_v0.md',BASE.parent/'phase5c3_v0/phase5c3_margin_governance_v0.md',
                  BASE.parent/'phase5c2_v0/phase5c2_challenge_set_design_v0.md',BASE/'comparison_c1/phase5c4c1_validation_v0.json',
                  BASE/'comparison_c1/phase5c4c1_disagreement_summary_v0.json',BASE/'comparison_c1/phase5c4c1_agreement_metrics_v0.json']
    manifest={'schema':'phase5c4-resource-constrained-amendment-manifest-v0','phase':'5C.4-C2-Lite','phase_status':'PASS',
              'protocol_version':'phase5c4-resource-constrained-v0','protocol_state':'ADOPTED_NOT_EXECUTED',
              'created_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'authority':{'kind':'EXPLICIT_USER_VERSIONED_PROTOCOL_AMENDMENT','request_path':str(request),'request_sha256':filehash(request)},
              'role':'TRUSTED_DATASET_CUSTODIAN / PROTOCOL_COORDINATOR',
              'future_v2_implementation_in_this_context':'FORBIDDEN',
              'benchmark_track':rules['benchmark_track'],'human_legal_validation':'NOT COMPLETED',
              'target':rules['target'],'actual_final_retained_count':None,
              'third_model_adjudication_authorized':True,'third_model_adjudication_started':False,'final_selection_started':False,
              'human_gate_change':{'old_stronger_track':'HUMAN_LEGAL_REVIEW_REQUIRED remains historically true',
                                   'new_track':'Model C adjudication plus corpus/annotation quality gates may replace expert signoff for this explicitly limited benchmark',
                                   'not_a_claim_original_expert_gate_passed':True},
              'override_domains':['annotation acceptance route and claim strength','activate existing 36/12/24 alternative','dimension/subtype/control quotas as soft objectives','group equivalent C1 issues with complete normalization crosswalk'],
              'unchanged_contracts':['corpus-v0.1','immutable prior artifacts and queries','evaluator-only gold','OR/AND support and P+/Q/U ledger','outcome-independent selection','whole-cluster separation','DEV exposure restrictions','HOLDOUT blindness','D6 post-lock only','historical denominator separation','provisional acceptance margins'],
              'sources':{rel(p):{'sha256':before[rel(p)]['sha256'],'size_bytes':before[rel(p)]['size_bytes']} for p in source_paths},
              'frozen_source_bindings':bindings,'source_bindings_pass':True,
              'prior_comparison':{'candidates':60,'full_substantive_agreement':0,'unresolved_issues':503,'candidate_priority':cs['candidate_priority_distribution'],
                                  'interpretation':'Conservative confirmed agreement, not 60 legally incorrect candidates'},
              'selection_rules':'phase5c4_selection_rules_v0.json','adjudicator_protocol':'phase5c4_adjudicator_c_protocol_v0.md',
              'claim_boundaries':'phase5c4_research_claim_boundaries_v0.md','amendment':'phase5c4_resource_constrained_amendment_v0.md',
              'D6':'EMPIRICAL_UNVERIFIED','holdout_blindness':'REQUIRED','holdout_storage_isolation':'NOT_YET_ENFORCED',
              'implementation_safe_workspace_validated':False,'implementation_started':False,'dataset_frozen':False,'dataset_freeze_ready':False,
              'acceptance_margins':rules['acceptance_margins'],
              'historical_benchmark':rules['historical_benchmark'],
              'execution':{'network_api_calls':0,'production_calls':0,'evaluator_calls':0,'retrieval_reranking_inference_calls':0,'system_outputs_substantively_inspected':0,'C_adjudications':0,'candidate_selections':0,
                           'basis':'This phase used local protocol reads/writes, standard-library validation and binary integrity hashing only. No project runtime or inference pipeline was imported; counts are task-initiated activity, not OS-wide attestation.'},
              'preexisting_integrity':'PASS','ready_for_model_adjudication_final_selection':True,
              'readiness_meaning':'Protocol authorization only; C needs a separately prepared, validated packet and fresh independent context. No completed adjudication, selection or freeze is claimed.',
              'blocking_release_gates':['independent C annotation and hard retention gates','feasible cluster-safe 12/24 selection','query/gold/split lock','validated HOLDOUT access boundary'],
              'final_artifact_names':NAMES,'public_content_policy':'Protocol and aggregate facts only; no candidate text, gold or split mapping copied. Baseline inventory and source paths are custodian provenance, not an implementation-safe export.'}
    write('phase5c4_amendment_manifest_v0.json',manifest)
    validation={'schema':'phase5c4-resource-constrained-amendment-validation-v0','phase_status':'PASS','checks':checks,
                'check_count':len(checks),'source_bindings_checked':len(bindings),'source_bindings_status':'PASS',
                'required_pass_gates':{k:'PASS' for k in ['resource_constraint_rationale','honest_benchmark_claim','no_false_human_validation','36_equals_12_plus_24','C_adjudication_authorized','no_system_outcome_selection','D6_unmeasured','HOLDOUT_blindness_preserved','no_inference_API','old_artifacts_unchanged']},
                'validation_scope':'Protocol consistency, source provenance and artifact integrity only; not legal adjudication or dataset validation.',
                'human_legal_validation':'NOT COMPLETED','C_adjudication_started':False,'selection_started':False,
                'D6':'EMPIRICAL_UNVERIFIED','storage_isolation':'NOT_YET_ENFORCED','preexisting_integrity':'PASS',
                'ready_for_model_adjudication_final_selection':True,'ready_for_final_dataset_freeze':False,
                'no_candidate_text_or_gold_authored':True,'no_system_outputs_inspected':True}
    write('phase5c4_amendment_validation_v0.json',validation)
    console='''Phase 5C.4-C2-Lite amendment:
PASS

Benchmark track:
RESOURCE-CONSTRAINED MODEL-ADJUDICATED

Independent human legal validation:
NO

Third model adjudication authorized:
YES

Target retained:
36

Target DEV:
12

Target HOLDOUT TEST:
24

System-output-based selection:
FORBIDDEN

D6:
EMPIRICAL_UNVERIFIED

HOLDOUT blindness:
REQUIRED

HOLDOUT storage isolation:
NOT_YET_ENFORCED

Agentic v2 implementation:
NOT STARTED

Network/API calls:
0

Production/evaluator/retrieval calls:
0

Preexisting artifact integrity:
PASS

Ready for model adjudication/final challenge selection:
YES

STOP
'''
    write('phase5c4_amendment_console_v0.txt',console)
    require({p.name for p in OUT.iterdir()}==set(NAMES)-{'artifact_hashes_v0.json'},'ARTIFACT_SET_MISMATCH')
    write('artifact_hashes_v0.json',{'purpose':'Versioned protocol amendment provenance; not dataset freeze','algorithm':'sha256','self_excluded':True,
                                  'artifacts':{rel(p):{'sha256':filehash(p),'size_bytes':p.stat().st_size} for p in sorted(OUT.iterdir()) if p.is_file()}})
    print(console,end='')

def verify():
    require({p.name for p in OUT.iterdir()}==set(NAMES),'FINAL_ARTIFACT_SET_MISMATCH')
    for name,v in read(OUT/'artifact_hashes_v0.json')['artifacts'].items():require(filehash(ROOT/name)==v['sha256'],'FINAL_ARTIFACT_HASH_MISMATCH')
    _,checks=protocol_checks();v=read(OUT/'phase5c4_amendment_validation_v0.json');m=read(OUT/'phase5c4_amendment_manifest_v0.json')
    require(v['checks']==checks and v['phase_status']==m['phase_status']=='PASS','FINAL_VALIDATION_MISMATCH')
    integrity=read(OUT/'integrity_before_after_v0.json')
    require(integrity['before_inventory_sha256']==integrity['after_preexisting_inventory_sha256'],'INTEGRITY_DIGEST_MISMATCH')
    print('Read-only amendment verification PASS; '+str(len(checks))+' protocol checks; 11 artifacts; no adjudication or selection executed.')

if __name__=='__main__':
    try:
        if sys.argv[1:]==['--verify']:verify()
        else:require(not sys.argv[1:],'UNKNOWN_ARGUMENT');main()
    except Exception as e:
        print('Amendment validation stopped: FAIL; downstream readiness not authorized by this run.',file=sys.stderr)
        if isinstance(e,RuntimeError) and re.fullmatch('[A-Z_0-9]+',str(e)):print('Validation code: '+str(e),file=sys.stderr)
        else:print('Error type: '+type(e).__name__,file=sys.stderr)
        raise SystemExit(1) from None
