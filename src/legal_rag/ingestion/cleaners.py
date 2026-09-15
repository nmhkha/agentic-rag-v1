from __future__ import annotations

import csv
import re
import unicodedata
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[3]

REGISTRY_PATH = PROJECT_ROOT / "data" / "source_registry" / "documents.csv"
EXTRACTED_DIRECTORY = PROJECT_ROOT / "data" / "extracted"
VALIDATION_DIRECTORY = PROJECT_ROOT / "data" / "validation"

BOILERPLATE_PATH = (
    PROJECT_ROOT
    / "data"
    / "source_registry"
    / "boilerplate_lines.txt"
)

REPORT_PATH = VALIDATION_DIRECTORY / "cleaning_report.csv"


def read_registry() -> list[dict[str, str]]:
    if not REGISTRY_PATH.exists():
        raise FileNotFoundError(
            f"Không tìm thấy registry: {REGISTRY_PATH}"
        )

    with REGISTRY_PATH.open(
        "r",
        encoding="utf-8-sig",
        newline="",
    ) as file:
        reader = csv.DictReader(file)

        required_columns = {
            "document_id",
            "extraction_method",
        }

        fieldnames = set(reader.fieldnames or [])
        missing_columns = required_columns - fieldnames

        if missing_columns:
            raise ValueError(
                "documents.csv thiếu các cột: "
                f"{sorted(missing_columns)}"
            )

        return list(reader)


def load_boilerplate_lines(path: Path | None = None) -> set[str]:
    """
    Chỉ xóa những dòng được người dùng liệt kê chính xác trong file cấu hình.

    File boilerplate_lines.txt có thể chứa:
    - dòng quảng bá;
    - tên website;
    - thông báo tải xuống;
    - footer lặp lại.

    Dòng bắt đầu bằng # được coi là chú thích.
    """
    path = path or BOILERPLATE_PATH

    if not path.exists():
        return set()

    boilerplate_lines: set[str] = set()

    for raw_line in path.read_text(
        encoding="utf-8"
    ).splitlines():
        line = normalize_single_line(raw_line)

        if not line or line.startswith("#"):
            continue

        boilerplate_lines.add(line)

    return boilerplate_lines


def normalize_single_line(line: str) -> str:
    """
    Chuẩn hóa một dòng theo cách bảo thủ:
    - Unicode NFC;
    - thay non-breaking space;
    - gom khoảng trắng ngang;
    - bỏ khoảng trắng đầu/cuối.
    """
    line = unicodedata.normalize("NFC", line)
    line = line.replace("\u00a0", " ")
    line = re.sub(r"[ \t]+", " ", line)
    return line.strip()


def clean_text(
    raw_text: str,
    boilerplate_lines: set[str],
) -> tuple[str, list[str]]:
    """
    Làm sạch text nhưng không thay đổi cấu trúc pháp lý.

    Không thực hiện:
    - lower-case;
    - sửa chính tả;
    - ghép câu dựa trên suy đoán;
    - xóa dòng chỉ chứa số;
    - xóa tự động Điều/Khoản/Điểm;
    - thay thế nội dung bằng LLM.
    """
    raw_text = unicodedata.normalize("NFC", raw_text)
    raw_text = raw_text.replace("\r\n", "\n").replace("\r", "\n")

    cleaned_lines: list[str] = []
    removed_lines: list[str] = []

    previous_line_was_blank = False

    for raw_line in raw_text.split("\n"):
        line = normalize_single_line(raw_line)

        if line in boilerplate_lines:
            removed_lines.append(line)
            continue

        if not line:
            if cleaned_lines and not previous_line_was_blank:
                cleaned_lines.append("")

            previous_line_was_blank = True
            continue

        cleaned_lines.append(line)
        previous_line_was_blank = False

    while cleaned_lines and cleaned_lines[-1] == "":
        cleaned_lines.pop()

    cleaned_text = "\n".join(cleaned_lines).strip()

    return cleaned_text, removed_lines


def count_nonempty_lines(text: str) -> int:
    return sum(
        1
        for line in text.splitlines()
        if line.strip()
    )
