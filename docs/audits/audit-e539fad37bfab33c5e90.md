# Public audit excerpt

Original SHA256: `e539fad37bfab33c5e90eefeb49748ca3ec4832af979ab021497631a36c925a4`

Original file: `RESULTS.json`; 3929 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{}
```

## Selected aggregate measurements

```json
{
  "models": {
    "qwen38": {
      "arms": {
        "A": {
          "format_passes": 0,
          "quality_attempts": 0,
          "quality_passes": 0
        },
        "B": {
          "format_passes": 0,
          "quality_attempts": 0,
          "quality_passes": 0
        }
      },
      "comparison": {
        "format_pass_change": 0,
        "note": "Existing baseline errors do not suppress speed results. Two starts per arm; no independent confirmation claimed.",
        "quality_pass_change": 0,
        "status": "DESCRIPTIVE_COMPARISON"
      },
      "complete": false,
      "failed_starts": [
        {
          "index": 0,
          "model": "qwen38"
        },
        {
          "index": 1,
          "model": "qwen38"
        },
        {
          "index": 2,
          "model": "qwen38"
        },
        {
          "index": 3,
          "model": "qwen38"
        }
      ],
      "numerical_results": [
        {
          "begin_ns": 352884209308105,
          "end_ns": 352885018565924,
          "model": "qwen38",
          "passed": true,
          "reference": "existing CPU reference backend",
          "returncode": 0
        },
        {
          "begin_ns": 352912777659550,
          "end_ns": 352913282126462,
          "model": "qwen38",
          "passed": true,
          "reference": "existing CPU reference backend",
          "returncode": 0
        }
      ]
    }
  }
}
```
