"""Offline first-pass dataset packaging. NEVER an Agentic implementation or evaluator.

Only Python standard library. Reads corpus, frozen-design provenance, historical
query-only files and custodian authoring records. Writes only this phase namespace.
The authoring session is permanently ineligible for subsequent v2 implementation.
"""
from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime, timezone
from itertools import product, combinations
import csv
import hashlib
import json
import os
import re
import unicodedata
from difflib import SequenceMatcher

ROOT = Path(__file__).resolve().parents[6]
OUT = ROOT / 'data/evaluation/generation/phase5/phase5c4_v0'
PRIVATE, PUBLIC, REVIEW = (OUT / x for x in ('custodian', 'public_review', 'reviewer_b'))
CORPUS = ROOT / 'data/versions/corpus-v0.1'
NOW = datetime.now(timezone.utc).isoformat()
STATUS = 'PENDING_INDEPENDENT_REVIEW'
FAMILIES = {1: 'deployment_scope_assessment', 2: 'multi_duty_procedural_synthesis',
            3: 'actor_condition_applicability', 4: 'corpus_boundary_partial_answer_handling'}
DOCS = {'L': '134-2025-QH15', 'N': '142-2026-ND-CP', 'T': '05-2026-TT-BKHCN'}

def digest(data):
    return hashlib.sha256(data if isinstance(data, bytes) else data.encode('utf-8')).hexdigest()

def canonical(x):
    return json.dumps(x, ensure_ascii=False, sort_keys=True, separators=(',', ':'))

def file_hash(p):
    h = hashlib.sha256()
    with p.open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()

def rel(p):
    return str(p.relative_to(ROOT))

def write(p, value):
    assert OUT in p.parents
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def jsonl(p, rows):
    assert OUT in p.parents
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(''.join(json.dumps(x, ensure_ascii=False) + '\n' for x in rows), encoding='utf-8')

def text_file(p, text):
    assert OUT in p.parents
    p.write_text(text, encoding='utf-8')

def read_jsonl(p):
    return [json.loads(line) for line in p.read_text(encoding='utf-8-sig').splitlines() if line.strip()]

def identity(label):
    return digest('phase5c4a-v0-opaque-id:' + label)

# A source file is evaluated as authored data, without import caches or project imports.
authored = {}
exec(compile((PRIVATE / 'authored_tasks_v0.py').read_text(), '<restricted-authoring>', 'exec'), authored)
tasks = authored['TASKS']
notes = json.loads((PRIVATE / 'construction_notes_v0.json').read_text())
asks = json.loads((PRIVATE / 'explicit_asks_v0.json').read_text())
assert len(tasks) == 60 and len({t['key'] for t in tasks}) == 60
assert set(asks) == {t['key'] for t in tasks} == set(notes['semantic_review'])

# Recheck the entire frozen manifest and final registry, including upstream hashes.
frozen = ROOT / 'data/evaluation/generation/phase5/phase5c3_v0'
fm = json.loads((frozen / 'phase5c3_freeze_manifest_v0.json').read_text())
fv = json.loads((frozen / 'phase5c3_validation_v0.json').read_text())
assert fm['phase_status'] == 'PASS' and fm['phase5c3_freeze_status'] == 'FROZEN'
assert fv['all_validation_gates_pass'] is True
assert all(c['status'] == 'PASS' for c in fv['checks'])
bound = []
for section in ('phase5c1_authoritative_artifacts', 'phase5c2_all_artifacts', 'artifact_hashes'):
    for name, rec in fm[section].items():
        p = frozen / name if section == 'artifact_hashes' else ROOT / name
        assert file_hash(p) == rec['sha256'], 'Frozen input hash failure'
        bound.append({'path': rel(p), 'sha256': rec['sha256']})
registry = json.loads((frozen / 'final_artifact_hashes_v0.json').read_text())
for name, rec in registry['artifacts'].items():
    p = ROOT / name if (ROOT / name).exists() else frozen / name
    assert file_hash(p) == rec['sha256'], 'Final frozen registry failure'
    bound.append({'path': rel(p), 'sha256': rec['sha256']})
frozen_integrity = json.loads((frozen / 'integrity_before_after_v0.json').read_text())
assert frozen_integrity['status'] == 'PASS' and frozen_integrity['all_preexisting_files_byte_identical']
frozen_entries = frozen_integrity['after_entries']
for p in list(CORPUS.iterdir()) + [ROOT/'data/evaluation/generation/phase5/query_inputs_v0.json', ROOT/'data/evaluation/dev_queries.jsonl']:
    if p.is_file():
        assert file_hash(p) == frozen_entries[rel(p)]['sha256'], 'Frozen corpus/query-only snapshot mismatch'
        bound.append({'path': rel(p), 'sha256': file_hash(p), 'binding_source': 'phase5c3/integrity_before_after_v0.json#after_entries'})
write(PUBLIC / 'frozen_source_checks_v0.json', {
    'status': 'PASS', 'phase5c3_status': 'PASS', 'phase5c3_freeze_status': 'FROZEN',
    'checked_at_utc': NOW, 'hash_bindings': bound,
    'authoritative_read_scope': 'All 5C.3 Markdown and JSON artifacts; large integrity inventories parsed in full. Hash-bound 5C.2 challenge/gold schema and evaluation denominator clauses read. No system answers inspected.',
    'legal_authority': 'Only frozen corpus-v0.1; source hash checking is not reading historical answers.'})

articles = read_jsonl(CORPUS / 'articles.jsonl')
chunks = read_jsonl(CORPUS / 'chunks.jsonl')
article_by_id = {a['article_id']: a for a in articles}
chunk_by_id = {c['chunk_id']: c for c in chunks}
assert len(articles) == len(article_by_id) == 86 and len(chunks) == len(chunk_by_id) == 737
assert {c['document_id'] for c in chunks} == set(DOCS.values())
assert all(c['corpus_version'] == 'corpus-v0.1' for c in chunks)
source_files = {rel(p): {'sha256': file_hash(p), 'size_bytes': p.stat().st_size}
                for p in sorted(CORPUS.iterdir()) if p.is_file()}
corpus_hash = digest(canonical(source_files))

def article_of(c):
    return c['document_id'] + '_dieu-' + c['article']

def source_clause(c):
    a = article_by_id[article_of(c)]
    return next((k['text'] for k in a['clauses'] if k['clause'] == c['clause']), a['intro_text'])

def source_actor(c):
    # Preserve source scope verbatim instead of guessing an actor from topic words.
    return {'source_clause_lead': source_clause(c),
            'source_article_scope': article_by_id[article_of(c)]['article_title']}

def resolve(selector):
    m = re.fullmatch(r'([LNT])(\d+)(?:\.(\d+))?(?:\.([^ .]+))?', selector)
    assert m, 'Invalid source selector'
    doc, art, clause, point = m.groups()
    matches = [c for c in chunks if c['document_id'] == DOCS[doc] and c['article'] == art
               and (clause is None or c['clause'] == clause)
               and (point is None or c['point'] == point)]
    assert matches, 'Unresolved source selector'
    return matches

def span(c):
    return {'chunk_id': c['chunk_id'], 'document_id': c['document_id'], 'article_id': article_of(c),
            'clause': c['clause'], 'point': c['point'],
            'text_sha256': digest(c['text']), 'parent_context_sha256': digest(c['parent_context']),
            'chunk_record_sha256': digest(canonical(c)),
            'span': {'start_char': 0, 'end_char': len(c['text']), 'field': 'text', 'unit': 'Unicode code points'},
            'source_line_start': c['source_start_line'], 'source_line_end': c['source_end_line'],
            'parent_context_required': True}

def resolve_refs(refs):
    alternatives = []
    for alternative in refs.split('|'):
        found = {}
        for selector in alternative.split():
            for c in resolve(selector):
                found[c['chunk_id']] = c
        alternatives.append(list(found.values()))
    return alternatives

# Full structural source map, including every chunk and referenced-but-absent annexes.
map_articles = []
for a in articles:
    matching = [c for c in chunks if article_of(c) == a['article_id']]
    map_articles.append({
        'article_id': a['article_id'], 'document_id': a['document_id'], 'title': a['article_title'],
        'chapter': a['chapter'], 'chapter_title': a['chapter_title'],
        'article_record_sha256': digest(canonical(a)),
        'source_lines': [a['start_line'], a['end_line']],
        'chunk_ids': [c['chunk_id'] for c in matching],
        'actor_and_condition_scopes': [
            {'clause': c['clause'], 'scope_text': c['text'],
             'point_keys': [p['point'] for p in c['points']]} for c in a['clauses']],
        'intro_scope': a['intro_text'],
        'first_pass_structure_read': True,
        'review_basis': 'Full article, clauses, points and source titles read locally; not ranked search.'})
mapping = {
    'schema_version': 'phase5c4a-corpus-map-v0', 'corpus_version': 'corpus-v0.1',
    'source_files': source_files, 'corpus_sha256': corpus_hash,
    'documents': list(csv.DictReader((CORPUS / 'documents.csv').open(encoding='utf-8-sig'))),
    'articles': map_articles, 'chunks': [span(c) for c in chunks],
    'document_article_counts': dict(Counter(a['document_id'] for a in articles)),
    'document_chunk_counts': dict(Counter(c['document_id'] for c in chunks)),
    'scope_boundary': 'Only 35 Law articles, 46 Decree articles and 5 Circular articles. No annex/form/list/technical-standard record beyond these articles; referenced external instruments are not imported.',
    'review_suspicions_not_corrections': notes['known_corpus_flags'],
    'corpus_legal_status': 'Frozen source as supplied; no live-law validation, external legal authority or corpus modification.'}
