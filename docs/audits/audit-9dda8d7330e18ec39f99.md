# Public audit excerpt

Original SHA256: `9dda8d7330e18ec39f99def00d4e6d2d69ddd8b449317135508334ed51873da0`

Original file: `RESULTS.json`; 48199 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.6677924399999999,
              "format_passes": 2,
              "gpu_energy_j": 179.75425984064262,
              "semantic_passes": 2,
              "tokens_per_s": 79.06999262252762,
              "ttft_s": 0.12392607650000001
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6614945804999999,
              "format_passes": 0,
              "gpu_energy_j": 465.36120324224237,
              "semantic_passes": 0,
              "tokens_per_s": 79.47758121074824,
              "ttft_s": 0.0634407505
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2383268,
              "format_passes": 2,
              "gpu_energy_j": 58.64174472035373,
              "semantic_passes": 2,
              "tokens_per_s": 78.19457632615897,
              "ttft_s": 0.072027615
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2420400205,
              "format_passes": 0,
              "gpu_energy_j": 60.7991398624421,
              "semantic_passes": 0,
              "tokens_per_s": 77.21114141627908,
              "ttft_s": 0.125429738
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.18197597850000002,
              "format_passes": 2,
              "gpu_energy_j": 40.303746179879134,
              "semantic_passes": 2,
              "tokens_per_s": 77.59978357672975,
              "ttft_s": 0.0659759625
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3582328885,
              "format_passes": 0,
              "gpu_energy_j": 87.65026083185572,
              "semantic_passes": 0,
              "tokens_per_s": 78.80446468066884,
              "ttft_s": 0.07906875599999999
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.469356737,
              "format_passes": 0,
              "gpu_energy_j": 117.71975713937472,
              "semantic_passes": 2,
              "tokens_per_s": 79.02494508964892,
              "ttft_s": 0.11502082599999999
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0827276845,
              "format_passes": 2,
              "gpu_energy_j": 289.76098320413047,
              "semantic_passes": 2,
              "tokens_per_s": 77.7913511073474,
              "ttft_s": 0.8255826355
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2340150965,
              "format_passes": 0,
              "gpu_energy_j": 51.126460726202836,
              "semantic_passes": 0,
              "tokens_per_s": 78.01279678680808,
              "ttft_s": 0.067355917
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.19997079550000002,
              "format_passes": 0,
              "gpu_energy_j": 47.71736038749944,
              "semantic_passes": 0,
              "tokens_per_s": 2542.6571984154643,
              "ttft_s": 0.199750029
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7203859355,
              "format_passes": 0,
              "gpu_energy_j": 189.44746502582677,
              "semantic_passes": 0,
              "tokens_per_s": 2848.241238039197,
              "ttft_s": 0.720153151
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4238247574999998,
              "format_passes": 0,
              "gpu_energy_j": 384.1208108531757,
              "semantic_passes": 0,
              "tokens_per_s": 2880.660928099353,
              "ttft_s": 1.423449698
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.29584762200000003,
              "format_passes": 2,
              "gpu_energy_j": 73.88098219391532,
              "semantic_passes": 2,
              "tokens_per_s": 78.49118851500415,
              "ttft_s": 0.0792446285
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.354683792,
              "format_passes": 2,
              "gpu_energy_j": 91.10267989630995,
              "semantic_passes": 2,
              "tokens_per_s": 78.62822397938643,
              "ttft_s": 0.0748854095
            },
            "spec-branch": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.5261550715,
              "format_passes": 0,
              "gpu_energy_j": 1003.2606760617008,
              "semantic_passes": 0,
              "tokens_per_s": 79.40307633785766
            },
            "spec-code": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.5943230235000003,
              "format_passes": 0,
              "gpu_energy_j": 1019.0006557783687,
              "semantic_passes": 0,
              "tokens_per_s": 79.27908964845045
            },
            "spec-repeat": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.408851087,
              "format_passes": 0,
              "gpu_energy_j": 966.6654591567483,
              "semantic_passes": 0,
              "tokens_per_s": 79.46493675267469
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3694670455,
              "format_passes": 2,
              "gpu_energy_j": 94.66221438755434,
              "semantic_passes": 2,
              "tokens_per_s": 78.79865440531282,
              "ttft_s": 0.07756384250000001
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.620945479,
              "format_passes": 0,
              "gpu_energy_j": 160.39875173744832,
              "semantic_passes": 0,
              "tokens_per_s": 78.79344282811363,
              "ttft_s": 0.318883391
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5630407749999999,
              "format_passes": 0,
              "gpu_energy_j": 148.34222668684097,
              "semantic_passes": 0,
              "tokens_per_s": 78.56733788264597,
              "ttft_s": 0.25754323349999997
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
              "e2e_s": 0.6719969525,
              "format_passes": 2,
              "gpu_energy_j": 180.36057070868702,
              "semantic_passes": 2,
              "tokens_per_s": 78.49850478199468,
              "ttft_s": 0.1242009745
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6751311150000001,
              "format_passes": 0,
              "gpu_energy_j": 468.703059234898,
              "semantic_passes": 0,
              "tokens_per_s": 78.8125056723653,
              "ttft_s": 0.06377766
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2404132645,
              "format_passes": 2,
              "gpu_energy_j": 58.90015055940191,
              "semantic_passes": 2,
              "tokens_per_s": 77.38323628398138,
              "ttft_s": 0.0724627865
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.24407172049999998,
              "format_passes": 0,
              "gpu_energy_j": 60.21509552144729,
              "semantic_passes": 0,
              "tokens_per_s": 76.3987009082129,
              "ttft_s": 0.126202115
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1842949015,
              "format_passes": 2,
              "gpu_energy_j": 40.96116683067903,
              "semantic_passes": 2,
              "tokens_per_s": 76.58090535883277,
              "ttft_s": 0.066765486
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.36046365300000005,
              "format_passes": 0,
              "gpu_energy_j": 93.12887631600972,
              "semantic_passes": 0,
              "tokens_per_s": 78.12524060603855,
              "ttft_s": 0.0788168585
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.472445051,
              "format_passes": 0,
              "gpu_energy_j": 119.55191727266381,
              "semantic_passes": 2,
              "tokens_per_s": 78.39647551717444,
              "ttft_s": 0.115308791
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0872113485,
              "format_passes": 2,
              "gpu_energy_j": 292.5005625865199,
              "semantic_passes": 2,
              "tokens_per_s": 77.10902850428545,
              "ttft_s": 0.8277325550000001
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.234881246,
              "format_passes": 0,
              "gpu_energy_j": 56.0764018849345,
              "semantic_passes": 0,
              "tokens_per_s": 77.62801942765044,
              "ttft_s": 0.0673666145
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.200227513,
              "format_passes": 0,
              "gpu_energy_j": 49.29095684936787,
              "semantic_passes": 0,
              "tokens_per_s": 2538.628125299555,
              "ttft_s": 0.200085378
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7225943545,
              "format_passes": 0,
              "gpu_energy_j": 189.58783399877598,
              "semantic_passes": 0,
              "tokens_per_s": 2839.5285860726462,
              "ttft_s": 0.7223399420000001
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.426015101,
              "format_passes": 0,
              "gpu_energy_j": 385.1732803670942,
              "semantic_passes": 0,
              "tokens_per_s": 2876.207564924948,
              "ttft_s": 1.425667659
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.297470327,
              "format_passes": 2,
              "gpu_energy_j": 73.86937023960165,
              "semantic_passes": 2,
              "tokens_per_s": 77.89603966579818,
              "ttft_s": 0.079223238
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3558877705,
              "format_passes": 2,
              "gpu_energy_j": 91.17044266834822,
              "semantic_passes": 2,
              "tokens_per_s": 78.16219920716652,
              "ttft_s": 0.074417979
            },
            "spec-branch": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.648592338,
              "format_passes": 0,
              "gpu_energy_j": 424.20657360323827,
              "semantic_passes": 0,
              "tokens_per_s": 191.2148436077847
            },
            "spec-code": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.8980210245,
              "format_passes": 0,
              "gpu_energy_j": 194.76234955842853,
              "semantic_passes": 0,
              "tokens_per_s": 490.8121708926134
            },
            "spec-repeat": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.3560339205,
              "format_passes": 0,
              "gpu_energy_j": 339.49487282075063,
              "semantic_passes": 0,
              "tokens_per_s": 221.2813838034822
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3767628875,
              "format_passes": 2,
              "gpu_energy_j": 97.60038822891944,
              "semantic_passes": 2,
              "tokens_per_s": 77.6315014987273,
              "ttft_s": 0.08050157499999999
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6264269005,
              "format_passes": 0,
              "gpu_energy_j": 166.13203049434202,
              "semantic_passes": 0,
              "tokens_per_s": 78.06631539837718,
              "ttft_s": 0.3212684835
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5650836735,
              "format_passes": 0,
              "gpu_energy_j": 149.490461104188,
              "semantic_passes": 0,
              "tokens_per_s": 78.04524886858229,
              "ttft_s": 0.2567286465
            }
          }
        }
      },
      "change_exercised": true,
      "comparison": {
        "format_pass_change": 0,
        "note": "Descriptive paired comparison; actual fresh starts per arm: {'A': 2, 'B': 2}. Quality and speed remain separate.",
        "quality_pass_change": 0,
        "status": "DESCRIPTIVE_COMPARISON",
        "tasks": {
          "code": {
            "e2e_change_pct": 0.629613671577367,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.337299860699769,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.7227619752807724,
            "ttft_change_pct": 0.22182417757734552
          },
          "decode": {
            "e2e_change_pct": 0.8207390297894746,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.7181208853192622,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.8368089821699232,
            "ttft_change_pct": 0.5310616557097525
          },
          "energy": {
            "e2e_change_pct": 0.8754636490734491,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.44065168981661795,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.0375911991560516,
            "ttft_change_pct": 0.6041731355397539
          },
          "filtering": {
            "e2e_change_pct": 0.8394066385397414,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.9606128348463638,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.0522322208474488,
            "ttft_change_pct": 0.6157845916890947
          },
          "german": {
            "e2e_change_pct": 1.274301706804648,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.6311651226309731,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.3129910560762403,
            "ttft_change_pct": 1.1966835648665297
          },
          "ha_sim": {
            "e2e_change_pct": 0.6227134837732962,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 6.250540993442022,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.8619106511066899,
            "ttft_change_pct": -0.3185803252045427
          },
          "jarvis_memory": {
            "e2e_change_pct": 0.6579886377555022,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.5563743740312885,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.7952799862898097,
            "ttft_change_pct": 0.25035900889809337
          },
          "long_context": {
            "e2e_change_pct": 0.41410818843801156,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.9454617913342123,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.8771188484956172,
            "ttft_change_pct": 0.2604123933273028
          },
          "math": {
            "e2e_change_pct": 0.3701254803448073,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 9.68175987232922,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.4932233877079861,
            "ttft_change_pct": 0.015882049382542895
          },
          "prefill": {
            "e2e_change_pct": 0.12837749600289605,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.297744152421034,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.15845915518695186,
            "ttft_change_pct": 0.1678843310706224
          },
          "prefill2048": {
            "e2e_change_pct": 0.30656053806314976,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.07409387765102693,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.3058958577732307,
            "ttft_change_pct": 0.30365638155767094
          },
          "prefill4096": {
            "e2e_change_pct": 0.15383518852740696,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.2739944007669859,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.15459518789471272,
            "ttft_change_pct": 0.15581590295155046
          },
          "pve_sim": {
            "e2e_change_pct": 0.5484935079180575,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.01571710874550547,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.7582365109584321,
            "ttft_change_pct": -0.026992996755603738
          },
          "sorting": {
            "e2e_change_pct": 0.33945123153527046,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.07438065720501985,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.5926940081237064,
            "ttft_change_pct": -0.624194356578911
          },
          "spec-branch": {
            "e2e_change_pct": -53.246743136038496,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -57.71721311070807,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 140.81540971305873
          },
          "spec-code": {
            "e2e_change_pct": -75.01557265085358,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -80.88692598439415,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 519.0941054810744
          },
          "spec-repeat": {
            "e2e_change_pct": -60.22020657718452,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -64.87979687234275,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 178.46417910353924
          },
          "time": {
            "e2e_change_pct": 1.9746935725015735,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.1038507395738657,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.4811838037006142,
            "ttft_change_pct": 3.7875025337998025
          },
          "tool-call": {
            "e2e_change_pct": 0.8827540718756133,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.5743911313464105,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.9228273364354167,
            "ttft_change_pct": 0.7479513098880508
          },
          "tool-final": {
            "e2e_change_pct": 0.3628331358417336,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.7740442104668066,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.6645115236607713,
            "ttft_change_pct": -0.316291361621035
          }
        }
      },
      "complete": true,
      "speculation": {
        "arms": {
          "A": {
            "accepted_n": 0,
            "checkpoint_events": 0,
            "draft_n": 0,
            "median_e2e_s": 3.5609658375000004,
            "restore_events": 0,
            "starts": 2
          },
          "B": {
            "acceptance_pct": 88.46708313310909,
            "accepted_n": 3682,
            "checkpoint_events": 114,
            "draft_n": 4162,
            "median_e2e_s": 1.515089286,
            "restore_events": 28,
            "starts": 2
          }
        },
        "change_exercised": true,
        "note": "Token drift is reported separately from semantic quality and protocol validity. No draft is inactivity, not an optimization gain. Internal RAM checkpoint trace is not a new model checkpoint."
      }
    }
  }
}
```

</details>
