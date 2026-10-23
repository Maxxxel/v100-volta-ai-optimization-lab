# OmniCoder V1 / V2: CPU weight integrity

This artifact review adds **zero GPU experiments, model requests or benchmark scores**. All historical configuration IDs, scores, qualifications and negative findings remain unchanged.

## Decision

**Different dequantized GGUF representations are proven. Underlying checkpoint / new fine-tuning: NOT UNAMBIGUOUSLY DETERMINABLE.** This is the requested three-way verdict at the source-weight level. Different file hashes or reconstruction grids do not prove a new trained checkpoint.

| Measured scope | Value |
| --- | --- |
| Date (UTC) | 2026-10-23T16:53:59.269311+00:00 |
| Matched tensors | 427 |
| Compared weight values | 8953803264 |
| Changed tensors | 248 |
| Numerically identical tensors | 179 |
| Exactly different reconstructed values | 5637941302 |
| Global RMSE | 0.00020962777077129858 |
| Relative L2 against V1 | 0.013860729616140833 |
| Maximum absolute difference | 0.041259765625 |
| CPU comparison elapsed seconds | 258.00507805205416 |

Both files contain 427 shape-matched tensors. Shared F32 equality and other metadata agreement are reported explicitly below; these are observations, not proof of identical remaining unquantized source weights.

| Observed identity check | Measured result |
| --- | --- |
| Identical quantized tensors | output.weight, token_embd.weight |
| Architecture metadata agreement | True |
| Tokenizer / template metadata agreement | True |

## Exact artifact identities

