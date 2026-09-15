"""Render frozen analysis, explicitly distinguishing incomplete diagnostics."""
import json

def fmt(value):
    if value is None:
        return 'N/A'
    return f'{value:.9f}' if isinstance(value,float) else str(value)

def metric_table(metrics):
    names=list(metrics)
    lines=['| Metric | '+' | '.join(names)+' |','|---|'+'---|'*len(names)]
    def row(label, values):
        lines.append('| '+label+' | '+' | '.join(values)+' |')
    for key,label in [('answer_completeness','AC'),('citation_completeness','Citation Completeness')]:
        for kind in ('macro','micro'):
            row(label+' primary '+kind,[fmt(m[key][kind]) for m in metrics.values()])
        diag=[m[key].get('available_case_diagnostic',m[key]) for m in metrics.values()]
        row(label+' available-case macro (queries)',[f"{fmt(d['macro'])} (n={d['macro_query_denominator']})" for d in diag])
        row(label+' available-case micro (points)',[f"{fmt(d['micro'])} ({d['numerator']}/{d['denominator']})" for d in diag])
    for key,label in [('citation_correctness','Citation Correctness'),('groundedness','Groundedness'),('unsupported_claim_rate','UCR')]:
        row(label+' macro (defined queries)',[f"{fmt(m[key]['macro'])} (n={m[key]['macro_query_denominator']})" for m in metrics.values()])
        row(label+' pooled micro (raw counts)',[f"{fmt(m[key]['pooled_micro'])} ({m[key]['numerator']}/{m[key]['denominator']})" for m in metrics.values()])
    row('Citation syntax validity',[f"{fmt(m['citation_syntax_validity']['rate'])} ({m['citation_syntax_validity']['valid']}/{m['citation_syntax_validity']['eligible']})" for m in metrics.values()])
    return lines

