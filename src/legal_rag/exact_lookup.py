"""Deterministic exact legal-provision lookup over frozen corpus-v0.2."""

from __future__ import annotations

import json
import re
import unicodedata
from dataclasses import dataclass
from functools import lru_cache
from typing import Any, Iterable

from .navigation import (
    ARTICLE_NOT_FOUND,
    CLAUSE_NOT_FOUND,
    DOCUMENT_AMBIGUOUS,
    DOCUMENT_NOT_FOUND,
    SUCCESS,
    CHUNKS_PATH,
    DocumentCandidate,
    DocumentNavigator,
    EXPECTED_CHUNK_COUNT,
    _load_jsonl,
    _normalize_identifier,
    _sha256,
    frozen_document_navigator,
    legal_number_key,
)


EXACT_LEGAL_LOOKUP = "EXACT_LEGAL_LOOKUP"
EXACT_ARTICLE_LOOKUP = "EXACT_ARTICLE_LOOKUP"
EXACT_CLAUSE_LOOKUP = "EXACT_CLAUSE_LOOKUP"
EXACT_POINT_LOOKUP = "EXACT_POINT_LOOKUP"
NOT_EXACT_LOOKUP = "NOT_EXACT_LOOKUP"
POINT_NOT_FOUND = "POINT_NOT_FOUND"


@dataclass(frozen=True)
class ExactLookupRequest:
    intent: str
    document_reference: str | None = None
    article: str | None = None
    clause: str | None = None
    point: str | None = None


@dataclass(frozen=True)
class ExactLookupResult:
    handled: bool
    route: str
    intent: str
    status: str
    document_id: str | None = None
    document_number: str | None = None
    document_title: str | None = None
    article: str | None = None
    clause: str | None = None
    point: str | None = None
    content: str = ""
    message: str = ""
    candidates: tuple[DocumentCandidate, ...] = ()
    retrieval_call_count: int = 0
    llm_call_count: int = 0


_ARTICLE_ID = r"[0-9]+[a-zA-Z]?"
_CLAUSE_ID = r"[0-9]+[a-zA-Z]?"
_POINT_ID = r"[a-zA-Zà-ỹÀ-ỸđĐ]"
_END = r"\s*[?.!。]*\s*$"
_DIRECT_SUFFIX = r"(?:quy\s+định\s+gì|có\s+nội\s+dung\s+gì|nội\s+dung\s+(?:là\s+)?gì)"
_DIRECT_PREFIX = r"(?:(?:cho\s+tôi|xin)\s+(?:biết\s+)?(?:nội\s+dung\s+)?|nội\s+dung\s+)"
_LEGAL_DOCUMENT = r"(?:luật|bộ\s+luật|nghị\s+định|thông\s+tư|quyết\s+định|pháp\s+lệnh|hiến\s+pháp)\b.+"
_DOCUMENT_NUMBER = r"\d{1,4}\s*[/.-]\s*(?:\d{4}\s*[/.-]\s*)?[A-Za-zÀ-ỹĐđ0-9-]+"

_BASES = (
    (
        EXACT_POINT_LOOKUP,
        rf"điểm\s+(?P<point>{_POINT_ID})\s+khoản\s+(?P<clause>{_CLAUSE_ID})"
        rf"\s+điều\s+(?P<article>{_ARTICLE_ID})",
    ),
    (
        EXACT_CLAUSE_LOOKUP,
        rf"khoản\s+(?P<clause>{_CLAUSE_ID})\s+điều\s+(?P<article>{_ARTICLE_ID})",
    ),
    (EXACT_ARTICLE_LOOKUP, rf"điều\s+(?P<article>{_ARTICLE_ID})"),
)


def _normalize_query(value: str) -> str:
    value = unicodedata.normalize("NFC", value)
    value = value.translate(str.maketrans({"“": '"', "”": '"', "‘": "'", "’": "'"}))
    return re.sub(r"\s+", " ", value).strip()


def _clean_reference(value: str) -> str:
    return value.strip().strip(" \t\r\n,;:.?!\"'")


