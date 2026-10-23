# Supplemental laboratory benchmarks

These local agent, QA, context and native performance tests remain auditable but do not contribute to the official-category percentage mean. [Return to official benchmark results](benchmarks.md).

## Agents · isolated 18

Frozen 18 development agent tasks with unchanged effect/policy simulator; all tools isolated; not a new holdout.

Task identity: `104b1abf22c5d6ea46d7d29e3186a3c540b39140cf4e1feadbec0ec6f871e186`. **Task-matched whole-configuration comparisons**; native sampling, budgets and builds are shown below. These are development results, with no repeated-seed model-superiority claim. Record dates come from the original audit or frozen plan; missing dates remain labelled.

![Agents · isolated 18: Successful tasks; missing results labelled NOT MEASURED](assets/benchmarks/agents-success.svg){ .benchmark-svg }

![Agents · isolated 18: Mean task E2E; missing results labelled NOT MEASURED](assets/benchmarks/agents-latency.svg){ .benchmark-svg }

![Agents · isolated 18: GPU energy per success; missing results labelled NOT MEASURED](assets/benchmarks/agents-energy.svg){ .benchmark-svg }

![Agents · isolated 18: Peak device VRAM; missing results labelled NOT MEASURED](assets/benchmarks/agents-vram.svg){ .benchmark-svg }

| Profile / record date | Success | Successful tasks/s | Total task time / GPU energy | Peak VRAM | Audit |
|---|---|---|---|---|---|
| Qwen3.5 9B Q4_K_M — Fast non-reasoning; no MTP / 2026-10-20 | 8/18 | 0.03729 | 214.550 s / 56164.79 J | 5956.5 | [R228](experiments/R228.md) |
| Ornith 1.5 9B Q6_K — Fast non-reasoning; no MTP / 2026-10-20 | 14/18 | 0.06949 | 201.470 s / 54846.31 J | 7356.5 | [R253](experiments/R253.md) |
| Qwen3.8 27B GSQ/RCO IQ3_S — Fast non-reasoning; no MTP / 2026-10-20 | 14/18 | 0.02934 | 477.196 s / 130284.60 J | 12454.5 | [R260](experiments/R260.md) |
| Gemma4 12B IT QAT Q4_0 — Fast non-reasoning; no MTP / 2026-10-22 | 9/18 | 0.02778 | 323.942 s / 79448.26 J | 8118.5 | [R426](experiments/R426.md) |
| Ternary Bonsai 2 27B PQ2_0 — Thinking medium; local2048; independent repeat / 2026-10-22 | 17/18 | 0.02835 | 599.644 s / 161928.85 J | 8158.5 | [R440](experiments/R440.md) |
| Ternary Bonsai 2 27B PQ2_0 — Thinking medium; prefix reuse; local2048; qualified18-task profile / 2026-10-22 | 18/18 | 0.03945 | 456.320 s / 121439.49 J | 8158.5 | [R442](experiments/R442.md) |
| Qwen3.8 27B GSQ/RCO IQ3_S — Fast; MTP3 / 2026-10-20 | 14/18 | 0.03425 | 408.702 s / 105913.80 J | 13600.5 | [R261](experiments/R261.md) |
| OmniCoder2 9B Q6_K — MTP + weight cache; 300 W / 2026-10-20 | 13/18 | 0.08002 | 162.465 s / 41893.39 J | 14106.5 | [R219](experiments/R219.md) |
| Ternary Bonsai 2 27B PQ2_0 — Thinking medium; 2048 output / 2026-10-21 | 17/18 | 0.02838 | 599.016 s / 161409.67 J | 8158.5 | [R286](experiments/R286.md) |

### Qwen3.5 9B · Q4_K_M · R228

Fast non-reasoning; no MTP. Additional policy violations observed; no assistant qualification

| Condition | Audited value |
|---|---|
| Separate process-VRAM observation (not device peak) | NOT MEASURED |
| Hardware / power | Tesla V100-SXM2 16 GB HBM2 / 300 W |
| Engine | llama.cpp / CUDA 12.8 / SM70 (exact audited binary below) |
| Date | 2026-10-20 |
| Context, batching, KV, speculation | {"--batch-size": "2048", "--cache-type-k": "f16", "--cache-type-v": "f16", "--ctx-size": "8192", "--reasoning": "off", "--threads": "6", "--ubatch-size": "512", "retain_prefix": false} |
| Actual tuning / weight artifact / engine kernel | {"artifact_state": "SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED", "declared_profile": null, "draft_artifact": null, "draft_model_sha256": null, "engine_build_id": "dded13c80bc8e7d01a43ac6745d06bb22d7a15a3f5fba68729c536286e5066d4", "engine_source_commit": null, "environment_knobs": {"GGML_CUDA_GRAPH_OPT": "0"}, "executed_model_sha256": "02d45dc1cf451ba2475ac33b301c2dd8f985abe4c182ce04a1f2f5bf0260278d", "interpretation": "No-MTP inference does not imply a non-grafted weight file. GRAPH_OPT=0 does not imply CUDA Graphs disabled. An absent setting is unrecorded, never assumed off.", "kernel_library": "libggml-cuda.so.0.26.0", "kernel_library_sha256": "f76ecefe4dff5bb7bacf5721159b607f008d7f23b0fc848134637b6673b0e1f5", "runtime_flags": {"--batch-size": "2048", "--cache-reuse": "0", "--cache-type-k": "f16", "--cache-type-v": "f16", "--ctx-checkpoints": "2", "--ctx-size": "8192", "--flash-attn": "on", "--n-gpu-layers": "99", "--parallel": "1", "--reasoning": "off", "--threads": "6", "--ubatch-size": "512"}, "weight_artifact": "qwen3.5-9b.gguf"} |
| Tuning provenance | Pinned executed launch; executed launch SHA=c50f0ed3e069576b1731c02b966309d67a5356a7f6ff6de01d5e74cb826e0ec3 |
| Sampling / output cap | {"seed": 1001, "temperature": 0} / 1400 |
| Cache / timing scope | Warm model; per-request KV reset; OS file cache uncontrolled; model startup excluded |
| Measurement batches | Single suite or repeated cycles as stated |
| Actual template controls | See pinned native request evidence |
| Actual input-token range (if exported) | Not included in this public aggregate |
| Task count / repeats | 18 unique; one observed answer per task; no repeated-run uncertainty measured |
| Model SHA-256 | 02d45dc1cf451ba2475ac33b301c2dd8f985abe4c182ce04a1f2f5bf0260278d |
| Engine binary SHA-256 | 08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54 |
| Template SHA-256 | a4aee8afcf2e0711942cf848899be66016f8d14a889ff9ede07bca099c28f715 |
| Scorer adapter SHA-256 | See audit scoring contract |
| EvalPlus provenance SHA-256 | Not applicable / not duplicated |
| Plan SHA-256 | fa8712f46e5cc987775cecd5fe3662414cd31b252b614f51c550946f5f704cb1 |

Original audit SHA-256 (originals retained privately; public excerpts are not the original files):

- [audit-f48de8313838adc8b3b4](audits/audit-f48de8313838adc8b3b4.md): `f48de8313838adc8b3b4940143dd90a7822a1e350aca33f67feaafb6318cebf3`

### Ornith 1.5 9B · Q6_K · R253

Fast non-reasoning; no MTP. Additional policy violations observed; no assistant qualification

