"""Deterministic legal cross-reference extraction and expansion over frozen corpus-v2.1."""

from __future__ import annotations

import json
import re
import unicodedata
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Sequence

from .paths import CORPUS_VERSION_DIR

DEFAULT_CORPUS_PATH = CORPUS_VERSION_DIR / "chunks" / "chunks.jsonl"
DEFAULT_SOURCES_PATH = CORPUS_VERSION_DIR / "registry" / "sources.json"

# Known document titles & numbers mapped to document_id in corpus-v2.1
DOCUMENT_NAME_MAP = {
    "luật trí tuệ nhân tạo": "134-2025-QH15",
    "134/2025/qh15": "134-2025-QH15",
    "nghị định 142": "142-2026-ND-CP",
    "142/2026/nđ-cp": "142-2026-ND-CP",
    "142/2026/nd-cp": "142-2026-ND-CP",
    "thông tư 05": "05-2026-TT-BKHCN",
    "05/2026/tt-bkhcn": "05-2026-TT-BKHCN",
    "khung đạo đức trí tuệ nhân tạo": "05-2026-TT-BKHCN",
    "khung đạo đức": "05-2026-TT-BKHCN",
    "luật công nghiệp công nghệ số": "20-2026-VBHN-VPQH",
    "20/vbhn-vpqh": "20-2026-VBHN-VPQH",
    "luật dữ liệu": "60-2024-QH15",
    "60/2024/qh15": "60-2024-QH15",
    "luật bảo vệ dữ liệu cá nhân": "91-2025-QH15",
    "91/2025/qh15": "91-2025-QH15",
    "nghị định 356": "356-2025-ND-CP",
    "356/2025/nđ-cp": "356-2025-ND-CP",
    "356/2025/nd-cp": "356-2025-ND-CP",
    "luật an ninh mạng": "116-2025-QH15",
    "116/2025/qh15": "116-2025-QH15",
    "luật chuyển đổi số": "148-2025-QH15",
    "148/2025/qh15": "148-2025-QH15",
    "nghị định 224": "224-2026-ND-CP",
    "224/2026/nđ-cp": "224-2026-ND-CP",
    "224/2026/nd-cp": "224-2026-ND-CP",
    "luật thương mại điện tử": "122-2025-QH15",
    "122/2025/qh15": "122-2025-QH15",
    "nghị định 248": "248-2026-ND-CP",
    "248/2026/nđ-cp": "248-2026-ND-CP",
    "248/2026/nd-cp": "248-2026-ND-CP",
    "luật bảo vệ quyền lợi người tiêu dùng": "47-2026-VBHN-VPQH",
    "47/vbhn-vpqh": "47-2026-VBHN-VPQH",
    "nghị định 29": "29-2026-VBHN-BCT",
    "29/vbhn-bct": "29-2026-VBHN-BCT",
    "luật giao dịch điện tử": "20-2023-QH15",
    "20/2023/qh15": "20-2023-QH15",
    "luật sở hữu trí tuệ": "67-2026-VBHN-VPQH",
    "67/vbhn-vpqh": "67-2026-VBHN-VPQH",
    "quyết định 367": "367-2026-QD-TTG",
    "367/qđ-ttg": "367-2026-QD-TTG",
}

# Decree -> Parent Law mapping
PARENT_LAW_MAP = {
    "142-2026-ND-CP": "134-2025-QH15",
    "356-2025-ND-CP": "91-2025-QH15",
    "224-2026-ND-CP": "148-2025-QH15",
    "248-2026-ND-CP": "122-2025-QH15",
    "29-2026-VBHN-BCT": "47-2026-VBHN-VPQH",
}

# Chained clauses: e.g. "khoản 1, khoản 2 và khoản 3 Điều 10" or "khoản 1, khoản 2 Điều này"
_P_CHAINED_CLAUSES = re.compile(
    r"(?:quy\s+định\s+tại|nêu\s+tại|hướng\s+dẫn\s+tại|theo|áp\s+dụng|tại)?\s*"
    r"((?:khoản\s+\d+[a-z]?\s*(?:,\s*|\s+và\s+)?)+)"
    r"điều\s+(?P<article>\d+[a-z]?|này)"
    r"(?:\s+(?:của\s+)?(?P<doc_ref>luật\s+này|nghị\s+định\s+này|thông\s+tư\s+này|văn\s+bản\s+này|luật\s+[^\.,;\n\(\)]+|nghị\s+định\s+[^\.,;\n\(\)]+|thông\s+tư\s+[^\.,;\n\(\)]+))?",
    re.IGNORECASE,
)