| Artifact | Bytes | SHA256 | Pinned quantizer source |
| --- | --- | --- | --- |
| Tesslate_OmniCoder-9B-Q6_K.gguf | 7700259936 | `a73cc3136da753063e667edef95bec3bbf47829e34a2a31bf0f5a29c970f9052` | [bartowski/Tesslate_OmniCoder-9B-GGUF](https://huggingface.co/bartowski/Tesslate_OmniCoder-9B-GGUF/tree/f0fbc2243f49ab2dbdf91fe5930dd73e6bce767c) |
| OmniCoder-2-9B.Q6_K.gguf | 7359259904 | `b0c1664c86338be24090a45d8b86bd106ba755d004f8746d99ee5ad69258fc3b` | [mradermacher/OmniCoder-2-9B-GGUF](https://huggingface.co/mradermacher/OmniCoder-2-9B-GGUF/tree/bd26f7e9e5012cb18e3934e505d76a01028ebbdc) |

## Precision policy is different despite the Q6_K labels

| V1 / V2 storage | Tensors | Weight values | Changed tensors | Changed values | RMSE | Max abs |
| --- | --- | --- | --- | --- | --- | --- |
| F32 / F32 | 177 | 1061376 | 0 | 0 | 0.0 | 0.0 |
| F32 / Q6_K | 48 | 6291456 | 48 | 6267364 | 0.00032476172259403367 | 0.005767822265625 |
| Q6_K / Q6_K | 142 | 7621050368 | 140 | 4317870769 | 0.00018191985262574017 | 0.041259765625 |
| Q8_0 / Q6_K | 60 | 1325400064 | 60 | 1313803169 | 0.00032568161043735315 | 0.01784992218017578 |

Actual V1 storage counts: `{"F32": 225, "Q6_K": 142, "Q8_0": 60}`. Actual V2 counts: `{"F32": 177, "Q6_K": 250}`. A same-precision Q6_K pair can still use different quantizer versions or calibration. A changed decoded value is not by itself a trained-weight delta.

No matched unquantized source pair or independently calibrated quantizer error controls are available. Differences of decoded quantized values alone do not establish a new fine-tune or a difference beyond source quantization/conversion effects. Reported per-tensor exact differences/RMSE are measurements, not a training-delta significance test.

## Source provenance and reported faulty release

| Question | Finding |
| --- | --- |
| V1_quantizer | Publisher specifies llama.cpp b8292 and importance-matrix quantization. The GGUF itself records248 imatrix entries and802 calibration chunks. |
| V2_quantizer | Publisher labels static quants and links separately to imatrix variants. The retained file has250 Q6_K and177 F32 tensors. Its conversion/build/calibration inputs are not independently reconstructed. Missing imatrix metadata alone is not proof no imatrix was used. |
| V2_upstream_lineage | The retained V2 GGUF SHA256 matches the pinned quantizer LFS object. Its declared source is Tesslate/OmniCoder-2-9B, but an exact upstream conversion revision or verified unquantized source identity is unavailable. The GGUF declares a quantization timestamp of2026-03-25T10:47:42+01:00; this is metadata, not an independently verified release chronology. |
| cached_source_object_observation | `{"bytes": 18819722360, "classification": "EXTERNALLY_REPORTED_LFS_OBJECT_IDENTITY_NOT_LOCAL_SOURCE_TENSOR_CENSUS", "limit": "Previously cached public HF metadata reports one identical complete safetensors object for V1 upstream and the disputed OxCoder source. Neither full source file was downloaded or independently hashed here. This does not establish V2 lineage, a corrected checkpoint, training history or publisher intent. OxCoder inspection remains stopped by user request.", "repositories": ["Tesslate/OmniCoder-9B", "OrionLLM/OxCoder-9B"], "revisions": ["9edd36a30fc7b95b6fd81b7ea16a73cbaf205734", "07ba04e2149bace1b43c66448471a70378a7a708"], "safetensors_lfs_sha256": "d4fca6821fe35b46e684ab88217ec25cdbfcdf9fa208c01110be95a200fcc33b"}` |
| reported_faulty_release_relationship | NOT VERIFIED. No exact V2 upstream revision or corrected-versus-original source payload binding is established. Neither two different GGUF hashes nor their quantized numerical differences establish the claimed fine-tune or resolve a reported faulty initial release. The historical benchmark still measures the exact retained artifact. |

The cached upstream LFS observation is explicitly **external metadata**, not a completed independent source-tensor comparison. No new OxCoder investigation was resumed. Establishing whether V2 came from an originally faulty or corrected release requires an exact upstream conversion revision plus trustworthy original/corrected source payloads. Those prerequisites are absent.

## Method and limits

Inputs were opened read-only, then all parsing and numerical work ran as UID65534 with GPU devices hidden, one CPU thread and a 768 MiB service limit. Both full-file SHA256 values were verified before comparison; inode, size and modification time were rechecked afterward. All comparable tensors were decoded completely in bounded chunks; no tensor sampling substitutes for the full comparison. Native C and NumPy implementations were cross-checked on the first/last chunk of every tensor, plus zero/nonzero/signed and deliberately changed controls. This is two CPU implementations from the reviewed engine tooling, not an independent unquantized training oracle. Float32 reconstructed values are compared exactly; differences use float64 accumulation. No model inference or task-quality claim follows from this audit.

The missing quantization-noise control is a matched unquantized source pair, or controlled re-quantizations of a known common source with pinned conversion/calibration recipes. Without it, no significance threshold is invented. The original main V2 artifact remains the reproducible identity of its historical benchmark results.

[All per-tensor measurements](artifact-reviews/omnicoder-tensors.md). [Public numerical dataset](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/blob/main/data/benchmark-register.json) (`artifact_weight_reviews`): counts, metrics and tensor payload hashes only; no weight values or model files.

## Preserved and removed artifacts

15 other OmniCoder2 GGUF variants were removed at the user’s explicit request, freeing89099358208 allocated bytes. The main Q6_K file and its alias remain. Historical audits/hashes and scientific qualification are preserved. Removed variants, including the grafted MTP artifact, need re-fetch or reconstruction before replay; historical qualification does not imply current local artifact availability.

| Removed artifact |
| --- |
| OmniCoder-2-9B.IQ4_XS.gguf |
| OmniCoder-2-9B.Q2_K.gguf |
| OmniCoder-2-9B.Q3_K_M.gguf |
| OmniCoder-2-9B.Q4K-Q05-CAL4-512M.gguf |
| OmniCoder-2-9B.Q4_K_M-Q02-CAL4-fromQ8.gguf |
| OmniCoder-2-9B.Q4_K_M.gguf |
| OmniCoder-2-9B.Q5_K_M.gguf |
| OmniCoder-2-9B.Q5_K_S.gguf |
| OmniCoder-2-9B.Q6_K-MTP-grafted.gguf |
| OmniCoder-2-9B.Q6_K-Q03-attention-Q8_0.gguf |
| OmniCoder-2-9B.Q6_K.H08-private-copy.gguf |
| OmniCoder-2-9B.Q8_0.gguf |
| OmniCoder-2-9B.i1-IQ2_XS.gguf |
| OmniCoder-2-9B.i1-IQ3_S.gguf |
| OmniCoder-2-9B.i1-Q4_K_M.gguf |

## Evidence

[audit-f020a7c2e0c3ef2c527e](audits/audit-f020a7c2e0c3ef2c527e.md), [audit-6a15be92f408e91f019a](audits/audit-6a15be92f408e91f019a.md), [audit-b8bb370f8cb74784bd95](audits/audit-b8bb370f8cb74784bd95.md), [audit-7baaaf5407cf58fc4e46](audits/audit-7baaaf5407cf58fc4e46.md)

| Source | Pinned SHA256 | Original reference |
| --- | --- | --- |
| V1 quantizer metadata | `bb0f9edf12c59d6f52676330122d61989cf894f7f6fde1771d73b6867c5d8183` | [Source](https://huggingface.co/bartowski/Tesslate_OmniCoder-9B-GGUF/tree/f0fbc2243f49ab2dbdf91fe5930dd73e6bce767c) |
| V1 quantization recipe | `2045dda120295de0d4d4d9760a0b3a455b46701f0d92b85885edc25248690e01` | [Source](https://huggingface.co/bartowski/Tesslate_OmniCoder-9B-GGUF/blob/f0fbc2243f49ab2dbdf91fe5930dd73e6bce767c/README.md) |
| V1 published upstream metadata | `ff65927e92d19172fd2ac959b01262731fc12ce2991170b9bcd54005bc8b66b8` | [Source](https://huggingface.co/Tesslate/OmniCoder-9B/tree/9edd36a30fc7b95b6fd81b7ea16a73cbaf205734) |
| V2 quantizer metadata | `5c8ec952a987800e3cdf08b03469df59b20fa5b702d9168cf121bd8089a0db64` | [Source](https://huggingface.co/mradermacher/OmniCoder-2-9B-GGUF/tree/bd26f7e9e5012cb18e3934e505d76a01028ebbdc) |
| V2 quantization recipe | `7fde0b3c62f38591dee93d94b335ff610d59c25fcf4218381c43c25f36185006` | [Source](https://huggingface.co/mradermacher/OmniCoder-2-9B-GGUF/blob/bd26f7e9e5012cb18e3934e505d76a01028ebbdc/README.md) |
| Previously cached OxCoder metadata; no resumed investigation | `6e29b7efcbfb148d24f6e2b824c962d37915b653b3527f1130394c64bf5b591d` | [Source](https://huggingface.co/OrionLLM/OxCoder-9B/tree/07ba04e2149bace1b43c66448471a70378a7a708) |

Original numerical audit SHA256: `f020a7c2e0c3ef2c527e1884c59283a96942620769e1fee304b18024620c5bc4`. Original tensor journal SHA256: `6370686a7d3bb23e14bacdd2711ec27859a8b7ba290d5901ecc4098d5c830d94`. Source plan SHA256: `6a15be92f408e91f019aec853d5552035f65a1c227c9a55cbaf022b6a1c22813`. Decision SHA256: `b8bb370f8cb74784bd95edec916c59b5a33faf803aa04a78b4e19a768400d760`.

**LOCALLY MEASURED:** full artifact identities, tensor layouts and all matched dequantized comparisons. **EXTERNALLY EVIDENCED:** publisher recipes, repository revisions and LFS metadata. **NOT VERIFIED:** a distinct fine-tune, differences beyond controlled quantization noise, exact V2 upstream conversion lineage or a corrected initial release.

