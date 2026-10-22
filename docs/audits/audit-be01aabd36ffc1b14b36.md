# Public audit excerpt

Original SHA256: `be01aabd36ffc1b14b36643715cb2e25b0d8d08e07b4313e2b876c82437022fe`

Original file: `INDEPENDENT_REVIEW.json`; 5034 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "interpretation": "Primary18logicaloperations with3at-least-once deliveries each; fault-recovery and separate-session tests intentionally add36otherlogicaloperations. Do not compare total54candidateeffects to the primary18 alone.",
  "limitations": [
    "Local socketpair with trusted test caller and simulated durable receiver. No external services, network authentication or productive effects.",
    "Parent test checks fault disconnects and durable state; a separate OS-exit-code/event trace was not archived. No claim of power-loss or concurrency certification.",
    "R240ledgerclass unchanged; this adds process/IPC and real process-exit boundary, not a new model optimization.",
    "No separate prelaunch PLANfile archived; fixed assertions are preserved in the execution script. No retrospective performance threshold or GPU qualification."
  ]
}
```

## Selected aggregate measurements

```json
{
  "new_GPU_runs": 0
}
```
