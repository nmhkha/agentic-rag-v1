from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[2]
CHUNKS_PATH = PROJECT_ROOT / "data" / "processed" / "chunks.jsonl"
VALIDATION_DIRECTORY = PROJECT_ROOT / "data" / "validation"
DUPLICATE_REPORT_PATH = VALIDATION_DIRECTORY / "duplicate_chunks_report.txt"
SHORT_REPORT_PATH = VALIDATION_DIRECTORY / "short_chunks_report.txt"
MIN_CHARS = 20


def read_chunks() -> list[dict[str, Any]]:
    chunks: list[dict[str, Any]] = []
    with CHUNKS_PATH.open("r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            try:
                chunks.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValueError(
                    f"JSONL lỗi tại dòng {line_number}: {exc}"
                ) from exc
    return chunks


def main() -> None:
    chunks = read_chunks()
    by_id: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for chunk in chunks:
        by_id[str(chunk["chunk_id"])].append(chunk)

    duplicate_groups = {
        chunk_id: rows
        for chunk_id, rows in by_id.items()
        if len(rows) > 1
    }

    duplicate_lines = [
        f"duplicate_chunk_ids = {len(duplicate_groups)}",
        f"duplicate_rows = {sum(len(rows) for rows in duplicate_groups.values())}",
        "",
    ]
    for chunk_id, rows in sorted(duplicate_groups.items()):
        duplicate_lines.append(f"[{chunk_id}] count={len(rows)}")
        texts = {str(row.get("text") or "") for row in rows}
        duplicate_lines.append(
            f"same_text={'yes' if len(texts) == 1 else 'no'}"
        )
        for row in rows:
            duplicate_lines.append(
                "  "
                f"source_start_line={row.get('source_start_line')} | "
                f"level={row.get('chunk_level')} | "
                f"text={row.get('text')!r}"
            )
        duplicate_lines.append("")

    short_chunks = [
        chunk
        for chunk in chunks
        if len(str(chunk.get("text") or "").strip()) < MIN_CHARS
    ]
    short_lines = [
        f"short_chunk_count = {len(short_chunks)}",
        "classification = warning (không tự động xóa)",
        "",
    ]
    for chunk in short_chunks:
        text = str(chunk.get("text") or "")
        short_lines.append(
            f"{chunk['chunk_id']} | "
            f"source_start_line={chunk.get('source_start_line')} | "
            f"length={len(text.strip())} | text={text!r}"
        )

    VALIDATION_DIRECTORY.mkdir(parents=True, exist_ok=True)
    DUPLICATE_REPORT_PATH.write_text(
        "\n".join(duplicate_lines).rstrip() + "\n",
        encoding="utf-8",
    )
    SHORT_REPORT_PATH.write_text(
        "\n".join(short_lines).rstrip() + "\n",
        encoding="utf-8",
    )

    print(f"duplicate_chunk_ids = {len(duplicate_groups)}")
    print(f"short_chunk_count = {len(short_chunks)}")
    print(
        "reports = "
        f"{DUPLICATE_REPORT_PATH.relative_to(PROJECT_ROOT)}, "
        f"{SHORT_REPORT_PATH.relative_to(PROJECT_ROOT)}"
    )


if __name__ == "__main__":
    main()
