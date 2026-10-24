# Hardware & scope

One NVIDIA Tesla V100-SXM2 ·16 GB HBM2 ·Volta SM70. Serialized local inference with recorded model, engine and kernel identities.

- CUDA12.8 compiler baseline; driver580.178.04 recorded per run. Compiler, toolkit and loaded runtime identities remain distinct.
- FP16 Tensor Cores; native BF16/FP8 Tensor Cores, cp.async and TMA are not assumed.
- Attention KV, recurrent state, graphs and caches share the device memory budget.
- Temperature is telemetry; existing ECC, VRAM, power, thermal and restore guards remain mandatory.

[Reproduce](reproduce.md) · [Safety and admission](broker-admission.md)
