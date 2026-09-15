# Phase 5C.2 — Agentic v2 behavioral and controller requirements

Artifact status: **DRAFT FOR EXTERNAL REVIEW**. Scope: **READ-ONLY DESIGN ANALYSIS**. Implementation status: **NOT_STARTED**. These are proposed contracts, not implemented behavior, approved implementation, or empirical findings.

## 1. Decision and evidence boundary

Research/design justified = **YES**. Agentic v2 implementation authorization = **NOT YET**. A separate challenge set is justified for independent investigation; its construction requires a later reviewed phase. Frozen Answer Revision = **Insufficient evidence**; frozen Evidence Expansion = **Insufficient evidence**. Neither label changes here.

**31-query / 102-point benchmark remains the primary HISTORICAL COMPARABILITY BENCHMARK.** Its R0/R1/R2/A1/A2 outcomes and failure analyses helped form these requirements; **the 31-query benchmark is no longer an untouched confirmatory holdout** for v2. Keep its files, gold, scoring and conclusions unchanged. Future use is historical comparison, regression and compatibility reporting. It cannot alone establish v2 generalization or causal contribution. No thresholds may be tuned on these 31 queries.

The authoritative starting point is [5C.1 synthesis](../phase5c1_v0/phase5c1_research_synthesis_v0.md), [evidence matrix](../phase5c1_v0/phase5c1_evidence_matrix_v0.json), [requirement map](../phase5c1_v0/phase5c1_problem_requirement_map_v0.json), [decision log](../phase5c1_v0/phase5c1_decision_log_v0.md), [manifest](../phase5c1_v0/phase5c1_manifest_v0.json) and [integrity](../phase5c1_v0/integrity_before_after_v0.json). Phase 5A interpretation and final 5B.2-F complete 93/93 analysis remain historical authority. Tier A means controlled/frozen evidence, not automatic causality; B means observational traces; C means exploratory diagnostic only.

| Requirement | Findings / tiers | Retained decision | What the evidence permits |
| --- | --- | --- | --- |
| V2-R1 Completeness-aware Answer Revision | F2, F5 / A | INVESTIGATE_BEFORE_IMPLEMENTATION | Investigate supported omissions and revision recovery; nine frozen generation-omission points exist, but revision contribution is insufficiently attributed. |
| V2-R2 Evidence-aware completeness verification | F8 / B | REFINE | Refine the behavioral specification: internal complete and benchmark complete differed in 17 cases; this is not a confirmed software defect. |
| V2-R3 Missing-aspect carry-through / goal persistence | F9 / C | INVESTIGATE_BEFORE_IMPLEMENTATION | Candidate Aspect Ledger only; one diagnostic does not establish a general failure or authorize an intervention. |
| V2-R4 Selective, higher-value expansion | F1, F6, F7 / A, B | INVESTIGATE_BEFORE_IMPLEMENTATION | Study useful coverage per cost; aggregate macro tie, net +1 point and overhead do not justify deleting expansion. |
| V2-R5 Independent challenge benchmark | F1, F2, F4, F7, F8, F9 / A, B, C | INVESTIGATE_BEFORE_IMPLEMENTATION | Design broader evaluation coverage. F9 motivates a dimension only; no claim that the old set is uniformly easy. |
| V2-R6 Historical comparability and stochastic safeguards | F3, F4, F5, F6 / A | KEEP_AS_IS | Preserve provenance, paired transitions, all-run reporting and attribution limits. This is a research safeguard, not a new runtime mechanism. |

F3's historical improvement must be read beside F4's R1→R2 variation. F5's descriptive signal and F6's weak aggregate signal retain all safety and stochastic caveats. F7 usage measures exposure, not effectiveness. F8 calibration (Tier B) and F9 carry-through (Tier C) must never be collapsed into one confirmed problem.

## 2. Runtime vocabulary and boundaries

Runtime may use the original query, corpus, retrieved evidence, retriever/reranker, runtime prompts/config and its own stage outputs. It must not use required legal points/aspects from gold, supporting-evidence gold labels, reference answers, evaluator labels, difficulty/dimension labels or TEST quality outputs. Runtime aspect IDs are locally generated opaque IDs; they are never gold point IDs. An evaluator can map them to gold only after production outputs are sealed.

Separate four questions: (a) what the user asks; (b) what available evidence supports under applicable conditions; (c) what the answer actually asserts; (d) what remains unknown. A retrieved chunk may be relevant without being applicable or answer-worthy. The checker must not treat plausible wording as completeness or demand that all retrieved chunks be cited.

