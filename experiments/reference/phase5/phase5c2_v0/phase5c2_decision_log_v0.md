# Phase 5C.2 — Decision log

Artifact status: **DRAFT FOR EXTERNAL REVIEW**. All entries are design decisions subject to external review. No design freeze, dataset creation or implementation authorization occurs here.

| ID | Decision | Status / reason |
| --- | --- | --- |
| DC2-01 | Research/design justified; implementation authorization NOT YET | Preserve distinction between problem investigation, prototype authorization and post-implementation adoption |
| DC2-02 | Answer Revision and Evidence Expansion both retain Insufficient evidence | F5/F6 and Phase 5A attribution safeguards; research status cannot relabel frozen results |
| DC2-03 | V2-R1 INVESTIGATE_BEFORE_IMPLEMENTATION | F2/F5 Tier A; specific supported repairs, draft/final recovery, grounding and cost require independent validation |
| DC2-04 | V2-R2 REFINE | F8 Tier B; distinguish query demands, evidence support, answer coverage and corpus/evidence uncertainty |
| DC2-05 | V2-R3 INVESTIGATE_BEFORE_IMPLEMENTATION | F9 Tier C remains unconfirmed; Aspect Ledger is a candidate abstraction only, with independent multi-case DEV confirmation before implementation |
| DC2-06 | V2-R4 INVESTIGATE_BEFORE_IMPLEMENTATION | F1/F6/F7 A/B; expansion value includes applicable support gains/losses and cost, not just novel chunks |
| DC2-07 | V2-R5 INVESTIGATE_BEFORE_IMPLEMENTATION | F1/F2/F4/F7/F8/F9 A/B/C; challenge design justified, actual construction awaits external review and later scope |
| DC2-08 | V2-R6 KEEP_AS_IS | F3/F4/F5/F6 A; retain provenance, repeated-run safeguards, paired comparisons and all-run reporting |
| DC2-09 | Retain frozen 31-query / 102-point benchmark as primary HISTORICAL COMPARABILITY BENCHMARK | It informed v2 design and is NOT UNTOUCHED CONFIRMATORY HOLDOUT; no replacement, retuning or historical causal claim |
| DC2-10 | Prefer 60 candidates, 48 retained, DEV 16 / HOLDOUT TEST 32 | Four task families, twice DEV allocation in TEST, twelve legal-quality reserves; resource/uncertainty arithmetic is prospective, not measured power |
| DC2-11 | Corpus-first construction; no query/gold records now | corpus/legal structure → legal task → query; no selection on v1 failures or v2 retrieval/answers |
| DC2-12 | D1–D10 taxonomy, overlapping dimensions | Target DEV 4 / TEST 8 per dimension; D6 is post-lock empirical target only, never an outcome-conditioned admission rule; retain shortfalls and limit claims |
| DC2-13 | Split by independent scenario/template/proposition clusters; evaluator-side TEST gold | Same frozen corpus allowed across splits, not document-held-out generalization; implementers preferably never inspect TEST queries before sealing |
| DC2-14 | Exclude exact/trivial medical-diagnostic paraphrases from HOLDOUT TEST; prefer excluding all new splits | Existing diagnostic remains EXPLORATORY / NON-BENCHMARK / NON-CONFIRMATORY and does not count toward R3 confirmation |
| DC2-15 | Separate applicability from evidence role, and runtime evidence absence from corpus absence | supporting_context is a role; direct/conditional/not_applicable/uncertain are applicability; annotate actor/scope/conditions |
| DC2-16 | Orthogonal aspect state and guarded promotion | Explicit asks are response obligations; inferred candidates need support, applicability and intent. Terminal exclusion/merge is recorded without forcing every candidate into the answer |
| DC2-17 | Preserve every stage/check and answer version | No overwrite of first completeness; later citation edit invalidates stale checks. Unverified final bytes cannot receive success_complete |
| DC2-18 | No automatic budget enlargement | Historical final Top-5, one expansion episode, three subqueries, one answer/citation revision and six LLM calls retained as reference. Enlargements are UNTESTED DESIGN OPTION |
| DC2-19 | Runtime outcome and independent benchmark label separated | Full success, partial-with-disclosure, insufficiency, incomplete, citation failure, verification incomplete and runtime error do not erase unresolved flags |
| DC2-20 | Preferred three production repeats; minimum two; optional five | One replication is not a variance estimate; separate query sampling, production stochasticity and judge stochasticity |
| DC2-21 | Minimal staged attribution: S, V1, C, E | C completeness/authorized-goal bundle then incremental expansion contrast; no forced implementation order or isolated R3 claim from bundle gains |
| DC2-22 | AC primary on sufficiently corpus-supported substantive aspects, paired with Q/U and adequacy | Qualified partial content Q and unresolved disclosure U scored separately; zero-answerable queries remain in answerability/adequacy and safety reporting |
| DC2-23 | Prospective margins proposed for review, not frozen | AC practical gain 0.05; safety deterioration tolerance 0.02 plus severe-claim veto, uncertainty/cost requirements. Not calibrated on frozen 31; must be reviewed before TEST |
| DC2-24 | No TEST quality access until all arms/repeats sealed | Strict query-only projection, separated processes/contexts, deny gold and historical analyses, preserve all attempts; isolation acceptance tests are future requirements only |
| DC2-25 | Recommended next phase 5C.3 external review; 5C.4 builds/freezes dataset | 5C.5 DEV confirmation/authorization precedes 5D.1 implementation; 5D.2 seals/runs TEST; 5D.3 evaluates/attributes |
| DC2-26 | Artifact validation and whole-project hash check only | No production/evaluator/imported project modules, model/API/network, retrieval/reranking inference, benchmark/bootstrap/A3/A4 execution |

## Open review decisions and stop gates

External reviewers must accept or revise corpus-dimension feasibility, independent cluster allocation, legal-review capacity, annotation severity/partial-support rubric, proposed margins, production/judge budget, confidentiality ownership and permitted implementation scope. These unresolved review choices are why the artifact is a draft, not a runnable protocol or implementation authorization. No user clarification is needed to finish the currently authorized design artifacts.

D6 cannot be guaranteed without future retrieval, and target enforcement must not turn into failure-based selection. R3 cannot be confirmed from unretained historical state. Three repetitions and 32 TEST items can leave safety/effect intervals inconclusive; do not lower margins after results. Corpus coverage is limited to the frozen corpus, not current external law. Rich trace requirements still need a budget-feasible implementation design in a later authorized phase.

## Execution and integrity record

This phase used only local filesystem reads, standard-library artifact writing and structural/provenance/hash checks. Baseline inventory was captured before design artifact writing and covers every preexisting regular project file, including hidden files and the environment; symlink targets recorded without following external links. All new project files are restricted to `data/evaluation/generation/phase5/phase5c2_v0/`. See [validation](phase5c2_validation_v0.json), [manifest](phase5c2_manifest_v0.json) and [integrity](integrity_before_after_v0.json) for measured verification outcomes; these checks do not claim empirical design effectiveness or OS-level network attestation.

Research justified YES; implementation authorization NOT YET; challenge design justified YES; historical benchmark replaced NO; exact queries/gold created 0. Network/API, production/evaluator and inference calls 0. Design remains DRAFT FOR EXTERNAL REVIEW. STOP.
