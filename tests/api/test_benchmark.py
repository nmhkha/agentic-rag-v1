from __future__ import annotations

import pytest

from tools.research.api.benchmark_e2e import percentile, summarize


def test_latency_summary_uses_nearest_rank_p95() -> None:
    assert percentile([30.0, 10.0, 20.0], 0.95) == 30.0
    assert summarize([10.0, 20.0, 30.0]) == {
        "min": 10.0,
        "mean": 20.0,
        "p50": 20.0,
        "p95": 30.0,
        "max": 30.0,
    }


def test_latency_summary_rejects_empty_samples() -> None:
    with pytest.raises(ValueError, match="empty"):
        summarize([])