The scope of a broad request is finite: record explicit asks plus narrowly justified candidate subaspects tied to intent. Do not imply an exhaustive catalogue of all external law. Unknown facts and corpus limits remain visible. No domain-specific medical rules, medical templates or copied diagnostic queries are proposed.

## 3. V2-R1 — Completeness-aware Answer Revision

**Candidate trigger:** a retained first completeness check identifies an omitted or incorrectly expressed answer-worthy aspect with sufficient applicable support in the final evidence snapshot; or identifies unsupported wording/overstatement or an omitted limitation that can be repaired using that snapshot. Trigger requires a specific repair target, an admissible proposed change and remaining revision/check budget. A missing aspect with no support is not permission to invent its legal answer. Citation syntax repair is separately recorded and not counted as semantic point recovery.

**Required inputs:** exact original query; immutable draft answer and answer ID; final evidence snapshot with stable citation IDs, chunk/source identity and text; first completeness payload; runtime aspect origins and promotion history if that candidate abstraction is authorized; applicability conditions; unresolved aspects; repair targets with evidence links; remaining budgets. No gold or benchmark points.

**Allowed additions:** propositions entailed by the supplied evidence and relevant to intent; qualifications preserving scope, actor and conditions; appropriate citations to supplied evidence; explicit disclosure of unresolved user requests. Conditional rules may be presented conditionally without assuming the condition holds. Correctly supported draft content should be retained unless a logged contradiction or applicability correction justifies removal.

**Forbidden additions:** external-law claims from model memory, invented duties/testing requirements, unsupported inferred aspects, unconditional application of conditional evidence, references to unavailable chunks, or a claim of exhaustiveness beyond checked scope. Revision does not silently retrieve more evidence, expand Top-K or allocate another round.

**Grounding contract:** map every new/changed legal claim to supporting spans in the exact evidence snapshot; recheck entailment and applicability, not just citation syntax. Retain claim additions/removals and source linkage for evaluator review. If evidence only partly supports a request, preserve supported content with qualifications and explicitly name the unresolved portion. If no material part can be supported, return calibrated insufficiency. A corpus search failure only establishes that runtime did not find evidence; it cannot certify corpus-wide absence.

**Success has two levels:** runtime may estimate repair completed when targets are addressed or properly disclosed and the final checks pass. Future evaluator success requires draft→final recovery of independently annotated, previously omitted supported content, no unacceptable grounding/citation deterioration, and reported cost. Pure wording changes and new citations without semantic recovery do not count as point recovery. Correct disclosure is measured separately from supported-point recovery.

**Trace:** draft and revised answers are distinct immutable versions, even if identical in bytes. Checks reference exact answer/evidence hashes. Retain the first and second completeness payloads, revision decision/reason, target aspect IDs, attempted/failed/skipped state, legal claim changes and final selection. A later citation edit creates a third version and requires checks bound to that version; stale success cannot be inherited. If remaining budget cannot validate an edited version, disclose unverified state rather than claim complete. No new call budget is implied.

Before implementation: external review of trigger/repair boundaries and annotation rubric; independently constructed DEV cases demonstrating supported omissions and negative controls where repair must abstain; feasible budget and isolation design. Before adoption: repeated, mechanism-localized recovery plus safety/cost gates in the evaluation protocol. Current decision remains INVESTIGATE_BEFORE_IMPLEMENTATION.

## 4. V2-R2 — Evidence-aware completeness verification

**REFINE is the research decision, not implementation authorization.** The checker produces separate fields for query scope, supported/applicable evidence, answer coverage, missing supported content, missing evidence, unresolved conditions, unsupported answer claims and disclosure coverage. Its labels are runtime estimates, not evaluator-certified answers.

Conceptual inputs are query + evidence snapshot + answer version (absent for pre-answer coverage) + retained runtime aspect history. For each considered aspect, record query alignment, origin, evidence links, applicability, sufficiency, answer spans and disposition. Pre-answer coverage asks whether available evidence can support the scoped request; post-answer completeness asks whether the answer faithfully uses that evidence and acknowledges unresolved asks. Evidence insufficiency and generation omission can coexist.

Relevant evidence ≠ required evidence. A contextual chunk or a rule for a different actor does not create an answer obligation. The checker need not cite every chunk; it must justify why an answer-worthy supported aspect is missing, why an explicit ask remains unresolved, or why a candidate is excluded. Silence about an irrelevant retrieved chunk is correct.