| Condition | Audited value |
|---|---|
| Separate process-VRAM observation (not device peak) | NOT MEASURED |
| Hardware / power | Tesla V100-SXM2 16 GB HBM2 / 300 W |
| Engine | llama.cpp / CUDA 12.8 / SM70 (exact audited binary below) |
| Date | 2026-10-20 |
| Context, batching, KV, speculation | {"--batch-size": "2048", "--cache-type-k": "f16", "--cache-type-v": "f16", "--ctx-size": "8192", "--reasoning": "off", "--spec-type": "none", "--threads": "6", "--ubatch-size": "512", "retain_prefix": false} |
| Actual tuning / weight artifact / engine kernel | {"artifact_state": "SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED", "declared_profile": null, "draft_artifact": null, "draft_model_sha256": null, "engine_build_id": "dded13c80bc8e7d01a43ac6745d06bb22d7a15a3f5fba68729c536286e5066d4", "engine_source_commit": null, "environment_knobs": {"GGML_CUDA_GRAPH_OPT": "0"}, "executed_model_sha256": "b6f76e74f86245b3caee014b797c10dca931c4dfdaabfb134eab655f81e4154a", "interpretation": "No-MTP inference does not imply a non-grafted weight file. GRAPH_OPT=0 does not imply CUDA Graphs disabled. An absent setting is unrecorded, never assumed off.", "kernel_library": "libggml-cuda.so.0.26.0", "kernel_library_sha256": "f76ecefe4dff5bb7bacf5721159b607f008d7f23b0fc848134637b6673b0e1f5", "runtime_flags": {"--batch-size": "2048", "--cache-reuse": "0", "--cache-type-k": "f16", "--cache-type-v": "f16", "--ctx-checkpoints": "2", "--ctx-size": "8192", "--flash-attn": "on", "--n-gpu-layers": "99", "--parallel": "1", "--reasoning": "off", "--spec-type": "none", "--threads": "6", "--ubatch-size": "512"}, "weight_artifact": "Ornith-1.5-9B-Q6_K.gguf"} |
| Tuning provenance | Pinned executed launch; executed launch SHA=5364368307fc6b7dc42108f484801c184bfb223b82c8a9fab9d5334b2f8170ba |
| Sampling / output cap | {"seed": 1001, "temperature": 0} / 1400 |
| Cache / timing scope | Warm model; per-request KV reset; OS file cache uncontrolled; model startup excluded |
| Measurement batches | Single suite or repeated cycles as stated |
| Actual template controls | See pinned native request evidence |
| Actual input-token range (if exported) | Not included in this public aggregate |
| Task count / repeats | 18 unique; one observed answer per task; no repeated-run uncertainty measured |
| Model SHA-256 | b6f76e74f86245b3caee014b797c10dca931c4dfdaabfb134eab655f81e4154a |
| Engine binary SHA-256 | 08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54 |
| Template SHA-256 | 9dd2fbd270feaa1fbef2d4f634d7887c9c506e3bde140f8e7351c8944e8fd235 |
| Scorer adapter SHA-256 | See audit scoring contract |
| EvalPlus provenance SHA-256 | Not applicable / not duplicated |
| Plan SHA-256 | 8c20cddbcc71524da3919ade5ca0fbcc4fa72816fd1db6853348f82ea1f5a950 |

Original audit SHA-256 (originals retained privately; public excerpts are not the original files):

- [audit-c35dd0584281950f1dfd](audits/audit-c35dd0584281950f1dfd.md): `c35dd0584281950f1dfd8c72d357463f0efe9b45c10a50d5eb631bbb91325a42`

### Qwen3.8 27B · GSQ/RCO IQ3_S · R260

Fast non-reasoning; no MTP. Additional policy violations observed; no assistant qualification

| Condition | Audited value |
|---|---|
| Separate process-VRAM observation (not device peak) | NOT MEASURED |
| Hardware / power | Tesla V100-SXM2 16 GB HBM2 / 300 W |
| Engine | llama.cpp / CUDA 12.8 / SM70 (exact audited binary below) |
| Date | 2026-10-20 |
| Context, batching, KV, speculation | {"--batch-size": "2048", "--cache-type-k": "f16", "--cache-type-v": "f16", "--ctx-size": "8192", "--reasoning": "off", "--spec-type": "none", "--threads": "6", "--ubatch-size": "512", "retain_prefix": false} |
| Actual tuning / weight artifact / engine kernel | {"artifact_state": "MTP_BEARING_OR_GRAFTED_GGUF", "declared_profile": "provider_GSQ_RCO_IQ3S_27B_fast_off_noMTP", "draft_artifact": null, "draft_model_sha256": null, "engine_build_id": "dded13c80bc8e7d01a43ac6745d06bb22d7a15a3f5fba68729c536286e5066d4", "engine_source_commit": null, "environment_knobs": {"GGML_CUDA_GRAPH_OPT": "0"}, "executed_model_sha256": "58fd826723939933dc86f45b7fe04545cbc2de1c70f6fe2cdd3858c87a98c12f", "interpretation": "No-MTP inference does not imply a non-grafted weight file. GRAPH_OPT=0 does not imply CUDA Graphs disabled. An absent setting is unrecorded, never assumed off.", "kernel_library": "libggml-cuda.so.0.26.0", "kernel_library_sha256": "f76ecefe4dff5bb7bacf5721159b607f008d7f23b0fc848134637b6673b0e1f5", "runtime_flags": {"--batch-size": "2048", "--cache-reuse": "0", "--cache-type-k": "f16", "--cache-type-v": "f16", "--ctx-checkpoints": "2", "--ctx-size": "8192", "--flash-attn": "on", "--n-gpu-layers": "99", "--parallel": "1", "--reasoning": "off", "--spec-type": "none", "--threads": "6", "--ubatch-size": "512"}, "weight_artifact": "Qwen3.8-27B-GSQ-RCO-IQ3_S-mtp.gguf"} |
| Tuning provenance | Pinned executed launch; executed launch SHA=d90d33c3fcb9aadb2507f28cfa410493721994950c276f22fdb5ddbd39f56b40 |
| Sampling / output cap | {"seed": 1001, "temperature": 0} / 1400 |
| Cache / timing scope | Warm model; per-request KV reset; OS file cache uncontrolled; model startup excluded |
| Measurement batches | Single suite or repeated cycles as stated |
| Actual template controls | See pinned native request evidence |
| Actual input-token range (if exported) | Not included in this public aggregate |
| Task count / repeats | 18 unique; one observed answer per task; no repeated-run uncertainty measured |
| Model SHA-256 | 58fd826723939933dc86f45b7fe04545cbc2de1c70f6fe2cdd3858c87a98c12f |
| Engine binary SHA-256 | 08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54 |
| Template SHA-256 | c3cf9e34abf4f9e36c2d72165aa9c132d3e2a725b6c2586aaa3a8af9d7a81041 |
| Scorer adapter SHA-256 | See audit scoring contract |
| EvalPlus provenance SHA-256 | Not applicable / not duplicated |
| Plan SHA-256 | fb28c2f2e80ced215af46c100f17c9f9c3192e629f3e5efde7683776967b278b |

Original audit SHA-256 (originals retained privately; public excerpts are not the original files):

- [audit-7ea265b5613fdf6bd79c](audits/audit-7ea265b5613fdf6bd79c.md): `7ea265b5613fdf6bd79c6760b4925284a8c3d434edace84ad822e0982651cf0d`

### Gemma4 12B IT QAT · Q4_0 · R426

Fast non-reasoning; no MTP. Additional policy violations observed; no assistant qualification

| Condition | Audited value |
|---|---|
| Separate process-VRAM observation (not device peak) | NOT MEASURED |
| Hardware / power | Tesla V100-SXM2 16 GB HBM2 / 300 W |
| Engine | llama.cpp / CUDA 12.8 / SM70 (exact audited binary below) |
| Date | 2026-10-22 |
| Context, batching, KV, speculation | {"--batch-size": "2048", "--cache-type-k": "f16", "--cache-type-v": "f16", "--ctx-size": "8192", "--reasoning": "off", "--spec-type": "none", "--threads": "6", "--ubatch-size": "512", "retain_prefix": false} |
| Actual tuning / weight artifact / engine kernel | {"artifact_state": "SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED", "declared_profile": "official_QAT_fast_T1_P095_K64_native_agents1400", "draft_artifact": null, "draft_model_sha256": null, "engine_build_id": "dded13c80bc8e7d01a43ac6745d06bb22d7a15a3f5fba68729c536286e5066d4", "engine_source_commit": null, "environment_knobs": {"GGML_CUDA_GRAPH_OPT": "0", "GGML_CUDA_O2_WEIGHT_CACHE_MIB": "0"}, "executed_model_sha256": "93567e57a8fe10b23569b9d9ec38cd005deedf71e29477c421a4b83f418a538b", "interpretation": "No-MTP inference does not imply a non-grafted weight file. GRAPH_OPT=0 does not imply CUDA Graphs disabled. An absent setting is unrecorded, never assumed off.", "kernel_library": "libggml-cuda.so.0.26.0", "kernel_library_sha256": "f76ecefe4dff5bb7bacf5721159b607f008d7f23b0fc848134637b6673b0e1f5", "runtime_flags": {"--batch-size": "2048", "--cache-reuse": "0", "--cache-type-k": "f16", "--cache-type-v": "f16", "--ctx-checkpoints": "2", "--ctx-size": "8192", "--flash-attn": "auto", "--n-gpu-layers": "99", "--parallel": "1", "--reasoning": "off", "--spec-type": "none", "--threads": "6", "--ubatch-size": "512"}, "weight_artifact": "gemma-4-12b-it-qat-q4_0.gguf"} |
| Tuning provenance | Pinned executed launch; executed launch SHA=9d96f094876023be84f3b4a5abece6fd91975921470f27c388e5e06ec37d635c |
| Sampling / output cap | {"min_p": 0.0, "presence_penalty": 0.0, "repeat_penalty": 1.0, "seed": 1001, "temperature": 1.0, "top_k": 64, "top_p": 0.95} / 1400 |
| Cache / timing scope | Warm model; per-request KV reset; OS file cache uncontrolled; model startup excluded |
| Measurement batches | Single suite or repeated cycles as stated |
| Actual template controls | See pinned native request evidence |
| Actual input-token range (if exported) | Not included in this public aggregate |
| Task count / repeats | 18 unique; one observed answer per task; no repeated-run uncertainty measured |
| Model SHA-256 | 93567e57a8fe10b23569b9d9ec38cd005deedf71e29477c421a4b83f418a538b |
| Engine binary SHA-256 | 08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54 |
| Template SHA-256 | ae53464bf3be25802b3a5b37def7fd89667067d7577049b3b2d74c4d8de4c6d4 |
| Scorer adapter SHA-256 | See audit scoring contract |
| EvalPlus provenance SHA-256 | Not applicable / not duplicated |
| Plan SHA-256 | bc06f49a06e3fa99d8cc16a1f3c8e91dc2f4ba6aa60405198febff6dd0244d94 |

