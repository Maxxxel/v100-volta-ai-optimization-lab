# Public audit excerpt

Original SHA256: `e8381f970f1ac60c7afa1398e2e76cf3f02aa52eaf88f046a11a5553224eebc3`

Original file: `RESULTS.json`; 59508 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
          "format_passes": 32,
          "quality_attempts": 48,
          "quality_passes": 36,
          "tasks": {
            "code": {
              "attempts": 4,
              "complete": 4,
              "e2e_s": 0.665888072,
              "format_passes": 4,
              "gpu_energy_j": 176.70727583911088,
              "semantic_passes": 4,
              "tokens_per_s": 79.34509194436885,
              "ttft_s": 0.12386921249999999
            },
            "concurrent-decode": {
              "attempts": 48,
              "complete": 48,
              "e2e_s": 4.215682054,
              "format_passes": 0,
              "semantic_passes": 0,
              "tokens_per_s": 79.48722602877297,
              "ttft_s": 2.6168991
            },
            "concurrent-quality": {
              "attempts": 48,
              "complete": 48,
              "e2e_s": 0.955844879,
              "format_passes": 0,
              "semantic_passes": 0,
              "tokens_per_s": 78.54845226229824,
              "ttft_s": 0.7263983970000001
            },
            "decode": {
              "attempts": 12,
              "complete": 12,
              "e2e_s": 1.6592325065,
              "format_passes": 0,
              "gpu_energy_j": 461.38999642179834,
              "semantic_passes": 0,
              "tokens_per_s": 79.59151383150297,
              "ttft_s": 0.0632300485
            },
            "energy": {
              "attempts": 4,
              "complete": 4,
              "e2e_s": 0.23785367400000001,
              "format_passes": 4,
              "gpu_energy_j": 56.46536319551626,
              "semantic_passes": 4,
              "tokens_per_s": 78.27554112860298,
              "ttft_s": 0.071804069
            },
            "filtering": {
              "attempts": 4,
              "complete": 4,
              "e2e_s": 0.241699476,
              "format_passes": 0,
              "gpu_energy_j": 61.92366133959899,
              "semantic_passes": 0,
              "tokens_per_s": 77.50703754050312,
              "ttft_s": 0.12551583
            },
            "german": {
              "attempts": 4,
              "complete": 4,
              "e2e_s": 0.182699517,
              "format_passes": 4,
              "gpu_energy_j": 42.912550564476,
              "semantic_passes": 4,
              "tokens_per_s": 77.2810837262448,
              "ttft_s": 0.0663882235
            },
            "ha_sim": {
              "attempts": 4,
              "complete": 4,
              "e2e_s": 0.35793240449999997,
              "format_passes": 0,
              "gpu_energy_j": 92.39894556475649,
              "semantic_passes": 0,
              "tokens_per_s": 78.82098352331091,
              "ttft_s": 0.07886053500000001
            },
            "jarvis_memory": {
              "attempts": 4,
              "complete": 4,
              "e2e_s": 0.46937261,
              "format_passes": 0,
              "gpu_energy_j": 118.26343691553953,
              "semantic_passes": 4,
              "tokens_per_s": 79.01594978838409,
              "ttft_s": 0.11518412950000001
            },
            "long_context": {
              "attempts": 4,
              "complete": 4,
              "e2e_s": 1.081444661,
              "format_passes": 4,
              "gpu_energy_j": 290.31100554567746,
              "semantic_passes": 4,
              "tokens_per_s": 77.99917751080591,
              "ttft_s": 0.8249572025
            },
            "math": {
              "attempts": 4,
              "complete": 4,
              "e2e_s": 0.233558247,
              "format_passes": 0,
              "gpu_energy_j": 56.33012985236101,
              "semantic_passes": 0,
              "tokens_per_s": 78.28921343508478,
              "ttft_s": 0.067382255
            },
            "prefill": {
              "attempts": 12,
              "complete": 12,
              "e2e_s": 0.199373448,
              "format_passes": 0,
              "gpu_energy_j": 48.67357541870932,
              "semantic_passes": 0,
              "tokens_per_s": 2546.4217778446136,
              "ttft_s": 0.19923866299999998
            },
            "prefill2048": {
              "attempts": 12,
              "complete": 12,
              "e2e_s": 0.7210766425,
              "format_passes": 0,
              "gpu_energy_j": 190.406322766982,
              "semantic_passes": 0,
              "tokens_per_s": 2845.1834310630397,
              "ttft_s": 0.7208280755
            },
            "prefill4096": {
              "attempts": 12,
              "complete": 12,
              "e2e_s": 1.4231923210000001,
              "format_passes": 0,
              "gpu_energy_j": 385.1161608347818,
              "semantic_passes": 0,
              "tokens_per_s": 2881.4814886447243,
              "ttft_s": 1.4228684165
            },
            "pve_sim": {
              "attempts": 4,
              "complete": 4,
              "e2e_s": 0.295304554,
              "format_passes": 4,
              "gpu_energy_j": 74.77066848169287,
              "semantic_passes": 4,
              "tokens_per_s": 78.53590828027794,
              "ttft_s": 0.07902387550000001
            },
            "sorting": {
              "attempts": 4,
              "complete": 4,
              "e2e_s": 0.3532014365,
              "format_passes": 4,
              "gpu_energy_j": 90.0089135687248,
              "semantic_passes": 4,
              "tokens_per_s": 78.77413242484349,
              "ttft_s": 0.073965383
            },
            "time": {
              "attempts": 4,
              "complete": 4,
              "e2e_s": 0.36926634449999995,
              "format_passes": 4,
              "gpu_energy_j": 94.95532887061455,
              "semantic_passes": 4,
              "tokens_per_s": 78.89872012344746,
              "ttft_s": 0.0776594565
            },
            "tool-call": {
              "attempts": 12,
              "complete": 12,
              "e2e_s": 0.6214610225,
              "format_passes": 0,
              "gpu_energy_j": 164.36035865581883,
              "semantic_passes": 0,
              "tokens_per_s": 78.88329960040795,
              "ttft_s": 0.319968158
            },
            "tool-final": {
              "attempts": 12,
              "complete": 12,
              "e2e_s": 0.5622156075,
              "format_passes": 0,
              "gpu_energy_j": 145.60616964616207,
              "semantic_passes": 0,
              "tokens_per_s": 78.77221633914652,
              "ttft_s": 0.2570356885
            }
          }
        },
        "B": {
          "format_passes": 32,
          "quality_attempts": 48,
          "quality_passes": 36,
          "tasks": {
            "code": {
              "attempts": 4,
              "complete": 4,
              "e2e_s": 0.6670234500000001,
              "format_passes": 4,
              "gpu_energy_j": 181.20720320756737,
              "semantic_passes": 4,
              "tokens_per_s": 79.22325427391937,
              "ttft_s": 0.1238923005
            },
            "concurrent-decode": {
              "attempts": 48,
              "complete": 48,
              "e2e_s": 3.1599214900000003,
              "format_passes": 0,
              "semantic_passes": 0,
              "tokens_per_s": 65.96162232001603,
              "ttft_s": 1.2330864860000001
            },
            "concurrent-quality": {
              "attempts": 48,
              "complete": 48,
              "e2e_s": 0.942228091,
              "format_passes": 0,
              "semantic_passes": 0,
              "tokens_per_s": 58.80534641668515,
              "ttft_s": 0.4063537485
            },
            "decode": {
              "attempts": 12,
              "complete": 12,
              "e2e_s": 1.687323493,
              "format_passes": 0,
              "gpu_energy_j": 470.66020409122825,
              "semantic_passes": 0,
              "tokens_per_s": 78.41786987574848,
              "ttft_s": 0.06744301450000001
            },
            "energy": {
              "attempts": 4,
              "complete": 4,
              "e2e_s": 0.23836608799999998,
              "format_passes": 4,
              "gpu_energy_j": 60.35116769355085,
              "semantic_passes": 4,
              "tokens_per_s": 78.04106221711129,
              "ttft_s": 0.071719644
            },
            "filtering": {
              "attempts": 4,
              "complete": 4,
              "e2e_s": 0.2450971865,
              "format_passes": 0,
              "gpu_energy_j": 63.19162119390391,
              "semantic_passes": 0,
              "tokens_per_s": 77.06964810624656,
              "ttft_s": 0.12829696299999999
            },
            "german": {
              "attempts": 4,
              "complete": 4,
              "e2e_s": 0.18052758800000002,
              "format_passes": 4,
              "gpu_energy_j": 42.43215029806262,
              "semantic_passes": 4,
              "tokens_per_s": 77.37479252203048,
              "ttft_s": 0.06392877050000001
            },
            "ha_sim": {
              "attempts": 4,
              "complete": 4,
              "e2e_s": 0.3617456865,
              "format_passes": 0,
              "gpu_energy_j": 90.35720657380482,
              "semantic_passes": 0,
              "tokens_per_s": 78.5476689851174,
              "ttft_s": 0.07879780850000001
            },
            "jarvis_memory": {
              "attempts": 4,
              "complete": 4,
              "e2e_s": 0.4698846625,
              "format_passes": 0,
              "gpu_energy_j": 120.68468072240353,
              "semantic_passes": 4,
              "tokens_per_s": 78.92419216756056,
              "ttft_s": 0.1150366605
            },
            "long_context": {
              "attempts": 4,
              "complete": 4,
              "e2e_s": 1.084239632,
              "format_passes": 4,
              "gpu_energy_j": 291.45191134336255,
              "semantic_passes": 4,
              "tokens_per_s": 77.75136934731123,
              "ttft_s": 0.8269622625
            },
            "math": {
              "attempts": 4,
              "complete": 4,
              "e2e_s": 0.236923761,
              "format_passes": 0,
              "gpu_energy_j": 56.87203065672263,
              "semantic_passes": 0,
              "tokens_per_s": 78.01565316110447,
              "ttft_s": 0.069869408
            },
            "prefill": {
              "attempts": 12,
              "complete": 12,
              "e2e_s": 0.21313080499999998,
              "format_passes": 0,
              "gpu_energy_j": 51.35541146886037,
              "semantic_passes": 0,
              "tokens_per_s": 2381.211548687027,
              "ttft_s": 0.212993539
            },
            "prefill2048": {
              "attempts": 12,
              "complete": 12,
              "e2e_s": 0.7257481065,
              "format_passes": 0,
              "gpu_energy_j": 193.25089282852474,
              "semantic_passes": 0,
              "tokens_per_s": 2826.7910551357318,
              "ttft_s": 0.725494184
            },
            "prefill4096": {
              "attempts": 12,
              "complete": 12,
              "e2e_s": 1.437787368,
              "format_passes": 0,
              "gpu_energy_j": 388.4693840920494,
              "semantic_passes": 0,
              "tokens_per_s": 2852.523737683725,
              "ttft_s": 1.4374290545
            },
            "pve_sim": {
              "attempts": 4,
              "complete": 4,
              "e2e_s": 0.29559036699999997,
              "format_passes": 4,
              "gpu_energy_j": 75.06534418221656,
              "semantic_passes": 4,
              "tokens_per_s": 78.56095027377731,
              "ttft_s": 0.0792065195
            },
            "sorting": {
              "attempts": 4,
              "complete": 4,
              "e2e_s": 0.3565795745,
              "format_passes": 4,
              "gpu_energy_j": 91.89581744155672,
              "semantic_passes": 4,
              "tokens_per_s": 78.06693024785028,
              "ttft_s": 0.074901131
            },
            "time": {
              "attempts": 4,
              "complete": 4,
              "e2e_s": 0.370303728,
              "format_passes": 4,
              "gpu_energy_j": 95.4897605224303,
              "semantic_passes": 4,
              "tokens_per_s": 78.75471729981203,
              "ttft_s": 0.078118962
            },
            "tool-call": {
              "attempts": 12,
              "complete": 12,
              "e2e_s": 0.621546892,
              "format_passes": 0,
              "gpu_energy_j": 167.5606843003341,
              "semantic_passes": 0,
              "tokens_per_s": 78.8082566252966,
              "ttft_s": 0.3200500255
            },
            "tool-final": {
              "attempts": 12,
              "complete": 12,
              "e2e_s": 0.562086641,
              "format_passes": 0,
              "gpu_energy_j": 148.46880084026606,
              "semantic_passes": 0,
              "tokens_per_s": 78.69123858347992,
              "ttft_s": 0.2574635765
            }
          }
        }
      },
      "change_exercised": true,
      "comparison": {
        "format_pass_change": 0,
        "note": "Existing baseline errors do not suppress speed results. Two starts per arm; no independent confirmation claimed.",
        "quality_pass_change": 0,
        "status": "DESCRIPTIVE_COMPARISON",
        "tasks": {
          "code": {
            "e2e_change_pct": 0.17050583239761608,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.5465433424221917,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.1535541360704551,
            "ttft_change_pct": 0.01863901411338631
          },
          "concurrent-decode": {
            "e2e_change_pct": -25.043647753232577,
            "format_pass_change": 0,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -17.01607212190409,
            "ttft_change_pct": -52.879861283149964
          },
          "concurrent-quality": {
            "e2e_change_pct": -1.4245813624325532,
            "format_pass_change": 0,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -25.134939361611597,
            "ttft_change_pct": -44.0591072091807
          },
          "decode": {
            "e2e_change_pct": 1.6930108583308456,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.0091913004882667,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.4745842857557867,
            "ttft_change_pct": 6.662917552562075
          },
          "energy": {
            "e2e_change_pct": 0.21543245112958243,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 6.881748877767158,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.29955578474565314,
            "ttft_change_pct": -0.11757690222262696
          },
          "filtering": {
            "e2e_change_pct": 1.4057583227859327,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.047617706826532,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.5643222191636377,
            "ttft_change_pct": 2.215762744826688
          },
          "german": {
            "e2e_change_pct": -1.188798435630234,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.1194866305874185,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.1212570932850987,
            "ttft_change_pct": -3.704652527718244
          },
          "ha_sim": {
            "e2e_change_pct": 1.065363725680779,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.2096994489193,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.3467535242219988,
            "ttft_change_pct": -0.07954105307552695
          },
          "jarvis_memory": {
            "e2e_change_pct": 0.10909296560785986,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.0473308319232997,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.11612544184973483,
            "ttft_change_pct": -0.12802892259563547
          },
          "long_context": {
            "e2e_change_pct": 0.2584478985189653,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.39299433224744273,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.3177061238374579,
            "ttft_change_pct": 0.24305018417001278
          },
          "math": {
            "e2e_change_pct": 1.440974165215425,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.9620087966811353,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.34942268797620857,
            "ttft_change_pct": 3.691109773634005
          },
          "prefill": {
            "e2e_change_pct": 6.900295469635442,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 5.509839840366837,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -6.487936546687356,
            "ttft_change_pct": 6.903718280823856
          },
          "prefill2048": {
            "e2e_change_pct": 0.6478456969295054,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.493947270345597,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.6464390213476001,
            "ttft_change_pct": 0.6473261320687707
          },
          "prefill4096": {
            "e2e_change_pct": 1.0255147378637197,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.8707043739735854,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.0049605064309963,
            "ttft_change_pct": 1.0233299039567045
          },
          "pve_sim": {
            "e2e_change_pct": 0.09678584232060139,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.39410601310305715,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.0318860430186918,
            "ttft_change_pct": 0.23112508573437385
          },
          "sorting": {
            "e2e_change_pct": 0.9564338224315128,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.0963522367051013,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.8977593979444087,
            "ttft_change_pct": 1.2651161422364332
          },
          "time": {
            "e2e_change_pct": 0.2809309636394586,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.5628242860850508,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.1825160451400465,
            "ttft_change_pct": 0.5916929125044712
          },
          "tool-call": {
            "e2e_change_pct": 0.013817358915702016,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.9471396087769266,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.09513163811795122,
            "ttft_change_pct": 0.025586139730826574
          },
          "tool-final": {
            "e2e_change_pct": -0.022938975417885477,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.9660095455161564,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.1027998949756137,
            "ttft_change_pct": 0.16647026819389676
          }
        }
      },
      "complete": true,
      "concurrency": {
        "aggregate_throughput_change_pct": 60.46885451633584,
        "arms": {
          "A": {
            "active_slots_max": 1,
            "aggregate_tokens_per_s": 76.30105831648278,
            "exact_serial_matches": 48,
            "exercised": true,
            "marker_passes": 48,
            "offered_load": 4,
            "parallel_format_passes": 32,
            "parallel_quality_attempts": 48,
            "parallel_quality_passes": 36,
            "request_e2e_s": 4.215682054,
            "wave_elapsed_s": 6.7102608235000005,
            "waves": 12
          },
          "B": {
            "active_slots_max": 2,
            "aggregate_tokens_per_s": 122.43943426430131,
            "exact_serial_matches": 10,
            "exercised": true,
            "marker_passes": 48,
            "offered_load": 4,
            "parallel_format_passes": 32,
            "parallel_quality_attempts": 48,
            "parallel_quality_passes": 36,
            "request_e2e_s": 3.1599214900000003,
            "wave_elapsed_s": 4.1816593095000005,
            "waves": 12
          }
        },
        "change_exercised": true,
        "note": "Aggregate four-request wall-clock throughput; per-request native throughput and correctness are reported separately. Two starts per arm give preliminary results."
      }
    }
  }
}
```

</details>
