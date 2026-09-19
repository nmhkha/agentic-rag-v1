# Web API handoff

## Scope and prerequisites

This is a local demonstration/research application, not a hardened public
service. The frontend is vanilla HTML/CSS/JS. Retrieval, Agentic control flow,
prompts and citation validation are unchanged. Use one Uvicorn worker and keep
the checkout, corpus and existing indexes together; an isolated wheel is not a
complete deployment of the research assets.

Tested on Windows, Python 3.12.14, torch 2.5.1+cpu, AMD Ryzen 7 6800HS Creator
Edition (8 physical cores / 16 logical processors), CPU inference. CUDA has not
been validated in this handoff. Start from the repository root:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
.\.venv\Scripts\python.exe -m pip check
```

Do not overwrite an existing environment blindly. Stop processes using it and
preserve a broken environment outside the deliverables before recreating it.
`einops` is required by Jina remote code. Network access is needed for initial
dependency/model downloads and subsequently for the LLM provider.

## Hugging Face / Jina cache preparation

The earlier experiment-specific `HF_MODULES_CACHE` workaround is no longer
necessary. The default Hub cache contained an incomplete remote-code snapshot:
top-level Jina code existed, but relative-import modules were missing. Fetching
only `*.py` at the exact remote-code revision repaired that cache, without
downloading model weights again or modifying core code.

Required snapshots for the tested baseline:

| Repository | Revision |
| --- | --- |
| jinaai/jina-embeddings-v3 | `ab036b023d30b4d1138c4c3bfa9f0c445ab455d6` |
| jinaai/xlm-roberta-flash-implementation | `bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3` |
| BAAI/bge-reranker-v2-m3 | `953dc6f6f85a1b2dbfca4c34a2796e7dde08d41e` |

Use the standard Hugging Face Hub cache. On a clean machine, the following
one-time Python setup downloads several GB of weights; on the tested machine
only the remote-code `snapshot_download` was needed. Run this with the venv's
Python while online. It deliberately makes the cache's `main` references point
at the tested revisions, so use a dedicated `HF_HUB_CACHE` if other projects
need different versions. These references are local cache metadata, not Git
branches or changes to the upstream models.

```python
from pathlib import Path
from huggingface_hub import snapshot_download

models = [
    ("jinaai/jina-embeddings-v3", "ab036b023d30b4d1138c4c3bfa9f0c445ab455d6",
     ["*.json", "*.safetensors", "*.model", "*.txt"]),
    ("jinaai/xlm-roberta-flash-implementation", "bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3",
     ["*.py"]),
    ("BAAI/bge-reranker-v2-m3", "953dc6f6f85a1b2dbfca4c34a2796e7dde08d41e",
     ["*.json", "*.safetensors", "*.model", "*.txt"]),
]
for repo, revision, patterns in models:
    snapshot = Path(snapshot_download(repo, revision=revision,
                                     allow_patterns=patterns, max_workers=1))
    refs = snapshot.parent.parent / "refs"
    refs.mkdir(exist_ok=True)
    (refs / "main").write_text(revision, encoding="utf-8")
```

Windows without symlink privileges may use copies and more disk space. A
parallel-download attempt encountered WinError 1314; the single-worker retry
completed successfully. Do not erase the cache or redownload weights as a first
response to a missing Python module.

For runtime, use a writable module cache independent of old experiments and
keep Hub/Transformers offline after preparation:

```powershell
$env:HF_MODULES_CACHE = Join-Path (Get-Location) '.cache\huggingface\modules'
$env:HF_HUB_OFFLINE = '1'
$env:TRANSFORMERS_OFFLINE = '1'
.\.venv\Scripts\python.exe -c "from legal_rag.retrieval.pipeline import RetrievalPipeline; p=RetrievalPipeline(); print(p.retriever.dense.model.config._commit_hash); print(p.retriever.reranker.resolved_revision)"
```

The production pipeline was successfully loaded offline into a newly empty
module cache during handoff, resolving the revisions above on CPU. A completely
fresh-machine download/install has not been exercised. Jina uses
`trust_remote_code`; treat cached code as executable dependencies.

Limitation: core's reranker constructor defaults to `revision=None`, and the
cross-repository remote-code lookup can follow `main`. Exact reproducibility
therefore relies on the prepared cache references plus offline mode, not a
new core-level pin. Online runtime or a shared cache updated by another project
can invalidate that assumption. No core change was made to hide this limitation.

## Temporary LLM configuration and serving

`.env.example` contains placeholders only and is not automatically loaded.
Set variables in the server process environment. In PowerShell, hidden input
avoids putting a credential literal in shell history:

```powershell
$env:RAG_LLM_MODEL = 'gemini-3.5-flash-lite'
$env:RAG_LLM_BASE_URL = 'https://generativelanguage.googleapis.com/v1beta/openai/'
$credentialInput = Read-Host 'Temporary LLM API key' -AsSecureString
$env:RAG_LLM_API_KEY = [System.Net.NetworkCredential]::new('', $credentialInput).Password
try {
    .\.venv\Scripts\python.exe -m uvicorn legal_rag.api.app:app --host 127.0.0.1 --port 8000 --workers 1
} finally {
    Remove-Item Env:RAG_LLM_API_KEY -ErrorAction SilentlyContinue
    Remove-Variable credentialInput -ErrorAction SilentlyContinue
}
```

Do not log environment contents. Do not commit credentials, local `.env`, traces
or review dumps. Rotate any credential previously shared in conversation before
handoff. Stop the server cleanly with Ctrl+C. Do not use `--reload` for measurements.

- Frontend: `http://127.0.0.1:8000/`
- Readiness: `GET http://127.0.0.1:8000/api/v1/health`
- Answers: `POST http://127.0.0.1:8000/api/v1/answers`
- OpenAPI UI: `http://127.0.0.1:8000/docs`

