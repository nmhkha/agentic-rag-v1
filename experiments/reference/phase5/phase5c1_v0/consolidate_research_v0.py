"""Phase 5C.1: standard-library, stored-artifact synthesis; no runtime imports.

Exclusive creation deliberately prevents rerunning over completed outputs.
No retrieval, model, evaluator, bootstrap, or production entrypoint is executed.
"""
from pathlib import Path
from collections import Counter
from fractions import Fraction
import datetime
import hashlib
import json
import os
import re

ROOT = Path(__file__).resolve().parents[5]
OUT = Path(__file__).resolve().parent
G = ROOT / 'data/evaluation/generation'
P = G / 'phase5'
F = P / 'phase5b2f_v0'
sources = {}
checks = {}


def read(p):
    p = Path(p)
    data = p.read_bytes()
    sources[str(p.relative_to(ROOT))] = {'sha256': hashlib.sha256(data).hexdigest(), 'size_bytes': len(data), 'review': 'read and parsed in full; used for source reconciliation or research synthesis'}
    if p.suffix == '.json':
        return json.loads(data)
    if p.suffix == '.jsonl':
        return [json.loads(line) for line in data.decode().splitlines() if line.strip()]
    return data.decode()


def write(name, data):
    with (OUT / name).open('x', encoding='utf-8') as f:
        f.write(data if isinstance(data, str) else json.dumps(data, ensure_ascii=False, indent=2) + '\n')


def check(name, condition):
    checks[name] = bool(condition)
    assert condition, name


def link(p, label=None):
    p = Path(p)
    return f'[{label or p.name}]({os.path.relpath(p, OUT)})'


def number(x):
    return f'{x:.12f}'


def table(headers, rows):
    return '\n'.join(['| ' + ' | '.join(headers) + ' |', '| ' + ' | '.join(['---'] * len(headers)) + ' |'] + ['| ' + ' | '.join(map(str, row)) + ' |' for row in rows])


before = json.loads((OUT / 'integrity_before_inventory_v0.json').read_text())
design = read(P / 'phase5a_ablation_manifest_v0.json')
spec = read(P / 'phase5a_ablation_spec_v0.md')
final = read(F / 'phase5b2f_metrics_v0.json')
canonical = read(F / 'canonical_judgments_manifest.json')
provenance = read(F / 'provenance_v0.json')
prior_integrity = read(F / 'integrity_before_after_v0.json')
prior_hashes = read(F / 'final_artifact_hashes_v0.json')
for name in ['validation_v0.json', 'recovery_completion_gate_v0.json']:
    read(F / name)
check('phase5b2f_complete', final['status'] == 'PASS' and final['valid_semantic_records'] == 93 and final['query_count'] == 31 and final['unique_required_point_tuples'] == 102)
for rel, digest in prior_hashes['files'].items():
    check('phase5b2f_hash:' + rel, hashlib.sha256((F / rel).read_bytes()).hexdigest() == digest)

reports = [G/'reports/standard_rag_eval_v0.md', G/'reports/standard_rag_failure_analysis_v0.md', G/'reports/agentic_rag_eval_v1_agentic-v1.md', G/'reports/agentic_trace_analysis_v0.md', F/'phase5b2f_final_report_v0.md', ROOT/'data/evaluation/results/candidate-union-v0_report.md', ROOT/'retriever-reranker-comparison-v0.md']
for p in reports:
    read(p)
r0 = read(G/'standard_rag_eval_v0.jsonl')
r1 = read(G/'agentic_rag_eval_v1_agentic-v1.jsonl')
r0m = read(G/'standard_rag_metrics_v0.json')
r1m = read(G/'agentic_rag_metrics_v1_agentic-v1.json')
fa = read(G/'failure_analysis_metrics_v0.json')
points = read(G/'failure_analysis_points_v0.jsonl')
queries = read(G/'failure_analysis_queries_v0.json')
tr = read(G/'agentic_trace_analysis_metrics_v0.json')
tr_rows = read(G/'agentic_trace_analysis_v0.jsonl')
corpus = read(ROOT/'data/versions/corpus-v0.1/corpus_validation_manifest.json')
union = read(ROOT/'data/evaluation/results/candidate-union-v0_metrics.json')
reranker = read(ROOT/'data/evaluation/results/bge-reranker-v2-m3-v0_metrics.json')
eff = read(F/'efficiency_v0.json')
rep = read(F/'replication_R1_R2.json')
contrasts = {a: read(F/f'contrast_R2_{a}.json') for a in ['A1', 'A2']}
bootstraps = {a: read(F/f'bootstrap_R2_{a}.json') for a in contrasts}
transition_rows = {pair: read(F/f'point_transitions_{pair}.jsonl') for pair in ['R1_R2','R2_A1','R2_A2']}
variant_names = {'R2': 'full-agentic-replication', 'A1': 'agentic-v1-no-answer-revision', 'A2': 'agentic-v1-no-evidence-expansion'}
records = {'R0': r0, 'R1': r1}
for alias, variant in variant_names.items():
    records[alias] = read(F/variant/'evaluation_complete.jsonl')
    read(F/variant/'metrics.json')
    read(P/variant/'run_manifest.json')
    read(P/variant/'variant_manifest.json')

# Reconcile existing labels by integer set/count arithmetic, never by semantic judging.
order = design['query_order']
metrics = final['metrics']
check('frozen_query_order', all([r['query_id'] for r in rows] == order for rows in records.values()))
for alias, rows in records.items():
    total = sum(len(r['required_point_ids']) for r in rows)
    support = sum(len(r['supported_point_ids']) for r in rows)
    macro = float(sum((Fraction(len(r['supported_point_ids']), len(r['required_point_ids'])) for r in rows), Fraction()) / len(rows))
    expected = r0m['answer_completeness'] if alias == 'R0' else metrics[alias]['answer_completeness']
    check(alias + '_saved_label_AC', total == 102 and abs(macro - expected['macro']) < 1e-12 and abs(support/total - expected['micro']) < 1e-12)
    check(alias + '_no_errors', all(not r.get('evaluation_error') and not r.get('generation_error') for r in rows))
    check(alias + '_query_and_point_binding', all(r['query'] == base['query'] and r['required_point_ids'] == base['required_point_ids'] for r, base in zip(rows, r0)))
    check(alias + '_supported_subset', all(set(r['supported_point_ids']) <= set(r['required_point_ids']) for r in rows))
for c in canonical['records']:
    saved = read(ROOT/c['source_record_path'])
    row = next(r for r in records[c['alias']] if r['query_id'] == c['query_id'])
    check('canonical_source:' + c['alias'] + ':' + c['query_id'], saved == row)
    output = read(ROOT/c['production_output_path'])
    check('production_output_hash:' + c['alias'] + ':' + c['query_id'], sources[c['production_output_path']]['sha256'] == c['production_output_hash'])
for r in r1:
    check('R1_trace:' + r['query_id'], read(Path(r['trace_path'])) == r['trace'])
r2_traces = {}
for r in records['R2']:
    path = ROOT/'data/rag/traces/phase5/full-agentic-replication'/f"{r['query_id']}.json"
    disk = read(path)
    check('R2_sealed_trace:' + r['query_id'], disk == r['trace'])
    r2_traces[r['query_id']] = disk
    read(path.parent/'observations'/path.name)
triggers = {key: [qid for qid, t in r2_traces.items() if t[key]] for key in ['revision_used','expansion_used','citation_revision_used']}
for a, key in [('A1','revision_used'),('A2','expansion_used')]:
    check(a + '_trigger_stratum_binding', triggers[key] == contrasts[a]['triggered_query_ids'])
    check(a + '_frozen_label', contrasts[a]['interpretation'] == 'Insufficient evidence')
    check(a + '_bootstrap_binding', bootstraps[a] == contrasts[a]['bootstrap'])
for pair, rows in transition_rows.items():
    left, right = pair.split('_')
    check(pair + '_transition_universe', len(rows) == 102 and len({(r['query_id'],r['point_id']) for r in rows}) == 102)
    by_variant = {a: {r['query_id']: set(r['supported_point_ids']) for r in records[a]} for a in [left,right]}
    for r in rows:
        for a in [left,right]:
            check(pair + ':' + r['query_id'] + '/' + r['point_id'] + ':' + a, r[a+'_supported'] == (r['point_id'] in by_variant[a][r['query_id']]))