# Single reference patterns
_P_SINGLE_REF = re.compile(
    r"(?:"
    # Case 1: with explicit prefix (theo, tại, căn cứ, quy định tại, ...)
    r"(?:(?:theo\s+(?:quy\s+định\s+)?tại|quy\s+định\s+tại|quy\s+định\s+ở|nêu\s+tại|hướng\s+dẫn\s+tại|áp\s+dụng\s+theo|căn\s+cứ|tại)\s+)"
    r"(?:điểm\s+(?P<point_1>[a-zà-ỹđ])\s+)?"
    r"(?:khoản\s+(?P<clause_1>\d+[a-z]?)\s+)?"
    r"điều\s+(?P<article_1>\d+[a-z]?)"
    r"(?:\s+(?:của\s+)?(?P<doc_1>luật\s+này|nghị\s+định\s+này|thông\s+tư\s+này|luật\s+[^\.,;\n\(\)]+|nghị\s+định\s+[^\.,;\n\(\)]+))?"
    r"|"
    # Case 2: without prefix, but has clause and/or point
    r"(?:điểm\s+(?P<point_2>[a-zà-ỹđ])\s+)?"
    r"khoản\s+(?P<clause_2>\d+[a-z]?)\s+"
    r"điều\s+(?P<article_2>\d+[a-z]?)"
    r"(?:\s+(?:của\s+)?(?P<doc_2>luật\s+này|nghị\s+định\s+này|thông\s+tư\s+này|luật\s+[^\.,;\n\(\)]+|nghị\s+định\s+[^\.,;\n\(\)]+))?"
    r"|"
    # Case 3: article only with explicit suffix (Điều X Luật này / của Luật này)
    r"điều\s+(?P<article_3>\d+[a-z]?)\s+(?:của\s+)?(?P<doc_3>luật\s+này|nghị\s+định\s+này|thông\s+tư\s+này|luật\s+[^\.,;\n\(\)]+|nghị\s+định\s+[^\.,;\n\(\)]+)"
    r"|"
    # Case 4: khoản X điều này
    r"(?:điểm\s+(?P<point_4>[a-zà-ỹđ])\s+)?"
    r"khoản\s+(?P<clause_4>\d+[a-z]?)\s+điều\s+này"
    r")",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class CrossReferenceTarget:
    document_id: str
    article: str
    clause: str | None = None
    point: str | None = None
    raw_match: str = ""


class CrossReferenceResolver:
    """Extracts and resolves cross-references and clause hierarchies."""

    def __init__(self, corpus_path: Path = DEFAULT_CORPUS_PATH):
        self.corpus_path = corpus_path
        self.chunks_by_id: dict[str, dict[str, Any]] = {}
        self.chunks_by_clause: dict[tuple[str, str, str], list[str]] = defaultdict(list)
        self.chunks_by_article: dict[tuple[str, str], list[str]] = defaultdict(list)
        self.chunk_to_clause_key: dict[str, tuple[str, str, str]] = {}
        self._load_corpus()

    def _load_corpus(self) -> None:
        if not self.corpus_path.exists():
            raise FileNotFoundError(f"Corpus chunks not found: {self.corpus_path}")

        with open(self.corpus_path, "r", encoding="utf-8") as f:
            for line in f:
                c = json.loads(line)
                cid = c["chunk_id"]
                doc = c["document_id"]
                art = str(c.get("article_number") or "").lower()
                clause = str(c.get("clause") or "")

                self.chunks_by_id[cid] = c
                if art:
                    self.chunks_by_article[(doc, art)].append(cid)
                    if clause:
                        ckey = (doc, art, clause)
                        self.chunks_by_clause[ckey].append(cid)
                        self.chunk_to_clause_key[cid] = ckey

    def get_clause_siblings(self, chunk_id: str) -> list[str]:
        """Return all sibling chunks belonging to the same clause."""
        ckey = self.chunk_to_clause_key.get(chunk_id)
        if ckey and ckey in self.chunks_by_clause:
            return list(self.chunks_by_clause[ckey])
        return [chunk_id]

    def _resolve_doc_id(self, doc_ref: str | None, current_doc_id: str) -> str:
        """Resolve document reference text to a document_id."""
        if not doc_ref:
            return current_doc_id
        cleaned = doc_ref.strip().lower()
        if cleaned in ("luật này", "nghị định này", "thông tư này", "văn bản này"):
            return current_doc_id

        # Check explicit name mapping
        for name, doc_id in DOCUMENT_NAME_MAP.items():
            if name in cleaned:
                return doc_id

        # Check if decree refers to "của Luật"
        if cleaned == "luật" and current_doc_id in PARENT_LAW_MAP:
            return PARENT_LAW_MAP[current_doc_id]

        return current_doc_id

    def extract_references_from_text(
        self, text: str, document_id: str, current_article: str = "", current_clause: str = ""
    ) -> list[CrossReferenceTarget]:
        """Parse explicit cross-references in a legal chunk's text."""
        targets: list[CrossReferenceTarget] = []
        seen = set()

        # 1. Chained clauses e.g. "khoản 1, khoản 2 và khoản 3 Điều 10" or "khoản 1, khoản 2 Điều này"
        for m in _P_CHAINED_CLAUSES.finditer(text):
            art_str = m.group("article").lower()
            doc_ref = m.group("doc_ref")
            target_doc = self._resolve_doc_id(doc_ref, document_id)

            target_art = current_article.lower() if art_str == "này" else art_str
            if not target_art:
                continue

            clauses = re.findall(r"khoản\s+(\d+[a-z]?)", m.group(1), re.IGNORECASE)
            for c_val in clauses:
                if target_doc == document_id and target_art == current_article.lower() and c_val == current_clause:
                    continue
                tkey = (target_doc, target_art, c_val, None)
                if tkey not in seen:
                    seen.add(tkey)
                    targets.append(
                        CrossReferenceTarget(
                            document_id=target_doc,
                            article=target_art,
                            clause=c_val,
                            point=None,
                            raw_match=m.group(0),
                        )
                    )

        # 2. Single references
        for m in _P_SINGLE_REF.finditer(text):
            point = (m.group("point_1") or m.group("point_2") or m.group("point_4") or "").lower() or None
            clause = m.group("clause_1") or m.group("clause_2") or m.group("clause_4") or None
            art = (m.group("article_1") or m.group("article_2") or m.group("article_3") or "").lower()
            doc_ref = m.group("doc_1") or m.group("doc_2") or m.group("doc_3")

            if m.group("clause_4") is not None:
                # "khoản X Điều này"
                target_art = current_article.lower()
                target_doc = document_id
            else:
                target_art = art
                target_doc = self._resolve_doc_id(doc_ref, document_id)

            if not target_art:
                continue

            # Skip self-reference
            if target_doc == document_id and target_art == current_article.lower() and (clause is None or clause == current_clause):
                continue

            tkey = (target_doc, target_art, clause, point)
            if tkey not in seen:
                seen.add(tkey)
                targets.append(
                    CrossReferenceTarget(
                        document_id=target_doc,
                        article=target_art,
                        clause=clause,
                        point=point,
                        raw_match=m.group(0),
                    )
                )

        return targets

    def resolve_target(self, target: CrossReferenceTarget, max_article_chunks: int = 4) -> list[str]:
        """Resolve a target reference into concrete chunk IDs."""
        doc = target.document_id
        art = target.article

        # If specific clause is requested -> return all chunks in that clause
        if target.clause:
            clause_chunks = self.chunks_by_clause.get((doc, art, target.clause))
            if clause_chunks:
                if target.point:
                    sorted_chunks = sorted(
                        clause_chunks,
                        key=lambda cid: 0 if f"diem-{target.point}" in cid.lower() else 1,
                    )
                    return sorted_chunks
                return list(clause_chunks)

        # If only article is requested -> return capped chunks of that article
        art_chunks = self.chunks_by_article.get((doc, art), [])
        return list(art_chunks[:max_article_chunks])

    def expand(
        self,
        retrieved_chunk_ids: Sequence[str],
        *,
        enable_clause_expansion: bool = True,
        enable_cross_references: bool = True,
        max_source_chunks_for_refs: int = 5,
        max_refs_per_chunk: int = 5,
        max_total_chunks: int = 40,
    ) -> list[str]:
        """Expand retrieved chunks with their clause siblings and followed cross-references."""
        expanded: list[str] = []
        seen: set[str] = set()

        def add_chunk(cid: str) -> bool:
            if cid in self.chunks_by_id and cid not in seen:
                seen.add(cid)
                expanded.append(cid)
                return True
            return False

        # Phase 1: Add original chunks and their clause siblings
        for idx, cid in enumerate(retrieved_chunk_ids):
            if len(expanded) >= max_total_chunks:
                break
            add_chunk(cid)
            if enable_clause_expansion:
                for sib in self.get_clause_siblings(cid):
                    if len(expanded) >= max_total_chunks:
                        break
                    add_chunk(sib)

        # Phase 2: Follow cross-references from the top retrieved chunks
        if enable_cross_references:
            for cid in list(retrieved_chunk_ids)[:max_source_chunks_for_refs]:
                if len(expanded) >= max_total_chunks:
                    break
                c = self.chunks_by_id.get(cid)
                if not c:
                    continue

                doc = c["document_id"]
                art = str(c.get("article_number") or c.get("article") or "").lower()
                clause = str(c.get("clause") or "")
                text = c.get("text", "")
                parent_ctx = c.get("parent_context") or ""
                lead_lines = [
                    line.strip()
                    for line in parent_ctx.splitlines()
                    if line.strip().startswith(("Mở đầu điều:", "Nội dung dẫn của khoản:"))
                ]
                combined_text = f"{text}\n" + "\n".join(lead_lines) if lead_lines else text

                refs = self.extract_references_from_text(
                    combined_text, document_id=doc, current_article=art, current_clause=clause
                )
                for ref in refs[:max_refs_per_chunk]:
                    ref_chunks = self.resolve_target(ref)
                    for r_cid in ref_chunks:
                        if len(expanded) >= max_total_chunks:
                            break
                        add_chunk(r_cid)
                        # Optionally pull clause siblings of the referenced chunk
                        if enable_clause_expansion:
                            for r_sib in self.get_clause_siblings(r_cid):
                                if len(expanded) >= max_total_chunks:
                                    break
                                add_chunk(r_sib)

        return expanded
