#!/usr/bin/env python3
"""Custodian-only, additive B0 projection. Standard library; no project imports.

Run once to build, or --verify to check the completed artifact set read-only.
Never print source rows, identifiers, query literals, mapping, or annotation values.
"""
import copy
import datetime
import hashlib
import hmac
import json
import os
from pathlib import Path
import re
import secrets
import stat
import sys

HERE = Path(__file__).resolve().parent
BASE = HERE.parent.parent
ROOT = BASE.parents[4]
CUSTODIAN = BASE / 'custodian'
VISIBLE = BASE / 'reviewer_b_packet_v1'
CORPUS = ROOT / 'data/versions/corpus-v0.1'
SOURCE = CUSTODIAN / 'challenge_candidates_v0.jsonl'
VISIBLE_NAMES = {'reviewer_b_queries_v1.jsonl', 'reviewer_b_packet_manifest_v1.json',
                 'reviewer_b_annotation_instructions_v1.md'}
PRIVATE_NAMES = {'reviewer_b_id_mapping_v1.json', 'reviewer_b_shuffle_provenance_v1.json',
                 'contaminated_packet_quarantine_v0.json', 'reviewer_b_packet_projection_audit_v1.json'}
REMEDIATION_NAMES = {'integrity_baseline_v0.json', 'sanitize_reviewer_b_v1.py',
                     'execution_and_access_v0.json', 'integrity_before_after_v0.json',
                     'phase5c4b0_validation_v0.json', 'phase5c4b0_console_v0.txt',
                     'phase5c4b0_review_summary_v0.md', 'fresh_reviewer_b_handoff_v1.md',
                     'artifact_hashes_v0.json'}

# Reviewed, candidate-independent text. Do not interpolate any candidate content.
INSTRUCTIONS = '''# Independent Reviewer B — packet v1

Only a brand-new session that has never inspected earlier packets, custodian
materials, A judgments, comparison files, or prior B results may use this packet.
The previous B session and the session that prepared this packet cannot annotate.
This session must never implement or tune Agentic v2.

Authorized input consists of the three files in this directory and the entire
original corpus at data/versions/corpus-v0.1/. The only substantive input per
candidate is its exact query. Use review_id_b solely as an opaque bookkeeping
identifier. Neither identifiers nor presentation order specify any judgment.
Process the single combined file in its supplied order. Do not infer groupings.
Do not inspect sibling directories, earlier packets, A artifacts, mappings,
construction records, public candidate summaries, or system outputs.

Independently record the scope, explicit asks, bounded interpretation,
query-contained facts, unspecified facts, and justified exclusions. Reconstruct
required legal aspects and obligations. Locate support bundles independently,
record exact evidence locations and necessary hierarchical context, assess
applicability and sufficiency separately, and judge answerability. Document
uncertainty rather than silently supplying missing facts. Assign dimensions
except D6 and an admission recommendation independently. Do not copy or infer
prior interpretations, selected evidence, labels, or decisions.

The preceding paragraph describes tasks, not new label definitions. Apply the
separately authorized generic frozen annotation rubric. If that rubric is absent
or ambiguous, obtain a candidate-independent rubric before making judgments;
do not consult A examples or invent dimension definitions. D6 stays
EMPIRICAL_UNVERIFIED and must not be measured or used for admission here.

Read and search the entire frozen corpus directly with ordinary deterministic
local text lookup and hierarchy inspection. Record this separately as annotation
research, including files/search expressions consulted. No evidence has been
preselected. Do not execute production BM25, dense retrieval, reranking, Agentic
pipelines, generation models, or evaluators. No network or API calls are allowed.

No historical contamination reference is supplied. If later authorized, obtain
a separate blind resource containing historical/exploratory query text only,
without labels, scores, failures, system answers, or candidate similarity hints.
Do not claim historical duplication review is complete without that resource.

Keep all exact queries, notes, and judgments private. Store later annotations
only in a separately authorized new results namespace keyed by review_id_b;
do not change these inputs. Do not compare with A or adjudicate during the
independent pass. Complete and lock independent work before any separately
authorized comparison. Do not freeze or release the dataset here.

This directory contains HOLDOUT plaintext. Its authorized role is
INDEPENDENT_ANNOTATOR_B; implementation access is FORBIDDEN. Storage isolation
is NOT_YET_ENFORCED. Owner-only file modes and these instructions do not create
a validated role boundary. Stop if unexpected prefilled interpretations appear.
'''

# Case-insensitive raw byte substring scan; separators and camel-case variants
# are caught because stems are scanned independently (no word-boundary shortcut).
FORBIDDEN = re.compile(
    rb'split|dev|test|reserve|family|families|cluster|dimension|answerability|'
    rb'scope|explicit[ _-]*asks?|bounded|aspect|support|chunk|article|'
    rb'applicability|sufficiency|retain|exclude|annotator|confidence|risk|gold|'
    rb'required[ _-]*points?|proposition|materiality|difficulty|mechanism|'
    rb'evidence[ _-]*span|relevant[ _-]*user[ _-]*facts|unspecified[ _-]*facts|'
    rb'D(?:10|[1-9])(?![0-9a-f])', re.I)
ID_PATTERN = re.compile(r'rb_[0-9a-f]{32}\Z')

def require(condition, code):
    if not condition:
        raise RuntimeError(code)  # codes only; never stringify data

def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def sha(data):
    return hashlib.sha256(data).hexdigest()

