# Phase 5C.3 — Frozen design specification v0

Effective only when `phase5c3_freeze_manifest_v0.json` records all validation gates PASS and freeze status FROZEN. Scope: external-review amendment and design freeze. No implementation, dataset construction, annotation, benchmark or inference occurs here. Frozen design rules are distinct from future numeric decisions and implementation authorization.

## 1. Binding source composition and precedence

The [binding registry](phase5c3_spec_bindings_v0.json) pins every inherited normative source by SHA-256 and section/JSON selector, with explicit overrides. The [freeze manifest](phase5c3_freeze_manifest_v0.json) binds all Phase 5C.1 and Phase 5C.2 artifacts, this specification, amendments, decision table, margin governance, quota requirements, trace/matrix amendment layer and integrity evidence.

Read inherited 5C.2 clauses through this precedence: the explicit 5C.3 amendment clauses and dedicated decision-table/margin/quota contracts govern their named domains; this specification governs composition and retained requirements; hash-bound 5C.2 normative sections apply everywhere else. Trace and validation-matrix requirements receive the same amendments through [the cross-artifact amendment layer](phase5c3_trace_matrix_amendment_v0.json). There is no alternative choice between old and new wording. Source manifest/console/decision-log statements about 5C.2 being a draft are historical provenance, not the effective 5C.3 status. Historical empirical claims are not re-certified by design freeze. Any unresolved semantic contradiction is a FAIL gate, not permission to choose the convenient clause.

## 2. Retained evidence and research decisions

Answer Revision = **Insufficient evidence**. Evidence Expansion = **Insufficient evidence**. These frozen Phase 5 conclusions MUST NOT change. V2-R1/R3/R4/R5 remain INVESTIGATE_BEFORE_IMPLEMENTATION; V2-R2 remains REFINE; V2-R6 remains KEEP_AS_IS. R3 goal persistence remains **UNCONFIRMED_TIER_C**. The future independent DEV confirmation floor and observability requirements in requirements §5/matrix V2-R3 are retained as a reviewed investigation prerequisite, not observed replication, power certification or implementation approval. The exploratory diagnostic does not count toward confirmation and is not copied into new challenge records.

The frozen 31-query / 102-point benchmark remains the primary historical comparability benchmark.

It is NOT an untouched confirmatory holdout because its outcomes informed v2 requirements.

Future uses: historical comparison, regression and compatibility. It alone is insufficient for v2 generalization, confirmatory mechanism contribution or a causal claim. Its data, gold, scoring, corpus and labels remain unchanged and are not pooled with challenge scoring.

## 3. Behavioral and applicability contracts

Retain requirements §§2–8 and trace/matrix semantics except the explicit A4 additions. Revision repairs only supported applicable content within supplied evidence and frozen-reference budgets; immutable draft, revised and final versions and current-version checks remain mandatory. Checker scope, evidence availability, answer completeness and uncertainty remain separate. Expansion remains bounded, targeted and conditional on later authorization, with candidate-pool and final-context support gain/loss distinguished.

The Aspect Ledger remains multi-axis with independent **Origin, Admission, Search, Support, Applicability, Answer disposition**. Stable IDs, append-only events and explicit merge/exclusion references remain binding if the mechanism is later authorized. `controller_inferred` does not automatically become `answer_worthy`: promotion requires direct relevance to bounded user intent, adequate evidence support and defensible applicability. Partial evidence permits only a narrower supported qualified statement. Explicit user asks remain response obligations even when evidence is unavailable; use calibrated unresolved disclosure without fabricated law. No state may silently disappear merely because retrieval ended. This design approval does not confirm or authorize R3.

Preserve `retrieved ≠ relevant ≠ applicable ≠ answer-worthy`. A special actor/system-class rule cannot become a general duty without supported applicability conditions. Evidence role and applicability are independent; conditional rules preserve conditions and unknown facts. Runtime evidence not found is not corpus-wide absence. Examples remain abstract; no medical-specific rules or templates are introduced.

Reference budgets remain final Top-5, BM25@20 and Dense@20, one expansion episode, at most three subqueries, one answer revision, one citation revision and six logical agentic production LLM calls. Richer traces do not grant additional calls. Increases remain separately authorized UNTESTED DESIGN OPTIONs. No current runtime, prompt or configuration changes occur.

