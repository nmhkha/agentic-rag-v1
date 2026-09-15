# M3 generation and shared-runtime migration

## Scope and mapping

M3 migrates reusable generation behavior and Standard RAG orchestration. It
does not migrate Agentic RAG or evaluation.

| Legacy source | Package target | Status |
| --- | --- | --- |
| `scripts/llm_client.py` | `src/legal_rag/llm_client.py` | `LEGACY_PENDING_REMOVAL` |
| `scripts/evidence_formatter.py` | `generation/evidence.py` | `LEGACY_PENDING_REMOVAL` |
| `scripts/response_formatter.py` | `generation/formatter.py` | `LEGACY_PENDING_REMOVAL` |
| `scripts/citation_validator.py` | `generation/verifier.py` | `LEGACY_PENDING_REMOVAL` |
| `scripts/rag_baseline.py` | `generation/prompts.py`, `answerer.py`, `standard.py` | `LEGACY_PENDING_REMOVAL` |

The prompt remains unchanged at `prompts/legal_rag_v0.txt`. The legacy files
remain unchanged and present.

## Module responsibilities and public API

- `prompts.py`: reads prompt text exactly and performs the legacy ordered
  `{query}` then `{evidence_context}` replacements.
- `evidence.py`: formats ordered M2 `Evidence` objects and builds the citation
  map. Missing values are omitted exactly as before.
- `answerer.py`: builds the prompt and delegates one string to an injected
  `LLMClient`; it performs no retrieval or citation rewriting.
- `formatter.py`: parses the model JSON/fenced or embedded JSON fallback and
  renders the final answer/source text.
- `verifier.py`: extracts strict `[E<number>]` citations and reports unknown,
  malformed, and declared-ID mismatches without correction.
- `standard.py`: orchestrates M2 retrieval, evidence formatting, generation,
  parsing, and verification; it also retains trace construction/writing.
- `legal_rag.llm_client`: defines the generation protocol and exact
  OpenAI-compatible HTTP implementation.

Stable symbols are exported from `legal_rag.generation`: `load_prompt`,
`build_prompt`, `format_evidence`, `generate_answer`, `parse_model_output`,
`format_final_response`, `CitationValidation`, `validate_citations`, `run_rag`,
`make_trace`, and `write_trace`. `LLMClient`, `OpenAICompatibleClient`, and
`client_from_env` are available from `legal_rag.llm_client`.

## Prompt and evidence contracts

The prompt file is decoded as UTF-8 without normalization, rewriting, or added
instructions. Legacy Standard RAG sends the complete constructed prompt as one
user prompt; the shared client wraps it as exactly one `messages` entry.

Evidence remains numbered in input order. Each block starts with `[E#]`, emits
available document title/number, Article/Clause/Point labels and official URL,
then a blank line, `Nội dung:`, and the chunk's `text`. Blocks are separated by
two newlines. The citation map retains only `chunk_id`, document number,
Article, Clause, Point, and official source URL.

## Citation and response contracts

Only case-sensitive citations matching `\[E([1-9][0-9]*)\]` are accepted.
Unknown citations and bracketed E-like malformed tokens are errors. Repeating a
valid evidence citation is permitted and deduplicated in first-seen order.
When supplied, `used_evidence_ids` must have the same set as citations in the
answer. No correction or revision occurs in this layer.

Model output must resolve to a JSON object containing string `answer`; fenced
JSON and a single embedded object retain the legacy fallbacks. Evidence and
missing-information fields retain their list validation and defaults. Final
serialization retains the existing Vietnamese source heading and official URL
lines.

## LLM configuration and request behavior

The client reads `RAG_LLM_MODEL`, `RAG_LLM_BASE_URL`, and `RAG_LLM_API_KEY`
lazily in `client_from_env`; all three are required and have no code default.
It does not load `.env` or make a request on import. `RAG_LLM_PROVIDER` is used
by Standard RAG trace metadata with default `openai-compatible` but does not
alter client selection.

The working configuration names `gemini-3.5-flash-lite`, confirming the
historical model. The example configuration still names an older model and is
not treated as the runtime default. The base URL is stripped of a trailing
slash and `/chat/completions` is appended unless already present. Requests keep
one user message, temperature 0, JSON-object response format, bearer auth,
UTF-8 JSON, and the 120-second default timeout. HTTP error bodies remain capped
at 500 decoded characters. API keys are neither logged nor included in traces.

## Standard RAG flow and CLI

`run_rag` performs:

```text
query -> M2 RetrievalPipeline Top-5 -> format_evidence -> build_prompt
      -> injected LLMClient.generate -> parse_model_output
      -> validate_citations -> run dictionary
```

`scripts/run_standard_rag.py` is a thin CLI that constructs the existing M2
pipeline/client, delegates to `run_rag`, optionally prints evidence, validates
citations, and formats the final response. It contains no retrieval or
generation algorithm.

## Tests and deterministic equivalence

Twelve new offline tests cover exact prompt loading/replacement; evidence order,
separators and missing metadata; model-output parsing errors/fallbacks; final
serialization; all established citation cases plus malformed forms; answerer
injection; Standard RAG output and deterministic trace fields; environment
resolution; endpoint/body/header/timeout construction; and response extraction.
The HTTP call is replaced with an in-memory fake.

All 31 historical queries were paired with their frozen M2 Top-5 IDs. For each
query, legacy and packaged code received the same evidence and deterministic
fake model response:

| Comparison | Result |
| --- | --- |
| Evidence text and citation map | 31/31 byte/value exact |
| Constructed prompt and client input | 31/31 exact |
| Evidence IDs/order and complete `run_rag` dictionary | 31/31 exact |
| Final response serialization | 31/31 exact |
| Deterministic trace/config fields (timestamp excluded) | 31/31 exact |
| Citation validation fixtures | exact |

Temporary comparison details remain under `/tmp/legal-rag-m2/`. No Gemini/API
call, network request, model download, real generation benchmark, or official
evaluation write occurred.

M2 retrieval tests remain 10/10 and M1 ingestion tests remain 9/9. All M2
retrieval file hashes and the Agentic v1 hash were captured before M3 and
verified unchanged afterward.

## Deferred work

Agentic controller/state/nodes and all evaluation/benchmark migration remain
deferred. M4 can reuse the prompt, evidence, answerer, formatter, verifier,
client, and M2 pipeline APIs without copying their logic.