For broad queries the checker records its bounded scope and uncertainty. For partial evidence it cannot set complete merely because everything already written sounds correct. Conversely, it must not mark a fully supported concise answer incomplete merely because unrelated material was retrieved. Preserve false-positive and false-negative cases for evaluator-side calibration.

Before implementation: reviewer agreement on bounded scope, omission versus absence and status semantics, plus independent DEV evidence of both mismatch directions. Adoption requires improved calibration without indiscriminate insufficiency, extra looping or grounding loss. No classifier or prompt is specified or changed here.

## 5. V2-R3 — Candidate Aspect Ledger and lifecycle

**Tier C hypothesis, unconfirmed.** The proposed linear chain IDENTIFIED→SEARCHED→SUPPORTED→PARTIALLY_SUPPORTED→NOT_SUPPORTED→NOT_APPLICABLE→ANSWERED→UNRESOLVED conflates search activity, evidence quality, legal applicability and answer disposition. They are orthogonal: sufficient and partial support are alternatives, not obligatory sequential steps. An aspect can be answered without expansion; an answered aspect can become unsupported if final evidence selection loses its sources.

Use stable aspect IDs and an append-only event history with these separate axes:

| Axis | Proposed values / semantics |
| --- | --- |
| Origin | query_explicit; controller_inferred. Preserve the query span or inference rationale and parent aspect IDs. |
| Admission | candidate; answer_worthy; excluded; merged. Explicit asks enter answer_worthy as response obligations, not as assertions of legal truth. Inferred aspects start candidate. |
| Search | not_searched; searched; search_blocked. Search results do not determine applicability or sufficiency. |
| Support | unassessed; sufficient; partial; not_found_in_available_evidence; conflicting. Runtime never promotes not_found to proved no_support_in_corpus. |
| Applicability | unassessed; direct; conditional; not_applicable; uncertain. Contextual role is stored separately. |
| Answer disposition | pending; answered_supported; answered_qualified; unresolved_disclosed; unresolved_undisclosed; excluded_with_reason; merged_into. |

**Promotion:** inferred candidate→answer_worthy only with a direct user-intent link, supporting evidence, and defensible applicability. Conditional applicability is enough only for a supported conditional statement preserving unknown conditions; it is never enough for an unconditional duty. Partial evidence may support a narrower, explicitly qualified subaspect, not the entire inferred claim. No-support inferred candidates stay unverified or are excluded with a reason; they do not become obligations to mention in the answer. An explicit ask with no support stays a response obligation satisfied through accurate limitation disclosure, not hallucination.

**Transitions:** every identification, search, support/applicability assessment, promotion, demotion, merge, evidence loss and final disposition appends an event with prior/new state, source stage and reason. Deduplication points old IDs to a survivor and preserves origins and query spans. Demotion of an inferred aspect requires new evidence or corrected scope; retrieval ending is not a demotion reason. Explicit asks cannot be silently excluded; if a premise does not apply, a supported explanation or unresolved disclosure addresses the ask. Contradictory evidence may reopen answered aspects.

**Carry-through invariant:** every previously identified ID resolves at every later snapshot to a current ID or explicit terminal merge/exclusion event. Every answer-worthy ID at finalization is either supported/qualified in the answer or unresolved with recorded disclosure state. Candidate exclusions need an audit record, not necessarily user-facing prose. This prevents disappearance while avoiding a requirement to narrate everything the LLM thought of.

**Confirmation prerequisite:** later independent DEV review must first identify at least three distinct carry-through failures across at least two legal-task families/independent scenario clusters, with available applicable support or an undisclosed explicit unresolved ask, stage evidence and competing explanations examined by two reviewers. This is a proposed minimum replication floor for external review, not a prevalence estimate, powered sample size or confirmed threshold. If v1 lacks the intermediate payload needed to establish disappearance, label the case unobservable; do not reconstruct an invented state. Later separately authorized observation instrumentation must preserve v1 behavior before new DEV evidence can qualify. The single medical diagnostic cannot count toward this floor. Failure to establish the problem means defer R3; other reviewed requirements need not depend on it.

## 6. Evidence applicability contract

Record an aspect–evidence relationship rather than a global relevance label. Fields: evidence/chunk/source IDs and spans; relevance {direct, contextual, irrelevant, uncertain}; evidence role {normative_support, supporting_context, counterevidence}; scope, actor, and condition predicates with query facts supporting each; predicate assessment {met, unmet, unknown, not_required}; applicability {direct, conditional, not_applicable, uncertain, unassessed}; uncertainty explanation; support assessment and assessor provenance.

