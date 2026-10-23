# OmniCoder V1 / V2: same-quantizer weight comparison

This follow-up uses mradermacher Q6_K for both versions. The [earlier bartowski/mradermacher comparison](weight-integrity.md) remains a separate measured result. **No GPU jobs, model inference, benchmark score changes or edits to original main weights.**

## Verdict

**Identical model weights proven — for every stored tensor in these two exact GGUF files.** All tensor names, shapes, GGML types and payload bytes match. Deterministic dequantization therefore produces the same numerical values for every tensor. This is stronger than matching file sizes or sampled tensor checks.

This does not prove the identity or training history of every unquantized upstream checkpoint. It does not establish whether an original upstream publication was faulty or subsequently corrected. It directly establishes what is stored in the retained deployed artifacts.

| Measured scope | Value |
| --- | --- |
| Review recorded (UTC) | 2026-10-23T17:16:48.493005+00:00 |
| Compared tensors | 427 |
| Compared weight values | 8953803264 |
| Compared tensor payload bytes | 7348291584 |
| Byte-identical tensor payloads | 427 |
| Different tensor payloads | 0 |
| Elapsed download + CPU comparison s | 205.37342375493608 |
| New GPU runs | 0 |

## Exact files and source revisions

| Version | File | Bytes | Locally verified SHA256 | Pinned quantizer repository |
| --- | --- | --- | --- | --- |
| V1 | OmniCoder-9B.Q6_K.gguf | 7359259904 | `7a2c7ae3d465979c696ae191e8d398d86c031c5b09e8e86af4a994850b1d9889` | [mradermacher/OmniCoder-9B-GGUF](https://huggingface.co/mradermacher/OmniCoder-9B-GGUF/tree/34839038227e9837d7e9d78a91c1b509e8a217b9) |
| V2 | OmniCoder-2-9B.Q6_K.gguf | 7359259904 | `b0c1664c86338be24090a45d8b86bd106ba755d004f8746d99ee5ad69258fc3b` | [mradermacher/OmniCoder-2-9B-GGUF](https://huggingface.co/mradermacher/OmniCoder-2-9B-GGUF/tree/bd26f7e9e5012cb18e3934e505d76a01028ebbdc) |

Different complete-file hashes are **not** a weight-difference proof. Full-file hashes were independently verified locally for both files; the entire tensor payload of each was then checked. Storage counts for each file: `{"F32": 177, "Q6_K": 250}`. Same publisher or Q6_K label alone would not establish equal recipes. Here, actual tensor formats and complete payloads provide the evidence.

## Recorded metadata differences

| Field | V1 | V2 |
| --- | --- | --- |
| general.basename | OmniCoder | OmniCoder-2 |
| general.name | OmniCoder 9B | OmniCoder 2 9B |
| general.source.url | https://huggingface.co/Tesslate/OmniCoder-9B | https://huggingface.co/Tesslate/OmniCoder-2-9B |
| general.url | https://huggingface.co/mradermacher/OmniCoder-9B-GGUF | https://huggingface.co/mradermacher/OmniCoder-2-9B-GGUF |
| mradermacher.quantized_at | 2026-03-13T09:07:48+01:00 | 2026-03-25T10:47:42+01:00 |

The bounded header comparison found the listed metadata differences; all other parsed metadata agree, including tokenizer arrays, template and architecture. Quantization dates above are file metadata, not an independently established release chronology.

## Method

First inspect pinned publisher LFS hashes without downloading weight files. Because those hashes differ, inspect a bounded V1 header and compare it with the previously fully verified main V2. All tensor descriptors agree. Then download only the necessary single V1 Q6_K file, verify its complete SHA256, fully rehash the read-only local main V2, and compare **every byte of every tensor** in bounded chunks. Each tensor has separate SHA256 identities and an actual byte-equality result. The existing reviewed GGUF parser is reused to recheck both complete files. Network access, parsing and comparison run unprivileged as UID65534 with GPU devices hidden; the service survives terminal disconnection. Main V2 inode, size and modification time remain unchanged.

Every matched tensor has identical GGML type, shape and byte payload. Deterministic dequantization therefore yields identical reconstructed values for all tensors; another full dequantization would add no information.

No repeated full dequantization or GPU benchmark is needed to prove decoded equality when the type, dimensions and every payload byte already match. This proof concerns quantized stored weights; it is not an inference-performance or model-training claim.

## Relation to the earlier result

The earlier result compared different quantizer implementations and per-tensor precision policies. Its measured reconstruction differences remain valid. This same-quantizer follow-up addresses that confound directly and does not rewrite the earlier audit. Historical benchmark results continue to identify the exact artifact and runtime tested; no score is copied into a new model row, and no fine-tuning advantage is inferred from a version label.

## Canonical name and duplicate removal

The retained original main file is now named `OmniCoder-9B.Q6_K.gguf`. Its original inode, full SHA256, modification time and internal GGUF metadata remain intact. Old paths remain compatibility symlinks; frozen references and historical audit identities are preserved. The newly downloaded mradermacher V1 regular-file copy was removed after comparison; its short filename now links to the retained main artifact. This frees 7359266816 allocated bytes. The earlier bartowski comparison artifact was not part of this deletion.

For the exact checked main hash, the presentation name is **OmniCoder 9B (V1/V2 weight-equivalent Q6_K)**. Original historical model labels remain accessible and are not rewritten inside immutable profiles or runs. Other quantizations and grafted artifacts are not automatically renamed or declared tensor-identical.

[Complete per-tensor equality table](artifact-reviews/omnicoder-same-quantizer-tensors.md). Full payload hashes are in the [public benchmark register](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/blob/main/data/benchmark-register.json), under `same_quantizer_weight_reviews`. No model values or weights are redistributed.

## Audit identities

[audit-36c5628322e65e0bca66](audits/audit-36c5628322e65e0bca66.md), [audit-c781081055b2edb51609](audits/audit-c781081055b2edb51609.md), [audit-73e6dff02c234be9effe](audits/audit-73e6dff02c234be9effe.md), [audit-7d0f5b394f8250c59398](audits/audit-7d0f5b394f8250c59398.md), [audit-cda68ec3ecfd3ec441a6](audits/audit-cda68ec3ecfd3ec441a6.md)

| Evidence | Original SHA256 |
| --- | --- |
| audit | `36c5628322e65e0bca66a33126b217681e6122c4f14d35d237879ff4a8f5117b` |
| header | `c781081055b2edb51609d3253a3f4cf7e98b2c461069e9e1c087c18937ae7e47` |
| tensor_results | `bc235d0ad27316be11ffca3c643a5c198d51aa1c48815f4cc8bbcd6868fcedb5` |
| plan | `73e6dff02c234be9effec9c3a71af4c529cb5dcd172e469008eae9d6a8b18220` |
| verification | `7d0f5b394f8250c59398bc9fe84e5be15d52c970a821b6fda45601c91376fd52` |
| rename | `cda68ec3ecfd3ec441a670db211a42e13f568b74e057c54b1dfaa13b5ea34377` |

**LOCALLY MEASURED:** complete file hashes, all tensor layouts and every tensor payload. **EXTERNALLY EVIDENCED:** publisher repository identities and LFS metadata. **NOT VERIFIED:** unquantized training lineage, publisher intent, a repaired upstream release or new V1 task-performance measurements.

