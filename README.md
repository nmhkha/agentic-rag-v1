# Vietnamese Legal Agentic RAG

An end-to-end, reproducible research and production framework for retrieval and multi-hop reasoning over Vietnamese legal instruments. Specialized for complex regulatory domains, combining deterministic legal routing, domain-specific citation graph expansion, and finite-state multi-turn agentic evidence collection.

---

## 🏛️ Key Capabilities

- **Frozen Legal Corpus v2.1 (Default)**: Covers **17 normative legal instruments** (Laws, Decrees, Circulars, Decisions), comprising **945 articles** and **6,122 deterministic chunks**. Features **Vertical Overlap** (3,626 chunks enriched with leading article titles and clause context in `retrieval_text` to eliminate truncated legal references).
- **Practical Legal Router**: Zero-latency deterministic handling of exact lookups (`Điều X`, `Khoản Y Điều Z`) and legal navigation queries (`Liệt kê các điểm/khoản...`), bypassing unnecessary LLM invocations.
- **Hybrid Retrieval & Reranking**: Sparse BM25 + Dense Semantic (`jina-embeddings-v3`, L2-normalized 1024-d vectors) with candidate union reranked by `BAAI/bge-reranker-v2-m3`.
- **Domain-Specific Expansions**:
  - **Clause-Level Expansion (Mở rộng theo khoản)**: Automatically recovers sibling points ($a, b, c\dots$) to guarantee complete statutory evidence sets.
  - **Deterministic Cross-Reference Following (Nhảy dẫn chiếu)**: Automatically detects and traverses intra-document and inter-document statutory cross-references (`Điều X`, `khoản Y Điều Z`, `khoản X Điều này`, `của Luật này`).
- **Agentic Multi-Turn Loop (v1)**: LLM-driven evidence sufficiency evaluator (`Coverage Check`), dynamic missing-aspect extraction, and bounded targeted sub-query reformulation.
- **FastAPI Web Service**: High-throughput REST API with an interactive web UI client and trace auditing.

---

## 📐 System Architecture

```text
                                 [ User Query ]
                                        │
                                        ▼
                           ┌─────────────────────────┐
                           │  Practical Legal Router │
                           └────────────┬────────────┘
                                        │
            ┌───────────────────────────┴───────────────────────────┐
            ▼ (Deterministic match)                                 ▼ (Complex query)
   ┌───────────────────┐                                 ┌─────────────────────┐
   │ Exact Lookup /    │                                 │  Hybrid Retrieval   │
   │ Legal Navigation  │                                 │ (BM25 + Jina-v3)    │
   └────────┬──────────┘                                 └──────────┬──────────┘
            │                                                       │
            │                                                       ▼
            │                                            ┌─────────────────────┐
            │                                            │  BGE Reranker v2-m3 │
            │                                            └──────────┬──────────┘
            │                                                       │
            │                                                       ▼
            │                                            ┌─────────────────────┐
            │                                            │  Domain Expansions  │
            │                                            │ (Clause + Cross-Ref)│
            │                                            └──────────┬──────────┘
            │                                                       │
            │                                                       ▼
            │                                            ┌─────────────────────┐
            │                                            │ Agentic Multi-Turn  │
            │                                            │ (Coverage Check /   │
            │                                            │  Sub-query Reform)  │
            │                                            └──────────┬──────────┘
            │                                                       │
            └───────────────────────────┬───────────────────────────┘
                                        │
                                        ▼
                           ┌─────────────────────────┐
                           │ Grounded Answer with    │
                           │ Audited Legal Citations │
                           └─────────────────────────┘
```

---

## 📊 Empirical Benchmarks

### 1. In-Domain Benchmark: 31 Legacy Queries (Miền Trí Tuệ Nhân Tạo)
Evaluated across all 6,122 chunks in `corpus-v2.1` (with Vertical Overlap & re-encoded dense vectors) via `eval-sets/retrieval/retrieval_eval.jsonl`:

