"""Deterministic navigation over the frozen corpus-v2.1 legal structure."""

from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any, Iterable

from .paths import CORPUS_VERSION_DIR


CORPUS_ROOT = CORPUS_VERSION_DIR
CORPUS_MANIFEST_PATH = CORPUS_ROOT / "corpus_manifest.json"
SOURCES_PATH = CORPUS_ROOT / "registry" / "sources.json"
ARTICLES_PATH = CORPUS_ROOT / "articles" / "articles.jsonl"
CHUNKS_PATH = CORPUS_ROOT / "chunks" / "chunks.jsonl"

EXPECTED_CORPUS_VERSION = "corpus-v2.1"
EXPECTED_CORPUS_FINGERPRINT = (
    "93eb407ca67d567e6d3d92cb1a36e7b164fa4f96b11d8634ed94a66a88a5fb0f"
)
EXPECTED_CHUNKS_SHA256 = (
    "ab5103cf4469b5c5ae0b1462c6998308bd4fc1e46bc54ac66071c99a2ee08f98"
)
EXPECTED_SOURCE_COUNT = 17
EXPECTED_ARTICLE_COUNT = 945
EXPECTED_CHUNK_COUNT = 6122

DOCUMENT_ARTICLE_LIST = "DOCUMENT_ARTICLE_LIST"
DOCUMENT_ARTICLE_COUNT = "DOCUMENT_ARTICLE_COUNT"
ARTICLE_CLAUSE_LIST = "ARTICLE_CLAUSE_LIST"
CLAUSE_POINT_LIST = "CLAUSE_POINT_LIST"
NOT_NAVIGATION = "NOT_NAVIGATION"

SUCCESS = "SUCCESS"
DOCUMENT_NOT_FOUND = "DOCUMENT_NOT_FOUND"
DOCUMENT_AMBIGUOUS = "DOCUMENT_AMBIGUOUS"
ARTICLE_NOT_FOUND = "ARTICLE_NOT_FOUND"
CLAUSE_NOT_FOUND = "CLAUSE_NOT_FOUND"


@dataclass(frozen=True)
class NavigationRequest:
    intent: str
    document_reference: str | None = None
    article: str | None = None
    clause: str | None = None


@dataclass(frozen=True)
class DocumentCandidate:
    document_id: str
    document_number: str
    document_title: str


@dataclass(frozen=True)
class NavigationItem:
    canonical_id: str
    number: str
    label: str
    title: str | None = None
    text: str | None = None


@dataclass(frozen=True)
class NavigationResult:
    handled: bool
    intent: str
    status: str
    document_id: str | None = None
    document_number: str | None = None
    document_title: str | None = None
    article: str | None = None
    clause: str | None = None
    items: tuple[NavigationItem, ...] = ()
    count: int = 0
    message: str = ""
    candidates: tuple[DocumentCandidate, ...] = ()


_ARTICLE_ID = r"[0-9]+[a-zA-Z]?"
_CLAUSE_ID = r"[0-9]+[a-zA-Z]?"
_END = r"\s*[?.!。]*\s*$"

_POINT_LIST = re.compile(
    rf"^liệt\s+kê\s+các\s+điểm\s+(?:của|trong|thuộc)\s+khoản\s+(?P<clause>{_CLAUSE_ID})"
    rf"\s+(?:(?:của|trong|thuộc)\s+)?điều\s+(?P<article>{_ARTICLE_ID})\s+(?:(?:của|trong|thuộc)\s+)?(?P<document>.+?){_END}",
    re.IGNORECASE,
)
_CLAUSE_LIST = re.compile(
    rf"^liệt\s+kê\s+các\s+khoản\s+(?:của|trong|thuộc)\s+điều\s+(?P<article>{_ARTICLE_ID})"
    rf"\s+(?:(?:của|trong|thuộc)\s+)?(?P<document>.+?){_END}",
    re.IGNORECASE,
)
_CLAUSE_QUESTION = re.compile(
    rf"^điều\s+(?P<article>{_ARTICLE_ID})\s+(?:của|trong|thuộc)\s+(?P<document>.+?)"
    rf"\s+có\s+(?:những\s+)?khoản\s+nào{_END}",
    re.IGNORECASE,
)
_ARTICLE_COUNT = re.compile(
    rf"^(?P<document>.+?)\s+có\s+bao\s+nhiêu\s+điều{_END}", re.IGNORECASE
)
_ARTICLE_LIST = re.compile(
    rf"^liệt\s+kê\s+các\s+(?:điều(?:\s+khoản)?|khoản)\s+(?:của|trong|thuộc)\s+(?P<document>.+?){_END}",
    re.IGNORECASE,
)


