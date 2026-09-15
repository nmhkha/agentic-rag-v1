# Generation annotation v1 report

## Summary

- v0 required-point count: **42**
- v1 required-point count: **102**
- Point-count delta: **+60**
- Queries: **31**; all query IDs and query texts remain frozen.
- Dataset status: **draft**; all 31 records retain `annotation_status = "draft"`.

## 1. Point-count delta per query

| Query | v0 | v1 | Delta |
|---|---:|---:|---:|
| eval001 | 1 | 3 | +2 |
| eval002 | 1 | 2 | +1 |
| eval003 | 1 | 1 | +0 |
| eval004 | 3 | 6 | +3 |
| eval005a | 2 | 7 | +5 |
| eval005b | 2 | 6 | +4 |
| eval006 | 1 | 3 | +2 |
| eval007 | 2 | 6 | +4 |
| eval008 | 2 | 3 | +1 |
| eval009 | 1 | 1 | +0 |
| eval010 | 1 | 2 | +1 |
| eval011 | 1 | 2 | +1 |
| eval012 | 1 | 4 | +3 |
| eval013 | 2 | 5 | +3 |
| eval014 | 2 | 4 | +2 |
| eval015 | 1 | 2 | +1 |
| eval016 | 2 | 4 | +2 |
| eval017 | 1 | 3 | +2 |
| eval018 | 2 | 4 | +2 |
| eval019 | 1 | 3 | +2 |
| eval020 | 1 | 1 | +0 |
| eval021 | 1 | 3 | +2 |
| eval022 | 1 | 3 | +2 |
| eval023 | 1 | 2 | +1 |
| eval024 | 1 | 1 | +0 |
| eval025 | 2 | 3 | +1 |
| eval026 | 1 | 4 | +3 |
| eval027 | 1 | 4 | +3 |
| eval028 | 1 | 4 | +3 |
| eval029 | 1 | 2 | +1 |
| eval030 | 1 | 4 | +3 |

## 2. Changed queries

eval001, eval002, eval004, eval005a, eval005b, eval006, eval007, eval008, eval010, eval011, eval012, eval013, eval014, eval015, eval016, eval017, eval018, eval019, eval021, eval022, eval023, eval025, eval026, eval027, eval028, eval029, eval030.

The changes apply the audit's independently scorable semantic propositions. No point was merged.

## 3. Unchanged queries

eval003, eval009, eval020, eval024.

These queries already had semantically coherent point granularity and were copied from v0 unchanged.

## 4. Reference answers changed

eval002, eval019, eval022, eval025. Changes were limited to direct answering and scope/condition clarification, especially authority in `eval002`, organisational principles in `eval019`, open-data scope in `eval022`, and the direct-administrative-decision condition in `eval025`.

## 5. Scope clarifications

- `eval002`: the Prime Minister's issuing authority is the core answer; the Ministry of Science and Technology's preparation/submission role is contextual and marked `important`.
- `eval006`: the ongoing transparency duty is attributed to both provider and deployer, as stated by the corpus.
- `eval019`: the reference answer is limited to organisational principles; data categories and quality/connectivity/exploitation are not required points.
- `eval022`: points and reference answer are scoped to the asked open-data responsibility, without turning every data category in the gold chunk into a required point.
- `eval025`: paragraph-7 use contexts count only together with the condition that the result is a direct basis for an administrative decision; no invented threshold was added.
- `eval029`: the query's significant-rights-impact language remains framing for the general framework principles, not a new legal threshold.

## 6. Low/medium confidence annotations

No low-confidence annotation is present. Dataset `annotation_confidence = "medium"` remains unchanged for `eval022` and `eval025`. The audit proposal itself marked `eval008`, `eval025`, and `eval028` as medium confidence; these labels were not silently changed in the dataset.

## 7. Potential remaining ambiguity

- `eval008`: the boundary between the general trigger, listed simulation/recreation cases, and creative-content handling may merit human review.
- `eval019`: whether quality, connectivity, and exploitation should be retained as an `important` performance point depends on the intended evaluation scope; v1 follows the instruction to keep the answer on organisational principles.
- `eval022`: the underlying statutory sentence covers open, conditional-open, and commercial data, while the query asks about open data; v1 preserves the query scope.
- `eval028`: the framework's accountability principles are general guidance; reviewers may decide how much evidence a generated answer must provide for each split point.

## 8. Independent-scoring quality check

For the required minimum set (`eval001`, `eval005a`, `eval005b`, `eval006`, `eval007`, `eval014`, `eval019`, `eval022`, `eval025`, `eval027`, `eval028`, `eval029`, `eval030`), a human reviewer can independently decide coverage for each required point from the point description and its supporting gold chunk(s). Result: **YES for all listed queries**; no query is flagged.

## Validation basis

The v1 manifest records hashes for the v0 source, frozen retrieval evaluation, and frozen corpus. Supporting chunks are restricted to existing retrieval gold chunks. Run `python3 scripts/validate_generation_eval.py` and the unit tests after generation.
