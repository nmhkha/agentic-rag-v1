"""Custodian-only B1 projection and audit; local standard library only."""
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import sys

HERE = Path(__file__).resolve().parent
BASE = HERE.parent.parent
ROOT = BASE.parents[4]
SOURCE = BASE / 'reviewer_b/contamination_query_only_sources_v0.json'
OUTPUT = BASE / 'reviewer_b_packet_v1/contamination_reference_medical_v1.json'
AUDIT = HERE / 'medical_reference_projection_audit_v1.json'
CONSOLE = HERE / 'phase5c4b1_console_v0.txt'
AUTHORITATIVE_QUERY = 'Tôi muốn xây dựng một chatbot y tế, tôi cần lưu ý điều gì'
FORBIDDEN = re.compile(rb'score|gold|answer|trace|retrieval|expansion|revision|failure|dimension|support|aspect|evidence|agentic|standard|annotator|intervention|answerability', re.I)

def require(condition, code):
    if not condition:
        raise RuntimeError(code)

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def path_name(path):
    return path.relative_to(ROOT).as_posix()

def encoded(obj):
    return (json.dumps(obj, ensure_ascii=False, indent=2) + '\n').encode('utf-8')

def no_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, 'DUPLICATE_KEY')
        result[key] = value
    return result

def validate(raw):
    try:
        obj = json.loads(raw, object_pairs_hook=no_duplicate_keys)
    except (ValueError, UnicodeError):
        raise RuntimeError('INVALID_JSON') from None
    require(type(obj) is dict and set(obj) == {'reference_id', 'query'}, 'EXACT_KEYS_REQUIRED')
    require(type(obj['reference_id']) is str and obj['reference_id'] == 'expl_medical_001', 'REFERENCE_ID_MISMATCH')
    require(type(obj['query']) is str and obj['query'].encode('utf-8') == AUTHORITATIVE_QUERY.encode('utf-8'), 'QUERY_BYTE_IDENTITY_FAILED')
    require(raw == encoded({'reference_id': 'expl_medical_001', 'query': AUTHORITATIVE_QUERY}), 'UNEXPECTED_RAW_BYTES')
    require(not FORBIDDEN.search(raw), 'FORBIDDEN_RAW_TERM')
    return obj

def write_new(path, raw):
    with os.fdopen(os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600), 'wb') as f:
        f.write(raw)

def inventory():
    result = {}
    for directory, dirs, files in os.walk(ROOT, followlinks=False):
        for name in sorted(dirs + files):
            p = Path(directory) / name
            mode = p.lstat().st_mode
            if stat.S_ISLNK(mode):
                result[path_name(p)] = {'kind': 'symlink', 'target': os.readlink(p), 'mode': stat.S_IMODE(mode)}
            elif stat.S_ISREG(mode):
                h = hashlib.sha256()
                with p.open('rb') as f:
                    for b in iter(lambda: f.read(1048576), b''):
                        h.update(b)
                result[path_name(p)] = {'kind': 'file', 'sha256': h.hexdigest(), 'size_bytes': p.stat().st_size, 'mode': stat.S_IMODE(mode)}
            else:
                require(stat.S_ISDIR(mode), 'UNSUPPORTED_ENTRY')
    return dict(sorted(result.items()))

