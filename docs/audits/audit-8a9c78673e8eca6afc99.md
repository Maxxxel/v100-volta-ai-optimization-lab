# Public audit excerpt

Original SHA256: `8a9c78673e8eca6afc99a70918734adae6a4654ab759146e8800f3ea0564b195`

Original file: `INDEPENDENT_REVIEW.json`; 2163 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "limits": [
    "Native same-process CUDA vs CPU reference; randomized native tensor data not archived and separate processes are not identical-input A/B.",
    "Component telemetry is not model energy per successful task, tokens/s or task latency.",
    "Pass at16K does not qualify an independent16K model profile.",
    "No thermal/ECC/VRAM safety violation; all original weights/source/audits preserved."
  ]
}
```

## Selected aggregate measurements

```json
{
  "actual_GPU_execution": true,
  "model_starts": 0
}
```
