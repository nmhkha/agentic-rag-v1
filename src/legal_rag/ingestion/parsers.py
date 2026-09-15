from __future__ import annotations

import csv
import json
import re
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[3]

REGISTRY_PATH = (
    PROJECT_ROOT
    / "data"
    / "source_registry"
    / "documents.csv"
)

EXTRACTED_DIRECTORY = (
    PROJECT_ROOT
    / "data"
    / "extracted"
)

PROCESSED_DIRECTORY = (
    PROJECT_ROOT
    / "data"
    / "processed"
)

VALIDATION_DIRECTORY = (
    PROJECT_ROOT
    / "data"
    / "validation"
)

ARTICLES_OUTPUT_PATH = (
    PROCESSED_DIRECTORY
    / "articles.jsonl"
)

REPORT_PATH = (
    VALIDATION_DIRECTORY
    / "parser_report.csv"
)


PART_PATTERN = re.compile(
    r"^\s*Phần(?:\s+thứ)?\s+(.+?)\s*$",
    re.IGNORECASE,
)

CHAPTER_PATTERN = re.compile(
    r"^\s*Chương\s+([IVXLCDM]+|\d+[A-Za-z]?)"
    r"(?:\s*[.:\-–—]\s*(.*))?\s*$",
    re.IGNORECASE,
)

SECTION_PATTERN = re.compile(
    r"^\s*Mục\s+(\d+[A-Za-z]?)"
    r"(?:\s*[.:\-–—]\s*(.*))?\s*$",
    re.IGNORECASE,
)

SUBSECTION_PATTERN = re.compile(
    r"^\s*Tiểu\s+mục\s+(\d+[A-Za-z]?)"
    r"(?:\s*[.:\-–—]\s*(.*))?\s*$",
    re.IGNORECASE,
)

ARTICLE_PATTERN = re.compile(
    r"^\s*Điều\s+(\d+[A-Za-z]?)\s*[.]\s*(.*)\s*$",
    re.IGNORECASE,
)

CLAUSE_PATTERN = re.compile(
    r"^\s*(\d+)\s*[.]\s+(.+?)\s*$",
)

POINT_PATTERN = re.compile(
    r"^\s*([a-zA-ZđĐ])\s*[)]\s+(.+?)\s*$",
)

SUSPICIOUS_STRUCTURE_PATTERN = re.compile(
    r"^\s*(Điều|Chương|Mục|Tiểu\s+mục)\b",
    re.IGNORECASE,
)

APPENDIX_START_PATTERN = re.compile(
    r"^\s*Phụ\s+lục(?:\s+[IVXLCDM]+|\s+\d+)?\s*$",
    re.IGNORECASE,
)


def normalize_line(line: str) -> str:
    line = unicodedata.normalize("NFC", line)
    line = line.replace("\u00a0", " ")
    line = re.sub(r"[ \t]+", " ", line)
    return line.strip()


def join_lines(lines: list[str]) -> str:
    """
    Nối các dòng liên tục bằng khoảng trắng.

    Đây chỉ là biểu diễn text của một đơn vị pháp lý.
    File .cleaned.txt vẫn được giữ nguyên để đối chiếu.
    """
    return re.sub(
        r"\s+",
        " ",
        " ".join(line for line in lines if line),
    ).strip()


def is_probable_heading_title(line: str) -> bool:
    """
    Heuristic bảo thủ để nhận diện tiêu đề nằm ở dòng kế tiếp,
    ví dụ:

        Chương I
        NHỮNG QUY ĐỊNH CHUNG
    """
    if not line or len(line) > 220:
        return False

    if ARTICLE_PATTERN.match(line):
        return False

    if CLAUSE_PATTERN.match(line):
        return False

    if POINT_PATTERN.match(line):
        return False

    letters = [
        char
        for char in line
        if char.isalpha()
    ]

    if not letters:
        return False

    uppercase_ratio = (
        sum(char.isupper() for char in letters)
        / len(letters)
    )

    # Tiêu đề viết hoa toàn bộ hoặc câu ngắn không kết thúc bằng dấu câu.
    return (
        uppercase_ratio >= 0.7
        or (
            len(line.split()) <= 15
            and not re.search(r"[.;:!?]$", line)
        )
    )


