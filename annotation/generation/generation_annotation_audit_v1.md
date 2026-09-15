# Generation annotation audit v1

## Scope and method

This is a structural audit of `required_points` and `reference_answer` in
`generation_eval_v0.json`. It uses only the frozen query, linked gold chunks,
and the current draft annotation. It does not alter queries, gold chunks,
answerability, confidence labels, or `annotation_status`; it is not a legal
verification.

Audit rule: a required point should express one independently scorable legal
proposition. A list of alternatives may remain one point when the alternatives
are a single legal rule, but independent duties, triggers, principles, or
procedural consequences should be separated.

`Scope mismatch` means a mismatch between the question and the current
point/answer's use of the supplied gold evidence. It is not a claim that the
gold set should be changed. `Confidence` is confidence in this audit proposal.

## Per-query findings

| Query | Current → proposed points | Points to split | Points to merge | Trim reference answer? | Query/gold scope mismatch | Confidence |
|---|---:|---|---|---|---|---|
| eval001 | 1 → 3 | P1 into high-, medium-, and low-risk classifications; each is independently coverable. | None. | No. | No. | High |
| eval002 | 1 → 2 | P1 into (a) the Prime Minister's issuing authority and (b) the Ministry's preparation/submission role. | None. | Yes—answer the authority first; the Ministry role is contextual. | Mild: the query asks issuer, while the chunk also supplies a preparatory duty. | High |
| eval003 | 1 → 1 | None; timing and covered risk levels form one applicability rule. | None. | No. | No. | High |
| eval004 | 3 → 6 | P1: management-system duty / risk identification-assessment. P2: data governance / human oversight / technical-or-managerial controls. | None. | No. | No. | High |
| eval005a | 2 → 7 | P1 into risk management, data governance, technical records/logs, human oversight. P2 into transparency/incident response, accountability/information provision, and cooperation. | None. | No. | No. | High |
| eval005b | 2 → 6 | P1 into compliant operation/monitoring and data security/human intervention. P2 into standards compliance, transparency/incident response, accountability/information provision, and cooperation. | None. | No. | No. | High |
| eval006 | 1 → 3 | P1 into disclosure of direct AI interaction (with legal exception), machine-readable marking of AI-generated audio/image/video, and ongoing maintenance of transparency information. | None. | No. | Mild attribution ambiguity: chunk 5 imposes the ongoing duty on both provider and deployer; it should not be written as provider-only. | High |
| eval007 | 2 → 6 | P1 into clarity/recognizability, timing, non-concealment, suitability to content/delivery, and non-interference. | None. P2 is a single optional-form mechanism, though its individual forms could be tested separately only if desired. | No. | No. | High |
| eval008 | 2 → 3 | P1 into the general public-disclosure trigger and illustrative cases (real-person simulation / real-event recreation, including its exception). | None. | No. | No. | Medium |
| eval009 | 1 → 1 | None. | None. | No. | No. | High |
| eval010 | 1 → 2 | P1 into urgent technical response (remedy/suspend/recall) and notification to competent authority. | None. | No. | No. | High |
| eval011 | 1 → 2 | P1 into recognition of conformity-assessment results and exemption/reduction/adjustment of compliance duties. | None. | No. | No. | High |
| eval012 | 1 → 4 | P1 into provincial authority, ministry/ministerial-level authority, Ministry of Public Security authority, and the multi-ministry allocation rule. | None. | No. | No. | High |
| eval013 | 2 → 5 | P1 into four criteria: risk, data nature, trial scope/scale, and impact. P2 remains the highest-level/overall-impact rule. | None. | No. | No. | High |
| eval014 | 2 → 4 | P1 into application and trial proposal. P2 into affected-person protection material and technical/personnel/infrastructure material. | None. | No. | No. | High |
| eval015 | 1 → 2 | P1 into safety/security/rights risk trigger and breach-of-limits/failure-to-remedy trigger. | None. | No. | No. | High |
| eval016 | 2 → 4 | P1 into periodic reporting by level 1–2 and level 3. P2 into event report and final report. | None. | No. | No. | High |
| eval017 | 1 → 3 | P1 into eligibility/application package and filing deadline; agency decision deadline; written reasons for refusal/non-extension. | None. | No. | No. | High |
| eval018 | 2 → 4 | P1 into assessment/completion-certificate process and written-reasons duty on refusal. P2 into recognition of results and compliance-duty adjustment. | None. | No. | No. | High |
| eval019 | 1 → 3 | P1 into open principle, safety principle, and controlled-access principle. Quality/connectivity/exploitation is a performance requirement that can remain an important fourth point if the evaluation values it. | None. | Yes—remove data categories because the query asks organisational principles. | Mild: current answer adds the data categories, which are supported but outside the question's requested principle scope. | High |
| eval020 | 1 → 1 | None; permitted access/use conditional on three cumulative condition groups is one definition. | None. | No. | No. | High |
| eval021 | 1 → 3 | P1 into open data, conditional open data, and commercial organisation/enterprise data. | None. | No. | No. | High |
| eval022 | 1 → 3 | P1 into build/update data within management scope; curate/quality-label-standardise listed essential datasets; unified connection/sharing/exploitation. | None. | No. | Mild: the query is limited to open data, while gold point (a) and current answer also cover conditional-open and commercial data. Keep the answer scoped to the asked open-data duty or explicitly state the broader statutory rule. | High |
| eval023 | 1 → 2 | P1 into national-database quality/connectivity/exploitation requirement and agency-database connection/technical-quality-security duty. | None. | No. | No. | High |
| eval024 | 1 → 1 | None; exploitation of vulnerability to cause harm is one prohibition; the listed groups are scope. | None. | No. | No. | High |
| eval025 | 2 → 4 | P1 into high-risk-system trigger; the direct-administrative-decision trigger; and, if coverage of the incorporated scope is evaluated, a separate point for the paragraph-7 use contexts. P2 into qualifying change and the before-continuing-use reassessment consequence. | None. | No—minor wording clarification only. | No, but the paragraph-7 contexts are supporting scope, not an independent assessment trigger unless paired with the direct-decision condition. | Medium |
| eval026 | 1 → 4 | P1 into system/purpose description, risk identification/assessment, controls/mitigation, and human oversight/intervention. | None. | No. | No. | High |
| eval027 | 1 → 4 | P1 into safety/reliability/non-harm; rights/fairness/transparency/non-discrimination; human/community/societal well-being and sustainable development; innovation and social responsibility. | None. | No. | No. | High |
| eval028 | 1 → 4 | P1 into impact identification; explanatory documentation and design/training/testing evidence; allocation of decision-accountability; lifecycle responsibility plus complaint/remedy channel. | None. | No. | No. | Medium |
| eval029 | 1 → 2 | P1 into proportionate human oversight/intervention and rights-protective review. | None. | No. | Mild: the question frames a significant-rights-impact scenario; the gold rules are general framework principles, not a separate threshold-triggered rule. Preserve this as contextual framing rather than inventing a threshold. | High |
| eval030 | 1 → 4 | P1 into non-replacement of human authority/responsibility; human control/intervention; system/data/information security; inspectability and monitoring of development/operation. | None. | No. | No. | High |

## Priority remediation order

The most consequential over-grouping is in `eval005a`, `eval005b`, `eval006`,
`eval022`, `eval025`, `eval027`, `eval028`, `eval029`, and `eval030` because a
single coverage decision currently masks several distinct duties or principles.
`eval019` should additionally trim its answer to the principles asked.

No point-merging recommendation was identified: the present issue is uniformly
under-segmentation, not duplicate semantic points. These are proposed edits for
later human review only; this audit makes no annotation-status change.
