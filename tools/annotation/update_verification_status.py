#!/usr/bin/env python3
"""Safely update verification status for exactly one registry document."""

from __future__ import annotations

import argparse
import csv
import os
import shutil
import tempfile
from datetime import datetime
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
REGISTRY_PATH = PROJECT_ROOT / "data/source_registry/documents.csv"
BACKUP_DIR = REGISTRY_PATH.parent / "backups"
ALLOWED_STATUSES = {
    "pending",
    "structure_verified",
    "content_verified",
    "verified",
    "needs_review",
    "rejected",
}


def read_csv(path: Path) -> tuple[list[str], list[list[str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as source:
        records = list(csv.reader(source))
    if not records:
        raise ValueError(f"CSV rỗng: {path}")
    header, rows = records[0], records[1:]
    required = {"document_id", "verification_status", "verified_by"}
    missing = required - set(header)
    if missing:
        raise ValueError(f"CSV thiếu cột: {sorted(missing)}")
    if any(len(row) != len(header) for row in rows):
        raise ValueError("CSV có dòng không cùng số cột với header")
    return header, rows


def safe_write(header: list[str], rows: list[list[str]]) -> Path:
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
    backup = BACKUP_DIR / f"documents.{timestamp}.csv"
    shutil.copy2(REGISTRY_PATH, backup)
    fd, temporary_name = tempfile.mkstemp(
        prefix=".documents.", suffix=".csv.tmp", dir=REGISTRY_PATH.parent
    )
    temporary = Path(temporary_name)
    try:
        with os.fdopen(fd, "w", encoding="utf-8-sig", newline="") as target:
            writer = csv.writer(target)
            writer.writerow(header)
            writer.writerows(rows)
            target.flush()
            os.fsync(target.fileno())
        checked_header, checked_rows = read_csv(temporary)
        if (checked_header, checked_rows) != (header, rows):
            raise RuntimeError("Kiểm tra file tạm thất bại")
        if temporary.read_bytes()[:3] != b"\xef\xbb\xbf":
            raise RuntimeError("File tạm không giữ UTF-8 BOM")
        os.replace(temporary, REGISTRY_PATH)
    except Exception:
        temporary.unlink(missing_ok=True)
        raise
    return backup


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--document-id", required=True)
    parser.add_argument("--status", required=True, choices=sorted(ALLOWED_STATUSES))
    parser.add_argument("--verified-by", default="")
    args = parser.parse_args()

    verified_by = args.verified_by.strip()
    if args.status != "pending" and not verified_by:
        parser.error("--verified-by không được rỗng khi status khác pending")

    header, rows = read_csv(REGISTRY_PATH)
    positions = {name: index for index, name in enumerate(header)}
    matches = [
        row for row in rows
        if row[positions["document_id"]].strip() == args.document_id
    ]
    if len(matches) != 1:
        parser.error(
            f"document_id phải khớp đúng 1 dòng; tìm thấy {len(matches)}: "
            f"{args.document_id}"
        )

    row = matches[0]
    old_status = row[positions["verification_status"]]
    old_verified_by = row[positions["verified_by"]]
    row[positions["verification_status"]] = args.status
    row[positions["verified_by"]] = verified_by
    backup = safe_write(header, rows)

    print(f"document_id: {args.document_id}")
    print(f"verification_status: {old_status or '<empty>'} -> {args.status}")
    print(f"verified_by: {old_verified_by or '<empty>'} -> {verified_by or '<empty>'}")
    print(f"Backup: {backup.relative_to(PROJECT_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
