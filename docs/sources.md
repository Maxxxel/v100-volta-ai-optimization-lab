# Research papers & sources

Original sources are cited rather than republished. Source revisions refer to the reviewed snapshot, not an assertion that upstream is unchanged. Secondary/community claims are discovery leads rather than local causal evidence.


## VOLTA_GUIDE

```json
{
  "axes": [
    "C09",
    "C10",
    "C11",
    "C14",
    "HBM01",
    "HBM02",
    "HBM03",
    "HBM04",
    "HBM05",
    "HBM06",
    "HBM07"
  ],
  "classification": "PARTIALLY_COVERED",
  "evidence_class": "EXTERN_BELEGT",
  "id": "VOLTA_GUIDE",
  "local_test_status": "NO_NEW_GPU_TEST",
  "obstacles": [],
  "revision": "v13.4;updated2026-10-12;archivedSHA",
  "scope": "Scheduling, occupancy, memory reuse and explicit warp synchronization checked. Hardware basis already cited locally; not a new measured gain.",
  "url": "https://docs.nvidia.com/cuda/volta-tuning-guide/index.html"
}
```

## VOLTA_MICROARCH

```json
{
  "axes": [
    "C09",
    "C10",
    "C14",
    "HBM01",
    "HBM02",
    "HBM03",
    "HBM04",
    "HBM05",
    "HBM07"
  ],
  "bibliographic_source_sha256": "9672a7afe464cd6740245e7cf6e10aacea30bbcd3064468dfaedf9abeb41b898",
  "bibliography": {
    "arxiv_id": [
      "1804.06826"
    ],
    "author": [
      "Jia, Zhe",
      "Maggioni, Marco",
      "Staiger, Benjamin",
      "Scarpazza, Daniele P."
    ],
    "date": [
      "2018/04/18"
    ],
    "pdf_url": [
      "https://arxiv.org/pdf/1804.06826"
    ],
    "title": [
      "Dissecting the NVIDIA Volta GPU Architecture via Microbenchmarking"
    ]
  },
  "classification": "PARTIALLY_COVERED",
  "evidence_class": "EXTERN_BELEGT",
  "id": "VOLTA_MICROARCH",
  "local_test_status": "NO_NEW_GPU_TEST",
  "obstacles": [],
  "revision": "1804.06826v1;2018-04-18",
  "scope": "66-page originalPDF archived; sections2–4 inspected via webPDF text. Register banks and shared-memory banks are different mechanisms. Published compiler/hardware results are not our counter measurements.",
  "url": "https://arxiv.org/abs/1804.06826"
}
```

## ARCHWIKI

```json
{
  "axes": [
    "H03",
    "H04",
    "H05"
  ],
  "classification": "ALREADY_COVERED",
  "evidence_class": "EXTERN_BELEGT",
  "id": "ARCHWIKI",
  "local_test_status": "NO_NEW_GPU_TEST",
  "obstacles": [],
  "revision": "MediaWiki887502;lastedit2026-10-11 14:24",
  "scope": "Clock/power sections inspected. Direct local originalHTML obtained despite webreader anti-bot rejection. Existing H03/H04 audits govern; desktop/Xorg recommendations do not establish Tesla applicability.",
  "url": "https://wiki.archlinux.org/title/NVIDIA/Tips_and_tricks"
}
```

## BANDWIDTH_BLOG

```json
{
  "axes": [
    "HBM01",
    "HBM06",
    "HBM07",
    "HBM19",
    "H03"
  ],
  "classification": "PARTIALLY_COVERED",
  "evidence_class": "EXTERN_BELEGT",
  "id": "BANDWIDTH_BLOG",
  "local_test_status": "NO_NEW_GPU_TEST",
  "obstacles": [],
  "revision": "No exposed immutable revision;contentSHA pinned",
  "scope": "Secondary roofline intuition. Decode can be bandwidth-limited; division of modelbytes by time is not measured DRAM traffic. Hybrid state, KV, cache, dequantization, launch overhead, batch and prefill change the bound.",
  "url": "https://precipice.tech/blog/llm-inferenz-speicherbandbreite"
}
```

