# Public audit excerpt

Original SHA256: `faa39053df3ce18fb628be0e4e6d363da5d046b42f8df88cd87113e7a4a5cc4b`

Original file: `INDEPENDENT_REVIEW.json`; 6614 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "limits": [
    "B-only native check; archived max64 comparator, not a fresh drift control.",
    "No universal lossless/speculative-state claim, no production changes, no champion promotion."
  ]
}
```

## Selected aggregate measurements

```json
{
  "actual_GPU_execution": true,
  "native_metrics": {
    "decode": {
      "A0_E2E_change_percent": -61.80540420278828,
      "median_E2E_s": 0.640423883,
      "median_GPU_j": 137.39011057877642
    },
    "prefill": {
      "A0_E2E_change_percent": -9.078868702731723,
      "median_E2E_s": 0.194769109,
      "median_GPU_j": 55.12688814841488
    },
    "prefill2048": {
      "A0_E2E_change_percent": -3.246472035875936,
      "median_E2E_s": 0.706923485,
      "median_GPU_j": 162.17123809335143
    },
    "prefill4096": {
      "A0_E2E_change_percent": -1.4783317913268479,
      "median_E2E_s": 1.40354557,
      "median_GPU_j": 348.0189843178038
    }
  },
  "original12": [
    {
      "grade": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      },
      "prior_success_loss": false
    },
    {
      "grade": {
        "format_pass": false,
        "raw_preserved": true,
        "semantic_pass": false
      },
      "prior_success_loss": false
    },
    {
      "grade": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      },
      "prior_success_loss": false
    },
    {
      "grade": {
        "format_pass": false,
        "raw_preserved": true,
        "semantic_pass": false
      },
      "prior_success_loss": false
    },
    {
      "grade": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      },
      "prior_success_loss": false
    },
    {
      "grade": {
        "format_pass": false,
        "raw_preserved": true,
        "semantic_pass": true
      },
      "prior_success_loss": false
    },
    {
      "grade": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      },
      "prior_success_loss": false
    },
    {
      "grade": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      },
      "prior_success_loss": false
    },
    {
      "grade": {
        "format_pass": false,
        "raw_preserved": true,
        "semantic_pass": false
      },
      "prior_success_loss": false
    },
    {
      "grade": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      },
      "prior_success_loss": false
    },
    {
      "grade": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      },
      "prior_success_loss": false
    },
    {
      "grade": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      },
      "prior_success_loss": false
    }
  ]
}
```