def _normalize_query(value: str) -> str:
    value = unicodedata.normalize("NFC", value)
    value = value.translate(str.maketrans({"“": '"', "”": '"', "‘": "'", "’": "'"}))
    return re.sub(r"\s+", " ", value).strip()


def _clean_reference(value: str) -> str:
    return value.strip().strip(" \t\r\n,;:.?!\"'")


def detect_navigation(query: str) -> NavigationRequest:
    """Recognize only the four deliberately narrow Vietnamese navigation forms."""
    normalized = _normalize_query(query)
    for pattern, intent in (
        (_POINT_LIST, CLAUSE_POINT_LIST),
        (_CLAUSE_LIST, ARTICLE_CLAUSE_LIST),
        (_CLAUSE_QUESTION, ARTICLE_CLAUSE_LIST),
        (_ARTICLE_COUNT, DOCUMENT_ARTICLE_COUNT),
        (_ARTICLE_LIST, DOCUMENT_ARTICLE_LIST),
    ):
        match = pattern.fullmatch(normalized)
        if match is None:
            continue
        groups = match.groupdict()
        return NavigationRequest(
            intent=intent,
            document_reference=_clean_reference(groups["document"]),
            article=groups.get("article"),
            clause=groups.get("clause"),
        )
    return NavigationRequest(intent=NOT_NAVIGATION)


def _normalize_title(value: Any) -> str:
    value = unicodedata.normalize("NFC", str(value or "")).casefold()
    value = re.sub(r"[^0-9a-zà-ỹđ]+", " ", value, flags=re.IGNORECASE)
    return re.sub(r"\s+", " ", value).strip()


def _ascii_key(value: Any) -> str:
    value = unicodedata.normalize("NFD", str(value or "")).casefold().replace("đ", "d")
    value = "".join(character for character in value if not unicodedata.combining(character))
    return re.sub(r"[^0-9a-z]", "", value)


_NUMBER_IN_REFERENCE = re.compile(
    r"(?<!\d)(\d{1,4}\s*[/.-]\s*(?:\d{4}\s*[/.-]\s*)?[A-Za-zÀ-ỹĐđ0-9-]+)",
    re.IGNORECASE,
)


def _number_reference_key(reference: str) -> str | None:
    match = _NUMBER_IN_REFERENCE.search(reference)
    return _ascii_key(match.group(1)) if match else None


_VIETNAMESE_ORDER = {character: index for index, character in enumerate(
    "aăâbcdđeêghiklmnoôơpqrstuưvxy", start=1
)}


