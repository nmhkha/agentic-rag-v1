# Retriever Comparison v0

| Metric | BM25 | Dense | Hybrid | Hybrid vs best baseline |
|---|---:|---:|---:|---:|
| Chunk Hit@1 | 0.322581 | 0.548387 | 0.387097 | -0.161290 |
| Chunk Hit@3 | 0.548387 | 0.645161 | 0.612903 | -0.032258 |
| Chunk Hit@5 | 0.709677 | 0.709677 | 0.645161 | -0.064516 |
| Chunk Recall@5 | 0.445289 | 0.487788 | 0.442729 | -0.045059 |
| Chunk Recall@10 | 0.576370 | 0.585228 | 0.604992 | +0.019764 |
| Chunk MRR@10 | 0.481452 | 0.620161 | 0.536060 | -0.084101 |
| Article Hit@1 | 0.677419 | 0.645161 | 0.612903 | -0.064516 |
| Article Hit@3 | 0.967742 | 0.870968 | 0.935484 | -0.032258 |
| Article Hit@5 | 0.967742 | 0.870968 | 0.967742 | +0.000000 |
| Article MRR@10 | 0.801075 | 0.752688 | 0.775269 | -0.025806 |

## Difficulty comparison

### easy

| Metric | BM25 | Dense | Hybrid |
|---|---:|---:|---:|
| hit_at_1 | 0.500000 | 0.700000 | 0.500000 |
| hit_at_3 | 0.600000 | 0.700000 | 0.600000 |
| hit_at_5 | 0.600000 | 0.900000 | 0.600000 |
| recall_at_5 | 0.550000 | 0.800000 | 0.600000 |
| recall_at_10 | 0.683333 | 0.833333 | 0.783333 |
| mrr_at_10 | 0.566667 | 0.750000 | 0.583333 |
### hard

| Metric | BM25 | Dense | Hybrid |
|---|---:|---:|---:|
| hit_at_1 | 0.125000 | 0.375000 | 0.375000 |
| hit_at_3 | 0.500000 | 0.500000 | 0.625000 |
| hit_at_5 | 0.875000 | 0.500000 | 0.750000 |
| recall_at_5 | 0.490079 | 0.383929 | 0.500992 |
| recall_at_10 | 0.581349 | 0.561508 | 0.571429 |
| mrr_at_10 | 0.401042 | 0.486458 | 0.559375 |
### medium

| Metric | BM25 | Dense | Hybrid |
|---|---:|---:|---:|
| hit_at_1 | 0.307692 | 0.538462 | 0.307692 |
| hit_at_3 | 0.538462 | 0.692308 | 0.615385 |
| hit_at_5 | 0.692308 | 0.692308 | 0.615385 |
| recall_at_5 | 0.337179 | 0.311538 | 0.285897 |
| recall_at_10 | 0.491026 | 0.408974 | 0.488462 |
| mrr_at_10 | 0.465385 | 0.602564 | 0.485348 |

## Complementarity analysis

- BM25-only successes: 6; Hybrid Hit@5 success: 2; IDs: eval005a, eval005b, eval007, eval022, eval023, eval028
- Dense-only successes: 6; Hybrid Hit@5 success: 2; IDs: eval001, eval002, eval010, eval012, eval021, eval025
- Both successes: 16; Hybrid Hit@5 success: 16; IDs: eval003, eval004, eval006, eval008, eval009, eval013, eval014, eval015, eval016, eval017, eval018, eval019, eval020, eval024, eval029, eval030
- Both failures: 3; Hybrid Hit@5 success: 0; IDs: eval011, eval026, eval027

Hybrid recovered both-baseline failures: 0 (none)  
Hybrid preserved one-sided successes: 4 (eval001, eval007, eval025, eval028)  
Hybrid degraded at Hit@5: 8 (eval002, eval005a, eval005b, eval010, eval012, eval021, eval022, eval023)

## Hybrid degraded strong baseline results

Count: 12

| query_id | BM25 first gold rank | Dense first gold rank | Hybrid first gold rank |
|---|---:|---:|---:|
| eval001 | 6 | 1 | 2 |
| eval002 | not in top 10 | 4 | 9 |
| eval005a | 4 | not in top 10 | 10 |
| eval005b | 4 | 6 | 8 |
| eval010 | not in top 10 | 1 | not in top 10 |
| eval012 | not in top 10 | 3 | 6 |
| eval013 | 2 | 1 | 2 |
| eval014 | 5 | 1 | 2 |
| eval018 | 2 | 1 | 2 |
| eval021 | 6 | 4 | 9 |
| eval022 | 1 | not in top 10 | not in top 10 |
| eval023 | 3 | not in top 10 | 9 |

## Five prior BM25 failure cases

| query_id | BM25 rank | Dense rank | Hybrid rank | BM25 Hit@5 | Dense Hit@5 | Hybrid Hit@5 | Hybrid Recall@5 |
|---|---:|---:|---:|---:|---:|---:|---:|
| eval002 | not in top 10 | 4 | 9 | 0 | 1 | 0 | 0.000000 |
| eval010 | not in top 10 | 1 | not in top 10 | 0 | 1 | 0 | 0.000000 |
| eval011 | not in top 10 | not in top 10 | not in top 10 | 0 | 0 | 0 | 0.000000 |
| eval012 | not in top 10 | 3 | 6 | 0 | 1 | 0 | 0.000000 |
| eval026 | not in top 10 | not in top 10 | not in top 10 | 0 | 0 | 0 | 0.000000 |
