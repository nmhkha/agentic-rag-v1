# Proposed layout v0

Preserve existing frozen source and artifact paths. This is a future structure, not a move instruction.

```text
src/legal_rag/
  common/          # new, independently versioned helpers for v2
  retrieval/       # v2 interfaces; do not silently replace frozen modules
  standard/        # optional new adapter, original remains under scripts/
  agentic_v2/      # new controller, config and prompts with independent versions
scripts/
  agentic_rag.py    # KEEP original v1
  rag_baseline.py   # KEEP original Standard RAG
  evaluate_agentic_rag.py
  evaluate_standard_rag.py
  ...              # KEEP frozen transitive modules and Phase 5 infrastructure
  run/             # new v2 CLI; optional original-preserving v1 launcher
  evaluate/        # new v2 evaluation entrypoints
  dataset/         # reviewed nonfrozen construction tooling
  analysis/        # reviewed analysis entrypoints
  validate/        # reviewed nonfrozen validators
  utilities/       # reviewed registry/source helpers
  legacy/          # only approved, unbound historical tools
prompts/
  legal_rag_v0.txt  # KEEP frozen prompt
  agentic_v2/      # new versioned prompts
tests/            # existing paths initially stay in place
  retrieval/       # future tests
  standard/
  agentic_v1/
  agentic_v2/
data/              # KEEP current corpus/index/gold/results/traces/Phase5 paths
docs/
  repository_cleanup_v0/
archive/           # only after separately approved provenance-preserving plan
```

The leading spaces beforetests/docs are illustrative indentation only. CSV destinations are candidates for nonfrozen files, not approved moves. No ACTIVE_V2 implementation was identified. Phase 5C is design/review material and should remain in its original research lineage.

A future v1 wrapper should invoke the intact original script with its expected repository layout. Moving the module then leaving a shim at its old location would change frozen bytes and is not acceptable. New v2 modules must avoid depending implicitly on mutable sys.path or importing evaluation/gold from production. Data/result separation can first be documented through an index rather than relocating frozen artifacts.