Original audit SHA-256 (originals retained privately; public excerpts are not the original files):

- [audit-021cfb8ba15cb4471b11](audits/audit-021cfb8ba15cb4471b11.md): `021cfb8ba15cb4471b111ebcbe44088d2d26d06809f01981d24db6cde1b6f4a5`

### Ternary Bonsai 2 27B · PQ2_0 · R440

Thinking medium; local2048; independent repeat. No additional policy claim is inferred from this discipline.

| Condition | Audited value |
|---|---|
| Separate process-VRAM observation (not device peak) | NOT MEASURED |
| Hardware / power | Tesla V100-SXM2 16 GB HBM2 / 300 W |
| Engine | llama.cpp / CUDA 12.8 / SM70 (exact audited binary below) |
| Date | 2026-10-22 |
| Context, batching, KV, speculation | {"--batch-size": "2048", "--cache-type-k": "f16", "--cache-type-v": "f16", "--ctx-size": "8192", "--reasoning": "on", "--spec-type": "none", "--threads": "6", "--ubatch-size": "512", "retain_prefix": false} |
| Actual tuning / weight artifact / engine kernel | {"artifact_state": "SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED", "declared_profile": "published_medium_thinking_agent2048_localcap", "draft_artifact": null, "draft_model_sha256": null, "engine_build_id": "bonsai-pq2-sm70-9a9394a895b9", "engine_source_commit": null, "environment_knobs": {"GGML_CUDA_GRAPH_OPT": "0", "GGML_CUDA_O2_WEIGHT_CACHE_MIB": "0"}, "executed_model_sha256": "3907dc1658db1f78a9826bf8d5bcb8dc65db0d466388937af57f2294fae62ec1", "interpretation": "No-MTP inference does not imply a non-grafted weight file. GRAPH_OPT=0 does not imply CUDA Graphs disabled. An absent setting is unrecorded, never assumed off.", "kernel_library": "libggml-cuda.so.0.21.0", "kernel_library_sha256": "60c874aa652e9eb7d09ae128b79d31cbe0042f5e76476fd1d3192c47e7291d12", "runtime_flags": {"--batch-size": "2048", "--cache-reuse": "0", "--cache-type-k": "f16", "--cache-type-v": "f16", "--ctx-checkpoints": "2", "--ctx-size": "8192", "--flash-attn": "on", "--n-gpu-layers": "99", "--parallel": "1", "--reasoning": "on", "--spec-type": "none", "--threads": "6", "--ubatch-size": "512"}, "weight_artifact": "Ternary-Bonsai-2-27B-PQ2_0.gguf"} |
| Tuning provenance | Pinned executed launch; executed launch SHA=7ef52300f9ff184625fd3a17be1122af7aaad7b94242a6375e0ceda6040ba51c |
| Sampling / output cap | {"min_p": 0.05, "presence_penalty": 0.0, "repeat_penalty": 1.0, "temperature": 1.0, "top_k": 20, "top_p": 0.95} / 2048 |
| Cache / timing scope | Warm model; per-request KV reset; OS file cache uncontrolled; model startup excluded |
| Measurement batches | R440:one fresh18-case repeat of the same development tasks; not a newholdout or36independent tasks |
| Actual template controls | See pinned native request evidence |
| Actual input-token range (if exported) | Not included in this public aggregate |
| Task count / repeats | 18 unique; one observed answer per task; no repeated-run uncertainty measured |
| Model SHA-256 | 3907dc1658db1f78a9826bf8d5bcb8dc65db0d466388937af57f2294fae62ec1 |
| Engine binary SHA-256 | 94c60d4646249fe067c75a56b15e6a8a9070a5e422cae16ee8dd9973389a6a27 |
| Template SHA-256 | See exact plan audit; not duplicated in public subset |
| Scorer adapter SHA-256 | See audit scoring contract |
| EvalPlus provenance SHA-256 | Not applicable / not duplicated |
| Plan SHA-256 | b10a050b49051f92a3a8fcd6960005e56e2a42ced50b6b081e0718d74f44760f |

Original audit SHA-256 (originals retained privately; public excerpts are not the original files):

- [audit-f4df3d5aa78011e3584d](audits/audit-f4df3d5aa78011e3584d.md): `f4df3d5aa78011e3584d3639348b5135ed9accc95661823a349cffc8480e018c`

### Ternary Bonsai 2 27B · PQ2_0 · R442

Thinking medium; prefix reuse; local2048; qualified18-task profile. No additional policy claim is inferred from this discipline.

| Condition | Audited value |
|---|---|
| Separate process-VRAM observation (not device peak) | NOT MEASURED |
| Hardware / power | Tesla V100-SXM2 16 GB HBM2 / 300 W |
| Engine | llama.cpp / CUDA 12.8 / SM70 (exact audited binary below) |
| Date | 2026-10-22 |
| Context, batching, KV, speculation | {"--batch-size": "2048", "--cache-type-k": "f16", "--cache-type-v": "f16", "--ctx-size": "8192", "--reasoning": "on", "--spec-type": "none", "--threads": "6", "--ubatch-size": "512", "retain_prefix": true} |
| Actual tuning / weight artifact / engine kernel | {"artifact_state": "SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED", "declared_profile": "published_medium_thinking_agent2048_localcap", "draft_artifact": null, "draft_model_sha256": null, "engine_build_id": "bonsai-pq2-sm70-9a9394a895b9", "engine_source_commit": null, "environment_knobs": {"GGML_CUDA_GRAPH_OPT": "0", "GGML_CUDA_O2_WEIGHT_CACHE_MIB": "0"}, "executed_model_sha256": "3907dc1658db1f78a9826bf8d5bcb8dc65db0d466388937af57f2294fae62ec1", "interpretation": "No-MTP inference does not imply a non-grafted weight file. GRAPH_OPT=0 does not imply CUDA Graphs disabled. An absent setting is unrecorded, never assumed off.", "kernel_library": "libggml-cuda.so.0.21.0", "kernel_library_sha256": "60c874aa652e9eb7d09ae128b79d31cbe0042f5e76476fd1d3192c47e7291d12", "runtime_flags": {"--batch-size": "2048", "--cache-reuse": "0", "--cache-type-k": "f16", "--cache-type-v": "f16", "--ctx-checkpoints": "2", "--ctx-size": "8192", "--flash-attn": "on", "--n-gpu-layers": "99", "--parallel": "1", "--reasoning": "on", "--spec-type": "none", "--threads": "6", "--ubatch-size": "512"}, "weight_artifact": "Ternary-Bonsai-2-27B-PQ2_0.gguf"} |
| Tuning provenance | Pinned executed launch; executed launch SHA=6ed4d9ef5af0d32d2137468e8e1552a15eae7347f98d52aeac1ae7fc85456e9c |
| Sampling / output cap | {"min_p": 0.05, "presence_penalty": 0.0, "repeat_penalty": 1.0, "temperature": 1.0, "top_k": 20, "top_p": 0.95} / 2048 |
| Cache / timing scope | Warm model; firstturn resets eachcase, laterturns retainprefix in one slot; OSfilecache uncontrolled, startup/warmupexcluded |
| Measurement batches | R442:one full18candidate; R441:independentfirst3screen; R443:timelyfreshcold3control. Not a newholdout or36independenttasks. |
| Actual template controls | See pinned native request evidence |
| Actual input-token range (if exported) | Not included in this public aggregate |
| Task count / repeats | 18 unique; one observed answer per task; no repeated-run uncertainty measured |
| Model SHA-256 | 3907dc1658db1f78a9826bf8d5bcb8dc65db0d466388937af57f2294fae62ec1 |
| Engine binary SHA-256 | 94c60d4646249fe067c75a56b15e6a8a9070a5e422cae16ee8dd9973389a6a27 |
| Template SHA-256 | See exact plan audit; not duplicated in public subset |
| Scorer adapter SHA-256 | See audit scoring contract |
| EvalPlus provenance SHA-256 | Not applicable / not duplicated |
| Plan SHA-256 | 1683005b2a201069d0d3de6e0984cdcd7fcf213463ea2f63914d7350bc8135f0 |