check('failure_taxonomy_reconciles', dict(Counter(r['primary_failure'] for r in points)) == fa['aggregate']['primary_failure_counts'])
omissions = [r for r in points if r['primary_failure'] == 'answer_generation']
check('generation_omission_evidence', len(omissions) == fa['aggregate']['generation_bottleneck_top5_sufficient_answer_incomplete'] and all(r['top5_sufficient_evidence'] for r in omissions))
check('failure_query_rows', queries['query_count'] == 31 and len(queries['queries']) == 31)
cal = tr['self_check_calibration']
cal_count = Counter(('internal_complete' if r['trace']['completeness_check']['complete'] else 'internal_incomplete') + ('_and_benchmark_complete' if len(r['supported_point_ids']) == len(r['required_point_ids']) else '_and_benchmark_incomplete') for r in r1)
check('self_check_matrix', [cal_count['internal_complete_and_benchmark_complete'],cal_count['internal_complete_and_benchmark_incomplete'],cal_count['internal_incomplete_and_benchmark_complete'],cal_count['internal_incomplete_and_benchmark_incomplete']] == [cal['internal_complete_and_benchmark_complete'],cal['internal_complete_but_benchmark_incomplete'],cal['internal_incomplete_but_benchmark_complete'],cal['internal_incomplete_and_benchmark_incomplete']])
check('self_check_false_success_rows', [r['query_id'] for r in tr_rows if r['success_status_but_benchmark_incomplete']] == cal['success_status_but_benchmark_incomplete_query_ids'])

chat_path = ROOT/'data/rag/traces/agentic-rag-v1_20260909T132915.670264Z.json'
chat = read(chat_path)
check('chatbot_excluded_from_benchmark', chat['query'] not in [r['query'] for r in r0])
check('chatbot_trace_facts', chat['coverage_check']['sufficient'] is False and chat['expansion_used'] is True and chat['revision_used'] is True and chat['completeness_check']['complete'] is True)
cited = list(dict.fromkeys(re.findall(r'\[(E\d+)\]', chat['final_answer'])))
added = [e for e in chat['final_evidence'] if e['chunk_id'] not in chat['initial_top5']]
uncited = [e for e in chat['final_evidence'] if e['evidence_id'] not in cited]
check('chatbot_new_final_evidence_from_expansion', all(e['chunk_id'] in set(chat['expansion_candidates']) for e in added))
diagnostic = {'classification': 'EXPLORATORY / NON-BENCHMARK / NON-CONFIRMATORY', 'source': str(chat_path.relative_to(ROOT)), 'query': chat['query'], 'benchmark_query_id': None, 'included_in_metrics': False, 'coverage_check': chat['coverage_check'], 'missing_aspects': chat['missing_aspects'], 'sub_queries': chat['sub_queries'], 'initial_top5': chat['initial_top5'], 'new_final_evidence': [{k:e[k] for k in ['evidence_id','chunk_id','article','text','retrieval_text']} for e in added], 'final_evidence_ids': [e['evidence_id'] for e in chat['final_evidence']], 'draft_answer': chat['draft_answer'], 'final_answer': chat['final_answer'], 'final_cited_ids': cited, 'uncited_final_evidence_ids': [e['evidence_id'] for e in uncited], 'expansion_used': chat['expansion_used'], 'revision_used': chat['revision_used'], 'final_completeness': chat['completeness_check'], 'transitions': chat['state']['transitions'], 'initial_completeness_payload': 'not separately retained; the recorded completeness object is the final recheck', 'interpretation': 'Exploratory observation suggests a possible goal-persistence / evidence-to-answer coverage gap.', 'scope_caveat': 'E6 and E26 partially relate to previously missing aspects; they do not establish complete medical testing standards or all developer obligations. Uncited evidence is not automatically a required omission. E58 is used after revision, providing counterevidence to total goal loss.', 'confirmation_required': 'requires confirmation on a separately designed challenge set'}
write('phase5c1_exploratory_diagnostic_v0.json', diagnostic)

def finding(fid, title, statement, tier, artifacts, supporting, qids, conflicts, limits, confidence, allowed, prohibited):
    return dict(finding_id=fid, title=title, statement=statement, evidence_tier=tier, supporting_artifacts=[str(p.relative_to(ROOT)) for p in artifacts], supporting_metrics=supporting, supporting_query_ids=qids, counterevidence_or_conflicts=conflicts, limitations=limits, confidence=confidence, confidence_basis={'high':'Tier A: reconciled frozen records and summaries; confidence applies to the bounded descriptive statement, not causal attribution.', 'medium':'Reconciled evidence supports a bounded pattern; observational inference or controlled replication/conflicting outcomes limit attribution.', 'low':'Tier C: one exploratory trace without independent gold or controlled confirmation.'}[confidence], allowed_claim=allowed, prohibited_overclaim=prohibited)