def file_sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for b in iter(lambda: stream.read(1048576), b''):
            h.update(b)
    return h.hexdigest()

def rel(path):
    return path.relative_to(ROOT).as_posix()

def encoded(obj):
    return (json.dumps(obj, ensure_ascii=False, indent=2) + '\n').encode('utf-8')

def compact(obj):
    return json.dumps(obj, ensure_ascii=False, separators=(',', ':')).encode('utf-8')

def write_new(path, data):
    raw = data if isinstance(data, bytes) else data.encode('utf-8')
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, 'wb') as stream:
        stream.write(raw)

def write_json(path, obj):
    write_new(path, encoded(obj))

def read_json(path):
    return json.loads(path.read_bytes())

def snapshot():
    entries = {}
    for base, dirs, files in os.walk(ROOT, followlinks=False):
        for name in sorted(dirs + files):
            p = Path(base) / name
            s = p.lstat()
            if stat.S_ISLNK(s.st_mode):
                entries[rel(p)] = {'kind': 'symlink', 'target': os.readlink(p),
                                   'mode': stat.S_IMODE(s.st_mode)}
            elif stat.S_ISREG(s.st_mode):
                entries[rel(p)] = {'kind': 'file', 'sha256': file_sha(p),
                                   'size_bytes': s.st_size, 'mode': stat.S_IMODE(s.st_mode)}
            else:
                require(stat.S_ISDIR(s.st_mode), 'UNSUPPORTED_FILESYSTEM_ENTRY')
    return dict(sorted(entries.items()))

def is_allowed_addition(name):
    p = ROOT / name
    return ((p.parent == VISIBLE and p.name in VISIBLE_NAMES) or
            (p.parent == CUSTODIAN and p.name in PRIVATE_NAMES) or
            (p.parent == HERE and p.name in REMEDIATION_NAMES))

def no_duplicate_keys(pairs):
    result = {}
    for k, v in pairs:
        require(k not in result, 'DUPLICATE_JSON_KEY')
        result[k] = v
    return result

def validate_rows(raw, expected_count=60):
    try:
        lines = raw.decode('utf-8').splitlines()
        rows = [json.loads(line, object_pairs_hook=no_duplicate_keys) for line in lines]
    except (ValueError, UnicodeError):
        raise RuntimeError('INVALID_JSONL') from None
    require(len(rows) == expected_count, 'WRONG_RECORD_COUNT')
    ids, queries = set(), set()
    for row in rows:
        require(type(row) is dict and set(row) == {'review_id_b', 'query'}, 'EXACT_SCHEMA_REQUIRED')
        require(type(row['review_id_b']) is str and ID_PATTERN.fullmatch(row['review_id_b']), 'NON_OPAQUE_ID')
        require(type(row['query']) is str and bool(row['query'].strip()), 'NONEMPTY_STRING_QUERY_REQUIRED')
        require(row['review_id_b'] not in ids, 'DUPLICATE_REVIEW_ID')
        require(row['query'] not in queries, 'DUPLICATE_EXACT_QUERY')
        ids.add(row['review_id_b']); queries.add(row['query'])
    return rows

def query_literal(line):
    # Locate a top-level JSON query value without reserializing or normalizing it.
    text = line.decode('utf-8')
    decoder = json.JSONDecoder(object_pairs_hook=no_duplicate_keys)
    require(text.startswith('{'), 'SOURCE_OBJECT_REQUIRED')
    i = 1
    while True:
        while text[i].isspace(): i += 1
        if text[i] == '}': break
        key, i = decoder.raw_decode(text, i)
        while text[i].isspace(): i += 1
        require(text[i] == ':', 'SOURCE_COLON_REQUIRED'); i += 1
        while text[i].isspace(): i += 1
        start = i
        value, i = decoder.raw_decode(text, i)
        if key == 'query':
            require(type(value) is str, 'SOURCE_QUERY_STRING_REQUIRED')
            return text[start:i].encode('utf-8')
        while text[i].isspace(): i += 1
        if text[i] == '}': break
        require(text[i] == ',', 'SOURCE_COMMA_REQUIRED'); i += 1
    raise RuntimeError('SOURCE_QUERY_MISSING')

def validator_checks():
    good = [{'review_id_b': 'rb_' + '1' * 32, 'query': 'Synthetic input one'},
            {'review_id_b': 'rb_' + '2' * 32, 'query': 'Synthetic input two'}]
    raw = b'\n'.join(compact(r) for r in good) + b'\n'
    validate_rows(raw, 2)
    cases = []
    for key in ['scope', 'provisionalSplit', 'gold', 'metadata']:
        r = copy.deepcopy(good); r[0][key] = {'nested': 'value'}
        cases.append((f'extra_{key}', b'\n'.join(compact(x) for x in r)))
    for value in [None, '', ' \t', {}, [], 42]:
        r = copy.deepcopy(good); r[0]['query'] = value
        cases.append(('invalid_query_type_or_blank', b'\n'.join(compact(x) for x in r)))
    for ident in ['DEV_001', 'rb_family_one', 'rb_' + 'x' * 32, None, {'id': 'nested'}]:
        r = copy.deepcopy(good); r[0]['review_id_b'] = ident
        cases.append(('non_opaque_or_nonstring_id', b'\n'.join(compact(x) for x in r)))
    for key in ['review_id_b', 'query']:
        r = copy.deepcopy(good); r[1][key] = r[0][key]
        cases.append(('duplicate_' + key, b'\n'.join(compact(x) for x in r)))
    cases += [('duplicate_JSON_key', raw.replace(b'"query":', b'"query":"hidden","query":', 1)),
              ('comment', raw + b'# scope\n'), ('blank_record', raw + b'\n'),
              ('extra_record', raw + compact(good[0])), ('array_row', b'[]\n' + compact(good[1])),
              ('invalid_utf8', b'\xff\n' + compact(good[1]))]
    results = []
    for name, bad in cases:
        try:
            validate_rows(bad, 2)
        except RuntimeError:
            results.append({'case': name, 'rejected': True})
        else:
            raise RuntimeError('VALIDATOR_NEGATIVE_CONTROL_FAILED')
    probes = [b'provisionalSplit', b'DEV', b'family', b'explicitAsk', b'required-point',
              b'bounded_interpretation', b'answerability', b'gold', b'D10']
    require(all(FORBIDDEN.search(p) for p in probes), 'RAW_SCANNER_VARIANT_CONTROL_FAILED')
    return {'positive_control': 'PASS', 'negative_controls': results,
            'raw_scanner_variant_controls': len(probes), 'candidate_examples_used': False}

