# Supplemental model comparisons


> **SUPPLEMENTAL / HISTORICAL EVIDENCE.** BFCL static100 and MBPP+223 are frozen subsets. Original HumanEval+ records retain their historical scope here; independently verified full164 API admissions appear in [official local highscores](benchmarks.md), with the unchanged upstream reference anomaly and local evaluation limits disclosed. No combined percentage mean is calculated.

<div class="hero"><strong>Measured tasks. Visible trade-offs.</strong><p>Separate coding, native tools and agent results on one V100. No combined score and no automatic winner.</p></div>

- No mean is calculated across subsets or incompatible protocols.
- Whole configurations: model, tokenizer, native template, output budget, sampling, quantization and engine can differ. Task/scorer matching permits comparison of these profiles, not causal architecture claims.
- GPU board energy includes failed task attempts; excludes load/warmup and CPU/system energy. Latency is measured request/case time; startup and judge time are excluded.
- NOT MEASURED means no full comparable audited result in this cohort. Partial screens are not converted into full-suite scores.

Charts run from best measured value at the top to worst at the bottom: success/throughput descending; latency/energy/VRAM ascending. Missing measurements follow all measured values. Ties retain a stable profile order. Teal bars are measured values; amber identifies a recorded policy warning. NOT MEASURED is never plotted as zero. The tables below each cohort provide exact profile metadata and original audit hashes. Error bars are omitted for single runs; repeated-cycle min–max and historical median absolute deviation (MAD) are labelled explicitly.

Measurement-only fingerprint: `4c76e5c1cfd545d9fd7ac75c4353f5f7d7bef2f87991231122e4b5471493010c`. Charts change when these audited measurements/conditions change, independently of matrix revision. New full-suite results are admitted through the existing canonical benchmark reference registry after audit; changed task identities fail the cohort gate rather than silently entering a ranking. Download the [validated aggregate dataset](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/blob/main/data/comparison.json).

## Supplemental cohort overview

Frozen subsets and historical full-suite records remain visible. Current official API admissions are separate; no cross-benchmark mean is computed.

| Model / quantization | HumanEval+164 historical | BFCL v4 static100 subset | MBPP+223 subset |
|---|---|---|---|
| OmniCoder2 9B / Q6_K | 132/164 (80.49%) [R217](experiments/R217.md) | 88/100 (88.00%) [R183](experiments/R183.md) | 162/223 (72.65%) [R415](experiments/R415.md) |
| Qwen3.5 9B / Q4_K_M | 132/164 (80.49%) [R255](experiments/R255.md) | 87/100 (87.00%) [R227](experiments/R227.md) | NOT MEASURED |
| Qwen3.8 27B / GSQ/RCO IQ3_S | 150/164 (91.46%) [R118](experiments/R118.md) | NOT MEASURED | 172/223 (77.13%) [R416](experiments/R416.md) |
| Ornith 1.5 9B / Q6_K | 117/164 (71.34%) [R254](experiments/R254.md) | NOT MEASURED | NOT MEASURED |
| Ternary Bonsai 2 27B / PQ2_0 | 151/164 (92.07%) [R279](experiments/R279.md) | 90/100 (90.00%) [R281](experiments/R281.md) | NOT MEASURED |
| OxCoder 9B / Q6_K | NOT MEASURED | NOT MEASURED | NOT MEASURED |
| Gemma4 12B IT QAT / Q4_0 | 149/164 (90.85%) [R425](experiments/R425.md) | 84/100 (84.00%) [R424](experiments/R424.md) | 168/223 (75.34%) [R428](experiments/R428.md) |
| LFM2.5 8B A1B / Q6_K | NOT MEASURED | NOT MEASURED | NOT MEASURED |
| MiMo V2.6 Distill Qwen 9B / See admission record | NOT MEASURED | NOT MEASURED | NOT MEASURED |
| Qwen3.6 27B / See admission record | NOT MEASURED | NOT MEASURED | NOT MEASURED |
| LFM2.5 24B A2B QAD / See admission record | NOT MEASURED | NOT MEASURED | NOT MEASURED |
| LightOnOCR 3 4B / See admission record | NOT MEASURED | NOT MEASURED | NOT MEASURED |
| UI-Venus 1.5 8B / Holo2 8B / See admission record | NOT MEASURED | NOT MEASURED | NOT MEASURED |
| Qwen3.8 Flash-MTP-Derivat / See admission record | NOT MEASURED | NOT MEASURED | NOT MEASURED |

All 14 baseline/candidate tracks remain visible. Partial or research-only models have NOT MEASURED entries until complete comparable runs exist. The official-agent category is currently NOT MEASURED locally; our own agent tests are [supplemental laboratory evidence](local-benchmarks.md), not a substitute for an official agent benchmark.

## Configuration parameters and ranked benchmark results

Each row is one audited supplemental discipline/profile. **Ranks are calculated only within the same task cohort**, using solved/tasks, descending, with equal rates sharing a rank. They are not allround model rankings. The optimization/profile column describes the actual tested configuration; full controls and hashes appear in the chart metadata sections below.

| Task cohort | Rank within cohort | Model | Quant | Success | Request wall s | GPU J / success | VRAM MiB | Engine | Build | Thinking | MTP | Draft max | Flash attention | KV K | KV V | HBM MiB | Context | Output | Batch | Microbatch | Threads | Temperature | Top-p | Top-k | Min-p | Seed | Power W | Warning | Audit / full settings |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| coding | 1 | Ternary Bonsai 2 27B | PQ2_0 | 151/164 (92.1%) | 2519.755 | 4601.69 | 8158.5 | llama.cpp | bonsai-pq2-s | on | none | NOT MEASURED | on | f16 | f16 | 0 | 8192 | 4096 | 2048 | 512 | 6 | 1.0 | 0.95 | 20 | 0.05 | 1001 | 300 | NOT MEASURED | [R279](experiments/R279.md) |
| coding | 2 | Qwen3.8 27B | GSQ/RCO IQ3_S | 150/164 (91.5%) | 575.610 | 1053.96 | NOT MEASURED | llama.cpp | dded13c80bc8 | off | draft-mtp | 3 | auto | f16 | f16 | NOT MEASURED | 8192 | 1024 | 2048 | 512 | 6 | 0 | NOT MEASURED | NOT MEASURED | NOT MEASURED | 1001 | 300 | MTP target-token identity is not lossless; no allround qualification | [R118](experiments/R118.md) |
| coding | 3 | Gemma4 12B IT QAT | Q4_0 | 149/164 (90.9%) | 741.044 | 1234.65 | 8118.5 | llama.cpp | dded13c80bc8 | off | none | NOT MEASURED | auto | f16 | f16 | 0 | 8192 | 1024 | 2048 | 512 | 6 | 1.0 | 0.95 | 64 | 0.0 | 1001 | 300 | NOT MEASURED | [R425](experiments/R425.md) |
| coding | 4 | Qwen3.8 27B | GSQ/RCO IQ3_S | 148/164 (90.2%) | 1095.974 | 2107.33 | NOT MEASURED | llama.cpp | dded13c80bc8 | off | none | NOT MEASURED | auto | f16 | f16 | NOT MEASURED | 8192 | 1024 | 2048 | 512 | 6 | 0 | NOT MEASURED | NOT MEASURED | NOT MEASURED | 1001 | 300 | NOT MEASURED | [R117](experiments/R117.md) |
| coding | 5 | OmniCoder2 9B | Q6_K | 132/164 (80.5%) | 268.206 | 563.38 | 14106.5 | llama.cpp | bbae88916812 | off | draft-mtp | 3 | on | f16 | f16 | 6144 | 8192 | 1024 | 2048 | 512 | 6 | 0 | NOT MEASURED | NOT MEASURED | NOT MEASURED | 1001 | 300 | NOT MEASURED | [R217](experiments/R217.md) |
| coding | 5 | Qwen3.5 9B | Q4_K_M | 132/164 (80.5%) | 452.206 | 930.19 | 5956.5 | llama.cpp | dded13c80bc8 | off | NOT MEASURED | NOT MEASURED | on | f16 | f16 | NOT MEASURED | 8192 | 1024 | 2048 | 512 | 6 | 0 | NOT MEASURED | NOT MEASURED | NOT MEASURED | 1001 | 300 | NOT MEASURED | [R255](experiments/R255.md) |
| coding | 7 | Ornith 1.5 9B | Q6_K | 117/164 (71.3%) | 456.936 | 1116.98 | 7356.5 | llama.cpp | dded13c80bc8 | off | none | NOT MEASURED | on | f16 | f16 | NOT MEASURED | 8192 | 1024 | 2048 | 512 | 6 | 0 | NOT MEASURED | NOT MEASURED | NOT MEASURED | 1001 | 300 | NOT MEASURED | [R254](experiments/R254.md) |
| mbpp | 1 | Qwen3.8 27B | GSQ/RCO IQ3_S | 172/223 (77.1%) | 477.232 | 742.14 | 13616.5 | llama.cpp | dded13c80bc8 | off | draft-mtp | 3 | on | f16 | f16 | NOT MEASURED | 8192 | 1024 | 2048 | 512 | 6 | 0.0 | NOT MEASURED | NOT MEASURED | NOT MEASURED | 1001 | 300 | Known native-tool/policy limitations remain; coding only, no allround or lossless claim. | [R416](experiments/R416.md) |
| mbpp | 2 | Gemma4 12B IT QAT | Q4_0 | 168/223 (75.3%) | 877.635 | 1286.10 | 8118.5 | llama.cpp | dded13c80bc8 | off | none | NOT MEASURED | auto | f16 | f16 | 0 | 8192 | 1024 | 2048 | 512 | 6 | 1.0 | 0.95 | 64 | 0.0 | 1001 | 300 | Native-tool84/100 and agent9/18 with additional policy faults retained; coding results do not qualify an assistant. | [R428](experiments/R428.md) |
| mbpp | 3 | OmniCoder2 9B | Q6_K | 162/223 (72.6%) | 487.010 | 850.49 | 7364.5 | llama.cpp | dded13c80bc8 | off | none | NOT MEASURED | on | f16 | f16 | NOT MEASURED | 8192 | 1024 | 2048 | 512 | 6 | 0.0 | NOT MEASURED | NOT MEASURED | NOT MEASURED | 1001 | 300 | NOT MEASURED | [R415](experiments/R415.md) |
| tools | 1 | Ternary Bonsai 2 27B | PQ2_0 | 90/100 (90.0%) | 593.425 | 1773.91 | 8158.5 | llama.cpp | bonsai-pq2-s | on | none | NOT MEASURED | on | f16 | f16 | 0 | 8192 | 4096 | 2048 | 512 | 6 | 1.0 | 0.95 | 20 | 0.05 | 1001 | 300 | NOT MEASURED | [R281](experiments/R281.md) |
| tools | 2 | OmniCoder2 9B | Q6_K | 88/100 (88.0%) | 107.007 | 311.81 | NOT MEASURED | llama.cpp | dded13c80bc8 | off | draft-mtp | 3 | auto | f16 | f16 | NOT MEASURED | 8192 | 1024 | 2048 | 512 | 6 | 0 | NOT MEASURED | NOT MEASURED | NOT MEASURED | 1001 | 300 | NOT MEASURED | [R183](experiments/R183.md) |
| tools | 3 | Qwen3.5 9B | Q4_K_M | 87/100 (87.0%) | 123.930 | 374.01 | 5956.5 | llama.cpp | dded13c80bc8 | off | NOT MEASURED | NOT MEASURED | on | f16 | f16 | NOT MEASURED | 8192 | NOT MEASURED | 2048 | 512 | 6 | 0 | NOT MEASURED | NOT MEASURED | NOT MEASURED | 1001 | 300 | NOT MEASURED | [R227](experiments/R227.md) |
| tools | 4 | Gemma4 12B IT QAT | Q4_0 | 84/100 (84.0%) | 144.726 | 412.35 | 8118.5 | llama.cpp | dded13c80bc8 | off | none | NOT MEASURED | auto | f16 | f16 | NOT MEASURED | 8192 | 1024 | 2048 | 512 | 6 | 1.0 | 0.95 | 64 | 0.0 | 1001 | 300 | NOT MEASURED | [R424](experiments/R424.md) |

