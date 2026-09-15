from __future__ import annotations

import csv
import re
import zipfile
from pathlib import Path
from typing import TYPE_CHECKING, Iterator
from xml.etree import ElementTree

if TYPE_CHECKING:
    from docx.document import Document as DocumentObject
    from docx.table import Table
    from docx.text.paragraph import Paragraph

try:
    from docx import Document
    from docx.document import Document as DocumentObject
    from docx.oxml.table import CT_Tbl
    from docx.oxml.text.paragraph import CT_P
    from docx.table import Table
    from docx.text.paragraph import Paragraph
except ImportError:  # Keep package imports usable before optional dependencies install.
    Document = None
    DocumentObject = object
    CT_Tbl = CT_P = Table = Paragraph = object


PROJECT_ROOT = Path(__file__).resolve().parents[3]
REGISTRY_PATH = PROJECT_ROOT / "data" / "source_registry" / "documents.csv"
OUTPUT_DIRECTORY = PROJECT_ROOT / "data" / "extracted"
REPORT_PATH = PROJECT_ROOT / "data" / "validation" / "extraction_report.csv"


def iter_block_items(document: DocumentObject) -> Iterator[Paragraph | Table]:
    """
    Duyệt paragraph và table theo đúng thứ tự xuất hiện trong DOCX.
    """
    body = document.element.body

    for child in body.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, document)
        elif isinstance(child, CT_Tbl):
            yield Table(child, document)


def normalize_line(text: str) -> str:
    """
    Chỉ chuẩn hóa khoảng trắng cơ bản.
    Không lower-case và không sửa nội dung pháp luật.
    """
    text = text.replace("\u00a0", " ")
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()


def extract_table(table: Table) -> list[str]:
    """
    Chuyển bảng thành các dòng text.
    Mỗi ô được ngăn cách bởi ký tự ' | '.
    """
    lines: list[str] = []

    for row in table.rows:
        cells = [normalize_line(cell.text) for cell in row.cells]

        # Bỏ các dòng bảng hoàn toàn trống
        if any(cells):
            lines.append(" | ".join(cells))

    return lines


def extract_docx_text(docx_path: Path) -> tuple[str, int, int]:
    """
    Trích xuất text từ DOCX, giữ thứ tự paragraph và table.

    Returns:
        text: Nội dung trích xuất
        paragraph_count: Số paragraph không rỗng
        table_count: Số bảng
    """
    if Document is None:
        return _extract_docx_with_stdlib(docx_path)

    document = Document(docx_path)

    output_lines: list[str] = []
    paragraph_count = 0
    table_count = 0

    for block in iter_block_items(document):
        if isinstance(block, Paragraph):
            line = normalize_line(block.text)

            if line:
                output_lines.append(line)
                paragraph_count += 1
            else:
                # Giữ một dòng trống để bảo toàn ranh giới tương đối
                if output_lines and output_lines[-1] != "":
                    output_lines.append("")

        elif isinstance(block, Table):
            table_lines = extract_table(block)

            if table_lines:
                output_lines.extend(table_lines)
                output_lines.append("")
                table_count += 1

    # Không để quá hai dòng trống liên tiếp
    text = "\n".join(output_lines)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()

    return text, paragraph_count, table_count


_WORD_NS = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def _xml_text(element: ElementTree.Element) -> str:
    """Approximate python-docx's paragraph/cell ``.text`` for OOXML fallback."""
    pieces: list[str] = []
    for node in element.iter():
        if node.tag == f"{_WORD_NS}t" and node.text:
            pieces.append(node.text)
        elif node.tag == f"{_WORD_NS}tab":
            pieces.append("\t")
        elif node.tag in {f"{_WORD_NS}br", f"{_WORD_NS}cr"}:
            pieces.append("\n")
    return "".join(pieces)


def _cell_text(cell: ElementTree.Element) -> str:
    """Match ``python-docx`` by joining a cell's paragraphs with newlines."""
    return "\n".join(
        _xml_text(paragraph)
        for paragraph in cell.findall(f"{_WORD_NS}p")
    )


def _extract_docx_with_stdlib(docx_path: Path) -> tuple[str, int, int]:
    """Offline fallback retaining the legacy paragraph/table serialization."""
    with zipfile.ZipFile(docx_path) as archive:
        root = ElementTree.fromstring(archive.read("word/document.xml"))

    body = root.find(f"{_WORD_NS}body")
    if body is None:
        return "", 0, 0

    output_lines: list[str] = []
    paragraph_count = 0
    table_count = 0

    for block in body:
        if block.tag == f"{_WORD_NS}p":
            line = normalize_line(_xml_text(block))
            if line:
                output_lines.append(line)
                paragraph_count += 1
            elif output_lines and output_lines[-1] != "":
                output_lines.append("")
        elif block.tag == f"{_WORD_NS}tbl":
            table_lines: list[str] = []
            for row in block.findall(f"{_WORD_NS}tr"):
                cells = [
                    normalize_line(_cell_text(cell))
                    for cell in row.findall(f"{_WORD_NS}tc")
                ]
                if any(cells):
                    table_lines.append(" | ".join(cells))
            if table_lines:
                output_lines.extend(table_lines)
                output_lines.append("")
                table_count += 1

    text = re.sub(r"\n{3,}", "\n\n", "\n".join(output_lines)).strip()
    return text, paragraph_count, table_count


def extract_document(docx_path: str | Path) -> tuple[str, int, int]:
    """Public library entry point for legacy-compatible DOCX extraction."""
    return extract_docx_text(Path(docx_path))


def read_registry(registry_path: Path) -> list[dict[str, str]]:
    if not registry_path.exists():
        raise FileNotFoundError(f"Không tìm thấy registry: {registry_path}")

    with registry_path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        required_columns = {
            "document_id",
            "working_docx_path",
            "extraction_method",
        }

        fieldnames = set(reader.fieldnames or [])
        missing_columns = required_columns - fieldnames

        if missing_columns:
            raise ValueError(
                f"documents.csv thiếu các cột: {sorted(missing_columns)}"
            )

        return list(reader)


def resolve_project_path(path_value: str) -> Path:
    path = Path(path_value)

    if path.is_absolute():
        return path

    return PROJECT_ROOT / path
