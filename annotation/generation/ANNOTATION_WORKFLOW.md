# Generation evaluation annotation workflow

`generation_eval_v0.json` is a **template**, not approved ground truth. Its 31 records exactly mirror the frozen `retrieval_eval.jsonl` benchmark; its answerability label is a preliminary statement that the existing gold set contains directly relevant evidence.

For each record, a legal reviewer should:

1. Read only the query and its linked retrieval gold chunks from the immutable corpus snapshot.
2. Replace the empty `required_points` with concise semantic legal requirements. Every point needs a unique `point_id`, `required` or `important` importance, and one or more gold `supporting_chunk_ids`.
3. Write a concise corpus-grounded `reference_answer`, retaining legally material conditions, exceptions, and scope.
4. Use `insufficient_evidence` only where the linked gold evidence cannot safely answer the question; explain why in `annotation_notes`.
5. Mark the record `draft` during review and `verified` only after human legal review. Do not use generated RAG answers as annotation source material.

Run `python3 scripts/validate_generation_eval.py` before accepting a revision. The validator fixes query identity to the benchmark, verifies source hashes, and rejects unsupported, duplicate, malformed, or non-gold chunk references. It does not perform semantic legal adjudication; that remains a human-review responsibility.
