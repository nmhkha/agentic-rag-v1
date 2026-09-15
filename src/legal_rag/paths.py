"""Minimal repository-relative paths shared by runtime packages."""

from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = REPOSITORY_ROOT / "data"
CORPUS_VERSION_DIR = DATA_DIR / "versions" / "corpus-v0.1"
INDEX_DIR = REPOSITORY_ROOT / "experiments" / "indexes"
PROMPT_DIR = REPOSITORY_ROOT / "prompts"
EXPERIMENT_RUNS_DIR = REPOSITORY_ROOT / "experiments" / "runs"
GENERATION_TRACE_DIR = EXPERIMENT_RUNS_DIR / "generation" / "traces"