def legal_number_key(value: Any) -> tuple[Any, ...]:
    """Natural ordering for identifiers such as 2, 10, 10a and a, đ, e."""
    normalized = unicodedata.normalize("NFC", str(value or "")).casefold().strip()
    match = re.fullmatch(r"(\d+)(.*)", normalized)
    if match:
        suffix = tuple(_VIETNAMESE_ORDER.get(char, 1000 + ord(char)) for char in match.group(2))
        return (0, int(match.group(1)), suffix)
    letters = tuple(_VIETNAMESE_ORDER.get(char, 1000 + ord(char)) for char in normalized)
    return (1, letters)


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as handle:
        for line_number, raw_line in enumerate(handle, 1):
            if not raw_line.strip():
                continue
            try:
                row = json.loads(raw_line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON in {path} at line {line_number}: {exc}") from exc
            if not isinstance(row, dict):
                raise ValueError(f"Expected JSON object in {path} at line {line_number}")
            rows.append(row)
    return rows


def _load_frozen_records() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    manifest = json.loads(CORPUS_MANIFEST_PATH.read_text(encoding="utf-8"))
    expected = {
        "corpus_version": EXPECTED_CORPUS_VERSION,
        "status": "FROZEN",
        "source_count": EXPECTED_SOURCE_COUNT,
        "article_count": EXPECTED_ARTICLE_COUNT,
        "chunk_count": EXPECTED_CHUNK_COUNT,
        "corpus_fingerprint_sha256": EXPECTED_CORPUS_FINGERPRINT,
        "chunks_sha256": EXPECTED_CHUNKS_SHA256,
    }
    mismatches = [
        f"{key}={manifest.get(key)!r}" for key, value in expected.items()
        if manifest.get(key) != value
    ]
    if mismatches:
        raise RuntimeError(f"Frozen {EXPECTED_CORPUS_VERSION} identity mismatch: " + ", ".join(mismatches))
    if _sha256(ARTICLES_PATH) != manifest.get("articles_sha256"):
        raise RuntimeError(f"Frozen {EXPECTED_CORPUS_VERSION} articles SHA-256 mismatch")
    if _sha256(SOURCES_PATH) != manifest.get("resolved_registry_sha256"):
        raise RuntimeError(f"Frozen {EXPECTED_CORPUS_VERSION} source registry SHA-256 mismatch")

    source_payload = json.loads(SOURCES_PATH.read_text(encoding="utf-8"))
    documents = source_payload.get("documents")
    if not isinstance(documents, list) or len(documents) != EXPECTED_SOURCE_COUNT:
        raise RuntimeError(f"Frozen {EXPECTED_CORPUS_VERSION} source registry count mismatch")
    articles = _load_jsonl(ARTICLES_PATH)
    if len(articles) != EXPECTED_ARTICLE_COUNT:
        raise RuntimeError(f"Frozen {EXPECTED_CORPUS_VERSION} article count mismatch")
    return documents, articles


class DocumentNavigator:
    """Resolve documents and enumerate their legal structure without retrieval."""

    def __init__(
        self,
        documents: Iterable[dict[str, Any]],
        articles: Iterable[dict[str, Any]],
    ) -> None:
        self.documents = tuple(dict(document) for document in documents)
        self.articles = tuple(dict(article) for article in articles)

    @classmethod
    def from_frozen_corpus(cls) -> "DocumentNavigator":
        documents, articles = _load_frozen_records()
        return cls(documents, articles)

    @staticmethod
    def _candidate(document: dict[str, Any]) -> DocumentCandidate:
        return DocumentCandidate(
            document_id=str(document.get("document_id", "")),
            document_number=str(document.get("document_number", "")),
            document_title=str(document.get("title") or document.get("document_title") or ""),
        )

    @staticmethod
    def _aliases(document: dict[str, Any]) -> tuple[str, ...]:
        aliases: list[str] = []
        for key in ("aliases", "canonical_aliases"):
            value = document.get(key, [])
            if isinstance(value, str):
                aliases.append(value)
            elif isinstance(value, list):
                aliases.extend(str(item) for item in value if item)
        return tuple(aliases)

    def resolve_document(
        self, reference: str
    ) -> tuple[dict[str, Any] | None, tuple[DocumentCandidate, ...]]:
        number_key = _number_reference_key(reference)
        if number_key:
            exact_number = [
                item for item in self.documents
                if _ascii_key(item.get("document_number")) == number_key
                or _ascii_key(item.get("document_id")) == number_key
            ]
            if len(exact_number) == 1:
                return exact_number[0], ()
            if len(exact_number) > 1:
                return None, tuple(self._candidate(item) for item in exact_number)

        normalized = _normalize_title(reference)
        exact_title = [
            item for item in self.documents
            if _normalize_title(item.get("title") or item.get("document_title")) == normalized
        ]
        if len(exact_title) == 1:
            return exact_title[0], ()
        if len(exact_title) > 1:
            return None, tuple(self._candidate(item) for item in exact_title)

        exact_alias = [
            item for item in self.documents
            if normalized in {_normalize_title(alias) for alias in self._aliases(item)}
        ]
        if len(exact_alias) == 1:
            return exact_alias[0], ()
        if len(exact_alias) > 1:
            return None, tuple(self._candidate(item) for item in exact_alias)

        if len(normalized) < 6:
            return None, ()
        substring = []
        for item in self.documents:
            names = [item.get("title"), item.get("document_title"), item.get("official_title")]
            names.extend(self._aliases(item))
            normalized_names = [_normalize_title(name) for name in names if name]
            if any(normalized in name or name in normalized for name in normalized_names):
                substring.append(item)
        if len(substring) == 1:
            return substring[0], ()
        return None, tuple(self._candidate(item) for item in substring)

    def navigate(self, query: str) -> NavigationResult:
        request = detect_navigation(query)
        if request.intent == NOT_NAVIGATION:
            return NavigationResult(False, NOT_NAVIGATION, NOT_NAVIGATION)

        document, candidates = self.resolve_document(request.document_reference or "")
        if document is None:
            if candidates:
                choices = "; ".join(
                    f"{item.document_title} ({item.document_number})" for item in candidates
                )
                return NavigationResult(
                    True, request.intent, DOCUMENT_AMBIGUOUS,
                    article=request.article, clause=request.clause,
                    candidates=candidates,
                    message=f"Không thể xác định duy nhất văn bản. Các ứng viên: {choices}",
                )
            return NavigationResult(
                True, request.intent, DOCUMENT_NOT_FOUND,
                article=request.article, clause=request.clause,
                message=f"Không tìm thấy văn bản: {request.document_reference}",
            )

        document_id = str(document["document_id"])
        document_number = str(document["document_number"])
        document_title = str(document.get("title") or document.get("document_title"))
        base = {
            "handled": True,
            "intent": request.intent,
            "document_id": document_id,
            "document_number": document_number,
            "document_title": document_title,
            "article": request.article,
            "clause": request.clause,
        }
        document_articles = self._document_articles(document_id)

        if request.intent in (DOCUMENT_ARTICLE_LIST, DOCUMENT_ARTICLE_COUNT):
            items = tuple(self._article_item(article) for article in document_articles)
            if request.intent == DOCUMENT_ARTICLE_COUNT:
                message = f"{document_title} ({document_number}) có {len(items)} điều."
            else:
                lines = [f"{document_title} ({document_number}) gồm {len(items)} điều:", ""]
                lines.extend(item.label for item in items)
                message = "\n".join(lines)
            return NavigationResult(
                **base, status=SUCCESS, items=items, count=len(items), message=message
            )

        article = next(
            (item for item in document_articles
             if _normalize_identifier(item.get("article_number") or item.get("article"))
             == _normalize_identifier(request.article)),
            None,
        )
        if article is None:
            return NavigationResult(
                **base, status=ARTICLE_NOT_FOUND,
                message=f"Không tìm thấy Điều {request.article} trong {document_title} ({document_number}).",
            )

        if request.intent == ARTICLE_CLAUSE_LIST:
            items = self._clause_items(article)
            heading = self._article_item(article).label
            lines = [heading, ""]
            lines.extend(item.label for item in items)
            return NavigationResult(
                **base, status=SUCCESS, items=items, count=len(items), message="\n".join(lines)
            )

        clauses = self._unique_sorted(article.get("clauses", []), "clause")
        clause = next(
            (item for item in clauses
             if _normalize_identifier(item.get("clause")) == _normalize_identifier(request.clause)),
            None,
        )
        if clause is None:
            return NavigationResult(
                **base, status=CLAUSE_NOT_FOUND,
                message=(f"Không tìm thấy khoản {request.clause} của Điều {request.article} "
                         f"trong {document_title} ({document_number})."),
            )
        article_id = str(article["article_id"])
        points = self._unique_sorted(clause.get("points", []), "point")
        items = tuple(
            NavigationItem(
                canonical_id=f"{article_id}_khoan-{request.clause}_diem-{point['point']}",
                number=str(point["point"]),
                label=f"Điểm {point['point']}) {str(point.get('text', '')).strip()}".rstrip(),
                text=str(point.get("text", "")).strip(),
            )
            for point in points
        )
        return NavigationResult(
            **base, status=SUCCESS, items=items, count=len(items),
            message="\n".join(item.label for item in items),
        )

    def _document_articles(self, document_id: str) -> tuple[dict[str, Any], ...]:
        records = [item for item in self.articles if item.get("document_id") == document_id]
        unique: dict[str, dict[str, Any]] = {}
        for item in records:
            unique.setdefault(str(item.get("article_id", "")), item)
        return tuple(sorted(
            unique.values(),
            key=lambda item: legal_number_key(item.get("article_number") or item.get("article")),
        ))

    @staticmethod
    def _unique_sorted(records: Any, key: str) -> tuple[dict[str, Any], ...]:
        if not isinstance(records, list):
            return ()
        unique: dict[str, dict[str, Any]] = {}
        for item in records:
            if isinstance(item, dict) and item.get(key) not in (None, ""):
                unique.setdefault(_normalize_identifier(item[key]), item)
        return tuple(sorted(unique.values(), key=lambda item: legal_number_key(item[key])))

    @staticmethod
    def _article_item(article: dict[str, Any]) -> NavigationItem:
        number = str(article.get("article_number") or article.get("article"))
        title = str(article.get("article_title") or "").strip() or None
        label = f"Điều {number}" + (f". {title}" if title else "")
        return NavigationItem(
            canonical_id=str(article["article_id"]), number=number,
            label=label, title=title,
        )

    def _clause_items(self, article: dict[str, Any]) -> tuple[NavigationItem, ...]:
        article_id = str(article["article_id"])
        items = []
        for clause in self._unique_sorted(article.get("clauses", []), "clause"):
            number = str(clause["clause"])
            text = str(clause.get("text", "")).strip()
            lines = [f"Khoản {number}. {text}".rstrip()]
            for point in self._unique_sorted(clause.get("points", []), "point"):
                lines.append(f"{point['point']}) {str(point.get('text', '')).strip()}".rstrip())
            items.append(NavigationItem(
                canonical_id=f"{article_id}_khoan-{number}",
                number=number,
                label="\n".join(lines),
                text="\n".join(lines[1:]) if len(lines) > 1 else text,
            ))
        return tuple(items)


def _normalize_identifier(value: Any) -> str:
    return unicodedata.normalize("NFC", str(value or "")).casefold().strip()


@lru_cache(maxsize=1)
def frozen_document_navigator() -> DocumentNavigator:
    return DocumentNavigator.from_frozen_corpus()


def try_document_navigation(
    query: str, navigator: DocumentNavigator | None = None
) -> NavigationResult:
    """Try navigation without loading corpus assets for ordinary RAG queries."""
    request = detect_navigation(query)
    if request.intent == NOT_NAVIGATION:
        return NavigationResult(False, NOT_NAVIGATION, NOT_NAVIGATION)
    return (navigator or frozen_document_navigator()).navigate(query)


__all__ = [
    "ARTICLE_CLAUSE_LIST", "ARTICLE_NOT_FOUND", "CLAUSE_NOT_FOUND",
    "CLAUSE_POINT_LIST", "DOCUMENT_AMBIGUOUS", "DOCUMENT_ARTICLE_COUNT",
    "DOCUMENT_ARTICLE_LIST", "DOCUMENT_NOT_FOUND", "DocumentCandidate",
    "DocumentNavigator", "NavigationItem", "NavigationRequest", "NavigationResult",
    "NOT_NAVIGATION", "SUCCESS", "detect_navigation", "frozen_document_navigator",
    "legal_number_key", "try_document_navigation", "CHUNKS_PATH",
]