def main():
    os.umask(0o077)
    Path(__file__).chmod(0o600)
    require(ROOT == Path.cwd().resolve(), 'RUN_FROM_PROJECT_ROOT')
    require(not any(p.exists() for p in [OUTPUT, AUDIT, CONSOLE]), 'OUTPUT_ALREADY_EXISTS')
    before = inventory()
    source_raw = SOURCE.read_bytes()
    source = json.loads(source_raw, object_pairs_hook=no_duplicate_keys)
    matches = [(i, row) for i, row in enumerate(source['queries'])
               if type(row) is dict and row.get('query') == AUTHORITATIVE_QUERY]
    require(len(matches) == 1, 'SOURCE_EXACT_MATCH_NOT_UNIQUE')
    index, record = matches[0]
    require(set(record) == {'id', 'query'}, 'SOURCE_RECORD_METADATA_NOT_ALLOWED')
    require(type(record['id']) is str and re.fullmatch(r'[A-Za-z0-9_-]{1,100}', record['id']), 'SOURCE_ID_NOT_PLAIN_IDENTIFIER')
    require(not FORBIDDEN.search(encoded(record)), 'SOURCE_RECORD_FORBIDDEN_TERM')
    source_query = record['query'].encode('utf-8')
    require(source_query == AUTHORITATIVE_QUERY.encode('utf-8'), 'SOURCE_PROVENANCE_QUERY_MISMATCH')
    raw = encoded({'reference_id': 'expl_medical_001', 'query': record['query']})
    obj = validate(raw)
    controls = []
    for field in ['score', 'gold', 'trace', 'annotation_A', 'metadata', 'reference_type']:
        modified = dict(obj); modified[field] = {'hidden': True}
        controls.append(encoded(modified))
    for value in [None, '', {}, [], AUTHORITATIVE_QUERY + ' ']:
        modified = dict(obj); modified['query'] = value
        controls.append(encoded(modified))
    controls += [raw.replace(b'"query":', b'"query":"hidden","query":', 1), raw + b'// trace\n']
    for bad in controls:
        try:
            validate(bad)
        except RuntimeError:
            pass
        else:
            raise RuntimeError('NEGATIVE_CONTROL_ACCEPTED')
    write_new(OUTPUT, raw)
    require(OUTPUT.read_bytes() == raw, 'WRITTEN_OUTPUT_MISMATCH')
    validate(OUTPUT.read_bytes())
    after = inventory()
    changed = sorted(k for k in before if before[k] != after.get(k))
    additions = sorted(after.keys() - before.keys())
    require(not changed, 'PREEXISTING_FILE_CHANGED')
    require(additions == [path_name(OUTPUT)], 'UNEXPECTED_ADDITION')
    old_files = {k: v for k, v in before.items() if k != path_name(Path(__file__))}
    old_after = {k: after[k] for k in old_files}
    console = '''Phase 5C.4-B1 reference preparation:
PASS

Role:
TRUSTED_DATASET_CUSTODIAN

Medical contamination reference created:
YES

Reference records:
1

Visible fields:
reference_id, query

System outcome metadata included:
NO

Annotation A metadata included:
NO

Gold/evidence metadata included:
NO

Exact diagnostic query byte identity:
PASS

Structural audit:
PASS

Semantic leakage audit:
PASS

Network/API calls:
0

Production/evaluator calls:
0

Retrieval/reranking inference:
0

Ready for Reviewer B contamination completion:
YES

Dataset freeze ready:
NO

STOP
'''
    require(source_query not in console.encode('utf-8'), 'PUBLIC_QUERY_LEAK')
    audit = {
        'phase': '5C.4-B1', 'status': 'PASS', 'role': 'TRUSTED_DATASET_CUSTODIAN',
        'purpose': 'contamination screening only',
        'reference_status': 'EXPLORATORY / NON-BENCHMARK / NON-CONFIRMATORY',
        'not_gold_or_challenge_item': True, 'substantive_annotation_influence': 'FORBIDDEN',
        'source_used': path_name(SOURCE), 'source_sha256': sha(source_raw),
        'source_record_index_zero_based': index, 'source_record_keys': sorted(record),
        'source_record_serialized_sha256': sha(encoded(record)),
        'source_validation': {'status': 'PASS', 'plain_query_identifier_and_exact_text_only': True,
                              'source_record_forbidden_raw_scan_matches': 0,
                              'outer_wrapper_fields_copied': False,
                              'quarantine_bypassed_for_B': False,
                              'access_basis': 'Explicit B1 custodian-only source inspection; old packet remains quarantined for B.'},
        'sanitized_output': path_name(OUTPUT), 'sanitized_output_sha256': sha(raw),
        'reference_id': 'expl_medical_001', 'reference_records': 1,
        'allowed_fields': ['reference_id', 'query'],
        'source_query_utf8_sha256': sha(source_query),
        'projected_query_utf8_sha256': sha(obj['query'].encode('utf-8')),
        'authoritative_user_query_utf8_sha256': sha(AUTHORITATIVE_QUERY.encode('utf-8')),
        'exact_byte_identity': 'PASS',
        'byte_identity_definition': 'Decoded query strings encoded as UTF-8, compared exactly with no Unicode normalization, trimming or rewriting. JSON formatting is not query content.',
        'structural_audit': 'PASS', 'negative_controls_rejected': len(controls),
        'forbidden_field_scan': {'status': 'PASS', 'pattern': FORBIDDEN.pattern.decode('ascii'),
                                 'raw_output_matches': 0, 'query_exemptions_needed': 0,
                                 'scope': 'Entire source record and entire output bytes including keys and values; exact canonical output layout enforced, no comments or extra bytes.'},
        'semantic_leakage_audit': {'status': 'PASS', 'query_adjacent_information': 'Fixed reference identifier only',
                                   'query_copied_from_validated_source': True,
                                   'system_outcomes_A_labels_gold_evidence_copied': False,
                                   'interpretations_hypotheses_or_similarity_hints_copied': False},
        'integrity': {'status': 'PASS', 'preexisting_regular_files': sum(v['kind'] == 'file' for v in old_files.values()),
                      'preexisting_symlinks': sum(v['kind'] == 'symlink' for v in old_files.values()),
                      'before_inventory_sha256': sha(encoded(old_files)), 'after_inventory_sha256': sha(encoded(old_after)),
                      'inventory_encoding': 'UTF8 JSON, indent=2, ensure_ascii=False, paths sorted, trailing newline',
                      'all_preexisting_bytes_modes_and_symlink_targets_unchanged': True,
                      'changed_or_missing': changed,
                      'allowed_B1_additions': [path_name(p) for p in [Path(__file__), OUTPUT, AUDIT, CONSOLE]],
                      'scope': 'All preexisting regular project files streamed for hashes only, including annotation files without substantive inspection. B1-created script excluded from preexisting counts; its hash recorded separately.'},
        'B0_compatibility': 'Authorized additive B1 reference. Original B0 packet files, manifest and historical audit unchanged. B0 exact-three-file allowlist is a historical B0 check; this B1 audit records the extension.',
        'execution': {'annotation_B_substantive_results_opened': False, 'annotation_A_opened': False,
                      'annotation_performed': 0, 'A_B_comparison': 0, 'adjudication': 0, 'D6_runs': 0,
                      'candidate_query_or_split_changes': 0, 'network_api_calls': 0,
                      'production_evaluator_calls': 0, 'retrieval_reranking_inference': 0,
                      'system_outputs_substantively_accessed': 0,
                      'exact_diagnostic_query_printed_publicly': False,
                      'basis': 'Task-initiated local standard-library operations only; binary integrity hashing is not substantive annotation/output inspection; not OS-wide network attestation.'},
        'storage_isolation': 'NOT_YET_ENFORCED',
        'future_v2_implementation_in_this_context': 'FORBIDDEN',
        'reviewer_B_contamination_completion_ready': True, 'contamination_screening_performed_here': False,
        'B_substantive_retry_status': 'User-reported PASS; substantive B results not opened or independently reassessed in B1',
        'dataset_freeze_ready': False, 'script_sha256': sha(Path(__file__).read_bytes()),
        'console_sha256': sha(console.encode('utf-8')),
    }
    require(source_query not in encoded(audit), 'AUDIT_QUERY_PLAINTEXT_LEAK')
    write_new(CONSOLE, console.encode('utf-8'))
    write_new(AUDIT, encoded(audit))
    require(sha(OUTPUT.read_bytes()) == audit['sanitized_output_sha256'], 'FINAL_OUTPUT_HASH_MISMATCH')
    print(console, end='')

if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print('Phase 5C.4-B1 reference preparation: FAIL; retry not authorized by this run.', file=sys.stderr)
        if isinstance(error, RuntimeError) and re.fullmatch('[A-Z_]+', str(error)):
            print('Audit code: ' + str(error), file=sys.stderr)
        else:
            print('Error type: ' + type(error).__name__, file=sys.stderr)
        raise SystemExit(1) from None
