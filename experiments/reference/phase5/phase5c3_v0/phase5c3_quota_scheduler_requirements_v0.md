# Phase 5C.3 — Global quota scheduler design requirements

Binding future design only. No scheduler, provider integration, API request, quota verification or runtime modification is implemented in 5C.3.

## Quota configuration and ownership

Every live provider request in the same quota domain MUST be governed by one coordinated GLOBAL PROVIDER REQUEST SCHEDULER across applicable workers, processes and hosts. A quota domain identifies the provider/account/project/model-or-pool limits actually shared; use opaque credential references, never secret values. Production and evaluator using distinct providers/pools have separately recorded domains/configurations. If they share a pool, one coordinated scheduler governs both, including their retries, even when their phases execute sequentially. Other applicable live workload in the same pool must participate or have a conservatively reserved allocation; an uncoordinated external consumer cannot be assumed absent without an execution-time declaration.

Before live production, resolve and seal `provider_rate_limit_config` with: schema/version/hash; domain ID; provider and applicable account/project/model pool references; actual request ceiling; window duration and enforcement semantics; permitted burst (conservative no-burst default); any other applicable concurrency/token ceilings; workload reservations; clock policy; shared durable state location/ownership; retry policy hash; scheduling rule/seed; configuration source and verification date; and approving operator. No credentials or quality labels belong in this config. Unknown active quota configuration is a STOP condition for live work. Resolving current quotas is future work only.

15 RPM was previously observed/declared for the project (external-review historical context). It is not a permanent scientific property or an assumed current quota. The future execution-time value must be explicitly resolved and sealed. No web/API verification occurs in this phase.

## Mandatory scheduler behavior

| ID | Required behavior | Future verification obligation |
| --- | --- | --- |
| QS01 | Enforce configured request-rate ceilings globally across applicable workers/processes; prevent bursts above quota and serialize or rate-limit as needed | Concurrent workers cannot each consume a full local quota; test the combined dispatch stream against every configured window and burst bound |
| QS02 | Every physical provider attempt obtains an atomic shared dispatch reservation before sending; keep logical-call and physical-attempt identities distinct | One logical call with retry appears as multiple physical attempts consuming quota |
| QS03 | Transport retries and shared-pool evaluator retries traverse the same scheduler; a retry is never an unmetered bypass | Failed, throttled, timed-out and ambiguous attempts remain counted and linked |
| QS04 | Persist attempt/reservation timestamps durably before dispatch and append actual send/completion/error timestamps when known | Crash immediately before/after send cannot erase the recent quota footprint; reservation and dispatch bounds remain distinguishable |
| QS05 | Crash/restart reconstructs pending reservations, recent attempts and quota debt before allowing another dispatch | No immediate post-restart burst; lost/corrupt/unavailable coordination state means pause, never fall back to independent worker limiters |
| QS06 | Persist provider retry-after/not-before data when available, raw value plus normalized timestamp and scope/domain | Recovery honors the maximum of quota eligibility and provider not-before; shared-domain throttling blocks other workers as applicable |
| QS07 | Scheduling order is quality-blind under a predeclared FIFO or balanced/interleaved seeded schedule; no quality-based prioritization | Inputs to scheduling exclude gold, answer quality, disagreement, evaluator scores, difficulty and expected mechanism; resource-readiness skips remain logged |
| QS08 | Preserve sufficient clock/restart metadata, synchronization tolerance and conservative handling of ambiguous timestamps | Backward clock jumps, skew, stale worker leases and ambiguous sends cannot permit early dispatch; uncertainty pauses or retains reservations for the applicable conservative window |
| QS09 | Retries obey the separately sealed recovery policy and budgets as well as quota | No retry of accepted answers; keep first valid allowed response and all attempt records; no hidden extra logical calls |
| QS10 | All live requests have an explicit domain and sealed config reference; coordinated state has atomic reservation/fencing semantics | No missing-domain bypass, duplicate dispatch reservation or stale-leader oversubscription; coordination failures block dispatch |

Spacing requests can be a conservative strategy; fixed-minute counter resets alone must not create an over-quota boundary burst. Where multiple applicable limits exist, dispatch must satisfy all of them. Durably recorded reservation time is not proof that a provider received a request; mark send/receipt uncertainty explicitly. An ambiguous send consumes the conservative quota reservation and follows the inherited no-duplicate-guessing recovery rule.

## Trace amendment and isolation

Extend every provider physical-attempt record with `attempt_id`, `logical_call_id`, `quota_domain_id`, `provider_rate_limit_config_hash`, `scheduler_reservation_id`, `reservation_at_utc`, `eligible_not_before_utc`, `dispatched_at_utc` (nullable), `completed_at_utc` (nullable), `attempt_state`, `retry_parent_attempt_id` (nullable), `retry_after_raw` (nullable), `provider_not_before_utc` (nullable), `clock_epoch_or_restart_id`, `coordinator_fencing_token`, `durable_event_ref`, and known token/latency/error metadata. Every timestamp includes a declared clock basis. Append events rather than overwriting failures; record unknown values as null with reasons.

The conceptual trace schema's `ProductionLLMCall.physical_attempts` references these fields; evaluator request ledgers use the same scheduling metadata in separate evaluator-only storage. Scheduler state contains minimal timing/identity/resource metadata, not exact queries, responses, gold or evaluation results. A production process cannot read evaluator payloads through the shared scheduler. Physical attempts count toward provider quota; logical calls remain the scientific budget unit; evaluator calls remain separate from production totals. This design adds no LLM budget and does not authorize live execution.
