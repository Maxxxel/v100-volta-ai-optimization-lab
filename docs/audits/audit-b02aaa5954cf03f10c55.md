# Public audit excerpt

Original SHA256: `b02aaa5954cf03f10c55843447e4ac37f88ae7c06771b304f44ad3026f29ec54`

Original file: `AUDIT.json`; 81156 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decision": "MTP_OFF_LOGIT_REFERENCE_VALID",
  "evidence_class": "LOKAL_GEMESSEN",
  "limits": [
    "Instrumented CPU server diagnostic only; all CUDA/model/sampler/KV artifacts unchanged",
    "Predeclared old branch/sequence inputs and same-arm outputs; not new independent quality questions",
    "Raw target logits exclude EOG for ranking because diagnostic ignore_eos=true; no fabricated speculative API probabilities",
    "No timing/speed comparison from instrumented runs and no inference of exact greedy losslessness from a small margin",
    "Broader functional coding scores retained from R117/R118; native assistant tool-profile negatives unchanged"
  ]
}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "actual_generation_requests": 32
}
```

</details>
