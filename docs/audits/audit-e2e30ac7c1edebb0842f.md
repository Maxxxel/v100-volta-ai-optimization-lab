# Public audit excerpt

Original SHA256: `e2e30ac7c1edebb0842f2b83e697bd783d399890eeb8efa206a45a890abc7e31`

Original file: `RESULTS.json`; 48119 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "models": {
    "omnicoder2": {
      "arms": {
        "A": {
          "format_passes": 16,
          "quality_attempts": 24,
          "quality_passes": 18,
          "tasks": {
            "code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.666332776,
              "format_passes": 2,
              "gpu_energy_j": 177.23237063994475,
              "semantic_passes": 2,
              "tokens_per_s": 79.31787287524361,
              "ttft_s": 0.124170025
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.660357969,
              "format_passes": 0,
              "gpu_energy_j": 458.68296812912274,
              "semantic_passes": 0,
              "tokens_per_s": 79.52945977532525,
              "ttft_s": 0.0631974945
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.237990234,
              "format_passes": 2,
              "gpu_energy_j": 56.716106165179475,
              "semantic_passes": 2,
              "tokens_per_s": 78.2998100583095,
              "ttft_s": 0.07193707299999999
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.24163202150000002,
              "format_passes": 0,
              "gpu_energy_j": 55.735386267286714,
              "semantic_passes": 0,
              "tokens_per_s": 77.63573735151647,
              "ttft_s": 0.12561257799999997
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.18248658699999998,
              "format_passes": 2,
              "gpu_energy_j": 39.876948164552225,
              "semantic_passes": 2,
              "tokens_per_s": 77.46254141541506,
              "ttft_s": 0.06622502
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35795968499999997,
              "format_passes": 0,
              "gpu_energy_j": 86.45327575328938,
              "semantic_passes": 0,
              "tokens_per_s": 78.88386879633563,
              "ttft_s": 0.0790012715
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.47107487000000003,
              "format_passes": 0,
              "gpu_energy_j": 117.52575155593681,
              "semantic_passes": 2,
              "tokens_per_s": 78.76146285870662,
              "ttft_s": 0.1155614425
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.081891878,
              "format_passes": 2,
              "gpu_energy_j": 290.1263293825864,
              "semantic_passes": 2,
              "tokens_per_s": 77.99426237081474,
              "ttft_s": 0.8254306645
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23337729899999998,
              "format_passes": 0,
              "gpu_energy_j": 55.683037627606325,
              "semantic_passes": 0,
              "tokens_per_s": 78.33276816063457,
              "ttft_s": 0.06737760849999999
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.20006502199999998,
              "format_passes": 0,
              "gpu_energy_j": 48.81805449905731,
              "semantic_passes": 0,
              "tokens_per_s": 2537.4986359011596,
              "ttft_s": 0.199928185
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.721190486,
              "format_passes": 0,
              "gpu_energy_j": 189.08067340837334,
              "semantic_passes": 0,
              "tokens_per_s": 2844.5380700064807,
              "ttft_s": 0.7209689324999999
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4276482905,
              "format_passes": 0,
              "gpu_energy_j": 381.29830575680376,
              "semantic_passes": 0,
              "tokens_per_s": 2872.6578419783273,
              "ttft_s": 1.427344643
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.295442522,
              "format_passes": 2,
              "gpu_energy_j": 74.73808374793958,
              "semantic_passes": 2,
              "tokens_per_s": 78.54262030170821,
              "ttft_s": 0.078970812
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3536369515,
              "format_passes": 2,
              "gpu_energy_j": 88.26127245317225,
              "semantic_passes": 2,
              "tokens_per_s": 78.69884559181682,
              "ttft_s": 0.074093138
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.369672311,
              "format_passes": 2,
              "gpu_energy_j": 95.13268891530296,
              "semantic_passes": 2,
              "tokens_per_s": 78.79293722069468,
              "ttft_s": 0.077702888
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6192541975000001,
              "format_passes": 0,
              "gpu_energy_j": 166.54581206734525,
              "semantic_passes": 0,
              "tokens_per_s": 79.05981119291002,
              "ttft_s": 0.318302939
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.56120418,
              "format_passes": 0,
              "gpu_energy_j": 148.1385314848375,
              "semantic_passes": 0,
              "tokens_per_s": 78.83262299647444,
              "ttft_s": 0.2564130025
            }
          }
        },
        "B": {
          "format_passes": 16,
          "quality_attempts": 24,
          "quality_passes": 18,
          "tasks": {
            "code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.666818741,
              "format_passes": 2,
              "gpu_energy_j": 176.9154607681209,
              "semantic_passes": 2,
              "tokens_per_s": 79.24029718134693,
              "ttft_s": 0.1241304735
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.661031034,
              "format_passes": 0,
              "gpu_energy_j": 463.6941798258056,
              "semantic_passes": 0,
              "tokens_per_s": 79.49566018334568,
              "ttft_s": 0.06309513750000001
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2380171425,
              "format_passes": 2,
              "gpu_energy_j": 60.21229537644216,
              "semantic_passes": 2,
              "tokens_per_s": 78.23951429292373,
              "ttft_s": 0.0718273035
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2421069455,
              "format_passes": 0,
              "gpu_energy_j": 61.04385689133998,
              "semantic_passes": 0,
              "tokens_per_s": 77.61345148560525,
              "ttft_s": 0.1260945385
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.183199218,
              "format_passes": 2,
              "gpu_energy_j": 40.58311016750932,
              "semantic_passes": 2,
              "tokens_per_s": 77.33387596145059,
              "ttft_s": 0.0667619095
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.359227388,
              "format_passes": 0,
              "gpu_energy_j": 91.32065538424607,
              "semantic_passes": 0,
              "tokens_per_s": 78.69308979897582,
              "ttft_s": 0.0795844595
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.469427397,
              "format_passes": 0,
              "gpu_energy_j": 120.78426619395302,
              "semantic_passes": 2,
              "tokens_per_s": 79.14462922743036,
              "ttft_s": 0.1155991295
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0822369200000002,
              "format_passes": 2,
              "gpu_energy_j": 288.25113296931454,
              "semantic_passes": 2,
              "tokens_per_s": 78.04029788236824,
              "ttft_s": 0.825915279
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2333357755,
              "format_passes": 0,
              "gpu_energy_j": 53.839864658620314,
              "semantic_passes": 0,
              "tokens_per_s": 78.40370197292737,
              "ttft_s": 0.0674572645
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.1996264525,
              "format_passes": 0,
              "gpu_energy_j": 48.76745341875679,
              "semantic_passes": 0,
              "tokens_per_s": 2543.596328937806,
              "ttft_s": 0.1994603725
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7209023175,
              "format_passes": 0,
              "gpu_energy_j": 191.09092985063583,
              "semantic_passes": 0,
              "tokens_per_s": 2845.842622323596,
              "ttft_s": 0.7206674534999999
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4216926685,
              "format_passes": 0,
              "gpu_energy_j": 382.58682991058276,
              "semantic_passes": 0,
              "tokens_per_s": 2884.446282507439,
              "ttft_s": 1.421367807
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2956188735,
              "format_passes": 2,
              "gpu_energy_j": 72.42862238502792,
              "semantic_passes": 2,
              "tokens_per_s": 78.70990846818574,
              "ttft_s": 0.079608817
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35348264949999997,
              "format_passes": 2,
              "gpu_energy_j": 86.20003605530405,
              "semantic_passes": 2,
              "tokens_per_s": 78.75015097301493,
              "ttft_s": 0.074029075
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.369389014,
              "format_passes": 2,
              "gpu_energy_j": 95.88848678518438,
              "semantic_passes": 2,
              "tokens_per_s": 78.92321523101415,
              "ttft_s": 0.0778872915
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6214217805,
              "format_passes": 0,
              "gpu_energy_j": 164.84094472741657,
              "semantic_passes": 0,
              "tokens_per_s": 78.92598540802743,
              "ttft_s": 0.31889948749999997
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5625809424999999,
              "format_passes": 0,
              "gpu_energy_j": 149.16132728706134,
              "semantic_passes": 0,
              "tokens_per_s": 78.57656267728912,
              "ttft_s": 0.25704258550000003
            }
          }
        }
      },
      "change_exercised": false,
      "complete": true,
      "diagnostic_only": true,
      "hardware_diagnostic": [
        {
          "after_start_index": 1,
          "begin_ns": 410161773543303,
          "end_ns": 410168272581517,
          "exec_gate_ns": 410163598104282,
          "model": "omnicoder2",
          "owned_host_pid": 277583,
          "registration": {
            "at_ns": 410163469974841,
            "pid": 233330
          },
          "returncode": 0,
          "runtime_gate_ns": 410163755189782,
          "runtime_ready": {
            "pid": 233330
          },
          "schema": 1
        }
      ],
      "speed_gain_qualified": false
    }
  }
}
```

</details>