A high-risk-system provision is not an unconditional rule for every AI system. A regulator's duty is not automatically a developer's duty. If actor or necessary scope fails, applicability is not_applicable; if a material fact is missing, conditional/uncertain and disclose that limitation. Context may explain terms without being a required legal proposition. Retrieval rank or keyword overlap cannot establish applicability. Runtime judgments and later independent evaluator judgments live in different records; no evaluator verdict is fed back into TEST runtime.

## 7. V2-R4 — Expansion decisions and value accounting

Expansion is a candidate bounded attempt to fill a specific evidence gap. A hard/broad label is never a runtime trigger. Ask in order: (1) Which explicit or defensibly relevant candidate aspect lacks sufficient applicable evidence? (2) Is it specific enough to search without guessing law? (3) Does the proposed subquery add a legal concept, actor, condition or relation rather than repeat original wording? (4) Is the search feasible within remaining frozen-reference budgets? Log decision and uncertainty; expected value is a reasoned hypothesis, not future gold leakage.

After retrieval distinguish: new unique candidate chunks, new articles/documents, new applicable support, newly resolved aspects, irrelevant material, failed applicability and support lost at final Top-5 selection. Novelty alone is not legal value. Measure candidate-pool gain and final-context gain separately; an added chunk evicted before generation cannot be credited as final evidence coverage. Record which retained aspects gained/lost support, not just counts. An evidence novelty gain without any applicable coverage gain is no demonstrated legal value. Conditional clarification can be useful without resolving a whole aspect and must be reported separately.

**Expansion Value Accounting** fields: before/after evidence snapshot IDs; attempted subqueries and target aspect IDs; new_unique_chunks/new_articles/new_documents as sets plus counts; candidate and final supported-aspect gains/losses; newly_resolved_aspects; condition_clarifications; irrelevant_new_evidence; applicability_failures; unknown_applicability; final_topk_changed as ordered-list and set comparisons; retrieval/merge-rerank work, LLM stages if any, wall time and token/call ledgers. Runtime uses its own support estimates. Evaluator records validated gains in a separate post-seal join.

**Stop:** skip if no specific searchable gap, query is informationally redundant or budget is unavailable. After an attempt, stop at budget exhaustion, no new applicable support/clarification, repeated candidate set, or no unresolved searchable aspect. Do not keep searching simply because success has not occurred. A failed/zero-value expansion retains unresolved aspects and leads to accurate status/disclosure. Within the one allowed expansion episode, any early termination of remaining subqueries must be reasoned and logged; its utility is untested.

Before implementation: independent DEV evidence that search opportunity and noise can be distinguished, reviewed novelty/applicability rubric, and cost-feasible stopping conditions. Adoption needs measurable evidence/answer gains beyond run variation and justified cost. Low v1 aggregate value does not justify removing expansion, and multiple search rounds are not authorized.

## 8. Budgets and historical reference

Read-only historical sources: `scripts/agentic_rag.py` constants and `scripts/retrieval_pipeline.py` configuration. Reference: BM25@20 ∪ Dense@20, reranked final Top-5; at most one retrieval expansion episode, three subqueries, one answer revision, one citation revision, six logical production LLM calls. Standard has one initial retrieval and one answer-generation call. Initial plus three subqueries yields at most four retrieval calls in this reference, with merge-reranks recorded separately. No current runtime or prompts are edited.

Use these bounds as the default comparison envelope. The richer trace/check contract describes information that must be retained if the implementation can produce it; it does not grant extra LLM calls for each field. Budget feasibility must be reviewed before implementation and sealed before TEST. Increasing Top-K above 5, rounds, subquery count, LLM ceiling or context size is an **UNTESTED DESIGN OPTION**, requiring separate authorization, DEV validation and a separately declared comparison. It is not part of the preferred design.

## 9. Controller outcome taxonomy

Keep orthogonal `execution_state`, `answer_status`, `citation_state`, `stop_reason`, unresolved IDs and check freshness. Runtime status is a self-assessment; evaluator labels are separate. Primary outcome precedence is runtime_error > citation_failure > verification_incomplete > incomplete_answer > insufficient_evidence / success_partial_with_disclosure / success_complete. Preserve all secondary flags when a higher-priority outcome wins.