## 4. Deterministic controller decision specification

The [machine-readable decision table](phase5c3_controller_status_decision_table_v0.json) is the sole final-status derivation contract, superseding the old textual precedence. It defines predicate domains, scope, null semantics, invalid combinations, under-specified review cases and mutually exclusive runtime rows. The static validation enumerates the entire declared finite predicate domain; this is a specification check, not execution of an Agentic controller or evaluator.

Valid states produce exactly one of runtime_error, citation_failure, verification_incomplete, incomplete_answer, insufficient_evidence, success_partial_with_disclosure, success_complete. `INVALID_STATE` and `REQUIRES_REVIEW` have null final_status and block any success assertion pending recorded resolution. Runtime statuses are estimates, never benchmark-certified. Retain orthogonal `citation_state`, `execution_state`, `completeness_state`, `unresolved_aspects`, `stop_reason` and all known secondary failure flags. The existing `answer_status` remains a compatibility field, with alias consistency defined in the amendment layer. Budget exhaustion is not itself success or evidence insufficiency; stale checks remain verification_incomplete when no higher explicit failure applies.

## 5. Challenge design, blindness and gold

Retain the full corpus-first procedure, independent legal QA and gold schema in challenge §§3–7, and replace access §2 with A1. The implementation team/agent MUST NOT inspect exact HOLDOUT TEST queries before sealing implementation, architecture, prompts, policies, budgets and evaluation configuration. After sealing a separate production runner receives the strict `query_id` and `query` projection only, plus minimal sealed runtime configuration. Gold, dimensions, difficulty, family/answerability/expected-mechanism labels and all quality/evaluator results are forbidden. Custodian/legal annotator roles must be separated from implementers with retained TEST knowledge. Exposure events and affected clusters must be durably recorded and claims downgraded, or a later authorized independent fresh cohort used; the exposed split cannot be called untouched. Runtime gold access is FORBIDDEN, including DEV.

All D1–D10 dimensions remain: broad/open-ended, multi-aspect, multi-article, cross-document, dispersed evidence, initial Top-5 partial, generation omission risk, decomposition/reformulation opportunity, applicability reasoning, partial/insufficient corpus evidence. Inherited operational definitions, overlap rules, D9/D10 composition and controls remain binding as design targets/gates with documented feasibility review. D6 remains `empirical_unverified` until query/gold/split lock and later blind characterization. D6 cannot select, rewrite or replace an item; a below-target result must be reported as a limitation without cherry-picked replacements or a targeted confirmatory expansion claim.

**PREFERRED DESIGN TARGET:** 60 candidates → 48 retained → 16 DEV + 32 HOLDOUT TEST, with 12 candidate reserves. Alternatives remain 36 retained (12/24) under tighter resources and 60 retained (20/40) with greater cost; the candidate-pool planning ratio remains approximately 1.25. Counts are not constructed records or statistical power certification. Whole scenario/template/proposition clusters stay in one split; near-duplicate scenario/proposition bundles cannot cross DEV/TEST. Reserves are for pre-output legal-quality/duplicate/cluster issues only; exposed DEV reserves cannot migrate into TEST. If whole-cluster allocation prevents exact targets, resolve and document corpus-first feasibility before dataset freeze, never split a cluster to hit a number.

Gold remains evaluator-only: separate required legal aspects, alternative support bundles, evidence role, applicability, evidence sufficiency, answerability and disclosure obligations. Support logic is OR across acceptable alternative bundles and AND within each jointly necessary bundle. Citing every valid alternative is not required. P+ substantive, Q qualified-partial and U unresolved-disclosure obligations remain disjoint under the annotation rubric; disclosure alone is not substantive aspect credit. No challenge record is created now.

## 6. Protocol, contrast, margins and uncertainty

