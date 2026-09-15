# Candidate Union v0 Diagnostic Report

BM25@20 ∪ Dense@20 is an unranked, chunk-id-deduplicated candidate pool. No RRF, fusion ranking, reranking, or retriever tuning was performed.

## Configuration

- BM25 depth: 20
- Dense depth: 20
- Verified queries: 31

## Chunk candidate coverage

| Metric | BM25 | Dense | Union |
|---|---:|---:|---:|
| Any-Gold Coverage | 0.935484 | 0.903226 | 0.967742 |
| Full-Gold Coverage | 0.612903 | 0.483871 | 0.709677 |
| Macro Candidate Recall | 0.764209 | 0.680056 | 0.842550 |
| Micro Candidate Recall | 0.704082 | 0.581633 | 0.785714 |

## Perfect-reranker theoretical upper bounds

- Hit@1 upper bound: 0.967742
- Full-answer candidate coverage: 0.709677

These are candidate-coverage upper bounds, not measured reranker performance.

## Gold source attribution

| Source | Count | Ratio |
|---|---:|---:|
| BOTH | 49 | 0.500000 |
| BM25_ONLY | 20 | 0.204082 |
| DENSE_ONLY | 8 | 0.081633 |
| NEITHER | 21 | 0.214286 |

## Query-level source attribution

| Class | Count |
|---|---:|
| BOTH_FIND_GOLD | 27 |
| BM25_ONLY_FINDS_GOLD | 2 |
| DENSE_ONLY_FINDS_GOLD | 1 |
| NEITHER_FINDS_GOLD | 1 |

## Candidate pool

- Average size: 30.387097
- Min / max: 24 / 38
- Average overlap count: 9.612903
- Average overlap ratio: 0.329757
- Size distribution: {"24": 1, "26": 4, "28": 3, "29": 4, "30": 4, "31": 3, "32": 3, "33": 6, "34": 1, "35": 1, "38": 1}

## Article candidate coverage

| Metric | BM25 | Dense | Union |
|---|---:|---:|---:|
| Any-Gold Coverage | 0.967742 | 0.967742 | 0.967742 |
| Full-Gold Coverage | 0.967742 | 0.967742 | 0.967742 |

## Difficulty breakdown

| Difficulty | Queries | Union any | Union full | Macro recall | Avg pool |
|---|---:|---:|---:|---:|---:|
| easy | 10 | 1.000000 | 0.900000 | 0.950000 | 30.900000 |
| hard | 8 | 1.000000 | 0.750000 | 0.827381 | 30.500000 |
| medium | 13 | 0.923077 | 0.538462 | 0.769231 | 29.923077 |

## Query type breakdown

Groups with one sample are descriptive only; no strong inference is made.

| Query type | Queries | Union any | Macro recall |
|---|---:|---:|---:|
| accountability | 1 | 1.000000 | 1.000000 |
| actor_obligation | 5 | 1.000000 | 0.523810 |
| authority | 2 | 1.000000 | 1.000000 |
| classification | 1 | 1.000000 | 1.000000 |
| condition | 3 | 1.000000 | 0.916667 |
| data_governance | 3 | 1.000000 | 0.833333 |
| definition | 1 | 1.000000 | 1.000000 |
| ethics | 1 | 1.000000 | 0.500000 |
| human_oversight | 1 | 1.000000 | 1.000000 |
| incident | 1 | 1.000000 | 1.000000 |
| procedure | 5 | 1.000000 | 1.000000 |
| prohibition | 1 | 1.000000 | 1.000000 |
| public_sector | 2 | 1.000000 | 0.875000 |
| rights_risk | 1 | 1.000000 | 1.000000 |
| sandbox | 2 | 0.500000 | 0.500000 |
| transparency | 1 | 1.000000 | 1.000000 |

## Special failures

| Query | Gold | BM25 found@20 | Dense found@20 | Union found | Union recall |
|---|---:|---:|---:|---:|---:|
| eval002 | 1 | 1 | 1 | 1 | 1.000000 |
| eval005a | 7 | 1 | 1 | 2 | 0.285714 |
| eval010 | 1 | 0 | 1 | 1 | 1.000000 |
| eval011 | 2 | 0 | 0 | 0 | 0.000000 |
| eval012 | 3 | 3 | 3 | 3 | 1.000000 |
| eval022 | 3 | 2 | 0 | 2 | 0.666667 |
| eval023 | 2 | 1 | 0 | 1 | 0.500000 |
| eval026 | 4 | 1 | 2 | 3 | 0.750000 |

Missing gold chunks: 21. Queries with no gold in union: 1.

For missing gold, full-corpus BM25/Dense ranks in the CSV are diagnostic only; candidate depth remains 20.

## Diagnostic interpretation

Candidate generation appears strong enough to justify testing a reranker. Candidate generation has very high any-gold coverage; ranking is likely the dominant bottleneck for most queries.

This statement is diagnostic and does not select a final architecture.