@dataclass
class Point:
    number: str
    start_line: int
    text_lines: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "point": self.number.lower(),
            "start_line": self.start_line,
            "text": join_lines(self.text_lines),
        }


@dataclass
class Clause:
    number: str
    start_line: int
    text_lines: list[str] = field(default_factory=list)
    points: list[Point] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "clause": self.number,
            "start_line": self.start_line,
            "text": join_lines(self.text_lines),
            "points": [
                point.to_dict()
                for point in self.points
            ],
        }


@dataclass
class Article:
    document_id: str
    document_number: str
    document_title: str

    number: str
    title: str
    start_line: int

    part_number: str | None
    part_title: str | None

    chapter_number: str | None
    chapter_title: str | None

    section_number: str | None
    section_title: str | None

    subsection_number: str | None
    subsection_title: str | None

    intro_lines: list[str] = field(default_factory=list)
    direct_points: list[Point] = field(default_factory=list)
    clauses: list[Clause] = field(default_factory=list)

    end_line: int | None = None

    def to_dict(self) -> dict[str, Any]:
        article_id = (
            f"{self.document_id}_dieu-{self.number.lower()}"
        )

        return {
            "article_id": article_id,
            "document_id": self.document_id,
            "document_number": self.document_number,
            "document_title": self.document_title,
            "part": self.part_number,
            "part_title": self.part_title,
            "chapter": self.chapter_number,
            "chapter_title": self.chapter_title,
            "section": self.section_number,
            "section_title": self.section_title,
            "subsection": self.subsection_number,
            "subsection_title": self.subsection_title,
            "article": self.number,
            "article_title": self.title,
            "start_line": self.start_line,
            "end_line": self.end_line,
            "intro_text": join_lines(self.intro_lines),
            "direct_points": [
                point.to_dict()
                for point in self.direct_points
            ],
            "clauses": [
                clause.to_dict()
                for clause in self.clauses
            ],
        }


