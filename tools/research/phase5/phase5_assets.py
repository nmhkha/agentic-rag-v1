"""Offline model/cache and actual pipeline configuration verification."""
from __future__ import annotations
import importlib.metadata
import hashlib
import json
import os
from pathlib import Path
import platform
import sys
from phase5_common import digest, file_hash

DENSE = ('jinaai/jina-embeddings-v3', 'ab036b023d30b4d1138c4c3bfa9f0c445ab455d6')
RERANKER = ('BAAI/bge-reranker-v2-m3', '953dc6f6f85a1b2dbfca4c34a2796e7dde08d41e')


def cache_root():
    return Path(os.environ.get('HF_HUB_CACHE', os.environ.get('HUGGINGFACE_HUB_CACHE', str(Path(os.environ.get('HF_HOME', Path.home() / '.cache/huggingface')) / 'hub'))))


def inspect_snapshot(cache, model_id, revision, *, require_main=False):
    repo = Path(cache) / ('models--' + model_id.replace('/', '--'))
    snapshot = repo / 'snapshots' / revision
    result = dict(model_id=model_id, expected_revision=revision, resolved_revision=None,
                  snapshot=str(snapshot), model_pass=False, tokenizer_pass=False, files={}, errors=[])
    if not snapshot.is_dir() or snapshot.is_symlink():
        result['errors'].append('missing exact snapshot directory')
        return result
    if require_main:
        ref = repo / 'refs/main'
        if not ref.is_file() or ref.read_text().strip() != revision:
            result['errors'].append('default revision=None does not resolve to expected refs/main')
    required = ['config.json', 'tokenizer_config.json', 'tokenizer.json', 'special_tokens_map.json']
    if (snapshot / 'sentencepiece.bpe.model').exists():
        required.append('sentencepiece.bpe.model')
    weights = snapshot / 'model.safetensors'
    if weights.is_file():
        required.append(weights.name)
    elif (snapshot / 'model.safetensors.index.json').is_file():
        required.append('model.safetensors.index.json')
        try:
            required.extend(set(json.loads((snapshot / required[-1]).read_text())['weight_map'].values()))
        except (ValueError, KeyError):
            result['errors'].append('invalid weight shard index')
    else:
        result['errors'].append('missing safetensors weights')
    for name in sorted(set(required)):
        path = snapshot / name
        resolved = path.resolve()
        if not path.is_file() or not path.stat().st_size or not resolved.is_relative_to(repo.resolve()):
            result['errors'].append('missing/empty/escaped asset: ' + name)
            continue
        result['files'][name] = {'resolved_path': str(resolved), 'sha256': file_hash(path), 'size': path.stat().st_size}
        if resolved.parent.name == 'blobs':
            if len(resolved.name) == 64:
                blob_hash = result['files'][name]['sha256']
            elif len(resolved.name) == 40:
                content = path.read_bytes()
                blob_hash = hashlib.sha1(b'blob ' + str(len(content)).encode() + b'\0' + content).hexdigest()
            else:
                blob_hash = None
            if blob_hash != resolved.name:
                result['errors'].append('cache blob content hash mismatch: ' + name)
        if name.endswith('.json'):
            try:
                json.loads(path.read_text())
            except ValueError:
                result['errors'].append('invalid JSON: ' + name)
    result['resolved_revision'] = revision
    result['tokenizer_pass'] = all(k in result['files'] for k in ('tokenizer_config.json', 'tokenizer.json', 'special_tokens_map.json')) and not any('token' in e or 'revision' in e for e in result['errors'])
    result['model_pass'] = not result['errors']
    return result


def environment():
    versions = {d.metadata['Name']: d.version for d in importlib.metadata.distributions() if d.metadata['Name']}
    return dict(python_executable=sys.executable, python_version=platform.python_version(), packages=dict(sorted(versions.items())),
                configured_model=os.environ.get('RAG_LLM_MODEL', ''), expected_model='gemini-3.5-flash-lite')