Ranking metric: task pass rate for this cohort only. Time includes failed attempts; GPU energy per success divides the whole suite energy by successful tasks. Warnings remain visible even for high scores. Missing values are never zero.

## Coding · HumanEvalPlus

HumanEvalPlus frozen 164; base AND plus; HumanEval/32 known invalid retained as failure (163 subset is separate).

Task identity: `cc7377147a38ea139e77745d18fcc35c267dd192d4b99c89d8a4e653ef4d39d5`. **Task-matched whole-configuration comparisons**; native sampling, budgets and builds are shown below. These are development results, with no repeated-seed model-superiority claim. Record dates come from the original audit or frozen plan; missing dates remain labelled.

![Coding · HumanEvalPlus: Successful tasks; missing results labelled NOT MEASURED](assets/benchmarks/coding-success.svg){ .benchmark-svg }

![Coding · HumanEvalPlus: Mean task E2E; missing results labelled NOT MEASURED](assets/benchmarks/coding-latency.svg){ .benchmark-svg }

![Coding · HumanEvalPlus: GPU energy per success; missing results labelled NOT MEASURED](assets/benchmarks/coding-energy.svg){ .benchmark-svg }

![Coding · HumanEvalPlus: Peak device VRAM; missing results labelled NOT MEASURED](assets/benchmarks/coding-vram.svg){ .benchmark-svg }

| Profile / record date | Success | Successful tasks/s | Total task time / GPU energy | Peak VRAM | Audit |
|---|---|---|---|---|---|
| OmniCoder2 9B Q6_K — MTP + weight cache; fast / 2026-10-20 | 132/164 | 0.49216 | 268.206 s / 74366.52 J | 14106.5 | [R217](experiments/R217.md) |
| Ornith 1.5 9B Q6_K — Fast non-reasoning / 2026-10-20 | 117/164 | 0.25605 | 456.936 s / 130686.39 J | 7356.5 | [R254](experiments/R254.md) |
| Qwen3.5 9B Q4_K_M — Fast non-reasoning / 2026-10-20 | 132/164 | 0.29190 | 452.206 s / 122784.66 J | 5956.5 | [R255](experiments/R255.md) |
| Gemma4 12B IT QAT Q4_0 — Fast non-reasoning / 2026-10-22 | 149/164 | 0.20107 | 741.044 s / 183962.59 J | 8118.5 | [R425](experiments/R425.md) |
| Qwen3.8 27B GSQ/RCO IQ3_S — Fast; no MTP / NOT RECORDED | 148/164 | 0.13504 | 1095.974 s / 311884.76 J | NOT MEASURED | [R117](experiments/R117.md) |
| Qwen3.8 27B GSQ/RCO IQ3_S — Fast; MTP3 / NOT RECORDED | 150/164 | 0.26059 | 575.610 s / 158094.20 J | NOT MEASURED | [R118](experiments/R118.md) |
| Ternary Bonsai 2 27B PQ2_0 — Thinking medium; 4096 output / 2026-10-21 | 151/164 | 0.05993 | 2519.755 s / 694855.82 J | 8158.5 | [R279](experiments/R279.md) |

### OmniCoder2 9B · Q6_K · R217

MTP + weight cache; fast. No additional policy claim is inferred from this discipline.

| Condition | Audited value |
|---|---|
| Separate process-VRAM observation (not device peak) | NOT MEASURED |
| Hardware / power | Tesla V100-SXM2 16 GB HBM2 / 300 W |
| Engine | llama.cpp / CUDA 12.8 / SM70 (exact audited binary below) |
| Date | 2026-10-20 |
| Context, batching, KV, speculation | {&quot;--batch-size&quot;: &quot;2048&quot;, &quot;--cache-type-k&quot;: &quot;f16&quot;, &quot;--cache-type-v&quot;: &quot;f16&quot;, &quot;--ctx-size&quot;: &quot;8192&quot;, &quot;--reasoning&quot;: &quot;off&quot;, &quot;--spec-draft-n-max&quot;: &quot;3&quot;, &quot;--spec-type&quot;: &quot;draft-mtp&quot;, &quot;--threads&quot;: &quot;6&quot;, &quot;--ubatch-size&quot;: &quot;512&quot;} |
| Actual tuning / weight artifact / engine kernel | {&quot;artifact_state&quot;: &quot;MTP_BEARING_OR_GRAFTED_GGUF&quot;, &quot;declared_profile&quot;: null, &quot;draft_artifact&quot;: null, &quot;draft_model_sha256&quot;: null, &quot;engine_build_id&quot;: &quot;bbae889168127411ddd91d4576791ef20917e7a534d974d134347a33ea626499&quot;, &quot;engine_source_commit&quot;: null, &quot;environment_knobs&quot;: {&quot;GGML_CUDA_GRAPH_OPT&quot;: &quot;0&quot;, &quot;GGML_CUDA_O2_WEIGHT_CACHE_MIB&quot;: &quot;6144&quot;}, &quot;executed_model_sha256&quot;: &quot;78af5105675a93f2909d625288a87be86ceef620985ab255f72dc028e0290e82&quot;, &quot;interpretation&quot;: &quot;No-MTP inference does not imply a non-grafted weight file. GRAPH_OPT=0 does not imply CUDA Graphs disabled. An absent setting is unrecorded, never assumed off.&quot;, &quot;kernel_library&quot;: &quot;libggml-cuda.so.0.26.0&quot;, &quot;kernel_library_sha256&quot;: &quot;b1596b98ba033d8a400d5ecaba5630168c5c5626b493ed2230ecb239c84a62ad&quot;, &quot;runtime_flags&quot;: {&quot;--batch-size&quot;: &quot;2048&quot;, &quot;--cache-reuse&quot;: &quot;0&quot;, &quot;--cache-type-k&quot;: &quot;f16&quot;, &quot;--cache-type-v&quot;: &quot;f16&quot;, &quot;--ctx-checkpoints&quot;: &quot;2&quot;, &quot;--ctx-size&quot;: &quot;8192&quot;, &quot;--flash-attn&quot;: &quot;on&quot;, &quot;--n-gpu-layers&quot;: &quot;99&quot;, &quot;--parallel&quot;: &quot;1&quot;, &quot;--reasoning&quot;: &quot;off&quot;, &quot;--spec-draft-n-max&quot;: &quot;3&quot;, &quot;--spec-draft-n-min&quot;: &quot;1&quot;, &quot;--spec-type&quot;: &quot;draft-mtp&quot;, &quot;--threads&quot;: &quot;6&quot;, &quot;--ubatch-size&quot;: &quot;512&quot;}, &quot;weight_artifact&quot;: &quot;OmniCoder-2-9B.Q6_K-MTP-grafted.gguf&quot;} |
| Tuning provenance | Pinned executed launch; executed launch SHA=31e37154cfd129fd6a3033c62fdff0c266f4522c1939b4ce2f7c91c6a337476a |
| Sampling / output cap | {&quot;seed&quot;: 1001, &quot;temperature&quot;: 0} / 1024 |
| Cache / timing scope | Warm model; per-request KV reset; OS file cache uncontrolled; model startup excluded |
| Measurement batches | Single suite or repeated cycles as stated |
| Actual template controls | See pinned native request evidence |
| Actual input-token range (if exported) | Not included in this public aggregate |
| Task count / repeats | 164 unique; one observed answer per task; no repeated-run uncertainty measured |
| Model SHA-256 | 78af5105675a93f2909d625288a87be86ceef620985ab255f72dc028e0290e82 |
| Engine binary SHA-256 | 08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54 |
| Template SHA-256 | a4aee8afcf2e0711942cf848899be66016f8d14a889ff9ede07bca099c28f715 |
| Scorer adapter SHA-256 | dea3b58b17e93734bf27e15e3f07419982b28f622427519a0779c5c8106cf3ad |
| EvalPlus provenance SHA-256 | 332b4dfcdd92cb653859dd392c9e2430726aa85cc6560dcfc76282d06310e64d |
| Plan SHA-256 | a9dbcbb0fe047611864d33b97e5f8dd8c21651c35075bb353a418dc477b2d15c |

Original audit SHA-256 (originals retained privately; public excerpts are not the original files):

- [audit-1f940596d115e34ae02f](audits/audit-1f940596d115e34ae02f.md): `1f940596d115e34ae02fb770a10219149578150e431be646376f8fb223d15c0e`

### Ornith 1.5 9B · Q6_K · R254

Fast non-reasoning. No additional policy claim is inferred from this discipline.

| Condition | Audited value |
|---|---|
| Separate process-VRAM observation (not device peak) | NOT MEASURED |
| Hardware / power | Tesla V100-SXM2 16 GB HBM2 / 300 W |
| Engine | llama.cpp / CUDA 12.8 / SM70 (exact audited binary below) |
| Date | 2026-10-20 |
| Context, batching, KV, speculation | {&quot;--batch-size&quot;: &quot;2048&quot;, &quot;--cache-type-k&quot;: &quot;f16&quot;, &quot;--cache-type-v&quot;: &quot;f16&quot;, &quot;--ctx-size&quot;: &quot;8192&quot;, &quot;--reasoning&quot;: &quot;off&quot;, &quot;--spec-type&quot;: &quot;none&quot;, &quot;--threads&quot;: &quot;6&quot;, &quot;--ubatch-size&quot;: &quot;512&quot;} |
| Actual tuning / weight artifact / engine kernel | {&quot;artifact_state&quot;: &quot;SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED&quot;, &quot;declared_profile&quot;: null, &quot;draft_artifact&quot;: null, &quot;draft_model_sha256&quot;: null, &quot;engine_build_id&quot;: &quot;dded13c80bc8e7d01a43ac6745d06bb22d7a15a3f5fba68729c536286e5066d4&quot;, &quot;engine_source_commit&quot;: null, &quot;environment_knobs&quot;: {&quot;GGML_CUDA_GRAPH_OPT&quot;: &quot;0&quot;}, &quot;executed_model_sha256&quot;: &quot;b6f76e74f86245b3caee014b797c10dca931c4dfdaabfb134eab655f81e4154a&quot;, &quot;interpretation&quot;: &quot;No-MTP inference does not imply a non-grafted weight file. GRAPH_OPT=0 does not imply CUDA Graphs disabled. An absent setting is unrecorded, never assumed off.&quot;, &quot;kernel_library&quot;: &quot;libggml-cuda.so.0.26.0&quot;, &quot;kernel_library_sha256&quot;: &quot;f76ecefe4dff5bb7bacf5721159b607f008d7f23b0fc848134637b6673b0e1f5&quot;, &quot;runtime_flags&quot;: {&quot;--batch-size&quot;: &quot;2048&quot;, &quot;--cache-reuse&quot;: &quot;0&quot;, &quot;--cache-type-k&quot;: &quot;f16&quot;, &quot;--cache-type-v&quot;: &quot;f16&quot;, &quot;--ctx-checkpoints&quot;: &quot;2&quot;, &quot;--ctx-size&quot;: &quot;8192&quot;, &quot;--flash-attn&quot;: &quot;on&quot;, &quot;--n-gpu-layers&quot;: &quot;99&quot;, &quot;--parallel&quot;: &quot;1&quot;, &quot;--reasoning&quot;: &quot;off&quot;, &quot;--spec-type&quot;: &quot;none&quot;, &quot;--threads&quot;: &quot;6&quot;, &quot;--ubatch-size&quot;: &quot;512&quot;}, &quot;weight_artifact&quot;: &quot;Ornith-1.5-9B-Q6_K.gguf&quot;} |
| Tuning provenance | Pinned executed launch; executed launch SHA=ea7b735c8b49e4f7f5da3613c632c6987ff50bcce8799dd33a0d175ee0102b0e |
| Sampling / output cap | {&quot;seed&quot;: 1001, &quot;temperature&quot;: 0} / 1024 |
| Cache / timing scope | Warm model; per-request KV reset; OS file cache uncontrolled; model startup excluded |
| Measurement batches | Single suite or repeated cycles as stated |
| Actual template controls | See pinned native request evidence |
| Actual input-token range (if exported) | Not included in this public aggregate |
| Task count / repeats | 164 unique; one observed answer per task; no repeated-run uncertainty measured |
| Model SHA-256 | b6f76e74f86245b3caee014b797c10dca931c4dfdaabfb134eab655f81e4154a |
| Engine binary SHA-256 | 08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54 |
| Template SHA-256 | 9dd2fbd270feaa1fbef2d4f634d7887c9c506e3bde140f8e7351c8944e8fd235 |
| Scorer adapter SHA-256 | dea3b58b17e93734bf27e15e3f07419982b28f622427519a0779c5c8106cf3ad |
| EvalPlus provenance SHA-256 | 332b4dfcdd92cb653859dd392c9e2430726aa85cc6560dcfc76282d06310e64d |
| Plan SHA-256 | b46e4897903b1a45684bdc73d94f7ba1bf30603a8c1bd0bd9c8561b6ca1ea668 |