findings = [
finding('F1','Localization mạnh hơn full evidence coverage','Candidate coverage và article localization tương đối mạnh; exact chunk và multi-point coverage vẫn thiếu.','A',[ROOT/'data/evaluation/results/candidate-union-v0_metrics.json',ROOT/'data/evaluation/results/bge-reranker-v2-m3-v0_metrics.json',G/'failure_analysis_metrics_v0.json'],{'candidate_chunk':union['chunk_level'],'candidate_article':union['article_level'],'reranked_chunk':reranker['chunk_level'],'reranked_article':reranker['article_level'],'point_candidate_sufficient':fa['aggregate']['candidate_had_sufficient_evidence'],'point_top5_sufficient':fa['aggregate']['top5_retained_sufficient_evidence'],'point_denominator':102},reranker['worst_5'],['Union còn 21/98 annotated gold chunk occurrences chưa tìm thấy; article hit không bảo đảm đủ các khoản/điểm.'],['Retrieval gold chunk universe 98 khác generation required-point universe 102; annotated support không bao quát mọi alternative evidence.'],'high','Retrieval localizes relevant articles well on this frozen set but does not solve full evidence coverage.','Retrieval is solved completely; any-gold coverage equals answer completeness.'),
finding('F2','Standard failures gồm cả generation omission','Có các điểm thiếu trong answer dù toàn bộ annotated support đã ở Top-5; đây là căn cứ trực tiếp đề xuất Answer Revision.','A',[G/'failure_analysis_points_v0.jsonl',G/'failure_analysis_queries_v0.json',G/'failure_analysis_metrics_v0.json',G/'reports/standard_rag_failure_analysis_v0.md'],fa['aggregate'],sorted({r['query_id'] for r in omissions}),['Primary retrieval miss 16 và evidence coverage 17 vẫn lớn; không quy mọi failure cho generation.','Report 4A dùng câu “pure retrieval miss is smaller”; số authoritative là 16 > 9 generation. Giữ nguyên nguồn, không lặp lại cách xếp hạng sai đó.'],['Taxonomy là phân loại post-hoc trên frozen labels; 28 mất support ở Top-5 không đồng nhất 17 primary evidence failures. Partial point support không xác định riêng.'],'high','Evidence sufficient under frozen annotated-support criterion can coexist with generation omission.','Every unsupported point is a retrieval failure, or all 28 support losses are answer failures.'),
finding('F3','Historical R0 → R1 improvement','AC tăng trong historical R1 so với R0, với chi phí tăng và safety thay đổi theo macro/micro; replication phải đặt cạnh.','A',[G/'standard_rag_eval_v0.jsonl',G/'standard_rag_metrics_v0.json',G/'agentic_rag_eval_v1_agentic-v1.jsonl',G/'agentic_rag_metrics_v1_agentic-v1.json',G/'agentic_trace_analysis_metrics_v0.json',F/'replication_R1_R2.json'],{'historical_AC':tr['answer_completeness'],'pooled_safety':tr['additional_micro_metrics'],'R1_efficiency':tr['efficiency'],'replication_AC':rep['deltas']['answer_completeness']},[r['query_id'] for r in tr_rows if r['gained_supported_point_ids'] or r['lost_supported_point_ids']],['R1→R2 AC giảm; R0→R1 macro groundedness tăng nhưng pooled groundedness giảm.'],['Historical system comparison is not a controlled intervention effect. R0 cost is configured logical baseline; historical environment not fully pinned.'],'high','Observed historical AC improvement with higher logical call cost; attribution remains limited.','R1 proves that each agentic mechanism causes improvement or safety uniformly improves.'),
finding('F4','Same-configuration variation material','R1→R2 có point churn và safety drift đủ để giới hạn attribution của chênh lệch nhỏ.','A',[F/'replication_R1_R2.json',F/'point_transitions_R1_R2.jsonl',F/'phase5b2f_metrics_v0.json'],{k:v for k,v in rep.items() if k!='per_query'},sorted({r['query_id'] for r in transition_rows['R1_R2'] if r['R1_supported'] != r['R2_supported']}),['Net -2 che khuất 4 point transitions. Groundedness macro và pooled đi ngược chiều.'],['One replication; cannot separate generation and judge variability or estimate a noise distribution.'],'high','One production run cannot establish every small difference as a mechanism effect.','Observed replication is formal variance, a noise bound, or a correction to subtract from ablation effects.'),
finding('F5','Answer Revision: descriptive positive signal','R2−A1 positive AC signal tập trung ở R2 revision-used stratum; frozen conclusion vẫn Insufficient evidence.','A',[F/'contrast_R2_A1.json',F/'bootstrap_R2_A1.json',F/'point_transitions_R2_A1.jsonl',F/'efficiency_v0.json',F/'replication_R1_R2.json'],{k:v for k,v in contrasts['A1'].items() if k!='per_query'},triggers['revision_used'],contrasts['A1']['conflicts']+['Replication gross churn 4 equals ablation churn 4; safeguard takes precedence.','Bootstrap lower endpoint is zero.'],['4 R2-used queries; post-treatment descriptive stratum; no randomized subgroup or benchmark-equivalent draft evaluation.'],'medium','Descriptive positive, mechanism-specific signal justifies further research; Insufficient evidence remains frozen.','Supported contribution, statistically significant causal effect, or guaranteed benefit.'),
finding('F6','Expansion: weak aggregate contribution','Macro AC bằng A2, net +1 point với churn và retrieval overhead; chưa đủ attribution.','A',[F/'contrast_R2_A2.json',F/'bootstrap_R2_A2.json',F/'point_transitions_R2_A2.jsonl',F/'efficiency_v0.json',F/'replication_R1_R2.json'],{k:v for k,v in contrasts['A2'].items() if k!='per_query'},triggers['expansion_used'],['R2-used subset favors R2 by 3 points; non-used subset favors A2 by 2.','A2 has better claim safety summaries; macro/net replication attribution flag true.'],['Triggered gains concentrated at eval014; no attribution from non-used query differences. CI spans both signs.'],'medium','Evidence Expansion v1 shows weak aggregate value relative to retrieval work on this benchmark; Insufficient evidence.','Expansion is useless, unnecessary, or causally proven helpful on all triggered queries.'),
finding('F7','Interventions used on minority of R2 queries','R2 dùng revision và expansion trên một phần benchmark; usage không đo effectiveness hay difficulty.','B',[F/'full-agentic-replication/evaluation_complete.jsonl',F/'canonical_judgments_manifest.json']+[ROOT/'data/rag/traces/phase5/full-agentic-replication'/f'{q}.json' for q in order],{'query_count':len(order),'usage':{k:{'count':len(v),'rate':len(v)/len(order),'query_ids':v} for k,v in triggers.items()}},order,['Many no-use queries remain benchmark-incomplete; checks still execute. R1 usage differs from R2.'],['Observational trace usage, not randomized exposure or independent difficulty annotation.'],'medium','many queries were resolved without invoking the corresponding intervention; resolved means the controller returned an output, not benchmark-complete.','Low trigger rate proves ineffectiveness, or the entire frozen benchmark is easy.'),
finding('F8','Self-check calibration mismatch','Internal completeness và controller success không đồng nghĩa benchmark completeness.','B',[G/'agentic_trace_analysis_v0.jsonl',G/'agentic_trace_analysis_metrics_v0.json',G/'reports/agentic_trace_analysis_v0.md'],cal,cal['potential_false_success_query_ids'],['13 complete/complete agreements and one internal-incomplete but benchmark-complete query.','Checker and benchmark evaluate different available information/criteria.'],['Tier B observational mismatch; no assertion of a software bug. Seven initial checker payloads overwritten; eval005b final check precedes citation edit.'],'medium','Frozen Phase 4E observes a completeness calibration mismatch and a false-success pattern.','Self-check is definitely buggy; controller success is benchmark-complete; mismatch proves a causal mechanism.'),
finding('F9','Possible missing-aspect carry-through gap','Exploratory observation suggests a possible goal-persistence / evidence-to-answer coverage gap.','C',[chat_path],diagnostic,[],['Revision adds E58 human oversight: a real evidence-to-answer carry-through occurs.','E6 concerns sector regulators; E26 limits disclosure duties. Neither fully resolves the original missing medical details.','Not citing every retrieved chunk is not inherently an error.'],['EXPLORATORY / NON-BENCHMARK / NON-CONFIRMATORY; one query; no gold or evaluator; initial completeness payload absent.','requires confirmation on a separately designed challenge set'],'low','Hypothesis about retaining unresolved aspects through evidence, answer and final check.','Agentic v1 definitely has this bug; this query confirms causal failure or alters Phase 5 metrics.')
]
write('phase5c1_evidence_matrix_v0.json', {'schema':'phase5c1-evidence-matrix-v0','confidence_policy':'Confidence concerns the allowed bounded claim: high for reconciled Tier A descriptions; medium for Tier A attribution-limited patterns or consistent Tier B observations; low for Tier C hypotheses. Tier does not confer causality.','findings':findings})

requirements = []
def req(rid, problem, evidence, tier, current, desired, why, risk, evaluation, status):
    requirements.append(dict(requirement_id=rid,problem=problem,evidence=evidence,evidence_tier=tier,current_behavior=current,desired_behavior=desired,why_justified=why,known_risk=risk,how_to_evaluate_later=evaluation,status=status,planning_only=True))