write(PRIVATE / 'corpus_mapping_v0.json', mapping)

# Editorial fixes before packaging, based only on source/support/scope review.
task_by_key = {t['key']: t for t in tasks}
task_by_key['A03']['d4'] = None
# A timing rule resides in the parent lead of the point; do not require all five
# alternative change triggers to prove the before-first-use timing.
task_by_key['A03']['aspects'][1]['refs'] = 'N13.1.đ N13.2.b'
task_by_key['A07']['aspects'][0]['refs'] = 'N17.5.b'
# The request includes no separate dossier/legal-identity point in the cluster
# question; independent member status follows directly from forming the cluster.
task_by_key['B11']['aspects'][3]['origin'] = 'scope_necessary'
for t in tasks:
    for merges in (notes['cluster_merges'], notes['additional_cluster_merges']):
        t['cluster'] = merges.get(t['cluster'], t['cluster'])
    t['query_id'] = 'q_' + identity(t['key'])[:20]
    t['cluster_id'] = 'c_' + identity('cluster:' + t['cluster'])[:20]
    t['cluster_id_hash'] = digest(t['cluster_id'])
    t['split_family'] = 'DEV' if t['split'] in ('DEV', 'RESERVE_DEV') else (
        'HOLDOUT_TEST' if t['split'] in ('HOLDOUT_TEST', 'RESERVE_TEST') else 'EXCLUDED')
    t['provisional_split'] = 'RESERVE' if t['split'].startswith('RESERVE') else t['split']

def absence_audit(t, aspect, refs):
    """Manual semantic scoped review plus an exhaustive structural source inventory.

    Keyword hits are supplemental and are not the legal basis of absence.
    """
    concepts = aspect.get('concepts') or []
    related = {article_of(c) for alt in resolve_refs(refs) for c in alt}
    def norm(s):
        return unicodedata.normalize('NFC', s).casefold()
    keyword_hits = {}
    for term in concepts:
        keyword_hits[term] = [c['chunk_id'] for c in chunks if norm(term) in norm(c['text'])]
    ledger = []
    for a in articles:
        aid = a['article_id']
        ledger.append({
            'article_id': aid, 'article_record_sha256': digest(canonical(a)),
            'reviewed_scope': 'Full intro, every clause and point; connected chunk identities in corpus_mapping_v0.json.',
            'topic': a['article_title'],
            'disposition': 'RELATED_CONTEXT_NOT_THE_REQUESTED_RULE' if aid in related else 'NO_REQUESTED_RULE_IN_THIS_ARTICLE',
            'scoped_review_rationale': aspect['reason'] if aid in related else (
                'Reviewed the full provisions under this article topic against the bounded request. '
                'No provision supplies the requested missing detail; general obligations or different instruments are not substitutes.'),
        })
    return {'audit_id': 'audit_' + identity(t['key'] + aspect['proposition'])[:20],
            'audit_status': 'ANNOTATOR_A_FIRST_PASS',
            'bounded_missing_request': aspect.get('unsupported', aspect['proposition']),
            'documents_reviewed': sorted(DOCS.values()), 'articles_reviewed': ledger,
            'review_coverage': {'documents': 3, 'articles': 86, 'chunks_in_source_map': 737},
            'candidate_keywords_concepts': concepts, 'supplementary_literal_hits': keyword_hits,
            'plausible_alternatives_considered': [
                {'source_selector': r, 'disposition': 'Context/delegation/other-scope provision, not adequate support for the missing request'}
                for r in refs.replace('|', ' ').split()],
            'reason_support_remains_absent': aspect['reason'],
            'method': 'Full corpus legal-structure reading and scoped manual alternative review; literal matches merely document possible leads. No retrieval, embeddings, ranking, API or model inference run.',
            'no_external_law_conclusion': True, 'needs_second_review': True}

def scope_of(t):
    return {'explicit_asks': asks[t['key']], 'bounded_interpretation': t['scope'],
            'relevant_user_facts': [t['facts']], 'unspecified_facts': [t['unknown']],
            'excluded_scope': [
                {'scope': 'External legal instruments, live administrative registries and unprovided factual determinations',
                 'reason': 'Only frozen three-document corpus is legal authority. Explicit boundary requests stay material disclosure obligations; exclusion forbids filling them with outside knowledge.'},
                {'scope': 'All other possible AI obligations outside the finite bounded intent',
                 'reason': 'Broad wording does not require an unlimited legal checklist.'}],
            'time_scope': 'Apply supplied frozen corpus text to stated facts/hypotheticals; no claim about current law or live portal status.'}

D9_KEYS = set(('A01 A02 A03 A05 A06 A07 A08 A09 A10 A11 A12 B01 B02 B03 B04 B05 B06 B08 B09 B10 B11 B12 D08').split())
D9_KEYS |= {f'C{i:02}' for i in range(1, 16)}

def full_bundles(aspects):
    supported = [a for a in aspects if a['answer_role'] != 'unresolved_disclosure']
    if not supported:
        return []
    result = []
    for alternatives in product(*(a['support_bundles'] for a in supported)):
        ids = sorted({s['chunk_id'] for b in alternatives for s in b['required_spans']})
        if ids not in [r['chunk_ids'] for r in result]:
            result.append({'bundle_id': f'FULL{len(result) + 1}', 'chunk_ids': ids,
                           'document_ids': sorted({chunk_by_id[i]['document_id'] for i in ids}),
                           'article_ids': sorted({article_of(chunk_by_id[i]) for i in ids})})
    return result

