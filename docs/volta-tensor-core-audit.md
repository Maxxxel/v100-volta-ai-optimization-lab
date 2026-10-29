# Volta Tensor-Core path audit

**Read-only evidence review · 29 October 2026 · no GPU run started.** This audit separates observed kernel dispatch from actual Tensor-Core utilization.

## What the existing traces show

An existing OmniCoder2 Q6_K trace used 99 GPU layers and the frozen model artifact SHA256 `b0c1664c86338be24090a45d8b86bd106ba755d004f8746d99ee5ad69258fc3b`. The recorded llama-server binary SHA256 was `71199b6d5fdcde4c27ea83a0bf278fdb2d432ad43fe51411b564c6354e9bb8bd`.

| Existing trace | Captured CUDA kernel events | Observed path | Interpretation |
|---|---:|---|---|
| Prefill | 2,468 | 50.22% of summed kernel time classified as GEMM. Named Volta FP16 tensor-op kernels include 150 `cutlass_70_tensorop_s884gemm_f16_128x128_tn_align8` launches (64.687 ms; 37.31%), plus Volta `s884gemm_fp16` variants. | Volta Tensor-Core-capable GEMM dispatch is present in this prefill trace. |
| Decode | 119,014 | Quantized matrix-vector kernels account for 77.82% of summed kernel time. The two leading `mul_mat_vec_q` variants account for 46.70% and 30.44%. | Decode is dominated by quantized matrix-vector dispatch in this trace; no named Volta tensor-op GEMM kernel appears among its 34 kernel classes. |

These are event counts and durations from the existing C6B trace analysis, not a new benchmark. The trace warns that not all CUDA events may have been collected; its release gate is false. It is useful for identifying observed dispatch, not for ranking performance or estimating utilization.

## R81 and hardware telemetry

R81’s existing ABBA comparison found no practical speed gain for the `NO_VOLTA_PERM` variant: measured decode-throughput delta was about +0.063%, with prefill and E2E changes below 1%. Its independent numerical qualification was incomplete, so it was not promoted.

The archived 162-row telemetry has median GPU utilization 94%, median SM clock 1,530 MHz, memory clock 877 MHz, median board power 269.51 W, maximum 291.19 W, maximum temperature 63 °C and no uncorrected ECC increase. These samples aggregate all arms and include idle observations. They do not record per-kernel Tensor-Core activity, DRAM bytes/bandwidth, stall reasons, or power/thermal throttle reasons; therefore they cannot identify a compute, HBM, or power bottleneck.

## Measurement boundary

Nsight Compute 2022.4.1 is present, but its read-only metric query returned `ERR_NVGPUCTRPERM`. No permissions or driver settings were changed. Existing Nsight Systems traces contain no Tensor-Core hardware counters. Therefore:

- **Observed:** Volta tensor-op GEMM kernels execute in the captured OmniCoder2 prefill; the captured decode kernel time is mainly quantized matrix-vector work.
- **Not measured:** Tensor-Core active-cycle/utilization rate, SM/HBM roofline position, memory transactions, kernel stalls, or per-kernel clock and throttle state.
- **Decision:** `PATH_OBSERVED; THROUGHPUT_DIAGNOSIS_PARTIAL`. Do not infer Tensor-Core underuse or claim an optimization opportunity from dispatch names alone.

A deeper diagnosis requires a valid admitted profiler experiment with counter access and matched kernel-level telemetry. The existing evidence does not justify changing GPU permissions or repeating R81.

## Provenance

- Existing trace-analysis SHA256: `9f57086039efa3435c588490b11838323e662cb04caa88f259fc680a154e67aa`
- Existing OmniCoder2 decode trace SHA256: `abb53640adbea356331fdb4122ebfe9cf815d3449ab16143737a25b9ea4b49ae`
- Existing OmniCoder2 prefill trace SHA256: `e0fefed80ae1861598d05098d9b5b4217f1dd9e6ce898b2682817a85470b9671`
- [R81 original audit excerpt](experiments/R81.md)
