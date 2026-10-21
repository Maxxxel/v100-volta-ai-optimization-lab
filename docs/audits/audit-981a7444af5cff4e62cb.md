# Public audit excerpt

Original SHA256: `981a7444af5cff4e62cbb794c2a3bbab4e7cfd4f8f3b326a9076fb3179632cba`

Original file: `AUDIT.json`; 2647 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "E02_ACTUAL_NATIVE_RENDER_DIFFERS_FROM_FROZEN_NATIVE_PROMPT_NOT_ADMITTED_FOR_TIMING",
  "evidence_class": "LOKAL_GEMESSEN",
  "limits": [
    "OneactualnativeTooldebugrenderonly, no full5case/100BFCL/generationquality/performancequalification",
    "DifferenttoolJSONfieldorderchangesrenderedprompt; notproofmodelqualityloss",
    "FrozenmatchingnativeR206prompt reused, no newGPUstart/benchmark/rewrittenrawdata",
    "No measuredsampler/tokenIDparityand no fairnativefrontendtimingclaim",
    "Alllegacyfailure/protocol/sourcefilespreserved; read-onlyadmissionadaptationexplicitlyrecorded"
  ]
}
```

## Selected aggregate measurements

```json
{
  "actual_generation_requests": 0,
  "model_starts": 1
}
```
