# Phase 5B.2-E-R1 — Evaluator quota-recovery amendment v0

Status: **FROZEN when the companion manifest is created and independently verified.**
Recovery protocol version: **`phase5b2e-quota-recovery-v1`**.

This amendment implements transport recovery, offline eligibility verification,
synthetic testing and a future execution contract. Phase 5B.2-E-R1 makes **zero
network/API, production, retrieval or real semantic evaluation calls**. It does
not run paired analysis, bootstrap, quality interpretation or Phase 5C. No actual
recovery ledger or recovery request is created during this phase. Execution of
Phase 5B.2-E-R2 requires later external review and authorization.

## 1. Immutable evidence and trust anchors

All 93 production outputs remain sealed and error-free. All preexisting project
artifacts covered by the initial snapshot remain byte-identical, including the
64 accepted v0 judgments, 165 evaluator attempts, request/response slots, errors,
93 evaluation envelopes, incomplete report and available-case diagnostics.

The existing durable production recovery manifest is anchored to:

`60f2c25b82082e41d466439afa0d93106484ca8fb4cdd41bbdb35cd1f83282bc`

The final Phase 5B.2-E v0 provenance manifest is anchored to:

`073e6a5ed1b1759d11afce596dce7af4bf6dec5390f693a089a354e2be9ca53c`

The unchanged independent production recovery verifier checks all three original
and supplemental seals, durable file hashes, ledger/trace/observer reconciliation,
query identities, historical artifacts and pinned runtime/model assets. Original
v0 production seals retain their historical `FAILED_EPHEMERAL_LIFECYCLE` status;
they are neither repaired nor replaced. Original semantic v0 attempt budgets also
remain exhausted; v1 is a separate protocol and namespace.

The amendment manifest records all original evaluation artifact hashes, all 93
production output hashes, source/gold hashes and the complete before/after project
inventory. A new external SHA-256 for the amendment manifest is printed at freeze.

## 2. Exact eligibility and completed locks

The trusted offline projector checks completion and transport state only. It
verifies v0 record/envelope equality, attempt order/counts, absence of replay,
request-prompt bindings, response receipts, production hashes and exact query
text. Existing accepted judgments are protected by the anchored v0 artifact
inventory; they are not semantically reevaluated.

Any slot with an existing judgment or a completed/accepted v0 state must have
consistent completion evidence. If inconsistent, verification fails; the slot is
never reclassified as recoverable. All 64 accepted slots remain permanently locked.

Only an absent judgment with `evaluation_status=FAILED`, exactly three exhausted
v0 attempts, no production error, and three transport/provider failures explicitly
identified as HTTP 429 / provider code 429 / `RESOURCE_EXHAUSTED` is eligible.
Parser errors, non-429 failures, unknown errors, mismatched hashes, changed query
bindings or any disagreement with the expected slot list cause FAIL/STOP.

| Variant | Locked v0 judgments | Eligible | v0 attempts (unchanged) |
|---|---:|---:|---:|
| R2 — full-agentic-replication | 23 | 8 | 53 |
| A1 — agentic-v1-no-answer-revision | 22 | 9 | 56 |
| A2 — agentic-v1-no-evidence-expansion | 19 | 12 | 56 |
| Total | 64 | 29 | 165 |

The report's completion counts and exact failed IDs are cross-checked against
the actual record/attempt/response files. Its quality values are not inputs to
eligibility. The fixed recovery order is:

