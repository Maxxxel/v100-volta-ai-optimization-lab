# Public audit excerpt

Original SHA256: `01a7b6f1fece7c7f7fbaa579cafa276548757833ac49c06244eeb7765030e3c2`

Original file: `research-metadata.json`; 5111 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decision": "No Champion update or model exclusion. OmniCoder shows13/18 with lower observed task cost than14/18 Qwen3.8; this one-task difference is not a qualified model-quality win. Qwen3.5 has8/18 and lower total time/VRAM but higher GPU J/success. Gemma9/18 retains the strongest recorded coding result and requires targeted context diagnosis. Preserve all qualified model profiles and continue justified missing-model/agent qualification; consider an isolated Gemma16K context variant after source/risk admission, unchanged4K output, before broader tuning.",
  "limits": [
    "Previously used development tasks, not unseen validation or Terminal-Bench. Different models, quantizations, templates and native samplers are whole profiles, not causal optimization factors.",
    "One requested seed per profile; Gemma uses its native T1 while the others requestT0. Paired fixed-set p-values are descriptive, without population significance or multiple-comparison winner selection.",
    "Gemma has two actual context/output reservation preflight failures at4103/4185 prompt tokens plus4096 output versus8192 context. Preserve9/18 and count those failures separately; larger-context counterfactual quality is not measured.",
    "GPU counter brackets are measured GPU-only case costs including failures and between-case setup; they are not statistical confidence intervals or host/system energy. Light bounded CPU sidework was allowed."
  ],
  "scope": "Four native model-profile comparisons on exactly the same18 original frozen simulated development tasks/order/oracles. Each has one GPU session, separate immutable identity and independent reply replay. Existing official coding/tools results are retained; Qwen3.8 selected tools200 remains partial and is not promoted."
}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "comparison": {
    "R519_versus_R518": {
      "candidate_gained": 1,
      "candidate_lost": 6,
      "fixed_set_exact_two_sided_p": 0.125,
      "peak_vram_change_mib": -1400.0,
      "task_s_change_percent": -16.774982299355102
    },
    "R520_versus_R518": {
      "candidate_gained": 2,
      "candidate_lost": 6,
      "fixed_set_exact_two_sided_p": 0.2890625,
      "peak_vram_change_mib": 762.0,
      "task_s_change_percent": 16.194604318934115
    },
    "R521_versus_R518": {
      "candidate_gained": 4,
      "candidate_lost": 3,
      "fixed_set_exact_two_sided_p": 1,
      "peak_vram_change_mib": 5098.0,
      "task_s_change_percent": 84.3292546057816
    }
  },
  "model_requests": 0,
  "models": {
    "R518": {
      "GPU_j_per_success_lower": 5447.822,
      "GPU_j_per_success_upper": 5455.779076923077,
      "audit_sha256": "b99333f1afac7255e644d570fed93e27cc523b8130c5ef1688f5a941ad5cfd53",
      "model": "OmniCoder-9B",
      "model_sha256": "b0c1664c86338be24090a45d8b86bd106ba755d004f8746d99ee5ad69258fc3b",
      "peak_vram_mib": 7356.5,
      "policy_gate_passes": 15,
      "preflight_cases": 0,
      "profile_sha256": "478cc0072ffa3b60d110117a73538beb9ceab19dcf280b6dd025dd8efcec89df",
      "solved": 13,
      "task_s": 258.246524431,
      "tasks": 18
    },
    "R519": {
      "GPU_j_per_success_lower": 7042.298,
      "GPU_j_per_success_upper": 7051.751,
      "audit_sha256": "2256e0b376afc37e9ba2365b340b24965865734b1a2510f72bc2d823dd3c59ef",
      "model": "Qwen3.5-9B",
      "model_sha256": "02d45dc1cf451ba2475ac33b301c2dd8f985abe4c182ce04a1f2f5bf0260278d",
      "peak_vram_mib": 5956.5,
      "policy_gate_passes": 11,
      "preflight_cases": 0,
      "profile_sha256": "bb5da299c67348aa26a26bc5f292becabb3065e546fc549bb79d5fc76032f7c7",
      "solved": 8,
      "task_s": 214.925715669,
      "tasks": 18
    },
    "R520": {
      "GPU_j_per_success_lower": 8036.579333333334,
      "GPU_j_per_success_upper": 8047.347333333334,
      "audit_sha256": "7fdbd2538f59dfd94cc19dc48283a4cb27d832a86e7bf6139a59ca8d0479a6d8",
      "model": "Gemma4-12B",
      "model_sha256": "93567e57a8fe10b23569b9d9ec38cd005deedf71e29477c421a4b83f418a538b",
      "peak_vram_mib": 8118.5,
      "policy_gate_passes": 15,
      "preflight_cases": 2,
      "profile_sha256": "2920276080023c405bffccbe137bce837b8e7debd75ce8737b941b7af454b5ac",
      "solved": 9,
      "task_s": 300.06852723,
      "tasks": 18
    },
    "R521": {
      "GPU_j_per_success_lower": 9276.77,
      "GPU_j_per_success_upper": 9283.121642857142,
      "audit_sha256": "865881cda504326bdc452d8b76c68c11eb9d220ec6a5c1c89ce44d2f914f89ca",
      "model": "Qwen3.8-27B",
      "model_sha256": "58fd826723939933dc86f45b7fe04545cbc2de1c70f6fe2cdd3858c87a98c12f",
      "peak_vram_mib": 12454.5,
      "policy_gate_passes": 17,
      "preflight_cases": 0,
      "profile_sha256": "f4876b4154dfed25382bba4eaf3e2a31c638297284c0118b373ea90cbc425df8",
      "solved": 14,
      "task_s": 476.023893529,
      "tasks": 18
    }
  }
}
```

</details>