req('V2-R1','Generation omission; Completeness-aware Answer Revision',['F2','F5'],['A'],'Có evidence nhưng bỏ ý; current revision có descriptive positive signal, frozen label Insufficient evidence.','Revision có mục tiêu phục hồi các ý liên quan được evidence hỗ trợ, bảo toàn grounding/citation và báo phần chưa giải quyết.','9 omission points ở R0; R2-used stratum 9/19 so với 5/19.','Checker sai hoặc revision thêm claim unsupported; chi phí tăng.','Predeclare separate development/challenge evaluation, frozen historical reporting, draft/final completeness and safety, repeated paired runs and call budgets; no tuning on the 31 queries.','INVESTIGATE_BEFORE_IMPLEMENTATION')
req('V2-R2','Weak completeness/self-check calibration; Evidence-aware completeness verification',['F8'],['B'],'Internal complete=true có thể đi cùng benchmark-incomplete; 15 controller success chưa complete.','Quyết định complete/success phản ánh phạm vi evidence và các ý được trả lời, phân biệt insufficient evidence với omitted supported content.','Frozen Phase 4E mismatch có 17 trường hợp, nên đủ lý do refine requirement.','Checker quá bảo thủ, lặp sửa không cần thiết hoặc học lén gold; internal check không thể giả định biết benchmark labels.','On separately designed cases, predeclare calibration matrix and stop-status definitions, preserve each check/answer stage; benchmark labels stay evaluator-side.','REFINE')
req('V2-R3','Possible goal persistence from missing aspect → evidence → answer',['F9'],['C'],'Missing aspects dẫn tới subqueries, final evidence mở rộng nhưng final check chỉ mô tả những ý đã có trong answer.','Mỗi aspect đã nêu cần có kết cục rõ: được trả lời có hỗ trợ, chưa đủ evidence, hoặc ngoài phạm vi với lý do.','Một diagnostic gợi ý khoảng trống; chưa xác nhận thành problem tổng quát.','Ép trả lời mọi aspect tự sinh, đưa evidence không áp dụng vào answer hoặc overfit domain y tế.','requires confirmation on a separately designed challenge set; cross-domain aspect-to-evidence-to-answer review with explicit relevance/applicability, without hardcoded medical rules.','INVESTIGATE_BEFORE_IMPLEMENTATION')
req('V2-R4','Evidence Expansion efficiency; More selective / higher-value expansion policy',['F1','F6','F7'],['A','B'],'9/31 R2 expansions; 11 additional retrievals and 9 merge-reranks; macro AC tie with A2.','Expansion chỉ nên tiêu thêm công khi có cơ sở kỳ vọng bổ sung evidence liên quan và cải thiện answer, với budget và lợi ích quan sát được.','Weak aggregate contribution relative to measured retrieval work justifies examining selectivity, not deleting expansion.','Trigger quá chặt bỏ lỡ evidence phân tán; trigger quá rộng tốn công; one-run differences confound effects.','Future predeclared comparison of evidence gains/losses, final point support, calibration, safety and retrieval/merge cost on independent cases and repeated runs. No automatic increase in retrieval rounds.','INVESTIGATE_BEFORE_IMPLEMENTATION')
req('V2-R5','Hard-query evaluation gap; Separate challenge/hard-query benchmark',['F1','F2','F4','F7','F8','F9'],['A','B','C'],'Current frozen 31 queries give historical evidence but limited observed mechanism exposures; one broad exploratory query has no gold.','Thiết kế dataset riêng cho broad/open-ended, multi-aspect, multi-article, dispersed evidence, initial Top-5 partial, synthesis, omission risk và decomposition/reformulation opportunity.','Đủ lý do mở rộng phạm vi đánh giá nghiên cứu; không chứng minh benchmark hiện tại easy.','Selection theo lỗi v1, contamination từ chatbot diagnostic, tối ưu riêng challenge hoặc thay benchmark lịch sử.','Predeclare dataset, annotation/applicability criteria, splits, metrics and repeated-run protocol before running v2; retain frozen 31 as primary historical benchmark. No dataset created in 5C.1.','INVESTIGATE_BEFORE_IMPLEMENTATION')
req('V2-R6','Historical comparability and stochastic attribution',['F3','F4','F5','F6'],['A'],'R1→R2 shows material variation; frozen precedence safeguards block stronger labels.','Giữ frozen historical benchmark, provenance, paired point transitions, macro/micro safety, separate call ledgers và predeclared attribution rules; future design must account for repeated runs.','Traceability and replication prevent interpreting small single-run differences as proven contribution.','Cost of future repeated runs; retrospective selection or changing labels from new outcomes.','Audit protocol/design before future execution; show all runs and query-sampling vs generation/judge uncertainty separately.','KEEP_AS_IS')
problem_map = [
 {'problem_id':'P1','problem':'Generation omission','evidence':['F2','F5'],'strength':'Tier A frozen omission evidence; revision contribution insufficient','candidate_requirement':'V2-R1','ready_for_v2_design':'YES — hypothesis/validation design only'},
 {'problem_id':'P2a','problem':'Weak completeness/self-check calibration','evidence':['F8'],'strength':'Tier B observational mismatch','candidate_requirement':'V2-R2','ready_for_v2_design':'YES — refine requirement, no implementation'},
 {'problem_id':'P2b','problem':'Explicit missing-aspect carry-through gap','evidence':['F9'],'strength':'Tier C exploratory only','candidate_requirement':'V2-R3','ready_for_v2_design':'YES — confirmation-study design only; problem unconfirmed'},
 {'problem_id':'P3','problem':'Evidence Expansion efficiency','evidence':['F1','F6','F7'],'strength':'Tier A weak aggregate result plus Tier B usage; no established causal utility','candidate_requirement':'V2-R4','ready_for_v2_design':'YES — candidate criteria and validation design only'},
 {'problem_id':'P4','problem':'Hard-query evaluation gap','evidence':['F1','F2','F4','F7','F8','F9'],'strength':'A/B motivate evaluation coverage; C generates hypotheses only','candidate_requirement':'V2-R5','ready_for_v2_design':'YES — evaluation requirement, not production mechanism'},
 {'problem_id':'P5','problem':'Attribution and historical comparability','evidence':['F3','F4','F5','F6'],'strength':'Tier A single replication plus frozen safeguards','candidate_requirement':'V2-R6','ready_for_v2_design':'YES — preserve research constraints'}
]
for row in problem_map:
    row['status'] = next(r['status'] for r in requirements if r['requirement_id']==row['candidate_requirement'])
write('phase5c1_problem_requirement_map_v0.json', {'schema':'phase5c1-problem-requirement-map-v0','decision_classes':['KEEP_AS_IS','REFINE','INVESTIGATE_BEFORE_IMPLEMENTATION','DEFER','REJECT'],'planning_only':True,'problem_requirement_map':problem_map,'candidate_requirements':requirements})

# Report opens with the requested timeline, then follows the 17 requested sections.
timeline = table(['Phase','Question','Main result','Evidence tier','Status'],[
 ['Corpus','Có nền dữ liệu cố định để nghiên cứu? ',f"corpus-v0.1: {corpus['document_count']} documents, {corpus['article_count']} articles, {corpus['chunk_count']} chunks; {corpus['error_count']} errors, {corpus['warning_count']} warnings",'A — frozen validation artifact','Historical validation passed; unchanged'],
 ['Retrieval','Localization có đủ cho full answer?',f"Article Hit@5 {number(reranker['article_level']['hit_at_5'])}; chunk Recall@5 {number(reranker['chunk_level']['recall_at_5'])}",'A','Historical frozen'],
 ['Standard RAG','Top-5 → answer đủ ý?',f"AC macro {number(r0m['answer_completeness']['macro'])}; {r0m['supported_point_count']}/102",'A','R0 frozen'],
 ['Failure Analysis','Failure nằm ở đâu?',f"Primary causes: {fa['aggregate']['primary_failure_counts']}",'A — frozen point audit, descriptive','Phase 4A complete'],
 ['Agentic v1','Conditional intervention giúp ở đâu?',f"R1 AC macro {number(metrics['R1']['answer_completeness']['macro'])}; {metrics['R1']['answer_completeness']['raw']}; higher call cost",'A — historical comparison','R1 frozen; attribution limited'],
 ['Trace Analysis','Hành vi và self-check có khớp outcomes?',f"{cal['internal_complete_but_benchmark_incomplete']} internal-complete/benchmark-incomplete; {cal['success_status_but_benchmark_incomplete']} false-success pattern",'B','Phase 4E observational'],
 ['Controlled Ablation','Revision/expansion contribution vượt replication?',f"{final['valid_semantic_records']}/93 judgments; A1 và A2: Insufficient evidence",'A; trigger descriptions B','Phase 5B.2-F PASS'],
 ['Exploratory hard-query diagnostic','Missing aspects còn được theo dõi tới answer?', 'Expansion/revision used; E58 added to answer; E6/E26 unused; completeness=true','C','EXPLORATORY / NON-BENCHMARK / NON-CONFIRMATORY']])
