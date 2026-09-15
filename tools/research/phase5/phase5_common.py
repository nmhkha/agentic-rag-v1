"""Small serialization primitives shared by the isolated worker and trusted tools."""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path


def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(',', ':'), allow_nan=False).encode('utf-8')


def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()


def file_hash(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def sync_dir(path):
    fd = os.open(path, os.O_RDONLY | os.O_DIRECTORY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def exclusive_json(path, value):
    exclusive_bytes(path, canonical(value))


def exclusive_bytes(path, data):
    """A partial/crashed write remains a collision, never an excuse to regenerate."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('xb') as stream:
        stream.write(data)
        stream.flush()
        os.fsync(stream.fileno())
    sync_dir(path.parent)


def validate_queries(rows, expected_hash, expected_count=31):
    if type(rows) is not list or len(rows) != expected_count:
        raise ValueError('query count/schema mismatch')
    ids, texts = set(), set()
    for row in rows:
        if type(row) is not dict or set(row) != {'query_id', 'query'}:
            raise ValueError('query record must have exactly two fields')
        if any(type(row[k]) is not str or not row[k].strip() for k in row):
            raise ValueError('query values must be nonempty strings')
        if row['query_id'] in ids or row['query'] in texts:
            raise ValueError('duplicate query')
        ids.add(row['query_id'])
        texts.add(row['query'])
    if digest(rows) != expected_hash:
        raise ValueError('query order/text/hash mismatch')
    return rows