def corpus_inventory():
    return {p.relative_to(CORPUS).as_posix(): {'sha256': file_sha(p), 'size_bytes': p.stat().st_size}
            for p in sorted(CORPUS.rglob('*')) if p.is_file()}

def expected_manifest(packet_hash, corpus):
    return {'schema': 'reviewer-b-packet-v1', 'candidate_count': 60,
            'record_fields': ['review_id_b', 'query'],
            'files': {'reviewer_b_queries_v1.jsonl': packet_hash,
                      'reviewer_b_annotation_instructions_v1.md': sha(INSTRUCTIONS.encode('utf-8'))},
            'corpus_location': 'data/versions/corpus-v0.1/',
            'corpus_inventory_sha256': sha(compact(corpus)),
            'corpus_access': 'ENTIRE_ORIGINAL_CORPUS',
            'contains_holdout_plaintext': True,
            'authorized_roles': ['INDEPENDENT_ANNOTATOR_B'],
            'implementation_access': 'FORBIDDEN',
            'storage_isolation': 'NOT_YET_ENFORCED',
            'new_session_required': True}

def source_records():
    lines = SOURCE.read_bytes().splitlines()
    source = [json.loads(line, object_pairs_hook=no_duplicate_keys) for line in lines]
    require(len(source) == 60, 'SOURCE_COUNT')
    require(len({s['query_id'] for s in source}) == 60, 'SOURCE_IDS_NOT_UNIQUE')
    for s in source:
        require(type(s['query']) is str and sha(s['query'].encode('utf-8')) == s['query_sha256'], 'SOURCE_QUERY_HASH')
    return source, {s['query_id']: query_literal(line) for s, line in zip(source, lines)}