Original audit SHA-256 (originals retained privately; public excerpts are not the original files):

- [audit-a0726ce1921a21ae1360](audits/audit-a0726ce1921a21ae1360.md): `a0726ce1921a21ae13604536c04208d97a1d36cbe33230120b39b854d9f3f1ed`
- [audit-d0773e91e5e3773010d0](audits/audit-d0773e91e5e3773010d0.md): `d0773e91e5e3773010d094ed1af4ea578b34366a73fd19ee6bf345b275e70982`

### Qwen3.8 27B · GSQ/RCO IQ3_S · R261

Fast; MTP3. Additional policy failure inherited; coding-specialist screen, no general assistant qualification

| Condition | Audited value |
|---|---|
| Separate process-VRAM observation (not device peak) | NOT MEASURED |
| Hardware / power | Tesla V100-SXM2 16 GB HBM2 / 300 W |
| Engine | llama.cpp / CUDA 12.8 / SM70 (exact audited binary below) |
| Date | 2026-10-20 |
| Context, batching, KV, speculation | {"--batch-size": "2048", "--cache-type-k": "f16", "--cache-type-v": "f16", "--ctx-size": "8192", "--reasoning": "off", "--spec-draft-n-max": "3", "--spec-type": "draft-mtp", "--threads": "6", "--ubatch-size": "512", "retain_prefix": false} |
| Actual tuning / weight artifact / engine kernel | {"artifact_state": "MTP_BEARING_OR_GRAFTED_GGUF", "declared_profile": "provider_GSQ_RCO_IQ3S_MTP3_coding_specialist_screen", "draft_artifact": null, "draft_model_sha256": null, "engine_build_id": "dded13c80bc8e7d01a43ac6745d06bb22d7a15a3f5fba68729c536286e5066d4", "engine_source_commit": null, "environment_knobs": {"GGML_CUDA_GRAPH_OPT": "0"}, "executed_model_sha256": "58fd826723939933dc86f45b7fe04545cbc2de1c70f6fe2cdd3858c87a98c12f", "interpretation": "No-MTP inference does not imply a non-grafted weight file. GRAPH_OPT=0 does not imply CUDA Graphs disabled. An absent setting is unrecorded, never assumed off.", "kernel_library": "libggml-cuda.so.0.26.0", "kernel_library_sha256": "f76ecefe4dff5bb7bacf5721159b607f008d7f23b0fc848134637b6673b0e1f5", "runtime_flags": {"--batch-size": "2048", "--cache-reuse": "0", "--cache-type-k": "f16", "--cache-type-v": "f16", "--ctx-checkpoints": "2", "--ctx-size": "8192", "--flash-attn": "on", "--n-gpu-layers": "99", "--parallel": "1", "--reasoning": "off", "--spec-draft-n-max": "3", "--spec-draft-n-min": "1", "--spec-type": "draft-mtp", "--threads": "6", "--ubatch-size": "512"}, "weight_artifact": "Qwen3.8-27B-GSQ-RCO-IQ3_S-mtp.gguf"} |
| Tuning provenance | Pinned executed launch; executed launch SHA=9772400631819ce1ab70d1b9ff0b7a085c1917694242fcda629339623901c5a6 |
| Sampling / output cap | {"seed": 1001, "temperature": 0} / 1400 |
| Cache / timing scope | Warm model; per-request KV reset; OS file cache uncontrolled; model startup excluded |
| Measurement batches | Single suite or repeated cycles as stated |
| Actual template controls | See pinned native request evidence |
| Actual input-token range (if exported) | Not included in this public aggregate |
| Task count / repeats | 18 unique; one observed answer per task; no repeated-run uncertainty measured |
| Model SHA-256 | 58fd826723939933dc86f45b7fe04545cbc2de1c70f6fe2cdd3858c87a98c12f |
| Engine binary SHA-256 | 08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54 |
| Template SHA-256 | c3cf9e34abf4f9e36c2d72165aa9c132d3e2a725b6c2586aaa3a8af9d7a81041 |
| Scorer adapter SHA-256 | See audit scoring contract |
| EvalPlus provenance SHA-256 | Not applicable / not duplicated |
| Plan SHA-256 | c78e3a0d6960cf2c19c584789ec4ebcd6b1535ae3a38ce87b065061897d562d1 |

Original audit SHA-256 (originals retained privately; public excerpts are not the original files):

- [audit-87f6ea8a70d72917e748](audits/audit-87f6ea8a70d72917e748.md): `87f6ea8a70d72917e7486912fe5b5201c8e9b68d21d020ec6a698c3b54f3b43e`

### OmniCoder2 9B · Q6_K · R219

MTP + weight cache; 300 W. No additional policy claim is inferred from this discipline.

| Condition | Audited value |
|---|---|
| Separate process-VRAM observation (not device peak) | NOT MEASURED |
| Hardware / power | Tesla V100-SXM2 16 GB HBM2 / 300 W |
| Engine | llama.cpp / CUDA 12.8 / SM70 (exact audited binary below) |
| Date | 2026-10-20 |
| Context, batching, KV, speculation | {"--batch-size": "2048", "--cache-type-k": "f16", "--cache-type-v": "f16", "--ctx-size": "8192", "--reasoning": "off", "--spec-draft-n-max": "3", "--spec-type": "draft-mtp", "--threads": "6", "--ubatch-size": "512", "retain_prefix": false} |
| Actual tuning / weight artifact / engine kernel | {"artifact_state": "MTP_BEARING_OR_GRAFTED_GGUF", "declared_profile": null, "draft_artifact": null, "draft_model_sha256": null, "engine_build_id": "bbae889168127411ddd91d4576791ef20917e7a534d974d134347a33ea626499", "engine_source_commit": null, "environment_knobs": {"GGML_CUDA_GRAPH_OPT": "0", "GGML_CUDA_O2_WEIGHT_CACHE_MIB": "6144"}, "executed_model_sha256": "78af5105675a93f2909d625288a87be86ceef620985ab255f72dc028e0290e82", "interpretation": "No-MTP inference does not imply a non-grafted weight file. GRAPH_OPT=0 does not imply CUDA Graphs disabled. An absent setting is unrecorded, never assumed off.", "kernel_library": "libggml-cuda.so.0.26.0", "kernel_library_sha256": "b1596b98ba033d8a400d5ecaba5630168c5c5626b493ed2230ecb239c84a62ad", "runtime_flags": {"--batch-size": "2048", "--cache-reuse": "0", "--cache-type-k": "f16", "--cache-type-v": "f16", "--ctx-checkpoints": "2", "--ctx-size": "8192", "--flash-attn": "on", "--n-gpu-layers": "99", "--parallel": "1", "--reasoning": "off", "--spec-draft-n-max": "3", "--spec-draft-n-min": "1", "--spec-type": "draft-mtp", "--threads": "6", "--ubatch-size": "512"}, "weight_artifact": "OmniCoder-2-9B.Q6_K-MTP-grafted.gguf"} |
| Tuning provenance | Pinned executed launch; executed launch SHA=31e37154cfd129fd6a3033c62fdff0c266f4522c1939b4ce2f7c91c6a337476a |
| Sampling / output cap | {"seed": 1001, "temperature": 0} / 1400 |
| Cache / timing scope | Warm model; per-request KV reset; OS file cache uncontrolled; model startup excluded |
| Measurement batches | Single suite or repeated cycles as stated |
| Actual template controls | See pinned native request evidence |
| Actual input-token range (if exported) | Not included in this public aggregate |
| Task count / repeats | 18 unique; Observed min–max of three repeated 18-case cycle aggregates; not 54 independent tasks. |
| Model SHA-256 | 78af5105675a93f2909d625288a87be86ceef620985ab255f72dc028e0290e82 |
| Engine binary SHA-256 | 08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54 |
| Template SHA-256 | a4aee8afcf2e0711942cf848899be66016f8d14a889ff9ede07bca099c28f715 |
| Scorer adapter SHA-256 | See audit scoring contract |
| EvalPlus provenance SHA-256 | Not applicable / not duplicated |
| Plan SHA-256 | 096e2b2496adec4ad1feee8e69d3db0d18aaba5990cf61961a074266ad29c5c7 |

