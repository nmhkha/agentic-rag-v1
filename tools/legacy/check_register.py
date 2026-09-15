from pathlib import Path
import csv
from datetime import date


REGISTRY_PATH = Path("data/source_registry/documents.csv")

REQUIRED_COLUMNS = {
    "document_id",
    "document_number",
    "document_title",
    "document_type",
    "issuing_authority",
    "issued_date",
    "effective_from",
    "status",
    "corpus_layer",
    "local_pdf_path",
    "review_status",
}

VALID_DOCUMENT_TYPES = {
    "luat",
    "nghi_dinh",
    "thong_tu",
    "quyet_dinh",
    "nghi_quyet",
}

VALID_STATUSES = {
    "con_hieu_luc",
    "het_hieu_luc",
    "het_hieu_luc_mot_phan",
    "chua_co_hieu_luc",
    "khong_xac_dinh",
}

VALID_CORPUS_LAYERS = {
    "core",
    "related",
    "sectoral",
    "historical",
    "guidance",
}

VALID_REVIEW_STATUSES = {
    "pending",
    "verified",
    "needs_review",
    "rejected",
}


def validate_date(value: str, field_name: str, row_number: int) -> list[str]:
    errors = []

    if not value:
        return errors

    try:
        date.fromisoformat(value)
    except ValueError:
        errors.append(
            f"Dòng {row_number}: {field_name} phải có định dạng YYYY-MM-DD, "
            f"nhận được '{value}'"
        )

    return errors


def validate_registry(path: Path) -> list[str]:
    errors: list[str] = []

    if not path.exists():
        return [f"Không tìm thấy registry: {path}"]

    with path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames is None:
            return ["Registry không có header"]

        missing_columns = REQUIRED_COLUMNS - set(reader.fieldnames)

        if missing_columns:
            errors.append(
                f"Thiếu các cột bắt buộc: {sorted(missing_columns)}"
            )
            return errors

        seen_document_ids: set[str] = set()

        for row_number, row in enumerate(reader, start=2):
            document_id = row["document_id"].strip()

            if not document_id:
                errors.append(f"Dòng {row_number}: document_id đang trống")
            elif document_id in seen_document_ids:
                errors.append(
                    f"Dòng {row_number}: document_id bị trùng: {document_id}"
                )
            else:
                seen_document_ids.add(document_id)

            if not row["document_number"].strip():
                errors.append(
                    f"Dòng {row_number}: document_number đang trống"
                )

            if not row["document_title"].strip():
                errors.append(
                    f"Dòng {row_number}: document_title đang trống"
                )

            document_type = row["document_type"].strip()

            if document_type not in VALID_DOCUMENT_TYPES:
                errors.append(
                    f"Dòng {row_number}: document_type không hợp lệ: "
                    f"{document_type}"
                )

            status = row["status"].strip()

            if status not in VALID_STATUSES:
                errors.append(
                    f"Dòng {row_number}: status không hợp lệ: {status}"
                )

            corpus_layer = row["corpus_layer"].strip()

            if corpus_layer not in VALID_CORPUS_LAYERS:
                errors.append(
                    f"Dòng {row_number}: corpus_layer không hợp lệ: "
                    f"{corpus_layer}"
                )

            review_status = row["review_status"].strip()

            if review_status not in VALID_REVIEW_STATUSES:
                errors.append(
                    f"Dòng {row_number}: review_status không hợp lệ: "
                    f"{review_status}"
                )

            errors.extend(
                validate_date(
                    row["issued_date"].strip(),
                    "issued_date",
                    row_number,
                )
            )

            errors.extend(
                validate_date(
                    row["effective_from"].strip(),
                    "effective_from",
                    row_number,
                )
            )

            errors.extend(
                validate_date(
                    row.get("effective_to", "").strip(),
                    "effective_to",
                    row_number,
                )
            )

    return errors


def main() -> None:
    errors = validate_registry(REGISTRY_PATH)

    if errors:
        print(f"Registry có {len(errors)} lỗi:")

        for error in errors:
            print(f"- {error}")

        raise SystemExit(1)

    print("Registry hợp lệ.")
    print(f"File: {REGISTRY_PATH}")


if __name__ == "__main__":
    main()