# M1 ingestion migration

## Scope and mapping

M1 bootstraps the `legal-rag` package with a `src/` layout and migrates only
the reusable ingestion behavior. The original scripts remain unchanged and are
marked `LEGACY_PENDING_REMOVAL`.

| Legacy file | New module | Status |
| --- | --- | --- |
| `scripts/extract_docx.py` | `src/legal_rag/ingestion/extractors.py` | `LEGACY_PENDING_REMOVAL` |
| `scripts/clean_docx_text.py` | `src/legal_rag/ingestion/cleaners.py` | `LEGACY_PENDING_REMOVAL` |
| `scripts/parse_legal_structure.py` | `src/legal_rag/ingestion/parsers.py` | `LEGACY_PENDING_REMOVAL` |
| `scripts/validate_corpus.py` | `src/legal_rag/ingestion/validators.py` | `LEGACY_PENDING_REMOVAL` |

No retrieval, generation, evaluation, Agentic RAG v1, benchmark-gold,
historical-trace, or Phase 5 file is changed.

## Public library functions

The package exports these primary APIs from `legal_rag.ingestion`:

- `extract_document(path)` returns `(text, paragraph_count, table_count)`.
- `clean_text(raw_text, boilerplate_lines)` returns cleaned text and the exact
  normalized boilerplate lines removed.
- `parse_legal_structure(text, document_id=..., document_number=...,
  document_title=...)` returns the legacy `Article` objects.
- `validate_corpus(registry_path=..., articles_path=..., chunks_path=...)`
  returns a `ValidationCollector` and chunk statistics without writing reports
  or terminating the process.

Lower-level legacy-compatible functions and data classes remain available from
their respective modules. Importing any module performs no ingestion, argument
parsing, file write, or process exit.

## Preserved behavior

The migration retains body-level paragraph/table order; table row rendering
with `" | "`; skipping wholly empty rows; relative blank boundaries; Unicode
NFC; NBSP replacement; horizontal whitespace compaction; CRLF/CR conversion;
single repeated blanks; exact configured boilerplate removal; and the existing
Part, Chapter, Section, Subsection, Article, Clause, and Point rules.

The historical appendix rule is unchanged: a line matching the legacy appendix
start pattern closes the current Article and excludes that line and all
following non-empty lines from article parsing. The source cleaned text remains
untouched.

No lowercasing beyond the legacy point/identifier serialization, spelling
correction, semantic rewrite, LLM cleaning, character guessing, semantic merge,
or new chunking heuristic was introduced. Chunk IDs and chunk validation rules
remain unchanged. Chunk construction itself is deliberately not migrated.

`python-docx` is declared as the extraction dependency. A small standard-library
OOXML fallback keeps package imports and deterministic offline verification
possible when that dependency has not yet been installed; its output was checked
byte-for-byte against all available legacy-produced raw artifacts.

## CLI

`scripts/ingest.py` is a thin command for one document. It accepts source and
metadata arguments, calls the library for extraction, cleaning, and parsing,
and writes raw text, cleaned text, and article JSONL beneath the requested
output directory. It does not duplicate ingestion rules.

Example after `pip install -e .`:

```bash
python scripts/ingest.py data/raw/docx/134-2025-QH15.docx \
  --output-dir /tmp/legal-rag-ingest \
  --document-id 134-2025-QH15 \
  --document-number 134/2025/QH15 \
  --document-title "Luật mẫu" \
  --boilerplate-file data/source_registry/boilerplate_lines.txt
```

The CLI stops after parsing. `scripts/build_chunks.py` remains deferred, so the
CLI neither creates chunks nor runs corpus-level validation, which requires an
existing chunks JSONL. The library validator can validate explicit existing
registry/article/chunk paths independently.

## Tests and equivalence checks

The ingestion suite contains 9 offline tests across the required four files.
It covers paragraph/table order, empty table rows, document counts, NFC, NBSP,
horizontal whitespace, line endings, repeated blanks, exact boilerplate
removal, the complete supported legal hierarchy, Clause and Point parsing,
appendix exclusion, date/identity/duplicate structure checks, duplicate chunk
IDs, and retrieval-text containment.

Representative cleaning and parsing tests load the unchanged legacy modules and
compare outputs directly. Full-corpus checks additionally produced:

| Stage | Compared corpus | Result |
| --- | --- | --- |
| Extraction | 3 DOCX files vs checked-in legacy `.raw.txt` | byte-identical |
| Cleaning | 3 raw files, old vs new and checked-in `.cleaned.txt` | byte-identical |
| Parsing | 3 cleaned files, old vs new (35 + 46 + 5 Articles) | structurally identical |
| Validation | current registry/articles/chunks, old vs new | identical: 0 errors, 4 warnings |

All comparisons were read-only or wrote beneath `/tmp`; no corpus artifact was
overwritten. Editable installation was verified in a temporary virtual
environment with dependency resolution disabled because M1 prohibits network
access. Normal `pip install -e .` will install the declared `python-docx`
dependency when an index is available.

## Deferred script classification

| File | Classification | M1 decision |
| --- | --- | --- |
| `scripts/build_chunks.py` | ingestion core | Deferred; preserves current chunk IDs and heuristics in place until the chunking boundary is migrated explicitly. |
| `scripts/hash_raw_files.py` | dataset maintenance | Deferred; hashes source assets but is not ingestion transformation logic. |
| `scripts/check_register.py` | legacy-only tooling | Deferred; it targets older `local_pdf_path`/`review_status` columns rather than the current registry schema. |
| `scripts/update_source_hashes.py` | dataset maintenance | Deferred; safely updates registry source hashes and backups. |
| `scripts/update_verification_status.py` | annotation tooling | Deferred; records manual verification state and reviewer identity. |
| `scripts/create_verification_samples.py` | annotation tooling | Deferred; creates deterministic human-review checklists. |
| `scripts/inspect_chunk_issues.py` | validation tooling | Deferred; reports duplicate/short chunks without changing ingestion output. |

## Known limitations

- Chunk creation is intentionally absent from the M1 CLI.
- Corpus-level validation needs already-built `articles.jsonl` and
  `chunks.jsonl` inputs.
- The standard-library DOCX fallback covers the legacy serialization used by
  the available corpus. `python-docx` remains the declared primary dependency
  for general DOCX compatibility.
- The copied `.venv` contains an inherited installation-path inconsistency, so
  packaging verification used a clean temporary environment rather than
  mutating that environment or the frozen repository.
