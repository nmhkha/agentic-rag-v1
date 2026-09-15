# Phase 5C.1 decision log

Research planning only. Both frozen Phase 5 mechanism labels: **Insufficient evidence**.

| Decision | Status | Evidence / reason |
| --- | --- | --- |
| V2-R1 | INVESTIGATE_BEFORE_IMPLEMENTATION | F2, F5; 9 omission points ở R0; R2-used stratum 9/19 so với 5/19. |
| V2-R2 | REFINE | F8; Frozen Phase 4E mismatch có 17 trường hợp, nên đủ lý do refine requirement. |
| V2-R3 | INVESTIGATE_BEFORE_IMPLEMENTATION | F9; Một diagnostic gợi ý khoảng trống; chưa xác nhận thành problem tổng quát. |
| V2-R4 | INVESTIGATE_BEFORE_IMPLEMENTATION | F1, F6, F7; Weak aggregate contribution relative to measured retrieval work justifies examining selectivity, not deleting expansion. |
| V2-R5 | INVESTIGATE_BEFORE_IMPLEMENTATION | F1, F2, F4, F7, F8, F9; Đủ lý do mở rộng phạm vi đánh giá nghiên cứu; không chứng minh benchmark hiện tại easy. |
| V2-R6 | KEEP_AS_IS | F3, F4, F5, F6; Traceability and replication prevent interpreting small single-run differences as proven contribution. |
| Declare revision supported contribution | REJECT | F5; frozen churn safeguard and CI; label stays Insufficient evidence |
| Delete expansion as useless | REJECT | F6; triggered +3 points, stochastic confounding, narrow benchmark |
| Medical-specific prompt/template/rule | REJECT | F9 is exploratory; no tuning to ad-hoc query |
| A3/A4 or citation mechanism implementation | DEFER | Outside 5C.1; R2 citation revision 0/31, R1 1/31; no controlled A3/A4 evidence |
| Proceed to Phase 5C.2 design | INVESTIGATE_BEFORE_IMPLEMENTATION | YES for requirements/challenge-set design only; no code or dataset now |

Evidence tiers never upgraded by planning status. P2a calibration (B) and P2b goal persistence (C) remain separate. No benchmark reinterpretation, implementation, extra run or new dataset. Historical report 4A wording conflict recorded against authoritative counts 16 retrieval / 9 generation without changing old bytes. Earlier INCOMPLETE manifests are historical; final 93/93 namespace is primary.

Answer Revision: retain as research candidate because used-stratum signal aligns with generation omissions; investigate because churn safeguard, CI and safety conflicts limit attribution; full-set cost delta 7 LLM calls. Expansion: investigate selective value because macro tie/net +1 costs 11 retrievals and 9 reranks; triggered signal does not establish causality.

Ready for 5C.2 DESIGN: YES. STOP.
