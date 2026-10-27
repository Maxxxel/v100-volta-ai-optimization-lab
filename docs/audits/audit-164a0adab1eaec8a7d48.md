# Public audit excerpt

Original SHA256: `164a0adab1eaec8a7d48a03575fe4322139c31964396d93ebfb2c6bc72720ee3`

Original file: `AUDIT.json`; 4265 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
  "actual_generation_requests": 155,
  "model_starts": 1,
  "native_lean_harness_screen": {
    "arms": [
      {
        "GPU_j_per_success_lower": 4369.212576923077,
        "GPU_j_per_success_upper": 4374.574038461538,
        "arm": "upstream-node-shrink-v1",
        "case_wall_s": 418.846482548,
        "complete": true,
        "completed_cases": 33,
        "completion_tokens_reported": 23524,
        "input_tokens_attempted": 279297,
        "input_tokens_reported": 279297,
        "invalid_actions": 0,
        "model_calls_attempted": 155,
        "peak_sampled_device_vram_mib": 7680.5,
        "planned_cases": 33,
        "policy_gate_passes": 27,
        "policy_violations": 6,
        "reasoning_tokens_reported": null,
        "rejected_calls": 6,
        "request_errors": 0,
        "response_wall_s": 411.248780368,
        "solved": 26,
        "successful_tasks_per_s": 0.062075249723555666,
        "tool_calls": 122,
        "total_tokens_reported": 302821,
        "transform_cpu_s": 0.181019642,
        "transform_wall_s": 4.586701679
      }
    ],
    "case_executions": 33,
    "codec_overhead": {
      "catalog_visits": 155,
      "codec_children_CPU_s": 4.526338,
      "codec_parent_CPU_s": 0.078581111,
      "codec_wall_s": 4.484415842,
      "host_CPU_energy_j": null,
      "request_transforms": 155,
      "unknown_catalog_requests": 0
    },
    "comparison": {
      "conservative_energy_per_success_reduction_percent": -11.46674920400721,
      "decision": "REJECT_OBSERVED_QUALITY_OR_POLICY_REGRESSION",
      "latency_reduction_percent": -4.15490489025061,
      "new_policy_failure_cases": 2,
      "observed_quality_and_policy_gate": false,
      "paired_gained": 0,
      "paired_lost": 2,
      "token_reduction_percent": -0.4178259125019457
    },
    "comparison_audit_id": "audit-1094f79b033edabb4753",
    "correction_audit_id": null,
    "dataset_id": "jarvis-original-caveman-node-shrink-screen33-v1",
    "experiment_id": "R600",
    "implementation": {
      "engine_binary_sha256": "08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54",
      "simulator_archive_sha256": "be731f9a8f289cbcaedc502189a723ee09c7b0de187904de9f30945ffe6c86da",
      "source_commit": null,
      "transform_module_sha256": "23239654f8ebf8ef5493f2ac267c5085597788e374f7df7d8243659ab571bab5",
      "transport_sha256": "e602e12551aa5dba13f55ca58a9709e30d32a6eb6029f1fd90ba8637ad60406d"
    },
    "independent_review_audit_id": "audit-c9aec392c6166ebfd8ff",
    "model": "OmniCoder bartowski Q6 · original Node shrink B-only33",
    "model_sha256": "a73cc3136da753063e667edef95bec3bbf47829e34a2a31bf0f5a29c970f9052",
    "official_benchmark": false,
    "paired_unique_cases": 0,
    "profile_sha256": "b39505ffe08c8c742f9521aeadb87270dc33482324b27a0194e3d28ba97ca09e",
    "quality_audit_id": "audit-fca23c0d57c99aa9c02c",
    "request_wrapper_source": {
      "file": "assets/harness/original-node-shrink-request.cjs",
      "license": "MIT",
      "sha256": "cb547fe1f29b5e3d7d6ef1e9b658c07d03519ae2c27c3050a74e9d6c489038b8"
    },
    "scope": "B-only33 exposed development cases. Stored original-request control is a separate historical measurement, not a fresh paired run or official benchmark. Failed tasks remain in costs; no population equivalence or adoption.",
    "scorer_sha256": "40f34ec50d64fd46cccac52f8ef66d4a1aed0d253dde3829933b4a1e4553ccb6",
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
    "task_phase_s": 418.85531691,
    "transform_source": {
      "file": "assets/harness/original-node-shrink-adapter.py",
      "license": "MIT",
      "scope": "Exact lab-owned request transform; private task fixtures, responses, models and privileged execution code are excluded.",
      "sha256": "23239654f8ebf8ef5493f2ac267c5085597788e374f7df7d8243659ab571bab5",
      "source_audit_id": "audit-164a0adab1eaec8a7d48"
    },
    "upstream_Node_source": {
      "artifacts": [
        {
          "name": "caveman-node",
          "sha256": "67ca5783febb8bf85736c79fcdd92c8d6d465a0eb2a082672bcdfa76a506751c"
        },
        {
          "name": "caveman-shrink.cjs",
          "sha256": "87b89523c9466f7634b2f70dbaaa483648756e927127a4d11ba95f64003fde7f"
        },
        {
          "name": "caveman-shrink-request.cjs",
          "sha256": "cb547fe1f29b5e3d7d6ef1e9b658c07d03519ae2c27c3050a74e9d6c489038b8"
        }
      ],
      "commit": "9b68f7ed12b05e7efaff18e65c5a3fc2849fd0a4",
      "license": "Apache-2.0",
      "node_version": "24.22.0",
      "repository": "https://github.com/JuliusBrussee/caveman"
    },
    "winner_qualified": false
  },
  "peak_device_vram_mib": 7680.5,
  "solved": 26,
  "tasks": 33
}
```

</details>
