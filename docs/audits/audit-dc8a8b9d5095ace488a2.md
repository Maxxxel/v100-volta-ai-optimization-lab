# Public audit excerpt

Original SHA256: `dc8a8b9d5095ace488a268758a7212dd991e3c1ee0670971548d4bfd612ef3f8`

Original file: `AUDIT.json`; 6001 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "K05_K4_GDN_SNAPSHOT_ROLLBACK_NUMERIC_PASS",
  "limitations": [
    "Synthetic normalized Q/K and stable scalar gates, not captured model activations",
    "Tests CUDA GDN snapshot tensor semantics and caller-style restore continuation; does not prove all llama_memory_recurrent scheduler, prefix, multi-slot or MTP state transitions",
    "No model inference or speed/quality benchmark"
  ]
}
```

## Selected aggregate measurements

NOT MEASURED / not included in the approved public schema.