| Alias | Variant ID | Query ID |
|---|---|---|
| R2 | full-agentic-replication | eval021 |
| R2 | full-agentic-replication | eval022 |
| R2 | full-agentic-replication | eval023 |
| R2 | full-agentic-replication | eval024 |
| R2 | full-agentic-replication | eval025 |
| R2 | full-agentic-replication | eval026 |
| R2 | full-agentic-replication | eval027 |
| R2 | full-agentic-replication | eval028 |
| A1 | agentic-v1-no-answer-revision | eval014 |
| A1 | agentic-v1-no-answer-revision | eval016 |
| A1 | agentic-v1-no-answer-revision | eval019 |
| A1 | agentic-v1-no-answer-revision | eval020 |
| A1 | agentic-v1-no-answer-revision | eval022 |
| A1 | agentic-v1-no-answer-revision | eval023 |
| A1 | agentic-v1-no-answer-revision | eval024 |
| A1 | agentic-v1-no-answer-revision | eval025 |
| A1 | agentic-v1-no-answer-revision | eval026 |
| A2 | agentic-v1-no-evidence-expansion | eval015 |
| A2 | agentic-v1-no-evidence-expansion | eval016 |
| A2 | agentic-v1-no-evidence-expansion | eval017 |
| A2 | agentic-v1-no-evidence-expansion | eval018 |
| A2 | agentic-v1-no-evidence-expansion | eval019 |
| A2 | agentic-v1-no-evidence-expansion | eval020 |
| A2 | agentic-v1-no-evidence-expansion | eval022 |
| A2 | agentic-v1-no-evidence-expansion | eval023 |
| A2 | agentic-v1-no-evidence-expansion | eval024 |
| A2 | agentic-v1-no-evidence-expansion | eval025 |
| A2 | agentic-v1-no-evidence-expansion | eval026 |
| A2 | agentic-v1-no-evidence-expansion | eval027 |

The list is derived from completion evidence in original query order, then
required to equal the expected list. No metric, point count or intervention flag
changes membership or ordering.

## 3. Stored 429 evidence and limits

The v0 attempt ledger retains the frozen client's HTTP error text, truncated to
500 response-body characters. Its response slot retains only `status=error` and
`type=RuntimeError`. The error text includes HTTP 429, provider code 429,
`RESOURCE_EXHAUSTED`, the metric
`generativelanguage.googleapis.com/generate_content_free_tier_requests`, reported
limit 15, the model name, and explicit `Please retry in ...s.` messages.

V0 did **not** save response headers, complete structured RetryInfo, quota ID or
structured quota dimensions. Those fields remain explicitly unavailable. The
projector extracts only complete fields actually retained in the truncated body;
it does not reconstruct missing response metadata. The manifest preserves an
evidence entry for each stored transport error, including source ledger, variant,
query, v0 attempt index, error-text hash and available fields.

The reported limit does **not** establish a requests-per-minute/day window.
There is no inferred quota window, global fixed pacing interval or rate limit.
Historical retry delays remain historical evidence; they are not reused as a new
session's minimum inter-request interval.

## 4. Frozen transport policy

`MAX_RECOVERY_ATTEMPTS_PER_ELIGIBLE_SLOT = 3`, separate from the three v0 attempts.
Attempt indices 1–3 in the new namespace persist across restarts. Attempt 4 is
rejected. The first valid parsed judgment permanently stops provider requests for
that slot. Valid v0 slots cannot reserve an attempt, enter the recovery adapter,
or reach the provider.

Each HTTP 429 ends the entire recovery session immediately with `QUOTA_BLOCKED`.
No next request, including one for a different slot, occurs in that invocation.
If an explicit reliable delay is supplied, a durable global not-before deadline
is saved. A later resume cannot request before that deadline. This schedules
recovery without a blocking sleep or an automatic retry loop.

Reliable evidence is restricted to:

1. A positive, finite structured `google.rpc.RetryInfo.retryDelay` duration.
2. A positive `Retry-After` delta or a valid timezone-aware HTTP date. An available
   response `Date` supplies the server-relative interval; otherwise receipt time
   is the reference.
3. An exact positive, finite `Please retry in N[.fraction]s.` provider message.

If multiple reliable delays exist, honor their maximum. The persisted deadline
uses local receipt handling time, conservatively after response arrival, and is
rounded upward. Zero, negative, nonfinite, malformed or absent delay information
does not authorize an immediate retry.

Without a reliable delay, persist `QUOTA_BLOCKED` with no inferred deadline.
Automatic resume remains blocked, regardless of elapsed time. A later externally
reviewed session may supply a nonempty review reference bound to the exact
quota-stop record SHA-256; this authorization is a new append-only record. It
does not change eligibility, response labels, attempt counts or v0 evidence.
This amendment does not itself authorize such a resume or any provider request.

