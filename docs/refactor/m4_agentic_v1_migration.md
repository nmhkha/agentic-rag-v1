# M4 Agentic RAG v1 migration

## Scope and mapping

M4 is a structural migration of `scripts/agentic_rag.py` into
`src/legal_rag/agentic/v1`. The legacy script remains byte-identical and is
`LEGACY_PENDING_REMOVAL`.

| Legacy responsibility | Package module |
| --- | --- |
| Runtime data classes | `state.py` |
| Frozen budgets and transition predicates | `policies.py` |
| Agent prompts, response parsing, retrieval/check/generate/revise/validate operations | `nodes.py` |
| State-machine orchestration | `controller.py` |
| Trace schema, model guard, execution errors, persistence | `trace.py` |
| CLI construction/output | `scripts/run_agentic_rag.py` |

No Agentic v2 concept, evaluation logic, gold-label access, retrieval
implementation, generation helper copy, new retry, or research behavior was
introduced.

## State model

`AgentState` preserves the legacy query, initial/current/expansion evidence,
retrieval round, coverage result, missing aspects, subqueries, draft/final
answer, completeness result, citation result, revision counters, candidate
IDs, retrieval and LLM call metadata, mechanism-use booleans, run ID,
execution error, final status, and ordered transitions. `CoverageCheck`,
`CompletenessCheck`, and `CitationCheck` retain their exact fields and defaults.

No v2 Aspect Ledger, applicability ledger, answer-worthiness, or goal state is
present.

## Controller flow

```text
initialized
  -> initial_retrieval (BM25@20 + Dense@20 union -> BGE; Top-5 context)
  -> coverage_check
       -> [if allowed and missing] expansion_retrieval_1..3
          -> cross-query dedup -> evidence_merge_rerank -> Top-5
  -> answer_generation
  -> completeness_check
       -> [if incomplete and allowed] answer_revision -> completeness_check
  -> citation_check
       -> [if invalid and allowed] citation_revision -> citation_recheck
       -> [if deterministic low-overlap gate requires] semantic_citation_alignment
          -> [optional in-call corrected payload] citation_recheck
  -> final:success | final:insufficient_evidence
     | final:incomplete_answer | final:citation_check_failed
```

Execution exceptions are recorded separately as `final:execution_error` by the
CLI boundary, matching the legacy audit behavior.

## Nodes and shared-runtime reuse

Node functions accept explicit state, pipeline, transition callback, and/or LLM
call callback. They perform one responsibility: retrieval and audit recording,
coverage check, answer generation, completeness check, answer revision,
deterministic citation validation, or citation revision. The controller alone
chooses transitions.

Retrieval uses M2 `RetrievalPipeline.retrieve_with_audit` with
`all_candidates=True`, preserving BM25@20 + Dense@20 union/dedup, BGE reranking,
and Top-5 entry into LLM context. Expansion subqueries remain
`f"{missing_aspect} {original_query}"`, at most three, for one expansion round.
Expansion evidence is insertion-order deduplicated, assigned execution-wide
evidence IDs, pooled with initial evidence, and reranked through the same M2
reranker. RRF is not used.

Formatting, the Standard answer prompt, output parsing, and citation validation
use M3 modules. Agentic-only coverage, completeness, answer-revision,
citation-revision, and semantic-alignment prompts remain in `nodes.py` with
byte-identical construction. The LLM client is injected; imports do not create
a client, load retrieval models, or call an API.

## Frozen policies and budgets

The legacy source values match the M4 specification:

```text
MAX_SUB_QUERIES = 3
MAX_RETRIEVAL_EXPANSIONS = 1
MAX_ANSWER_REVISIONS = 1
MAX_CITATION_REVISIONS = 1
MAX_LLM_CALLS = 6
```

Explicit helpers preserve the original expansion, answer-revision,
citation-revision, LLM-budget, and final-status boolean chains. Tests enumerate
all finite input combinations: expansion/revision predicates, call counts 0–8,
and all 32 final-status boolean combinations.

The deterministic lexical citation-alignment gate and optional single semantic
alignment call are historical v1 behavior. They were retained exactly and are
not an Agentic v2 addition.

## Trace contract

`trace_for_state` retains field names and order for run/query metadata,
retrieval configuration, prompt/model/provider, candidate counts and IDs,
coverage, expansion, final evidence, draft/completeness/revisions, citations,
final answer/status, retrieval and LLM calls, budgets, full serialized state,
and timestamp. No field was renamed. Exact comparisons omit only timestamp
values.

## Offline tests and equivalence

Twenty M4 tests cover state serialization, citation adaptation, exhaustive
policy tables, exact Agentic prompt construction, parsing/fallbacks, lexical
alignment routing, all explicit nodes through the controller, trace schema and
writing, execution error capture, and the required controller paths:

- straight-through success;
- bounded evidence expansion and merge;
- one answer revision;
- one citation revision;
- combined expansion + both revisions at six LLM calls;
- insufficient and incomplete termination;
- LLM-budget rejection;
- malformed controller JSON;
- empty/malformed revision output.

The scripted fake records `call_index`, complete prompt, and returned response.
Reachable branch scenarios were run through both legacy and packaged
controllers with identical pipeline/client instances and matched state,
prompts, call sequence, transitions, statuses, and deterministic traces.

For all 31 historical queries, the harness reconstructed the frozen initial
Top-5 `Evidence` objects from the stored in-repository v1 traces. Both
controllers received identical evidence/audit metadata and scripted decisions.
Every query matched on:

- initial evidence IDs/order;
- LLM call count, stages, prompts, and responses;
- transition sequence;
- expansion, answer-revision, and citation-revision behavior;
- final status and complete serialized state;
- deterministic trace fields (timestamp excluded).

Result: **31/31 controller-equivalent**. No real retrieval model or LLM was
loaded, no API/network call occurred, and no benchmark was rerun.

Regression results are M3 12/12, M2 10/10, and M1 9/9.

## Stored historical sanity check

The 31 stored files (moved in M6 to `experiments/traces/agentic-rag-v1/agentic-v1`) report:

| Measure | Stored result | Expected reference |
| --- | ---: | ---: |
| Expansion used | 6/31 | 6/31 |
| Answer revision used | 7/31 | 7/31 |
| Citation revision used | 1/31 | 1/31 |
| Success | 28 | 28 |
| Insufficient evidence | 2 | 2 |
| Incomplete answer | 1 | 1 |

There is no discrepancy.

## CLI and limitations

`scripts/run_agentic_rag.py` only parses the legacy useful flags, constructs
the M2 pipeline and M3 environment client, runs the packaged controller,
formats output, and writes/shows the unchanged trace schema. The expected model
guard remains `gemini-3.5-flash-lite`.

As in M2, loading dense and reranker models together may exceed memory on this
machine. M4 controller tests therefore use deterministic fake retrieval and do
not eagerly construct either model. Production construction remains lazy at
the CLI/runtime boundary.