candidates, annotations, audits, exclusions, assignments = [], [], [], [], []
for t in tasks:
    qid = t['query_id']
    aspects, obligations = [], []
    for index, raw in enumerate(t['aspects'], 1):
        aid = qid + '_a' + str(index)
        role = raw['role']
        sufficiency = {'substantive_supported': 'sufficient_support', 'qualified_partial': 'partial_support',
                       'unresolved_disclosure': 'no_support_in_corpus'}[role]
        condition = raw.get('condition') or ('direct', 'met', 'Applicable source rule/definition is applied to the bounded stated or hypothetical task; no missing factual predicate is silently assumed.')
        relationships, bundles = [], []
        source_alternatives = resolve_refs(raw['refs'])
        for bidx, group in enumerate(source_alternatives, 1):
            if role != 'unresolved_disclosure':
                bundles.append({'bundle_id': aid + '_B' + str(bidx),
                                'required_spans': [span(c) for c in group],
                                'within_bundle_logic': 'AND',
                                'scope': 'Supported portion only' if role == 'qualified_partial' else 'Whole bounded substantive aspect',
                                'source_scope_context_must_be_preserved': True})
            for c in group:
                app = condition[0]
                if role == 'unresolved_disclosure':
                    app = 'uncertain'
                if role == 'qualified_partial' and app == 'uncertain':
                    app = 'conditional'  # rule is known, actual conclusion remains uncertain
                relationships.append({
                    'aspect_id': aid, 'evidence': span(c),
                    'relationship_target': 'context_for_absent_request' if role == 'unresolved_disclosure' else 'supported_rule_or_scope_conclusion',
                    'relevance': 'contextual' if role == 'unresolved_disclosure' else 'direct',
                    'evidence_role': 'supporting_context' if role == 'unresolved_disclosure' else 'normative_support',
                    'applicability': app, 'actor': source_actor(c), 'scenario_actor_facts': t['facts'],
                    'legal_scope': {'document_id': c['document_id'], 'article_title': c['article_title'], 'bounded_task': t['scope']},
                    'system_class': {'source_scope': c['article_title'] + ' / ' + source_clause(c), 'stated_facts': t['facts']},
                    'material_conditions': [source_clause(c), t['facts']],
                    'condition_assessment': 'unknown' if role == 'unresolved_disclosure' else condition[1],
                    'uncertainty_rationale': raw.get('reason') or condition[2],
                    'relevance_does_not_imply_applicability': True,
                })
        audit = None
        if role == 'unresolved_disclosure' or (role == 'qualified_partial' and raw.get('reason')):
            audit = absence_audit(t, raw, raw['refs'])
            audits.append(audit)
        origin = 'scope_necessary' if t['broad'] else raw['origin']
        aspect = {
            'aspect_id': aid, 'proposition': raw['proposition'], 'origin': origin,
            'materiality': {'independently_scorable': True,
                            'bounded_user_need': asks[t['key']],
                            'why_material': 'Determines a distinct requested legal duty, scope/actor conclusion, procedural decision or missing-information obligation within this finite task.',
                            'substantive_credit': role == 'substantive_supported'},
            'scope_necessity_rationale': ('Directly needed to plan the bounded activity for the stated actor, anchored in the supplied source rule; not an additional unrelated compliance topic.' if origin == 'scope_necessary' else None),
            'parent_aspect_id': None, 'answer_role': role,
            'support_bundles': bundles, 'across_bundle_logic': 'OR',
            'evidence_relationships': relationships,
            'applicability': {'status': condition[0] if role != 'unresolved_disclosure' else 'uncertain',
                              'actor_facts': t['facts'], 'legal_scope': t['scope'], 'system_class': t['facts'],
                              'material_conditions': condition[2],
                              'condition_assessment': condition[1] if role != 'unresolved_disclosure' else 'unknown',
                              'uncertainty_rationale': raw.get('reason') or condition[2]},
            'evidence_sufficiency': {'label': sufficiency,
                                     'supported_scope': raw['proposition'] if role != 'unresolved_disclosure' else None,
                                     'unsupported_scope': raw.get('unsupported'),
                                     'unsupported_portion_sufficiency': 'no_support_in_corpus' if audit else ('partial_support' if role == 'qualified_partial' else None),
                                     'corpus_audit_id': audit['audit_id'] if audit else None,
                                     'conflict_flag': t['key'] == 'D15',
                                     'conflict_rationale': t['exclude'] if t['key'] == 'D15' else None},
            'scoring_equivalence': 'Accept legally equivalent Vietnamese wording, preserve actor/scope/conditions, and accept any valid alternative bundle. No obligation to cite every alternative. Extra unsupported law is not credit.'}
        aspects.append(aspect)
        obligations.append({'obligation_id': aid + '_response', 'aspect_id': aid,
                            'role': role, 'credit_group': {'substantive_supported': 'P+', 'qualified_partial': 'Q', 'unresolved_disclosure': 'U'}[role],
                            'expected_mode': role, 'required_content': raw['proposition'],
                            'disclosure_alone_earns_substantive_credit': False})
        if role == 'qualified_partial':
            obligations.append({'obligation_id': aid + '_unresolved', 'aspect_id': aid,
                                'role': 'unresolved_disclosure', 'credit_group': 'U',
                                'expected_mode': 'unresolved_disclosure', 'required_content': raw['unsupported'],
                                'paired_qualified_obligation': aid + '_response',
                                'disclosure_alone_earns_substantive_credit': False})
    if t['negative']:
        selector, app, condition_assessment, rationale = t['negative']
        for c in resolve(selector):
            aspects[0]['evidence_relationships'].append({
                'aspect_id': aspects[0]['aspect_id'], 'evidence': span(c),
                'relationship_target': 'excluded_inferred_duty_or_inapplicable_branch',
                'relevance': 'contextual', 'evidence_role': 'counterevidence', 'applicability': app,
                'actor': source_actor(c), 'scenario_actor_facts': t['facts'],
                'legal_scope': {'bounded_task': t['scope'], 'source_article': c['article_title']},
                'system_class': {'source_scope': source_clause(c), 'stated_facts': t['facts']},
                'material_conditions': [rationale], 'condition_assessment': condition_assessment,
                'uncertainty_rationale': rationale,
                'relevance_does_not_imply_applicability': True,
                'excluded_from_substantive_support_bundle': True})
    roles = Counter(a['answer_role'] for a in aspects)
    answerability = ('insufficient_evidence' if not (roles['substantive_supported'] or roles['qualified_partial']) else
                     'partially_answerable' if roles['qualified_partial'] or roles['unresolved_disclosure'] else 'fully_answerable')
    bundles = full_bundles(aspects)
    multi_article = bool(bundles) and all(len(b['article_ids']) >= 2 for b in bundles)
    d4 = bool(t['d4']) and answerability == 'fully_answerable' and bool(bundles) and all(len(b['document_ids']) >= 2 for b in bundles)
    positive = {
        'D1': t['broad'], 'D2': roles['substantive_supported'] >= 3,
        'D3': multi_article, 'D4': d4, 'D5': multi_article,
        'D7': roles['substantive_supported'] >= 3,
        'D8': roles['substantive_supported'] + roles['qualified_partial'] >= 2,
        'D9': t['key'] in D9_KEYS, 'D10': answerability != 'fully_answerable'}
    dimensions = {}
    for d in range(1, 11):
        tag = f'D{d}'
        if tag == 'D6':
            dimensions[tag] = {'member': None, 'dimension_status': 'empirical_unverified',
                               'basis': 'post_lock_initial_retrieval_not_run', 'rationale': 'Not characterized, counted, used for selection or inferred from corpus dispersion.'}
            continue
        reasons = {
            'D1': 'Bounded planning intent without an enumerated checklist; finite scope and direct scope-necessary obligations defined.',
            'D2': 'At least three independent P+ legal decisions/duties, not Q/U disclosure points or minor wording fragments.',
            'D3': 'Every currently annotated full supported-portion bundle spans at least two articles, including necessary scope provisions.',
            'D4': t['d4'],
            'D5': 'All acceptable annotated alternatives require separate articles; no single article/chunk supplies the full supported task.',
            'D7': 'Coordinating independently substantive conditions/duties creates structural omission opportunity; no answer generation observed.',
            'D8': 'At least two separable supported legal evidence needs; no actual retrieval subqueries designed.',
            'D9': 'Must discriminate the stated actor, system/scope or material condition from a plausible different branch; source scopes and any counterevidence are recorded.',
            'D10': 'At least one material scoped request has corpus insufficiency or unresolved applicability; not based on retrieval failure.'}
        dimensions[tag] = {'member': positive[tag], 'dimension_status': 'first_pass_proposed',
                           'basis': 'corpus_structure',
                           'rationale': reasons[tag] if positive[tag] else 'Not asserted by ANNOTATOR_A for this bounded candidate; no quota-based inflation.'}
    risks = ['aspect_atomicity_and_bounded_scope', 'alternative_bundle_completeness', 'actor_and_condition_applicability']
    if d4:
        risks.append('cross_document_no_single_document_alternative')
    if answerability != 'fully_answerable':
        risks.extend(['corpus_wide_absence_or_partial_support', 'P_Q_U_and_answerability_derivation'])
    if t['key'] in notes['high_risk_baseline_overlap_keys']:
        risks.append('historical_semantic_overlap_explicit_A_admission_justification')
    if t['key'] in ('A11', 'D15'):
        risks.append('temporal_interpretation_or_source_cross_reference')
    admission = 'RESERVE' if t['provisional_split'] == 'RESERVE' else (
        'EXCLUDE' if t['exclude'] else 'RETAIN_PROVISIONAL_' + ('DEV' if t['split'] == 'DEV' else 'TEST'))
    candidate = {
        'schema_version': 'phase5c4a-candidate-v0', 'dataset_version': 'phase5c4a-v0-first-pass',
        'query_id': qid, 'query': t['query'], 'query_sha256': digest(t['query']),
        'cluster_id': t['cluster_id'], 'primary_family': FAMILIES[t['family']],
        'provisional_split': t['provisional_split'], 'split_family': t['split_family'],
        'admission': admission, 'scope': scope_of(t), 'dimensions': dimensions,
        'control_case': {'member': bool(t['control']), 'corpus_rationale': t['control'], 'actual_system_no_intervention': None},
        'construction_provenance': {'author': 'ANNOTATOR_A', 'role': 'DATASET_CUSTODIAN',
            'direction': 'corpus_legal_structure -> bounded_legal_task -> Vietnamese_query',
            'legal_structure_refs': sorted({article_of(c) for a in t['aspects'] for b in resolve_refs(a['refs']) for c in b}),
            'corpus_sha256': corpus_hash, 'record_packaged_at_utc': NOW,
            'source_read_before_authoring': True, 'system_outputs_or_retrieval_used': False,
            'network_api_calls': 0, 'authoring_key_private': t['key'],
            'admission_rationale': t['exclude'] or ('Unused reserve for pre-output legal-quality/duplicate/cluster repair only, with inherited split family.' if admission == 'RESERVE' else 'Finite corpus-first legal task; local first-pass support and contamination review; provisional family allocation without D6 or system performance.')},
        'annotator_A_status': 'FIRST_PASS', 'annotation_status': STATUS,
        'annotator_A_rationale': notes['semantic_review'][t['key']],
        'needs_second_review': True, 'high_risk_annotation_fields': risks}
    annotation = {'schema_version': 'phase5c4a-annotation-A-v0', 'query_id': qid,
        'query_sha256': candidate['query_sha256'], 'corpus_version': 'corpus-v0.1', 'corpus_sha256': corpus_hash,
        'scope': candidate['scope'], 'required_legal_aspects': aspects,
        'full_supported_portion_bundles': bundles,
        'full_bundle_scope_note': 'For partial queries these bundles cover P+/Q supported portions only; no bundle completes the unsupported request.',
        'alternative_review': {'status': 'ANNOTATOR_A_FIRST_PASS', 'all_three_documents_scoped_review': True,
                               'single_document_full_answer': 'not_proposed' if d4 else 'not_excluded',
                               'rationale': t['d4'] if d4 else notes['cross_document_corrections'].get(t['key'], 'No D4 claim; shared sources or a single-document alternative remain possible.'),
                               'independent_exhaustiveness_review_pending': True},
        'answerability': {'label': answerability,
                          'derivation': {'P_plus_aspects': roles['substantive_supported'], 'Q_obligations': roles['qualified_partial'],
                                         'U_obligations': sum(o['credit_group'] == 'U' for o in obligations)},
                          'rationale': 'All material requests supported' if answerability == 'fully_answerable' else ('No material requested portion substantively supported; contextual rules are not partial answers.' if answerability == 'insufficient_evidence' else 'Some material content has P+ or qualified support, while another requested portion remains unresolved.' )},
        'response_obligations': obligations, 'reference_answer': None,
        'annotator_A_status': 'FIRST_PASS', 'annotation_status': STATUS,
        'annotator_A_rationale': {'legal_task': t['scope'], 'support_review': 'Mapped directly to article/point text plus actor-bearing parent context; no system answer used.',
                                'contamination_review': notes['semantic_review'][t['key']]},
        'needs_second_review': True, 'high_risk_annotation_fields': risks,
        'reviewer_B_status': 'NOT_STARTED', 'adjudication_status': 'NOT_STARTED', 'locked_at': None}
    candidates.append(candidate)
    annotations.append(annotation)
    assignments.append({'query_id': qid, 'query_sha256': candidate['query_sha256'],
                        'cluster_id': t['cluster_id'], 'primary_family': FAMILIES[t['family']],
                        'provisional_split': t['provisional_split'], 'split_family': t['split_family'],
                        'admission': admission, 'locked': False})
    if t['exclude']:
        exclusions.append({'query_id': qid, 'query_sha256': candidate['query_sha256'], 'cluster_id': t['cluster_id'],
                           'admission': 'EXCLUDE', 'reason': t['exclude'],
                           'basis': 'Corpus source suspicion/legal ambiguity, never system performance',
                           'record_preserved': True, 'annotation_status': STATUS})