Original audit SHA-256 (originals retained privately; public excerpts are not the original files):

- [audit-a898f240d6d584ddfcaa](audits/audit-a898f240d6d584ddfcaa.md): `a898f240d6d584ddfcaaa6fdcf3b3d1a75c250ee73960005a4fe362f2551abb9`

### Qwen3.5 9B · Q4_K_M · R255

Fast non-reasoning. No additional policy claim is inferred from this discipline.

| Condition | Audited value |
|---|---|
| Separate process-VRAM observation (not device peak) | NOT MEASURED |
| Hardware / power | Tesla V100-SXM2 16 GB HBM2 / 300 W |
| Engine | llama.cpp / CUDA 12.8 / SM70 (exact audited binary below) |
| Date | 2026-10-20 |
| Context, batching, KV, speculation | {&quot;--batch-size&quot;: &quot;2048&quot;, &quot;--cache-type-k&quot;: &quot;f16&quot;, &quot;--cache-type-v&quot;: &quot;f16&quot;, &quot;--ctx-size&quot;: &quot;8192&quot;, &quot;--reasoning&quot;: &quot;off&quot;, &quot;--threads&quot;: &quot;6&quot;, &quot;--ubatch-size&quot;: &quot;512&quot;} |
| Actual tuning / weight artifact / engine kernel | {&quot;artifact_state&quot;: &quot;SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED&quot;, &quot;declared_profile&quot;: &quot;fast_nonreasoning_greedy&quot;, &quot;draft_artifact&quot;: null, &quot;draft_model_sha256&quot;: null, &quot;engine_build_id&quot;: &quot;dded13c80bc8e7d01a43ac6745d06bb22d7a15a3f5fba68729c536286e5066d4&quot;, &quot;engine_source_commit&quot;: null, &quot;environment_knobs&quot;: {&quot;GGML_CUDA_GRAPH_OPT&quot;: &quot;0&quot;}, &quot;executed_model_sha256&quot;: &quot;02d45dc1cf451ba2475ac33b301c2dd8f985abe4c182ce04a1f2f5bf0260278d&quot;, &quot;interpretation&quot;: &quot;No-MTP inference does not imply a non-grafted weight file. GRAPH_OPT=0 does not imply CUDA Graphs disabled. An absent setting is unrecorded, never assumed off.&quot;, &quot;kernel_library&quot;: &quot;libggml-cuda.so.0.26.0&quot;, &quot;kernel_library_sha256&quot;: &quot;f76ecefe4dff5bb7bacf5721159b607f008d7f23b0fc848134637b6673b0e1f5&quot;, &quot;runtime_flags&quot;: {&quot;--batch-size&quot;: &quot;2048&quot;, &quot;--cache-reuse&quot;: &quot;0&quot;, &quot;--cache-type-k&quot;: &quot;f16&quot;, &quot;--cache-type-v&quot;: &quot;f16&quot;, &quot;--ctx-checkpoints&quot;: &quot;2&quot;, &quot;--ctx-size&quot;: &quot;8192&quot;, &quot;--flash-attn&quot;: &quot;on&quot;, &quot;--n-gpu-layers&quot;: &quot;99&quot;, &quot;--parallel&quot;: &quot;1&quot;, &quot;--reasoning&quot;: &quot;off&quot;, &quot;--threads&quot;: &quot;6&quot;, &quot;--ubatch-size&quot;: &quot;512&quot;}, &quot;weight_artifact&quot;: &quot;qwen3.5-9b.gguf&quot;} |
| Tuning provenance | Pinned executed launch; executed launch SHA=3f9f03d82b8ea223618b23239e0fda91a1d00bb4a17adb337b033347840929b4 |
| Sampling / output cap | {&quot;seed&quot;: 1001, &quot;temperature&quot;: 0} / 1024 |
| Cache / timing scope | Warm model; per-request KV reset; OS file cache uncontrolled; model startup excluded |
| Measurement batches | Single suite or repeated cycles as stated |
| Actual template controls | See pinned native request evidence |
| Actual input-token range (if exported) | Not included in this public aggregate |
| Task count / repeats | 164 unique; one observed answer per task; no repeated-run uncertainty measured |
| Model SHA-256 | 02d45dc1cf451ba2475ac33b301c2dd8f985abe4c182ce04a1f2f5bf0260278d |
| Engine binary SHA-256 | 08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54 |
| Template SHA-256 | a4aee8afcf2e0711942cf848899be66016f8d14a889ff9ede07bca099c28f715 |
| Scorer adapter SHA-256 | dea3b58b17e93734bf27e15e3f07419982b28f622427519a0779c5c8106cf3ad |
| EvalPlus provenance SHA-256 | 332b4dfcdd92cb653859dd392c9e2430726aa85cc6560dcfc76282d06310e64d |
| Plan SHA-256 | 528c2a92df377e362e50fc0a7c90999be9091fff514d36589eb0482bdc553d27 |

Original audit SHA-256 (originals retained privately; public excerpts are not the original files):

- [audit-69ed2894e20c7705ff38](audits/audit-69ed2894e20c7705ff38.md): `69ed2894e20c7705ff385fc72bb70a5f0e9e353f42744449fadd8407f0c73fdb`

### Gemma4 12B IT QAT · Q4_0 · R425

Fast non-reasoning. No additional policy claim is inferred from this discipline.

| Condition | Audited value |
|---|---|
| Separate process-VRAM observation (not device peak) | NOT MEASURED |
| Hardware / power | Tesla V100-SXM2 16 GB HBM2 / 300 W |
| Engine | llama.cpp / CUDA 12.8 / SM70 (exact audited binary below) |
| Date | 2026-10-22 |
| Context, batching, KV, speculation | {&quot;--batch-size&quot;: &quot;2048&quot;, &quot;--cache-type-k&quot;: &quot;f16&quot;, &quot;--cache-type-v&quot;: &quot;f16&quot;, &quot;--ctx-size&quot;: &quot;8192&quot;, &quot;--reasoning&quot;: &quot;off&quot;, &quot;--spec-type&quot;: &quot;none&quot;, &quot;--threads&quot;: &quot;6&quot;, &quot;--ubatch-size&quot;: &quot;512&quot;} |
| Actual tuning / weight artifact / engine kernel | {&quot;artifact_state&quot;: &quot;SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED&quot;, &quot;declared_profile&quot;: &quot;official_QAT_fast_T1_P095_K64_coding1024&quot;, &quot;draft_artifact&quot;: null, &quot;draft_model_sha256&quot;: null, &quot;engine_build_id&quot;: &quot;dded13c80bc8e7d01a43ac6745d06bb22d7a15a3f5fba68729c536286e5066d4&quot;, &quot;engine_source_commit&quot;: null, &quot;environment_knobs&quot;: {&quot;GGML_CUDA_GRAPH_OPT&quot;: &quot;0&quot;, &quot;GGML_CUDA_O2_WEIGHT_CACHE_MIB&quot;: &quot;0&quot;}, &quot;executed_model_sha256&quot;: &quot;93567e57a8fe10b23569b9d9ec38cd005deedf71e29477c421a4b83f418a538b&quot;, &quot;interpretation&quot;: &quot;No-MTP inference does not imply a non-grafted weight file. GRAPH_OPT=0 does not imply CUDA Graphs disabled. An absent setting is unrecorded, never assumed off.&quot;, &quot;kernel_library&quot;: &quot;libggml-cuda.so.0.26.0&quot;, &quot;kernel_library_sha256&quot;: &quot;f76ecefe4dff5bb7bacf5721159b607f008d7f23b0fc848134637b6673b0e1f5&quot;, &quot;runtime_flags&quot;: {&quot;--batch-size&quot;: &quot;2048&quot;, &quot;--cache-reuse&quot;: &quot;0&quot;, &quot;--cache-type-k&quot;: &quot;f16&quot;, &quot;--cache-type-v&quot;: &quot;f16&quot;, &quot;--ctx-checkpoints&quot;: &quot;2&quot;, &quot;--ctx-size&quot;: &quot;8192&quot;, &quot;--flash-attn&quot;: &quot;auto&quot;, &quot;--n-gpu-layers&quot;: &quot;99&quot;, &quot;--parallel&quot;: &quot;1&quot;, &quot;--reasoning&quot;: &quot;off&quot;, &quot;--spec-type&quot;: &quot;none&quot;, &quot;--threads&quot;: &quot;6&quot;, &quot;--ubatch-size&quot;: &quot;512&quot;}, &quot;weight_artifact&quot;: &quot;gemma-4-12b-it-qat-q4_0.gguf&quot;} |
| Tuning provenance | Pinned executed launch; executed launch SHA=5073fa0549efa164f9e9a585fc7c3170e985d99bddcdd4587e57f9cadc6dc054 |
| Sampling / output cap | {&quot;min_p&quot;: 0.0, &quot;presence_penalty&quot;: 0.0, &quot;repeat_penalty&quot;: 1.0, &quot;seed&quot;: 1001, &quot;temperature&quot;: 1.0, &quot;top_k&quot;: 64, &quot;top_p&quot;: 0.95} / 1024 |
| Cache / timing scope | Warm model; per-request KV reset; OS file cache uncontrolled; model startup excluded |
| Measurement batches | Single suite or repeated cycles as stated |
| Actual template controls | See pinned native request evidence |
| Actual input-token range (if exported) | Not included in this public aggregate |
| Task count / repeats | 164 unique; one observed answer per task; no repeated-run uncertainty measured |
| Model SHA-256 | 93567e57a8fe10b23569b9d9ec38cd005deedf71e29477c421a4b83f418a538b |
| Engine binary SHA-256 | 08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54 |
| Template SHA-256 | ae53464bf3be25802b3a5b37def7fd89667067d7577049b3b2d74c4d8de4c6d4 |
| Scorer adapter SHA-256 | dea3b58b17e93734bf27e15e3f07419982b28f622427519a0779c5c8106cf3ad |
| EvalPlus provenance SHA-256 | 332b4dfcdd92cb653859dd392c9e2430726aa85cc6560dcfc76282d06310e64d |
| Plan SHA-256 | 5e3286490116ec60196fc87fa052ce1b05a6d8f16b9fffbcd09b429e4c126d3d |

Original audit SHA-256 (originals retained privately; public excerpts are not the original files):

- [audit-23d38cbb14bfd9a5f424](audits/audit-23d38cbb14bfd9a5f424.md): `23d38cbb14bfd9a5f424fa93c3220c2481e59e4d49706aa8ee6f35b34000dafe`

### Qwen3.8 27B · GSQ/RCO IQ3_S · R117

Fast; no MTP. No additional policy claim is inferred from this discipline.