class LegalStructureParser:
    def __init__(
        self,
        document_id: str,
        document_number: str,
        document_title: str,
    ) -> None:
        self.document_id = document_id
        self.document_number = document_number
        self.document_title = document_title

        self.part_number: str | None = None
        self.part_title: str | None = None

        self.chapter_number: str | None = None
        self.chapter_title: str | None = None

        self.section_number: str | None = None
        self.section_title: str | None = None

        self.subsection_number: str | None = None
        self.subsection_title: str | None = None

        self.current_article: Article | None = None
        self.current_clause: Clause | None = None
        self.current_point: Point | None = None

        self.articles: list[Article] = []

        self.pending_heading_type: str | None = None
        self.pending_article_title = False

        self.suspicious_lines: list[tuple[int, str]] = []
        self.preamble_nonempty_lines = 0
        self.appendix_start_line: int | None = None
        self.appendix_excluded_line_count = 0

    def _set_pending_title(
        self,
        heading_type: str,
    ) -> None:
        self.pending_heading_type = heading_type

    def _apply_pending_heading_title(
        self,
        line: str,
    ) -> bool:
        if not self.pending_heading_type:
            return False

        if not is_probable_heading_title(line):
            self.pending_heading_type = None
            return False

        if self.pending_heading_type == "part":
            self.part_title = line
        elif self.pending_heading_type == "chapter":
            self.chapter_title = line
        elif self.pending_heading_type == "section":
            self.section_title = line
        elif self.pending_heading_type == "subsection":
            self.subsection_title = line

        self.pending_heading_type = None
        return True

    def _close_point(self) -> None:
        if self.current_point is None:
            return

        if self.current_clause is not None:
            self.current_clause.points.append(
                self.current_point
            )
        elif self.current_article is not None:
            self.current_article.direct_points.append(
                self.current_point
            )

        self.current_point = None

    def _close_clause(self) -> None:
        self._close_point()

        if (
            self.current_clause is not None
            and self.current_article is not None
        ):
            self.current_article.clauses.append(
                self.current_clause
            )

        self.current_clause = None

    def _close_article(
        self,
        end_line: int,
    ) -> None:
        self._close_clause()

        if self.current_article is None:
            return

        self.current_article.end_line = max(
            self.current_article.start_line,
            end_line,
        )

        self.articles.append(
            self.current_article
        )
        self.current_article = None
        self.pending_article_title = False

    def _start_article(
        self,
        number: str,
        title: str,
        line_number: int,
    ) -> None:
        self._close_article(line_number - 1)

        self.current_article = Article(
            document_id=self.document_id,
            document_number=self.document_number,
            document_title=self.document_title,
            number=number,
            title=title,
            start_line=line_number,
            part_number=self.part_number,
            part_title=self.part_title,
            chapter_number=self.chapter_number,
            chapter_title=self.chapter_title,
            section_number=self.section_number,
            section_title=self.section_title,
            subsection_number=self.subsection_number,
            subsection_title=self.subsection_title,
        )

        self.pending_article_title = not bool(title)

    def _start_clause(
        self,
        number: str,
        text: str,
        line_number: int,
    ) -> None:
        self._close_clause()

        self.current_clause = Clause(
            number=number,
            start_line=line_number,
            text_lines=[text],
        )

    def _start_point(
        self,
        number: str,
        text: str,
        line_number: int,
    ) -> None:
        self._close_point()

        self.current_point = Point(
            number=number,
            start_line=line_number,
            text_lines=[text],
        )

    def _append_body_line(
        self,
        line: str,
    ) -> None:
        if self.current_point is not None:
            self.current_point.text_lines.append(line)
            return

        if self.current_clause is not None:
            self.current_clause.text_lines.append(line)
            return

        if self.current_article is not None:
            self.current_article.intro_lines.append(line)
            return

        self.preamble_nonempty_lines += 1

    def parse(
        self,
        text: str,
    ) -> list[Article]:
        lines = text.splitlines()

        for line_number, raw_line in enumerate(
            lines,
            start=1,
        ):
            line = normalize_line(raw_line)

            # articles.jsonl chỉ mô hình hóa Điều/Khoản/Điểm của phần quy
            # phạm chính. Phụ lục và mẫu biểu có hệ thống đánh số riêng;
            # nếu tiếp tục parse, các số đó bị gắn nhầm vào Điều cuối hoặc
            # tạo lại Điều 1..n. Nội dung nguồn vẫn nguyên vẹn trong
            # .cleaned.txt và vùng bị loại khỏi article parser được báo cáo.
            if self.appendix_start_line is not None:
                if line:
                    self.appendix_excluded_line_count += 1
                continue

            if APPENDIX_START_PATTERN.match(line):
                self._close_article(line_number - 1)
                self.appendix_start_line = line_number
                self.appendix_excluded_line_count = 1
                continue

            if not line:
                continue

            part_match = PART_PATTERN.match(line)
            chapter_match = CHAPTER_PATTERN.match(line)
            section_match = SECTION_PATTERN.match(line)
            subsection_match = SUBSECTION_PATTERN.match(line)
            article_match = ARTICLE_PATTERN.match(line)

            if part_match:
                self._close_article(line_number - 1)

                value = part_match.group(1).strip()
                self.part_number = value
                self.part_title = None

                self.chapter_number = None
                self.chapter_title = None
                self.section_number = None
                self.section_title = None
                self.subsection_number = None
                self.subsection_title = None

                self._set_pending_title("part")
                continue

            if chapter_match:
                self._close_article(line_number - 1)

                self.chapter_number = (
                    chapter_match.group(1).upper()
                )
                inline_title = (
                    chapter_match.group(2) or ""
                ).strip()
                self.chapter_title = inline_title or None

                self.section_number = None
                self.section_title = None
                self.subsection_number = None
                self.subsection_title = None

                if not inline_title:
                    self._set_pending_title("chapter")
                else:
                    self.pending_heading_type = None

                continue

            if section_match:
                self._close_article(line_number - 1)

                self.section_number = (
                    section_match.group(1)
                )
                inline_title = (
                    section_match.group(2) or ""
                ).strip()
                self.section_title = inline_title or None

                self.subsection_number = None
                self.subsection_title = None

                if not inline_title:
                    self._set_pending_title("section")
                else:
                    self.pending_heading_type = None

                continue

            if subsection_match:
                self._close_article(line_number - 1)

                self.subsection_number = (
                    subsection_match.group(1)
                )
                inline_title = (
                    subsection_match.group(2) or ""
                ).strip()
                self.subsection_title = (
                    inline_title or None
                )

                if not inline_title:
                    self._set_pending_title("subsection")
                else:
                    self.pending_heading_type = None

                continue

            if article_match:
                number = article_match.group(1)
                title = article_match.group(2).strip()

                self._start_article(
                    number=number,
                    title=title,
                    line_number=line_number,
                )
                self.pending_heading_type = None
                continue

            if self._apply_pending_heading_title(line):
                continue

            if (
                self.current_article is not None
                and self.pending_article_title
            ):
                if is_probable_heading_title(line):
                    self.current_article.title = line
                    self.pending_article_title = False
                    continue

                self.pending_article_title = False

            if self.current_article is not None:
                clause_match = CLAUSE_PATTERN.match(line)

                if clause_match:
                    self._start_clause(
                        number=clause_match.group(1),
                        text=clause_match.group(2),
                        line_number=line_number,
                    )
                    continue

                point_match = POINT_PATTERN.match(line)

                if point_match:
                    self._start_point(
                        number=point_match.group(1),
                        text=point_match.group(2),
                        line_number=line_number,
                    )
                    continue

            if SUSPICIOUS_STRUCTURE_PATTERN.match(line):
                self.suspicious_lines.append(
                    (line_number, line)
                )

            self._append_body_line(line)

        self._close_article(len(lines))

        return self.articles


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
            "document_number",
            "document_title",
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