Other transport failures end the session after consuming only the reserved
attempt; a later authorized resume retains the remaining budget. A frozen parser
failure can consume the next separate v1 attempt, up to three. A started request
with no durable response is ambiguous: its reservation remains consumed and
automatic resubmission is blocked. It is never treated as an unused attempt.

## 5. Unchanged semantic adapter

The original `evaluate_record`, `judge_prompt`, `parse_judge`, `point_audit`,
`citation_validator.validate_citations` and their source files remain unchanged.
Gold, required points, query text, production answer and evidence remain bound to
their original hashes. The model remains `gemini-3.5-flash-lite`, temperature 0,
the exact endpoint hash, JSON-object response format, one user message and
120-second timeout. No decoding/prompt/scoring/model substitution is permitted.

The quota transport emits the same URL, request body bytes, headers, method and
timeout as the frozen client for identical inputs. Recovery metadata is stored
outside the request payload. The transport performs one submission and retains
structured error metadata; it has no hidden retries. It validates model, endpoint
and timeout both at construction and before each submission.

For each reserved attempt, the trusted adapter invokes the unchanged evaluator
with a one-response client. Returned text is passed unchanged to the frozen
parser. The adapter audits parse validity using that same parser; it introduces
no new semantic checker or rubric. If the evaluator asks for another response
after a failure, an infrastructure-only `BaseException` boundary exits its
immediate retry loop and returns control to the recovery scheduler. Provider
errors use the same boundary before any further request. Successful scoring is
the original `evaluate_record` result, with no label repair or manual override.

The inner evaluator's `evaluation_attempts` field describes its local invocation;
the authoritative cross-session v1 attempt count is the durable
`recovery_attempt_index`. Original v0 counters are copied as provenance and never
reset, added into v1 counters, or overwritten.

## 6. Append-only recovery ledger and crash behavior

Future execution uses only the new directory:

`data/evaluation/generation/phase5/phase5b2er2_v1/`

It remains absent after Phase 5B.2-E-R1. The immutable amendment manifest declares
all 29 initial recovery states as `NOT_STARTED`.

```text
phase5b2er2_v1/
  protocol_binding.json
  session.lock
  quota_stop_0001.json
  quota_stop_0001_resume_authorization.json  # only if separately authorized
  <alias>/<query_id>/<recovery_attempt_index>/
    started.json
    wire_response.json
    evaluation_record.json                 # successful result only
    receipt.json
```

Numbered, exclusively created and fsynced JSON records form an append-only
journal. No existing request, response, receipt or result is rewritten. The
mutable advisory lock contains no evaluation evidence. A bound ledger rejects an
altered plan, added slots, counter gaps, index 4, unsafe paths, symlinks and a new
reservation while the previous request remains unresolved. A global nonblocking
file lock prevents simultaneous recovery schedulers.

`started.json` records variant ID, query ID, production hash, gold/query binding,
v0 evaluation status/count, v1 attempt index, start time and `STARTED` status.
The response record binds raw returned text or transport metadata to the exact
start-record hash and prompt hash. Receipts record transport and HTTP status,
quota metadata, response hash, parse status, end time, result hash, final attempt
status and slot status after the attempt. Three failed attempts yield
`RECOVERY_EXHAUSTED`; a third 429 also retains its session-level `QUOTA_BLOCKED`
event. Remaining untouched slots stay `NOT_STARTED`.

On resume, a persisted response is replayed through the same frozen parser without
a provider call. A valid result/receipt protects the slot forever. Result and
response hashes are rechecked. A crash between a 429 receipt and the global stop
record causes the stop record to be reconstructed conservatively before any
request. A crash before a response is durable remains ambiguous and cannot trigger
automatic resubmission. A valid parsed response that cannot be finalized requires
offline finalization; it cannot trigger another judge request.

