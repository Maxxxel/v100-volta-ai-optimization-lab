# Model Comparison & Benchmarks

<div class="hero"><strong>One result. One exact configuration. One verified protocol.</strong><p>Local official highscores, with full provenance. Publisher claims and laboratory subsets stay separate.</p></div>

Only complete runs passing the task-set, official-scorer, canonical-control and independent-audit gates enter these rankings. **NOT MEASURED** means no eligible result, not zero ability. Different benchmark versions never share a ranking. No cross-discipline overall score is calculated.

<div id="official-leaderboard" aria-live="polite"></div>

## Current admission status

0 eligible official runs. The 27 projected result groups remain available in [supplemental comparisons](supplemental-comparison.md) and the [configuration comparison](configuration-comparison.md). 246 content-addressed profiles and 219 additional audited configuration attempts are preserved; these are **not** counts of qualified optimizations or distinct GPU jobs.

| Local cohort | Official admission | Reason |
| --- | --- | --- |
| coding | SUPPLEMENTAL_SCORER_EXCEPTION | All164 answers observed, but original calibration leaves HumanEval/32 invalid and only163 primary tasks validated. No full-conformance official admission. |
| mbpp | SUPPLEMENTAL_SUBSET | 223 observed of378 official release tasks; local original-test filter and Mbpp/255 exclusion retained. |
| tools | SUPPLEMENTAL_SUBSET | 100 frozen static questions in5 categories, not the full official v4 category manifest/aggregation. |

## Next evidence gaps

| Priority | Technical decision / next step | GPU initially required |
| --- | --- | --- |
| P0 | Resolve HumanEval/32 with official reference/scorer calibration in CPU isolation, then rescore archived model answers if definitions remain identical. Preserve old scores with a new correction audit. | False |
| P1 | Admit full BFCLv4 manifest, scorer and categories before new full-tool runs. Keep native100 as pilot. | False |
| P1 | Assess missing155 MBPP+ tasks and resource-failed task with official scorer before deciding whether a full378 run is practical. Reuse all valid stored answers; no test-driven parameter tuning. | False |
| P2 | SWE-bench/Terminal-Bench isolated scaffold, disk/RAM and task-image admission; no production tools or implied128K support. | False |

[Benchmark definitions and publisher evidence](benchmark-register.md) · [Local agent and synthetic tests](local-benchmarks.md) · [Reproduction](reproduce.md)

Each profile records unknown fields as null (**NOT MEASURED**). An absent MTP/graph/cache setting is never assumed off. No-MTP execution does not establish that weights are original. Actual kernel execution is distinct from a requested backend. Historical development suites were reused; no unseen-holdout or absence-of-overfitting claim is made.