Original audit SHA-256 (originals retained privately; public excerpts are not the original files):

- [audit-7c91d45dc1aa187fe880](audits/audit-7c91d45dc1aa187fe880.md): `7c91d45dc1aa187fe8800d41cca25dc34e52b817b7f974e3c8bb16bd2d59cc2a`
- [audit-9a720eae0135df096db9](audits/audit-9a720eae0135df096db9.md): `9a720eae0135df096db9e1b28bed9134ef98bc6aa4bd656dbd9b5e0d7328ccb3`

### Ternary Bonsai 2 27B · PQ2_0 · R286

Thinking medium; 2048 output. No additional policy claim is inferred from this discipline.

| Condition | Audited value |
|---|---|
| Separate process-VRAM observation (not device peak) | NOT MEASURED |
| Hardware / power | Tesla V100-SXM2 16 GB HBM2 / 300 W |
| Engine | llama.cpp / CUDA 12.8 / SM70 (exact audited binary below) |
| Date | 2026-10-21 |
| Context, batching, KV, speculation | {"--batch-size": "2048", "--cache-type-k": "f16", "--cache-type-v": "f16", "--ctx-size": "8192", "--reasoning": "on", "--spec-type": "none", "--threads": "6", "--ubatch-size": "512", "retain_prefix": false} |
| Actual tuning / weight artifact / engine kernel | {"artifact_state": "SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED", "declared_profile": "published_medium_thinking_agent2048_localcap", "draft_artifact": null, "draft_model_sha256": null, "engine_build_id": "bonsai-pq2-sm70-9a9394a895b9", "engine_source_commit": null, "environment_knobs": {"GGML_CUDA_GRAPH_OPT": "0", "GGML_CUDA_O2_WEIGHT_CACHE_MIB": "0"}, "executed_model_sha256": "3907dc1658db1f78a9826bf8d5bcb8dc65db0d466388937af57f2294fae62ec1", "interpretation": "No-MTP inference does not imply a non-grafted weight file. GRAPH_OPT=0 does not imply CUDA Graphs disabled. An absent setting is unrecorded, never assumed off.", "kernel_library": "libggml-cuda.so.0.21.0", "kernel_library_sha256": "60c874aa652e9eb7d09ae128b79d31cbe0042f5e76476fd1d3192c47e7291d12", "runtime_flags": {"--batch-size": "2048", "--cache-reuse": "0", "--cache-type-k": "f16", "--cache-type-v": "f16", "--ctx-checkpoints": "2", "--ctx-size": "8192", "--flash-attn": "on", "--n-gpu-layers": "99", "--parallel": "1", "--reasoning": "on", "--spec-type": "none", "--threads": "6", "--ubatch-size": "512"}, "weight_artifact": "Ternary-Bonsai-2-27B-PQ2_0.gguf"} |
| Tuning provenance | Frozen plan; executed launch SHA=NOT RECORDED |
| Sampling / output cap | {"min_p": 0.05, "presence_penalty": 0.0, "repeat_penalty": 1.0, "temperature": 1.0, "top_k": 20, "top_p": 0.95} / 2048 |
| Cache / timing scope | Warm model; per-request KV reset; OS file cache uncontrolled; model startup excluded |
| Measurement batches | R285:16 + R286:2 disjoint agent cases; R284 failed before agent generation and is excluded |
| Actual template controls | See pinned native request evidence |
| Actual input-token range (if exported) | Not included in this public aggregate |
| Task count / repeats | 18 unique; one observed answer per task; no repeated-run uncertainty measured |
| Model SHA-256 | 3907dc1658db1f78a9826bf8d5bcb8dc65db0d466388937af57f2294fae62ec1 |
| Engine binary SHA-256 | 94c60d4646249fe067c75a56b15e6a8a9070a5e422cae16ee8dd9973389a6a27 |
| Template SHA-256 | See exact plan audit; not duplicated in public subset |
| Scorer adapter SHA-256 | See audit scoring contract |
| EvalPlus provenance SHA-256 | Not applicable / not duplicated |
| Plan SHA-256 | fb5cfb88f5b1a44a1f6cb6ee15aa02d0fbae7b6e83e61f507feca5a69f67fefb |

Original audit SHA-256 (originals retained privately; public excerpts are not the original files):

- [audit-355f55bd44c49fb08916](audits/audit-355f55bd44c49fb08916.md): `355f55bd44c49fb089167f11e666581db3bf3c188d499a6104c2d897d5be04af`
- [audit-c654b84d0dcad4ee1544](audits/audit-c654b84d0dcad4ee1544.md): `c654b84d0dcad4ee15440f026387212919515eb04b65b8dbf152f4f3efd33485`
- [audit-b1fc6b9a04856cba1af0](audits/audit-b1fc6b9a04856cba1af0.md): `b1fc6b9a04856cba1af0acf96a90c9ec3f7dfdd9c15e919f3b73b53cfaea52aa`

## Long inventory · 16K profiles

Twelve identical frozen long-inventory texts and typed native-call oracles; context16384, output256. Same requests/scoring with own native model templates/tokenizers and T0 versus T1 sampling. Original Omni16K partial R339 is excluded from full12 bars; Omni32K R338 remains a separate context/protocol evidence record. No full BFCL or agent claim.

Task identity: `c2218e9d5a2e2cef411698f637add2cf76465c6f0766ef22de16d8b5c4840a83`. **Task-matched whole-configuration comparisons**; native sampling, budgets and builds are shown below. These are development results, with no repeated-seed model-superiority claim. Record dates come from the original audit or frozen plan; missing dates remain labelled.

![Long inventory · 16K profiles: Successful tasks; missing results labelled NOT MEASURED](assets/benchmarks/long16k-success.svg){ .benchmark-svg }

![Long inventory · 16K profiles: Mean task E2E; missing results labelled NOT MEASURED](assets/benchmarks/long16k-latency.svg){ .benchmark-svg }

![Long inventory · 16K profiles: GPU energy per success; missing results labelled NOT MEASURED](assets/benchmarks/long16k-energy.svg){ .benchmark-svg }

![Long inventory · 16K profiles: Peak device VRAM; missing results labelled NOT MEASURED](assets/benchmarks/long16k-vram.svg){ .benchmark-svg }

| Profile / record date | Success | Successful tasks/s | Total task time / GPU energy | Peak VRAM | Audit |
|---|---|---|---|---|---|
| Gemma4 12B IT QAT Q4_0 — Native fast; T1; no MTP; 16K / 2026-10-22 | 12/12 | 0.09670 | 124.101 s / 33429.07 J | 8254.5 | [R429](experiments/R429.md) |
| Qwen3.8 27B GSQ/RCO IQ3_S — Native fast; T0; no MTP; 16K / 2026-10-22 | 12/12 | 0.04454 | 269.407 s / 73375.72 J | 12974.5 | [R432](experiments/R432.md) |

### Gemma4 12B IT QAT · Q4_0 · R429

Native fast; T1; no MTP; 16K. Separate agent-policy failures remain; this is read-only synthetic inventory retrieval, not agent or assistant qualification.