Only allowlisted HTTP response headers (`Retry-After`, `Date`) are read for quota
handling. API keys, Authorization headers and arbitrary transport exception text
are not written to the ledger. Provider messages are redacted against the active
key; raw HTTP response hashes are retained without storing credentials.

## 7. Quality-blind scheduling boundary

The trusted projector may read gold and existing evaluation envelopes to establish
immutable query/transport/completion bindings. It does not compute or inspect
quality scores for recovery decisions. The scheduler receives a strict schema
containing only identifiers, completion states, attempt counts and hashes.
Unexpected fields, including metrics, are rejected.

Scheduler filesystem operations run under the existing Python read allowlist,
restricted to the new recovery ledger. It cannot read metric files, v0 diagnostics,
contrasts, bootstrap outputs or trigger-quality artifacts. The trusted input
verifier and evaluator run outside that scheduling scope and return only
completion/transport receipts; scoring fields are rejected in scheduler receipts.
This is an auditable component and Python filesystem boundary, not a claim of
protection against hostile native code or arbitrary replacement of the trusted
worker. The future reviewed-session factory verifies the external manifest anchor
and requires the frozen quota transport with explicit real-request authorization.

## 8. Offline tests and validation

The additive test suite covers Q1–Q15 from the request and further durability
controls:

- Q1–Q3: all 64 valid v0 slots issue zero calls; exactly 29 failed 429 slots are
  eligible; first valid recovery response stops further attempts.
- Q4–Q7: explicit retry deadlines, whole-session stop without a reliable delay,
  restart-persistent counters, and rejection of attempt 4.
- Q8–Q11: changed production rejection, non-429 rejection, exact frozen order,
  and inability of quality files or added metric fields to influence scheduling.
- Q12–Q15: request byte equivalence, unchanged returned text at the frozen parser,
  protected v0/accepted result files and byte-identical original evidence.
- Q16–Q20: crash-safe global quota barriers, ambiguous-request blocking, replay of
  saved valid responses without a call, explicit delay extraction, and review-bound
  resume for unknown delays.
- Q21–Q26: credential omission, blocked sockets/live transport, endpoint/model
  rejection, frozen-parser failure handling, ledger binding/path validation and
  HTTP-date handling.
- Q27–Q30: exact trusted gold/query/production binding, transport-setting drift
  before submission, direct adapter rejection of completed v0 slots, and rejection
  of added slots or skipped unresolved reservations.
- Q31: an existing unbound resume-authorization file cannot release a quota stop.

All network audit events are blocked. A deliberate socket-creation negative test
must be rejected before networking; blocked attempts are reported separately from
zero actual network/API calls. Evaluator adapter exercises use synthetic inputs
and mocked responses only. No `evaluate_record` invocation on real benchmark data,
new Gemini request, retrieval, production controller call or bootstrap occurs.

Commands for offline validation and freezing:

```sh
python3 -B tests/test_phase5_evaluation_quota_recovery.py
python3 -B scripts/phase5_evaluation_quota_recovery_v1.py freeze \
  --before-snapshot /tmp/phase5b2er1-before.json \
  --test-results /tmp/phase5b2er1-tests.json
python3 -B scripts/phase5_evaluation_quota_recovery_v1.py verify \
  --manifest-sha256 <externally-reviewed-manifest-sha256>
```

The CLI exposes only `freeze` and `verify` and installs a network-denial audit
guard. The future session factory is library-only and is not invoked in this
phase. The test report is bound to the exact infrastructure/test source hashes.

## 9. Freeze and stop

PASS requires 64 completed locks, exactly 29 eligible slots in the declared order,
unchanged evaluator/model/prompt/gold/production, separate three-attempt v1 budgets,
passing quota/resume/quality-isolation tests, zero actual network/production/judge
calls, and unchanged historical artifacts. The manifest and integrity report
record these conditions and the hashes of every additive amendment artifact.

Ready for Phase 5B.2-E-R2 means **ready for external review**, not permission to
execute recovery. After freezing and independent verification: **STOP**. Do not
judge any remaining slot, revise v0 diagnostics, run bootstrap or calculate final
R1/R2/A1/A2 comparisons.
