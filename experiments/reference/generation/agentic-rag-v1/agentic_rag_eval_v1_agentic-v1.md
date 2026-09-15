# Agentic RAG v1 Evaluation

Variant: `agentic-v1`

## Completion and reliability

- Queries completed: **31/31**
- Queries judged: **31/31**
- Required points evaluated: **102**
- Generation errors: **0**
- Evaluation errors: **0**

## Comparison with Standard RAG

| Metric | Standard RAG | Agentic v1 | Delta |
|---|---:|---:|---:|
| Citation Completeness | 0.6753 | 0.7237 | 0.0484 |
| Citation Correctness | 0.9613 | 0.9828 | 0.0215 |
| Groundedness | 0.9613 | 0.9667 | 0.0054 |
| Unsupported Claim Rate | 0.0387 | 0.0333 | -0.0054 |

A negative delta for Unsupported Claim Rate is an improvement.

## Agent behavior

- Average retrieval calls: **1.2258**
- Average production LLM calls: **3.4839**
- Expansion rate: **0.1935**
- Answer revision rate: **0.2258**
- Citation revision rate: **0.0323**
- Semantic citation check rate: **0.0000**
- Final statuses: `{"incomplete_answer": 1, "insufficient_evidence": 2, "success": 28}`

## Integrity

- Corpus: `corpus-v0.1`
- Prompt: `legal-rag-prompt-v0`
- LLM: `gemini-3.5-flash-lite`
- Production controller received query text only; gold labels were used by the evaluator after generation.
- Frozen corpus and evaluation artifacts were not modified.