| Condition | Audited value |
|---|---|
| Separate process-VRAM observation (not device peak) | NOT MEASURED |
| Hardware / power | Tesla V100-SXM2 16 GB HBM2 / 300 W |
| Engine | llama.cpp / CUDA 12.8 / SM70 (exact audited binary below) |
| Date | 2026-10-22 |
| Context, batching, KV, speculation | {"--batch-size": "2048", "--cache-type-k": "f16", "--cache-type-v": "f16", "--ctx-size": "16384", "--reasoning": "off", "--spec-type": "none", "--threads": "6", "--ubatch-size": "512"} |
| Actual tuning / weight artifact / engine kernel | {"artifact_state": "SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED", "declared_profile": "official_QAT_fast_T1_P095_K64_ctx16K_native_functions256", "draft_artifact": null, "draft_model_sha256": null, "engine_build_id": "dded13c80bc8e7d01a43ac6745d06bb22d7a15a3f5fba68729c536286e5066d4", "engine_source_commit": null, "environment_knobs": {"GGML_CUDA_GRAPH_OPT": "0", "GGML_CUDA_O2_WEIGHT_CACHE_MIB": "0"}, "executed_model_sha256": "93567e57a8fe10b23569b9d9ec38cd005deedf71e29477c421a4b83f418a538b", "interpretation": "No-MTP inference does not imply a non-grafted weight file. GRAPH_OPT=0 does not imply CUDA Graphs disabled. An absent setting is unrecorded, never assumed off.", "kernel_library": "libggml-cuda.so.0.26.0", "kernel_library_sha256": "f76ecefe4dff5bb7bacf5721159b607f008d7f23b0fc848134637b6673b0e1f5", "runtime_flags": {"--batch-size": "2048", "--cache-reuse": "0", "--cache-type-k": "f16", "--cache-type-v": "f16", "--ctx-checkpoints": "2", "--ctx-size": "16384", "--flash-attn": "auto", "--n-gpu-layers": "99", "--parallel": "1", "--reasoning": "off", "--spec-type": "none", "--threads": "6", "--ubatch-size": "512"}, "weight_artifact": "gemma-4-12b-it-qat-q4_0.gguf"} |
| Tuning provenance | Pinned executed launch; executed launch SHA=a3cf8dbd61ec33d3acf8036eb0eecf3617856e72642061372d0e197eca83bc8b |
| Sampling / output cap | {"min_p": 0.0, "presence_penalty": 0.0, "repeat_penalty": 1.0, "seed": 1001, "temperature": 1.0, "top_k": 64, "top_p": 0.95} / 256 |
| Cache / timing scope | Warm model; per-request KV reset; OS file cache uncontrolled; model startup excluded |
| Measurement batches | Single suite or repeated cycles as stated |
| Actual template controls | {"enable_thinking": false} |
| Actual input-token range (if exported) | [14743, 14817] |
| Task count / repeats | 12 unique; one observed answer per task; no repeated-run uncertainty measured |
| Model SHA-256 | 93567e57a8fe10b23569b9d9ec38cd005deedf71e29477c421a4b83f418a538b |
| Engine binary SHA-256 | 08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54 |
| Template SHA-256 | ae53464bf3be25802b3a5b37def7fd89667067d7577049b3b2d74c4d8de4c6d4 |
| Scorer adapter SHA-256 | 719e912326059cd85d3c0915afd648c631fd2841fd4f5ba0baa5831c5cf2e807 |
| EvalPlus provenance SHA-256 | Not applicable / not duplicated |
| Plan SHA-256 | d817683964a08b892be642f76a2acc2018d3fd5492915cafe48ab66574d6e6f1 |

Original audit SHA-256 (originals retained privately; public excerpts are not the original files):

- [audit-13697d6c2db1e7cf8ca9](audits/audit-13697d6c2db1e7cf8ca9.md): `13697d6c2db1e7cf8ca9b8da7d086f1e2069d7a1d354b506ebc1abd92a1c5fcb`
- [audit-7b1ef9844e4319cdb9a5](audits/audit-7b1ef9844e4319cdb9a5.md): `7b1ef9844e4319cdb9a5e1f367a92e3646329a4d1094a884621fba8d1b9a9c00`

### Qwen3.8 27B · GSQ/RCO IQ3_S · R432

Native fast; T0; no MTP; 16K. Separate agent-policy failures remain; this is read-only synthetic inventory retrieval, not agent or assistant qualification.

| Condition | Audited value |
|---|---|
| Separate process-VRAM observation (not device peak) | NOT MEASURED |
| Hardware / power | Tesla V100-SXM2 16 GB HBM2 / 300 W |
| Engine | llama.cpp / CUDA 12.8 / SM70 (exact audited binary below) |
| Date | 2026-10-22 |
| Context, batching, KV, speculation | {"--batch-size": "2048", "--cache-type-k": "f16", "--cache-type-v": "f16", "--ctx-size": "16384", "--reasoning": "off", "--spec-type": "none", "--threads": "6", "--ubatch-size": "512"} |
| Actual tuning / weight artifact / engine kernel | {"artifact_state": "MTP_BEARING_OR_GRAFTED_GGUF", "declared_profile": "existing_GSQ_RCO_IQ3S_fast_T0_noMTP_ctx16K_native_functions256", "draft_artifact": null, "draft_model_sha256": null, "engine_build_id": "dded13c80bc8e7d01a43ac6745d06bb22d7a15a3f5fba68729c536286e5066d4", "engine_source_commit": null, "environment_knobs": {"GGML_CUDA_GRAPH_OPT": "0"}, "executed_model_sha256": "58fd826723939933dc86f45b7fe04545cbc2de1c70f6fe2cdd3858c87a98c12f", "interpretation": "No-MTP inference does not imply a non-grafted weight file. GRAPH_OPT=0 does not imply CUDA Graphs disabled. An absent setting is unrecorded, never assumed off.", "kernel_library": "libggml-cuda.so.0.26.0", "kernel_library_sha256": "f76ecefe4dff5bb7bacf5721159b607f008d7f23b0fc848134637b6673b0e1f5", "runtime_flags": {"--batch-size": "2048", "--cache-reuse": "0", "--cache-type-k": "f16", "--cache-type-v": "f16", "--ctx-checkpoints": "2", "--ctx-size": "16384", "--flash-attn": "on", "--n-gpu-layers": "99", "--parallel": "1", "--reasoning": "off", "--spec-type": "none", "--threads": "6", "--ubatch-size": "512"}, "weight_artifact": "Qwen3.8-27B-GSQ-RCO-IQ3_S-mtp.gguf"} |
| Tuning provenance | Pinned executed launch; executed launch SHA=966ae26f6cefb398e6ba06271c9f6cac198881b9031b5dbd94870e8f42447f62 |
| Sampling / output cap | {"seed": 1001, "temperature": 0.0} / 256 |
| Cache / timing scope | Warm model; per-request KV reset; OS file cache uncontrolled; model startup excluded |
| Measurement batches | Single suite or repeated cycles as stated |
| Actual template controls | {"enable_thinking": false} |
| Actual input-token range (if exported) | [14003, 14066] |
| Task count / repeats | 12 unique; one observed answer per task; no repeated-run uncertainty measured |
| Model SHA-256 | 58fd826723939933dc86f45b7fe04545cbc2de1c70f6fe2cdd3858c87a98c12f |
| Engine binary SHA-256 | 08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54 |
| Template SHA-256 | c3cf9e34abf4f9e36c2d72165aa9c132d3e2a725b6c2586aaa3a8af9d7a81041 |
| Scorer adapter SHA-256 | 719e912326059cd85d3c0915afd648c631fd2841fd4f5ba0baa5831c5cf2e807 |
| EvalPlus provenance SHA-256 | Not applicable / not duplicated |
| Plan SHA-256 | a08b57998f7de37c22b773f5b6168592d08190eb46e3087d6629ec2a49380635 |

Original audit SHA-256 (originals retained privately; public excerpts are not the original files):

- [audit-25a40c7b02bf60e588a1](audits/audit-25a40c7b02bf60e588a1.md): `25a40c7b02bf60e588a1ce906f5e567171fb9e5bbe23908407cdc430bff285ff`
- [audit-6612c4abb324bb5b83bb](audits/audit-6612c4abb324bb5b83bb.md): `6612c4abb324bb5b83bb99d699f4e9a86fdbe12cd2385013599195c719f90483`

## Long inventory · new 32K validation

Twelve identical subsequent local validation inventories frozen in R431 before Qwen screen outputs; context32768, output256, actualnative inputs above16384. Same texts/tools/oracles; own native tokenizers and T0 versus T1. Not a model-training holdout or population-accuracy claim. Partial runs remain on experiment pages and never become full12 scores.