| Pipeline Configuration | Chunk Recall@5 | Chunk Recall@10 | Chunk Recall@20 | Chunk Hit Rate | Article Hit Rate | Context Size |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **BM25 Baseline** | 65.8% *(+21.1%)* | 75.8% | 81.4% | 87.1% | 96.8% | 5–20 chunks |
| **Dense Baseline (Jina-v3)** | 65.8% *(+17.0%)* | 75.9% | 83.4% | 80.6% | 90.3% | 5–20 chunks |
| **Reranker Baseline (BGE)** | 80.9% *(+19.6%)* | 88.7% | 89.8% | 96.8% | 96.8% | 5–20 chunks |
| **Reranker + Clause Expansion** | 89.4% *(+9.6%)* | 90.9% | 90.9% | 96.8% | 100.0% | ~8.35 chunks |
| **Reranker + Combined (Clause + CrossRef)** | **92.7%** *(+8.6%)* | **94.1%** | **94.1%** | **100.0%** | **100.0%** | **~11.35 chunks** |

*So với `corpus-v0.2`, Vertical Overlap giúp nâng Recall@5 của Reranker từ 61.3% lên 80.9% và cấu hình Combined đạt độ phủ 100% tuyệt đối (31/31 câu).*

### 2. Cross-Corpus Benchmark: 40 Queries (17 Văn Bản Quy Phạm)
Đối chiếu trực tiếp trên toàn bộ 40 câu hỏi chuẩn (`corpus-v0.2` vs `corpus-v2.1`):

| Pipeline Configuration | Chunk Recall@5 | Chunk Hit Rate@5 | MRR@10 | Article Hit Rate@5 |
| :--- | :---: | :---: | :---: | :---: |
| **BM25 Sparse** | 24.7% → **30.5%** *(+5.8%)* | 37.5% → **45.0%** *(+7.5%)* | 0.2986 → **0.3275** | 52.5% → **55.0%** |
| **Dense Semantic (Jina-v3)** | 26.2% → **28.9%** *(+2.8%)* | 40.0% → **40.0%** | 0.3806 → 0.3158 | 52.5% → **52.5%** |
| **Rerank Baseline Top-5 (BGE)** | 30.7% → **36.6%** *(+5.9%)* | 45.0% → **50.0%** *(+5.0%)* | 0.3550 → **0.3975** | 55.0% → **55.0%** |

### 3. Agentic Multi-Turn Progression: 30 New Queries (17 Văn Bản Quy Phạm)
Evaluated multi-turn agentic iterative retrieval across 17 distinct legal instruments:

| Vòng Tìm Kiếm (Turn / Stage) | Chunk Recall | Relative Gain | Chunk Hit Rate | Article Hit Rate | Avg Chunks |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Turn 1 (Single-Pass Top-5)** | **22.8%** | *Baseline* | 30.0% | 43.3% | 5.0 |
| **Turn 2 (Agentic Hop 1 - Gap Filling)** | **33.9%** | **+48.7%** | **40.0%** | **46.7%** | 6.8 |
| **Turn 3 (Agentic Hop 2 - Deep Loop)** | **35.6%** | **+56.1%** | **40.0%** | **46.7%** | 8.0 |
| **Turn 3 + Deterministic Exp (Combined)** | **37.2%** | **+63.2%** | **40.0%** | **46.7%** | 16.1 |

*Detailed reports, empirical logs, and qualitative case studies are documented in [`docs/evaluation/`](docs/evaluation/).*

---

## 📁 Repository Structure