| Condition | Audited value |
|---|---|
| Separate process-VRAM observation (not device peak) | 12212 |
| Hardware / power | Tesla V100-SXM2 16 GB HBM2 / 300 W |
| Engine | llama.cpp / CUDA 12.8 / SM70 (exact audited binary below) |
| Date | NOT RECORDED |
| Context, batching, KV, speculation | {&quot;--batch-size&quot;: &quot;2048&quot;, &quot;--cache-type-k&quot;: &quot;f16&quot;, &quot;--cache-type-v&quot;: &quot;f16&quot;, &quot;--ctx-size&quot;: &quot;8192&quot;, &quot;--reasoning&quot;: &quot;off&quot;, &quot;--spec-type&quot;: &quot;none&quot;, &quot;--threads&quot;: &quot;6&quot;, &quot;--ubatch-size&quot;: &quot;512&quot;} |
| Actual tuning / weight artifact / engine kernel | {&quot;artifact_state&quot;: &quot;MTP_BEARING_OR_GRAFTED_GGUF&quot;, &quot;declared_profile&quot;: null, &quot;draft_artifact&quot;: null, &quot;draft_model_sha256&quot;: null, &quot;engine_build_id&quot;: &quot;dded13c80bc8e7d01a43ac6745d06bb22d7a15a3f5fba68729c536286e5066d4&quot;, &quot;engine_source_commit&quot;: null, &quot;environment_knobs&quot;: {&quot;GGML_CUDA_GRAPH_OPT&quot;: &quot;0&quot;}, &quot;executed_model_sha256&quot;: &quot;58fd826723939933dc86f45b7fe04545cbc2de1c70f6fe2cdd3858c87a98c12f&quot;, &quot;interpretation&quot;: &quot;No-MTP inference does not imply a non-grafted weight file. GRAPH_OPT=0 does not imply CUDA Graphs disabled. An absent setting is unrecorded, never assumed off.&quot;, &quot;kernel_library&quot;: &quot;libggml-cuda.so.0.26.0&quot;, &quot;kernel_library_sha256&quot;: &quot;f76ecefe4dff5bb7bacf5721159b607f008d7f23b0fc848134637b6673b0e1f5&quot;, &quot;runtime_flags&quot;: {&quot;--batch-size&quot;: &quot;2048&quot;, &quot;--cache-type-k&quot;: &quot;f16&quot;, &quot;--cache-type-v&quot;: &quot;f16&quot;, &quot;--ctx-checkpoints&quot;: &quot;2&quot;, &quot;--ctx-size&quot;: &quot;8192&quot;, &quot;--flash-attn&quot;: &quot;auto&quot;, &quot;--n-gpu-layers&quot;: &quot;99&quot;, &quot;--parallel&quot;: &quot;1&quot;, &quot;--reasoning&quot;: &quot;off&quot;, &quot;--spec-type&quot;: &quot;none&quot;, &quot;--threads&quot;: &quot;6&quot;, &quot;--ubatch-size&quot;: &quot;512&quot;}, &quot;weight_artifact&quot;: &quot;Qwen3.8-27B-GSQ-RCO-IQ3_S-mtp.gguf&quot;} |
| Tuning provenance | Pinned executed launch; executed launch SHA=c875d7d315510b68c0b91f272bf2725ada8e637a80786bab18f8f2632c45a3e6 |
| Sampling / output cap | {&quot;seed&quot;: 1001, &quot;temperature&quot;: 0} / 1024 |
| Cache / timing scope | Warm model; per-request KV reset; OS file cache uncontrolled; model startup excluded |
| Measurement batches | Single suite or repeated cycles as stated |
| Actual template controls | See pinned native request evidence |
| Actual input-token range (if exported) | Not included in this public aggregate |
| Task count / repeats | 164 unique; one observed answer per task; no repeated-run uncertainty measured |
| Model SHA-256 | 58fd826723939933dc86f45b7fe04545cbc2de1c70f6fe2cdd3858c87a98c12f |
| Engine binary SHA-256 | 08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54 |
| Template SHA-256 | c3cf9e34abf4f9e36c2d72165aa9c132d3e2a725b6c2586aaa3a8af9d7a81041 |
| Scorer adapter SHA-256 | ecb62cb09cc50680b985831c6799392bdbfebbf24c8820a876ecab31cfb65296 |
| EvalPlus provenance SHA-256 | 332b4dfcdd92cb653859dd392c9e2430726aa85cc6560dcfc76282d06310e64d |
| Plan SHA-256 | de4acb1d78b6a6ec052b975456574afc8d560af31dfcbce71044e5f31e4aed06 |

Original audit SHA-256 (originals retained privately; public excerpts are not the original files):

- [audit-0a001d95dc6b53c43508](audits/audit-0a001d95dc6b53c43508.md): `0a001d95dc6b53c43508ef53594a7cde7256e64c5089d38aa2def3b9d19f7087`

### Qwen3.8 27B · GSQ/RCO IQ3_S · R118

Fast; MTP3. MTP target-token identity is not lossless; no allround qualification

| Condition | Audited value |
|---|---|
| Separate process-VRAM observation (not device peak) | 13358 |
| Hardware / power | Tesla V100-SXM2 16 GB HBM2 / 300 W |
| Engine | llama.cpp / CUDA 12.8 / SM70 (exact audited binary below) |
| Date | NOT RECORDED |
| Context, batching, KV, speculation | {&quot;--batch-size&quot;: &quot;2048&quot;, &quot;--cache-type-k&quot;: &quot;f16&quot;, &quot;--cache-type-v&quot;: &quot;f16&quot;, &quot;--ctx-size&quot;: &quot;8192&quot;, &quot;--reasoning&quot;: &quot;off&quot;, &quot;--spec-draft-n-max&quot;: &quot;3&quot;, &quot;--spec-type&quot;: &quot;draft-mtp&quot;, &quot;--threads&quot;: &quot;6&quot;, &quot;--ubatch-size&quot;: &quot;512&quot;} |
| Actual tuning / weight artifact / engine kernel | {&quot;artifact_state&quot;: &quot;MTP_BEARING_OR_GRAFTED_GGUF&quot;, &quot;declared_profile&quot;: null, &quot;draft_artifact&quot;: null, &quot;draft_model_sha256&quot;: null, &quot;engine_build_id&quot;: &quot;dded13c80bc8e7d01a43ac6745d06bb22d7a15a3f5fba68729c536286e5066d4&quot;, &quot;engine_source_commit&quot;: null, &quot;environment_knobs&quot;: {&quot;GGML_CUDA_GRAPH_OPT&quot;: &quot;0&quot;}, &quot;executed_model_sha256&quot;: &quot;58fd826723939933dc86f45b7fe04545cbc2de1c70f6fe2cdd3858c87a98c12f&quot;, &quot;interpretation&quot;: &quot;No-MTP inference does not imply a non-grafted weight file. GRAPH_OPT=0 does not imply CUDA Graphs disabled. An absent setting is unrecorded, never assumed off.&quot;, &quot;kernel_library&quot;: &quot;libggml-cuda.so.0.26.0&quot;, &quot;kernel_library_sha256&quot;: &quot;f76ecefe4dff5bb7bacf5721159b607f008d7f23b0fc848134637b6673b0e1f5&quot;, &quot;runtime_flags&quot;: {&quot;--batch-size&quot;: &quot;2048&quot;, &quot;--cache-type-k&quot;: &quot;f16&quot;, &quot;--cache-type-v&quot;: &quot;f16&quot;, &quot;--ctx-checkpoints&quot;: &quot;2&quot;, &quot;--ctx-size&quot;: &quot;8192&quot;, &quot;--flash-attn&quot;: &quot;auto&quot;, &quot;--n-gpu-layers&quot;: &quot;99&quot;, &quot;--parallel&quot;: &quot;1&quot;, &quot;--reasoning&quot;: &quot;off&quot;, &quot;--spec-draft-n-max&quot;: &quot;3&quot;, &quot;--spec-draft-n-min&quot;: &quot;1&quot;, &quot;--spec-type&quot;: &quot;draft-mtp&quot;, &quot;--threads&quot;: &quot;6&quot;, &quot;--ubatch-size&quot;: &quot;512&quot;}, &quot;weight_artifact&quot;: &quot;Qwen3.8-27B-GSQ-RCO-IQ3_S-mtp.gguf&quot;} |
| Tuning provenance | Pinned executed launch; executed launch SHA=bc7247345fd05a34fe8d5b5e677025d19c6cb7d08f8bbb772808708e7b28bc32 |
| Sampling / output cap | {&quot;seed&quot;: 1001, &quot;temperature&quot;: 0} / 1024 |
| Cache / timing scope | Warm model; per-request KV reset; OS file cache uncontrolled; model startup excluded |
| Measurement batches | Single suite or repeated cycles as stated |
| Actual template controls | See pinned native request evidence |
| Actual input-token range (if exported) | Not included in this public aggregate |
| Task count / repeats | 164 unique; one observed answer per task; no repeated-run uncertainty measured |
| Model SHA-256 | 58fd826723939933dc86f45b7fe04545cbc2de1c70f6fe2cdd3858c87a98c12f |
| Engine binary SHA-256 | 08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54 |
| Template SHA-256 | c3cf9e34abf4f9e36c2d72165aa9c132d3e2a725b6c2586aaa3a8af9d7a81041 |
| Scorer adapter SHA-256 | ecb62cb09cc50680b985831c6799392bdbfebbf24c8820a876ecab31cfb65296 |
| EvalPlus provenance SHA-256 | 332b4dfcdd92cb653859dd392c9e2430726aa85cc6560dcfc76282d06310e64d |
| Plan SHA-256 | 7f3ab2f95edf05d58dec91ed60dab2ea85feb8c6c57ecb4c68cda36d6b661c54 |

Original audit SHA-256 (originals retained privately; public excerpts are not the original files):

- [audit-ab44bd9905753dd56faf](audits/audit-ab44bd9905753dd56faf.md): `ab44bd9905753dd56faf682336ba75ef247818df7d6ba3774c7ac50fdfc4feef`

### Ternary Bonsai 2 27B · PQ2_0 · R279

Thinking medium; 4096 output. No additional policy claim is inferred from this discipline.

