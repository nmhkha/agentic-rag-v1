"""Reusable ingestion APIs."""

from .chunking import build_article_chunks, build_chunks, serialize_chunks
from .cleaners import clean_text, load_boilerplate_lines, normalize_single_line
from .extractors import extract_document, extract_docx_text
from .parsers import LegalStructureParser, parse_legal_structure
from .validators import ValidationCollector, validate_corpus

__all__ = [
    "LegalStructureParser",
    "ValidationCollector",
    "build_article_chunks",
    "build_chunks",
    "clean_text",
    "extract_document",
    "extract_docx_text",
    "load_boilerplate_lines",
    "normalize_single_line",
    "parse_legal_structure",
    "serialize_chunks",
    "validate_corpus",
]