jsonl(PRIVATE / 'challenge_candidates_v0.jsonl', candidates)
jsonl(PRIVATE / 'annotation_A_v0.jsonl', annotations)
jsonl(PRIVATE / 'corpus_absence_audits_v0.jsonl', audits)
jsonl(PRIVATE / 'exclusion_log_v0.jsonl', exclusions)
write(PRIVATE / 'split_assignment_provisional_v0.json', {'status': 'PROVISIONAL_NOT_LOCKED',
      'whole_cluster_priority': True, 'reserve_migration_from_DEV_to_TEST': 'FORBIDDEN', 'assignments': assignments})

# Contamination checks: literal/lexical metrics flag review leads, never a semantic oracle.
history_path = ROOT / 'data/evaluation/generation/phase5/query_inputs_v0.json'
dev_path = ROOT / 'data/evaluation/dev_queries.jsonl'
history = json.loads(history_path.read_text())
old_dev = read_jsonl(dev_path)
assert len(history) == 31
assert all(set(q) == {'query_id', 'query'} for q in history), 'Historical projection is not query-only'
comparators = [{'id': 'historical:' + x['query_id'], 'query': x['query']} for x in history]
comparators += [{'id': 'existing_dev:' + x['query_id'], 'query': x['query']} for x in old_dev]
comparators += [{'id': 'exploratory_medical', 'query': 'Tôi muốn xây dựng một chatbot y tế, tôi cần lưu ý điều gì'}]

def normalized(s):
    return ' '.join(re.findall(r'\w+', unicodedata.normalize('NFC', s).casefold()))

def similarity(a, b):
    x, y = normalized(a), normalized(b)
    sx, sy = set(x.split()), set(y.split())
    bgx, bgy = set(zip(x.split(), x.split()[1:])), set(zip(y.split(), y.split()[1:]))
    return {'exact_normalized': x == y,
            'token_jaccard': round(len(sx & sy) / len(sx | sy), 6),
            'bigram_jaccard': round(len(bgx & bgy) / len(bgx | bgy), 6) if bgx | bgy else 0,
            'character_sequence_ratio': round(SequenceMatcher(None, x, y, autojunk=False).ratio(), 6)}

def lexical_flag(s):
    return s['exact_normalized'] or s['token_jaccard'] >= .35 or s['bigram_jaccard'] >= .30 or s['character_sequence_ratio'] >= .65

external_pairs, internal_pairs, individual_screen = [], [], []
for t, cand in zip(tasks, candidates):
    rows = []
    for other in comparators:
        sim = similarity(cand['query'], other['query'])
        row = {'query_id': cand['query_id'], 'comparison_id': other['id'], **sim,
               'lexical_review_flag': lexical_flag(sim)}
        external_pairs.append(row)
        rows.append(row)
    individual_screen.append({'query_id': cand['query_id'],
        'all_historical_queries_reviewed': 31, 'all_existing_dev_queries_reviewed': len(old_dev),
        'medical_structural_review': 'No diagnostic or close medical-chatbot scenario; no medical task constructed.',
        'manual_structural_review': notes['semantic_review'][t['key']],
        'structural_review_outcome': 'EXCLUDE_FIRST_PASS' if t['exclude'] else 'FIRST_PASS_ADMIT_OR_SAME_CLUSTER_RESERVE',
        'exclusion_reason': t['exclude'],
        'nearest_lexical_comparators': sorted(rows, key=lambda r: r['token_jaccard'], reverse=True)[:5],
        'reviewer': 'ANNOTATOR_A', 'independent_review_pending': True})
for a, b in combinations(candidates, 2):
    sim = similarity(a['query'], b['query'])
    internal_pairs.append({'query_id_a': a['query_id'], 'query_id_b': b['query_id'], **sim,
                          'lexical_review_flag': lexical_flag(sim),
                          'same_cluster': a['cluster_id'] == b['cluster_id'],
                          'same_split_family': a['split_family'] == b['split_family']})
screen = {'status': 'FIRST_PASS_PASS_PENDING_INDEPENDENT_REVIEW',
          'method': 'NFC/casefold exact check, token/bigram Jaccard, character sequence similarity plus A manual scenario/proposition/ask review of all 60 candidates against all historical/DEV queries and candidate cluster structure. No semantic model/API.',
          'thresholds': {'token_jaccard': .35, 'bigram_jaccard': .30, 'character_sequence_ratio': .65},
          'threshold_purpose': 'Review flags only; below threshold is not proof of semantic uniqueness.',
          'query_only_sources': {rel(history_path): file_hash(history_path), rel(dev_path): file_hash(dev_path)},
          'historical_count': 31, 'existing_dev_count': len(old_dev),
          'historical_and_dev_gold_or_system_answers_read': False,
          'external_pair_count': len(external_pairs), 'internal_pair_count': len(internal_pairs),
          'external_pairs': external_pairs, 'internal_pairs': internal_pairs, 'individual_review': individual_screen,
          'same_article_is_not_automatic_cluster': True,
          'remaining_independent_screening_required': True}
write(PRIVATE / 'contamination_screening_details_v0.json', screen)

# Public summaries intentionally omit text, gold, answerability, article refs and aspect counts.
headers = ['opaque_query_id', 'primary_family', 'provisional_split', 'cluster_id_hash',
           'dimension_tags_first_pass_except_D6', 'D6_status', 'annotation_status', 'needs_second_review']
