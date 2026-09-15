"""Check or update SHA-256 hashes for source files in documents.csv."""

from __future__ import annotations

import argparse
import csv
import hashlib
import os
import shutil
import sys
import tempfile
from datetime import datetime
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
REGISTRY_PATH = PROJECT_ROOT / "data/source_registry/documents.csv"
BACKUP_DIR = REGISTRY_PATH.parent / "backups"
BLOCK_SIZE = 1024 * 1024
SOURCE_FIELDS = (
    ("official_pdf_path", "official_pdf_hash", "PDF"),
    ("working_docx_path", "working_docx_hash", "DOCX"),
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(BLOCK_SIZE), b""):
            digest.update(block)
    return f"sha256:{digest.hexdigest()}"


def read_csv(path: Path) -> tuple[list[str], list[list[str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as source:
        rows = list(csv.reader(source))
    if not rows:
        raise ValueError(f"CSV rỗng: {path}")
    header, data = rows[0], rows[1:]
    required = {"document_id"} | {
        field for pair in SOURCE_FIELDS for field in pair[:2]
    }
    missing = required - set(header)
    if missing:
        raise ValueError(f"CSV thiếu cột: {sorted(missing)}")
    if any(len(row) != len(header) for row in data):
        raise ValueError("CSV có dòng không cùng số cột với header")
    return header, data


def resolve_source(raw_path: str) -> Path:
    path = Path(raw_path)
    return path if path.is_absolute() else PROJECT_ROOT / path


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
        if checked_header != header or checked_rows != rows:
            raise RuntimeError("Kiểm tra file tạm thất bại: dữ liệu đọc lại không khớp")
        if temporary.read_bytes()[:3] != b"\xef\xbb\xbf":
            raise RuntimeError("Kiểm tra file tạm thất bại: thiếu UTF-8 BOM")
        os.replace(temporary, REGISTRY_PATH)
    except Exception:
        temporary.unlink(missing_ok=True)
        raise
    return backup


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="Chỉ tính và so sánh")
    mode.add_argument("--update", action="store_true", help="Cập nhật hash hợp lệ")
    args = parser.parse_args()

    header, rows = read_csv(REGISTRY_PATH)
    positions = {name: index for index, name in enumerate(header)}
    missing_count = 0
    updates = 0

    for row in rows:
        document_id = row[positions["document_id"]].strip()
        for path_field, hash_field, file_type in SOURCE_FIELDS:
            raw_path = row[positions[path_field]].strip()
            current = row[positions[hash_field]].strip()
            path = resolve_source(raw_path)
            if not path.is_file():
                missing_count += 1
                print(
                    f"{document_id} | {file_type} | {raw_path} | "
                    f"current={current or '<empty>'} | computed=<unavailable> | missing"
                )
                continue

            computed = sha256_file(path)
            status = "match" if current == computed else "changed"
            print(
                f"{document_id} | {file_type} | {raw_path} | "
                f"current={current or '<empty>'} | computed={computed} | {status}"
            )
            if args.update and current != computed:
                row[positions[hash_field]] = computed
                updates += 1

    if args.update and updates:
        backup = safe_write(header, rows)
        print(f"Updated hashes: {updates}")
        print(f"Backup: {backup.relative_to(PROJECT_ROOT)}")
    elif args.update:
        print("Updated hashes: 0 (không có thay đổi)")

    if missing_count:
        print(f"ERROR: thiếu {missing_count} file nguồn", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
