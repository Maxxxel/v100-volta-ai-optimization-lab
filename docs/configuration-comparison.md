# Model benchmarks

Coding, tools and agents on one V100. Complete, locally qualified results only; click a score for its configuration and audit.

<div id="all-measured-results" aria-live="polite"></div>

<details><summary>Reading the comparison</summary>

HumanEval+164 · BFCL parallel_multiple200 (category only) · Terminal-Bench2.1 (not yet measured). Missing values are not zero. **Ø Benchmarks** averages available complete category percentages for the same configuration, with coverage n/3; it is not an official overall benchmark. Different coverage or protocols do not establish model superiority.

Task budget: **1,200 seconds total**, shared across parts; startup and wrapper limits are separate. Historical/partial results remain in the [archive](configuration-archive.md).

</details>

<details><summary>Scientific provenance and reproduction</summary>



Model names and file names are not proof of architecture, parameter count, QAT, SVD, original weights or the executed kernel. Requested flags and verified execution remain separate fields. Engine versions are never substituted with build hashes. Newly discovered fields automatically become selectable; historical fields are supplemented only through hash-bound evidence annotations; immutable profiles and results are never rewritten. Historical server logs reporting `build 0 (unknown)` cannot establish an upstream release or Git commit. Build IDs, executable hashes and CUDA-library hashes remain separate identities.

- Recorded field: model.hf_revision · Profiles with a value: 26 · Profiles without a value: 8
- Recorded field: model.hf_repository · Profiles with a value: 26 · Profiles without a value: 8
- Recorded field: model.parameter_count · Profiles with a value: 0 · Profiles without a value: 34
- Recorded field: model.qat · Profiles with a value: 0 · Profiles without a value: 34
- Recorded field: model.svd · Profiles with a value: 0 · Profiles without a value: 34
- Recorded field: model.architecture · Profiles with a value: 33 · Profiles without a value: 1
- Recorded field: engine.version · Profiles with a value: 0 · Profiles without a value: 34
- Recorded field: engine.git_commit · Profiles with a value: 0 · Profiles without a value: 34
- Recorded field: engine.fork_repository · Profiles with a value: 0 · Profiles without a value: 34
- Recorded field: engine.cuda_version · Profiles with a value: 0 · Profiles without a value: 34
- Recorded field: engine.driver_version · Profiles with a value: 0 · Profiles without a value: 34
- Recorded field: engine.executed_kernel_backend_path · Profiles with a value: 0 · Profiles without a value: 34
- Recorded field: runtime.thinking_level · Profiles with a value: 0 · Profiles without a value: 34
- Recorded field: runtime.reasoning_budget_tokens · Profiles with a value: 0 · Profiles without a value: 34
- Recorded field: optimizations.speculation_effective · Profiles with a value: 0 · Profiles without a value: 34
- Recorded field: optimizations.flash_attention_effective · Profiles with a value: 0 · Profiles without a value: 34
- Recorded field: optimizations.cuda_graphs.actual_capture_replay · Profiles with a value: 0 · Profiles without a value: 34
- Recorded field: engine.source_base_commit · Profiles with a value: 34 · Profiles without a value: 0
- Recorded field: engine.source_version_label · Profiles with a value: 34 · Profiles without a value: 0

Coverage counts above refer to capture profiles measured on the three selected category benchmarks before identical inference configurations are joined. Original captures and other benchmarks remain archived. A capture ID, audit hash or descriptive run label is not an inference parameter. Only broker-captured profiles with matching model bytes, engine/kernel builds, full ordered launch flags, inference runtime, optimization and observed sampling settings are joined. Evaluation-only HTTP, startup, scoring and collection time limits do not create a new inference configuration; their original per-run identities and limits remain available. Tool-choice adapter settings remain attached to their benchmark evidence; conflicting tool settings remain separate. Unknown identities never establish equivalence. **Engine-Version / Quellstand** shows a recorded release when available, otherwise the independently linked source-base commit plus local patch variant. A source revision is not an invented upstream release tag. Matching requires the build, server SHA256 and CUDA-library SHA256; shared executable bytes alone cannot establish identical kernels. Source receipts and patch lineage are linked in each profile; unknown historical release tags stay unknown. OmniCoder V1/V2 naming is unified as **OmniCoder 9B** in the display while immutable original labels and separate measured configurations are preserved. Additional column-picker fields expose pinned observed sampler/template controls and per-benchmark timing/energy provenance. TTFT remains unrecorded for non-streaming replies; prompt evaluation time is not TTFT. GPU J/output token includes prefill energy in the same case window.

Explicit presentation fields use only recorded options: MTP is true for `draft-mtp`, false for explicit `none`, and unknown otherwise. Thinking mode uses an explicit `enable_thinking` template boolean; a reasoning-parser flag does not prove thinking mode. Model names, optimization-knob zero values and absent flags never establish effective execution.

Prefill/decode/TTFT and other costs are shown only where the original run actually records them. Request wall time is not silently renamed total system latency. Per-benchmark metrics remain available. Compact performance summaries use the same available category results as the displayed mean: decode is total output tokens divided by total decode time, latency and output tokens are per evaluated task, GPU energy is per successful task including failed-task costs, and VRAM is the maximum session peak. Missing component metrics remain unknown; incompatible energy methods are not mixed. Counter-energy bounds are retained; sorting uses the upper bound explicitly. These workload-dependent summaries are not controlled speed or energy rankings across different coverage or tokenizers. CSV exports all filtered rows with the currently selected columns, complete identities and available audit links. CSV formula-like text is escaped.

The Top-5 analysis describes observed configurations and missing coverage. Suggested controlled A/B work is a research hypothesis, not a causal explanation, predicted speedup or automatic GPU authorization.

[Immutable configuration history](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/blob/main/data/configuration-history.json) · [Benchmark definitions and publisher evidence](benchmark-register.md) · [Original experiments](results.md)

## Provenance gaps — excluded from reconstructed profiles

- Experiment: R408 · Reason: Current historical plan differs from its original precheck pin; configuration not reconstructed from mismatched bytes. Original audit remains preserved. · Original audit: [audit-74e8e58e72e5b8769e71](audits/audit-74e8e58e72e5b8769e71.md)

## UI reproduction checks

Run `python -m unittest discover -s scripts` and `node --test scripts/test_master_table.cjs` with Node.js 22 or newer. The optional real-browser acceptance script is `scripts/test_master_browser.cjs`: it accepts a site root URL and artifact directory and uses Playwright 1.64.1. Browser screenshots, CSVs and reports belong outside the public export tree. It runs with GPU rendering disabled. Development asset overrides are explicitly reported and must be disabled for the final published-site check.

Filters accept substrings, `=value`, `!=value`, numeric comparisons such as `>=80`, and `?` for unknown. The CSV always includes immutable configuration IDs, all filtered rows, the currently visible columns and the exact identities of displayed family protocols and the per-row protocols actually included in the available-results mean, with its coverage and policy. Long field values can be inspected directly in a table dialog without leaving the page.


</details>
