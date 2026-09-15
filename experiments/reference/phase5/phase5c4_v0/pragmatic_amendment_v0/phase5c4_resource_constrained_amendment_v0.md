# Phase 5C.4-C2-Lite — resource-constrained protocol amendment v0

Status: ADOPTED PROTOCOL; adjudication, final selection and dataset lock NOT STARTED.
Track: **RESOURCE-CONSTRAINED MODEL-ADJUDICATED CHALLENGE BENCHMARK**.
Authority: the user's explicit Phase 5C.4-C2-Lite resource decision. This is a
versioned amendment for the new challenge track, not a rewrite of Phase 5C.3.

## Rationale and preserved history

This graduation/internship research project cannot fund expert legal adjudication
of all 60 candidates and 503 unresolved comparison issues. Construction A,
independent model-based annotation B and comparison C1 are complete. C1 records
0/60 confirmed full substantive agreement, with candidate priorities 5 CRITICAL,
41 HIGH and 14 MEDIUM. The zero is conservative: unresolved wording/content
equivalence also blocks full agreement; it does not mean 60 legally wrong items.
No system outputs informed construction/annotation. None are inspected here.

Independent human legal review remains **NOT COMPLETED**. The historical
HUMAN_LEGAL_REVIEW_REQUIRED gate accurately describes the stronger original
track. For this new track, independent model adjudication C plus the stated
quality gates replaces expert review as the annotation acceptance route. This
does not satisfy the original expert-review gate or certify legal correctness.
All old artifacts, statuses and hashes remain unchanged.

## Explicit amendment precedence

Read this amendment with the immutable Phase 5C.3 specification and its hash-bound
Phase 5C.2 sources. Only the following named domains are overridden for this track:

| Domain | Resource-constrained track rule |
| --- | --- |
| Phase 5C.3 §5 and inherited challenge §§3, 7: expert/legal signoff route | One independent MODEL_BASED_ADJUDICATOR_C may construct evaluator-only benchmark annotations after corpus checks; human expert validation is not claimed. |
| Phase 5C.3 §5 and inherited challenge §5: preferred size | Activate the already permitted alternative: 36 retained, comprising 12 DEV and 24 HOLDOUT TEST, from the existing 60 candidates. |
| Inherited challenge §4: numeric dimension/subtype/control targets | Treat D1–D5/D7–D10 coverage, D9/D10 subtype balance and control counts as documented coverage objectives, not exact mandatory quotas. Never inflate tags or retain ambiguous gold to meet them. Preserve operational definitions. |
| C1's 503 issue entries | C may group equivalent wording, boundaries and support alternatives with a normalization rationale and complete issue-to-decision crosswalk; material disagreement must be resolved or excluded from retained gold. |
| Research claim | Use the resource-constrained model-adjudicated track label and explicit expert-validation limitation. |

All other compatible design contracts remain: corpus-v0.1, evaluator-only gold,
separate relevance/applicability/sufficiency, OR across alternative bundles and
AND within a jointly necessary bundle, disjoint P+/Q/U credit, whole-cluster
separation, immutable queries, outcome-independent selection, and blind TEST.
Numeric acceptance margins remain PROVISIONAL; their final decision is deferred
to Phase 5C.5 before TEST. This amendment neither approves margins nor changes
the prohibition on outcome-based margin tuning or post-TEST threshold selection.

## Target and selection sequence

Target **36 = 12 DEV + 24 HOLDOUT TEST**. This is a target, not a selected set.
Do not backfill the pool, rewrite queries, or use system answers to achieve it.
Remaining candidates become RESERVE or EXCLUDE with reasons, not an automatically
fixed reserve count. Existing DEV exposure prevents migration into TEST, including
reserves. Use the [selection rules](phase5c4_selection_rules_v0.json).

First perform the independent C pass and record item-level eligibility. Then
select among eligible items using bounded scope, corpus clarity, support and
applicability clarity, adjudicability, contamination, whole-cluster independence,
four-family coverage and reasonable dimension coverage. Disagreement is only an
annotation-quality signal; agreement counts are not a ranking objective.
Near-duplicate and cluster disputes must be resolved or conservatively contained
before allocation. A split must not cut a scenario/proposition cluster.

If 36 safe items or the exact 12/24 allocation is infeasible, report the shortfall
and its corpus/cluster reasons. Do not force legal conclusions, move exposed DEV
items into TEST, relax a hard quality gate or claim a completed 36-item benchmark.
Any changed size requires a later explicit versioned decision before system use.

## Model adjudication and gates

One independent C adjudication pass is authorized by this amendment. Follow the
[C protocol](phase5c4_adjudicator_c_protocol_v0.md) in a fresh context that did not
author A, B or C1. This custodian context is not C and remains permanently barred
from Agentic-v2 implementation. C can independently inspect the frozen corpus
and resolve proposals; it must leave UNRESOLVED_LEGAL_AMBIGUITY where stable
corpus-grounded scoring cannot be defined. Such items normally become RESERVE
or EXCLUDE, never forced retained gold.

The exact query, final annotation and split must be locked together before any
later separately authorized blind D6 characterization. D6 stays
EMPIRICAL_UNVERIFIED, is not a selection feature and cannot justify replacements.
No C annotation, selection, lock, D6 measurement or system run occurs in this phase.

## HOLDOUT and release gate

This amendment relaxes human-review requirements only; HOLDOUT blindness remains
mandatory. HOLDOUT_STORAGE_ISOLATION_NOT_YET_ENFORCED remains the current state.
Before Agentic-v2 implementation begins, build and validate an implementation-safe
workspace/export that cannot access TEST query plaintext, gold, dimensions,
answerability or scores through files, archives, logs, caches, symlinks or mounts.
An ignore list, file convention or owner-only modes shared by all contexts do not
prove isolation. Test denied access from the actual implementation identity.
Retained HOLDOUT knowledge also disqualifies an implementation context.

That storage gate does not block authorizing C/selection in trusted contexts;
it continues to block final release/freeze readiness and implementation. Gold is
evaluator-only, including DEV; the later sealed production runner receives only
its authorized query projection. No current runtime or access architecture changes.

## Interpretation and stop

Use the [research claim boundaries](phase5c4_research_claim_boundaries_v0.md).
The frozen 31-query/102-point set remains the separate HISTORICAL COMPARABILITY
BENCHMARK, not an untouched v2 confirmatory holdout. Never pool its denominators
with this challenge. Reduced sample size and cluster dependence limit precision
and subgroup conclusions; the 36-item target is not a power certification.

Ready for independent model adjudication and later final selection: YES, under
this protocol. Benchmark annotations completed by C: NO. Dataset freeze ready:
NO. Implementation: NOT STARTED. Network/API, production/evaluator/retrieval: 0.
STOP after amendment validation and console reporting.
