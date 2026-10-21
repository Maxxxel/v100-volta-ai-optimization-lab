# Public audit excerpt

Original SHA256: `8c43cff1256b29cc15e5d0cbebee79deea0da4048749c5165d7370325a240d61`

Original file: `AUDIT.json`; 200878 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "ACTIVE_MTP_PIPELINE_REQUIRED_FOR_OBSERVED_BRANCH_SHIFT",
  "evidence_class": "LOKAL_GEMESSEN",
  "limits": [
    "One-factor proposal suppression with MTP3 context and n_rs_seq3 retained; allCUDA/model/sampler/KV code unchanged",
    "Branch output is an observed ablation outcome; old MTP3 token equivalence is not required",
    "Does not separate draft-head processing, target batching and rollback individually; no generalized losslessness or speed/quality superiority",
    "Original12/sequence/shortcaps and actual zero draft counters are mandatory; no automatic champion"
  ]
}
```

## Selected aggregate measurements

```json
{
  "actual_generation_requests": 32
}
```
