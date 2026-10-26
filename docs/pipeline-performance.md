# Pipeline Performance

**Verified snapshot: 2026-10-26T11:45:57.795690+00:00. This static page is not a live monitor.**

Last observed: R550 · AUDITED_RESULT_AVAILABLE.

| Experiment | Status | Tasks completed / planned | Startup s | Task s | CPU unit s | CI build / deploy s |
|---|---|---|---|---|---|---|
| [R550](experiments/R550.md) | COMPLETE | 33/33 | 117.701 | 621.917 | 11.61 | NOT MEASURED / NOT MEASURED |
| [R549](experiments/R549.md) | COMPLETE | 200/200 | 125.374 | 737.137 | 0.391 | NOT MEASURED / NOT MEASURED |
| [R548](experiments/R548.md) | COMPLETE | 164/164 | 103.223 | 599.39 | NOT MEASURED | NOT MEASURED / NOT MEASURED |
| [R547](experiments/R547.md) | COMPLETE | 32/32 | 169.93 | 85.771 | NOT MEASURED | NOT MEASURED / NOT MEASURED |
| [R546](experiments/R546.md) | COMPLETE | 400/400 | 74.774 | 818.456 | NOT MEASURED | NOT MEASURED / NOT MEASURED |
| [R545](experiments/R545.md) | COMPLETE | 32/32 | 59.144 | 601.23 | NOT MEASURED | NOT MEASURED / NOT MEASURED |
| [R544](experiments/R544.md) | COMPLETE | 164/164 | 90.856 | 794.734 | NOT MEASURED | 101.0 / 9.0 |
| [R543](experiments/R543.md) | COMPLETE | 33/33 | 76.467 | 291.735 | 11.483 | 101.0 / 9.0 |
| [R542](experiments/R542.md) | COMPLETE | 200/200 | 77.661 | 304.769 | 0.39 | 99.0 / 12.0 |
| [R541](experiments/R541.md) | COMPLETE | 164/164 | 76.322 | 350.48 | NOT MEASURED | 101.0 / 9.0 |
| [R540](experiments/R540.md) | COMPLETE | 64/64 | 73.986 | 117.603 | NOT MEASURED | NOT MEASURED / NOT MEASURED |
| [R539](experiments/R539.md) | COMPLETE | 32/32 | 77.515 | 43.946 | NOT MEASURED | 79.0 / 11.0 |
| [R538](experiments/R538.md) | PARTIAL | 199/200 | 157.935 | NOT MEASURED | 0.396 | 98.0 / 10.0 |
| [R537](experiments/R537.md) | COMPLETE | 15/15 | 94.459 | 214.07 | 2.034 | 103.0 / 12.0 |
| [R536](experiments/R536.md) | COMPLETE | 33/33 | 64.991 | 401.671 | 1.418 | 102.0 / 9.0 |
| [R535](experiments/R535.md) | COMPLETE | 33/33 | 51.961 | 407.791 | 1.447 | 107.0 / 17.0 |
| [R534](experiments/R534.md) | COMPLETE | 33/33 | 60.064 | 444.22 | 1.495 | NOT MEASURED / NOT MEASURED |
| [R533](experiments/R533.md) | COMPLETE | 33/33 | 165.62 | 759.431 | 1.372 | 58.0 / 18.0 |
| [R532](experiments/R532.md) | COMPLETE | 33/33 | 93.987 | 328.884 | 1.448 | 58.0 / 18.0 |
| [R531](experiments/R531.md) | COMPLETE | 33/33 | 61.527 | 319.983 | 1.363 | 58.0 / 18.0 |
| [R530](experiments/R530.md) | COMPLETE | 33/33 | 97.915 | 447.17 | 5.046 | 98.0 / 17.0 |

Startup includes admission, loading and warm-up. CPU unit sums can include failed diagnostics; they are not total overhead. CI may overlap later experiments. Missing task-end receipts remain unknown, including R538. Between-experiment gaps are not measured GPU idle time or cloud downtime.

**Confirmed publication blocker:** an interactive process held the publication lock for 6373.85 seconds. The lock was released. This blocked publication, not an already running GPU job. Uncommitted documentation was an additional gate. Publication locks must remain scoped to one bounded process.

Automation reuses the existing collector and publication timer: isolated CPU scoring/replay, hash checks, export, tests, commit and push. Publication failures cannot start or repeat GPU jobs. Push retries and deployment checks are bounded. New GPU work still requires its reviewed broker contract.

<details><summary>Measured CPU publication phases</summary>