lines = [timeline,'', '# Phase 5C.1 — Research Findings Consolidation', '', '## 1. Scope and methodology', '',
 'READ-ONLY RESEARCH SYNTHESIS. Chỉ tạo additive artifacts trong `data/evaluation/generation/phase5/phase5c1_v0/`. Phân tích các records, traces, frozen metrics và reports đã có; không thực hiện semantic judging, không chạy lại bootstrap, retrieval hay production. Network/API = 0; production = 0; evaluator = 0. Không thay corpus, gold, prompt, runtime, evaluator, benchmark hoặc interpretation Phase 5. Không chạy A3/A4.', '',
 'Authority: Phase 5A quy định interpretation; `phase5b2f_v0/` chứa final complete 93/93 benchmark. Các available-case outputs và run manifests ghi INCOMPLETE thuộc thời điểm trước recovery, không phải primary final analysis. Final canonical records dùng accepted v0 trước, nếu thiếu mới dùng accepted recovery v1; 64 + 29 judgments. Phase 5B ghi Phase 5C chưa bắt đầu là trạng thái lịch sử; 5C.1 này là synthesis mới, không sửa trạng thái trong nguồn.', '',
 'Tier A = controlled/frozen artifacts (không đồng nghĩa mọi historical comparison là causal); Tier B = observational traces; Tier C = diagnostic hypothesis. F7 dùng sealed traces nhưng phát biểu về hành vi nên xếp B. F2 dựa trên frozen point audit nên xếp A cho mô tả đếm, không nâng taxonomy thành thử nghiệm nhân quả. Confidence áp dụng cho allowed claim, không cho mọi suy diễn của finding.', '',
 'Kiểm kê trước bao phủ mọi preexisting regular file dưới project root, kể cả môi trường và hidden files; symlink ghi đích, không theo ra ngoài. Không có usable Git working tree. Đối chiếu local SHA-256, canonical production/source bindings, stored point transitions và sealed R2 traces; không import project modules. Chi tiết nguồn/hash ở '+link(OUT/'phase5c1_manifest_v0.json')+'.', '',
 '## 2. Research timeline', '', 'Bảng mở đầu thể hiện đường đi: corpus cố định → localization tốt nhưng thiếu full evidence → Standard bỏ ý → conditional agent → trace mismatch → controlled ablation giới hạn attribution → hypothesis ngoài benchmark. Không gộp các tầng bằng chứng.', '',
 '## 3. Standard RAG findings', '', '### F1 — Localization tương đối mạnh; retrieval chưa được giải quyết hoàn toàn', '',
 table(['Measurement / denominator','Frozen value'],[
 ['Union any-gold chunk coverage / 31 queries',number(union['chunk_level']['union_any_gold_coverage'])],
 ['Union full-gold chunk coverage / 31 queries',number(union['chunk_level']['union_full_gold_coverage'])],
 ['Union macro / micro candidate chunk recall',number(union['chunk_level']['union_macro_candidate_recall'])+' / '+number(union['chunk_level']['union_micro_candidate_recall'])],
 ['Union article any / full coverage',number(union['article_level']['union_any_gold_coverage'])+' / '+number(union['article_level']['union_full_gold_coverage'])],
 ['Reranker article Hit@5',number(reranker['article_level']['hit_at_5'])],
 ['Reranker exact chunk Hit@5 / Recall@5',number(reranker['chunk_level']['hit_at_5'])+' / '+number(reranker['chunk_level']['recall_at_5'])],
 ['Generation point annotated support: candidate / Top-5',f"{fa['aggregate']['candidate_had_sufficient_evidence']}/102 / {fa['aggregate']['top5_retained_sufficient_evidence']}/102"]]), '',
 'Candidate union là BM25@20 ∪ Dense@20 unranked; final RAG dùng reranked Top-5, không dùng RRF và không biến upper bound thành measured reranker quality. Retrieval denominator có 98 query-scoped gold chunk occurrences; generation có 102 required points. Article localization không bảo đảm đủ khoản/điểm hoặc synthesis. Nguồn: '+link(ROOT/'data/evaluation/results/candidate-union-v0_metrics.json')+', '+link(ROOT/'data/evaluation/results/bge-reranker-v2-m3-v0_metrics.json')+'.', '',
 '### F2 — Failures không chỉ nằm ở retrieval', '',
 table(['Primary point failure','Count / 102'],[[k,v] for k,v in fa['aggregate']['primary_failure_counts'].items()]), '',
 f"Standard hỗ trợ {r0m['supported_point_count']}/102 điểm, thiếu {fa['aggregate']['missing_points']}/102. Có {fa['aggregate']['generation_bottleneck_top5_sufficient_answer_incomplete']}/102 điểm mà Top-5 chứa toàn bộ annotated support nhưng answer vẫn bỏ ý. Đây là căn cứ trực tiếp cho Completeness-aware Answer Revision. Query/point identities: "+', '.join(r['query_id']+'/'+r['point_id'] for r in omissions)+'.', '',
 '28/102 points mất sufficient annotated support từ candidate → Top-5 là overlap diagnostic trên mọi điểm; 17/102 primary evidence-coverage failures là taxonomy của outcome. Không đồng nhất hai số. Citation 4 + no failure 56 = 60 supported points; 42 missing points thuộc 16 retrieval + 17 evidence + 9 generation. Primary causes là mutually exclusive, secondary causes thì không. Số partial points không xác định riêng từ binary labels.', '',
 'Đối chiếu phát hiện một cách diễn đạt không nhất quán trong report 4A: câu “pure retrieval miss is smaller” không được dùng để nói 16 nhỏ hơn 9. Bảng/JSON/point rows là authority cho các con số; nguồn cũ giữ nguyên byte. Nguồn: '+link(G/'failure_analysis_metrics_v0.json')+' và '+link(G/'failure_analysis_points_v0.jsonl')+'.', '',
 '## 4. Agentic v1 findings', '', '### F3 — Historical improvement, đặt ngay cạnh replication', '',
 table(['Run','AC macro','AC micro','Interpretation'],[['R0',number(r0m['answer_completeness']['macro']),f"{r0m['supported_point_count']}/102 = {number(r0m['answer_completeness']['micro'])}",'Historical Standard'],*[[a,number(metrics[a]['answer_completeness']['macro']),metrics[a]['answer_completeness']['raw']+' = '+number(metrics[a]['answer_completeness']['micro']), 'Historical Agentic' if a=='R1' else 'Same-configuration replication'] for a in ['R1','R2']]]), '',
 f"R0→R1 Δ macro {number(tr['answer_completeness']['macro_delta'])}; +{tr['answer_completeness']['net_required_point_gain']} net points (gained {tr['answer_completeness']['gained_required_points']}, lost {tr['answer_completeness']['lost_required_points']}). Ngay cạnh đó, R1→R2 Δ macro {number(rep['deltas']['answer_completeness']['macro'])}, net {rep['net_point_difference']}. Không quy historical gain cho một mechanism hay coi R1 là guaranteed performance.", '',
 table(['Metric','R0 macro','R1 macro','R0 pooled raw','R1 pooled raw'],[
 ['Citation completeness',number(r0m['citation_completeness']['macro']),number(metrics['R1']['citation_completeness']['macro']),'60/102',metrics['R1']['citation_completeness']['raw']],
 ['Citation correctness',number(r0m['citation_correctness']['macro']),number(metrics['R1']['citation_correctness']['macro']),'83/86',metrics['R1']['citation_correctness']['raw']],
 ['Groundedness',number(r0m['groundedness']['macro']),number(metrics['R1']['groundedness']['macro']),'83/86',metrics['R1']['groundedness']['raw']],
 ['Unsupported claim rate ↓',number(r0m['unsupported_claim_rate']['macro']),number(metrics['R1']['unsupported_claim_rate']['macro']),'3/86',metrics['R1']['unsupported_claim_rate']['raw']],
 ['Citation syntax validity',number(r0m['citation_syntax_validity']['rate']),number(metrics['R1']['citation_syntax_validity']['macro']),'30/31','31/31']]), '',
 'R1 macro safety nhìn thuận hơn nhưng pooled Groundedness 83/86→93/97 giảm, pooled UCR 3/86→4/97 tăng. Claim denominators khác nhau, không phải paired claim effects. Syntax validity tách khỏi semantic correctness; eval012 sửa được syntax trong R1 dù không dùng Citation Revision, nên không quy cải thiện này cho citation repair.', '',
 'R0 configured logical cost = 31 retrieval + 31 generation calls, không có measured HTTP ledger. R1 recorded trace cost = 38 retrieval + 108 production LLM calls, thêm 6 merge-reranks; overhead +22.58% retrieval và +248.39% LLM. Evaluator attempts không tính vào production. Không có token/currency/latency ledger đầy đủ để kết luận monetary cost. Nguồn: '+link(G/'agentic_trace_analysis_metrics_v0.json')+', '+link(G/'standard_rag_metrics_v0.json')+', '+link(F/'efficiency_v0.json')+'.', '',
 '## 5. Replication findings', '', '### F4 — Same-configuration stochastic variation là material', '',
 table(['Transition R1→R2','Count'],[['Gained',rep['gained_points']],['Lost',rep['lost_points']],['Net',rep['net_point_difference']],['Gross churn',rep['gross_churn']]]), '',
 'Gained: eval027/P4. Lost: eval002/P2, eval022/P2, eval026/P1. Gross churn giữ lại chuyển động bị che bởi net. Một single production run không đủ để coi mọi chênh lệch nhỏ là mechanism effect. Đây là một observed replication, không phải variance estimate, noise distribution, stochasticity CI hay số để trừ khỏi ablation delta.', '',
 table(['Metric','R1 macro','R2 macro','Δ R2−R1 macro','R1 pooled raw','R2 pooled raw'],[[key,number(metrics['R1'][key]['macro']),number(metrics['R2'][key]['macro']),number(rep['deltas'][key]['macro']),metrics['R1'][key]['raw'],metrics['R2'][key]['raw']] for key in ['citation_correctness','groundedness','unsupported_claim_rate','citation_syntax_validity']]), '',
 'Groundedness macro giảm nhưng pooled tăng; UCR macro tăng nhưng pooled giảm. Citation correctness giảm ở cả hai. Provider/backend, generation variation và semantic judge variation chưa tách được. Nguồn: '+link(F/'replication_R1_R2.json')+'; '+link(F/'point_transitions_R1_R2.jsonl')+'.']