Lifespan creates one pipeline, client and controller per worker. Health returns
`{"status":"ready"}` after startup; it does not make a provider call or prove
that the credential is valid. The process needs write access to the trace folder.

## Contract and timing

Request: `{"query":"Nội dung câu hỏi pháp lý"}`. Whitespace is trimmed; empty
queries and unknown fields are rejected with HTTP 422.

HTTP 200 includes `run_id`, `answer`, `status`, `citations`, `rag_latency_ms`,
and `trace_id`. Status is one of `success`, `insufficient_evidence`,
`incomplete_answer`, `citation_check_failed`; HTTP 200 alone is not a guarantee
of adequate legal evidence. Citations include `evidence_id`, `chunk_id`, and
nullable `document_title`, `document_number`, `article`, `clause`, `point`,
`source_url`. The UI displays only supplied source links and nonempty metadata.

Execution failures handled by the adapter return HTTP 500 with a generic detail
and correlation IDs; inspect the local trace, not a browser exception dump.
`trace_id` identifies a file under `experiments/runs/generation/traces/` and is
not a public trace-download URL. Traces may include questions, answers and error
details: review/redact before sharing.

`rag_latency_ms` measures controller execution only. In the browser, HTTP
end-to-end timing starts immediately before `fetch`, so it includes request
serialization performed for that call, transport, possible queuing, trace
persistence, response transfer and JSON decoding. In the benchmark script, the
request body is serialized first and timing starts immediately before opening
the HTTP request, so request-body serialization is excluded. Both measurements
exclude model startup and post-decoding browser rendering. Their difference
from `rag_latency_ms` is not pure network latency. Startup must be measured
separately.

## Tests and benchmark

```powershell
.\.venv\Scripts\python.exe -m pytest tests/api tests/retrieval tests/agentic -q -p no:cacheprovider
.\.venv\Scripts\python.exe -m pytest -q -p no:cacheprovider --basetemp tmp/pytest-handoff-local
.\.venv\Scripts\python.exe -m pip check
git diff --check
```

Choose a fresh, disposable `--basetemp` path: pytest clears its contents.
API tests inject fake clients/controllers/services and do not load weights or
call a real provider. The real offline pipeline load above is a separate check.

After readiness, an optional real-provider benchmark is:

```powershell
.\.venv\Scripts\python.exe tools/research/api/benchmark_e2e.py --query "Nội dung câu hỏi pháp lý" --warmup 1 --runs 5
```

Keep the same process and query throughout; do not include startup in samples.
The script saves run/trace IDs, HTTP/Agentic status, RAG and HTTP timing, summary
statistics and available CPU metadata under `experiments/runs/api-benchmark/`.
It does not automatically include LLM/retrieval counts or citation validity:
join the corresponding traces to inspect those. Record torch version, device
and missing physical-core information separately. Warm-up responses are
discarded. A request exception aborts the script before its final output write;
it is not a fault-tolerant benchmark collector. With five samples its nearest-rank
p95 is the maximum, not a reliable population estimate.

## Handoff verification and limitations

- Earlier real HTTP and browser-originated smoke tests passed, including answer,
  status, citations, trace correlation and both latency displays.
- Earlier 1 warm-up + 5 measured requests all returned HTTP 200 / success with
  valid citations. Observed HTTP mean was 47.84 s, median 25.88 s, range
  24.88–103.32 s. These are a small local baseline, not a service SLA.
- Final targeted API/retrieval/Agentic suite: 37 passed. Final full suite:
  106 passed, 1 failed. The failing ingestion test constructs a ZIP containing
  only `word/document.xml`; python-docx requires `[Content_Types].xml`. Windows
  cleanup can additionally report a locked-file error. The test and extractor
  are unchanged from HEAD; no core workaround was applied.
- Two dependency deprecation warnings remain. A first full-suite attempt also
  encountered sandbox permissions in the system temp folder; a repo-local
  disposable pytest base directory removes those five setup errors.
- `pip check` passed; final diff/secret audit results are recorded in the
  handoff response. No new real LLM request or benchmark was needed for these
  documentation/cache-only changes.
- No authentication, public-deployment hardening, concurrency control or new
  performance optimization was added. Demonstrate locally with one worker.

Commit source/API/static files, API tests, benchmark utility, dependency manifests,
README, this document, `.env.example` and `.gitignore`. Do not commit `.venv`,
`.cache`, `tmp`, local review dumps, generated benchmark/traces or credentials.
The frozen corpus/index/reference assets already tracked by Git remain intact.