## HBM_POWER

```json
{
  "axes": [
    "HBM01",
    "HBM02",
    "HBM03",
    "HBM04",
    "HBM05",
    "HBM06",
    "HBM07",
    "HBM19"
  ],
  "bibliographic_source_sha256": "ea774f886a8e5b8e01992e652bb8c6786a1618c9a0d7936f246a061d7af89edc",
  "bibliography": {
    "arxiv_id": [
      "2610.14244"
    ],
    "author": [
      "Olgun, Ataberk",
      "Galanopoulos, Spiros",
      "Kakolyris, Andreas Kosmas",
      "Yüksel, İsmail Emir",
      "Luo, Haocong",
      "Bostancı, F. Nisa",
      "Mutlu, Onur"
    ],
    "date": [
      "2026/10/09"
    ],
    "pdf_url": [
      "https://arxiv.org/pdf/2610.14244"
    ],
    "title": [
      "Understanding the Power Consumption of Modern High Bandwidth Memory: Experimental Analysis and Modeling Using Real HBM2 DRAM Chips"
    ]
  },
  "classification": "PARTIALLY_COVERED",
  "evidence_class": "EXTERN_BELEGT",
  "id": "HBM_POWER",
  "local_test_status": "NO_NEW_GPU_TEST",
  "obstacles": [
    "No separate HBM2 rail measurement or programmable DRAM command/bank mapping on this V100."
  ],
  "revision": "2610.14244v1;2026-10-09",
  "scope": "Full originalHTML inspected. Dedicated FPGA HBM2 characterization establishes data-pattern/internal-bus power mechanisms. Board-level NVML cannot identify HBM-rail current or internal bus toggles.",
  "url": "https://arxiv.org/abs/2610.14244"
}
```

## REDDIT_LEAD

```json
{
  "axes": [
    "E03",
    "H06",
    "HBM01"
  ],
  "classification": "DEFERRED",
  "evidence_class": "EXTERN_BELEGT",
  "id": "REDDIT_LEAD",
  "local_test_status": "NO_NEW_GPU_TEST",
  "obstacles": [
    "Partial access; no immutable edit history."
  ],
  "revision": "PostID1x4mtzx;editrevision unavailable",
  "scope": "Webreader rendered multi-GPU discussion; discovery lead only. No verified kernel cause or comparable single16GB result. LocalHTMLHTTP200 is a challenge, JSON403; no full local comment archive claimed.",
  "url": "https://www.reddit.com/r/LocalLLaMA/comments/1x4mtzx/"
}
```

## VLLM_REPORT

```json
{
  "axes": [
    "E03",
    "E06",
    "E07",
    "C03",
    "C10",
    "C11",
    "HBM04",
    "HBM06",
    "HBM18"
  ],
  "classification": "PARTIALLY_COVERED",
  "evidence_class": "EXTERN_BELEGT",
  "id": "VLLM_REPORT",
  "local_test_status": "NO_NEW_GPU_TEST",
  "obstacles": [],
  "revision": "295b5bd547edb07c9de0b58b7c98aaacfac8ec30",
  "scope": "Pinned methodology, benchmarkCSV, graphs/MoE/FP8 and negative-results chapters reviewed. External8×32GB/TP/othermodels; no local speedup transferred.",
  "url": "https://github.com/KumphanartDansiri/v100-vllm-2026"
}
```

## VLLM_IMPLEMENTATION

```json
{
  "axes": [
    "E03",
    "E06",
    "E07",
    "C03",
    "C05",
    "C10",
    "C11",
    "HBM02",
    "HBM04",
    "HBM06",
    "HBM18",
    "K05"
  ],
  "classification": "PARTIALLY_COVERED",
  "evidence_class": "EXTERN_BELEGT",
  "id": "VLLM_IMPLEMENTATION",
  "local_test_status": "NO_NEW_GPU_TEST",
  "obstacles": [
    "REQUIREMENTS retains older0.18/FP8-not-yet-validated prose conflicting with newer README; pinned implementation/logs govern specific scope."
  ],
  "revision": "9e1aa6bc3398c5ea823a80027963709d20ee1974",
  "scope": "Pinned Python/CUDA dispatch, build recipes, TurboMind alignment and FA adapter inspected. Upstream vLLM tags independently checked. No downloaded code executed.",
  "url": "https://github.com/KumphanartDansiri/vllm-fp8-w8a16-sm70"
}
```