for section, alias, title in [(6,'A1','Answer Revision evidence'),(7,'A2','Evidence Expansion evidence')]:
    c = contrasts[alias]
    b = bootstraps[alias]
    lines += ['',f'## {section}. {title}','','### '+('F5 — Descriptive positive signal' if alias=='A1' else 'F6 — Weak aggregate contribution'),'',
        table(['Scope','Queries / points','R2 macro AC',alias+' macro AC','R2 supported',alias+' supported'],[['Full set','31 / 102',number(c['metrics']['R2']['answer_completeness']['macro']),number(c['metrics'][alias]['answer_completeness']['macro']),c['metrics']['R2']['answer_completeness']['raw'],c['metrics'][alias]['answer_completeness']['raw']]]+[[s,v['query_count'].__str__()+' / '+str(v['required_point_denominator']),number(v['metrics']['R2']['answer_completeness']['macro']),number(v['metrics'][alias]['answer_completeness']['macro']),v['metrics']['R2']['answer_completeness']['raw'],v['metrics'][alias]['answer_completeness']['raw']] for s,v in c['strata'].items()]),'',
        f"Full-set micro: R2 {number(c['metrics']['R2']['answer_completeness']['micro'])}; {alias} {number(c['metrics'][alias]['answer_completeness']['micro'])}. Δ R2−{alias}: macro {number(c['deltas']['answer_completeness']['macro'])}; micro {number(c['deltas']['answer_completeness']['micro'])}. All quality deltas use R2−ablation; positive raw UCR favors ablation.",'',
        table(['Point transition','Count'],[[k,v] for k,v in c['point_transitions']['counts'].items()]+[['gross churn',c['gross_churn']],['net R2 contribution',c['net_R2_contribution']]]),'',
        'Changed point identities: '+json.dumps(c['point_transitions']['changed_point_ids'],ensure_ascii=False)+'.','',
        'R2-triggered query IDs: '+', '.join(c['triggered_query_ids'])+'. Triggered strata are descriptive post-treatment subsets, not randomized causal subgroups. Stochastic trigger disagreements: '+', '.join(c['stochastic_trigger_disagreement_query_ids'])+'.','',
        f"Frozen paired bootstrap 95% CI [{number(b['ci_lower'])}, {number(b['ci_upper'])}], observed mean {number(b['observed_delta'])}; {b['resamples']} paired-query resamples, seed {b['seed']}, n={b['sample_size']}. Chỉ đọc artifact bootstrap có sẵn. CI mô tả query-sampling uncertainty, không generation/judge stochasticity; không p-value hoặc significance claim.",'',
        f"Replication-attribution macro/net flag = {str(c['replication_attribution_flag']).lower()}; separate gross-churn flag = {str(c['replication_gross_churn_flag']).lower()}. Frozen interpretation: **{c['interpretation']}**. Giữ precedence Phase 5A §10; research planning status không thay frozen label.",'',
        table(['Safety metric','R2 macro',alias+' macro','R2 pooled raw',alias+' pooled raw'],[[key,number(c['metrics']['R2'][key]['macro']),number(c['metrics'][alias][key]['macro']),c['metrics']['R2'][key]['raw'],c['metrics'][alias][key]['raw']] for key in ['citation_correctness','groundedness','unsupported_claim_rate']]),'',
        'Nguồn: '+', '.join(link(F/n) for n in [f'contrast_R2_{alias}.json',f'bootstrap_R2_{alias}.json',f'point_transitions_R2_{alias}.jsonl','efficiency_v0.json'])+'.']
    if alias == 'A1':
        lines += ['','**Evidence ủng hộ giữ revision làm candidate:** only-R2=4, only-A1=0; 3 queries tốt hơn, 28 bằng, không query AC giảm; cả 4 gained points nằm trong 4 R2-used queries. Triggered 9/19 vs 5/19, trong khi 27 non-used queries 54/83 vs 54/83. Phase 4A xác nhận generation omission là failure class có thật. Điều này ủng hộ tiếp tục nghiên cứu chức năng revision, chưa chứng minh nên giữ nguyên policy.','',
        '**Evidence chống khẳng định chắc contribution:** replication churn 4 bằng contrast churn 4 kích hoạt safeguard dù macro/net flag false; CI chạm zero; 4 triggered queries; safety conflicts. Citation correctness và macro groundedness/UCR thuận A1, pooled groundedness/UCR thuận R2. eval007 dùng revision ở R2 nhưng A1 checker không muốn trigger; không phải cùng một draft được randomize.','',
        '**Cost:** R2 101 vs A1 94 production LLM calls; A1 tiết kiệm 7 (6.930693%). Bốn R2 revision branches gồm 4 repair + 4 dependent rechecks = 8 calls; A1 có một citation repair ở eval012 ngoài nhóm used, khiến net full-set saving là 7. Retrieval 42 vs 42; merge-rerank 9 vs 11 (A1 nhiều hơn 2 do run-path variation). Không biến 7 thành fixed cost mỗi revision.','',
        '**Recommendation: INVESTIGATE_BEFORE_IMPLEMENTATION (V2-R1).** Giữ Completeness-aware Answer Revision trong requirements research; chưa đủ cơ sở KEEP_AS_IS như một contribution đã xác nhận. Cần thiết kế đo recovery, safety và cost độc lập trước implementation.']
    else:
        lines += ['','**Có giúp ở triggered queries?** Có descriptive positive signal: 14/36 vs 11/36 ở 9 R2-used queries; 3 gained points đều ở eval014. Không chứng minh causal effect: stratum post-treatment và checks/generation vẫn stochastic. Ở 22 non-used queries, R2 49/66 vs A2 51/66; only-R2 eval007/P4, only-A2 eval022/P1,P2 và eval026/P1. Không quy các thay đổi non-used cho removal của expansion.','',
        '**Aggregate cải thiện?** Macro AC bằng nhau; R2 63/102 vs 62/102 chỉ net +1, only-R2 4 và only-A2 3, gross churn 7. A2 có safety summaries tốt hơn. Source conflict list trống vì classifier dùng các tiêu chí frozen; báo cáo này vẫn phơi bày macro tie, micro +1 và safety tradeoff mà không relabel.','',
        '**Overhead:** R2 retrieval 42 vs A2 31: saving 11 (26.190476%); merge-rerank 9 vs 0: saving 9; production LLM 101 vs 101: no LLM saving. Triggered LLM 31 vs 30 được bù bởi non-used 70 vs 71, nên không suy ra mọi per-query LLM cost bằng nhau.','',
        '**Stochastic confounding:** macro/net replication flag true (|0| ≤ |−0.026881720430| và |1| ≤ |−2|); gross-churn flag false (4 < 7). Bootstrap spans both signs; checker disagreement tại eval005b, eval011, eval029. Phase 4E bổ sung observation: 5/6 R1 expansions không đổi Top-5, không thêm annotated supporting chunks; đó là Tier B, không phủ định mọi expansion.','',
        '**Recommendation: INVESTIGATE_BEFORE_IMPLEMENTATION (V2-R4).** Đưa selectivity/value criteria vào design research; chưa chọn policy cụ thể, không tăng retrieval rounds và không kết luận Expansion unnecessary.']