def verify_projection(source, literals, corpus):
    require({p.name for p in VISIBLE.iterdir()} == VISIBLE_NAMES, 'UNEXPECTED_VISIBLE_FILE')
    require(all(p.is_file() and not p.is_symlink() for p in VISIBLE.iterdir()), 'VISIBLE_SYMLINK_OR_NONFILE')
    raw = (VISIBLE / 'reviewer_b_queries_v1.jsonl').read_bytes()
    rows = validate_rows(raw)
    mapping = read_json(CUSTODIAN / 'reviewer_b_id_mapping_v1.json')['mapping']
    provenance = read_json(CUSTODIAN / 'reviewer_b_shuffle_provenance_v1.json')
    by_source = {s['query_id']: s for s in source}
    by_b = {m['review_id_b']: m for m in mapping}
    require(len(mapping) == len(by_b) == 60 and {m['canonical_candidate_id'] for m in mapping} == set(by_source), 'MAPPING_BIJECTION')
    seed = bytes.fromhex(provenance['seed_hex'])
    key = bytes.fromhex(provenance['id_key_hex'])
    expected_ids = {s['query_id']: 'rb_' + hmac.new(key, s['query_id'].encode('utf-8'), hashlib.sha256).hexdigest()[:32] for s in source}
    expected_order = sorted(expected_ids.values(), key=lambda i: (hmac.new(seed, i.encode('ascii'), hashlib.sha256).digest(), i))
    require([r['review_id_b'] for r in rows] == expected_order, 'SHUFFLE_REPLAY_MISMATCH')
    require(provenance['input_list_sha256'] == sha(compact([s['query_id'] for s in source])), 'INPUT_LIST_HASH')
    require(provenance['output_order_sha256'] == sha(compact(expected_order)), 'OUTPUT_ORDER_HASH')
    byte_checks = []
    for row, line in zip(rows, raw.splitlines()):
        m = by_b[row['review_id_b']]; s = by_source[m['canonical_candidate_id']]
        require(row['review_id_b'] == expected_ids[s['query_id']], 'ID_REPLAY_MISMATCH')
        require(row['query'].encode('utf-8') == s['query'].encode('utf-8'), 'QUERY_UTF8_CHANGED')
        require(query_literal(line) == literals[s['query_id']], 'QUERY_JSON_LITERAL_CHANGED')
        require(m['source_query_sha256'] == m['projected_query_sha256'] == sha(row['query'].encode('utf-8')), 'MAPPING_QUERY_HASH')
        require(m['source_literal_sha256'] == m['projected_literal_sha256'] == sha(query_literal(line)), 'MAPPING_LITERAL_HASH')
        byte_checks.append({'review_id_b': row['review_id_b'], 'utf8_match': True, 'json_literal_match': True})
    manifest_raw = (VISIBLE / 'reviewer_b_packet_manifest_v1.json').read_bytes()
    expected_raw = encoded(expected_manifest(sha(raw), corpus))
    instructions_raw = (VISIBLE / 'reviewer_b_annotation_instructions_v1.md').read_bytes()
    require(manifest_raw == expected_raw, 'MANIFEST_GENERIC_TEMPLATE_MISMATCH')
    require(instructions_raw == INSTRUCTIONS.encode('utf-8'), 'INSTRUCTIONS_GENERIC_TEMPLATE_MISMATCH')
    # Query-adjacent bytes are reconstructed from approved syntax and opaque ID.
    # The query token itself must match the canonical source token byte for byte.
    spans = []
    offset = 0
    for row, line in zip(rows, raw.splitlines(keepends=True)):
        literal = literals[by_b[row['review_id_b']]['canonical_candidate_id']]
        prefix = b'{"review_id_b":' + compact(row['review_id_b']) + b',"query":'
        require(line == prefix + literal + b'}\n', 'UNEXPECTED_QUERY_ADJACENT_BYTES')
        spans.append((offset + len(prefix), offset + len(prefix) + len(literal)))
        offset += len(line)
    hits = []
    for name in sorted(VISIBLE_NAMES):
        data = (VISIBLE / name).read_bytes()
        for match in FORBIDDEN.finditer(data):
            if name == 'reviewer_b_queries_v1.jsonl':
                classification = ('IMMUTABLE_CANONICAL_QUERY_LITERAL' if any(a <= match.start() and match.end() <= b for a, b in spans)
                                  else 'OPAQUE_HEX_ID_OR_SCHEMA_SYNTAX_VERIFIED_BY_EXACT_RECONSTRUCTION')
            elif name.endswith('.md'):
                classification = 'REVIEWED_FIXED_GENERIC_RUBRIC_OR_ACCESS_INSTRUCTION'
            else:
                classification = 'EXACT_GENERIC_MANIFEST_ACCESS_ROLE_OR_OPAQUE_SHA256'
            hits.append({'file': name, 'start_byte': match.start(), 'end_byte': match.end(),
                         'matched_term_sha256': sha(match.group()), 'classification': classification})
        for match in FORBIDDEN.finditer(name.encode('ascii')):
            hits.append({'file': name, 'location': 'filename', 'start_byte': match.start(),
                         'classification': 'FIXED_GENERIC_PACKET_FILENAME'})
    # Other visible files must not contain a canonical ID, any exact query, or
    # any B-local ID. Their only variable inputs are whole-file/corpus hashes.
    adjacent = manifest_raw + instructions_raw
    require(not any(s['query'].encode('utf-8') in adjacent or s['query_id'].encode('utf-8') in adjacent for s in source), 'ADJACENT_CANONICAL_CONTENT')
    require(not any(r['review_id_b'].encode('ascii') in adjacent for r in rows), 'ADJACENT_CANDIDATE_ID')
    require(not any(s['query_id'].encode('utf-8') in raw for s in source), 'CANONICAL_ID_EXPOSED')
    return {'status': 'PASS', 'structural_audit': 'PASS', 'semantic_leakage_audit': 'PASS',
            'candidate_count': len(rows), 'exact_candidate_keys': ['review_id_b', 'query'],
            'query_identity_checks': byte_checks, 'raw_scan_hits': hits,
            'raw_scan_rule': FORBIDDEN.pattern.decode('ascii'),
            'raw_scan_policy': 'Scan all raw bytes and filenames, including immutable query literals. Each hit is classified only after exact query-token, ID generation, syntax and reviewed generic template verification. Generic rubric/access words are required and are not candidate labels. No unchecked free-text value or blanket keyword exception is permitted.',
            'unclassified_hits': 0, 'query_adjacent_unapproved_bytes': 0,
            'semantic_review': {'generic_instructions_authored_without_candidate_examples': True,
                                'no_candidate_specific_legal_hints': True,
                                'no_A_values_interpolated': True,
                                'no_selected_corpus_evidence': True,
                                'canonical_ids_absent': True,
                                'single_mixed_file': True,
                                'independent_id_and_order_replayed': True},
            'visible_file_hashes': {name: file_sha(VISIBLE / name) for name in sorted(VISIBLE_NAMES)}}

def frozen_checks(before):
    registry = read_json(BASE / 'public_review/artifact_hashes_v0.json')['artifacts']
    checks = []
    for name, expected in registry.items():
        require(before[name]['sha256'] == expected['sha256'], 'A_REGISTRY_HASH_MISMATCH')
        checks.append({'path': name, 'sha256': expected['sha256'], 'match': True})
    freeze_dir = BASE.parent / 'phase5c3_v0'
    freeze = read_json(freeze_dir / 'phase5c3_freeze_manifest_v0.json')
    require(freeze['phase_status'] == 'PASS' and freeze['phase5c3_freeze_status'] == 'FROZEN', 'PHASE3_NOT_FROZEN')
    for field in ['artifact_hashes', 'phase5c1_authoritative_artifacts', 'phase5c2_all_artifacts']:
        for name, expected in freeze[field].items():
            path = rel(freeze_dir / name) if field == 'artifact_hashes' else name
            require(before[path]['sha256'] == expected['sha256'], 'FROZEN_BINDING_MISMATCH')
            checks.append({'path': path, 'sha256': expected['sha256'], 'match': True})
    require(read_json(BASE / 'public_review/phase5c4a_validation_v0.json')['phase_status'] == 'PASS', 'A_STATUS_NOT_PASS')
    frozen_inventory = read_json(freeze_dir / 'integrity_before_after_v0.json')['after_entries']
    for path in sorted(CORPUS.rglob('*')):
        if path.is_file():
            name = rel(path)
            require(before[name]['sha256'] == frozen_inventory[name]['sha256'], 'ORIGINAL_CORPUS_FROZEN_HASH_MISMATCH')
            checks.append({'path': name, 'sha256': before[name]['sha256'], 'match': True})
    return checks