| Condition | Audited value |
|---|---|
| Separate process-VRAM observation (not device peak) | NOT MEASURED |
| Hardware / power | Tesla V100-SXM2 16 GB HBM2 / 300 W |
| Engine | llama.cpp / CUDA 12.8 / SM70 (exact audited binary below) |
| Date | 2026-10-21 |
| Context, batching, KV, speculation | {&quot;--batch-size&quot;: &quot;2048&quot;, &quot;--cache-type-k&quot;: &quot;f16&quot;, &quot;--cache-type-v&quot;: &quot;f16&quot;, &quot;--ctx-size&quot;: &quot;8192&quot;, &quot;--reasoning&quot;: &quot;on&quot;, &quot;--spec-type&quot;: &quot;none&quot;, &quot;--threads&quot;: &quot;6&quot;, &quot;--ubatch-size&quot;: &quot;512&quot;} |
| Actual tuning / weight artifact / engine kernel | {&quot;artifact_state&quot;: &quot;SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED&quot;, &quot;declared_profile&quot;: &quot;published_medium_thinking_4096&quot;, &quot;draft_artifact&quot;: null, &quot;draft_model_sha256&quot;: null, &quot;engine_build_id&quot;: &quot;bonsai-pq2-sm70-9a9394a895b9&quot;, &quot;engine_source_commit&quot;: null, &quot;environment_knobs&quot;: {&quot;GGML_CUDA_GRAPH_OPT&quot;: &quot;0&quot;, &quot;GGML_CUDA_O2_WEIGHT_CACHE_MIB&quot;: &quot;0&quot;}, &quot;executed_model_sha256&quot;: &quot;3907dc1658db1f78a9826bf8d5bcb8dc65db0d466388937af57f2294fae62ec1&quot;, &quot;interpretation&quot;: &quot;No-MTP inference does not imply a non-grafted weight file. GRAPH_OPT=0 does not imply CUDA Graphs disabled. An absent setting is unrecorded, never assumed off.&quot;, &quot;kernel_library&quot;: &quot;libggml-cuda.so.0.21.0&quot;, &quot;kernel_library_sha256&quot;: &quot;60c874aa652e9eb7d09ae128b79d31cbe0042f5e76476fd1d3192c47e7291d12&quot;, &quot;runtime_flags&quot;: {&quot;--batch-size&quot;: &quot;2048&quot;, &quot;--cache-reuse&quot;: &quot;0&quot;, &quot;--cache-type-k&quot;: &quot;f16&quot;, &quot;--cache-type-v&quot;: &quot;f16&quot;, &quot;--ctx-checkpoints&quot;: &quot;2&quot;, &quot;--ctx-size&quot;: &quot;8192&quot;, &quot;--flash-attn&quot;: &quot;on&quot;, &quot;--n-gpu-layers&quot;: &quot;99&quot;, &quot;--parallel&quot;: &quot;1&quot;, &quot;--reasoning&quot;: &quot;on&quot;, &quot;--spec-type&quot;: &quot;none&quot;, &quot;--threads&quot;: &quot;6&quot;, &quot;--ubatch-size&quot;: &quot;512&quot;}, &quot;weight_artifact&quot;: &quot;Ternary-Bonsai-2-27B-PQ2_0.gguf&quot;} |
| Tuning provenance | Frozen plan; executed launch SHA=NOT RECORDED |
| Sampling / output cap | {&quot;min_p&quot;: 0.05, &quot;presence_penalty&quot;: 0.0, &quot;repeat_penalty&quot;: 1.0, &quot;seed&quot;: 1001, &quot;temperature&quot;: 1.0, &quot;top_k&quot;: 20, &quot;top_p&quot;: 0.95} / 4096 |
| Cache / timing scope | Warm model; per-request KV reset; OS file cache uncontrolled; model startup excluded |
| Measurement batches | Single suite or repeated cycles as stated |
| Actual template controls | See pinned native request evidence |
| Actual input-token range (if exported) | Not included in this public aggregate |
| Task count / repeats | 164 unique; one observed answer per task; no repeated-run uncertainty measured |
| Model SHA-256 | 3907dc1658db1f78a9826bf8d5bcb8dc65db0d466388937af57f2294fae62ec1 |
| Engine binary SHA-256 | 94c60d4646249fe067c75a56b15e6a8a9070a5e422cae16ee8dd9973389a6a27 |
| Template SHA-256 | See exact plan audit; not duplicated in public subset |
| Scorer adapter SHA-256 | dea3b58b17e93734bf27e15e3f07419982b28f622427519a0779c5c8106cf3ad |
| EvalPlus provenance SHA-256 | 332b4dfcdd92cb653859dd392c9e2430726aa85cc6560dcfc76282d06310e64d |
| Plan SHA-256 | 84db86fe519aaf41421f1e920ccda55c7b2103f63cde297ee7910938398da0d5 |

Original audit SHA-256 (originals retained privately; public excerpts are not the original files):

- [audit-3cc9e94338b5c4d2b889](audits/audit-3cc9e94338b5c4d2b889.md): `3cc9e94338b5c4d2b889a5fd21d88cfc308a0d287fcab2e9981a24393725e0e9`
- [audit-e6219eada24128727880](audits/audit-e6219eada24128727880.md): `e6219eada24128727880ea8a7c2af81904eada756424d0c6141d546425791e71`
- [audit-948e1d010537c3c580cf](audits/audit-948e1d010537c3c580cf.md): `948e1d010537c3c580cf7020ee5abe80cce8bae0b09412275654d7d405aa39f5`
- [audit-74b93fada14b5c6b65e7](audits/audit-74b93fada14b5c6b65e7.md): `74b93fada14b5c6b65e7978ed61dadea14c4b179ced003df9e9eab626b42c1b6`
- [audit-32897bfde6c4ab6f8dd7](audits/audit-32897bfde6c4ab6f8dd7.md): `32897bfde6c4ab6f8dd73ac3d27a0b548cc8ff4807b59b10e046b87170a1b769`
- [audit-e4d67e27df9647a6df70](audits/audit-e4d67e27df9647a6df70.md): `e4d67e27df9647a6df704b60d8e96076a62a0ea327550e70521a681524931a81`
- [audit-cabcd14d12eea705c5e9](audits/audit-cabcd14d12eea705c5e9.md): `cabcd14d12eea705c5e935a0213aa17768f67e546da2ac1691becc784da8864f`
- [audit-a0b196e900db38e0a0cd](audits/audit-a0b196e900db38e0a0cd.md): `a0b196e900db38e0a0cd73ed2b69fd7e615121450ef9f246509e88c92ea78e53`

## Coding · MBPP+ admitted 223

MBPP+ v0.2.0 original-test release pool: 223/224 tasks admitted before new model outputs; Mbpp/255 official canonical solution exceeds sandbox memory and is separately DEFERRED. Original32 + disjoint191, one answer per task, base AND plus. Not full224 or full378 leaderboard; separate from HumanEval and no proof of training exclusion.

Task identity: `86471d0ad0e68285d87a8c1b1d70bd35f12f3d55d23eb72fef7eca5a663b6c45`. **Task-matched whole-configuration comparisons**; native sampling, budgets and builds are shown below. These are development results, with no repeated-seed model-superiority claim. Record dates come from the original audit or frozen plan; missing dates remain labelled.

![Coding · MBPP+ admitted 223: Successful tasks; missing results labelled NOT MEASURED](assets/benchmarks/mbpp-success.svg){ .benchmark-svg }

![Coding · MBPP+ admitted 223: Mean task E2E; missing results labelled NOT MEASURED](assets/benchmarks/mbpp-latency.svg){ .benchmark-svg }

![Coding · MBPP+ admitted 223: GPU energy per success; missing results labelled NOT MEASURED](assets/benchmarks/mbpp-energy.svg){ .benchmark-svg }

![Coding · MBPP+ admitted 223: Peak device VRAM; missing results labelled NOT MEASURED](assets/benchmarks/mbpp-vram.svg){ .benchmark-svg }

| Profile / record date | Success | Successful tasks/s | Total task time / GPU energy | Peak VRAM | Audit |
|---|---|---|---|---|---|
| OmniCoder2 9B Q6_K — Original Q6; no MTP or weight cache / 2026-10-22 | 162/223 | 0.33264 | 487.010 s / 137779.71 J | 7364.5 | [R415](experiments/R415.md) |
| Qwen3.8 27B GSQ/RCO IQ3_S — IQ3_S grafted MTP3; coding profile / 2026-10-22 | 172/223 | 0.36041 | 477.232 s / 127647.53 J | 13616.5 | [R416](experiments/R416.md) |
| Gemma4 12B IT QAT Q4_0 — Official QAT Q4_0; native fast; no MTP or weight cache / 2026-10-22 | 168/223 | 0.19142 | 877.635 s / 216064.31 J | 8118.5 | [R428](experiments/R428.md) |

### OmniCoder2 9B · Q6_K · R415

Original Q6; no MTP or weight cache. No additional policy claim is inferred from this discipline.

| Condition | Audited value |
|---|---|
| Separate process-VRAM observation (not device peak) | NOT MEASURED |
| Hardware / power | Tesla V100-SXM2 16 GB HBM2 / 300 W |
| Engine | llama.cpp / CUDA 12.8 / SM70 (exact audited binary below) |
| Date | 2026-10-22 |
| Context, batching, KV, speculation | {&quot;--batch-size&quot;: &quot;2048&quot;, &quot;--cache-type-k&quot;: &quot;f16&quot;, &quot;--cache-type-v&quot;: &quot;f16&quot;, &quot;--ctx-size&quot;: &quot;8192&quot;, &quot;--reasoning&quot;: &quot;off&quot;, &quot;--spec-type&quot;: &quot;none&quot;, &quot;--threads&quot;: &quot;6&quot;, &quot;--ubatch-size&quot;: &quot;512&quot;} |
| Actual tuning / weight artifact / engine kernel | {&quot;artifact_state&quot;: &quot;SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED&quot;, &quot;declared_profile&quot;: &quot;original_Q6_noMTP_noWeightCache_greedy1024&quot;, &quot;draft_artifact&quot;: null, &quot;draft_model_sha256&quot;: null, &quot;engine_build_id&quot;: &quot;dded13c80bc8e7d01a43ac6745d06bb22d7a15a3f5fba68729c536286e5066d4&quot;, &quot;engine_source_commit&quot;: null, &quot;environment_knobs&quot;: {&quot;GGML_CUDA_GRAPH_OPT&quot;: &quot;0&quot;}, &quot;executed_model_sha256&quot;: &quot;b0c1664c86338be24090a45d8b86bd106ba755d004f8746d99ee5ad69258fc3b&quot;, &quot;interpretation&quot;: &quot;No-MTP inference does not imply a non-grafted weight file. GRAPH_OPT=0 does not imply CUDA Graphs disabled. An absent setting is unrecorded, never assumed off.&quot;, &quot;kernel_library&quot;: &quot;libggml-cuda.so.0.26.0&quot;, &quot;kernel_library_sha256&quot;: &quot;f76ecefe4dff5bb7bacf5721159b607f008d7f23b0fc848134637b6673b0e1f5&quot;, &quot;runtime_flags&quot;: {&quot;--batch-size&quot;: &quot;2048&quot;, &quot;--cache-reuse&quot;: &quot;0&quot;, &quot;--cache-type-k&quot;: &quot;f16&quot;, &quot;--cache-type-v&quot;: &quot;f16&quot;, &quot;--ctx-checkpoints&quot;: &quot;2&quot;, &quot;--ctx-size&quot;: &quot;8192&quot;, &quot;--flash-attn&quot;: &quot;on&quot;, &quot;--n-gpu-layers&quot;: &quot;99&quot;, &quot;--parallel&quot;: &quot;1&quot;, &quot;--reasoning&quot;: &quot;off&quot;, &quot;--spec-type&quot;: &quot;none&quot;, &quot;--threads&quot;: &quot;6&quot;, &quot;--ubatch-size&quot;: &quot;512&quot;}, &quot;weight_artifact&quot;: &quot;OmniCoder-2-9B.Q6_K.gguf&quot;} |
| Tuning provenance | Pinned executed launch; executed launch SHA=32d3c6db0c57eb1134b67107a6629631f8b1ac2d7c4d18fbd689225be5f316a8 |
| Sampling / output cap | {&quot;seed&quot;: 1001, &quot;temperature&quot;: 0.0} / 1024 |
| Cache / timing scope | Warm model; per-request KV reset; OS file cache uncontrolled; model startup excluded |
| Measurement batches | R411:32 + R415:191, disjoint tasks; no repeats |
| Actual template controls | {&quot;enable_thinking&quot;: false} |
| Actual input-token range (if exported) | Not included in this public aggregate |
| Task count / repeats | 223 unique; one observed answer per task; no repeated-run uncertainty measured |
| Model SHA-256 | b0c1664c86338be24090a45d8b86bd106ba755d004f8746d99ee5ad69258fc3b |
| Engine binary SHA-256 | 08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54 |
| Template SHA-256 | a4aee8afcf2e0711942cf848899be66016f8d14a889ff9ede07bca099c28f715 |
| Scorer adapter SHA-256 | 1b044c31ebf9fa65aff9540afb50ab5e756af65cf464afcc78770131a76728d7 |
| EvalPlus provenance SHA-256 | Not applicable / not duplicated |
| Plan SHA-256 | bb595974d3f8a74077f6a350a967ceb402990061100ef6dd50582af3cf0ef473 |

Original audit SHA-256 (originals retained privately; public excerpts are not the original files):

- [audit-e65387abe0a60505cf31](audits/audit-e65387abe0a60505cf31.md): `e65387abe0a60505cf31669aea4e05193eedd2c7f472eeff8312200123cae6c2`
- [audit-c3eda7245a81d8aea7e7](audits/audit-c3eda7245a81d8aea7e7.md): `c3eda7245a81d8aea7e7503a0109288e7ee02de2efccda32d9e545050d32393b`
- [audit-779c649d0c7aedb3a542](audits/audit-779c649d0c7aedb3a542.md): `779c649d0c7aedb3a54236109c23f8c25787ab480e2a63639400a12146f208ec`
- [audit-7fc79c331d1e88062f8a](audits/audit-7fc79c331d1e88062f8a.md): `7fc79c331d1e88062f8a749a024abca4577d945eae39de2ba8b6991f388d90c4`
- [audit-e65387abe0a60505cf31](audits/audit-e65387abe0a60505cf31.md): `e65387abe0a60505cf31669aea4e05193eedd2c7f472eeff8312200123cae6c2`