lines += ['', '## 8. Controller/self-check findings', '', '### F7 — Usage trên sealed R2 traces', '',
 table(['Intervention','Used / 31','Rate','Query IDs'],[[k,f'{len(v)}/31',number(len(v)/31),', '.join(v) or 'None'] for k,v in triggers.items()]), '',
 'Đã đối chiếu từng R2 trace trên disk với embedded canonical record và production binding. Citation revision R2 = 0/31; historical R1 = 1/31. Answer revision R1 = 7/31 và expansion R1 = 6/31, khác R2. Many queries were resolved without invoking the corresponding intervention; ở đây “resolved” chỉ nghĩa controller đã trả output, không nghĩa benchmark-complete. Usage thấp không chứng minh ineffective; không gắn nhãn cả benchmark “easy”.', '',
 '### F8 — Tier B completeness calibration mismatch', '',
 table(['Internal completeness (last retained check)','Benchmark complete','Benchmark incomplete'],[['complete=true',cal['internal_complete_and_benchmark_complete'],cal['internal_complete_but_benchmark_incomplete']],['complete=false',cal['internal_incomplete_but_benchmark_complete'],cal['internal_incomplete_and_benchmark_incomplete']]]), '',
 f"Tổng 31. Internal complete=true có 17/30 benchmark-incomplete; controller success có {cal['success_status_but_benchmark_incomplete']}/{cal['status_breakdown']['success']['queries']} benchmark-incomplete. Hai tập không đồng nhất: eval001/014 có internal complete nhưng status insufficient_evidence. eval010 internal incomplete nhưng benchmark-complete. Controller `success` không đồng nghĩa benchmark-complete.", '',
 'False-success status query IDs: '+', '.join(cal['success_status_but_benchmark_incomplete_query_ids'])+'.', '',
 'Đây là calibration mismatch đã quan sát, không tự động là software bug. Internal checks dựa vào query/evidence còn benchmark dùng frozen required points. Initial checks bị overwritten trong bảy R1 revision cases; eval005b check cuối diễn ra trước citation edit. Không invent intermediate missing-point labels hoặc benchmark draft scores. Nguồn: '+link(G/'agentic_trace_analysis_metrics_v0.json')+' và '+link(G/'agentic_trace_analysis_v0.jsonl')+'.', '',
 '## 9. Exploratory chatbot diagnostic', '', '**EXPLORATORY / NON-BENCHMARK / NON-CONFIRMATORY — Tier C.** Query: '+chat['query']+'. Không thuộc 31-query benchmark, không có benchmark score và không được dùng để sửa kết luận Phase 5. Nguồn duy nhất: '+link(chat_path)+'. Đây là phân tích trace, không phải tư vấn pháp lý/y tế hay xác minh hiệu lực văn bản.', '',
 '### F9 — Chuỗi observation được xác minh', '',
 table(['Stage','Observed trace content'],[
 ['Missing aspects', '<br>'.join(chat['missing_aspects'])],
 ['Subqueries','<br>'.join(chat['sub_queries'])],
 ['Expansion','expansion_used=true; 2 subqueries; final Top-5 thêm E58, E6, E26 so với initial Top-5'],
 ['Draft','Chỉ nêu an toàn bệnh nhân, độ tin cậy và bảo vệ dữ liệu sức khỏe [E1]'],
 ['Revision','revision_used=true; answer thêm cơ chế giám sát thực chất của con người [E58]'],
 ['Final answer','Cites '+', '.join(cited)+'; E6, E2, E26 không được trích dẫn và các nội dung đặc thù của chúng không được nêu'],
 ['Final completeness','complete=true; missing_points=[]; reason chỉ nhắc E1 và E58; final_status=success']]), '',
 table(['New final evidence','Relation to detected gap','Answer usage / caveat'],[
 ['E58 — 142-2026-ND-CP_dieu-8_khoan-2_diem-b','Human oversight technical/operational mechanism; relevance to technical aspect','Added by revision. Context is criteria for high-risk list; do not infer unconditional application to all chatbots.'],
 ['E6 — 142-2026-ND-CP_dieu-43_khoan-1','Sector authorities establish detailed safety/risk/deployment standards; partial relation to missing technical standards','Not used; regulator duty, not concrete medical testing standard or direct developer duty.'],
 ['E26 — 142-2026-ND-CP_dieu-16_khoan-4','Limits on mandatory disclosure by providers/deployers when explaining/providing information; partial relation to legal duties','Not used; not a complete catalogue of developer obligations.']]), '',
 'E6/E26 cung cấp nội dung có liên quan một phần đến missing aspects nhưng answer không mang nội dung đó sang hoặc nói rõ phần còn chưa giải quyết. Không có căn cứ nói chúng đã đáp ứng đầy đủ missing aspects. Việc không cite mọi chunk tự nó không là lỗi; E2 cũng có thể không cần cho câu hỏi xây dựng chatbot. Revision thực sự mang E58 vào answer là counterevidence đối với giả thuyết “agent bỏ toàn bộ mục tiêu”.', '',
 '**Exploratory observation suggests a possible goal-persistence / evidence-to-answer coverage gap.** Mạnh hơn mức này là không được hỗ trợ. Final complete=true không có independent gold để chấm lại. Initial completeness payload không được lưu riêng; transition ghi hai checks nhưng không phục hồi được nguyên văn lý do trigger revision. Chỉ hypotheses/candidate V2-R3; **requires confirmation on a separately designed challenge set**. Không có medical rule, prompt sửa riêng hoặc subquery template riêng cho query này.', '',
 '## 10. Retrieval vs generation vs controller limitations', '',
 table(['Limitation','Definition','Evidence / boundary'],[
 ['Retrieval / final-evidence coverage','Evidence cần thiết không vào candidate hoặc final evidence','F1/F2: 81/102 candidate sufficient → 53/102 Top-5; distinguish candidate miss from selection loss. No evidence that all legal detail exists in corpus.'],
 ['Generation','Relevant supporting evidence present but answer omits its proposition','F2: 9 frozen points; F5 positive but insufficient attribution. F9 only partial related evidence, not confirmed omission gold.'],
 ['Controller/self-check','Sufficient/complete/stop decision does not track intended completeness','F8: Tier B mismatch. F9: Tier C possible missing-aspect carry-through gap, separately unconfirmed.']]), '',
 'Một query có thể có nhiều limitation; không sửa taxonomy frozen hoặc coi mọi unsupported claim là retrieval miss. Relevance, applicability, sufficient support, citation usage và answer coverage là các quan hệ khác nhau.', '',
 '## 11. Candidate Agentic v2 requirements', '', 'Chỉ behavior/evaluation requirements, không thiết kế implementation. Mỗi requirement có đúng một decision class; research design readiness không có nghĩa implementation readiness.']
for r in requirements:
    lines += ['', '### '+r['requirement_id'], '', '\n\n'.join(label+': '+(', '.join(r[key]) if isinstance(r[key],list) else r[key]) for label,key in [('Problem','problem'),('Evidence','evidence'),('Evidence tier','evidence_tier'),('Current behavior','current_behavior'),('Desired behavior','desired_behavior'),('Why justified','why_justified'),('Known risk','known_risk'),('How to evaluate later','how_to_evaluate_later'),('Status','status')])]
