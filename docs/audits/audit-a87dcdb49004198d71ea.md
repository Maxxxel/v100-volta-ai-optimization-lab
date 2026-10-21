# Public audit excerpt

Original SHA256: `a87dcdb49004198d71ea0d150b2e7d47a0840ceb8b303f6a7f6ca2482375534b`

Original file: `RESULTS.json`; 10715 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{}
```

## Selected aggregate measurements

```json
{
  "models": {
    "omnicoder2": {
      "change_exercised": false,
      "complete": false,
      "failed_starts": [
        {
          "index": 0,
          "model": "omnicoder2"
        },
        {
          "index": 1,
          "model": "omnicoder2"
        },
        {
          "index": 2,
          "model": "omnicoder2"
        },
        {
          "index": 3,
          "model": "omnicoder2"
        }
      ],
      "residency": {
        "change_exercised": false,
        "note": "Both arms same original engine, verbosity5 for actual layer assignment evidence, six threads and unchanged frozen quality/speed probes. Output stays on GPU, first4repeating layers move to CPU. Paired A/B isolates offload; original-baseline comparison also includes the shared diagnostic verbosity difference."
      }
    }
  }
}
```
