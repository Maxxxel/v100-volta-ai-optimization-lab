# Public audit excerpt

Original SHA256: `2e96ee859dddd9c156994aff864a402311c6926fd28fa6c9b6ed8f68567e6489`

Original file: `research-metadata.json`; 9197 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decision": "DIRECT_WEIGHTED_PORT_DEFERRED_UNWEIGHTED_FORWARD_ONLY_VARIANT_REMAINS_TESTABLE",
  "limits": [
    "Source equations and callbacks are admission evidence, not hardware performance/model quality.",
    "No pretrained foreign quantizer copied into Omni; no model/dataset/package download or untrusted pickle load.",
    "No assertion that KVQuant needs retraining in every variant or cannot run on SM70.",
    "No GPU run justified solely to observe this deterministic direct-RoPE mismatch; alternate forward-calibrated route requires its own frozen protocol."
  ]
}
```

</details>

## Selected aggregate measurements

NOT MEASURED / not included in the approved public schema.