### Qwen3.8 27B · GSQ/RCO IQ3_S · R416

IQ3_S grafted MTP3; coding profile. Known native-tool/policy limitations remain; coding only, no allround or lossless claim.

| Condition | Audited value |
|---|---|
| Separate process-VRAM observation (not device peak) | NOT MEASURED |
| Hardware / power | Tesla V100-SXM2 16 GB HBM2 / 300 W |
| Engine | llama.cpp / CUDA 12.8 / SM70 (exact audited binary below) |
| Date | 2026-10-22 |
| Context, batching, KV, speculation | {&quot;--batch-size&quot;: &quot;2048&quot;, &quot;--cache-type-k&quot;: &quot;f16&quot;, &quot;--cache-type-v&quot;: &quot;f16&quot;, &quot;--ctx-size&quot;: &quot;8192&quot;, &quot;--reasoning&quot;: &quot;off&quot;, &quot;--spec-draft-n-max&quot;: &quot;3&quot;, &quot;--spec-type&quot;: &quot;draft-mtp&quot;, &quot;--threads&quot;: &quot;6&quot;, &quot;--ubatch-size&quot;: &quot;512&quot;} |
| Actual tuning / weight artifact / engine kernel | {&quot;artifact_state&quot;: &quot;MTP_BEARING_OR_GRAFTED_GGUF&quot;, &quot;declared_profile&quot;: &quot;GSQ_RCO_IQ3S_graftedMTP3_fast_greedy1024&quot;, &quot;draft_artifact&quot;: null, &quot;draft_model_sha256&quot;: null, &quot;engine_build_id&quot;: &quot;dded13c80bc8e7d01a43ac6745d06bb22d7a15a3f5fba68729c536286e5066d4&quot;, &quot;engine_source_commit&quot;: null, &quot;environment_knobs&quot;: {&quot;GGML_CUDA_GRAPH_OPT&quot;: &quot;0&quot;}, &quot;executed_model_sha256&quot;: &quot;58fd826723939933dc86f45b7fe04545cbc2de1c70f6fe2cdd3858c87a98c12f&quot;, &quot;interpretation&quot;: &quot;No-MTP inference does not imply a non-grafted weight file. GRAPH_OPT=0 does not imply CUDA Graphs disabled. An absent setting is unrecorded, never assumed off.&quot;, &quot;kernel_library&quot;: &quot;libggml-cuda.so.0.26.0&quot;, &quot;kernel_library_sha256&quot;: &quot;f76ecefe4dff5bb7bacf5721159b607f008d7f23b0fc848134637b6673b0e1f5&quot;, &quot;runtime_flags&quot;: {&quot;--batch-size&quot;: &quot;2048&quot;, &quot;--cache-reuse&quot;: &quot;0&quot;, &quot;--cache-type-k&quot;: &quot;f16&quot;, &quot;--cache-type-v&quot;: &quot;f16&quot;, &quot;--ctx-checkpoints&quot;: &quot;2&quot;, &quot;--ctx-size&quot;: &quot;8192&quot;, &quot;--flash-attn&quot;: &quot;on&quot;, &quot;--n-gpu-layers&quot;: &quot;99&quot;, &quot;--parallel&quot;: &quot;1&quot;, &quot;--reasoning&quot;: &quot;off&quot;, &quot;--spec-draft-n-max&quot;: &quot;3&quot;, &quot;--spec-draft-n-min&quot;: &quot;1&quot;, &quot;--spec-type&quot;: &quot;draft-mtp&quot;, &quot;--threads&quot;: &quot;6&quot;, &quot;--ubatch-size&quot;: &quot;512&quot;}, &quot;weight_artifact&quot;: &quot;Qwen3.8-27B-GSQ-RCO-IQ3_S-mtp.gguf&quot;} |
| Tuning provenance | Pinned executed launch; executed launch SHA=a0b5d2a8db73afcc2943de0558c31d3e8de639a5a1365795f646aed9ff682e06 |
| Sampling / output cap | {&quot;seed&quot;: 1001, &quot;temperature&quot;: 0.0} / 1024 |
| Cache / timing scope | Warm model; per-request KV reset; OS file cache uncontrolled; model startup excluded |
| Measurement batches | R413:32 + R416:191, disjoint tasks; no repeats |
| Actual template controls | {&quot;enable_thinking&quot;: false} |
| Actual input-token range (if exported) | Not included in this public aggregate |
| Task count / repeats | 223 unique; one observed answer per task; no repeated-run uncertainty measured |
| Model SHA-256 | 58fd826723939933dc86f45b7fe04545cbc2de1c70f6fe2cdd3858c87a98c12f |
| Engine binary SHA-256 | 08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54 |
| Template SHA-256 | c3cf9e34abf4f9e36c2d72165aa9c132d3e2a725b6c2586aaa3a8af9d7a81041 |
| Scorer adapter SHA-256 | 1b044c31ebf9fa65aff9540afb50ab5e756af65cf464afcc78770131a76728d7 |
| EvalPlus provenance SHA-256 | Not applicable / not duplicated |
| Plan SHA-256 | ad7af282e525daf3a4b2fc1cdb71a37021cf347d0bd0d22d8bcd90a4998ac003 |

Original audit SHA-256 (originals retained privately; public excerpts are not the original files):

- [audit-48622d74f74d1c3f7630](audits/audit-48622d74f74d1c3f7630.md): `48622d74f74d1c3f76300417b6a167b884bb86d11ba1255a135a6e448b0ac8f0`
- [audit-066a121f6734b7aaf3d8](audits/audit-066a121f6734b7aaf3d8.md): `066a121f6734b7aaf3d87b38f43ecddb7d6b51c6a5cda5982b323d6b93a57dce`
- [audit-84dc3818048e9e8fb943](audits/audit-84dc3818048e9e8fb943.md): `84dc3818048e9e8fb9435aa06e7f5000b3e8e60d8c1daeab49f3e934440d4a78`
- [audit-12a7d0b17bab09967917](audits/audit-12a7d0b17bab09967917.md): `12a7d0b17bab09967917bafee75b68d3b4baa81550f298602c406d56b4e7f05a`
- [audit-48622d74f74d1c3f7630](audits/audit-48622d74f74d1c3f7630.md): `48622d74f74d1c3f76300417b6a167b884bb86d11ba1255a135a6e448b0ac8f0`

### Gemma4 12B IT QAT · Q4_0 · R428

Official QAT Q4_0; native fast; no MTP or weight cache. Native-tool84/100 and agent9/18 with additional policy faults retained; coding results do not qualify an assistant.

| Condition | Audited value |
|---|---|
| Separate process-VRAM observation (not device peak) | NOT MEASURED |
| Hardware / power | Tesla V100-SXM2 16 GB HBM2 / 300 W |
| Engine | llama.cpp / CUDA 12.8 / SM70 (exact audited binary below) |
| Date | 2026-10-22 |
| Context, batching, KV, speculation | {&quot;--batch-size&quot;: &quot;2048&quot;, &quot;--cache-type-k&quot;: &quot;f16&quot;, &quot;--cache-type-v&quot;: &quot;f16&quot;, &quot;--ctx-size&quot;: &quot;8192&quot;, &quot;--reasoning&quot;: &quot;off&quot;, &quot;--spec-type&quot;: &quot;none&quot;, &quot;--threads&quot;: &quot;6&quot;, &quot;--ubatch-size&quot;: &quot;512&quot;} |
| Actual tuning / weight artifact / engine kernel | {&quot;artifact_state&quot;: &quot;SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED&quot;, &quot;declared_profile&quot;: &quot;official_QAT_fast_T1_P095_K64_MBPP32_1024&quot;, &quot;draft_artifact&quot;: null, &quot;draft_model_sha256&quot;: null, &quot;engine_build_id&quot;: &quot;dded13c80bc8e7d01a43ac6745d06bb22d7a15a3f5fba68729c536286e5066d4&quot;, &quot;engine_source_commit&quot;: null, &quot;environment_knobs&quot;: {&quot;GGML_CUDA_GRAPH_OPT&quot;: &quot;0&quot;, &quot;GGML_CUDA_O2_WEIGHT_CACHE_MIB&quot;: &quot;0&quot;}, &quot;executed_model_sha256&quot;: &quot;93567e57a8fe10b23569b9d9ec38cd005deedf71e29477c421a4b83f418a538b&quot;, &quot;interpretation&quot;: &quot;No-MTP inference does not imply a non-grafted weight file. GRAPH_OPT=0 does not imply CUDA Graphs disabled. An absent setting is unrecorded, never assumed off.&quot;, &quot;kernel_library&quot;: &quot;libggml-cuda.so.0.26.0&quot;, &quot;kernel_library_sha256&quot;: &quot;f76ecefe4dff5bb7bacf5721159b607f008d7f23b0fc848134637b6673b0e1f5&quot;, &quot;runtime_flags&quot;: {&quot;--batch-size&quot;: &quot;2048&quot;, &quot;--cache-reuse&quot;: &quot;0&quot;, &quot;--cache-type-k&quot;: &quot;f16&quot;, &quot;--cache-type-v&quot;: &quot;f16&quot;, &quot;--ctx-checkpoints&quot;: &quot;2&quot;, &quot;--ctx-size&quot;: &quot;8192&quot;, &quot;--flash-attn&quot;: &quot;auto&quot;, &quot;--n-gpu-layers&quot;: &quot;99&quot;, &quot;--parallel&quot;: &quot;1&quot;, &quot;--reasoning&quot;: &quot;off&quot;, &quot;--spec-type&quot;: &quot;none&quot;, &quot;--threads&quot;: &quot;6&quot;, &quot;--ubatch-size&quot;: &quot;512&quot;}, &quot;weight_artifact&quot;: &quot;gemma-4-12b-it-qat-q4_0.gguf&quot;} |
| Tuning provenance | Pinned executed launch; executed launch SHA=cb2446d577f2f691cb10efb59fdf089464a54fcefc8b12145e8c17bbb214d5dd |
| Sampling / output cap | {&quot;min_p&quot;: 0.0, &quot;presence_penalty&quot;: 0.0, &quot;repeat_penalty&quot;: 1.0, &quot;seed&quot;: 1001, &quot;temperature&quot;: 1.0, &quot;top_k&quot;: 64, &quot;top_p&quot;: 0.95} / 1024 |
| Cache / timing scope | Warm model; per-request KV reset; OS file cache uncontrolled; model startup excluded |
| Measurement batches | R427:32 + R428:191, disjoint tasks; no repeats |
| Actual template controls | {&quot;enable_thinking&quot;: false} |
| Actual input-token range (if exported) | Not included in this public aggregate |
| Task count / repeats | 223 unique; one observed answer per task; no repeated-run uncertainty measured |
| Model SHA-256 | 93567e57a8fe10b23569b9d9ec38cd005deedf71e29477c421a4b83f418a538b |
| Engine binary SHA-256 | 08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54 |
| Template SHA-256 | ae53464bf3be25802b3a5b37def7fd89667067d7577049b3b2d74c4d8de4c6d4 |
| Scorer adapter SHA-256 | 1b044c31ebf9fa65aff9540afb50ab5e756af65cf464afcc78770131a76728d7 |
| EvalPlus provenance SHA-256 | Not applicable / not duplicated |
| Plan SHA-256 | 6e9646206b88a6d093d60ea2d1e163ad71247f87d33dadcc3ac61f792749ab67 |

Original audit SHA-256 (originals retained privately; public excerpts are not the original files):

