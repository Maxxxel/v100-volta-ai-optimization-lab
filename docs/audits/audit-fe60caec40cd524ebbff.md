# Public audit excerpt

Original SHA256: `fe60caec40cd524ebbff4496c065eadd999b9a346f4da4b520682a468861328a`

Original file: `research-metadata.json`; 3173 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "scope": "GPU energy counter bounds over selected tasks only; excludes model startup, warmup, CPU and full system. Historical control and differing outputs prevent causal energy attribution."
}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "arms": {
    "candidate": {
      "completion_tokens": 53663,
      "counter_bounds": {
        "complete_request_s": 829.979110849,
        "group_window_s": 830.633435905,
        "groups": 1,
        "included_between_request_setup_s": 0.654325056,
        "lower_j": 201543.061,
        "max_query_duration_s": 0.010865767,
        "scope": "Bounds from measured cumulative counter readings before/after each selected contiguous task group. No interpolation or extrapolation. Covers counter-query timing, not undocumented NVML sensor/calibration error. GPU only; includes setup inside each group, excludes unselected tasks, load, warmup and CPU/system energy.",
        "tasks": 164,
        "upper_j": 201633.736
      },
      "gpu_j_per_success_lower": 1371.0412312925168,
      "gpu_j_per_success_upper": 1371.658068027211,
      "raw_hashes_sha256": "cee77d783075e5ba832f1641ebc0418e1e5cd97031561a91e68e6ac1e2affa02",
      "requests_sha256": "82c50bb9c01e4c37c05be666140ae626e1a29b1f6fbeb4a15c7f6f0929a00be4",
      "successes": 147,
      "telemetry_sha256": "3068049c0640239977e1ca0433de0cb2f128d0febb8077b553ca37d7c1ad0610"
    },
    "reference": {
      "completion_tokens": 51322,
      "counter_bounds": {
        "complete_request_s": 754.737726997,
        "group_window_s": 757.154237101,
        "groups": 1,
        "included_between_request_setup_s": 2.416510104,
        "lower_j": 187683.969,
        "max_query_duration_s": 0.031467005,
        "scope": "Bounds from measured cumulative counter readings before/after each selected contiguous task group. No interpolation or extrapolation. Covers counter-query timing, not undocumented NVML sensor/calibration error. GPU only; includes setup inside each group, excludes unselected tasks, load, warmup and CPU/system energy.",
        "tasks": 164,
        "upper_j": 187773.403
      },
      "gpu_j_per_success_lower": 1203.1023653846155,
      "gpu_j_per_success_upper": 1203.6756602564103,
      "raw_hashes_sha256": "3d99e7a91460b3531685092a11966f3b275d32b5648169da1e7abacf0d3537f8",
      "requests_sha256": "34d988e4fc43c5118daa759d8330f84c33a44e5f7f3ea9e36c2244c69eee2005",
      "successes": 156,
      "telemetry_sha256": "d8705c6da6754cd16094cbdf2b2b5f33078b0be6bf31ce756c235dca71e5d10c"
    }
  }
}
```

</details>