Task identity: `d3848a79caceaef4ad202f0f6aa27d93558085e004006325ed83d471c7425d2a`. **Task-matched whole-configuration comparisons**; native sampling, budgets and builds are shown below. These are development results, with no repeated-seed model-superiority claim. Record dates come from the original audit or frozen plan; missing dates remain labelled.

![Long inventory · new 32K validation: Successful tasks; missing results labelled NOT MEASURED](assets/benchmarks/long32k_validation-success.svg){ .benchmark-svg }

![Long inventory · new 32K validation: Mean task E2E; missing results labelled NOT MEASURED](assets/benchmarks/long32k_validation-latency.svg){ .benchmark-svg }

![Long inventory · new 32K validation: GPU energy per success; missing results labelled NOT MEASURED](assets/benchmarks/long32k_validation-energy.svg){ .benchmark-svg }

![Long inventory · new 32K validation: Peak device VRAM; missing results labelled NOT MEASURED](assets/benchmarks/long32k_validation-vram.svg){ .benchmark-svg }

| Profile / record date | Success | Successful tasks/s | Total task time / GPU energy | Peak VRAM | Audit |
|---|---|---|---|---|---|
| Gemma4 12B IT QAT Q4_0 — Native fast; T1; no MTP; 32K / 2026-10-22 | 11/12 | 0.04133 | 266.136 s / 72487.35 J | 8526.5 | [R431](experiments/R431.md) |
| Qwen3.8 27B GSQ/RCO IQ3_S — Native fast; T0; no MTP; 32K / 2026-10-22 | 12/12 | 0.02189 | 548.199 s / 147942.94 J | 14010.5 | [R434](experiments/R434.md) |

### Gemma4 12B IT QAT · Q4_0 · R431

Native fast; T1; no MTP; 32K. Separate agent-policy failures remain; this is read-only synthetic inventory retrieval, not agent or assistant qualification.

| Condition | Audited value |
|---|---|
| Separate process-VRAM observation (not device peak) | NOT MEASURED |
| Hardware / power | Tesla V100-SXM2 16 GB HBM2 / 300 W |
| Engine | llama.cpp / CUDA 12.8 / SM70 (exact audited binary below) |
| Date | 2026-10-22 |
| Context, batching, KV, speculation | {"--batch-size": "2048", "--cache-type-k": "f16", "--cache-type-v": "f16", "--ctx-size": "32768", "--reasoning": "off", "--spec-type": "none", "--threads": "6", "--ubatch-size": "512"} |
| Actual tuning / weight artifact / engine kernel | {"artifact_state": "SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED", "declared_profile": "official_QAT_fast_T1_P095_K64_ctx32K_native_functions256", "draft_artifact": null, "draft_model_sha256": null, "engine_build_id": "dded13c80bc8e7d01a43ac6745d06bb22d7a15a3f5fba68729c536286e5066d4", "engine_source_commit": null, "environment_knobs": {"GGML_CUDA_GRAPH_OPT": "0", "GGML_CUDA_O2_WEIGHT_CACHE_MIB": "0"}, "executed_model_sha256": "93567e57a8fe10b23569b9d9ec38cd005deedf71e29477c421a4b83f418a538b", "interpretation": "No-MTP inference does not imply a non-grafted weight file. GRAPH_OPT=0 does not imply CUDA Graphs disabled. An absent setting is unrecorded, never assumed off.", "kernel_library": "libggml-cuda.so.0.26.0", "kernel_library_sha256": "f76ecefe4dff5bb7bacf5721159b607f008d7f23b0fc848134637b6673b0e1f5", "runtime_flags": {"--batch-size": "2048", "--cache-reuse": "0", "--cache-type-k": "f16", "--cache-type-v": "f16", "--ctx-checkpoints": "2", "--ctx-size": "32768", "--flash-attn": "auto", "--n-gpu-layers": "99", "--parallel": "1", "--reasoning": "off", "--spec-type": "none", "--threads": "6", "--ubatch-size": "512"}, "weight_artifact": "gemma-4-12b-it-qat-q4_0.gguf"} |
| Tuning provenance | Pinned executed launch; executed launch SHA=2be7fb9e0fdd740a6b628597934ed3e1f16f3bd11e6d9b6ba29aff790291a834 |
| Sampling / output cap | {"min_p": 0.0, "presence_penalty": 0.0, "repeat_penalty": 1.0, "seed": 1001, "temperature": 1.0, "top_k": 64, "top_p": 0.95} / 256 |
| Cache / timing scope | Warm model; per-request KV reset; OS file cache uncontrolled; model startup excluded |
| Measurement batches | Single suite or repeated cycles as stated |
| Actual template controls | {"enable_thinking": false} |
| Actual input-token range (if exported) | [29119, 29490] |
| Task count / repeats | 12 unique; one observed answer per task; no repeated-run uncertainty measured |
| Model SHA-256 | 93567e57a8fe10b23569b9d9ec38cd005deedf71e29477c421a4b83f418a538b |
| Engine binary SHA-256 | 08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54 |
| Template SHA-256 | ae53464bf3be25802b3a5b37def7fd89667067d7577049b3b2d74c4d8de4c6d4 |
| Scorer adapter SHA-256 | 719e912326059cd85d3c0915afd648c631fd2841fd4f5ba0baa5831c5cf2e807 |
| EvalPlus provenance SHA-256 | Not applicable / not duplicated |
| Plan SHA-256 | 1712592a47c05ef398bdf9acf30ee365b78fb402f952cc1c7283fac6014c6955 |

Original audit SHA-256 (originals retained privately; public excerpts are not the original files):

- [audit-cd8eb8e97cb00d82a151](audits/audit-cd8eb8e97cb00d82a151.md): `cd8eb8e97cb00d82a151afd35bd6e0d38cbd6e8eac1eadbaecebfa8baf450c80`
- [audit-57702f047eb73912c9f0](audits/audit-57702f047eb73912c9f0.md): `57702f047eb73912c9f0e0cb436535a0a757e711c5df86754bf0f30015097d4b`

### Qwen3.8 27B · GSQ/RCO IQ3_S · R434

Native fast; T0; no MTP; 32K. Separate agent-policy failures remain; this is read-only synthetic inventory retrieval, not agent or assistant qualification.

| Condition | Audited value |
|---|---|
| Separate process-VRAM observation (not device peak) | NOT MEASURED |
| Hardware / power | Tesla V100-SXM2 16 GB HBM2 / 300 W |
| Engine | llama.cpp / CUDA 12.8 / SM70 (exact audited binary below) |
| Date | 2026-10-22 |
| Context, batching, KV, speculation | {"--batch-size": "2048", "--cache-type-k": "f16", "--cache-type-v": "f16", "--ctx-size": "32768", "--reasoning": "off", "--spec-type": "none", "--threads": "6", "--ubatch-size": "512"} |
| Actual tuning / weight artifact / engine kernel | {"artifact_state": "MTP_BEARING_OR_GRAFTED_GGUF", "declared_profile": "existing_GSQ_RCO_IQ3S_fast_T0_noMTP_ctx32K_native_functions256", "draft_artifact": null, "draft_model_sha256": null, "engine_build_id": "dded13c80bc8e7d01a43ac6745d06bb22d7a15a3f5fba68729c536286e5066d4", "engine_source_commit": null, "environment_knobs": {"GGML_CUDA_GRAPH_OPT": "0"}, "executed_model_sha256": "58fd826723939933dc86f45b7fe04545cbc2de1c70f6fe2cdd3858c87a98c12f", "interpretation": "No-MTP inference does not imply a non-grafted weight file. GRAPH_OPT=0 does not imply CUDA Graphs disabled. An absent setting is unrecorded, never assumed off.", "kernel_library": "libggml-cuda.so.0.26.0", "kernel_library_sha256": "f76ecefe4dff5bb7bacf5721159b607f008d7f23b0fc848134637b6673b0e1f5", "runtime_flags": {"--batch-size": "2048", "--cache-reuse": "0", "--cache-type-k": "f16", "--cache-type-v": "f16", "--ctx-checkpoints": "2", "--ctx-size": "32768", "--flash-attn": "on", "--n-gpu-layers": "99", "--parallel": "1", "--reasoning": "off", "--spec-type": "none", "--threads": "6", "--ubatch-size": "512"}, "weight_artifact": "Qwen3.8-27B-GSQ-RCO-IQ3_S-mtp.gguf"} |
| Tuning provenance | Pinned executed launch; executed launch SHA=3c9647fe690b7bc9e5e1ca0c69a06e824fc78a4c3ad5cd303997419911752429 |
| Sampling / output cap | {"seed": 1001, "temperature": 0.0} / 256 |
| Cache / timing scope | Warm model; per-request KV reset; OS file cache uncontrolled; model startup excluded |
| Measurement batches | Single suite or repeated cycles as stated |
| Actual template controls | {"enable_thinking": false} |
| Actual input-token range (if exported) | [27415, 27777] |
| Task count / repeats | 12 unique; one observed answer per task; no repeated-run uncertainty measured |
| Model SHA-256 | 58fd826723939933dc86f45b7fe04545cbc2de1c70f6fe2cdd3858c87a98c12f |
| Engine binary SHA-256 | 08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54 |
| Template SHA-256 | c3cf9e34abf4f9e36c2d72165aa9c132d3e2a725b6c2586aaa3a8af9d7a81041 |
| Scorer adapter SHA-256 | 719e912326059cd85d3c0915afd648c631fd2841fd4f5ba0baa5831c5cf2e807 |
| EvalPlus provenance SHA-256 | Not applicable / not duplicated |
| Plan SHA-256 | 619156ecdd8a3ac287376ff4e6d661c8afef89e9244157cc66726bc7c4e5a9ab |

