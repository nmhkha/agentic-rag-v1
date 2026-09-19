#!/usr/bin/env python3
"""Measure HTTP end-to-end latency separately from server-reported RAG latency."""

from __future__ import annotations

import argparse
import json
import math
import os
import platform
import statistics
import subprocess
import sys
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
DEFAULT_OUTPUT_DIR = ROOT / "experiments" / "runs" / "api-benchmark"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Benchmark the legal RAG HTTP API")
    parser.add_argument("--url", default="http://127.0.0.1:8000/api/v1/answers")
    parser.add_argument("--query", required=True)
    parser.add_argument("--warmup", type=int, default=1)
    parser.add_argument("--runs", type=int, default=5)
    parser.add_argument("--timeout", type=float, default=900.0)
    parser.add_argument("--output", type=Path)
    return parser


def percentile(values: list[float], fraction: float) -> float:
    ordered = sorted(values)
    index = max(0, math.ceil(fraction * len(ordered)) - 1)
    return ordered[index]


def summarize(values: list[float]) -> dict[str, float]:
    if not values:
        raise ValueError("cannot summarize empty latency samples")
    return {
        "min": min(values),
        "mean": statistics.fmean(values),
        "p50": statistics.median(values),
        "p95": percentile(values, 0.95),
        "max": max(values),
    }


def cpu_metadata() -> dict[str, Any]:
    metadata: dict[str, Any] = {
        "processor": platform.processor() or os.getenv("PROCESSOR_IDENTIFIER", ""),
        "logical_processors": os.cpu_count(),
    }
    if sys.platform == "win32":
        try:
            import winreg

            with winreg.OpenKey(
                winreg.HKEY_LOCAL_MACHINE,
                r"HARDWARE\DESCRIPTION\System\CentralProcessor\0",
            ) as key:
                metadata["name"] = str(
                    winreg.QueryValueEx(key, "ProcessorNameString")[0]
                ).strip()
        except (OSError, ImportError):
            pass
        command = [
            "powershell.exe", "-NoProfile", "-Command",
            "Get-CimInstance Win32_Processor | "
            "Select-Object -First 1 Name,NumberOfCores,NumberOfLogicalProcessors | "
            "ConvertTo-Json -Compress",
        ]
        try:
            completed = subprocess.run(
                command, check=True, capture_output=True, text=True, timeout=10,
            )
            value = json.loads(completed.stdout)
            metadata.update({
                "name": value.get("Name"),
                "physical_cores": value.get("NumberOfCores"),
                "logical_processors": value.get("NumberOfLogicalProcessors"),
            })
        except (OSError, subprocess.SubprocessError, json.JSONDecodeError):
            metadata["details_unavailable"] = True
    return metadata


def request_answer(url: str, query: str, timeout: float) -> dict[str, Any]:
    body = json.dumps({"query": query}, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=body,
        method="POST",
        headers={"Content-Type": "application/json"},
    )
    started = time.perf_counter()
    with urllib.request.urlopen(request, timeout=timeout) as response:
        payload = json.loads(response.read().decode("utf-8"))
        status_code = response.status
    e2e_latency_ms = (time.perf_counter() - started) * 1000
    return {
        "http_status": status_code,
        "rag_status": payload.get("status"),
        "run_id": payload.get("run_id"),
        "trace_id": payload.get("trace_id"),
        "rag_latency_ms": payload.get("rag_latency_ms"),
        "http_e2e_latency_ms": e2e_latency_ms,
    }


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.warmup < 0 or args.runs < 1:
        raise ValueError("warmup must be >= 0 and runs must be >= 1")

    for _ in range(args.warmup):
        request_answer(args.url, args.query, args.timeout)
    samples = [request_answer(args.url, args.query, args.timeout) for _ in range(args.runs)]
    e2e_values = [float(sample["http_e2e_latency_ms"]) for sample in samples]
    rag_values = [
        float(sample["rag_latency_ms"])
        for sample in samples
        if sample["rag_latency_ms"] is not None
    ]
    result = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "url": args.url,
        "query": args.query,
        "warmup_runs": args.warmup,
        "measured_runs": args.runs,
        "machine": {
            "platform": platform.platform(),
            "python": platform.python_version(),
            "architecture": platform.machine(),
            "cpu": cpu_metadata(),
        },
        "latency_ms": {
            "http_end_to_end": summarize(e2e_values),
            "rag": summarize(rag_values) if rag_values else None,
        },
        "samples": samples,
    }

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    output = args.output or DEFAULT_OUTPUT_DIR / f"api-benchmark_{stamp}.json"
    if not output.is_absolute():
        output = ROOT / output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
