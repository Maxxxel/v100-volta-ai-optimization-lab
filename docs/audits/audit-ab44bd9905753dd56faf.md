# Public audit excerpt

Original SHA256: `ab44bd9905753dd56faf682336ba75ef247818df7d6ba3774c7ac50fdfc4feef`

Original file: `AUDIT.json`; 503127 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "MTP_CODING_TRADEOFF_CONFIRMED_NATIVE_TOOLS_STABILITY_PENDING",
  "evidence_class": "LOKAL_GEMESSEN",
  "limits": [
    "Onegreedyseed, same180frozenproblemtexts; one knowncanonicalHumanEval32exceptionexcludedfromprimary163only, full164reported",
    "Functionalcoding and GPUgeneration wall/Joule only; no BFCL/agent/stability qualification and nohost/load/idleenergy",
    "PriorR115 preEOGbranch tokenvariation remains; thisdoesnot establish bitidentity/losslessness",
    "No extra measured performance repetitions; original12 and4warmup generationrequests retained"
  ]
}
```

## Selected aggregate measurements

```json
{
  "actual_generation_requests": 196,
  "scopes": {
    "custom_long16": {
      "gpu_energy_j": 32722.085851543183,
      "gpu_j_per_success": 2181.4723901028788,
      "length_stops": 1,
      "solved": 15,
      "successes_per_second": 0.12481444056586465,
      "tasks": 16,
      "wall_s": 120.17840189
    },
    "standard_full164": {
      "gpu_energy_j": 158094.1982154647,
      "gpu_j_per_success": 1053.9613214364315,
      "length_stops": 2,
      "solved": 150,
      "successes_per_second": 0.26059330809467396,
      "tasks": 164,
      "wall_s": 575.609562259
    },
    "standard_validated163": {
      "gpu_energy_j": 155255.10845003065,
      "gpu_j_per_success": 1035.0340563335376,
      "length_stops": 2,
      "solved": 150,
      "successes_per_second": 0.2652678480939953,
      "tasks": 163,
      "wall_s": 565.466192295
    }
  }
}
```
