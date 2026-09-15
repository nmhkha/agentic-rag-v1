# Independent model adjudicator C protocol v0

Role: **MODEL_BASED_ADJUDICATOR_C**. One independent third adjudication pass is
authorized for evaluator-gold construction under the resource-constrained track.
This protocol does not start that pass. Human legal validation: NOT COMPLETED.

## Independence and packet preparation

Use a fresh context that did not author Annotation A, Annotation B or C1 comparison
judgments. A custodian prepares and hash-binds the packet; the current custodian
does not claim to be independent C. C and all contexts exposed to HOLDOUT remain
ineligible for future Agentic-v2 implementation. Record role, model/version when
available, session identity, prior exposure, authorized inputs and timestamps;
do not infer independent expertise from a model identity.

Allow exact immutable query, the complete original corpus-v0.1, Proposal X,
Proposal Y, disagreement registry, generic frozen rubric plus this amendment,
and query-text-only contamination references/results needed for admission review.
For this pass, assess the existing 60 candidates; grouping issues reduces review
overhead without silently declaring unreviewed candidates adjudicated.

Custodian must validate 60 unique identities and exact query/hash correspondence.
Present A/B annotations under neutral X/Y labels, including substantive scope,
aspects, evidence, applicability, sufficiency, answerability and proposed tags.
Keep the X/Y-to-A/B mapping and source hash provenance private; translate issue
references consistently. Do not include author identities, system-performance
information or historical outcome summaries. Proposals are hypotheses to check,
not authoritative answers. No proposal wins because it is longer or has more
citations. Packet preparation must not rewrite either original annotation.

Forbidden inputs: Standard/V1/V2 answers, scores, retrieval results/ranks, initial
Top-5, evaluator results, traces, mechanism/intervention usage and historical
benchmark scores. Full corpus access is permitted; production retrieval, dense
or reranker inference, evaluator execution and external API/network calls are not.
Deterministic local text search, direct reading and hierarchy inspection are
annotation research and must be logged separately from production inference.

## One adjudication pass

1. Verify input hashes, role eligibility and completeness. Stop on mapping failure
   or prohibited outcome exposure; preserve the event rather than hiding it.
2. Independently identify the finite task, explicit asks, user facts, unknown facts
   and justified exclusions from the exact query. Do not improve query wording.
3. Read X/Y and their disagreement groups. Independently inspect the relevant
   frozen corpus clauses, parent context, alternatives and counterevidence.
4. Resolve material issues first: required proposition, actor/duty, legal scope,
   condition, support bundle, sufficiency, answerability, contamination/admission.
   A corpus ambiguity cannot be repaired by guessing legislative intent.
5. Normalize wording-equivalent scope, synonymous aspect phrasing, equivalent
   valid evidence alternatives and non-material atomization only when bounded
   corpus semantics are equivalent. Record the shared legal meaning, evidence
   and normalization rationale. Preserve one-to-many issue-to-decision links;
   all 503 original issues must remain traceable, not individually repeated.
6. Return an independently reasoned decision, which may follow X, follow Y,
   combine only independently justified components, or differ from both.
   Never mechanically take union, intersection, X by default or Y by default.
7. For a stable record, produce a final annotation for this model-adjudicated
   benchmark; for an unstable record return UNRESOLVED_LEGAL_AMBIGUITY and a
   RESERVE/EXCLUDE recommendation. Do not force retained gold to hit 36 items.

## Required candidate output

Every record identifies the immutable query/hash and source/proposal hashes,
adjudicator role and decision timestamp. Record:

- Final bounded scope: asks, bounded interpretation, relevant facts, unspecified
  facts, excluded scope with reason, and applicable temporal boundary.
- Final coherent, independently scorable required legal aspects, their bounded
  role and materiality. No aspect inflation from splitting wording fragments.
- Final support bundles with document/article/clause/point/chunk, text field,
  exact span offsets and hashes, parent context and accepted alternatives.
  Preserve AND inside each necessary bundle and OR across valid alternatives.
- Applicability: direct, conditional, not_applicable or uncertain, with actor,
  legal scope, system class, material conditions and known/unknown predicates.
- Evidence sufficiency: sufficient_support, partial_support or
  no_support_in_corpus, including the supported/unsupported boundary and reason.
- Answerability: fully_answerable, partially_answerable or insufficient_evidence.
- Disjoint substantive P+, qualified Q and unresolved-disclosure U obligations;
  disclosure alone never earns substantive credit. Pair qualifications and
  disclosures under the inherited aspect ledger/rubric.
- D1–D5/D7–D10 membership with corpus/annotation rationale. D6 remains null with
  status EMPIRICAL_UNVERIFIED, never estimated from dispersion or disagreement.
- retain/reserve/exclude recommendation, per-gate eligibility, contamination
  finding and any cluster relationship requiring custodian allocation review.
- A complete crosswalk from C1 issues to resolution, normalization, duplication
  of another issue, or unresolved ambiguity, with evidence and rationale.

Every substantive supported assertion must have valid frozen-corpus evidence.
For partial/no-support aspects, identify the precise unsupported ask and record
a scoped whole-corpus audit, plausible alternatives and why support remains
absent. A failed keyword search is not proof of absence. An insufficient-evidence
item may be retained when the absence finding and disclosure scoring are stable;
that differs from unresolved legal ambiguity about what the corpus means.

Applicability need only be resolved sufficiently for stable scoring: an unknown
user fact can legitimately require a conditional response without making the
item ambiguous. Explicitly distinguish uncertainty in user facts, uncertainty in
source interpretation and the applicability of an absence disclosure itself.

## Eligibility and selection handoff

Apply all hard gates in phase5c4_selection_rules_v0.json. Failed hard gates mean
RESERVE or EXCLUDE. Prohibited contamination includes exact/trivial duplicates
of historical/diagnostic references and strong full-task near-duplicates; shared
articles or topical overlap alone are not prohibited. Adjudicate the bounded
scenario/proposition relation and record it. Unresolved contamination cannot
pass retention. Different material conditions may distinguish tasks, but their
scenario-cluster relationship must still be addressed before splitting.

Do not select by agreement count, Standard/V1/V2 quality, retrieval rank or expected
system difficulty. Custodian selection follows adjudicated eligibility and
cluster-safe coverage rules. C recommends admission; the target allocation is a
separate recorded step, not automatically C's first 36 retain recommendations.
No new benchmark items, split reassignment or gold lock occurs in this amendment.

## Completion, confidentiality and limitations

Create a separately authorized, new versioned C-results namespace for the future
pass. Never overwrite A/B/C1 or their historical outcomes. Store query/gold and
decision detail privately; public outputs contain only opaque IDs and aggregates.
Seal C results, issue crosswalk, final selection and query/gold/split hashes when
their gates pass. Do not run D6, systems or evaluation as part of C adjudication.

Keep independent_human_legal_validation = NOT_COMPLETED,
adjudicator_type = MODEL_BASED, and track = RESOURCE_CONSTRAINED_MODEL_ADJUDICATED.
“Final” denotes benchmark scoring annotation, not expert-validated legal truth.
HOLDOUT_STORAGE_ISOLATION_NOT_YET_ENFORCED still blocks implementation and final
release/freeze readiness until a real access boundary is separately validated.
