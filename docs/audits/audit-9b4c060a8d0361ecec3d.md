# Public audit excerpt

Original SHA256: `9b4c060a8d0361ecec3de3921dee48caae414dec75807ba06708059db8374ba6`

Original file: `AUDIT.json`; 2451 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "ARTIFACT_NUMERICAL_SAMPLES_ADMITTED_GPU_QUALITY_PENDING",
  "evidence_class": "LOKAL_ARTEFAKT_VERIFIZIERT",
  "limits": [
    "CPUpreparationonly;noGPUquality/VRAM/speedmeasurement",
    "16sampledrows/matrixnotfullweightoractivationbound;Q8referenceisquantized",
    "4smallindependentstdlibchunkswithQ6activationstatistics;no benchmarkquestions/answers",
    "Output/embedding have no calibrationvectors and use standardunweightedquantization",
    "No causalimatrixgainclaimwithout matchedsameQ8/samequantizer/noimatrixcontrol",
    "FailedCPUbuild/budgetrawsretained;originalweights/audits/referenceCunchanged"
  ]
}
```

## Selected aggregate measurements

```json
{
  "actual_GPU_execution": false,
  "model_starts": 0
}
```
