# Public audit excerpt

Original SHA256: `d798c15e0eb73ae5a51cc1b86f5283c1d4ccd0a3179ff297353894d45f91679a`

Original file: `research-metadata.json`; 4598 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "qualification": "NUMERIC_OUTPUT_EQUIVALENCE_OBSERVED_REQUIRES_CUDA_NUMERIC_ORACLE"
}
```

## Selected aggregate measurements

```json
{
  "A": {
    "format_passes": 16,
    "quality_n": 24,
    "semantic_passes": 18,
    "tasks": {
      "decode": {
        "median_decode_tps": 79.88102223598646,
        "median_e2e_s": 1.6748329865,
        "n": 6
      },
      "prefill": {
        "median_e2e_s": 0.213837671,
        "n": 6
      },
      "prefill2048": {
        "median_e2e_s": 0.728664958,
        "n": 6
      },
      "prefill4096": {
        "median_e2e_s": 1.4272513255,
        "n": 6
      }
    }
  },
  "B": {
    "format_passes": 16,
    "quality_n": 24,
    "semantic_passes": 18,
    "tasks": {
      "decode": {
        "median_decode_tps": 79.9310256382839,
        "median_e2e_s": 1.6764256880000001,
        "n": 6
      },
      "prefill": {
        "median_e2e_s": 0.21441668200000003,
        "n": 6
      },
      "prefill2048": {
        "median_e2e_s": 0.730521822,
        "n": 6
      },
      "prefill4096": {
        "median_e2e_s": 1.430769637,
        "n": 6
      }
    }
  },
  "delta": {
    "decode": {
      "decode_tps_percent": 0.06259734902955838,
      "e2e_percent": 0.09509613870983813
    },
    "prefill": {
      "e2e_percent": 0.2707712805196216
    },
    "prefill2048": {
      "e2e_percent": 0.2548309726731812
    },
    "prefill4096": {
      "e2e_percent": 0.24650959765391
    }
  }
}
```