Original audit SHA-256 (originals retained privately; public excerpts are not the original files):

- [audit-d8e1609bb2632a6b88cf](audits/audit-d8e1609bb2632a6b88cf.md): `d8e1609bb2632a6b88cfd55c530a935c3916a66913cdcb4dcc8b8bc2ba485cd9`
- [audit-dfffa11e6009d9343cf0](audits/audit-dfffa11e6009d9343cf0.md): `dfffa11e6009d9343cf0186cdb40df485da2c22f2f043bc52cbbb99bb4a96777`

## Historical synthetic performance — separate protocol

These imported A0 records use historical model/build identities and synthetic native workloads. They are separate from task-success comparisons above. Token/s across tokenizers is a workload measurement, not useful-task superiority. **Bars: stored median; whiskers: median ± measured MAD; labels: MAD and sample size.** There are no invented confidence intervals.

![Historical native Prefill · ~512 tokens: median, MAD and sample size](assets/benchmarks/historical-prefill.svg){ .benchmark-svg }

![Historical native Prefill · ~2K tokens: median, MAD and sample size](assets/benchmarks/historical-prefill2048.svg){ .benchmark-svg }

![Historical native Prefill · ~4K tokens: median, MAD and sample size](assets/benchmarks/historical-prefill4096.svg){ .benchmark-svg }

![Historical native Decode · 128 tokens: median, MAD and sample size](assets/benchmarks/historical-decode.svg){ .benchmark-svg }

### Historical OmniCoder2 9B · Q6_K

| Field | Original reference identity |
|---|---|
| Hardware | Tesla V100-SXM2 16 GB HBM2 |
| Date | NOT RECORDED in imported reference identity; audited in R135 |
| Power limit | NOT RECORDED; do not assume current 300 W |
| Model SHA-256 | b0c1664c86338be24090a45d8b86bd106ba755d004f8746d99ee5ad69258fc3b |
| Engine binary identity | ["71199b6d5fdcde4c27ea83a0bf278fdb2d432ad43fe51411b564c6354e9bb8bd"] |
| Runtime | {"batch_size": 2048, "cache_prompt": false, "ctx": 8192, "decode_ignore_eos": true, "decode_output": 128, "prefill_output": 1, "seed": 1001, "slots": 1, "temperature": 0, "thinking": false, "threads": 6, "tool_max_tokens": 128, "ubatch_size": 512} |
| Reference | e0a5d6c242421e9fd9fedd7f4796c7c0cb5154434fe3908a9053e3b9250da661 |
| Audit SHA-256 | 944476f62657e032732177de16aaaf2fad25362a09532004a73e6ba4a928edc4 |

| Workload | Prompt token count(s) | Generated token count(s) | n / sessions |
|---|---|---|---|
| prefill | [505] | [1] | 6 / 2 |
| prefill2048 | [2048] | [1] | 6 / 2 |
| prefill4096 | [4096] | [1] | 6 / 2 |
| decode | [31] | [128] | 6 / 2 |


[Original audit excerpt](audits/audit-944476f62657e0327321.md). Different tokenizers and historical model/build identities. Not a current task-success ranking; no cross-tokenizer quality or useful-throughput inference.

### Historical Qwen3.5 9B · Q4_K_M

| Field | Original reference identity |
|---|---|
| Hardware | Tesla V100-SXM2 16 GB HBM2 |
| Date | NOT RECORDED in imported reference identity; audited in R135 |
| Power limit | NOT RECORDED; do not assume current 300 W |
| Model SHA-256 | 02d45dc1cf451ba2475ac33b301c2dd8f985abe4c182ce04a1f2f5bf0260278d |
| Engine binary identity | ["71199b6d5fdcde4c27ea83a0bf278fdb2d432ad43fe51411b564c6354e9bb8bd"] |
| Runtime | {"batch_size": 2048, "cache_prompt": false, "ctx": 8192, "decode_ignore_eos": true, "decode_output": 128, "prefill_output": 1, "seed": 1001, "slots": 1, "temperature": 0, "thinking": false, "threads": 6, "tool_max_tokens": 128, "ubatch_size": 512} |
| Reference | 8d659da13e52a886c39537beefbeee5aee65931bd6ddc9a53faa05fe434c891f |
| Audit SHA-256 | 944476f62657e032732177de16aaaf2fad25362a09532004a73e6ba4a928edc4 |

| Workload | Prompt token count(s) | Generated token count(s) | n / sessions |
|---|---|---|---|
| prefill | [505] | [1] | 6 / 2 |
| prefill2048 | [2048] | [1] | 6 / 2 |
| prefill4096 | [4096] | [1] | 6 / 2 |
| decode | [31] | [128] | 6 / 2 |


[Original audit excerpt](audits/audit-944476f62657e0327321.md). Different tokenizers and historical model/build identities. Not a current task-success ranking; no cross-tokenizer quality or useful-throughput inference.

### Historical Qwen3.8 27B · GSQ/RCO IQ3_S

| Field | Original reference identity |
|---|---|
| Hardware | Tesla V100-SXM2 16 GB HBM2 |
| Date | NOT RECORDED in imported reference identity; audited in R135 |
| Power limit | NOT RECORDED; do not assume current 300 W |
| Model SHA-256 | 64b53b64c7aa39f20a7e54bd80582fe595b1d745624ee8a72e92508c0326d810 |
| Engine binary identity | ["71199b6d5fdcde4c27ea83a0bf278fdb2d432ad43fe51411b564c6354e9bb8bd"] |
| Runtime | {"batch_size": 2048, "cache_prompt": false, "ctx": 8192, "decode_ignore_eos": true, "decode_output": 128, "prefill_output": 1, "seed": 1001, "slots": 1, "temperature": 0, "thinking": false, "threads": 6, "tool_max_tokens": 128, "ubatch_size": 512} |
| Reference | 649420efeb0212271674362d3bb3b20bf268a46f5fc40ece74359d7f6ca572fb |
| Audit SHA-256 | 944476f62657e032732177de16aaaf2fad25362a09532004a73e6ba4a928edc4 |

| Workload | Prompt token count(s) | Generated token count(s) | n / sessions |
|---|---|---|---|
| prefill | [505] | [1] | 6 / 2 |
| prefill2048 | [2048] | [1] | 6 / 2 |
| prefill4096 | [4096] | [1] | 6 / 2 |
| decode | [31] | [128] | 6 / 2 |


[Original audit excerpt](audits/audit-944476f62657e0327321.md). Different tokenizers and historical model/build identities. Not a current task-success ranking; no cross-tokenizer quality or useful-throughput inference.

## Scientific metadata correction

The Bonsai agent campaign uses **2048 output tokens per turn**, from executed [R285](experiments/R285.md) and [R286](experiments/R286.md). Earlier chart metadata selected the failed pre-generation [R284](experiments/R284.md) plan and displayed 4096. The success counts, measured costs and immutable original audits are unchanged; coding/native-tool budgets remain separate. The R219 model artifact field now follows the pinned executed model path/identity instead of an inherited top-level plan hash: the executed artifact is the integrated MTP graft, not the original target GGUF. Runtime settings and original measurements are unchanged; no reference is silently rewritten.