| Experiment | Phase | Status | Seconds |
|---|---|---|---|
| R539 | integrity | COMPLETE | 0.042 |
| R539 | export | COMPLETE | 26.522 |
| R539 | render | COMPLETE | 1.221 |
| R539 | tests | COMPLETE | 2.808 |
| R539 | tests | COMPLETE | 2.152 |
| R539 | security | COMPLETE | 12.214 |
| R539 | build | COMPLETE | 40.107 |
| R539 | commit | COMPLETE | 0.112 |
| R539 | security | COMPLETE | 11.842 |
| R539 | push | COMPLETE | 3.084 |
| R540 | export | COMPLETE | 28.228 |
| R540 | render | COMPLETE | 1.218 |
| R540 | tests | COMPLETE | 2.922 |
| R540 | tests | COMPLETE | 2.321 |
| R540 | security | COMPLETE | 12.39 |
| R540 | build | COMPLETE | 40.195 |
| R540 | security | COMPLETE | 11.842 |
| R540 | commit | COMPLETE | 0.068 |
| R540 | push | COMPLETE | 2.887 |
| R540 | commit | COMPLETE | 0.111 |
| R540 | security | COMPLETE | 11.842 |
| R540 | push | COMPLETE | 2.836 |
| R541 | collect | FAILED | 24.06 |
| R541 | export | COMPLETE | 28.326 |
| R541 | render | COMPLETE | 1.269 |
| R541 | tests | COMPLETE | 2.722 |
| R541 | tests | COMPLETE | 2.22 |
| R541 | security | COMPLETE | 12.341 |
| R541 | build | COMPLETE | 40.145 |
| R541 | security | COMPLETE | 11.844 |
| R541 | commit | COMPLETE | 0.037 |
| R541 | push | COMPLETE | 3.638 |
| R541 | collect | COMPLETE | 0.079 |
| R541 | independent_review | COMPLETE | 23.128 |
| R541 | integrity | COMPLETE | 1.044 |
| R541 | export | COMPLETE | 26.773 |
| R541 | render | COMPLETE | 1.269 |
| R541 | tests | COMPLETE | 2.722 |
| R541 | tests | COMPLETE | 2.17 |
| R541 | security | COMPLETE | 12.392 |
| R541 | build | COMPLETE | 39.794 |
| R541 | security | COMPLETE | 11.891 |
| R541 | commit | COMPLETE | 0.024 |
| R541 | push | COMPLETE | 3.49 |
| R541 | export | COMPLETE | 26.371 |
| R541 | render | COMPLETE | 1.268 |
| R541 | tests | COMPLETE | 2.872 |
| R541 | tests | COMPLETE | 2.17 |
| R541 | security | COMPLETE | 12.29 |
| R541 | build | COMPLETE | 40.345 |
| R541 | export | COMPLETE | 26.371 |
| R541 | render | COMPLETE | 1.268 |
| R541 | tests | COMPLETE | 2.871 |
| R541 | tests | COMPLETE | 2.17 |
| R541 | security | COMPLETE | 12.29 |
| R541 | build | COMPLETE | 40.143 |
| R541 | security | COMPLETE | 11.892 |
| R541 | commit | COMPLETE | 0.024 |
| R541 | push | COMPLETE | 3.542 |
| R542 | collect | COMPLETE | 3.588 |
| R542 | integrity | COMPLETE | 0.071 |
| R542 | security | COMPLETE | 11.892 |
| R542 | push | COMPLETE | 1.447 |
| R543 | collect | FAILED | 0.399 |
| R543 | export | FAILED | 27.424 |
| R544 | collect | FAILED | 0.096 |
| R543 | independent_review | COMPLETE | 5.039 |
| R544 | security | COMPLETE | 12.028 |
| R544 | push | COMPLETE | 3.841 |
| R545 | collect | COMPLETE | 5.304 |
| R545 | security | COMPLETE | 12.009 |
| R545 | push | COMPLETE | 3.139 |
| R546 | collect | COMPLETE | 3.343 |
| R546 | security | COMPLETE | 11.943 |
| R546 | push | COMPLETE | 3.037 |
| R547 | collect | COMPLETE | 5.544 |
| R548 | collect | COMPLETE | 49.32 |
| R548 | independent_review | COMPLETE | 0.038 |
| R548 | integrity | COMPLETE | 0.043 |
| R549 | collect | COMPLETE | 2.318 |
| R549 | integrity | COMPLETE | 0.039 |
| R549 | security | COMPLETE | 12.094 |
| R549 | push | COMPLETE | 4.241 |
| R550 | collect | COMPLETE | 2.762 |
| R550 | independent_review | COMPLETE | 1.2 |

</details>

Only recorded phase windows are shown. Unknown preparation, broker-wait and cloud-wait durations are not estimated. Pending admission is not inferred from a queue entry. [Methodology](methodology.md) · [Research archive](archive.md).