def natural_article_key(
    article_number: str,
) -> tuple[int, str]:
    match = re.match(
        r"^(\d+)([A-Za-z]?)$",
        article_number,
    )

    if not match:
        return (10**9, article_number)

    return (
        int(match.group(1)),
        match.group(2).lower(),
    )


def find_duplicate_articles(
    articles: list[Article],
) -> list[str]:
    counts: dict[str, int] = {}

    for article in articles:
        counts[article.number] = (
            counts.get(article.number, 0) + 1
        )

    return sorted(
        number
        for number, count in counts.items()
        if count > 1
    )


def find_numeric_article_gaps(
    articles: list[Article],
) -> list[str]:
    """
    Chỉ kiểm tra chuỗi Điều thuần số.
    Các Điều như 10a, 10b không bị xem là lỗi.
    """
    numeric_numbers = sorted(
        {
            int(article.number)
            for article in articles
            if article.number.isdigit()
        }
    )

    if len(numeric_numbers) < 2:
        return []

    present = set(numeric_numbers)
    gaps: list[str] = []

    for number in range(
        numeric_numbers[0],
        numeric_numbers[-1] + 1,
    ):
        if number not in present:
            gaps.append(str(number))

    return gaps


def parse_legal_structure(
    text: str,
    *,
    document_id: str,
    document_number: str,
    document_title: str,
) -> list[Article]:
    """Parse cleaned text with the unchanged legacy hierarchy rules."""
    parser = LegalStructureParser(
        document_id=document_id,
        document_number=document_number,
        document_title=document_title,
    )
    return parser.parse(text)
