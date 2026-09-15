# Phase 5C.3 — Versioned design amendments

Design only. This amendment layer supersedes only the clauses identified below in the hash-bound Phase 5C.2 sources. Originals remain DRAFT FOR EXTERNAL REVIEW and byte-identical. The resulting specification freezes design obligations and future decision procedures; it does not freeze numeric acceptance margins, authorize v2 implementation, or certify runtime behavior.

## A1 — Mandatory HOLDOUT TEST blindness

Replaces challenge design §2, decision DC2-13, and any weaker access wording in requirements §10, evaluation §2, trace input boundaries and V2-R5/V2-R6 validation requirements.

**Implementation team / implementation agent MUST NOT inspect exact HOLDOUT TEST queries before the implementation, architecture, prompts, policies, budgets and evaluation configuration used for TEST are sealed.** The prohibition applies to retained human/agent knowledge, indirect logs and shared readable storage, not merely named files. TEST gold remains unavailable to implementers even after sealing. Dataset custodians/legal annotators may know TEST while constructing it, but MUST NOT simultaneously act as implementers with retained TEST knowledge.

After sealing, a separate production runner may receive only the strict production input projection `query_id + exact query`, plus minimal sealed runtime configuration. Query IDs must be opaque. No gold aspects, supporting evidence gold, answerability, dimensions, difficulty, family labels, expected mechanism, quality outcomes or evaluator results may reach that runner. Runtime gold access is FORBIDDEN on DEV as well as TEST. Offline implementer access to DEV gold remains allowed.

Before any TEST release, the custodian verifies the implementation/config/protocol seal and role/access declarations. Every premature exact-query exposure MUST append an exposure event recording timestamp, recipient/role, disclosure channel, affected query hashes/cluster IDs, scope of retained knowledge and disposition. Uncertain exposure scope is conservatively treated as affecting every potentially exposed cluster. Identify affected clusters and downgrade the confirmatory claim; the exposed split MUST NOT be called an `untouched confirmatory holdout`. Alternatively, construct a fresh independently constructed HOLDOUT TEST cohort in a later authorized version. Preserve the original exposure log and version links; deleting logs or hiding files does not restore blindness. A fresh cohort cannot reuse contaminated scenario/proposition clusters. Access-event metadata stays custodian-side.

## A2 — Final-authorized-v2 primary contrast

Replaces evaluation §1's description of E as automatically full v2, all hard-coded primary E−V1 clauses in §5, DC2-21 and dependent arm/metric/validation descriptions.

**PRIMARY TEST CONTRAST = FINAL_EXTERNALLY_AUTHORIZED_V2 − FROZEN_V1.** In Phase 5C.5, before implementation and before TEST exposure, external authorization MUST seal the final v2 definition, primary contrast, secondary contrasts and exact mechanism bundle membership. If final v2 is C, the primary contrast is C−V1. If the expansion policy is also authorized and final v2 is E, it is E−V1. E is planning notation, not the default final system. R3 remains unconfirmed; C/E names and membership must explicitly reflect its omission unless independently confirmed and authorized. No primary arm may be selected after seeing TEST outcomes.

For a C-final plan, register V1−S as secondary; E−C is absent unless an independently authorized expansion arm actually exists. For an E-final plan, register V1−S, C−V1 and E−C as secondaries if all corresponding arms are authorized. Do not duplicate the primary in the secondary family. Optional additional contrasts require explicit pre-TEST registration and cost review. The Phase 5C.2 multiplicity rule applies to the actual registered secondary count; unavailable mechanisms receive `not_authorized/not_tested`, not zero effect. C−V1 remains a bundle comparison if C changes multiple mechanisms. E−C isolates expansion policy only conditional on identical C membership, common components and declared budgets.

Phase 5D.2 verifies the implemented hashes against the Phase 5C.5 authorized definition and the Phase 5D.1 DEV-only work, then seals implementation/configuration/protocol before releasing any TEST query. A change to authorized membership requires a versioned external decision while TEST remains blind; it cannot be chosen from TEST outcomes.

## A3 — Provisional margins and binding governance

Replaces evaluation §5's numeric adoption/safety inequalities as frozen values, DC2-23 and challenge §8's suggestion that 5C.3 resolves numerical margins. The candidate values AC +0.05, Groundedness/Citation Correctness deterioration 0.02, and UCR increase 0.02 remain **PROVISIONAL DESIGN MARGINS — NOT YET FROZEN**. Approved final values are null in this phase.

The binding policy is [margin governance](phase5c3_margin_governance_v0.md). Final values require annotation/rubric and denominator/composition inputs, independent external rationale and approval before any HOLDOUT TEST system quality evaluation, never v1/v2 TEST scores. Phase 5C.4 supplies structure inputs; Phase 5C.5 finalizes margins. At TEST sealing, absent approval means STOP: no confirmatory TEST production or evaluation. In inherited inequalities, substitute the later approved symbols `delta_AC_min`, `epsilon_G`, `epsilon_CC`, `epsilon_UCR`; literal 0.05/0.02 figures are illustrative candidates only.

## A4 — Global provider request scheduler

Adds binding requirements to evaluation §§2/6, requirements §8, trace request-attempt ledgers and V2-R6 validation. Every future live provider request in a common quota domain, including production, transport retries and evaluator retries, MUST pass through one coordinated **GLOBAL PROVIDER REQUEST SCHEDULER**. Worker-local independent full-quota assumptions are forbidden. See [quota scheduler requirements](phase5c3_quota_scheduler_requirements_v0.md).

The execution-time `provider_rate_limit_config` must be resolved and sealed before live production. No permanent 15 RPM scientific constant is introduced; 15 RPM was previously observed/declared for the project, as historical context supplied by the external review. No current quota verification occurs in 5C.3.

## Accepted refinements needed for freeze

The [controller decision table](phase5c3_controller_status_decision_table_v0.json) replaces requirements §9's precedence-only specification and the trace Finalization status derivation. It preserves seven runtime outcomes and orthogonal secondary state; `INVALID_STATE` and `REQUIRES_REVIEW` are specification-validation dispositions with no asserted final runtime status. Runtime status is never benchmark-certified.

Production repeats remain preferred 3, minimum 2, optional stronger 5. Three runs do not automatically provide a precise variance estimate. Report query sampling, generation stochasticity, semantic judge stochasticity and backend/version drift separately. Repeats are not independent query samples. The eight-query fixed judge subset is a **resource-limited judge stability audit**, selected by a sealed deterministic hash/stratified rule before outputs, never by disagreement or performance; it is not a global judge-variance estimate.

All D1–D10 dimensions, multi-axis Aspect Ledger, inferred-admission and applicability safeguards, evaluator-only gold and denominator rules are retained. Size is a PREFERRED DESIGN TARGET, not statistical power certification. The frozen specification and binding registry make inherited clauses and their overrides explicit. No actual query, gold record or runtime code is created.