| Outcome | Runtime semantics |
| --- | --- |
| success_complete | Every scoped answer-worthy ask is addressed with sufficient applicable evidence, no material unresolved scope/condition remains, and required checks on exact final answer pass. Not benchmark-certified. |
| success_partial_with_disclosure | At least one material part answered with support; every remaining explicit/answer-worthy unresolved part is accurately disclosed; no known supported omission, unsupported claim or unchecked final edit remains. This is not full completeness. |
| insufficient_evidence | No material supported answer can be offered from available evidence; scope/uncertainty is disclosed. Cannot claim corpus-wide absence merely from Top-5 failure. |
| incomplete_answer | Supported answer-worthy content is omitted, or a known unresolved ask is not disclosed, or known unsupported wording persists. Budget termination does not turn this into success. |
| citation_failure | A required final citation syntax/semantic check fails; preserve answer completeness flags separately. |
| verification_incomplete | Necessary final checks were not reached, failed to parse, or refer to an earlier answer/evidence version; no positive success assertion. |
| runtime_error | Production cannot complete because of execution/transport error; retain partial artifacts and attempted calls. |

`stop_reason` distinguishes scope_addressed, evidence_limit, no_value_expansion, budget_exhausted, unsearchable_gap and execution_failure. Insufficient evidence with missing disclosure also carries incomplete_answer. Null/unreached checks are not false or passes. Conditions that are part of a correctly answered conditional request need not prevent success; missing conditions needed to conclude the actual user case do.

## 10. Trace, validation and staged authorization

The [trace schema design](phase5c2_trace_schema_design_v0.json) specifies append-only stages, evidence snapshots, aspect origins, draft/revised/final versions, checks, status and separate retrieval/production ledgers. It is a field-level design contract, not runnable production code. [Requirement validation matrix](phase5c2_requirement_validation_matrix_v0.json) maps each retained requirement to inputs, prohibitions, evidence, trace and confirmation gates. [Challenge design](phase5c2_challenge_set_design_v0.md) defines independent construction and gold schema only; [evaluation draft](phase5c2_evaluation_protocol_draft_v0.md) defines future comparisons and denominators.

Before any v2 implementation: external design review; independent DEV/TEST corpus-first construction, legal annotation and split freeze; DEV-only baseline confirmation of relevant failure/opportunity classes; R3's multi-case confirmation if that mechanism is proposed; reviewed acceptance/ablation/isolation/budget protocol; explicit later implementation authorization scoped to requirements that pass. Do not demand intervention efficacy before an intervention can be built: this gate authorizes a research prototype, while repeatable causal/quality evidence is a later adoption gate. Unconfirmed R3 may be deferred without blocking a separately reviewed checker/revision candidate.

Recommended sequence: **5C.3 external review → 5C.4 challenge construction/annotation and dataset freeze → 5C.5 DEV baseline confirmation and authorization review → 5D.1 DEV-only v2 implementation → 5D.2 implementation/protocol seal and HOLDOUT TEST production → 5D.3 evaluation and repeated-run/attribution analysis**. All repetitions and arms are predeclared before 5D.2; production outputs are sealed before 5D.3 sees quality. Dataset and implementation freezes here describe future gates, not current actions.

## 11. Required report conclusions

1. Agentic v2 research justified: **YES**, by bounded omission, calibration and coverage evidence plus unresolved attribution questions.
2. Agentic v2 implementation already justified/authorized: **NOT YET**. Current decisions and Tier C hypothesis do not grant authorization.
3. Separate challenge set justified: **YES**, for broader independent evaluation with DEV/HOLDOUT separation; efficacy remains unknown.
4. Replace frozen 31-query benchmark: **NO**. Retain historical comparability and all frozen conclusions.
5. Evidence before implementation: independent DEV failure/opportunity confirmation, legal/applicability agreement, R3 multi-case confirmation if included, feasible budget/isolation and externally reviewed protocol, followed by explicit authorization. Post-implementation adoption additionally requires repeated held-out gains, localized mechanism evidence, safety and cost.
6. Phase to build/freeze challenge dataset: **Phase 5C.4**, after **Phase 5C.3 external review**. No later phase begins here.

Network/API calls = 0; production = 0; evaluator = 0; retrieval/reranking inference = 0; answers generated = 0; benchmark/bootstrap/A3/A4 runs = 0; actual challenge queries and gold records = 0. Only additive design artifacts are created. Design remains DRAFT FOR EXTERNAL REVIEW. STOP.