def validate_environment(config):
    expected = dict(device='cpu', dense_dtype='float32', reranker_dtype='float32',
                    dense_batch_size=4, reranker_batch_size=1, llm_model='gemini-3.5-flash-lite',
                    llm_timeout_seconds=120.0, production_max_transport_attempts=1, max_llm_calls=6)
    for key, value in expected.items():
        if type(config.get(key)) is not type(value) or config[key] != value:
            raise ValueError('environment configuration drift: ' + key)


def inspect_loaded_pipeline(pipeline):
    """Check actual loaded models, never merely repeat manifest strings."""
    dense = pipeline.retriever.dense
    rank = pipeline.retriever.reranker
    values = dict(device=dense.device, dense_dtype=str(next(dense.model.parameters()).dtype).removeprefix('torch.'),
                  reranker_dtype=str(next(rank.model.parameters()).dtype).removeprefix('torch.'),
                  dense_batch_size=dense.batch_size, reranker_batch_size=rank.batch_size,
                  dense_revision=dense.model.config._commit_hash, reranker_revision=rank.model.config._commit_hash,
                  reranker_device=rank.device, reranker_max_length=rank.max_length,
                  dense_tokenizer=str(getattr(dense.model, 'tokenizer', None)),
                  reranker_tokenizer_source=rank.tokenizer.name_or_path)
    expected = dict(device='cpu', dense_dtype='float32', reranker_dtype='float32', dense_batch_size=4,
                    reranker_batch_size=1, dense_revision=DENSE[1], reranker_revision=RERANKER[1],
                    reranker_device='cpu', reranker_max_length=8192)
    for key, value in expected.items():
        if values[key] != value:
            raise ValueError('loaded pipeline drift: ' + key)
    # Compare the ACTUAL runtime tokenizer backend and special-token configuration
    # to an explicit local snapshot load. A model alias alone is insufficient.
    from transformers import AutoTokenizer
    for name, actual, identity in [('dense', dense.model.roberta.tokenizer, DENSE), ('reranker', rank.tokenizer, RERANKER)]:
        snapshot = cache_root() / ('models--' + identity[0].replace('/', '--')) / 'snapshots' / identity[1]
        expected_tokenizer = AutoTokenizer.from_pretrained(str(snapshot), local_files_only=True, trust_remote_code=True)
        def fingerprint(tokenizer):
            return digest({'backend': json.loads(tokenizer.backend_tokenizer.to_str()),
                           'special_tokens': tokenizer.special_tokens_map, 'model_max_length': tokenizer.model_max_length})
        actual_hash, expected_hash = fingerprint(actual), fingerprint(expected_tokenizer)
        if actual_hash != expected_hash:
            raise ValueError('actual tokenizer differs from exact snapshot: ' + name)
        values[name + '_tokenizer'] = dict(source=actual.name_or_path, snapshot=str(snapshot),
            revision=identity[1], actual_fingerprint=actual_hash, expected_fingerprint=expected_hash, verified=True)
    return values


def offline_load_probe(output, query_input):
    """Fresh process: same allowlist and loader as future production, zero queries."""
    from phase5_isolation import block_network
    counts = block_network()
    from phase5_ablation_runner import runtime_allowlist
    output = Path(output).absolute()
    output.mkdir(parents=True, exist_ok=True)
    os.environ.update(HF_MODULES_CACHE=str(output / 'modules'), TMPDIR=str(output),
                      HF_TOKEN_PATH=str(output / 'unused_hub_token'), HF_HUB_DISABLE_IMPLICIT_TOKEN='1')
    import tempfile
    tempfile.tempdir = str(output)
    guard = runtime_allowlist(output, Path(query_input), cache_root())
    try:
        with guard:
            from retrieval_pipeline import RetrievalPipeline
            values = inspect_loaded_pipeline(RetrievalPipeline())
        return {'status': 'PASS', 'actual': values, 'network': counts, 'reads': sorted(set(guard.reads))}
    except Exception as exc:
        return {'status': 'FAIL', 'error': type(exc).__name__ + ': ' + str(exc), 'network': counts}


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Offline load probe; no retrieval/generation')
    parser.add_argument('--scratch', type=Path, required=True)
    parser.add_argument('--query-input', type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(offline_load_probe(args.scratch, args.query_input)))
