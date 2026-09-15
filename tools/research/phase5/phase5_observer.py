"""Pass-through observations; no decision parsing, retries, or state mutations."""
from __future__ import annotations
from dataclasses import asdict, is_dataclass
from datetime import datetime, timezone
import re
import sys
from phase5_common import digest

_ACTIVE_EVENT = None
_AUDIT_INSTALLED = False


def _http_audit(event, args):
    if _ACTIVE_EVENT is not None and event == 'urllib.Request':
        current = _ACTIVE_EVENT['observable_http_attempts']
        _ACTIVE_EVENT['observable_http_attempts'] = (0 if current == 'unknown' else current) + 1


def redact(text, secrets=()):
    for secret in secrets:
        if secret:
            text = text.replace(secret, '[REDACTED]')
    text = re.sub(r'(?i)((?:authorization|x-api-key|api[_-]?key|password|credential|access_token|refresh_token)["\']?\s*[:=]\s*["\']?)[^\r\n,}"\']+', r'\1[REDACTED]', text)
    text = re.sub(r'(?i)\bbearer\s+[A-Za-z0-9._~+/=-]+', 'Bearer [REDACTED]', text)
    return text


def serial(value):
    if is_dataclass(value):
        return asdict(value)
    if isinstance(value, (list, tuple)):
        return [serial(x) for x in value]
    if isinstance(value, dict):
        return {k: serial(v) for k, v in value.items()}
    return value


class Observer:
    def __init__(self, state, secrets=()):
        global _AUDIT_INSTALLED
        if not _AUDIT_INSTALLED:
            sys.addaudithook(_http_audit)
            _AUDIT_INSTALLED = True
        self.state = state
        self._initial_coverage = state.coverage_check
        self._initial_completeness = state.completeness_check
        self.events = []
        self.first_completeness = None
        self.secrets = tuple(secrets)

    def call(self, kind, request, fn):
        global _ACTIVE_EVENT
        stage = self.state.transitions[-1]
        if stage == 'answer_revision' and self.first_completeness is None:
            # The unchanged controller has successfully parsed and assigned this.
            self.first_completeness = asdict(self.state.completeness_check)
        event = dict(stage=stage, attempt_index=1, logical_call_index=1 + sum(e['logical_call_type'] == kind for e in self.events),
                     logical_call_type=kind, request_hash=digest(serial(request)), response_hash=None,
                     timestamp=datetime.now(timezone.utc).isoformat(), status='started',
                     observable_http_attempts='unknown' if kind == 'llm' else None,
                     provider_internal_retries='unknown' if kind == 'llm' else None)
        self.events.append(event)
        previous = _ACTIVE_EVENT
        if kind == 'llm':
            _ACTIVE_EVENT = event
        try:
            value = fn()
        except Exception as exc:
            event.update(status='error', error_type=type(exc).__name__)
            # Exception messages can embed headers/URLs/credentials: omit entirely.
            raise
        finally:
            _ACTIVE_EVENT = previous
        event.update(status='success', response_hash=digest(serial(value)))
        if kind == 'llm' and isinstance(value, str):
            event['raw_response'] = redact(value, self.secrets)
        return value

    def metadata(self, flags):
        from agentic_rag import MAX_ANSWER_REVISIONS, MAX_RETRIEVAL_EXPANSIONS, MAX_LLM_CALLS
        state = self.state
        # The frozen controller replaces these objects only after successful parsing.
        # Identity observes that assignment even if the next deterministic stage fails.
        coverage_reached = state.coverage_check is not self._initial_coverage
        first = self.first_completeness
        if first is None and state.completeness_check is not self._initial_completeness:
            first = asdict(state.completeness_check)
        expansion = (not state.coverage_check.sufficient and bool(state.missing_aspects) and MAX_RETRIEVAL_EXPANSIONS > 0) if coverage_reached else None
        answer = (not first['complete'] and MAX_ANSWER_REVISIONS > 0) if first is not None else None
        return {
            'answer_revision_would_have_triggered': answer,
            'answer_revision_blocked_by_ablation': None if answer is None else answer and not flags['enable_answer_revision'],
            'answer_revision_reason': 'unreached_or_failed_check' if answer is None else 'incomplete' if answer else 'complete',
            'expansion_would_have_triggered': expansion,
            'expansion_blocked_by_ablation': None if expansion is None else expansion and not flags['enable_expansion'],
            'expansion_reason': 'unreached_or_failed_check' if expansion is None else 'sufficient' if state.coverage_check.sufficient else 'missing_aspects_nonempty' if state.missing_aspects else 'missing_aspects_empty',
            'first_completeness_check': first,
            'revision_attempted': state.revision_used, 'revision_count': state.revision_count,
            'expansion_attempted': state.expansion_used,
            'citation_revision_attempted': state.citation_revision_used,
            'citation_revision_count': state.citation_revision_count,
            'llm_budget_exhausted': len(state.llm_calls) >= MAX_LLM_CALLS,
            'error_type': state.execution_error['type'] if state.execution_error else None,
        }


class ObservedClient:
    def __init__(self, client, observer):
        self.client, self.observer = client, observer
        self.model = getattr(client, 'model', '')

    def generate(self, prompt):
        return self.observer.call('llm', prompt, lambda: self.client.generate(prompt))


class ObservedPipeline:
    def __init__(self, pipeline, observer):
        self.pipeline, self.observer = pipeline, observer

    def retrieve_with_audit(self, query, top_k=5, *, all_candidates=False):
        return self.observer.call('retrieval', [query, top_k, all_candidates], lambda: self.pipeline.retrieve_with_audit(query, top_k, all_candidates=all_candidates))

    def rerank_evidence_pool(self, query, pool, top_k=5):
        return self.observer.call('merge_rerank', [query, pool, top_k], lambda: self.pipeline.rerank_evidence_pool(query, pool, top_k))
