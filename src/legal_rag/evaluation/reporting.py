"""Generic writers for normalized evaluation results."""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any, Mapping, Sequence


def write_metrics(path: Path, metrics: Mapping[str, Any]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(metrics, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return path


def write_per_query(path: Path, rows: Sequence[Mapping[str, Any]]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = sorted({key for row in rows for key in row})
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({
                key: json.dumps(value, ensure_ascii=False)
                if isinstance(value, (dict, list)) else value
                for key, value in row.items()
            })
    return path


def render_report(pipeline: str, kind: str, metrics: Mapping[str, Any]) -> str:
    lines = [
        "# Evaluation report",
        "",
        f"- Pipeline: `{pipeline}`",
        f"- Evaluation kind: `{kind}`",
        f"- Queries: **{metrics.get('query_count', 0)}**",
        "",
    ]
    if kind == "retrieval":
        lines.extend(["## Retrieval metrics", ""])
        for level in ("chunk_level", "article_level"):
            lines.append(f"### {level.replace('_', ' ').title()}")
            lines.append("")
            for key, value in metrics[level].items():
                lines.append(f"- {key}: **{value:.10f}**")
            lines.append("")
    else:
        lines.extend([
            "## Generation metrics",
            "",
            f"- Answer Completeness macro: **{metrics['answer_completeness']['macro']:.10f}**",
            f"- Answer Completeness micro: **{metrics['answer_completeness']['micro']:.10f}**",
            f"- Citation Completeness macro: **{metrics['citation_completeness']['macro']:.10f}**",
            f"- Citation Completeness micro: **{metrics['citation_completeness']['micro']:.10f}**",
        ])
        for label, key in (
            ("Citation Correctness", "citation_correctness"),
            ("Groundedness", "groundedness"),
            ("Unsupported Claim Rate", "unsupported_claim_rate"),
        ):
            summary = metrics[key]
            macro = "N/A" if summary["macro"] is None else f"{summary['macro']:.10f}"
            pooled = "N/A" if summary["pooled"] is None else f"{summary['pooled']:.10f}"
            lines.extend([
                f"- {label} macro: **{macro}**",
                f"- {label} pooled: **{pooled}** ({summary['numerator']}/{summary['denominator']})",
            ])
        syntax = metrics["citation_syntax_validity"]
        lines.extend([
            f"- Citation syntax valid: **{syntax['valid_count']}/{syntax['query_count']}**",
            "",
            "Macro values average eligible query ratios. Micro/pooled values divide summed numerators by summed denominators; they are intentionally reported separately.",
            "",
        ])
    return "\n".join(lines)


def write_report(
    path: Path, pipeline: str, kind: str, metrics: Mapping[str, Any]
) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_report(pipeline, kind, metrics), encoding="utf-8")
    return path


def write_outputs(
    output_dir: Path,
    *,
    pipeline: str,
    kind: str,
    metrics: Mapping[str, Any],
    per_query: Sequence[Mapping[str, Any]],
) -> dict[str, Path]:
    return {
        "metrics": write_metrics(output_dir / "metrics.json", metrics),
        "per_query": write_per_query(output_dir / "per_query.csv", per_query),
        "report": write_report(output_dir / "report.md", pipeline, kind, metrics),
    }
