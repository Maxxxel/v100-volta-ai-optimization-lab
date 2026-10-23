# Configuration Comparison & Benchmark Master Table

**Default: Alle gemessenen Ergebnisse.** One continuous row per immutable configuration appearing in `history.runs`, with no pagination. Official, historical, supplemental and unqualified measured results are visible together, in distinct protocol/status columns. Plans and result-free configuration attempts remain in the [separate archive](configuration-archive.md). Every recorded profile field and startup flag is available through the categorized column picker. Each benchmark column is bound to its exact register definition, dataset/task set, scorer and qualification track. Unknown means **NICHT ERFASST**, never off or zero. Failed and weaker configurations remain visible.

Use **Nur offiziell qualifizierte Ergebnisse** to optionally restrict the display. **Durchschnittsmodus** only changes which exact protocols may enter the user-selected mean; it does not hide historical measurements in the default table. The user-defined arithmetic mean is not an official benchmark score; every selected result must exist for the exact same configuration. Distinct original run observations use their arithmetic mean, with count and dispersion; admission-history duplicates do not create extra observations. Provenance-defined observation counts do not establish statistical independence. Conflicting judgments are excluded from numerical summaries.

<div id="all-measured-results" aria-live="polite"></div>

## Comparing individual measurements

<div id="configuration-comparison" aria-live="polite"></div>

## Data coverage and missing fields

Model names and file names are not proof of architecture, parameter count, QAT, SVD, original weights or the executed kernel. Requested flags and verified execution remain separate fields. Engine versions are never substituted with build hashes. Newly discovered fields automatically become selectable; historical fields are supplemented only through hash-bound evidence annotations; immutable profiles and results are never rewritten. Historical server logs reporting `build 0 (unknown)` cannot establish an upstream release or Git commit. Build IDs, executable hashes and CUDA-library hashes remain separate identities.

| Recorded field | Profiles with a value | Profiles without a value |
| --- | --- | --- |
| model.hf_revision | 13 | 15 |
| model.hf_repository | 13 | 15 |
| model.parameter_count | 0 | 28 |
| model.qat | 0 | 28 |
| model.svd | 0 | 28 |
| model.architecture | 25 | 3 |
| engine.version | 0 | 28 |
| engine.git_commit | 0 | 28 |
| engine.fork_repository | 0 | 28 |
| engine.cuda_version | 0 | 28 |
| engine.driver_version | 0 | 28 |
| engine.executed_kernel_backend_path | 0 | 28 |
| runtime.thinking_level | 0 | 28 |
| runtime.reasoning_budget_tokens | 0 | 28 |
| optimizations.speculation_effective | 0 | 28 |
| optimizations.flash_attention_effective | 0 | 28 |
| optimizations.cuda_graphs.actual_capture_replay | 0 | 28 |

Coverage counts above refer only to measured configurations. Additional column-picker fields expose pinned observed sampler/template controls, engine-reported build information and per-benchmark timing/energy provenance. TTFT remains unrecorded for non-streaming replies; prompt evaluation time is not TTFT. GPU J/output token includes prefill energy in the same case window.

Explicit presentation fields use only recorded options: MTP is true for `draft-mtp`, false for explicit `none`, and unknown otherwise. Thinking mode uses an explicit `enable_thinking` template boolean; a reasoning-parser flag does not prove thinking mode. Model names, optimization-knob zero values and absent flags never establish effective execution.

Prefill/decode/TTFT and other costs are shown only where the original run actually records them. Request wall time is not silently renamed total system latency. Performance columns are benchmark-specific, not pooled across unrelated tasks. CSV exports all filtered rows with the currently selected columns, complete identities and available audit links. CSV formula-like text is escaped.

The Top-5 analysis describes observed configurations and missing coverage. Suggested controlled A/B work is a research hypothesis, not a causal explanation, predicted speedup or automatic GPU authorization.

[Immutable configuration history](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/blob/main/data/configuration-history.json) · [Benchmark definitions and publisher evidence](benchmark-register.md) · [Original experiments](results.md)

## Provenance gaps — excluded from reconstructed profiles

| Experiment | Reason | Original audit |
| --- | --- | --- |
| R408 | Current historical plan differs from its original precheck pin; configuration not reconstructed from mismatched bytes. Original audit remains preserved. | [audit-74e8e58e72e5b8769e71](audits/audit-74e8e58e72e5b8769e71.md) |

## UI reproduction checks

Run `python -m unittest discover -s scripts` and `node --test scripts/test_master_table.cjs` with Node.js 22 or newer. The optional real-browser acceptance script is `scripts/test_master_browser.cjs`: it accepts a site root URL and artifact directory and uses Playwright 1.64.1. Browser screenshots, CSVs and reports belong outside the public export tree. It runs with GPU rendering disabled. Development asset overrides are explicitly reported and must be disabled for the final published-site check.

Filters accept substrings, `=value`, `!=value`, numeric comparisons such as `>=80`, and `?` for unknown. The CSV always includes immutable configuration IDs, all filtered rows and the currently visible columns. Long field values can be inspected directly in a table dialog without leaving the page.

