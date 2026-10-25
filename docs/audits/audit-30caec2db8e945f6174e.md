# Public audit excerpt

Original SHA256: `30caec2db8e945f6174ed31fe2ede184a0fbc969327d42a32602d4ba03336576`

Original file: `research-metadata.json`; 1120 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decision": "Retain and compare native profiles using actual success, task time, GPU J/success and VRAM. One pass over18 exposed tasks cannot establish superiority, noninferiority or a Champion. Original official qualifications remain unchanged; no production adoption.",
  "scope": "Whole native model-profile comparison on frozen exposed development tasks. Models, quantization, templates and native samplers may differ; no causal optimization or population-quality inference."
}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "comparison": {
    "peak_vram_change_mib": 0.0,
    "task_phase_change_percent": -28.22055242275765
  },
  "model_requests": 0,
  "quality": {
    "candidate_completed": 18,
    "candidate_solved": 12,
    "fixed_set_exact_two_sided_p": 1,
    "paired_gained": 2,
    "paired_lost": 3,
    "reference_solved": 13,
    "tasks": 18
  }
}
```

</details>