```text
├── data/
│   └── versions/corpus-v2.1/       # Default frozen legal corpus v2.1 (Vertical Overlap chunks)
├── src/legal_rag/                  # Core importable Python package
│   ├── agentic/                    # Finite-state Agentic controllers
│   │   ├── v1/                     # Agentic RAG v1 (Coverage check & sub-queries)
│   │   └── v2/                     # Agentic RAG v2 architecture (Planner & Ledger)
│   ├── ingestion/                  # Legal chunking & document parsers
│   ├── retrieval/                  # Sparse BM25, Dense Jina-v3, BGE Reranker
│   ├── cross_reference.py          # Deterministic legal citation & clause resolver
│   ├── practical.py                # Practical routing router
│   ├── navigation.py               # Deterministic legal structural navigation
│   ├── exact_lookup.py             # Deterministic exact provision lookup
│   └── api/                        # FastAPI application and service endpoints
├── scripts/                        # User-facing execution and evaluation CLIs
│   ├── run_agentic_rag.py          # Main CLI for Agentic RAG execution
│   ├── run_standard_rag.py         # Baseline single-pass RAG runner
│   ├── eval_legacy_31.py           # Evaluation on 31 legacy benchmark queries
│   ├── run_eval_baseline_40.py     # Evaluation on 40 cross-corpus baseline queries
│   ├── eval_agentic_multiturn_v1_30.py # Multi-turn agentic evaluation runner
│   ├── eval_cross_reference_expansion.py # Citation expansion evaluation
│   ├── eval_clause_expansion.py    # Clause sibling expansion evaluation
│   └── build_corpus_v21.py         # Vertical Overlap corpus generator & indexer
├── eval-sets/                      # Benchmark queries & gold annotations
│   ├── retrieval/retrieval_eval.jsonl      # 31 legacy benchmark queries
│   └── retrieval/baseline_eval_40.jsonl    # 40-query cross-corpus benchmark
├── experiments/                    # Evaluation metrics, indexes, and trace runs
│   ├── indexes/corpus-v2.1/        # Precomputed Sparse (BM25) & Dense (Jina-v3) indices
│   └── retrieval/corpus-v2.1/      # Metric results JSON files (legacy_31, baseline_40)
├── docs/                           # Technical documentation and evaluation reports
│   └── evaluation/                 # Comprehensive Markdown reports
└── tests/                          # Package regression test suite
```

---

## 🚀 Installation & Environment Setup

### 1. Requirements
- Python 3.10+ (tested: 3.10.20 and 3.12.14).
- CUDA-compatible GPU recommended for accelerated reranking (CPU fallback supported).

### 2. Setup with Conda / Venv
```bash
# Clone the repository
git clone https://github.com/nmhkha/agentic-rag-v1.git
cd agentic-rag-v1

# Create and activate environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies in editable mode
pip install -e ".[dev]"
```

### 3. LLM Configuration
Copy `.env.example` to `.env` and provide your OpenAI-compatible LLM endpoint (e.g. Gemini API, vLLM, or Ollama):
```bash
cp .env.example .env
```
Edit `.env`:
```env
RAG_LLM_PROVIDER=openai-compatible
RAG_LLM_MODEL=gemini-3.5-flash-lite
RAG_LLM_BASE_URL=https://generativelanguage.googleapis.com/v1beta/openai/
RAG_LLM_API_KEY=your_api_key_here
```

---

## 💻 Quick Start & Usage

### 1. Run Agentic RAG CLI
```bash
# Execute Agentic RAG with full execution trace
python scripts/run_agentic_rag.py --query "Khi nào bên kiểm soát dữ liệu phải xóa hoặc hủy dữ liệu cá nhân?" --trace
```

### 2. Run Comprehensive Evaluation Suites
```bash
# Evaluate all 31 legacy queries (AI domain) across BM25, Dense, Rerank & Expansions
python scripts/eval_legacy_31.py

# Evaluate 40 cross-corpus baseline queries across BM25, Dense & Reranker
python scripts/run_eval_baseline_40.py

# Evaluate 3-turn Agentic Multi-turn loop on 30 cross-corpus queries
python scripts/eval_agentic_multiturn_v1_30.py

# Evaluate Clause Expansion & Cross-Reference Following
python scripts/eval_cross_reference_expansion.py
```

### 3. Launch Web API & UI
```bash
# Start FastAPI server on port 8000
python -m uvicorn legal_rag.api.app:app --host 127.0.0.1 --port 8000 --workers 1
```
Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser to access the interactive web interface.

---

## 📖 Research Documentation & Reports

Detailed technical documentation and empirical findings are available in `docs/`:
- [Legacy 31 Queries Benchmark Report](docs/evaluation/legacy_31_eval_report.md)
- [Agentic Multi-Turn Evaluation Report](docs/evaluation/agentic_multiturn_eval_report.md)
- [Cross-Reference & Citation Resolution Report](docs/evaluation/cross_reference_eval_report.md)
- [Clause-Level Expansion Report](docs/evaluation/clause_expansion_eval_report.md)
- [40-Query Baseline Evaluation Report](docs/evaluation/retrieval_baseline_eval_40_report.md)
- [Web API & Service Guide](docs/WEB_API_GUIDE.md)

---

## 🧪 Testing

Run package test suites to verify ingestion, parsers, retrievers, and agentic controllers:
```bash
pytest
```