- [audit-a496d811bed11b4d3351](audits/audit-a496d811bed11b4d3351.md): `a496d811bed11b4d3351353f73538f1922ff39dfdaef39e2c8e23f0f4850dd9f`
- [audit-1b31ba0c1159d8d3f3cd](audits/audit-1b31ba0c1159d8d3f3cd.md): `1b31ba0c1159d8d3f3cd1f3ff75c30157616d2ed5cd192f1ee9c4f39388c6401`
- [audit-f19c98d28f6d0f2baf73](audits/audit-f19c98d28f6d0f2baf73.md): `f19c98d28f6d0f2baf7356728309b91b1e04a95a5555932392d7e6fcb26c36d0`
- [audit-ff32d141eb26b6f4d1eb](audits/audit-ff32d141eb26b6f4d1eb.md): `ff32d141eb26b6f4d1ebb3cbc94ff906b85dba3b0e43657d9dc4e46822710c42`
- [audit-a496d811bed11b4d3351](audits/audit-a496d811bed11b4d3351.md): `a496d811bed11b4d3351353f73538f1922ff39dfdaef39e2c8e23f0f4850dd9f`

## Native Tools · balanced 100

Frozen balanced native-tool subset: 100 cases, 20 in each of five categories; official AST plus irrelevance rules; not full BFCL leaderboard.

Task identity: `7c273de654cb6f5dec4dacb5d65b1ea8cd236c8dac9ba674ecfed21e292b8698`. **Task-matched whole-configuration comparisons**; native sampling, budgets and builds are shown below. These are development results, with no repeated-seed model-superiority claim. Record dates come from the original audit or frozen plan; missing dates remain labelled.

![Native Tools · balanced 100: Successful tasks; missing results labelled NOT MEASURED](assets/benchmarks/tools-success.svg){ .benchmark-svg }

![Native Tools · balanced 100: Mean task E2E; missing results labelled NOT MEASURED](assets/benchmarks/tools-latency.svg){ .benchmark-svg }

![Native Tools · balanced 100: GPU energy per success; missing results labelled NOT MEASURED](assets/benchmarks/tools-energy.svg){ .benchmark-svg }

![Native Tools · balanced 100: Peak device VRAM; missing results labelled NOT MEASURED](assets/benchmarks/tools-vram.svg){ .benchmark-svg }

| Profile / record date | Success | Successful tasks/s | Total task time / GPU energy | Peak VRAM | Audit |
|---|---|---|---|---|---|
| OmniCoder2 9B Q6_K — MTP; fast / NOT RECORDED | 88/100 | 0.82237 | 107.007 s / 27438.98 J | NOT MEASURED | [R183](experiments/R183.md) |
| Qwen3.5 9B Q4_K_M — Fast non-reasoning / 2026-10-20 | 87/100 | 0.70201 | 123.930 s / 32539.27 J | 5956.5 | [R227](experiments/R227.md) |
| Gemma4 12B IT QAT Q4_0 — Fast non-reasoning / 2026-10-22 | 84/100 | 0.58041 | 144.726 s / 34637.24 J | 8118.5 | [R424](experiments/R424.md) |
| Ternary Bonsai 2 27B PQ2_0 — Thinking medium; 4096 output / 2026-10-21 | 90/100 | 0.15166 | 593.425 s / 159652.16 J | 8158.5 | [R281](experiments/R281.md) |

### OmniCoder2 9B · Q6_K · R183

MTP; fast. No additional policy claim is inferred from this discipline.

| Condition | Audited value |
|---|---|
| Separate process-VRAM observation (not device peak) | 8758 |
| Hardware / power | Tesla V100-SXM2 16 GB HBM2 / 300 W |
| Engine | llama.cpp / CUDA 12.8 / SM70 (exact audited binary below) |
| Date | NOT RECORDED |
| Context, batching, KV, speculation | {&quot;--batch-size&quot;: &quot;2048&quot;, &quot;--cache-type-k&quot;: &quot;f16&quot;, &quot;--cache-type-v&quot;: &quot;f16&quot;, &quot;--ctx-size&quot;: &quot;8192&quot;, &quot;--reasoning&quot;: &quot;off&quot;, &quot;--spec-draft-n-max&quot;: &quot;3&quot;, &quot;--spec-type&quot;: &quot;draft-mtp&quot;, &quot;--threads&quot;: &quot;6&quot;, &quot;--ubatch-size&quot;: &quot;512&quot;} |
| Actual tuning / weight artifact / engine kernel | {&quot;artifact_state&quot;: &quot;SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED&quot;, &quot;declared_profile&quot;: null, &quot;draft_artifact&quot;: &quot;Qwen3.5-9B-MTP-ONLY-Q6_K.gguf&quot;, &quot;draft_model_sha256&quot;: &quot;a794337c734d5536b150dbed898d7c3b406fb6f34dc65f53f5309e6fa4efb623&quot;, &quot;engine_build_id&quot;: &quot;dded13c80bc8e7d01a43ac6745d06bb22d7a15a3f5fba68729c536286e5066d4&quot;, &quot;engine_source_commit&quot;: null, &quot;environment_knobs&quot;: {&quot;GGML_CUDA_GRAPH_OPT&quot;: &quot;0&quot;}, &quot;executed_model_sha256&quot;: &quot;b0c1664c86338be24090a45d8b86bd106ba755d004f8746d99ee5ad69258fc3b&quot;, &quot;interpretation&quot;: &quot;No-MTP inference does not imply a non-grafted weight file. GRAPH_OPT=0 does not imply CUDA Graphs disabled. An absent setting is unrecorded, never assumed off.&quot;, &quot;kernel_library&quot;: &quot;libggml-cuda.so.0.26.0&quot;, &quot;kernel_library_sha256&quot;: &quot;f76ecefe4dff5bb7bacf5721159b607f008d7f23b0fc848134637b6673b0e1f5&quot;, &quot;runtime_flags&quot;: {&quot;--batch-size&quot;: &quot;2048&quot;, &quot;--cache-type-k&quot;: &quot;f16&quot;, &quot;--cache-type-v&quot;: &quot;f16&quot;, &quot;--ctx-checkpoints&quot;: &quot;2&quot;, &quot;--ctx-size&quot;: &quot;8192&quot;, &quot;--flash-attn&quot;: &quot;auto&quot;, &quot;--n-gpu-layers&quot;: &quot;99&quot;, &quot;--parallel&quot;: &quot;1&quot;, &quot;--reasoning&quot;: &quot;off&quot;, &quot;--spec-draft-n-max&quot;: &quot;3&quot;, &quot;--spec-draft-n-min&quot;: &quot;1&quot;, &quot;--spec-type&quot;: &quot;draft-mtp&quot;, &quot;--threads&quot;: &quot;6&quot;, &quot;--ubatch-size&quot;: &quot;512&quot;}, &quot;weight_artifact&quot;: &quot;OmniCoder-2-9B.Q6_K.gguf&quot;} |
| Tuning provenance | Pinned executed launch; executed launch SHA=96a33344adf44abaf1855b5be80ec75be760653e8b706f0672019fdad9c84978 |
| Sampling / output cap | {&quot;seed&quot;: 1001, &quot;temperature&quot;: 0} / 1024 |
| Cache / timing scope | Warm model; per-request KV reset; OS file cache uncontrolled; model startup excluded |
| Measurement batches | Single suite or repeated cycles as stated |
| Actual template controls | See pinned native request evidence |
| Actual input-token range (if exported) | Not included in this public aggregate |
| Task count / repeats | 100 unique; one observed answer per task; no repeated-run uncertainty measured |
| Model SHA-256 | b0c1664c86338be24090a45d8b86bd106ba755d004f8746d99ee5ad69258fc3b |
| Engine binary SHA-256 | 08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54 |
| Template SHA-256 | a4aee8afcf2e0711942cf848899be66016f8d14a889ff9ede07bca099c28f715 |
| Scorer adapter SHA-256 | 55290a596d5e49a066e58ba5ce3cc6c204520e730078e27abc4f50831782678d |
| EvalPlus provenance SHA-256 | Not applicable / not duplicated |
| Plan SHA-256 | 3de468fe73193dd6faa10bf982d9b022be06f1018d587b50399e03f1a88efd55 |

Original audit SHA-256 (originals retained privately; public excerpts are not the original files):

- [audit-74d034ef6a5873b4a5e9](audits/audit-74d034ef6a5873b4a5e9.md): `74d034ef6a5873b4a5e96b0fef4f39dcf84706bad9ee7d1baa3800b4dd7cefc2`

### Qwen3.5 9B · Q4_K_M · R227

Fast non-reasoning. No additional policy claim is inferred from this discipline.

| Condition | Audited value |
|---|---|
| Separate process-VRAM observation (not device peak) | NOT MEASURED |
| Hardware / power | Tesla V100-SXM2 16 GB HBM2 / 300 W |
| Engine | llama.cpp / CUDA 12.8 / SM70 (exact audited binary below) |
| Date | 2026-10-20 |
| Context, batching, KV, speculation | {&quot;--batch-size&quot;: &quot;2048&quot;, &quot;--cache-type-k&quot;: &quot;f16&quot;, &quot;--cache-type-v&quot;: &quot;f16&quot;, &quot;--ctx-size&quot;: &quot;8192&quot;, &quot;--reasoning&quot;: &quot;off&quot;, &quot;--threads&quot;: &quot;6&quot;, &quot;--ubatch-size&quot;: &quot;512&quot;} |
| Actual tuning / weight artifact / engine kernel | {&quot;artifact_state&quot;: &quot;SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED&quot;, &quot;declared_profile&quot;: null, &quot;draft_artifact&quot;: null, &quot;draft_model_sha256&quot;: null, &quot;engine_build_id&quot;: &quot;dded13c80bc8e7d01a43ac6745d06bb22d7a15a3f5fba68729c536286e5066d4&quot;, &quot;engine_source_commit&quot;: null, &quot;environment_knobs&quot;: {&quot;GGML_CUDA_GRAPH_OPT&quot;: &quot;0&quot;}, &quot;executed_model_sha256&quot;: &quot;02d45dc1cf451ba2475ac33b301c2dd8f985abe4c182ce04a1f2f5bf0260278d&quot;, &quot;interpretation&quot;: &quot;No-MTP inference does not imply a non-grafted weight file. GRAPH_OPT=0 does not imply CUDA Graphs disabled. An absent setting is unrecorded, never assumed off.&quot;, &quot;kernel_library&quot;: &quot;libggml-cuda.so.0.26.0&quot;, &quot;kernel_library_sha256&quot;: &quot;f76ecefe4dff5bb7bacf5721159b607f008d7f23b0fc848134637b6673b0e1f5&quot;, &quot;runtime_flags&quot;: {&quot;--batch-size&quot;: &quot;2048&quot;, &quot;--cache-reuse&quot;: &quot;0&quot;, &quot;--cache-type-k&quot;: &quot;f16&quot;, &quot;--cache-type-v&quot;: &quot;f16&quot;, &quot;--ctx-checkpoints&quot;: &quot;2&quot;, &quot;--ctx-size&quot;: &quot;8192&quot;, &quot;--flash-attn&quot;: &quot;on&quot;, &quot;--n-gpu-layers&quot;: &quot;99&quot;, &quot;--parallel&quot;: &quot;1&quot;, &quot;--reasoning&quot;: &quot;off&quot;, &quot;--threads&quot;: &quot;6&quot;, &quot;--ubatch-size&quot;: &quot;512&quot;}, &quot;weight_artifact&quot;: &quot;qwen3.5-9b.gguf&quot;} |
| Tuning provenance | Pinned executed launch; executed launch SHA=0c661184b276de887ef6001036e32e895b0cb07a39f79a19b6ff892cfef6edbb |
| Sampling / output cap | {&quot;seed&quot;: 1001, &quot;temperature&quot;: 0} / NOT RECORDED |
| Cache / timing scope | Warm model; per-request KV reset; OS file cache uncontrolled; model startup excluded |
| Measurement batches | Single suite or repeated cycles as stated |
| Actual template controls | See pinned native request evidence |
| Actual input-token range (if exported) | Not included in this public aggregate |
| Task count / repeats | 100 unique; one observed answer per task; no repeated-run uncertainty measured |
| Model SHA-256 | 02d45dc1cf451ba2475ac33b301c2dd8f985abe4c182ce04a1f2f5bf0260278d |
| Engine binary SHA-256 | 08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54 |
| Template SHA-256 | a4aee8afcf2e0711942cf848899be66016f8d14a889ff9ede07bca099c28f715 |
| Scorer adapter SHA-256 | 55290a596d5e49a066e58ba5ce3cc6c204520e730078e27abc4f50831782678d |
| EvalPlus provenance SHA-256 | 332b4dfcdd92cb653859dd392c9e2430726aa85cc6560dcfc76282d06310e64d |
| Plan SHA-256 | 04cef369fdba9073bd68111484d2163709a381f4b79e610da049aec1a5a9b887 |

