# Public audit excerpt

Original SHA256: `e969fc73e8b1da7c92d72cfa0d37189a2605560ec8debbcba30cf78d380d9ed2`

Original file: `AUDIT.json`; 11808 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "ISOLATED_RECEIVER_RETRY_CRASH_CONTRACT_PASSED_CPU_ONLY_NOT_GPU_OPTIMIZATION",
  "evidence_class": "CPU_LOKAL_GEMESSEN_KEIN_NEUER_GPU_TEST",
  "limits": [
    "Effects are only local simulator SQLite rows in the receiver transaction; no HomeAssistant/Proxmox/network/tool action.",
    "Unlike R240 direct calls, transport crosses a real socketpair/process boundary and process death beforecommit/aftercommit is injected. This is not a new model-quality test.",
    "Deduplication requires durable receiver-side atomic receipt/effect storage; caller-only retry caching does not make arbitrary external effects exactly-once.",
    "Trusted caller assigns session/request/capability context; regenerated replies/newlogicalrequests are not automatically the same operation.",
    "No concurrent-client, power-loss, production authentication/security, realservice adapter, inference speed or GPUJ/success qualification.",
    "Set-state tools may already be idempotent in final value; counts measure receiver dispatch events, not distinct physical changes."
  ],
  "measurement_type": "CPU_IPC_SHADOW_RETRY_PROCESS_CRASH_COMPONENT"
}
```

## Selected aggregate measurements

```json
{
  "actual_GPU_execution": false,
  "actual_generation_requests": 0,
  "after_commit_process_crash_controls": 18,
  "authority_revocation_controls": 18,
  "authorized_cases": 18,
  "baseline_primary_dispatch_events": 54,
  "before_commit_process_crash_controls": 18,
  "candidate_primary_dispatch_events": 18,
  "component_wall_s": 2.120590339996852,
  "denied_cases": 6,
  "denied_deliveries": 18,
  "malformed_envelope_controls": 18,
  "model_starts": 0,
  "new_GPU_runs": 0,
  "separate_session_controls": 18,
  "source_cases": 24
}
```
