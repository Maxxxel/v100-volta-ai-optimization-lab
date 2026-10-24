# Public audit excerpt

Original SHA256: `8e396ca57b7f61f3a9f25cdf7463f3aa382864122b5f33e62da47683ed2d535e`

Original file: `RESULTS.json`; 3929 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

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
          "begin_ns": 353066851853473,
          "end_ns": 353067609053543,
          "model": "qwen38",
          "passed": true,
          "reference": "existing CPU reference backend",
          "returncode": 0
        },
        {
          "begin_ns": 353095421613603,
          "end_ns": 353095927251043,
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

</details>