**PRIMARY TEST CONTRAST = FINAL_EXTERNALLY_AUTHORIZED_V2 − FROZEN_V1.** Phase 5C.5 seals final v2 definition, primary contrast, secondary list and exact mechanism bundle membership before implementation and TEST exposure. C-final gives C−V1; E-final gives E−V1 only if expansion is authorized. E is not automatically final v2; C/E membership and names must reflect whether R3 is actually confirmed and authorized. Primary arm selection after TEST outcomes is forbidden. Common components, frozen S/V1 architectures, actual secondary contrast multiplicity and attribution limitations from evaluation §§1/5 remain.

Numeric effect/safety margins remain **PROVISIONAL DESIGN MARGINS — NOT YET FROZEN**; 0.05 AC and 0.02 safety/UCR are candidates only. [Margin governance](phase5c3_margin_governance_v0.md) binds later annotation-structure rationale and external approval. Missing approved margins at TEST sealing means STOP: no confirmatory TEST. No outcome-based threshold tuning is allowed.

Retain preferred three production runs/query/arm, minimum two, optional stronger five, declared before TEST. Three is not automatically a precise variance estimate. Separate query sampling uncertainty, generation stochasticity, semantic judge stochasticity and backend/version drift. Do not pool repeated runs as independent queries. Inherited paired cluster resampling is conditional on observed generation/judging, not a joint uncertainty interval. Backend changes require a recorded compatibility decision, never silent pooling.

The fixed eight-query TEST subset, if retained, is a **resource-limited judge stability audit**, not a global judge-variance estimate. Before outputs, custodian seals exact subset IDs and the deterministic hash/stratified selection algorithm, seed/salt, strata allocation and tie-breaking rule; no selection by disagreement or performance. The main first valid judgment remains primary; two additional passes on identical final output/evidence bytes across all arms/runs characterize stability. No judging occurs now.

All arms/repeats must be sealed before evaluator join or TEST quality access. Keep strict runtime isolation, immutable attempts and quality-blind retry/recovery; failed scheduled slots remain accounted for. Add A4's globally coordinated quota scheduler to every shared-domain live request. Execution-time quota config must be resolved/sealed; current quota is not verified here. Production and evaluator ledgers remain separate even when scheduling shares a quota pool.

## 7. Metrics and denominator contract

Answer Completeness remains primary, computed only evaluator-side from independent gold after all production is sealed. Incorporate evaluation §4 in full, including numerator/denominator tables for answer-level, revision, expansion, controller and goal-persistence metrics. Per-query macro and pooled ratios remain separate; zero denominator is null/not_applicable, with eligible counts. Empty/error answers receive AC=0 where P+ exists and fail response adequacy; no-claim safety ratios are undefined, never perfect safety.

Revision retains draft→final recovery, mechanism-localized recovery, unsupported claims introduced and revision/recheck cost. Expansion retains evidence gain, newly resolved aspects, no-value expansion, retrieval overhead and final-context support gain/loss. Controller retains internal versus evaluator completeness, false-success, false-insufficient and status calibration. Goal persistence retains identified/answered supported applicable aspects, unresolved disclosure and aspect disappearance. Missing or unobservable state is not zero; failed stages are not no intervention; triggered subsets are descriptive post-treatment summaries. No runtime use of gold metrics is permitted. Legacy V1 traces/status are preserved; analysis mapping never rewrites runtime.

## 8. Phase gates and stop

| Phase | Authorized scope when its own gates are satisfied |
| --- | --- |
| 5C.3 | External review + amendment + design freeze only; current phase |
| 5C.4 | Challenge construction + independent legal annotation + dataset freeze; authorized next only if this freeze passes |
| 5C.5 | DEV-only baseline confirmation + mechanism authorization + acceptance-margin finalization + final-v2 decision rule |
| 5D.1 | Authorized Agentic v2 implementation using DEV only |
| 5D.2 | Implementation/config/protocol sealing + blind HOLDOUT TEST production |
| 5D.3 | Evaluator join + repeated-run analysis + attribution + research conclusion |

Agentic v2 research justified: YES. Agentic v2 implementation authorized: NOT YET. Challenge construction authorized next: YES only upon all 5C.3 validation gates passing and FROZEN manifest. This is authorization for future 5C.4 construction/annotation, not execution of that phase in this session. No query/gold, API/network, production/evaluator, inference, benchmark, chatbot diagnostic, A3/A4 or v2 implementation here. STOP after console reporting.
