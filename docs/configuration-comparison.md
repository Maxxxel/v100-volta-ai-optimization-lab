# Model Comparison & Benchmark Results

One table for every measured configuration. Full and **PARTIAL** results share one column per benchmark family; every cell shows its actual **solved / evaluated** count and qualification. Missing values are never zero. Select a score to inspect its exact protocol, settings, runtime, energy and original audit.

The optional official-only filter excludes partial and unqualified results. The custom mean follows its selected exact protocols; partial task sets never silently enter the official mean. Different task subsets do not establish model superiority.

<div id="all-measured-results" aria-live="polite"></div>

<details>
<summary>Scientific provenance, parameter coverage and reproduction</summary>



Model names and file names are not proof of architecture, parameter count, QAT, SVD, original weights or the executed kernel. Requested flags and verified execution remain separate fields. Engine versions are never substituted with build hashes. Newly discovered fields automatically become selectable; historical fields are supplemented only through hash-bound evidence annotations; immutable profiles and results are never rewritten. Historical server logs reporting `build 0 (unknown)` cannot establish an upstream release or Git commit. Build IDs, executable hashes and CUDA-library hashes remain separate identities.

- Recorded field: model.hf_revision · Profiles with a value: 17 · Profiles without a value: 11
- Recorded field: model.hf_repository · Profiles with a value: 17 · Profiles without a value: 11
- Recorded field: model.parameter_count · Profiles with a value: 0 · Profiles without a value: 28
- Recorded field: model.qat · Profiles with a value: 0 · Profiles without a value: 28
- Recorded field: model.svd · Profiles with a value: 0 · Profiles without a value: 28
- Recorded field: model.architecture · Profiles with a value: 26 · Profiles without a value: 2
- Recorded field: engine.version · Profiles with a value: 0 · Profiles without a value: 28
- Recorded field: engine.git_commit · Profiles with a value: 0 · Profiles without a value: 28
- Recorded field: engine.fork_repository · Profiles with a value: 0 · Profiles without a value: 28
- Recorded field: engine.cuda_version · Profiles with a value: 0 · Profiles without a value: 28
- Recorded field: engine.driver_version · Profiles with a value: 0 · Profiles without a value: 28
- Recorded field: engine.executed_kernel_backend_path · Profiles with a value: 0 · Profiles without a value: 28
- Recorded field: runtime.thinking_level · Profiles with a value: 0 · Profiles without a value: 28
- Recorded field: runtime.reasoning_budget_tokens · Profiles with a value: 0 · Profiles without a value: 28
- Recorded field: optimizations.speculation_effective · Profiles with a value: 0 · Profiles without a value: 28
- Recorded field: optimizations.flash_attention_effective · Profiles with a value: 0 · Profiles without a value: 28
- Recorded field: optimizations.cuda_graphs.actual_capture_replay · Profiles with a value: 0 · Profiles without a value: 28
- Recorded field: engine.source_base_commit · Profiles with a value: 28 · Profiles without a value: 0
- Recorded field: engine.source_version_label · Profiles with a value: 28 · Profiles without a value: 0

Coverage counts above refer to the measured benchmark configurations shown in this table, excluding local-only supplemental profiles. **Engine-Version / Quellstand** shows a recorded release when available, otherwise the independently linked source-base commit plus local patch variant. A source revision is not an invented upstream release tag. Matching requires the build, server SHA256 and CUDA-library SHA256; shared executable bytes alone cannot establish identical kernels. Source receipts and patch lineage are linked in each profile; unknown historical release tags stay unknown. OmniCoder V1/V2 naming is unified as **OmniCoder 9B** in the display while immutable original labels and separate measured configurations are preserved. Additional column-picker fields expose pinned observed sampler/template controls and per-benchmark timing/energy provenance. TTFT remains unrecorded for non-streaming replies; prompt evaluation time is not TTFT. GPU J/output token includes prefill energy in the same case window.

Explicit presentation fields use only recorded options: MTP is true for `draft-mtp`, false for explicit `none`, and unknown otherwise. Thinking mode uses an explicit `enable_thinking` template boolean; a reasoning-parser flag does not prove thinking mode. Model names, optimization-knob zero values and absent flags never establish effective execution.

Prefill/decode/TTFT and other costs are shown only where the original run actually records them. Request wall time is not silently renamed total system latency. Performance columns are benchmark-specific, not pooled across unrelated tasks. CSV exports all filtered rows with the currently selected columns, complete identities and available audit links. CSV formula-like text is escaped.

The Top-5 analysis describes observed configurations and missing coverage. Suggested controlled A/B work is a research hypothesis, not a causal explanation, predicted speedup or automatic GPU authorization.

[Immutable configuration history](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/blob/main/data/configuration-history.json) · [Benchmark definitions and publisher evidence](benchmark-register.md) · [Original experiments](results.md)

## Provenance gaps — excluded from reconstructed profiles

- Experiment: R408 · Reason: Current historical plan differs from its original precheck pin; configuration not reconstructed from mismatched bytes. Original audit remains preserved. · Original audit: [audit-74e8e58e72e5b8769e71](audits/audit-74e8e58e72e5b8769e71.md)

## UI reproduction checks

Run `python -m unittest discover -s scripts` and `node --test scripts/test_master_table.cjs` with Node.js 22 or newer. The optional real-browser acceptance script is `scripts/test_master_browser.cjs`: it accepts a site root URL and artifact directory and uses Playwright 1.64.1. Browser screenshots, CSVs and reports belong outside the public export tree. It runs with GPU rendering disabled. Development asset overrides are explicitly reported and must be disabled for the final published-site check.

Filters accept substrings, `=value`, `!=value`, numeric comparisons such as `>=80`, and `?` for unknown. The CSV always includes immutable configuration IDs, all filtered rows, the currently visible columns and the exact identities of displayed family protocols and protocols selected for the mean, including when their result is missing. Long field values can be inspected directly in a table dialog without leaving the page.


</details>