## CUDA128_QUEUE_CAPACITY

```json
{
  "axes": [
    "C16"
  ],
  "classification": "PARTIALLY_COVERED",
  "evidence_class": "EXTERN_BELEGT",
  "id": "CUDA128_QUEUE_CAPACITY",
  "local_test_status": "R389:0.25x/0.5x each4nativewarmups/7354.5MiB;2MiBdifferencevsstoredA0,64MiBpracticalgatefailed. No fullqualityclaim.",
  "obstacles": [
    "Fullquarter/halfquality/throughputnotrunafterprimary64MiBmemorygatefutility.",
    "No physicalqueuecapacity/transactioncounter measured."
  ],
  "revision": "ArchivedCUDA12.8.0; frozenHTMLSHA256:cdc49d93372b4e03e94d56f24345373f82ad76b8663c745073463263009637ce",
  "scope": "Documentedfractionalcommandbuffercapacities, not a promisedVRAMsaving or measuredphysicalqueuecounter. Existing1x/2x/4x andnewR389quarter/halfmemoryscreensremainseparate scoped evidence.",
  "url": "https://docs.nvidia.com/cuda/archive/12.8.0/cuda-c-programming-guide/index.html"
}
```

## Factor-specific bibliography

- [K05](factors/K05.md): https://raw.githubusercontent.com/KumphanartDansiri/vllm-fp8-w8a16-sm70/9e1aa6bc3398c5ea823a80027963709d20ee1974/docs/FA_V100_AUDIT.md, https://raw.githubusercontent.com/KumphanartDansiri/vllm-fp8-w8a16-sm70/9e1aa6bc3398c5ea823a80027963709d20ee1974/src/fp8_w8a16_sm70/fa_v100_prefill.py
- [C03](factors/C03.md): https://raw.githubusercontent.com/KumphanartDansiri/v100-vllm-2026/295b5bd547edb07c9de0b58b7c98aaacfac8ec30/docs/03_eager_vs_cudagraph.md, https://raw.githubusercontent.com/KumphanartDansiri/vllm-fp8-w8a16-sm70/9e1aa6bc3398c5ea823a80027963709d20ee1974/docs/PROFILING.md
- [C04](factors/C04.md): https://raw.githubusercontent.com/KumphanartDansiri/v100-vllm-2026/295b5bd547edb07c9de0b58b7c98aaacfac8ec30/docs/03_eager_vs_cudagraph.md, https://raw.githubusercontent.com/KumphanartDansiri/vllm-fp8-w8a16-sm70/9e1aa6bc3398c5ea823a80027963709d20ee1974/docs/PROFILING.md
- [C05](factors/C05.md): https://raw.githubusercontent.com/KumphanartDansiri/vllm-fp8-w8a16-sm70/9e1aa6bc3398c5ea823a80027963709d20ee1974/docs/FA_V100_AUDIT.md, https://raw.githubusercontent.com/KumphanartDansiri/vllm-fp8-w8a16-sm70/9e1aa6bc3398c5ea823a80027963709d20ee1974/src/fp8_w8a16_sm70/fa_v100_prefill.py
- [C10](factors/C10.md): https://raw.githubusercontent.com/KumphanartDansiri/v100-vllm-2026/295b5bd547edb07c9de0b58b7c98aaacfac8ec30/docs/02_fp16_moe_fix.md, https://raw.githubusercontent.com/KumphanartDansiri/vllm-fp8-w8a16-sm70/9e1aa6bc3398c5ea823a80027963709d20ee1974/src/fp8_w8a16_sm70/vllm_serve.py
- [C11](factors/C11.md): https://raw.githubusercontent.com/KumphanartDansiri/vllm-fp8-w8a16-sm70/9e1aa6bc3398c5ea823a80027963709d20ee1974/src/fp8_w8a16_sm70/fp8_dequant.cu, https://raw.githubusercontent.com/KumphanartDansiri/vllm-fp8-w8a16-sm70/9e1aa6bc3398c5ea823a80027963709d20ee1974/src/fp8_w8a16_sm70/turbomind_fp8_backend.py
- [Q03](factors/Q03.md): https://raw.githubusercontent.com/KumphanartDansiri/vllm-fp8-w8a16-sm70/9e1aa6bc3398c5ea823a80027963709d20ee1974/src/fp8_w8a16_sm70/fp8_dequant.cu, https://raw.githubusercontent.com/KumphanartDansiri/vllm-fp8-w8a16-sm70/9e1aa6bc3398c5ea823a80027963709d20ee1974/src/fp8_w8a16_sm70/turbomind_fp8_backend.py
- [E03](factors/E03.md): https://raw.githubusercontent.com/KumphanartDansiri/v100-vllm-2026/295b5bd547edb07c9de0b58b7c98aaacfac8ec30/docs/02_fp16_moe_fix.md, https://raw.githubusercontent.com/KumphanartDansiri/vllm-fp8-w8a16-sm70/9e1aa6bc3398c5ea823a80027963709d20ee1974/docker/Dockerfile.vllm019_cu126, https://raw.githubusercontent.com/KumphanartDansiri/vllm-fp8-w8a16-sm70/9e1aa6bc3398c5ea823a80027963709d20ee1974/docker/Dockerfile.vllm021_cu126, https://raw.githubusercontent.com/KumphanartDansiri/vllm-fp8-w8a16-sm70/9e1aa6bc3398c5ea823a80027963709d20ee1974/docs/FA_V100_AUDIT.md, https://raw.githubusercontent.com/KumphanartDansiri/vllm-fp8-w8a16-sm70/9e1aa6bc3398c5ea823a80027963709d20ee1974/src/fp8_w8a16_sm70/fa_v100_prefill.py, https://raw.githubusercontent.com/KumphanartDansiri/vllm-fp8-w8a16-sm70/9e1aa6bc3398c5ea823a80027963709d20ee1974/src/fp8_w8a16_sm70/fp8_dequant.cu, https://raw.githubusercontent.com/KumphanartDansiri/vllm-fp8-w8a16-sm70/9e1aa6bc3398c5ea823a80027963709d20ee1974/src/fp8_w8a16_sm70/turbomind_fp8_backend.py, https://raw.githubusercontent.com/KumphanartDansiri/vllm-fp8-w8a16-sm70/9e1aa6bc3398c5ea823a80027963709d20ee1974/src/fp8_w8a16_sm70/vllm_serve.py
- [E06](factors/E06.md): https://raw.githubusercontent.com/KumphanartDansiri/vllm-fp8-w8a16-sm70/9e1aa6bc3398c5ea823a80027963709d20ee1974/docker/Dockerfile.vllm019_cu126, https://raw.githubusercontent.com/KumphanartDansiri/vllm-fp8-w8a16-sm70/9e1aa6bc3398c5ea823a80027963709d20ee1974/docker/Dockerfile.vllm021_cu126
- [E07](factors/E07.md): https://raw.githubusercontent.com/KumphanartDansiri/vllm-fp8-w8a16-sm70/9e1aa6bc3398c5ea823a80027963709d20ee1974/docker/Dockerfile.vllm019_cu126, https://raw.githubusercontent.com/KumphanartDansiri/vllm-fp8-w8a16-sm70/9e1aa6bc3398c5ea823a80027963709d20ee1974/docker/Dockerfile.vllm021_cu126
- [HBM02](factors/HBM02.md): https://raw.githubusercontent.com/KumphanartDansiri/vllm-fp8-w8a16-sm70/9e1aa6bc3398c5ea823a80027963709d20ee1974/src/fp8_w8a16_sm70/fp8_dequant.cu, https://raw.githubusercontent.com/KumphanartDansiri/vllm-fp8-w8a16-sm70/9e1aa6bc3398c5ea823a80027963709d20ee1974/src/fp8_w8a16_sm70/turbomind_fp8_backend.py
- [HBM04](factors/HBM04.md): https://raw.githubusercontent.com/KumphanartDansiri/v100-vllm-2026/295b5bd547edb07c9de0b58b7c98aaacfac8ec30/docs/02_fp16_moe_fix.md, https://raw.githubusercontent.com/KumphanartDansiri/vllm-fp8-w8a16-sm70/9e1aa6bc3398c5ea823a80027963709d20ee1974/src/fp8_w8a16_sm70/vllm_serve.py
- [HBM06](factors/HBM06.md): https://raw.githubusercontent.com/KumphanartDansiri/vllm-fp8-w8a16-sm70/9e1aa6bc3398c5ea823a80027963709d20ee1974/src/fp8_w8a16_sm70/fp8_dequant.cu, https://raw.githubusercontent.com/KumphanartDansiri/vllm-fp8-w8a16-sm70/9e1aa6bc3398c5ea823a80027963709d20ee1974/src/fp8_w8a16_sm70/turbomind_fp8_backend.py
- [HBM18](factors/HBM18.md): https://raw.githubusercontent.com/KumphanartDansiri/vllm-fp8-w8a16-sm70/9e1aa6bc3398c5ea823a80027963709d20ee1974/docs/FA_V100_AUDIT.md, https://raw.githubusercontent.com/KumphanartDansiri/vllm-fp8-w8a16-sm70/9e1aa6bc3398c5ea823a80027963709d20ee1974/src/fp8_w8a16_sm70/fa_v100_prefill.py
- [BMT01](factors/BMT01.md): https://huggingface.co/datasets/hkust-nlp/Toolathlon, https://huggingface.co/tsinghua-sigs-robot-lab/VeriLoop-E2
- [BMT02](factors/BMT02.md): https://arxiv.org/abs/2211.17192, https://huggingface.co/SuperLogic/Qwen3.8-27B-Flash-MTP-GGUF
- [BMT03](factors/BMT03.md): https://arxiv.org/abs/2211.17192, https://huggingface.co/SuperLogic/Qwen3.8-27B-Flash-MTP-GGUF
- [BMT04](factors/BMT04.md): https://arxiv.org/abs/2211.17192
- [BMT05](factors/BMT05.md): https://arxiv.org/abs/2211.17192, https://huggingface.co/SuperLogic/Qwen3.8-27B-Flash-MTP-GGUF
- [BMT06](factors/BMT06.md): https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B, https://huggingface.co/datasets/benchflow/skillsbench, https://huggingface.co/tsinghua-sigs-robot-lab/VeriLoop-E2, https://huggingface.co/tsinghua-sigs-robot-lab/VeriLoop-E2/blob/44b6f230347f9ccf2a5ce96a44bcd74ecaaaa51f/README.md
- [BMT07](factors/BMT07.md): https://arxiv.org/abs/2309.06180, https://huggingface.co/datasets/hkust-nlp/Toolathlon
- [BMT08](factors/BMT08.md): https://arxiv.org/abs/2401.18079, https://arxiv.org/abs/2402.02750
- [BMT09](factors/BMT09.md): https://arxiv.org/abs/2402.02750, https://github.com/PrismML-Eng/Bonsai-demo/blob/db871ea96bffff5ce5609873c412b75d7cd5ba3c/community-benchmarks/bonsai2/cuda-tesla-v100-windows.md
- [BMT10](factors/BMT10.md): https://docs.nvidia.com/cuda/volta-tuning-guide/index.html, https://github.com/PrismML-Eng/Bonsai-demo/blob/db871ea96bffff5ce5609873c412b75d7cd5ba3c/community-benchmarks/bonsai2/cuda-tesla-v100-windows.md, https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf
- [BMT11](factors/BMT11.md): https://arxiv.org/abs/2601.20088, https://arxiv.org/abs/2608.13966, https://huggingface.co/LiquidAI/LFM2.5-24B-A2B, https://huggingface.co/QUASAR-QAT/Qwen3.8-27B-QUASAR-NVFP4, https://huggingface.co/QUASAR-QAT/Qwen3.8-27B-QUASAR-NVFP4/blob/4a22293aa6d1026844bc93a8727f1837e48acd89/README.md, https://huggingface.co/google/gemma-4-12B-it
- [BMT12](factors/BMT12.md): https://arxiv.org/abs/2312.17238, https://huggingface.co/LiquidAI/LFM2.5-24B-A2B
- [BMT13](factors/BMT13.md): https://arxiv.org/abs/2602.06036, https://huggingface.co/LiquidAI/LFM2.5-8B-A1B, https://huggingface.co/meta-models/Muse-Glimmer-30B-GGUF
- [BMT14](factors/BMT14.md): https://arxiv.org/abs/1703.04200, https://arxiv.org/abs/2106.09685, https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B
- [BMT15](factors/BMT15.md): https://arxiv.org/abs/2306.00978, https://arxiv.org/abs/2403.07378
- [BMT16](factors/BMT16.md): https://github.com/NVlabs/ToolOrchestra, https://huggingface.co/LiquidAI/LFM2.5-8B-A1B, https://huggingface.co/google/gemma-4-12B-it, https://huggingface.co/nvidia/Nemotron-Orchestrator-8B, https://huggingface.co/nvidia/Nemotron-Orchestrator-8B/blob/26df4b9aad5abdc5b7871ee4c71063ce888feb26/README.md, https://huggingface.co/ornith-ai/Ornith-1.5-9B
- [BMT17](factors/BMT17.md): https://docs.nvidia.com/cuda/volta-tuning-guide/index.html, https://huggingface.co/SuperLogic/Qwen3.8-27B-Flash-MTP-GGUF
- [BMT18](factors/BMT18.md): https://arxiv.org/abs/2210.03629, https://huggingface.co/datasets/hkust-nlp/Toolathlon
- [BMT19](factors/BMT19.md): https://huggingface.co/Nanbeige/Nanbeige4.2-3B, https://huggingface.co/Nanbeige/Nanbeige4.2-3B/blob/b82e54bd609793562a75cbf9337970a93369eab5/README.md, https://huggingface.co/Nanbeige/Nanbeige4.2-3B/blob/main/modeling_nanbeige.py, https://huggingface.co/Nanbeige/Nanbeige4.2-3B/raw/b82e54bd609793562a75cbf9337970a93369eab5/configuration_nanbeige.py, https://huggingface.co/Nanbeige/Nanbeige4.2-3B/raw/b82e54bd609793562a75cbf9337970a93369eab5/modeling_nanbeige.py
- [BMT20](factors/BMT20.md): https://huggingface.co/Nanbeige/Nanbeige4.2-3B/blob/b82e54bd609793562a75cbf9337970a93369eab5/README.md, https://huggingface.co/Nanbeige/Nanbeige4.2-3B/blob/main/configuration_nanbeige.py, https://huggingface.co/Nanbeige/Nanbeige4.2-3B/blob/main/modeling_nanbeige.py, https://huggingface.co/Nanbeige/Nanbeige4.2-3B/raw/b82e54bd609793562a75cbf9337970a93369eab5/configuration_nanbeige.py, https://huggingface.co/Nanbeige/Nanbeige4.2-3B/raw/b82e54bd609793562a75cbf9337970a93369eab5/modeling_nanbeige.py
- [BMT21](factors/BMT21.md): https://huggingface.co/ornith-ai/Ornith-1.5-9B, https://huggingface.co/ornith-ai/Ornith-1.5-9B/blob/489cb97981b8654bcfcf30ce1f94ed1b62e07b53/README.md
- [BMT22](factors/BMT22.md): https://github.com/hamishivi/tmax, https://huggingface.co/allenai/tmax-9b, https://huggingface.co/allenai/tmax-9b/blob/81ec54b29986d78191596d81900c0f8de2fa1b35/README.md
- [BMT23](factors/BMT23.md): https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6, https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6/blob/c5630abae1d940eafe0697512a0325494b02ab42/README.md, https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6/raw/c5630abae1d940eafe0697512a0325494b02ab42/configuration_paddleocr_vl.py, https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6/raw/c5630abae1d940eafe0697512a0325494b02ab42/modeling_paddleocr_vl.py, https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6/raw/c5630abae1d940eafe0697512a0325494b02ab42/processing_paddleocr_vl.py, https://huggingface.co/opendatalab/MinerU2.5-Pro-2605-1.2B, https://huggingface.co/opendatalab/MinerU2.5-Pro-2605-1.2B/blob/08aaea840498d49ce16247b6263196cf02814885/README.md
- [BMT24](factors/BMT24.md): https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6-GGUF, https://huggingface.co/lightonai/LightOnOCR-3-0.8B, https://huggingface.co/lightonai/LightOnOCR-3-0.8B/blob/36d8636925327c671bd8e479c517a004f7566bd9/README.md
- [BMT25](factors/BMT25.md): https://huggingface.co/Hcompany/Holo2-4B, https://huggingface.co/Hcompany/Holo2-4B/blob/44b125965ebefea6c04958f972a0219cff36e90d/README.md, https://huggingface.co/inclusionAI/UI-Venus-1.5-8B, https://huggingface.co/inclusionAI/UI-Venus-1.5-8B/blob/a06ff6c6f15a9eca210769dacc1603f73b4a500c/README.md
- [BMT26](factors/BMT26.md): https://huggingface.co/OpenMOSS-Team/MOSS-Transcribe-Diarize, https://huggingface.co/OpenMOSS-Team/MOSS-Transcribe-Diarize/blob/704aa4a9c304e8520be88901e0d1960158ef5b15/README.md, https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b, https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b/blob/ea30d66debe3740a08b573244286791d423d6b3e/README.md
- [BMT27](factors/BMT27.md): https://github.com/Maxxxel/v100-volta-ai-optimization-lab/issues/6, https://huggingface.co/datasets/LocalLLaMA/typed-decisions, https://huggingface.co/perplexity-ai/pplx-decider-v1.1-27b, https://huggingface.co/perplexity-ai/pplx-decider-v1.1-27b/blob/14c9d90137962d300f3de95633f7b6535e80c5ce/README.md
- [BMT28](factors/BMT28.md): https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16, https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16/blob/a9904d24bcc1d289a1950fa9d2b978c47cf903b9/README.md
- [BMT29](factors/BMT29.md): https://huggingface.co/ibm-granite/granite-4.2-8b, https://huggingface.co/ibm-granite/granite-4.2-8b/blob/f8de16cdcdbc6c779ca517604e050d82cc119e44/README.md, https://huggingface.co/meta-models/Muse-Glimmer-30B, https://huggingface.co/meta-models/Muse-Glimmer-30B/blob/a4e59da52a7bc87ae7251dd5545c0dd437c44b68/README.md
- [BMT30](factors/BMT30.md): https://huggingface.co/Nanbeige/Nanbeige4.2-3B/blob/b82e54bd609793562a75cbf9337970a93369eab5/README.md, https://huggingface.co/Nanbeige/Nanbeige4.2-3B/blob/main/modeling_nanbeige.py, https://huggingface.co/Nanbeige/Nanbeige4.2-3B/raw/b82e54bd609793562a75cbf9337970a93369eab5/configuration_nanbeige.py, https://huggingface.co/Nanbeige/Nanbeige4.2-3B/raw/b82e54bd609793562a75cbf9337970a93369eab5/modeling_nanbeige.py
- [BMT31](factors/BMT31.md): https://huggingface.co/Qwen/Qwen3.5-9B
- [BMT32](factors/BMT32.md): https://huggingface.co/MiniMaxAI/MiniMax-M3/blob/f0e1c1e04d40177e4673a22097036854f536e9c0/README.md, https://huggingface.co/XiaomiMiMo/MiMo-V2.5/blob/63651580ca774f8504f676040460aed3e1244ac1/README.md, https://huggingface.co/moonshotai/Kimi-K2.6/blob/7eb5002f6aadc958aed6a9177b7ed26bb94011bb/README.md, https://huggingface.co/stepfun-ai/Step-3.5-Flash/blob/ab446a3de5e171ea341227e24bb1f090e1b771f7/README.md