def detect_exact_lookup(query: str) -> ExactLookupRequest:
    """Recognize narrow direct-content requests, never semantic legal questions."""
    normalized = _normalize_query(query)
    for intent, base in _BASES:
        patterns = (
            rf"^{_DIRECT_PREFIX}{base}\s+(?:(?:của|trong|thuộc)\s+)?(?P<document>.+?){_END}",
            rf"^{base}\s+(?:(?:của|trong|thuộc)\s+)?(?P<document>.+?)\s+{_DIRECT_SUFFIX}{_END}",
            rf"^{base}\s+(?:của|trong|thuộc)\s+(?P<document>(?:{_LEGAL_DOCUMENT}|{_DOCUMENT_NUMBER})){_END}",
        )
        for raw_pattern in patterns:
            match = re.fullmatch(raw_pattern, normalized, flags=re.IGNORECASE)
            if match is None:
                continue
            groups = match.groupdict()
            return ExactLookupRequest(
                intent=intent,
                document_reference=_clean_reference(groups["document"]),
                article=groups.get("article"),
                clause=groups.get("clause"),
                point=groups.get("point"),
            )
    return ExactLookupRequest(intent=NOT_EXACT_LOOKUP)


class ExactProvisionLookup:
    """Resolve and render exact provisions from canonical corpus hierarchy."""

    def __init__(
        self,
        navigator: DocumentNavigator,
        articles: Iterable[dict[str, Any]],
        chunks: Iterable[dict[str, Any]],
    ) -> None:
        self.navigator = navigator
        self.articles = tuple(dict(article) for article in articles)
        self.chunks = tuple(dict(chunk) for chunk in chunks)
        by_article: dict[str, list[dict[str, Any]]] = {}
        for chunk in self.chunks:
            by_article.setdefault(str(chunk.get("article_id", "")), []).append(chunk)
        self._chunks_by_article = {
            key: self._deduplicate_chunks(value) for key, value in by_article.items()
        }

    @staticmethod
    def _deduplicate_chunks(
        chunks: Iterable[dict[str, Any]],
    ) -> tuple[dict[str, Any], ...]:
        unique: dict[tuple[str, str, str, str], dict[str, Any]] = {}
        for chunk in chunks:
            key = (
                str(chunk.get("canonical_chunk_id") or chunk.get("chunk_id") or ""),
                _normalize_identifier(chunk.get("clause") or chunk.get("clause_number")),
                _normalize_identifier(chunk.get("point") or chunk.get("point_number")),
                str(chunk.get("text") or "").strip(),
            )
            unique.setdefault(key, chunk)
        return tuple(sorted(
            unique.values(),
            key=lambda item: (
                int(item.get("source_start_line") or 0),
                legal_number_key(item.get("clause") or item.get("clause_number")),
                legal_number_key(item.get("point") or item.get("point_number")),
                str(item.get("canonical_chunk_id") or item.get("chunk_id") or ""),
            ),
        ))

    def lookup(self, query: str) -> ExactLookupResult:
        request = detect_exact_lookup(query)
        if request.intent == NOT_EXACT_LOOKUP:
            return ExactLookupResult(False, EXACT_LEGAL_LOOKUP, request.intent, NOT_EXACT_LOOKUP)

        document, candidates = self.navigator.resolve_document(request.document_reference or "")
        if document is None:
            if candidates:
                choices = "; ".join(
                    f"{item.document_title} ({item.document_number})" for item in candidates
                )
                return self._result(
                    request, DOCUMENT_AMBIGUOUS, candidates=candidates,
                    message=f"Không thể xác định duy nhất văn bản. Các ứng viên: {choices}",
                )
            return self._result(
                request, DOCUMENT_NOT_FOUND,
                message=f"Không tìm thấy văn bản: {request.document_reference}",
            )

        document_id = str(document.get("document_id", ""))
        article = next(
            (
                item for item in self.articles
                if str(item.get("document_id", "")) == document_id
                and _normalize_identifier(item.get("article_number") or item.get("article"))
                == _normalize_identifier(request.article)
            ),
            None,
        )
        document_fields = {
            "document_id": document_id,
            "document_number": str(document.get("document_number", "")),
            "document_title": str(document.get("title") or document.get("document_title") or ""),
        }
        if article is None:
            return self._result(
                request, ARTICLE_NOT_FOUND, **document_fields,
                message=(f"Không tìm thấy Điều {request.article} trong "
                         f"{document_fields['document_title']} ({document_fields['document_number']})."),
            )

        # Materialize all canonical chunks for the Article before selecting a subtree.
        # Leaf text is taken from these chunks where available; hierarchy introductions
        # come from the verified Article record because they are parent metadata.
        article_chunks = self._chunks_by_article.get(str(article.get("article_id", "")), ())
        structure = self._structure(article, article_chunks)
        content: str
        if request.intent == EXACT_ARTICLE_LOOKUP:
            content = self._render_article(document_fields, article, structure)
        else:
            clause = next(
                (item for item in structure["clauses"]
                 if _normalize_identifier(item["clause"]) == _normalize_identifier(request.clause)),
                None,
            )
            if clause is None:
                return self._result(
                    request, CLAUSE_NOT_FOUND, **document_fields,
                    message=(f"Không tìm thấy khoản {request.clause} của Điều {request.article} "
                             f"trong {document_fields['document_title']} "
                             f"({document_fields['document_number']})."),
                )
            if request.intent == EXACT_CLAUSE_LOOKUP:
                content = self._render_clause(document_fields, article, clause)
            else:
                point = next(
                    (item for item in clause["points"]
                     if _normalize_identifier(item["point"]) == _normalize_identifier(request.point)),
                    None,
                )
                if point is None:
                    return self._result(
                        request, POINT_NOT_FOUND, **document_fields,
                        message=(f"Không tìm thấy điểm {request.point} khoản {request.clause} "
                                 f"Điều {request.article} trong {document_fields['document_title']} "
                                 f"({document_fields['document_number']})."),
                    )
                content = self._render_point(document_fields, article, clause, point)

        return self._result(
            request, SUCCESS, content=content, message=content, **document_fields
        )

    @staticmethod
    def _result(
        request: ExactLookupRequest,
        status: str,
        **kwargs: Any,
    ) -> ExactLookupResult:
        return ExactLookupResult(
            handled=True,
            route=EXACT_LEGAL_LOOKUP,
            intent=request.intent,
            status=status,
            article=request.article,
            clause=request.clause,
            point=request.point,
            **kwargs,
        )

    @staticmethod
    def _structure(
        article: dict[str, Any], article_chunks: Iterable[dict[str, Any]]
    ) -> dict[str, Any]:
        chunk_text: dict[tuple[str, str], str] = {}
        article_text = ""
        for chunk in article_chunks:
            level = str(chunk.get("chunk_level") or "")
            text = str(chunk.get("text") or "").strip()
            clause = _normalize_identifier(chunk.get("clause") or chunk.get("clause_number"))
            point = _normalize_identifier(chunk.get("point") or chunk.get("point_number"))
            if level == "point" and clause and point:
                chunk_text.setdefault((clause, point), text)
            elif level == "clause" and clause:
                chunk_text.setdefault((clause, ""), text)
            elif level in {"article", "article_intro"}:
                article_text = article_text or text

        clauses: dict[str, dict[str, Any]] = {}
        raw_clauses = article.get("clauses")
        if isinstance(raw_clauses, list):
            for raw_clause in raw_clauses:
                if not isinstance(raw_clause, dict) or raw_clause.get("clause") in (None, ""):
                    continue
                number = str(raw_clause["clause"])
                key = _normalize_identifier(number)
                clause = clauses.setdefault(key, {
                    "clause": number,
                    "text": str(raw_clause.get("text") or "").strip(),
                    "points": [],
                })
                raw_points = raw_clause.get("points")
                if isinstance(raw_points, list):
                    seen_points: set[str] = set()
                    for raw_point in raw_points:
                        if not isinstance(raw_point, dict) or raw_point.get("point") in (None, ""):
                            continue
                        point_number = str(raw_point["point"])
                        point_key = _normalize_identifier(point_number)
                        if point_key in seen_points:
                            continue
                        seen_points.add(point_key)
                        clause["points"].append({
                            "point": point_number,
                            "text": chunk_text.get(
                                (key, point_key), str(raw_point.get("text") or "").strip()
                            ),
                        })
                clause["points"].sort(key=lambda item: legal_number_key(item["point"]))

        # Supplement leaf-only synthetic records from chunks without duplicating parents.
        for (clause_key, point_key), text in chunk_text.items():
            if not clause_key:
                continue
            clause = clauses.setdefault(clause_key, {
                "clause": clause_key,
                "text": chunk_text.get((clause_key, ""), ""),
                "points": [],
            })
            if point_key and not any(
                _normalize_identifier(item["point"]) == point_key for item in clause["points"]
            ):
                clause["points"].append({"point": point_key, "text": text})
                clause["points"].sort(key=lambda item: legal_number_key(item["point"]))

        intro = str(article.get("intro_text") or "").strip() or article_text
        return {
            "intro_text": intro,
            "clauses": sorted(clauses.values(), key=lambda item: legal_number_key(item["clause"])),
        }

    @staticmethod
    def _document_heading(document: dict[str, str]) -> str:
        return f"{document['document_title']} ({document['document_number']})"

    @staticmethod
    def _article_heading(article: dict[str, Any]) -> str:
        number = str(article.get("article_number") or article.get("article") or "")
        title = str(article.get("article_title") or "").strip()
        return f"Điều {number}" + (f". {title}" if title else "")

    @classmethod
    def _render_article(
        cls, document: dict[str, str], article: dict[str, Any], structure: dict[str, Any]
    ) -> str:
        lines = [cls._document_heading(document), "", cls._article_heading(article)]
        if structure["intro_text"]:
            lines.extend(("", structure["intro_text"]))
        for clause in structure["clauses"]:
            lines.extend(("", cls._clause_body(clause)))
        return "\n".join(lines)

    @classmethod
    def _render_clause(
        cls, document: dict[str, str], article: dict[str, Any], clause: dict[str, Any]
    ) -> str:
        return "\n".join((
            cls._document_heading(document), "", cls._article_heading(article), "",
            cls._clause_body(clause),
        ))

    @classmethod
    def _render_point(
        cls,
        document: dict[str, str],
        article: dict[str, Any],
        clause: dict[str, Any],
        point: dict[str, Any],
    ) -> str:
        article_number = str(article.get("article_number") or article.get("article") or "")
        return "\n".join((
            cls._document_heading(document),
            f"Điểm {point['point']} khoản {clause['clause']} Điều {article_number}",
            "",
            f"{point['point']}) {point['text']}".rstrip(),
        ))

    @staticmethod
    def _clause_body(clause: dict[str, Any]) -> str:
        lines = [f"Khoản {clause['clause']}. {clause['text']}".rstrip()]
        lines.extend(f"{point['point']}) {point['text']}".rstrip() for point in clause["points"])
        return "\n".join(lines)


