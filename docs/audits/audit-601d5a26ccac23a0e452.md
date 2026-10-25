# Public audit excerpt

Original SHA256: `601d5a26ccac23a0e4520f92ce47e2c1e5e6767991ee3042b65fa394a43d47aa`

Original file: `research-metadata.json`; 1528 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decision": "Retain Nexus as a promising practical agent profile:14/18 at258.38s and5011.18–5015.32GPU J/success. One more observed success than OmniCoder at similar task time, same recorded peak VRAM. Small exposed task set and one pass do not establish model superiority, noninferiority or a Champion. Continue model-profile comparisons and independent qualification; no production change.",
  "scope": "Whole existing Nexus OFF/T0 profile against OmniCoder native reference on identical frozen18 tasks/order/oracles. Different weights/quantization/template/sampling are not a causal optimization. Full existing coding130/164 and tools178/200 remain in their original qualified profile; no official-test repeat."
}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "comparison": {
    "GPU_j_per_success_lower": 5011.176214285714,
    "GPU_j_per_success_upper": 5015.319571428571,
    "peak_vram_change_mib": 0.0,
    "task_phase_change_percent": 0.051372503963920124
  },
  "model_requests": 0,
  "quality": {
    "candidate_solved": 14,
    "fixed_set_exact_two_sided_p": 1,
    "paired_gained": 3,
    "paired_lost": 2,
    "reference_solved": 13,
    "tasks": 18
  }
}
```

</details>