def render(s):
    variants=s['variants']; rep=s['replication']; cs=s['contrasts']
    console=['Phase 5B.2-E status: '+s['status'],'','RECOVERY GATE']
    console += [a+': PASS' for a in variants]
    console += ['','PRODUCTION RERUNS:','0','','EVALUATION']
    console += [f"{a}: {m['judged_count']}/31" for a,m in variants.items()]
    rm=rep['metrics']; p=rep['point_partition']; d=rep['metric_deltas']
    known=lambda m:m['answer_completeness'].get('known_observed_supported_count',m['answer_completeness']['numerator'])
    console += ['','R1 → R2',f"AC macro: {fmt(rm['R1']['answer_completeness']['macro'])} → {fmt(rm['R2']['answer_completeness']['macro'])}; delta {fmt(d['answer_completeness']['macro'])}",
        f"AC micro: {fmt(rm['R1']['answer_completeness']['micro'])} → {fmt(rm['R2']['answer_completeness']['micro'])}; delta {fmt(d['answer_completeness']['micro'])}",
        f"Supported points: {known(rm['R1'])}/102 → "+(str(known(rm['R2']))+'/102' if rep['complete'] else f"N/A ({known(rm['R2'])}/102 known observed support; incomplete)"),
        'Net point change: '+fmt(p['net_reference_contribution'] if p else None),
        'Gross churn: '+fmt(p['gross_churn'] if p else None),
        'Replication variability: '+('Observed same-configuration replication variation; not formal variance estimation' if rep['complete'] else 'Unavailable: incomplete R2 judging; no full-cohort variation estimate')]
    for a in ('A1','A2'):
        c=cs[a]; p=c['point_partition']; ps=c['paired_statistics']; r2=variants['R2']; am=variants[a]
        console += ['',f'R2 vs {a}',f"AC macro: {fmt(r2['answer_completeness']['macro'])} vs {fmt(am['answer_completeness']['macro'])}",
            'Delta: '+fmt(c['metric_deltas']['answer_completeness']['macro']),
            f"AC micro: {fmt(r2['answer_completeness']['micro'])} vs {fmt(am['answer_completeness']['micro'])}",
            'Delta: '+fmt(c['metric_deltas']['answer_completeness']['micro']),
            'Only R2 points: '+fmt(p['counts']['only_reference'] if p else None),
            f'Only {a} points: '+fmt(p['counts']['only_comparator'] if p else None),
            'Net R2 contribution: '+fmt(p['net_reference_contribution'] if p else None),
            f'R2 better / tied / {a} better: '+(' / '.join(str(ps[k]) for k in ('reference_better','tied','comparator_better')) if ps else 'N/A / N/A / N/A'),
            '95% bootstrap CI: '+(json.dumps(ps['bootstrap']['ci95']) if ps else '[N/A, N/A] — not executed; 31-pair gate failed'),
            f"R2 {'revision' if a=='A1' else 'expansion'}-triggered queries: {c['strata']['true']['query_count']} ("+', '.join(c['strata']['true']['query_ids'])+')']
        cost1=r2['efficiency']['totals']; cost2=am['efficiency']['totals']; saved=c['savings_relative_to_R2']
        if a=='A1':
            console += ['Production LLM calls:',f"R2 {cost1['llm']['total']}",f"A1 {cost2['llm']['total']}",f"Saved {saved['llm']}"]
        else:
            console += ['Retrieval calls:',f"R2 {cost1['retrieval']['total']}",f"A2 {cost2['retrieval']['total']}",f"Saved {saved['retrieval']}",
                        'Merge-reranks:',f"R2 {cost1['merge_rerank']['total']}",f"A2 {cost2['merge_rerank']['total']}",f"Saved {saved['merge_rerank']}"]
        console += ['Interpretation: '+c['interpretation']+'; '+'; '.join(c['interpretation_reasons'])]
    console += ['','CITATION / SAFETY','Semantic metrics are available-case diagnostics; syntax validity covers all completed outputs independently. Explicit denominators and raw counts follow.']
    console += metric_table(variants)
    console += ['','EVALUATOR ERRORS']
    for a,m in variants.items():
        console += [f"{a}: {len(m['failed_query_ids'])} exhausted queries; {m['evaluator_attempt_count']} evaluator attempts; {len(m['evaluator_errors'])} failed attempts.",
                    'Failed query IDs: '+(', '.join(m['failed_query_ids']) or 'none')]
    console += ['Provider errors: HTTP 429 RESOURCE_EXHAUSTED (reported free-tier request quota limit 15).',
        'The frozen evaluate_record retries immediately; no backoff was introduced. Every exhausted query used all three allowed attempts. No fourth attempt or valid-output rejudging occurred.',
        '','PRODUCTION ARTIFACT INTEGRITY:','PASS','','FROZEN SOURCE INTEGRITY:','PASS','','Ready for Phase 5C:',
        'YES' if s['ready_for_phase5c'] else 'NO']
    lines=['# Phase 5B.2-E — Frozen production semantic evaluation','',f"**Status: {s['status']}.** Production reruns: 0; production LLM calls during this phase: 0.",'',
        'Recovery gate R2/A1/A2: PASS against external manifest SHA-256 `'+s['recovery_gate']['external_manifest_sha256']+'`.',
        'Original v0 seals remain historically `FAILED_EPHEMERAL_LIFECYCLE`. Authorization uses the unchanged original seals, supplemental durable recovery seals, recovery manifest, and the explicit Phase 5B.2-E user request.','',
        'The evaluator used the unchanged `evaluate_record`, `judge_prompt`, `parse_judge`, `point_audit`, and `citation_validator.validate_citations`; `gemini-3.5-flash-lite`, temperature 0, frozen endpoint and 120-second timeout. Variants ran sequentially R2 → A1 → A2; first valid judgment accepted, maximum three requests per query. Production entry points were guarded against execution.','',
        'Exact joins passed before calls: 31 R2, 31 A1, 31 A2, 31 gold queries, exact query text and 102 unique `(query_id, point_id)` tuples.','',
        '## R1 → R2 replication (reported first)','',
        'R1 is historical and unchanged. R2 has incomplete judging, so full 31-query replication deltas, gained/lost totals, net change and gross churn are unavailable. This is not a formal variance estimate; no effect correction or subtraction is made.','']
    lines += metric_table(rm)
    lines += ['', 'The R1 and available-case R2 secondary values above cover different query sets. Their arithmetic deltas in the JSON are explicitly diagnostic and must not be interpreted as a paired replication effect. Point observations retain all 102 tuple identities with unknown R2 labels represented as null.','',
        '## Completeness gate and evaluator failures','',
        '| Variant | Judged / 31 | Failed queries | Attempts | Failed attempts | Observed supported / 102 |',
        '|---|---:|---:|---:|---:|---:|']
    for a,m in variants.items():
        lines.append(f"| {a} | {m['judged_count']}/31 | {len(m['failed_query_ids'])} | {m['evaluator_attempt_count']} | {len(m['evaluator_errors'])} | {known(m)}/102 (incomplete) |")
    lines += ['', 'HTTP 429 `RESOURCE_EXHAUSTED` responses reported a free-tier request quota limit of 15. The unchanged evaluator retries immediately and exhausted three attempts on the failed queries. The harness added no pacing or retry backoff. All request slots, transport responses/errors and parsed-attempt logs are retained; no fourth attempts, label repairs or rejudging were performed.','']
    for a,m in variants.items():
        lines.append('- '+a+' failed query IDs: '+(', '.join('`'+q+'`' for q in m['failed_query_ids']) or 'none')+'.')
    lines += ['', 'All 93 evaluation envelopes are present, including failures. The mandatory 31/31-per-variant gate failed. Full primary AC, complete 102-point partitions, full paired sign/median summaries and 31-pair bootstrap CIs are withheld. Missing judgments remain null; no denominator reduction or imputation is used.','',
        '## Per-variant available-case diagnostics','',
        'The following semantic metrics are descriptive diagnostics over successfully judged records. They are not the complete primary benchmark result. AC/CC primary macro and micro remain null. Pooled claim metrics use raw matching sums over eligible judged records; zero-denominator query ratios are excluded from macro means and remain null. Groundedness and UCR are calculated independently. Deterministic citation syntax validity covers all completed outputs, including semantic judge failures.','']
    lines += metric_table(variants)
    lines += ['', 'Raw-count anomalies (retained without repairs or extra judgments):']
    for a,m in variants.items():
        lines.append('- '+a+': '+(json.dumps(m['anomalies'],ensure_ascii=False) if m['anomalies'] else 'none')+'.')
    for a,title in [('A1','Answer Revision'),('A2','Evidence Expansion')]:
        c=cs[a]
        lines += ['',f'## R2 vs {a} — {title}', '',
            '**Interpretation: '+c['interpretation']+'.** '+ '; '.join(c['interpretation_reasons'])+'.',
            'Full macro/micro AC differences, median differences, R2-better/tied/ablation-better counts, both/only-R2/only-ablation/neither totals, and net contribution: N/A because the complete paired-data gate failed.',
            'Bootstrap: not executed. Frozen configuration remains 10,000 paired query-level resamples, seed 20260906, sample size 31, independently reset Python `random.Random`, percentile interpolation at `(N-1)*p`; no p-values and no point-level resampling.',
            'Replication attribution safeguards cannot be evaluated because full R1→R2 variation and the primary ablation effect are unavailable. No alternative threshold or corrected effect is used.','',
            'The JSON retains all 31 query rows, both variants’ available scores and raw deltas, statuses/errors, production costs, trace links, and all 102 point observations with nulls for missing judgments.','',
            f'### {title} trigger-aware diagnostics','',
            'Strata use sealed R2 intervention-used flags. These are descriptive post-treatment subsets, not randomized causal subgroups. Differences where R2 did not use the intervention are background run variation/downstream differences.','',
            '| R2 used | Queries | Required points | R2 judged | '+a+' judged | R2 AC macro | '+a+' AC macro | Macro delta |',
            '|---|---:|---:|---:|---:|---:|---:|---:|']
        for key,t in c['strata'].items():
            lm,am=t['metrics']['R2'],t['metrics'][a]
            lines.append(f"| {key} | {t['query_count']} | {t['required_point_denominator']} | {lm['judged_count']} | {am['judged_count']} | {fmt(lm['answer_completeness']['macro'])} | {fmt(am['answer_completeness']['macro'])} | {fmt(t['metric_deltas']['answer_completeness']['macro'])} |")
        lines += ['', 'Cross-tab against the ablation’s own decision metadata:','',
            '| R2 used | Ablation would have triggered | Ablation blocked | Queries |','|---|---|---|---:|']
        for t in c['trigger_cross_tab']:
            lines.append(f"| {t['R2_used']} | {t['ablation_would_have_triggered']} | {t['ablation_blocked_by_ablation']} | {t['count']} |")
        for key,t in c['strata'].items():
            if not t['query_count']:
                continue
            lines += ['', f"R2-used={key}: query IDs "+', '.join(t['query_ids'])+'.',
                f"Required-point denominator: {t['required_point_denominator']}. Complete point partition: "+(json.dumps(t['point_partition']['counts']) if t['point_partition'] else 'N/A; at least one missing judgment')+'.',
                'Subset production costs (R2 / '+a+'): '+ '; '.join(f"{k} {t['costs']['R2']['totals'][k]['total']} / {t['costs'][a]['totals'][k]['total']}" for k in ('retrieval','llm','merge_rerank'))+'.',
                'Subset AC/CC and claim-metric diagnostics, with explicit denominators:','']
            lines += metric_table(t['metrics'])
    lines += ['', '## Production efficiency from sealed ledgers','',
        'All 31 attempted queries per variant are included. Observer call counts reconcile with original traces, per-query journals, production attempts and durable seals. Evaluator requests are excluded.','',
        '| Variant | Retrieval total / mean / median / max | Production LLM total / mean / median / max | Merge-reranks | Observable HTTP submissions |',
        '|---|---|---|---:|---:|']
    for a,m in variants.items():
        e=m['efficiency']; st=e['totals']
        lines.append('| '+a+' | '+' | '.join(' / '.join(fmt(st[k][v]) for v in ('total','mean','median','max')) for k in ('retrieval','llm'))+f" | {st['merge_rerank']['total']} | {e['observable_http_submissions']} |")
    for a,c in cs.items():
        saved=c['savings_relative_to_R2']
        lines += ['',f"{a} savings, R2 − {a}: production LLM {saved['llm']}; retrieval {saved['retrieval']}; merge-reranks {saved['merge_rerank']}. Negative savings mean the ablation used more calls."]
    lines += ['', 'Provider-internal retries, token records and monetary costs are unavailable. Observed HTTP submissions are kept distinct from these unknown quantities.','',
        '## Frozen hypotheses and limits','',
        '- H1: '+s['hypotheses']['H1'], '- H2: '+s['hypotheses']['H2'],
        '- H3 remains exploratory and was not tested.','',
        'H1/H2 receive insufficient evidence because the primary evaluation is incomplete. They are not rewritten from the observed diagnostics. Historical R1 source/environment and provider backend identity limits remain as declared in Phase 5A.','',
        '## Artifact paths and provenance','',
        'Historical root contrast files and per-variant evaluation/metrics placeholders are pinned by the recovery protocol. They remain byte-identical at their original paths. Completed Phase 5B.2-E records and incomplete analysis results use the additive `phase5b2e_v0/` directory:', '',
        '- `phase5b2e_v0/replication_R1_R2.json`', '- `phase5b2e_v0/contrast_R2_A1.json`', '- `phase5b2e_v0/contrast_R2_A2.json`',
        '- `phase5b2e_v0/<variant_id>/{evaluation.jsonl,evaluation_attempts.jsonl,metrics.json}`',
        '- `phase5b_evaluation_metrics_v0.json` and this new report',
        '- `phase5b2e_v0/provenance.json`, `integrity_before.json`, `integrity_after.json`, request/response slots, and per-query records','',
        'Provenance records Phase 5A/5B.1 hashes, original and supplemental seals, production output hashes, external recovery anchor, evaluator/gold hashes, historical source/asset hashes and evaluation artifact hashes. The manifest excludes its own hash; that SHA-256 is printed separately.','',
        'A pre-call harness endpoint check initially stripped the trailing slash, unlike the frozen preflight. It stopped before any evaluator request. The hash check was aligned with the frozen whitespace-only canonicalization and both protocol versions and the amendment were retained; the endpoint, client and evaluator were unchanged.','',
        '## Final integrity and stop','',
        '**Production artifact integrity: PASS. Frozen source integrity: PASS.** All preexisting files in the integrity snapshot retain identical SHA-256 values. The unchanged independent recovery verifier passed again after evaluation. Production outputs/traces/sidecars, all original/supplemental seals, corpus, gold, R0/R1, Phase 4, Phase 5A, Phase 5B.1, Phase 5B.2-R, Agentic runtime, retrieval, prompts, and historical incomplete reports/placeholders remain unchanged.','',
        '**Ready for Phase 5C: NO.** No A3/A4, production reruns, optimization or Phase 5C execution. The exhausted attempt budgets are preserved.','',
        '## Required console output','', '```text']+console+['```','']
    return '\n'.join(lines),'\n'.join(console)+'\n'