def console_text(status):
    ok = status == 'PASS'
    return '\n'.join([
        f'Phase 5C.4-B0 status: {status}', 'Purpose: REVIEWER_B_PACKET_SANITIZATION',
        'Previous B attempt preserved: ' + ('YES' if ok else 'NO'),
        'Previous B context reusable: NO', 'Contaminated packet: ' + ('QUARANTINED' if ok else 'FAIL'),
        'Candidates projected: 60/60', 'Reviewer-B visible fields: review_id_b, query',
        'Extra candidate metadata exposed: NO', 'Prefilled scope exposed: NO',
        'Annotator A labels exposed: NO', 'Split/family/dimension exposed: NO',
        'B-local IDs opaque: ' + status, 'Quality-blind shuffle: ' + status,
        'Query byte identity: ' + status, 'Projection structural audit: ' + status,
        'Semantic leakage audit: ' + status, 'D6: EMPIRICAL_UNVERIFIED',
        'Annotation performed: 0', 'Network/API calls: 0', 'Production/evaluator calls: 0',
        'Retrieval/reranking inference: 0', 'HOLDOUT plaintext printed publicly: NO',
        'HOLDOUT storage isolation: NOT_YET_ENFORCED', 'Preexisting artifact integrity: ' + status,
        'Ready for fresh Phase 5C.4-B retry: ' + ('YES' if ok else 'NO'),
        'Dataset freeze ready: NO', 'Agentic v2 implementation: NOT STARTED', 'STOP', ''])

def verify_completed():
    before = read_json(HERE / 'integrity_baseline_v0.json')['entries']
    current = snapshot()
    require(all(current.get(k) == v for k, v in before.items()), 'PREEXISTING_INTEGRITY_FAILED')
    require(all(is_allowed_addition(k) for k in current.keys() - before.keys()), 'UNAUTHORIZED_ADDITION')
    for name, expected in read_json(HERE / 'artifact_hashes_v0.json')['artifacts'].items():
        require(file_sha(ROOT / name) == expected['sha256'], 'B0_ARTIFACT_HASH_MISMATCH')
    source, literals = source_records()
    verify_projection(source, literals, corpus_inventory())
    validator_checks()
    validation = read_json(HERE / 'phase5c4b0_validation_v0.json')
    require(validation['phase_status'] == 'PASS' and len(validation['gates']) == 17 and
            all(g['status'] == 'PASS' for g in validation['gates']), 'B0_GATES_FAILED')
    old = read_json(BASE / 'reviewer_b_results/phase5c4b_validation_v0.json')
    require(old['phase_status'] == 'FAIL' and old['stop_reason'] == 'REVIEWER_B_PACKET_CONTAMINATED', 'OLD_FAILURE_CHANGED')
    print('Read-only B0 verification: PASS; 17/17 gates; 60/60 exact queries; preexisting integrity PASS.')

