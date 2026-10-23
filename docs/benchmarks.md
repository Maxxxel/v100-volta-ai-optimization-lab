# Model Comparison & Benchmarks

<div class="hero"><strong>One result. One exact configuration. One verified protocol.</strong><p>Local official highscores, with full provenance. Publisher claims and laboratory subsets stay separate.</p></div>

Only complete runs passing the task-set, official-scorer, canonical-control and independent-audit gates enter these rankings. **NOT MEASURED** means no eligible result, not zero ability. Different benchmark versions never share a ranking. No cross-discipline overall score is calculated.

**Local official-benchmark API track.** This is an independent project ranking, not an entry on the benchmark authors’ leaderboard. Full164 HumanEval+ admissions preserve the exact official checker and pass@1 estimator through a streaming API adapter. The unchanged upstream HumanEval/32 canonical-reference residual anomaly is explicitly accounted for, with no dropped tasks or relaxed tolerance. Local scorer limits are 1GiB cgroup memory,805306368-byte per-process guard,one CPU,minimum1s/case and GT factor4. Publisher-protocol equivalence is not established. Scores are fixed-suite observations, not proof of overall model superiority.

**[All results & tuning configurations — searchable, sortable table](configuration-comparison.md#all-measured-results)** · [Historical detailed cohort table](supplemental-comparison.md#configuration-parameters-and-ranked-benchmark-results)

<div id="official-leaderboard" aria-live="polite"></div>

## Current admission status

7 eligible official runs under the declared local protocol. 37 versioned result records remain available in the [configuration comparison](configuration-comparison.md); these include preserved historical admission/protocol revisions of the same physical measurements. 249 content-addressed profiles and 223 additional audited configuration attempts are preserved; these are **not** counts of qualified optimizations or distinct GPU jobs. [Historical and subset comparisons](supplemental-comparison.md) remain accessible.

| Original local cohort classification | Historical scope | Reason before separate admission |
| --- | --- | --- |
| coding | SUPPLEMENTAL_SCORER_EXCEPTION | All164 answers observed, but original calibration leaves HumanEval/32 invalid and only163 primary tasks validated. No full-conformance official admission. |
| mbpp | SUPPLEMENTAL_SUBSET | 223 observed of378 official release tasks; local original-test filter and Mbpp/255 exclusion retained. |
| tools | SUPPLEMENTAL_SUBSET | 100 frozen static questions in5 categories, not the full official v4 category manifest/aggregation. |

## Archived response diagnostics

[OxCoder R448: output-cap and reasoning-channel investigation](oxcoder-diagnostic.md). Original scores and profile identities remain unchanged; this is a read-only explanation, not an optimized model result.

## Same-quantizer artifact comparison

[OmniCoder V1 / V2 from mradermacher: full tensor payload comparison](weight-integrity-same-quantizer.md). This is distinct from the earlier cross-quantizer comparison. Both reports and all historical benchmark results remain available.

## Earlier cross-quantizer artifact comparison

[OmniCoder V1 / V2: bartowski versus mradermacher](weight-integrity.md). Different quantized representations are measured; underlying checkpoint and fine-tuning identity remain inconclusive. Historical benchmark results are preserved.

## Next evidence gaps

| Priority | Technical decision / next step | GPU initially required |
| --- | --- | --- |
| P0_COMPLETE | All seven existing full164 model profiles independently replayed with exact official scoring functions. All1148 task outcomes confirmed, with both base and plus checks. Known unchanged upstream canonical32 anomaly explicitly admitted without exclusions/tolerance changes. Local evaluation limits and publisher-protocol separation remain mandatory. | False |
| P1 | Admit full BFCLv4 manifest, scorer and categories before new full-tool runs. Keep native100 as pilot. | False |
| P1 | Assess missing155 MBPP+ tasks and resource-failed task with official scorer before deciding whether a full378 run is practical. Reuse all valid stored answers; no test-driven parameter tuning. | False |
| P2 | SWE-bench/Terminal-Bench isolated scaffold, disk/RAM and task-image admission; no production tools or implied128K support. | False |

[Benchmark definitions and publisher evidence](benchmark-register.md) · [Local agent and synthetic tests](local-benchmarks.md) · [Reproduction](reproduce.md)

Each profile records unknown fields as null (**NOT MEASURED**). An absent MTP/graph/cache setting is never assumed off. No-MTP execution does not establish that weights are original. Actual kernel execution is distinct from a requested backend. Historical development suites were reused; no unseen-holdout or absence-of-overfitting claim is made.
