# Pipeline Performance

**Verified snapshot: 2026-10-25T21:52:22.304360+00:00. This static page is not a live monitor.**

Last observed: R540 · AUDITED_RESULT_AVAILABLE.

| Experiment | Status | Tasks completed / planned | Startup s | Task s | CPU unit s | CI build / deploy s |
|---|---|---|---|---|---|---|
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

</details>

Only recorded phase windows are shown. Unknown preparation, broker-wait and cloud-wait durations are not estimated. Pending admission is not inferred from a queue entry. [Methodology](methodology.md) · [Research archive](archive.md).
