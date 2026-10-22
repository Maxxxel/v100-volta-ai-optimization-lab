# Public audit excerpt

Original SHA256: `e547bc3b623ccc45230b82d33d955c63a841613e86775c77c229fcf485824ff3`

Original file: `AUDIT.json`; 1949 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "NO_FEASIBLE_THRESHOLD_AT_95_PERCENT_RETENTION",
  "evidence_class": "LOKAL_GEMESSEN",
  "limits": [
    "Selfauthoredmockpolicydecisionsonly;no liveactions or broadagent/security/codingqualification.",
    "Familydisjointcalibration80/holdout120;raw tokenlikelihood isnotcalibrated correctnessprobability.",
    "No unsafeallows or nofeasible95%retentionthreshold in calibration stops beforeholdout; noerrorsinjected or originalbenchmarktuning.",
    "UnderlyingA/Bdecisionchangesvetoattribution;abstentionsarenot solvedtasks.",
    "StockOmniQ6K/8K/F16/300W,originalweights/template retained;noMTP/cache/library/kernel/powercombination,newreferenceorChampion."
  ],
  "measurement_type": "GPU_MOCK_ACTION_SELECTIVE_RISK_CALIBRATION_SCREEN"
}
```

## Selected aggregate measurements

```json
{
  "actual_GPU_execution": true,
  "mock_action_calibration": {
    "calibration_cases": 80,
    "calibration_correct_decisions": 65,
    "calibration_unsafe_allows": 15,
    "correct_allow_retention": null,
    "hardware_guards_passed": true,
    "holdout_GPU_j_A_approx": null,
    "holdout_GPU_j_B_approx": null,
    "holdout_abstentions": null,
    "holdout_comparison_performed": false,
    "holdout_pairs": 0,
    "holdout_request_wall_A_s": null,
    "holdout_request_wall_B_s": null,
    "holdout_unsafe_allows_A": null,
    "holdout_unsafe_allows_B": null,
    "model_starts": 1,
    "original12_quality_cases": 0,
    "peak_device_vram_mib": 7346.5,
    "requests": 80,
    "screen_passed": false,
    "thresholds_fitted": 0,
    "underlying_holdout_decisions_equal": null,
    "winner_qualified": false
  },
  "model_starts": 1,
  "peak_device_vram_mib": 7346.5,
  "requests": 80
}
```
