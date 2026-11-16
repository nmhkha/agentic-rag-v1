"""Deterministic semantic retrieval restricted to one resolved legal document."""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from typing import Any

from .navigation import (
    DOCUMENT_AMBIGUOUS,
    DOCUMENT_NOT_FOUND,
    SUCCESS,
    DocumentCandidate,
    DocumentNavigator,
    frozen_document_navigator,
)
from .retrieval.pipeline import DEFAULT_TOP_K, Evidence


DOCUMENT_SCOPED_SEARCH = "DOCUMENT_SCOPED_SEARCH"
NOT_DOCUMENT_SCOPED_SEARCH = "NOT_DOCUMENT_SCOPED_SEARCH"
NO_RELEVANT_RESULTS = "NO_RELEVANT_RESULTS"


@dataclass(frozen=True)
class DocumentScopedSearchRequest:
    intent: str
    document_reference: str | None = None
    scoped_query: str | None = None


@dataclass(frozen=True)
class ScopedSearchItem:
    chunk_id: str
    document_id: str | None
    document_number: str | None
    document_title: str | None
    article_id: str | None
    article: str | None
    article_title: str | None
    clause: str | None
    point: str | None
    text: str
    bm25_rank: int | None
    dense_rank: int | None
    reranker_score: float
    rank: int
    evidence: Evidence


@dataclass(frozen=True)
class ProvisionResult:
    article_id: str
    article: str
    article_title: str | None
    best_reranker_score: float
    matches: tuple[ScopedSearchItem, ...]


@dataclass(frozen=True)
class DocumentScopedSearchResult:
    handled: bool
    route: str
    intent: str
    status: str
    document_id: str | None = None
    document_number: str | None = None
    document_title: str | None = None
    scoped_query: str | None = None
    results: tuple[ScopedSearchItem, ...] = ()
    provisions: tuple[ProvisionResult, ...] = ()
    retrieval_call_count: int = 0
    llm_call_count: int = 0
    message: str = ""
    candidates: tuple[DocumentCandidate, ...] = ()


_END = r"\s*[?.!。]*\s*$"
_LEGAL_DOCUMENT_START = re.compile(
    r"^(?:luật|bộ\s+luật|nghị\s+định|thông\s+tư|quyết\s+định|"
    r"pháp\s+lệnh|hiến\s+pháp)\b",
    re.IGNORECASE,
)
_DOCUMENT_NUMBER = re.compile(
    r"(?<!\d)\d{1,4}\s*[/.-]\s*(?:\d{4}\s*[/.-]\s*)?[A-Za-zÀ-ỹĐđ0-9-]+",
    re.IGNORECASE,
)
_EXACT_PROVISION = re.compile(
    r"\b(?:điều\s+\d+[a-zA-Z]?|khoản\s+\d+[a-zA-Z]?|"
    r"điểm\s+[a-zA-Zà-ỹÀ-ỸđĐ]\s+khoản)\b",
    re.IGNORECASE,
)
_REASONING = re.compile(
    r"\b(?:có\s+áp\s+dụng|áp\s+dụng\s+cho|trường\s+hợp\s+(?:của\s+)?tôi|"
    r"app\s+của\s+tôi|tôi\s+(?:có\s+)?cần|vi\s+phạm|đánh\s+giá)\b",
    re.IGNORECASE,
)

_PATTERNS = (
    # Trong <document> có những điều/quy định nào liên quan đến <topic>?
    re.compile(
        rf"^trong\s+(?P<document>.+?)\s+có\s+(?:những\s+)?"
        rf"(?:điều(?:\s+khoản)?|quy\s+định)\s+nào\s+"
        rf"(?:liên\s+quan\s+đến|về)\s+(?P<topic>.+?){_END}",
        re.IGNORECASE,
    ),
    # Tìm các điều khoản/quy định về <topic> trong <document>.
    re.compile(
        rf"^tìm\s+(?:kiếm\s+)?(?:các\s+)?(?:điều(?:\s+khoản)?|quy\s+định)\s+"
        rf"(?:liên\s+quan\s+đến|về)\s+(?P<topic>.+?)\s+trong\s+"
        rf"(?P<document>.+?){_END}",
        re.IGNORECASE,
    ),
    # <document> quy định/nói những gì về <topic>?
    re.compile(
        rf"^(?P<document>.+?)\s+(?:quy\s+định|nói)\s+(?:những\s+)?gì\s+"
        rf"(?:liên\s+quan\s+đến|về)\s+(?P<topic>.+?){_END}",
        re.IGNORECASE,
    ),
)