Original audit SHA-256 (originals retained privately; public excerpts are not the original files):

- [audit-3282effcb0cfa011c3fa](audits/audit-3282effcb0cfa011c3fa.md): `3282effcb0cfa011c3fa3df749c6a84d28051aaebad9d1b286031a3190c7df83`

### Gemma4 12B IT QAT · Q4_0 · R424

Fast non-reasoning. No additional policy claim is inferred from this discipline.

| Condition | Audited value |
|---|---|
| Separate process-VRAM observation (not device peak) | NOT MEASURED |
| Hardware / power | Tesla V100-SXM2 16 GB HBM2 / 300 W |
| Engine | llama.cpp / CUDA 12.8 / SM70 (exact audited binary below) |
| Date | 2026-10-22 |
| Context, batching, KV, speculation | {&quot;--batch-size&quot;: &quot;2048&quot;, &quot;--cache-type-k&quot;: &quot;f16&quot;, &quot;--cache-type-v&quot;: &quot;f16&quot;, &quot;--ctx-size&quot;: &quot;8192&quot;, &quot;--reasoning&quot;: &quot;off&quot;, &quot;--spec-type&quot;: &quot;none&quot;, &quot;--threads&quot;: &quot;6&quot;, &quot;--ubatch-size&quot;: &quot;512&quot;} |
| Actual tuning / weight artifact / engine kernel | {&quot;artifact_state&quot;: &quot;SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED&quot;, &quot;declared_profile&quot;: &quot;official_QAT_fast_T1_P095_K64_native_function_calling1024&quot;, &quot;draft_artifact&quot;: null, &quot;draft_model_sha256&quot;: null, &quot;engine_build_id&quot;: &quot;dded13c80bc8e7d01a43ac6745d06bb22d7a15a3f5fba68729c536286e5066d4&quot;, &quot;engine_source_commit&quot;: null, &quot;environment_knobs&quot;: {&quot;GGML_CUDA_GRAPH_OPT&quot;: &quot;0&quot;}, &quot;executed_model_sha256&quot;: &quot;93567e57a8fe10b23569b9d9ec38cd005deedf71e29477c421a4b83f418a538b&quot;, &quot;interpretation&quot;: &quot;No-MTP inference does not imply a non-grafted weight file. GRAPH_OPT=0 does not imply CUDA Graphs disabled. An absent setting is unrecorded, never assumed off.&quot;, &quot;kernel_library&quot;: &quot;libggml-cuda.so.0.26.0&quot;, &quot;kernel_library_sha256&quot;: &quot;f76ecefe4dff5bb7bacf5721159b607f008d7f23b0fc848134637b6673b0e1f5&quot;, &quot;runtime_flags&quot;: {&quot;--batch-size&quot;: &quot;2048&quot;, &quot;--cache-reuse&quot;: &quot;0&quot;, &quot;--cache-type-k&quot;: &quot;f16&quot;, &quot;--cache-type-v&quot;: &quot;f16&quot;, &quot;--ctx-checkpoints&quot;: &quot;2&quot;, &quot;--ctx-size&quot;: &quot;8192&quot;, &quot;--flash-attn&quot;: &quot;auto&quot;, &quot;--n-gpu-layers&quot;: &quot;99&quot;, &quot;--parallel&quot;: &quot;1&quot;, &quot;--reasoning&quot;: &quot;off&quot;, &quot;--spec-type&quot;: &quot;none&quot;, &quot;--threads&quot;: &quot;6&quot;, &quot;--ubatch-size&quot;: &quot;512&quot;}, &quot;weight_artifact&quot;: &quot;gemma-4-12b-it-qat-q4_0.gguf&quot;} |
| Tuning provenance | Pinned executed launch; executed launch SHA=7f57fcd2963fa613f6dc0252c5be6a15e52629d0233106694422274f172fbc96 |
| Sampling / output cap | {&quot;min_p&quot;: 0.0, &quot;presence_penalty&quot;: 0.0, &quot;repeat_penalty&quot;: 1.0, &quot;seed&quot;: 1001, &quot;temperature&quot;: 1.0, &quot;top_k&quot;: 64, &quot;top_p&quot;: 0.95} / 1024 |
| Cache / timing scope | Warm model; per-request KV reset; OS file cache uncontrolled; model startup excluded |
| Measurement batches | Single suite or repeated cycles as stated |
| Actual template controls | See pinned native request evidence |
| Actual input-token range (if exported) | Not included in this public aggregate |
| Task count / repeats | 100 unique; one observed answer per task; no repeated-run uncertainty measured |
| Model SHA-256 | 93567e57a8fe10b23569b9d9ec38cd005deedf71e29477c421a4b83f418a538b |
| Engine binary SHA-256 | 08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54 |
| Template SHA-256 | ae53464bf3be25802b3a5b37def7fd89667067d7577049b3b2d74c4d8de4c6d4 |
| Scorer adapter SHA-256 | 55290a596d5e49a066e58ba5ce3cc6c204520e730078e27abc4f50831782678d |
| EvalPlus provenance SHA-256 | 332b4dfcdd92cb653859dd392c9e2430726aa85cc6560dcfc76282d06310e64d |
| Plan SHA-256 | fb0bbe31323fc9bb761a901bca0bcdae8ce43d729dddee41acd188784f4a979e |

Original audit SHA-256 (originals retained privately; public excerpts are not the original files):

- [audit-45e2cae381364ba4f29f](audits/audit-45e2cae381364ba4f29f.md): `45e2cae381364ba4f29f2c96e7d010d2eb28b3bc53eb87de4b5f31a2910c2011`

### Ternary Bonsai 2 27B · PQ2_0 · R281

Thinking medium; 4096 output. No additional policy claim is inferred from this discipline.

| Condition | Audited value |
|---|---|
| Separate process-VRAM observation (not device peak) | NOT MEASURED |
| Hardware / power | Tesla V100-SXM2 16 GB HBM2 / 300 W |
| Engine | llama.cpp / CUDA 12.8 / SM70 (exact audited binary below) |
| Date | 2026-10-21 |
| Context, batching, KV, speculation | {&quot;--batch-size&quot;: &quot;2048&quot;, &quot;--cache-type-k&quot;: &quot;f16&quot;, &quot;--cache-type-v&quot;: &quot;f16&quot;, &quot;--ctx-size&quot;: &quot;8192&quot;, &quot;--reasoning&quot;: &quot;on&quot;, &quot;--spec-type&quot;: &quot;none&quot;, &quot;--threads&quot;: &quot;6&quot;, &quot;--ubatch-size&quot;: &quot;512&quot;} |
| Actual tuning / weight artifact / engine kernel | {&quot;artifact_state&quot;: &quot;SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED&quot;, &quot;declared_profile&quot;: &quot;published_medium_thinking_4096&quot;, &quot;draft_artifact&quot;: null, &quot;draft_model_sha256&quot;: null, &quot;engine_build_id&quot;: &quot;bonsai-pq2-sm70-9a9394a895b9&quot;, &quot;engine_source_commit&quot;: null, &quot;environment_knobs&quot;: {&quot;GGML_CUDA_GRAPH_OPT&quot;: &quot;0&quot;, &quot;GGML_CUDA_O2_WEIGHT_CACHE_MIB&quot;: &quot;0&quot;}, &quot;executed_model_sha256&quot;: &quot;3907dc1658db1f78a9826bf8d5bcb8dc65db0d466388937af57f2294fae62ec1&quot;, &quot;interpretation&quot;: &quot;No-MTP inference does not imply a non-grafted weight file. GRAPH_OPT=0 does not imply CUDA Graphs disabled. An absent setting is unrecorded, never assumed off.&quot;, &quot;kernel_library&quot;: &quot;libggml-cuda.so.0.21.0&quot;, &quot;kernel_library_sha256&quot;: &quot;60c874aa652e9eb7d09ae128b79d31cbe0042f5e76476fd1d3192c47e7291d12&quot;, &quot;runtime_flags&quot;: {&quot;--batch-size&quot;: &quot;2048&quot;, &quot;--cache-reuse&quot;: &quot;0&quot;, &quot;--cache-type-k&quot;: &quot;f16&quot;, &quot;--cache-type-v&quot;: &quot;f16&quot;, &quot;--ctx-checkpoints&quot;: &quot;2&quot;, &quot;--ctx-size&quot;: &quot;8192&quot;, &quot;--flash-attn&quot;: &quot;on&quot;, &quot;--n-gpu-layers&quot;: &quot;99&quot;, &quot;--parallel&quot;: &quot;1&quot;, &quot;--reasoning&quot;: &quot;on&quot;, &quot;--spec-type&quot;: &quot;none&quot;, &quot;--threads&quot;: &quot;6&quot;, &quot;--ubatch-size&quot;: &quot;512&quot;}, &quot;weight_artifact&quot;: &quot;Ternary-Bonsai-2-27B-PQ2_0.gguf&quot;} |
| Tuning provenance | Frozen plan; executed launch SHA=NOT RECORDED |
| Sampling / output cap | {&quot;min_p&quot;: 0.05, &quot;presence_penalty&quot;: 0.0, &quot;repeat_penalty&quot;: 1.0, &quot;seed&quot;: 1001, &quot;temperature&quot;: 1.0, &quot;top_k&quot;: 20, &quot;top_p&quot;: 0.95} / 4096 |
| Cache / timing scope | Warm model; per-request KV reset; OS file cache uncontrolled; model startup excluded |
| Measurement batches | Single suite or repeated cycles as stated |
| Actual template controls | See pinned native request evidence |
| Actual input-token range (if exported) | Not included in this public aggregate |
| Task count / repeats | 100 unique; one observed answer per task; no repeated-run uncertainty measured |
| Model SHA-256 | 3907dc1658db1f78a9826bf8d5bcb8dc65db0d466388937af57f2294fae62ec1 |
| Engine binary SHA-256 | 94c60d4646249fe067c75a56b15e6a8a9070a5e422cae16ee8dd9973389a6a27 |
| Template SHA-256 | See exact plan audit; not duplicated in public subset |
| Scorer adapter SHA-256 | b0c619f7f1022b4c06c18ba6c6e608006e1609b667ed0d90a399f906afd2c2a5 |
| EvalPlus provenance SHA-256 | Not applicable / not duplicated |
| Plan SHA-256 | c47c5993a526d67abb70d1cba56e1d9741cd82cb89ced1f488c179f7d5566555 |

Original audit SHA-256 (originals retained privately; public excerpts are not the original files):

- [audit-66c5bf1378a74271d1b1](audits/audit-66c5bf1378a74271d1b1.md): `66c5bf1378a74271d1b1ac12af19cd2490388f09906312cec02483605e71a1c3`
- [audit-6ba69d79b075c99f03ac](audits/audit-6ba69d79b075c99f03ac.md): `6ba69d79b075c99f03acc9d8dd5e343d27771106cebbbdbc0c6a0629a73e868f`
- [audit-c1f01d3d15d56ff49206](audits/audit-c1f01d3d15d56ff49206.md): `c1f01d3d15d56ff49206bcb86e1c8b925163c79ce3e41c61794fb7a490826981`

## Missing and partial evidence

A missing bar means no complete audited result under that cohort. In particular, a native echo-control is not a BFCL score, a truncated QA screen is not HumanEval+, and a 2/4 agent early stop is not an 18-task score. See [all model admission stages and negative screens](models.md) and [experiment history](results.md). No existing negative result or qualification limit is removed.

## Supplemental local tests

Own agent, QA, long-context and historical synthetic results remain [available separately](local-benchmarks.md). No combined score is calculated.