@lru_cache(maxsize=1)
def frozen_exact_lookup() -> ExactProvisionLookup:
    navigator = frozen_document_navigator()
    chunks = _load_jsonl(CHUNKS_PATH)
    if len(chunks) != EXPECTED_CHUNK_COUNT:
        raise RuntimeError("Frozen corpus-v0.2 chunk count mismatch")
    manifest = json.loads((CHUNKS_PATH.parent.parent / "corpus_manifest.json").read_text(encoding="utf-8"))
    if _sha256(CHUNKS_PATH) != manifest.get("chunks_sha256"):
        raise RuntimeError("Frozen corpus-v0.2 chunks SHA-256 mismatch")
    return ExactProvisionLookup(navigator, navigator.articles, chunks)


def try_exact_lookup(
    query: str,
    navigator: DocumentNavigator | None = None,
    lookup: ExactProvisionLookup | None = None,
) -> ExactLookupResult:
    """Try exact lookup without loading corpus assets for ordinary RAG queries."""
    request = detect_exact_lookup(query)
    if request.intent == NOT_EXACT_LOOKUP:
        return ExactLookupResult(False, EXACT_LEGAL_LOOKUP, NOT_EXACT_LOOKUP, NOT_EXACT_LOOKUP)
    if lookup is not None:
        return lookup.lookup(query)
    if navigator is not None:
        return ExactProvisionLookup(navigator, navigator.articles, ()).lookup(query)
    return frozen_exact_lookup().lookup(query)


__all__ = [
    "EXACT_ARTICLE_LOOKUP", "EXACT_CLAUSE_LOOKUP", "EXACT_LEGAL_LOOKUP",
    "EXACT_POINT_LOOKUP", "NOT_EXACT_LOOKUP", "POINT_NOT_FOUND",
    "ExactLookupRequest", "ExactLookupResult", "ExactProvisionLookup",
    "detect_exact_lookup", "frozen_exact_lookup", "try_exact_lookup",
]