def build():
    os.umask(0o077)
    before = read_json(HERE / 'integrity_baseline_v0.json')['entries']
    require(ROOT == Path.cwd().resolve(), 'RUN_FROM_PROJECT_ROOT')
    require(not VISIBLE.exists() and all(not (CUSTODIAN / n).exists() for n in PRIVATE_NAMES), 'OUTPUT_ALREADY_EXISTS')
    require(all(p.name in {'integrity_baseline_v0.json', 'sanitize_reviewer_b_v1.py'} for p in HERE.iterdir()), 'REMEDIATION_ALREADY_STARTED')
    Path(__file__).chmod(0o600)  # this B0-created script only
    checks = frozen_checks(before)
    old = read_json(BASE / 'reviewer_b_results/phase5c4b_validation_v0.json')
    require(old['phase_status'] == 'FAIL' and old['stop_reason'] == 'REVIEWER_B_PACKET_CONTAMINATED' and
            old['independently_reviewed_count'] == 0 and old['annotation_A_read'] is False and
            old['A_labels_entered_prompts_context'] is False, 'PREVIOUS_FAILURE_STATE_UNEXPECTED')
    require((BASE / 'reviewer_b_results/annotation_B_v0.jsonl').stat().st_size == 0, 'PRIOR_B_ANNOTATION_NONEMPTY')
    prior = {'status': 'REVIEWER_B_PACKET_CONTAMINATED', 'phase_status': 'FAIL',
             'candidates_annotated': 0, 'substantive_A_labels_read': False,
             'reusable_for_annotation': False, 'disqualification': 'PERMANENT'}
    # Commit independent seeds before accessing any candidate row. No reseeding
    # or post-shuffle balancing based on quality, family, split or performance.
    provenance = {'schema': 'reviewer-b-shuffle-provenance-v1', 'committed_at_utc': now(),
                  'seed_hex': secrets.token_hex(32), 'id_key_hex': secrets.token_hex(32),
                  'seed_source': 'OS cryptographic randomness; chosen once before source rows are parsed',
                  'algorithm': 'Sort B-local IDs ascending by HMAC-SHA256(seed, ASCII B-local ID), with ID tie-break',
                  'id_algorithm': 'rb_ + first 32 lowercase hex digits of HMAC-SHA256(id_key, UTF8 canonical ID)',
                  'quality_blind': True, 'seed_reselection': False,
                  'annotation_quality_or_system_performance_inputs': [],
                  'input_hash_serialization': 'UTF8 compact JSON array of canonical IDs in source order',
                  'output_hash_serialization': 'UTF8 compact JSON array of B IDs in presentation order',
                  'authorized_roles': ['TRUSTED_DATASET_CUSTODIAN'], 'reviewer_b_access': 'FORBIDDEN'}
    # Private commitment in a new access record predates candidate processing.
    access = {'role': 'TRUSTED_DATASET_CUSTODIAN',
              'future_v2_implementation_in_this_context': 'FORBIDDEN',
              'current_context_reviewer_b_annotation': 'FORBIDDEN',
              'previous_reviewer_b_attempt': prior, 'fresh_B_session_required': True,
              'seed_commitment': sha(compact(provenance)), 'seed_committed_at_utc': provenance['committed_at_utc'],
              'seed_commitment_serialization': 'UTF8 compact JSON provenance before input/output hashes and committed_provenance_keys are added',
              'seed_commitment_key_order': list(provenance),
              'permitted_additions': {'visible_files': sorted(VISIBLE_NAMES), 'custodian_files': sorted(PRIVATE_NAMES),
                                     'remediation_directory': rel(HERE), 'remediation_files': sorted(REMEDIATION_NAMES)},
              'HOLDOUT_STORAGE_ISOLATION': 'NOT_YET_ENFORCED',
              'isolation_limit': 'Owner-only files do not prevent same-owner contexts from reading; no role-separated storage tested.',
              'annotation_performed': 0, 'D6': 'EMPIRICAL_UNVERIFIED',
              'network_api_calls': 0, 'production_calls': 0, 'evaluator_calls': 0,
              'retrieval_reranking_inference_calls': 0, 'system_outputs_substantively_accessed': 0,
              'additional_generation_calls': 0, 'annotation_research_calls': 0,
              'exact_queries_printed_publicly': False, 'dataset_freeze_ready': False,
              'execution_basis': 'Task-initiated local standard-library JSON, filesystem and hashing operations only. Binary hashing of all project files is distinct from substantive system-output inspection. No OS-wide network attestation claimed.',
              'source_access': 'Canonical source parsed locally for exact query projection and private existing-ID/order audit only; no new judgments and no A/B comparison. Source values not printed.',
              'visible_input_boundary': rel(VISIBLE), 'hashing_boundary': 'All preexisting regular project files; symlinks not followed'}
    write_json(HERE / 'execution_and_access_v0.json', access)
    source, literals = source_records()
    seed = bytes.fromhex(provenance['seed_hex']); key = bytes.fromhex(provenance['id_key_hex'])
    ids = {s['query_id']: 'rb_' + hmac.new(key, s['query_id'].encode('utf-8'), hashlib.sha256).hexdigest()[:32] for s in source}
    ordered = sorted(source, key=lambda s: (hmac.new(seed, ids[s['query_id']].encode('ascii'), hashlib.sha256).digest(), ids[s['query_id']]))
    require([s['query_id'] for s in ordered] != [s['query_id'] for s in source], 'SOURCE_ORDER_PRESERVED')
    provenance['input_list_sha256'] = sha(compact([s['query_id'] for s in source]))
    provenance['output_order_sha256'] = sha(compact([ids[s['query_id']] for s in ordered]))
    provenance['committed_provenance_keys'] = access['seed_commitment_key_order']
    write_json(CUSTODIAN / 'reviewer_b_shuffle_provenance_v1.json', provenance)
    # Preserve the actual source JSON string token too, beyond decoded UTF8 equality.
    packet = b''.join(b'{"review_id_b":' + compact(ids[s['query_id']]) + b',"query":' + literals[s['query_id']] + b'}\n' for s in ordered)
    mapping = [{'review_id_b': ids[s['query_id']], 'canonical_candidate_id': s['query_id'],
                'source_query_sha256': s['query_sha256'], 'projected_query_sha256': sha(s['query'].encode('utf-8')),
                'source_literal_sha256': sha(literals[s['query_id']]), 'projected_literal_sha256': sha(literals[s['query_id']])} for s in ordered]
    write_json(CUSTODIAN / 'reviewer_b_id_mapping_v1.json',
               {'authorized_roles': ['TRUSTED_DATASET_CUSTODIAN'], 'reviewer_b_access': 'FORBIDDEN',
                'implementation_access': 'FORBIDDEN', 'source': rel(SOURCE), 'source_file_sha256': file_sha(SOURCE), 'mapping': mapping})
    quarantine = {rel(p): before[rel(p)] for p in sorted((BASE / 'reviewer_b').rglob('*')) if p.is_file()}
    failure_files = {rel(p): before[rel(p)] for p in sorted((BASE / 'reviewer_b_results').rglob('*')) if p.is_file()}
    write_json(CUSTODIAN / 'contaminated_packet_quarantine_v0.json',
               {'status': 'QUARANTINED_CONTAMINATED_INPUT', 'use_for_future_annotation': 'FORBIDDEN',
                'quarantine_mode': 'Additive provenance/access prohibition; original files preserved in place; not an enforced filesystem boundary',
                'contaminated_packet_files': quarantine, 'previous_failed_attempt_files': failure_files,
                'previous_reviewer_b_attempt': prior, 'old_files_deleted_moved_or_modified': False,
                'historical_A_blindness_claim': 'Superseded for future B routing by the preserved failed B audit and this v1 boundary; historical A files remain unchanged.',
                'future_B_input': rel(VISIBLE), 'future_B_context': 'BRAND_NEW_SESSION_REQUIRED'})
    corpus = corpus_inventory()
    VISIBLE.mkdir(mode=0o700)
    write_new(VISIBLE / 'reviewer_b_queries_v1.jsonl', packet)
    write_new(VISIBLE / 'reviewer_b_annotation_instructions_v1.md', INSTRUCTIONS)
    write_json(VISIBLE / 'reviewer_b_packet_manifest_v1.json', expected_manifest(sha(packet), corpus))
    audit = verify_projection(source, literals, corpus)
    audit['validator_controls'] = validator_checks()
    audit['source_file_sha256'] = file_sha(SOURCE)
    audit['frozen_source_checks'] = checks
    audit['whole_original_corpus_inventory'] = corpus
    audit['existing_identifier_order_audit'] = {
        'original_ids_hash_derived': all(re.fullmatch(r'q_[0-9a-f]{20}', s['query_id']) for s in source),
        'source_id_derivation': 'Existing construction script hashes a public fixed domain plus construction key; not independently salted for B.',
        'canonical_order_adjacent_same_primary_family': sum(a['primary_family'] == b['primary_family'] for a, b in zip(source, source[1:])),
        'canonical_order_adjacent_same_provisional_split': sum(a['provisional_split'] == b['provisional_split'] for a, b in zip(source, source[1:])),
        'decision': 'Do not expose canonical IDs or construction order. Independently keyed IDs and quality-blind order used for all 60; no post-shuffle tuning.',
        'limitations': 'Random order can have chance runs; no claim of zero statistical correlation. No interpretation or label was changed.'}
    audit['seed_commitment_verified'] = sha(compact({k: provenance[k] for k in access['seed_commitment_key_order']})) == access['seed_commitment']
    require(audit['seed_commitment_verified'], 'SEED_COMMITMENT_MISMATCH')
    write_json(CUSTODIAN / 'reviewer_b_packet_projection_audit_v1.json', audit)
    handoff = '''# Fresh Phase 5C.4-B session handoff

Use a completely new session. The previous failed B session and the B0 custodian
session are permanently ineligible for independent B annotation. This handoff
contains no candidate text, IDs, mapping, split, or A judgments.

Run Phase 5C.4-B independent annotation using ONLY the new input packet:
data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_packet_v1/
Read its manifest and instructions first. Each of its 60 records has exactly
review_id_b and query. The entire original data/versions/corpus-v0.1/ is allowed
for independent local text search/read/hierarchy inspection.

Do not read old reviewer_b/, reviewer_b_results/, custodian/, public per-candidate
summaries, mappings, A judgments, comparison materials, or system outputs. Do not
reopen this custodian directory; the user may paste this handoff into the fresh
session. Obtain any needed generic frozen rubric through a separately authorized
candidate-independent input before annotating; no A examples or implied labels.
No historical query reference is included; obtain a separately authorized blind
query-text-only resource before claiming historical duplication review complete.

Use a new reviewer_b_results_v1/ namespace if authorized by the new session's
task. Preserve all previous artifacts. Record only independently reconstructed
judgments keyed by review_id_b, with corpus research activity separate from
production inference. No A/B comparison, adjudication, D6 measurement, inference,
network/API, evaluator, dataset freeze, or Agentic v2 implementation. Never print
exact queries or gold publicly. D6 stays EMPIRICAL_UNVERIFIED. Storage isolation
remains NOT_YET_ENFORCED. Stop on any unexpected prefilled candidate information.

The historical B failure remains FAIL — REVIEWER_B_PACKET_CONTAMINATED at 0/60.
B0 PASS authorizes a fresh packet retry, not an annotation-completion or freeze
claim. No annotation has been performed by B0.
'''
    write_new(HERE / 'fresh_reviewer_b_handoff_v1.md', handoff)
    after = snapshot()
    differences = [name for name, entry in before.items() if after.get(name) != entry]
    added = sorted(after.keys() - before.keys())
    require(not differences, 'PREEXISTING_INTEGRITY_FAILED')
    require(all(is_allowed_addition(k) for k in added), 'UNAUTHORIZED_ADDITION')
    integrity = {'status': 'PASS', 'preexisting_regular_files': sum(e['kind'] == 'file' for e in before.values()),
                 'preexisting_symlinks': sum(e['kind'] == 'symlink' for e in before.values()),
                 'all_preexisting_files_byte_identical': True, 'modes_and_symlink_targets_unchanged': True,
                 'differences': differences, 'after_entries': {k: after[k] for k in before},
                 'additions_at_hash_sweep': added, 'permitted_final_additions': access['permitted_additions'],
                 'all_additions_scoped': True, 'baseline_sha256': file_sha(HERE / 'integrity_baseline_v0.json'),
                 'scope_note': 'Before captured before first B0 write; after hashes every preexisting file again. B0 summary, console, validation and hash registry are additive and verified by --verify afterward.'}
    write_json(HERE / 'integrity_before_after_v0.json', integrity)
    gate_names = ['previous_failed_B_attempt_preserved', 'previous_B_context_permanently_unusable',
                  'all_60_candidates_projected', 'exact_two_field_schema', 'no_A_scope_or_annotation_metadata',
                  'no_split_family_cluster_dimension_metadata', 'opaque_B_local_ids',
                  'quality_blind_order_with_committed_provenance', 'query_UTF8_and_JSON_literal_byte_identity',
                  'old_packet_quarantined_without_mutation', 'structural_raw_and_semantic_projection_audits',
                  'no_annotation_performed', 'D6_empirical_unverified', 'no_substantive_system_output_access',
                  'no_inference_API_network', 'all_preexisting_artifacts_unchanged', 'no_exact_queries_printed_publicly']
    validation = {'phase': '5C.4-B0', 'phase_status': 'PASS', 'purpose': 'REVIEWER_B_PACKET_SANITIZATION',
                  'gates': [{'gate_number': i + 1, 'gate': name, 'status': 'PASS'} for i, name in enumerate(gate_names)],
                  'previous_reviewer_b_attempt': prior, 'candidate_count': 60, 'annotation_performed': 0,
                  'fresh_B_retry_ready': True, 'fresh_session_required': True, 'B_annotation_started': False,
                  'dataset_freeze_ready': False, 'D6': 'EMPIRICAL_UNVERIFIED',
                  'storage_isolation': 'NOT_YET_ENFORCED', 'implementation': 'NOT_STARTED',
                  'execution_audit': 'execution_and_access_v0.json',
                  'projection_audit': '../reviewer_b_packet_projection_audit_v1.json',
                  'integrity_audit': 'integrity_before_after_v0.json', 'checked_at_utc': now()}
    console = console_text('PASS')
    summary = '''# Phase 5C.4-B0 — PASS

The new packet projects all 60 canonical candidates to exactly review_id_b and
query. Every query matches both decoded UTF-8 bytes and its original JSON string
token. No A scope, interpretation, evidence selection, split, family, cluster,
dimension or admission metadata is provided. The independent B IDs, private
mapping and deterministic quality-blind shuffle are validated locally.

The raw-byte audit scans all visible filenames and contents. Immutable query
literals and reviewed generic rubric/access language are explicitly classified;
they are not silently removed or treated as candidate metadata. All other bytes
match the approved projection and generic templates. Structural rejection checks
cover extra/nested fields, duplicate JSON keys, IDs and queries, malformed values,
comments, invalid encoding and incorrect counts.

The previous B failure is preserved unchanged at 0/60. The old input remains in
place with private QUARANTINED_CONTAMINATED_INPUT provenance and future use
FORBIDDEN. That B context and this custodian context cannot annotate independently.
A brand-new B session is required. Fresh retry is ready; no B annotation was run.

All preexisting files and symlinks match the before snapshot. Only the explicitly
allowed packet and additive custodian remediation artifacts were created.
Network/API, production/evaluator, retrieval/reranking inference, annotation and
D6 measurements are zero. Binary integrity hashing is not substantive inspection
of system outputs. No exact queries or gold were printed in public output.

HOLDOUT_STORAGE_ISOLATION_NOT_YET_ENFORCED remains in effect. Owner-only modes
do not isolate roles sharing an OS identity. Dataset freeze is not ready, and
Agentic v2 implementation is NOT STARTED and forbidden in this exposed context.
See fresh_reviewer_b_handoff_v1.md for the candidate-free next-session handoff.

STOP
'''
    for public_safe in [console, summary, handoff, encoded(validation).decode('utf-8')]:
        require(not any(s['query'] in public_safe for s in source), 'PUBLIC_EXACT_QUERY_FOUND')
    write_json(HERE / 'phase5c4b0_validation_v0.json', validation)
    write_new(HERE / 'phase5c4b0_console_v0.txt', console)
    write_new(HERE / 'phase5c4b0_review_summary_v0.md', summary)
    final_files = [p for p in VISIBLE.iterdir()] + [CUSTODIAN / n for n in PRIVATE_NAMES] + list(HERE.iterdir())
    write_json(HERE / 'artifact_hashes_v0.json',
               {'purpose': 'B0 remediation provenance only; not dataset freeze', 'algorithm': 'sha256',
                'self_excluded': True, 'artifacts': {rel(p): {'sha256': file_sha(p), 'size_bytes': p.stat().st_size}
                                                   for p in sorted(final_files) if p.is_file()}})
    print(console, end='')

if __name__ == '__main__':
    try:
        if sys.argv[1:] == ['--verify']:
            verify_completed()
        else:
            require(not sys.argv[1:], 'UNKNOWN_ARGUMENT')
            build()
    except Exception as error:
        # Keep exception values/source rows out of public console. Diagnose by
        # inspecting code or writing a new custodian-private failure record.
        print('Phase 5C.4-B0 execution stopped before completion; no fresh B retry authorized by this run.', file=sys.stderr)
        if isinstance(error, RuntimeError) and re.fullmatch(r'[A-Z_]+', str(error)):
            print('Validation code: ' + str(error), file=sys.stderr)
        else:
            print('Error type: ' + type(error).__name__, file=sys.stderr)
        raise SystemExit(1) from None
