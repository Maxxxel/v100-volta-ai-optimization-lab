# Public audit excerpt

Original SHA256: `d4b3b0fb2de368334ea4712db521546e0a6952db3ed06b3d9d5dd36235a2ddda`

Original file: `AUDIT.json`; 4260 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decision": "Screen only; fresh control and independent validation required before any promotion.",
  "evidence_class": "LOKAL_GEMESSEN"
}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "actual_generation_requests": 151,
  "model_starts": 1,
  "native_lean_harness_screen": {
    "arms": [
      {
        "GPU_j_per_success_lower": 4083.0299615384615,
        "GPU_j_per_success_upper": 4089.4858846153847,
        "arm": "upstream-tool-toon-v1",
        "case_wall_s": 391.540849768,
        "complete": true,
        "completed_cases": 33,
        "completion_tokens_reported": 21868,
        "input_tokens_attempted": 268793,
        "input_tokens_reported": 268793,
        "invalid_actions": 0,
        "model_calls_attempted": 151,
        "peak_sampled_device_vram_mib": 7688.5,
        "planned_cases": 33,
        "policy_gate_passes": 29,
        "policy_violations": 4,
        "reasoning_tokens_reported": null,
        "rejected_calls": 4,
        "request_errors": 0,
        "response_wall_s": 386.190954915,
        "solved": 26,
        "successful_tasks_per_s": 0.06640431008771065,
        "tool_calls": 118,
        "total_tokens_reported": 290661,
        "transform_cpu_s": 0.317739501,
        "transform_wall_s": 2.451414991
      }
    ],
    "case_executions": 33,
    "codec_overhead": {
      "codec_children_CPU_s": 2.318493,
      "codec_parent_CPU_s": 0.171910714,
      "codec_wall_s": 2.305083824,
      "completed_task_model_calls": 151,
      "host_CPU_energy_j": null,
      "request_transforms": 151,
      "tool_result_visits": 336,
      "warmup_input_tokens": 536,
      "warmup_model_calls": 2,
      "warmup_output_tokens": 129,
      "warmup_response_wall_s": 1.966683007
    },
    "comparison": {
      "conservative_energy_per_success_reduction_percent": -4.20253342747452,
      "decision": "REJECT_OBSERVED_QUALITY_OR_POLICY_REGRESSION",
      "latency_reduction_percent": 2.635209635405189,
      "new_policy_failure_cases": 1,
      "observed_quality_and_policy_gate": false,
      "paired_gained": 1,
      "paired_lost": 3,
      "token_reduction_percent": 3.6145257510089124
    },
    "comparison_audit_id": "audit-5abe28323e10aa0fc6e7",
    "correction_audit_id": null,
    "dataset_id": "jarvis-original-caveman-toon-screen33-v1",
    "experiment_id": "R598",
    "implementation": {
      "codec_binary_sha256": "80189ce6b009ea9fba762cdef88d568f20a8640fde4302f50a2cfcb36ab1d754",
      "engine_binary_sha256": "08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54",
      "simulator_archive_sha256": "be731f9a8f289cbcaedc502189a723ee09c7b0de187904de9f30945ffe6c86da",
      "source_commit": null,
      "transform_module_sha256": "c9a39349e84e94996ef12d8ab2c6b7833b11658fe9f37c99bda9d105df9e32a0",
      "transport_sha256": "e602e12551aa5dba13f55ca58a9709e30d32a6eb6029f1fd90ba8637ad60406d",
      "upstream_commit": "9b68f7ed12b05e7efaff18e65c5a3fc2849fd0a4",
      "upstream_repository": "https://github.com/JuliusBrussee/caveman"
    },
    "independent_review_audit_id": "audit-726bea0d9755c37c5257",
    "model": "OmniCoder bartowski Q6 · original TOON B-only33",
    "model_sha256": "a73cc3136da753063e667edef95bec3bbf47829e34a2a31bf0f5a29c970f9052",
    "official_benchmark": false,
    "paired_unique_cases": 0,
    "profile_sha256": "20b28ea71a8fb690a6950d51795a288d5804f9d0c1f9f0dc4ae590fa51dabc62",
    "quality_audit_id": "audit-a18604f3c172c5b04cb5",
    "scope": "B-only33 exposed development cases. Stored original-request control is a separate historical measurement, not a fresh paired run or official benchmark. Failed tasks remain in costs; no population equivalence or adoption.",
    "scorer_sha256": "a1e8352762347f269123c203022990a860b735414ee0b3949ae41a2d126515e1",
    "screen_only": true,
    "stored_reference": {
      "arm": "reference",
      "audit_sha256": "4cf83094ee818935f1bc82ef4013f7c74fec8d9ad93cf00f47afba643959ba4a",
      "experiment_id": "R587",
      "fresh_contemporaneous_control": false,
      "metrics": {
        "GPU_j_per_success_lower": 3924.5551428571425,
        "GPU_j_per_success_upper": 4014.947464285714,
        "arm": "reference",
        "case_wall_s": 402.138029879,
        "complete": true,
        "completed_cases": 33,
        "completion_tokens_reported": 22528,
        "input_tokens_attempted": 279033,
        "input_tokens_reported": 279033,
        "invalid_actions": 0,
        "model_calls_attempted": 154,
        "peak_sampled_device_vram_mib": 7680.5,
        "planned_cases": 33,
        "policy_gate_passes": 29,
        "policy_violations": 4,
        "reasoning_tokens_reported": null,
        "rejected_calls": 4,
        "request_errors": 0,
        "response_wall_s": 398.870619721,
        "solved": 28,
        "successful_tasks_per_s": 0.06962783402610534,
        "tool_calls": 121,
        "total_tokens_reported": 301561,
        "transform_cpu_s": 0.063391149,
        "transform_wall_s": 0.062968829
      },
      "new_GPU_runs": 0,
      "quality_sha256": "83922ba905007692993cc1c82af2002091f98e00044d7c05e4ef15adb1c4fe3d"
    },
    "task_phase_s": 391.549849328,
    "transform_source": {
      "file": "assets/harness/original-toon-adapter.py",
      "license": "MIT",
      "scope": "Exact lab-owned request transform; private task fixtures, responses, models and privileged execution code are excluded.",
      "sha256": "c9a39349e84e94996ef12d8ab2c6b7833b11658fe9f37c99bda9d105df9e32a0",
      "source_audit_id": "audit-d4b3b0fb2de368334ea4"
    },
    "winner_qualified": false
  },
  "peak_device_vram_mib": 7688.5,
  "solved": 26,
  "tasks": 33
}
```

</details>
