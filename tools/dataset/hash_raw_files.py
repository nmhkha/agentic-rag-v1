from pathlib import Path
import hashlib


ROOT = Path(__file__).resolve().parents[2]
RAW_PDF_DIRECTORY = ROOT / "data/raw/pdf"


def calculate_sha256(file_path: Path) -> str:
    sha256 = hashlib.sha256()

    with file_path.open("rb") as file:
        for block in iter(lambda: file.read(8192), b""):
            sha256.update(block)

    return sha256.hexdigest()


def main() -> None:
    pdf_files = sorted(RAW_PDF_DIRECTORY.glob("*.pdf"))

    if not pdf_files:
        print(f"Không tìm thấy PDF trong {RAW_PDF_DIRECTORY}")
        return

    for pdf_file in pdf_files:
        hash_value = calculate_sha256(pdf_file)

        print(f"{pdf_file.name}")
        print(f"sha256:{hash_value}")
        print()


if __name__ == "__main__":
    main()