def _normalize_query(value: str) -> str:
    value = unicodedata.normalize("NFC", value)
    value = value.translate(str.maketrans({"“": '"', "”": '"', "‘": "'", "’": "'"}))
    return re.sub(r"\s+", " ", value).strip()


def _clean(value: str) -> str:
    return value.strip().strip(" \t\r\n,;:.?!\"'")


def _is_explicit_document(reference: str) -> bool:
    return bool(_LEGAL_DOCUMENT_START.search(reference) or _DOCUMENT_NUMBER.search(reference))


def detect_document_scoped_search(query: str) -> DocumentScopedSearchRequest:
    """Recognize conservative document-named semantic search forms."""
    normalized = _normalize_query(query)
    if _EXACT_PROVISION.search(normalized) or _REASONING.search(normalized):
        return DocumentScopedSearchRequest(NOT_DOCUMENT_SCOPED_SEARCH)
    for pattern in _PATTERNS:
        match = pattern.fullmatch(normalized)
        if match is None:
            continue
        document = _clean(match.group("document"))
        topic = _clean(match.group("topic"))
        if not document or not topic or not _is_explicit_document(document):
            continue
        return DocumentScopedSearchRequest(
            DOCUMENT_SCOPED_SEARCH, document_reference=document, scoped_query=topic
        )
    return DocumentScopedSearchRequest(NOT_DOCUMENT_SCOPED_SEARCH)