lines += ['', '## 12. Hard-query evaluation need', '',
 '**Research justification: YES — sufficient to DESIGN a separate challenge set.** F1/F2 chứng minh có evidence/coverage/omission limitations; F4 cho thấy cần nghiên cứu uncertainty; F7 cho thấy số lần quan sát mỗi mechanism hữu hạn. F8 hỗ trợ kiểm tra completeness calibration. F9 chỉ tạo hypothesis, không chứng minh prevalence hoặc benchmark thiếu độ khó. Retrieval artifact hiện đã có 8 queries được gắn “hard”; không relabel chúng hoặc phủ nhận độ khó sẵn có.', '',
 'Mục tiêu dataset tương lai: broad/open-ended queries; multi-aspect; multi-article; evidence dispersed; initial Top-5 partial; synthesis required; generation omission risk; query decomposition/reformulation opportunity. Đây là dimensions cần predeclare và annotate khi thiết kế, chưa chọn queries hay tạo gold/dataset trong 5C.1. Không chỉ tuyển câu hỏi v1 thất bại hoặc sao chép medical diagnostic thành bài thi v2.', '',
 '**Current 31-query frozen benchmark remains the primary historical benchmark.** Challenge set sau này là dataset mới, tách development/test và khai báo trước khi chạy system v2; goals, scope/applicability, metrics, repeated-run analysis và cost accounting phải có trước kết quả. Không thay/loại bỏ/retune frozen 31 queries. Đây là evaluation requirement V2-R5, không là production mechanism hay lý do tự động thêm retrieval rounds.', '',
 '## 13. Decision table', '',
 table(['Problem','Evidence','Strength','Candidate requirement','Ready for v2 design?'],[[x['problem'],', '.join(x['evidence']),x['strength'],x['candidate_requirement']+' — '+x['status'],x['ready_for_v2_design']] for x in problem_map]), '',
 'Decision classes chỉ phục vụ research planning. V2-R1/V2-R3/V2-R4/V2-R5 cần INVESTIGATE_BEFORE_IMPLEMENTATION; V2-R2 REFINE phát biểu về calibration; V2-R6 KEEP_AS_IS đối với historical safeguards. A3/A4 và citation-only mechanism work: DEFER trong decision log vì không thuộc phạm vi và exposure quá ít; không tạo thêm v2 capability bằng suy đoán.', '',
 '## 14. What is known', '',
 '**Confirmed / relatively well-supported within frozen scope:** F1 localization mạnh hơn full evidence coverage; F2 generation omission cùng tồn tại với retrieval/evidence failures; F3 historical AC improvement và cost overhead là các số quan sát đã reconcile; F4 same-configuration point churn/safety drift có thật trong cặp R1/R2. F7 usage counts verified, F8 calibration mismatch consistently observed, nhưng hai findings này vẫn Tier B và không causal.', '',
 '**Suggestive findings:** F5 descriptive positive revision signal ở used stratum; F6 expansion có triggered signal nhưng weak aggregate contribution và overhead. Cả hai frozen conclusions vẫn **Insufficient evidence**. Tier A của dữ liệu không xóa attribution safeguards.', '',
 '**Exploratory findings:** F9 possible missing-aspect carry-through gap; evidence chỉ từ một ad-hoc trace, partly related evidence không đủ tạo confirmed omission. Revision cũng cho thấy một aspect được đưa vào answer.', '',
 '## 15. What remains unknown', '',
 'Contribution nào tồn tại ổn định qua production/judge repetitions? Revision recover supported omissions bao nhiêu so với added unsupported claims? Checker bỏ sót do missing evidence, incomplete goals hay đánh giá wording? Expansion tăng final evidence value khi nào và có đáng cost không? Goal persistence có tái diễn trên nhiều domains với applicable evidence không? Broad questions cần phạm vi/gold thế nào để “complete” không vô hạn? Những câu hỏi này cần thiết kế đánh giá mới; current data không cung cấp causal estimates, calibrated uncertainty, token cost hoặc benchmark-equivalent draft/final effects.', '',
 '## 16. Limitations', '',
 '31 queries/102 points là một frozen historical set, không đại diện mọi legal task. Query-sampling bootstrap không là generation/judge variance. Chỉ một R1→R2 replication; historical environment/provider provenance không đầy đủ. Triggered strata post-treatment, không randomized; không trừ replication delta. Macro và pooled safety có thể đi ngược chiều do denominator/claim composition. AC và citation completeness trùng nhau ở dữ liệu này không làm hai metrics độc lập. Annotated support overlap có thể bỏ sót alternatives; binary point labels không đo partial support. Corpus validation PASS là structural validation của 3 documents/737 chunks, không chứng minh toàn bộ pháp luật/medical requirements đã có. Unretained intermediate checks không thể tái tạo; unquoted evidence không tự động là omission. Tier C không có independent gold và chỉ được dùng tạo hypothesis. Không có usable Git provenance; local hash integrity chứng minh bytes unchanged từ snapshot trước, không là cryptographic signed execution attestation.', '',
 '## 17. Recommendation for Phase 5C.2', '',
 '**Is there sufficient research justification to proceed to Phase 5C.2 — Agentic v2 Requirements & Challenge-Set Design? YES.** Justification là các failure classes và calibration mismatches đã quan sát, coupled với attribution uncertainty cần được xử lý bằng design; không phải tuyên bố v2 chắc chắn tốt hơn. Phase 5C.2 chỉ DESIGN: cụ thể hóa requirements có traceability, tiêu chí challenge-set, predeclared evaluation và confirmation criteria. Không code, không tạo dataset trong 5C.1, không chạy benchmark/API/production/evaluator và không đổi controller. STOP.', '',
 'Source registry và validation: '+link(OUT/'phase5c1_manifest_v0.json')+', '+link(OUT/'phase5c1_validation_v0.json')+', '+link(OUT/'integrity_before_after_v0.json')+'. Full evidence/requirements: '+link(OUT/'phase5c1_evidence_matrix_v0.json')+', '+link(OUT/'phase5c1_problem_requirement_map_v0.json')+'.']
write('phase5c1_research_synthesis_v0.md','\n'.join(lines)+'\n')

decisions = table(['Decision','Status','Evidence / reason'],[[r['requirement_id'],r['status'],', '.join(r['evidence'])+'; '+r['why_justified']] for r in requirements]+[
 ['Declare revision supported contribution','REJECT','F5; frozen churn safeguard and CI; label stays Insufficient evidence'],
 ['Delete expansion as useless','REJECT','F6; triggered +3 points, stochastic confounding, narrow benchmark'],
 ['Medical-specific prompt/template/rule','REJECT','F9 is exploratory; no tuning to ad-hoc query'],
 ['A3/A4 or citation mechanism implementation','DEFER','Outside 5C.1; R2 citation revision 0/31, R1 1/31; no controlled A3/A4 evidence'],
 ['Proceed to Phase 5C.2 design','INVESTIGATE_BEFORE_IMPLEMENTATION','YES for requirements/challenge-set design only; no code or dataset now']])
write('phase5c1_decision_log_v0.md','# Phase 5C.1 decision log\n\nResearch planning only. Both frozen Phase 5 mechanism labels: **Insufficient evidence**.\n\n'+decisions+'\n\nEvidence tiers never upgraded by planning status. P2a calibration (B) and P2b goal persistence (C) remain separate. No benchmark reinterpretation, implementation, extra run or new dataset. Historical report 4A wording conflict recorded against authoritative counts 16 retrieval / 9 generation without changing old bytes. Earlier INCOMPLETE manifests are historical; final 93/93 namespace is primary.\n\nAnswer Revision: retain as research candidate because used-stratum signal aligns with generation omissions; investigate because churn safeguard, CI and safety conflicts limit attribution; full-set cost delta 7 LLM calls. Expansion: investigate selective value because macro tie/net +1 costs 11 retrievals and 9 reranks; triggered signal does not establish causality.\n\nReady for 5C.2 DESIGN: YES. STOP.\n')

check('finding_ids', [f['finding_id'] for f in findings] == [f'F{i}' for i in range(1,10)])
check('tier_assignment', Counter(f['evidence_tier'] for f in findings) == {'A':6,'B':2,'C':1})
check('one_status_per_requirement', all(r['status'] in ['KEEP_AS_IS','REFINE','INVESTIGATE_BEFORE_IMPLEMENTATION','DEFER','REJECT'] for r in requirements))
check('all_findings_have_source_bindings', all(p in sources for f in findings for p in f['supporting_artifacts']))
check('all_read_sources_preexisting', all(p in before['files'] for p in sources))
check('read_source_hashes_match_before', all(v['sha256'] == before['files'][p]['sha256'] for p,v in sources.items()))
check('report_starts_with_timeline', lines[0].startswith('| Phase | Question | Main result | Evidence tier | Status |'))
check('report_17_sections', all(f'## {i}. ' in '\n'.join(lines) for i in range(1,18)))
write('phase5c1_validation_v0.json', {'status':'PASS','method':'Local stored-object, integer-set, label-count, source-hash and document-structure reconciliation only; no semantic evaluator or bootstrap execution','checks':checks,'check_count':len(checks),'calls':{'network_api':0,'production':0,'evaluator':0},'limitations':['No OS-level packet capture; zero calls describes this workflow, not historical execution.','Source hashing does not prove model correctness or causal attribution.']})
write('phase5c1_manifest_v0.json', {'schema':'phase5c1-manifest-v0','created_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'phase':'5C.1','scope':'READ-ONLY RESEARCH SYNTHESIS; additive output only','status':'PASS','source_authority':{'design':str((P/'phase5a_ablation_spec_v0.md').relative_to(ROOT)),'final_primary_namespace':str(F.relative_to(ROOT)),'previous_available_case_diagnostics':'non-primary historical; retained unchanged'},'source_count':len(sources),'sources_reviewed':sources,'evidence_findings_by_tier':{t:[f['finding_id'] for f in findings if f['evidence_tier']==t] for t in ['A','B','C']},'frozen_labels':{a:contrasts[a]['interpretation'] for a in contrasts},'network_api_calls':0,'production_calls':0,'evaluator_calls':0,'new_bootstrap_runs':0,'benchmark_reruns':0,'A3_A4_runs':0,'implementation_changes':False,'challenge_dataset_created':False,'benchmark_replaced':False,'ready_for_phase5c2_design':True,'phase5c2_started':False,'output_namespace':str(OUT.relative_to(ROOT)),'integrity':'See integrity_before_after_v0.json; complete project scope, not only sources','artifact_hashes':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(OUT.iterdir()) if p.is_file()},'hash_coverage_note':'Manifest binds already-written analysis artifacts; final_artifact_hashes_v0.json binds manifest, integrity and console without circular self-hashing.'})
print(json.dumps({'synthesis_written':True,'sources':len(sources),'checks':len(checks),'next':'final whole-project before/after integrity and console sealing'},ensure_ascii=False))