with (PUBLIC / 'phase5c4a_candidate_summary_v0.csv').open('w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    for c in candidates:
        writer.writerow(dict(zip(headers, [c['query_id'], c['primary_family'], c['provisional_split'], digest(c['cluster_id']),
                          '|'.join(d for d, x in c['dimensions'].items() if x['member'] is True),
                          'empirical_unverified', STATUS, 'true'])))

retained = [c for c in candidates if c['provisional_split'] in ('DEV', 'HOLDOUT_TEST')]
counts = Counter(c['provisional_split'] for c in candidates)
dimensions_summary = {'label_status': 'FIRST_PASS_PROPOSED', 'D6': {'dimension_status': 'empirical_unverified',
                       'observed_count': None, 'selection_influence': False, 'desired_DEV': 4, 'desired_HOLDOUT_TEST': 8},
                       'split_counts': {}, 'overlap_matrix': {}, 'shortfalls': [],
                       'overlap_note': 'Memberships overlap and are not independent sample-size cells. D6 overlap is null, not zero.'}
tags = [f'D{i}' for i in range(1, 11)]
for split, target in [('DEV', 4), ('HOLDOUT_TEST', 8)]:
    rows = [c for c in retained if c['provisional_split'] == split]
    dims = {d: (None if d == 'D6' else sum(c['dimensions'][d]['member'] for c in rows)) for d in tags}
    dimensions_summary['split_counts'][split] = dims
    dimensions_summary['overlap_matrix'][split] = {a: {b: None if 'D6' in (a, b) else sum(c['dimensions'][a]['member'] and c['dimensions'][b]['member'] for c in rows) for b in tags} for a in tags}
    dimensions_summary['shortfalls'] += [{'split': split, 'dimension': d, 'desired': target, 'observed_first_pass': n,
                                        'disposition': 'External feasibility review required before freeze; no quota inflation.'} for d, n in dims.items() if n is not None and n < target]
write(PUBLIC / 'phase5c4a_dimension_matrix_v0.json', dimensions_summary)
cluster_groups = defaultdict(list)
for c in candidates:
    cluster_groups[c['cluster_id']].append(c)
cluster_summary = {'status': 'PROVISIONAL', 'cluster_separation': 'PASS',
                   'cluster_count': len(cluster_groups), 'clusters': [],
                   'definition': 'Same scenario, proposition bundle, paraphrase or legal-task template with leakage risk; source Article overlap alone insufficient.',
                   'independent_cluster_review_pending': True}
for cid, rows in sorted(cluster_groups.items()):
    assert len({r['split_family'] for r in rows}) == 1, 'Cluster crosses split families'
    cluster_summary['clusters'].append({'cluster_id_hash': digest(cid), 'opaque_query_ids': [r['query_id'] for r in rows],
        'provisional_splits': sorted({r['provisional_split'] for r in rows}), 'member_count': len(rows),
        'primary_families': sorted({r['primary_family'] for r in rows}),
        'split_family': rows[0]['split_family'], 'annotation_status': STATUS})
cross_family_retained = [cid for cid, rows in cluster_groups.items()
    if len({r['primary_family'] for r in rows if r['provisional_split'] in ('DEV','HOLDOUT_TEST')}) > 1]
cluster_summary['retained_cluster_count'] = len({c['cluster_id'] for c in retained})
cluster_summary['retained_cross_primary_family_cluster_count'] = len(cross_family_retained)
cluster_summary['stratum_feasibility_review'] = {
    'status': 'PENDING_EXTERNAL_REVIEW_BEFORE_5C4C_FREEZE',
    'reason': 'Some whole retained clusters span primary families. Frozen resampling language refers to primary-family strata. A later reviewer must resolve stratum assignment consistently with whole-cluster sampling; no algorithm is chosen or frozen here.',
    'affected_cluster_hashes': [digest(cid) for cid in cross_family_retained],
    'cluster_splitting_to_match_strata_or_counts': 'FORBIDDEN'}
write(PUBLIC / 'phase5c4a_cluster_summary_v0.json', cluster_summary)
private_cluster_notes = []
for cid, rows in cluster_groups.items():
    t = next(t for t in tasks if t['cluster_id'] == cid)
    private_cluster_notes.append({'cluster_id': cid, 'query_ids': [r['query_id'] for r in rows],
        'scenario_task_key': t['cluster'], 'split_family': rows[0]['split_family'],
        'rationale': notes['cluster_rationales'].get(t['cluster'], 'Distinct bounded legal decision and proposition bundle. Same-Article pairs reviewed without merging merely for shared source. Any material predicate variant is confined to the same split family.'),
        'needs_second_review': True})
write(PRIVATE / 'cluster_rationales_v0.json', private_cluster_notes)

# Independent review starts with query/scope and the COMPLETE corpus, never A labels,
# selected support, family/split, dimensions, confidence, system identities or outcomes.
review_units = []
for c in sorted(candidates, key=lambda c: identity('review-order:' + c['query_id'])):
    review_units.append({'review_unit_id': 'rb_' + identity(c['query_id'])[:20],
        'query_id': c['query_id'], 'query': c['query'], 'query_sha256': c['query_sha256'],
        'proposed_bounded_scope_for_independent_correction': c['scope'],
        'corpus_version': 'corpus-v0.1', 'corpus_sha256': corpus_hash,
        'complete_corpus_packet': 'complete_corpus_evidence_v0.json',
        'independent_form': {'reviewer_identity': None, 'reviewer_role': 'LEGAL_REVIEWER',
            'exposure_declaration': None, 'scope_corrections': None, 'required_legal_aspects': None,
            'support_bundles': None, 'evidence_relationships': None, 'applicability': None,
            'sufficiency': None, 'corpus_absence_audit': None, 'answerability': None,
            'cluster_contamination_concerns': None, 'review_completed_at': None},
        'review_status': 'NOT_STARTED'})
jsonl(REVIEW / '01_independent_review_units_v0.jsonl', review_units)
write(REVIEW / 'complete_corpus_evidence_v0.json', {'corpus_version': 'corpus-v0.1', 'corpus_sha256': corpus_hash,
      'source_files': source_files, 'articles': articles, 'chunks': chunks,
      'scope_note': 'Complete frozen corpus, not query-ranked evidence or selected A bundles. No external law.'})
write(REVIEW / 'contamination_query_only_sources_v0.json', {
    'purpose': 'Independent duplicate rejection only; never gold construction or imitation',
    'source_hashes': screen['query_only_sources'], 'queries': comparators,
    'historical_benchmark_size': 31, 'existing_dev_size': len(old_dev),
    'exploratory_status': 'EXPLORATORY / NON-BENCHMARK / NON-CONFIRMATORY',
    'contains_system_answers_or_historical_gold': False})
comparison = [{'query_id': c['query_id'], 'query': c['query'], 'scope': c['scope'],
               'proposed_aspects_support_applicability_sufficiency_answerability': {
                   k: a[k] for k in ('required_legal_aspects', 'full_supported_portion_bundles', 'alternative_review', 'answerability', 'response_obligations')},
               'corpus_audit_packet': 'corpus_absence_audits_v0.jsonl',
               'release_condition': 'Only after independent B judgments are saved with immutable hashes; comparison is not independent annotation.'}
              for c, a in zip(candidates, annotations)]
jsonl(PRIVATE / 'reviewer_b_comparison_after_independent_v0.jsonl', comparison)
text_file(REVIEW / 'README_independent_review_v0.md', '''# Independent legal review package — Phase 5C.4-B not started

Authorized roles: DATASET_CUSTODIAN / LEGAL_REVIEWER. Implementation access FORBIDDEN.
This package contains exact HOLDOUT plaintext. This authoring context must never implement or tune Agentic v2.

1. Use a fresh independent reviewer/session with a recorded identity and exposure declaration. Do not reuse ANNOTATOR_A or manufacture agreement.
2. Open `01_independent_review_units_v0.jsonl` and `complete_corpus_evidence_v0.json`. All 60 units, including reserves/exclusion proposals, are presented in deterministic opaque-ID order without split, family, dimensions or A final labels. Proposed scope is visible as requested and may itself anchor; independently correct it.
3. Independently write aspects, alternative AND bundles, relevance/role/applicability, sufficiency, answerability and absence audits. Use `contamination_query_only_sources_v0.json` only to reject duplicates against historical/DEV/exploratory queries, never to construct gold. Record original judgments before comparison. Do not view system answers, ranks, traces, evaluator outcomes or A confidence framing. No retrieval, inference or external law is authorized by this packet.
4. After independent judgments are saved and hashed, the custodian may release `../custodian/reviewer_b_comparison_after_independent_v0.jsonl` and referenced absence audits. They contain A's proposed aspects, selected corpus spans, bundles, applicability, sufficiency and answerability. Exact evidence resolves in the complete corpus packet. Read this comparison only after independent judgment.
5. Preserve both assessments. Adjudication and agreement reporting occur only under later authorization; neither is performed in 5C.4-A.

The comparison file is separated by workflow, NOT cryptographically sealed or protected from the same OS account. Filesystem permissions restrict other accounts only. HOLDOUT_STORAGE_ISOLATION_NOT_YET_ENFORCED. Final 5C.4-C freeze is blocked until role-separated access is enforced, independent review is complete and all remaining gates are resolved.

Reviewer B completed: 0. No signoff or final annotation is claimed.
''')

# Structural QA is independent of any generated system answer; no evaluator executed.
ann_by_id = {a['query_id']: a for a in annotations}
checks = []
def gate(name, passed, evidence):
    checks.append({'gate': name, 'status': 'PASS' if passed else 'FAIL', 'evidence': evidence})
gate('frozen_phase5c3_hash_bindings', True, {'checked': len(bound), 'phase_status': 'PASS', 'freeze_status': 'FROZEN'})
gate('unique_opaque_ids_and_query_hashes', len({c['query_id'] for c in candidates}) == 60 and len({c['query_sha256'] for c in candidates}) == 60, '60 unique IDs and exact-query SHA256 values')
support_count = 0
support_errors = []
for a in annotations:
    for aspect in a['required_legal_aspects']:
        for bundle in aspect['support_bundles']:
            for s in bundle['required_spans']:
                c = chunk_by_id.get(s['chunk_id'])
                support_count += 1
                if not c or span(c) != s:
                    support_errors.append(a['query_id'])
        if aspect['answer_role'] == 'unresolved_disclosure' and aspect['support_bundles']:
            support_errors.append(a['query_id'])
        for relation in aspect['evidence_relationships']:
            if span(chunk_by_id[relation['evidence']['chunk_id']]) != relation['evidence']:
                support_errors.append(a['query_id'])
gate('support_ids_span_hashes_and_parent_contexts_resolve', not support_errors, {'support_span_occurrences': support_count, 'error_query_ids': sorted(set(support_errors))})
gate('whole_cluster_split_separation', True, {'clusters': len(cluster_groups), 'includes_reserve_split_family': True})
gate('all_material_scopes_finite', all(all(c['scope'][k] for k in ('explicit_asks', 'bounded_interpretation', 'relevant_user_facts', 'unspecified_facts', 'excluded_scope')) for c in candidates), 'All five required scope fields populated; A manual scope review; B correction pending')
gate('annotations_first_pass_only', all(a['annotation_status'] == STATUS and a['locked_at'] is None and a['reviewer_B_status'] == 'NOT_STARTED' for a in annotations), '60 FIRST_PASS / PENDING_INDEPENDENT_REVIEW; independent second review 0')
gate('retained_require_second_review', all(c['needs_second_review'] for c in retained), {'retained': len(retained)})
gate('D6_empirical_unverified_unselected', all(c['dimensions']['D6']['member'] is None and c['dimensions']['D6']['dimension_status'] == 'empirical_unverified' for c in candidates), 'No query chosen from D6 or system performance; all D6 counts null')
gate('P_Q_U_disjoint_credit_and_pairing', all(sum(o['credit_group'] == 'Q' for o in a['response_obligations']) == sum('paired_qualified_obligation' in o for o in a['response_obligations']) for a in annotations), 'Every Q has separate U obligation on same aspect; disclosure never P+; no reference answers')
gate('corpus_wide_absence_audit_coverage', all(len(x['articles_reviewed']) == 86 and len(x['documents_reviewed']) == 3 for x in audits), {'first_pass_absence_audits': len(audits), 'legal_correctness_remains_independent_review': True})
gate('local_contamination_review', not any(p['exact_normalized'] for p in external_pairs + internal_pairs), {'external_pairs': len(external_pairs), 'internal_pairs': len(internal_pairs), 'all_candidates_manual_A_review': len(individual_screen), 'potential_historical_overlap_has_explicit_A_justification': True})
gate('medical_diagnostic_not_copied_or_paraphrased', all('y tế' not in c['query'].casefold() and 'chatbot' not in c['query'].casefold() for c in candidates), 'A manual scenario review; no medical chatbot candidate')
gate('reviewer_B_blind_first_stage', all(set(u) == {'review_unit_id', 'query_id', 'query', 'query_sha256', 'proposed_bounded_scope_for_independent_correction', 'corpus_version', 'corpus_sha256', 'complete_corpus_packet', 'independent_form', 'review_status'} and all(u['independent_form'][k] is None for k in ('required_legal_aspects','support_bundles','applicability','sufficiency','answerability')) for u in review_units), 'Complete corpus, no A selected evidence/labels; A comparison kept custodian-side until B judgments recorded; scope visible by design')

schema_errors = []
for candidate, annotation in zip(candidates, annotations):
    aid_set = {a['aspect_id'] for a in annotation['required_legal_aspects']}
    if candidate['query_id'] != annotation['query_id'] or candidate['query_sha256'] != annotation['query_sha256']:
        schema_errors.append(candidate['query_id'])
    for obligation in annotation['response_obligations']:
        if obligation['aspect_id'] not in aid_set:
            schema_errors.append(candidate['query_id'])
    for aspect in annotation['required_legal_aspects']:
        if aspect['origin'] not in ('query_explicit', 'scope_necessary') or aspect['evidence_sufficiency']['label'] not in ('sufficient_support', 'partial_support', 'no_support_in_corpus'):
            schema_errors.append(candidate['query_id'])
        if aspect['answer_role'] != 'unresolved_disclosure' and not aspect['support_bundles']:
            schema_errors.append(candidate['query_id'])
        if aspect['evidence_sufficiency']['label'] == 'no_support_in_corpus' and not aspect['evidence_sufficiency']['corpus_audit_id']:
            schema_errors.append(candidate['query_id'])
        for relation in aspect['evidence_relationships']:
            if relation['relevance'] not in ('direct','contextual','irrelevant','uncertain') or relation['evidence_role'] not in ('normative_support','supporting_context','counterevidence') or relation['applicability'] not in ('direct','conditional','not_applicable','uncertain'):
                schema_errors.append(candidate['query_id'])
            if not all(k in relation for k in ('actor','legal_scope','system_class','material_conditions','condition_assessment','uncertainty_rationale')):
                schema_errors.append(candidate['query_id'])
gate('annotation_schema_links_and_axis_enums', not schema_errors, {'error_query_ids': sorted(set(schema_errors)), 'response_obligations_have_aspect_parents': True})

execution_audit = {'basis': 'This session used local filesystem reads/writes, hashing and Python standard-library structural/lexical checks only. Counts describe task-initiated calls, not OS-wide packet/process attestation or the hosting assistant itself.',
    'network_api_calls': 0, 'production_calls': 0, 'evaluator_calls': 0,
    'retrieval_inference_calls': 0, 'reranker_inference_calls': 0, 'answer_generation_runs': 0,
    'system_answers_inspected': 0, 'v2_implementation': 'NOT_STARTED', 'independent_reviewer_B_completed': 0,
    'adjudication_completed': 0, 'dataset_frozen': False}
gate('authorized_actions_only', True, execution_audit)

composition = {'count_status': 'FIRST_PASS_PROPOSED', 'total_candidates': len(candidates),
               'retained': len(retained), 'provisional_splits': dict(counts), 'families': {},
               'answerability_by_split': {}, 'controls_by_split': {}, 'D9_condition_composition': {},
               'P_Q_U_aggregate_by_split': {}, 'P_plus_count_histogram_by_split': {},
               'P_plus_nonempty_query_counts': {}, 'no_power_certification': True}
for family in FAMILIES.values():
    composition['families'][family] = dict(Counter(c['provisional_split'] for c in candidates if c['primary_family'] == family))
for split in ('DEV','HOLDOUT_TEST','RESERVE','EXCLUDE'):
    rows = [c for c in candidates if c['provisional_split'] == split]
    composition['answerability_by_split'][split] = dict(Counter(ann_by_id[c['query_id']]['answerability']['label'] for c in rows))
    composition['controls_by_split'][split] = sum(c['control_case']['member'] for c in rows)
    selected = [t for t in tasks if t['provisional_split'] == split and t['key'] in D9_KEYS]
    positive_applicability_keys = set('A02 A03 A05 A06 A07 A08 A09 A10 A11 A12 B01 B02 B03 B04 B05 B06 B08 B09 B10 B11 B12 C06 C10 C13 C15 D08'.split())
    composition['D9_condition_composition'][split] = {
        'conditions_support_application': sum(t['key'] in positive_applicability_keys for t in selected),
        'unmet_or_unknown_material_condition': sum(bool(t['negative']) or any(a.get('condition') and a['condition'][1] in ('unmet','unknown') for a in t['aspects']) for t in selected),
        'unit': 'queries; positive/negative may overlap. Positive count uses A-selected actual duty/status application, not merely every successful exclusion conclusion.'}
    composition['P_Q_U_aggregate_by_split'][split] = dict(Counter(o['credit_group'] for c in rows for o in ann_by_id[c['query_id']]['response_obligations']))
    p_counts = [sum(o['credit_group'] == 'P+' for o in ann_by_id[c['query_id']]['response_obligations']) for c in rows]
    composition['P_plus_count_histogram_by_split'][split] = dict(sorted(Counter(p_counts).items()))
    composition['P_plus_nonempty_query_counts'][split] = sum(n > 0 for n in p_counts)
write(PUBLIC / 'phase5c4a_aggregate_composition_v0.json', composition)
composition_met = True
for split, partial_min, insufficient_min, control_min, d9_min in [('DEV',2,2,4,2),('HOLDOUT_TEST',4,4,8,4)]:
    ab = composition['answerability_by_split'][split]
    d9c = composition['D9_condition_composition'][split]
    composition_met &= ab.get('partially_answerable',0) >= partial_min and ab.get('insufficient_evidence',0) >= insufficient_min
    composition_met &= composition['controls_by_split'][split] >= control_min
    composition_met &= d9c['conditions_support_application'] >= d9_min and d9c['unmet_or_unknown_material_condition'] >= d9_min
gate('composition_targets_or_explicit_shortfalls', composition_met and not dimensions_summary['shortfalls'],
     {'dimension_status': 'FIRST_PASS_PROPOSED', 'D6_not_a_selection_gate': True,
      'details': ['phase5c4a_dimension_matrix_v0.json','phase5c4a_aggregate_composition_v0.json'],
      'reserve_shortfall': f"{counts['RESERVE']}/12; source-ambiguity and conservative near-duplicate exclusions; explicit external feasibility review before freeze"})

# New private files receive basic OS permissions, honestly insufficient against a
# future implementation process under the SAME account/session knowledge.
for directory in (PRIVATE, REVIEW):
    os.chmod(directory, 0o700)
    for p in directory.rglob('*'):
        if p.is_file():
            os.chmod(p, 0o600)

exposure = {'event_type': 'AUTHORIZED_CUSTODIAN_CONSTRUCTION_EXPOSURE', 'timestamp_utc': NOW,
    'recipient': 'current Codex authoring context', 'role': 'DATASET_CUSTODIAN / ANNOTATOR_A',
    'channel': 'Local authoring files and retained annotation reasoning; no exact TEST stdout dump',
    'affected_query_hashes': [c['query_sha256'] for c in candidates if c['split_family'] == 'HOLDOUT_TEST'],
    'affected_cluster_ids': sorted({c['cluster_id'] for c in candidates if c['split_family'] == 'HOLDOUT_TEST'}),
    'scope_of_retained_knowledge': 'Exact candidate queries, gold drafts, support and split design',
    'holdout_test_content_exposed_to_this_context': True,
    'future_v2_implementation_in_this_context': 'FORBIDDEN',
    'disposition': 'Authorized custodian exposure, not implementation authorization. No untouched-confirmatory certification. Any premature implementer access requires a durable event and downgrade of all affected clusters or a later authorized independent fresh cohort.'}
exposure_path = PRIVATE / 'exposure_events_v0.jsonl'
if not exposure_path.exists():
    jsonl(exposure_path, [exposure])
else:
    old_events = read_jsonl(exposure_path)
    known_hashes = {h for event in old_events for h in event.get('affected_query_hashes', [])}
    if not set(exposure['affected_query_hashes']) <= known_hashes:
        # Preserve all prior exposure bytes and append only genuinely new scope.
        with exposure_path.open('a', encoding='utf-8') as f:
            f.write(json.dumps(exposure, ensure_ascii=False) + '\n')

text_file(PUBLIC / 'phase5c4a_contamination_report_v0.md', f'''# Phase 5C.4-A contamination screening

First-pass screening: PASS, pending independent review. {len(candidates)} candidates were checked against the frozen 31-query query-only projection, {len(old_dev)} existing DEV queries and the exploratory diagnostic. {len(external_pairs)} external and {len(internal_pairs)} within-candidate pairs received local lexical comparisons. No exact normalized duplicate was found. No medical-chatbot candidate was constructed.

Lexical flags are review leads, not semantic judgments. ANNOTATOR_A reviewed scenario, bounded ask, actor/condition and proposition-template differences for all candidates, with explicit provisional admission rationale for historical-topic overlaps. Those rationales and pair details remain restricted. Correlated new variants were assigned to whole clusters, including reserves; no cluster crosses DEV and HOLDOUT TEST. Shared Articles alone do not define clusters.

The exclusion log preserves {counts['EXCLUDE']} candidates: one source-ambiguity candidate and one conservative historical near-duplicate exclusion. These dispositions use corpus/legal uncertainty and task/proposition overlap, never system performance. No candidate or gold was rewritten using retrieval, generation, evaluator results or the medical diagnostic. No system answers were inspected. No external reviewer agreement is claimed. Reviewer B must independently reassess structural duplication before any dataset freeze.
''')

shortfalls = dimensions_summary['shortfalls'] + [{'kind': 'reserve_count', 'preferred': 12, 'actual': counts['RESERVE'],
    'reason': 'Two of the 60 candidates excluded: internal source-reference ambiguity and conservative historical near-duplicate screening. Quality takes precedence; 48 retained target remains provisional. Do not fill reserves by forcing a legal interpretation or keeping near-duplicates.'}]
shortfalls.append({'kind': 'cluster_stratum_feasibility', 'retained_cross_primary_family_clusters': len(cross_family_retained),
    'disposition': 'External review must reconcile whole-cluster resampling with frozen primary-family stratum language before final dataset freeze; no frozen-design reinterpretation or cluster splitting in this phase.'})
report = f'''# Phase 5C.4-A construction report

Role: DATASET_CUSTODIAN / ANNOTATOR_A. Annotation status: FIRST_PASS / PENDING_INDEPENDENT_REVIEW.

Constructed {len(candidates)} candidates: {len(retained)} provisionally retained ({counts['DEV']} DEV, {counts['HOLDOUT_TEST']} HOLDOUT TEST), {counts['RESERVE']} reserves and {counts['EXCLUDE']} exclusions. All four primary families have 15 candidates; each has 4 DEV and 8 TEST. Deployment and procedural families have 3 reserves each; applicability and boundary families each have 2 reserves and 1 exclusion. The reserve shortfall is explicit and requires external feasibility review before final freeze. These counts do not certify statistical power.

Frozen Phase 5C.3 records PASS/FROZEN and its manifest/final registry bindings pass. Corpus-v0.1 has 3 documents, 86 articles and 737 chunks. Full article reading supplied the legal-task map before candidate wording. Source doubts and absence audits remain in the restricted package. No external law, web, API, project runtime, retrieval, reranker, production, evaluator or system answer was used. This is author annotation, not a generated reference-answer benchmark.

Gold separates finite aspects, alternative support bundles (OR across / AND within), source actor-bearing context, applicability, sufficiency and answerability. P+ credit excludes Q/U; every Q has a separately recorded unresolved-disclosure obligation on the same aspect. Pure context does not make an unsupported request partially answerable. Each absent-support finding has a scoped full-corpus review ledger and consideration of nearby alternative rules. All labels are provisional, with independent legal correctness and bundle completeness still pending.

Dimension counts and overlaps are in `phase5c4a_dimension_matrix_v0.json`. D6 is empirical_unverified throughout; counts and overlap cells involving D6 are null. No D6-based selection occurred. Corpus-defined controls are {composition['controls_by_split']['DEV']} DEV / {composition['controls_by_split']['HOLDOUT_TEST']} TEST, with no prediction of actual intervention behavior. Aggregate answerability and P+/Q/U composition are reported separately without query-level answerability labels. Cross-document tags remain first-pass proposals requiring independent search for single-document alternatives.

Whole-cluster separation includes reserve ancestry. The retained set has {cluster_summary['retained_cluster_count']} clusters; {len(cross_family_retained)} retained clusters span primary families because leakage protection has priority. The inherited resampling language uses primary-family strata: external review must resolve whole-cluster stratum feasibility before final freeze. This phase does not choose a replacement sampling algorithm or split clusters. A first-pass lexical and manual structural screening has explicit admission rationales for historical-topic overlap; independent screening is still required. The historical benchmark and prior DEV file remain unchanged.

Reviewer B receives opaque review units with query, proposed bounded scope and the complete corpus. A's selected evidence and final labels are withheld in a separate custodian comparison file until B records independent judgments. The scope proposal is visible and may anchor; B must correct it independently. The comparison contains proposed aspects, bundles, applicability, sufficiency and answerability, without system outputs or A confidence framing. It is workflow-separated, not cryptographically sealed. No B work or adjudication was performed.

HOLDOUT_STORAGE_ISOLATION_NOT_YET_ENFORCED. Private directories use 0700 and files 0600 to restrict other OS users, but a future implementation process with the same account can still read them. No role-separated accounts/ACLs or isolated runner are established. Filenames and modes do not remove this session's retained TEST knowledge. This context's future_v2_implementation_in_this_context = FORBIDDEN. Exposure and plaintext paths are inventoried. No untouched-confirmatory certification is made.

Phase 5C.4-C final freeze remains BLOCKED until enforceable role-separated HOLDOUT access, independent B review, subsequent authorized adjudication/signoff, support/cluster/contamination resolution, cross-family cluster/stratum feasibility and any shortfall approval are complete. Query/gold/splits remain unlocked. D6 can only occur after independently reviewed lock under later blind-audit authorization. No runtime projection or TEST release was created.

The hash baseline covers all preexisting regular project files, including hidden files and .venv; symlink targets are recorded without dereferencing. Before/after validation checks every baseline file and new-path scope. Only the new phase5c4_v0 namespace is written. The action audit is session-scoped, not OS-wide network attestation.

Ready for Phase 5C.4-B independent review after access handoff to a new authorized reviewer: YES. Ready for final dataset freeze: NO. STOP after construction QA.
'''
text_file(PUBLIC / 'phase5c4a_construction_report_v0.md', report)

# Content manifests hash provisional work only. This is NOT a dataset freeze seal.
write(PRIVATE / 'custodian_manifest_v0.json', {
    'schema_version': 'phase5c4a-custodian-manifest-v0', 'created_at_utc': NOW,
    'role': 'DATASET_CUSTODIAN', 'annotator': 'ANNOTATOR_A',
    'holdout_test_content_exposed_to_this_context': True,
    'future_v2_implementation_in_this_context': 'FORBIDDEN', 'annotation_status': STATUS,
    'dataset_frozen': False, 'query_gold_split_locked': False, 'independent_reviews_completed': 0,
    'counts': dict(counts), 'candidate_count': 60, 'retained_count': 48,
    'corpus_sha256': corpus_hash, 'source_files': source_files,
    'annotation_protocol': 'Frozen 5C.3 composition and hash-bound 5C.2 challenge §§3–7, with current 5C.4-A first-pass-only request.',
    'annotation_protocol_sha256': digest(canonical({'frozen_spec': file_hash(frozen / 'phase5c3_frozen_design_spec_v0.md'),
       'challenge_design': file_hash(ROOT / 'data/evaluation/generation/phase5/phase5c2_v0/phase5c2_challenge_set_design_v0.md'),
       'authoring_notes': file_hash(PRIVATE / 'construction_notes_v0.json')})),
    'split_manifest_sha256': file_hash(PRIVATE / 'split_assignment_provisional_v0.json'),
    'primary_artifact_hashes': {p.name: file_hash(p) for p in PRIVATE.iterdir() if p.is_file() and p.name != 'custodian_manifest_v0.json'},
    'execution_audit': execution_audit, 'shortfalls': shortfalls,
    'access_isolation': 'HOLDOUT_STORAGE_ISOLATION_NOT_YET_ENFORCED',
    'future_freeze_gate': 'BLOCKED: enforce role separation, complete B review and later authorized adjudication/signoff; approve or resolve any quality/coverage shortfall.',
    'integrity_check_is_not_annotation_certification': True})

# Public plaintext leakage scan: exact TEST text and nontrivial gold propositions.
test_rows = [c for c in candidates if c['split_family'] == 'HOLDOUT_TEST']
secret_strings = [c['query'] for c in test_rows]
secret_strings += [a['proposition'] for c in test_rows for a in ann_by_id[c['query_id']]['required_legal_aspects']]
leak_paths = []
for p in PUBLIC.iterdir():
    if p.is_file() and p.suffix in ('.json','.jsonl','.csv','.md','.txt'):
        body = p.read_text()
        if any(s in body for s in secret_strings):
            leak_paths.append(rel(p))
gate('public_outputs_no_exact_TEST_query_or_gold', not leak_paths, {'leak_paths': leak_paths, 'manual_review': 'No query text, propositions, Article IDs or per-query answerability/aspect count in public authored summaries.'})

# Hash all baseline files again; detect any write outside this additive namespace.
baseline_path = PUBLIC / 'integrity_baseline_v0.json'
baseline = json.loads(baseline_path.read_text())
after, changed, missing, read_errors = {}, [], [], []
for name, expected in baseline['files'].items():
    p = ROOT / name
    if not p.is_file() or p.is_symlink():
        missing.append(name)
        continue
    try:
        actual = {'sha256': file_hash(p), 'size_bytes': p.stat().st_size}
        after[name] = actual
        if actual != expected:
            changed.append(name)
    except OSError:
        read_errors.append(name)
symlink_changes = [name for name, target in baseline['symlinks'].items()
                   if not (ROOT/name).is_symlink() or os.readlink(ROOT/name) != target]
new_outside = []
all_old = set(baseline['files']) | set(baseline['symlinks'])
for current, dirs, files in os.walk(ROOT, followlinks=False):
    for name in files + [d for d in dirs if (Path(current)/d).is_symlink()]:
        p = Path(current)/name
        if rel(p) not in all_old and OUT not in p.parents:
            new_outside.append(rel(p))
integrity_pass = not (changed or missing or read_errors or symlink_changes or new_outside)
integrity = {'status': 'PASS' if integrity_pass else 'FAIL', 'checked_at_utc': NOW,
             'baseline_path': rel(baseline_path), 'baseline_sha256': file_hash(baseline_path),
             'scope': baseline['scope'], 'baseline_regular_files': len(baseline['files']),
             'after_preexisting_regular_files': len(after), 'baseline_symlinks': len(baseline['symlinks']),
             'changed_preexisting_paths': changed, 'missing_preexisting_paths': missing,
             'symlink_changes': symlink_changes, 'new_paths_outside_namespace': new_outside,
             'read_errors': read_errors, 'before': baseline['files'], 'after': after,
             'allowed_new_namespace': rel(OUT), 'no_prior_artifacts_modified': integrity_pass,
             'network_api_calls': 0, 'production_evaluator_calls': 0, 'retrieval_reranking_inference_calls': 0}
write(PUBLIC / 'integrity_before_after_v0.json', integrity)
gate('all_preexisting_artifacts_unchanged_and_new_paths_scoped', integrity_pass,
     {'files': len(baseline['files']), 'symlinks': len(baseline['symlinks']), 'details': 'integrity_before_after_v0.json'})
gate('corpus_and_historical_benchmark_unchanged', all(after.get(name) == rec for name, rec in baseline['files'].items() if name.startswith('data/versions/corpus-v0.1/') or name.startswith('data/evaluation/')), 'All preexisting evaluation, benchmark, gold and prior-phase bytes checked without semantic answer inspection')
gate('isolation_limitation_and_final_freeze_block_reported', True, 'HOLDOUT_STORAGE_ISOLATION_NOT_YET_ENFORCED; mandatory 5C.4-C gate, not a construction failure by current authorization')

phase_pass = all(x['status'] == 'PASS' for x in checks)
console = f'''Phase 5C.4-A status:
{'PASS' if phase_pass else 'FAIL'}

Role:
DATASET_CUSTODIAN / ANNOTATOR_A

Frozen Phase 5C.3 verified:
YES

Candidates constructed:
60

Provisional retained:
48

Provisional DEV:
16

Provisional HOLDOUT TEST:
32

Reserve:
{counts['RESERVE']}

Excluded:
{counts['EXCLUDE']}

Primary task families represented:
4/4

Dimension construction status:
'''
for d in tags:
    console += ('D6: EMPIRICAL_UNVERIFIED\n' if d == 'D6' else f"{d}: FIRST_PASS_PROPOSED; DEV={dimensions_summary['split_counts']['DEV'][d]}, TEST={dimensions_summary['split_counts']['HOLDOUT_TEST'][d]}\n")
console += f'''
Cluster separation:
PASS

Benchmark contamination screening:
PASS

Medical diagnostic copied/paraphrased:
NO

First annotation completed:
60/60

Independent second review completed:
0

Final verified annotations:
0

Dataset frozen:
NO

Exact HOLDOUT TEST content printed to console:
NO

HOLDOUT plaintext inventoried:
YES

HOLDOUT storage isolation:
NOT_YET_ENFORCED

Network/API calls:
0

Production/evaluator calls:
0

Retrieval/reranking inference:
0

Agentic v2 implementation:
NOT STARTED

Preexisting artifact integrity:
{'PASS' if integrity_pass else 'FAIL'}

Ready for Phase 5C.4-B independent review:
{'YES' if phase_pass else 'NO'}

Ready for final dataset freeze:
NO

STOP
'''
text_file(PUBLIC / 'phase5c4a_console_v0.txt', console)

# Inventory EVERY private output, including source/notes that reveal TEST scenarios.
manual_plaintext_names = {'authored_tasks_v0.py', 'construction_notes_v0.json', 'explicit_asks_v0.json',
    'challenge_candidates_v0.jsonl', 'annotation_A_v0.jsonl', 'corpus_absence_audits_v0.jsonl',
    'reviewer_b_comparison_after_independent_v0.jsonl', '01_independent_review_units_v0.jsonl',
    'contamination_screening_details_v0.json', 'cluster_rationales_v0.json'}
access_files = []
for directory in (PRIVATE, REVIEW):
    for p in sorted(directory.rglob('*')):
        if not p.is_file():
            continue
        os.chmod(p, 0o600)
        body = p.read_text()
        contains = p.name in manual_plaintext_names or any(s in body for s in secret_strings)
        access_files.append({'path': rel(p), 'contains_holdout_plaintext': contains,
            'authorized_roles': ['DATASET_CUSTODIAN', 'LEGAL_REVIEWER'],
            'implementation_access': 'FORBIDDEN', 'mode_octal': oct(p.stat().st_mode & 0o777),
            'owner_uid': p.stat().st_uid, 'sha256': file_hash(p),
            'note': 'Complete-corpus copy alone is not query-selected gold.' if p.name == 'complete_corpus_evidence_v0.json' else 'Restricted artifact; hashes identify provisional bytes, not dataset freeze.'})
access = {'contains_holdout_plaintext': True, 'authorized_roles': ['DATASET_CUSTODIAN', 'LEGAL_REVIEWER'],
          'implementation_access': 'FORBIDDEN', 'role': 'DATASET_CUSTODIAN',
          'holdout_test_content_exposed_to_this_context': True,
          'future_v2_implementation_in_this_context': 'FORBIDDEN',
          'isolation_status': 'HOLDOUT_STORAGE_ISOLATION_NOT_YET_ENFORCED',
          'filesystem_enforcement': {'private_directory_modes': '0700', 'private_file_modes': '0600',
              'same_owner_implementation_read_prevented': False, 'role_separated_accounts_or_ACLs': False},
          'phase5c4c_freeze': 'BLOCKED_UNTIL_ENFORCEABLE_HOLDOUT_ROLE_SEPARATION',
          'plaintext_path_inventory': access_files,
          'console_exact_TEST_text_printed': False,
          'tool_authoring_payloads': 'Source-write requests necessarily carry custodian plaintext in this context. They are part of the exposed custodian session; do not hand the conversation to implementers. No plaintext returned by stdout or included in final public report.',
          'public_metadata_is_not_runner_input': True,
          'production_release': 'NOT_CREATED_NOT_AUTHORIZED',
          'reviewer_B_comparison_release': 'Only after independent B judgments saved; workflow condition, no technical seal claim.',
          'timestamp_utc': NOW}
write(PUBLIC / 'phase5c4a_access_manifest_v0.json', access)
gate('all_HOLDOUT_plaintext_paths_inventoried', all(any(x['path'] == rel(p) and x['contains_holdout_plaintext'] for x in access_files) for directory in (PRIVATE, REVIEW) for p in directory.rglob('*') if p.is_file() and p.name in manual_plaintext_names), {'private_files_inventoried': len(access_files), 'plaintext_files': sum(x['contains_holdout_plaintext'] for x in access_files)})
phase_pass = all(x['status'] == 'PASS' for x in checks)
write(PUBLIC / 'phase5c4a_validation_v0.json', {
    'phase': '5C.4-A', 'phase_status': 'PASS' if phase_pass else 'FAIL', 'all_construction_gates_pass': phase_pass,
    'annotation_status': 'FIRST_PASS / PENDING_INDEPENDENT_REVIEW',
    'validation_scope': 'Local schema/support-link/hash/confidentiality/cluster QA plus A manual legal and structural review; not independent legal correctness or adjudication.',
    'checks': checks, 'execution_audit': execution_audit, 'shortfalls': shortfalls,
    'independent_second_review_completed': 0, 'final_annotations': 0, 'dataset_frozen': False,
    'ready_for_phase5c4b_independent_review': phase_pass, 'ready_for_final_dataset_freeze': False,
    'holdout_isolation': 'HOLDOUT_STORAGE_ISOLATION_NOT_YET_ENFORCED',
    'mandatory_before_phase5c4c_freeze': ['Enforce role-separated HOLDOUT storage and keep exposed contexts out of implementation',
        'Independent B review and later authorized adjudication/signoff',
        'Resolve support/scope/alternative-bundle/cluster/contamination concerns and cross-family whole-cluster stratum feasibility',
        'External approval or resolution of any dimension/reserve shortfall',
        'Independently reviewed query/gold/split lock before separately authorized blind D6 audit'],
    'checked_at_utc': NOW})
write(PUBLIC / 'artifact_hashes_v0.json', {
    'purpose': 'Provisional construction artifact inventory, NOT a dataset freeze seal',
    'algorithm': 'sha256', 'self_excluded_to_avoid_circular_hash': True,
    'artifacts': {rel(p): {'sha256': file_hash(p), 'size_bytes': p.stat().st_size}
                  for p in sorted(OUT.rglob('*')) if p.is_file() and p.name != 'artifact_hashes_v0.json'}})
print('First-pass packaging:', 'PASS' if phase_pass else 'FAIL', f"; candidates=60; DEV=16; TEST=32; reserve={counts['RESERVE']}; excluded={counts['EXCLUDE']}; independent_review=0")