class DocumentScopedSearcher:
    """Resolve first, then invoke one document-filtered hybrid retrieval call."""

    def __init__(self, navigator: DocumentNavigator, pipeline: Any) -> None:
        self.navigator = navigator
        self.pipeline = pipeline
        self._article_titles = {
            str(article.get("article_id", "")): (
                str(article.get("article_title") or "").strip() or None
            )
            for article in navigator.articles
        }

    def search(self, query: str) -> DocumentScopedSearchResult:
        request = detect_document_scoped_search(query)
        if request.intent == NOT_DOCUMENT_SCOPED_SEARCH:
            return DocumentScopedSearchResult(
                False, DOCUMENT_SCOPED_SEARCH, request.intent,
                NOT_DOCUMENT_SCOPED_SEARCH,
            )

        document, candidates = self.navigator.resolve_document(
            request.document_reference or ""
        )
        if document is None:
            if candidates:
                choices = "; ".join(
                    f"{item.document_title} ({item.document_number})"
                    for item in candidates
                )
                return DocumentScopedSearchResult(
                    True, DOCUMENT_SCOPED_SEARCH, request.intent,
                    DOCUMENT_AMBIGUOUS, scoped_query=request.scoped_query,
                    candidates=candidates,
                    message=f"Không thể xác định duy nhất văn bản. Các ứng viên: {choices}",
                )
            return DocumentScopedSearchResult(
                True, DOCUMENT_SCOPED_SEARCH, request.intent, DOCUMENT_NOT_FOUND,
                scoped_query=request.scoped_query,
                message=f"Không tìm thấy văn bản: {request.document_reference}",
            )

        document_id = str(document.get("document_id", ""))
        document_number = str(document.get("document_number", ""))
        document_title = str(document.get("title") or document.get("document_title") or "")
        evidence = self.pipeline.retrieve(
            request.scoped_query or "", DEFAULT_TOP_K, document_id=document_id
        )
        # Defense in depth: the retriever contract requires pre-ranking filtering;
        # reject a violating implementation instead of silently returning leakage.
        foreign = [item.chunk_id for item in evidence if item.document_id != document_id]
        if foreign:
            raise RuntimeError(
                "Document-scoped retriever returned foreign chunks: " + ", ".join(foreign)
            )

        items = tuple(self._item(item) for item in evidence)
        base = {
            "handled": True,
            "route": DOCUMENT_SCOPED_SEARCH,
            "intent": request.intent,
            "document_id": document_id,
            "document_number": document_number,
            "document_title": document_title,
            "scoped_query": request.scoped_query,
            "retrieval_call_count": 1,
            "llm_call_count": 0,
        }
        if not items:
            return DocumentScopedSearchResult(
                **base, status=NO_RELEVANT_RESULTS,
                message=(f"Không tìm thấy kết quả liên quan trong {document_title} "
                         f"({document_number})."),
            )

        provisions = self._aggregate(items)
        return DocumentScopedSearchResult(
            **base, status=SUCCESS, results=items, provisions=provisions,
            message=self._render(
                document_title, document_number, request.scoped_query or "", provisions
            ),
        )

    def _item(self, evidence: Evidence) -> ScopedSearchItem:
        return ScopedSearchItem(
            chunk_id=evidence.chunk_id,
            document_id=evidence.document_id,
            document_number=evidence.document_number,
            document_title=evidence.document_title,
            article_id=evidence.article_id,
            article=evidence.article,
            article_title=self._article_titles.get(str(evidence.article_id or "")),
            clause=evidence.clause,
            point=evidence.point,
            text=evidence.text,
            bm25_rank=evidence.bm25_rank,
            dense_rank=evidence.dense_rank,
            reranker_score=evidence.reranker_score,
            rank=evidence.rank,
            evidence=evidence,
        )

    @staticmethod
    def _aggregate(items: tuple[ScopedSearchItem, ...]) -> tuple[ProvisionResult, ...]:
        """Group in reranker order; an Article's score is its best chunk score."""
        grouped: dict[str, list[ScopedSearchItem]] = {}
        for item in items:
            key = item.article_id or f"{item.document_id}_dieu-{item.article}"
            grouped.setdefault(key, []).append(item)
        return tuple(
            ProvisionResult(
                article_id=article_id,
                article=str(matches[0].article or ""),
                article_title=matches[0].article_title,
                best_reranker_score=max(item.reranker_score for item in matches),
                matches=tuple(matches),
            )
            for article_id, matches in grouped.items()
        )

    @staticmethod
    def _render(
        document_title: str,
        document_number: str,
        scoped_query: str,
        provisions: tuple[ProvisionResult, ...],
    ) -> str:
        lines = [
            f'Trong {document_title} ({document_number}), các kết quả liên quan nhất '
            f'đến "{scoped_query}" gồm:',
            "",
        ]
        for index, provision in enumerate(provisions, 1):
            heading = f"{index}. Điều {provision.article}"
            if provision.article_title:
                heading += f". {provision.article_title}"
            lines.append(heading)
            for match in provision.matches:
                locator = []
                if match.clause:
                    locator.append(f"Khoản {match.clause}")
                if match.point:
                    locator.append(f"Điểm {match.point}")
                if locator:
                    lines.append(f"   - {'; '.join(locator)}")
                lines.append(f"   - {match.text}")
            lines.append("")
        return "\n".join(lines).rstrip()


def try_document_scoped_search(
    query: str,
    pipeline: Any,
    navigator: DocumentNavigator | None = None,
) -> DocumentScopedSearchResult:
    """Try the route without loading corpus data for non-matching queries."""
    request = detect_document_scoped_search(query)
    if request.intent == NOT_DOCUMENT_SCOPED_SEARCH:
        return DocumentScopedSearchResult(
            False, DOCUMENT_SCOPED_SEARCH, request.intent,
            NOT_DOCUMENT_SCOPED_SEARCH,
        )
    return DocumentScopedSearcher(
        navigator or frozen_document_navigator(), pipeline
    ).search(query)


__all__ = [
    "DOCUMENT_SCOPED_SEARCH", "NO_RELEVANT_RESULTS",
    "NOT_DOCUMENT_SCOPED_SEARCH", "DocumentScopedSearchRequest",
    "DocumentScopedSearchResult", "DocumentScopedSearcher", "ProvisionResult",
    "ScopedSearchItem", "detect_document_scoped_search",
    "try_document_scoped_search",
]
