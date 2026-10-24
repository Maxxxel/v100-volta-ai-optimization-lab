# Public audit excerpt

Original SHA256: `cfd5146d112f57f69bd05c41e793bba6df3e44cb16f0555ae4c7730a832a4e02`

Original file: `RESULTS.json`; 40327 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.6661701915,
              "format_passes": 2,
              "gpu_energy_j": 177.52972392640066,
              "semantic_passes": 2,
              "tokens_per_s": 79.33683740119179,
              "ttft_s": 0.12419021150000001
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.659025904,
              "format_passes": 0,
              "gpu_energy_j": 453.7420575960624,
              "semantic_passes": 0,
              "tokens_per_s": 79.60057246057747,
              "ttft_s": 0.062804954
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2381583615,
              "format_passes": 2,
              "gpu_energy_j": 58.95318515515257,
              "semantic_passes": 2,
              "tokens_per_s": 78.13909707262057,
              "ttft_s": 0.07177580750000001
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.24161948049999998,
              "format_passes": 0,
              "gpu_energy_j": 62.803669928399174,
              "semantic_passes": 0,
              "tokens_per_s": 77.50875155718387,
              "ttft_s": 0.125507918
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.182537001,
              "format_passes": 2,
              "gpu_energy_j": 41.90410608060948,
              "semantic_passes": 2,
              "tokens_per_s": 77.32212850569803,
              "ttft_s": 0.06608571799999999
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3579345995,
              "format_passes": 0,
              "gpu_energy_j": 90.16193644952435,
              "semantic_passes": 0,
              "tokens_per_s": 78.86311235735701,
              "ttft_s": 0.07892139249999999
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.468894166,
              "format_passes": 0,
              "gpu_energy_j": 118.06967898589164,
              "semantic_passes": 2,
              "tokens_per_s": 79.13893209236247,
              "ttft_s": 0.11505750949999999
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.078892849,
              "format_passes": 2,
              "gpu_energy_j": 289.6739791030923,
              "semantic_passes": 2,
              "tokens_per_s": 77.81965081863444,
              "ttft_s": 0.8218339415
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23317736449999998,
              "format_passes": 0,
              "gpu_energy_j": 58.358754766732375,
              "semantic_passes": 0,
              "tokens_per_s": 78.41198784714314,
              "ttft_s": 0.0673357815
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.1990610465,
              "format_passes": 0,
              "gpu_energy_j": 47.92459388926005,
              "semantic_passes": 0,
              "tokens_per_s": 2550.6077765395885,
              "ttft_s": 0.19889141
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.718276796,
              "format_passes": 0,
              "gpu_energy_j": 190.87770707181608,
              "semantic_passes": 0,
              "tokens_per_s": 2856.2814382803535,
              "ttft_s": 0.718049627
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.417946039,
              "format_passes": 0,
              "gpu_energy_j": 384.74964534817246,
              "semantic_passes": 0,
              "tokens_per_s": 2892.210829271711,
              "ttft_s": 1.417618622
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.294820863,
              "format_passes": 2,
              "gpu_energy_j": 72.72774604925561,
              "semantic_passes": 2,
              "tokens_per_s": 78.68023504296615,
              "ttft_s": 0.0786937735
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35273944700000004,
              "format_passes": 2,
              "gpu_energy_j": 86.98407476504875,
              "semantic_passes": 2,
              "tokens_per_s": 78.81759387177745,
              "ttft_s": 0.073543888
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3691365335,
              "format_passes": 2,
              "gpu_energy_j": 93.39819501954652,
              "semantic_passes": 2,
              "tokens_per_s": 78.83556499289347,
              "ttft_s": 0.0773835375
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.619968591,
              "format_passes": 0,
              "gpu_energy_j": 162.13470935912034,
              "semantic_passes": 0,
              "tokens_per_s": 78.95181503316547,
              "ttft_s": 0.318999673
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5609366705000001,
              "format_passes": 0,
              "gpu_energy_j": 147.58220319602952,
              "semantic_passes": 0,
              "tokens_per_s": 78.72543539463874,
              "ttft_s": 0.255976479
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
              "e2e_s": 0.6643380605,
              "format_passes": 2,
              "gpu_energy_j": 173.55578983813723,
              "semantic_passes": 2,
              "tokens_per_s": 79.62352106470931
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.653623354,
              "format_passes": 0,
              "gpu_energy_j": 459.13062871724856,
              "semantic_passes": 0,
              "tokens_per_s": 79.880073443892
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2373372775,
              "format_passes": 2,
              "gpu_energy_j": 59.498133241401305,
              "semantic_passes": 2,
              "tokens_per_s": 78.42238707557448
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2410126625,
              "format_passes": 0,
              "gpu_energy_j": 61.11823179576514,
              "semantic_passes": 0,
              "tokens_per_s": 77.89006800827507
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1823197805,
              "format_passes": 2,
              "gpu_energy_j": 40.78145812846033,
              "semantic_passes": 2,
              "tokens_per_s": 77.40798826045483
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35751088649999996,
              "format_passes": 0,
              "gpu_energy_j": 91.63526631138447,
              "semantic_passes": 0,
              "tokens_per_s": 78.89801812423522
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4694523105,
              "format_passes": 0,
              "gpu_energy_j": 117.5490579559501,
              "semantic_passes": 2,
              "tokens_per_s": 79.39591220391621
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.08344768,
              "format_passes": 2,
              "gpu_energy_j": 292.0096129538333,
              "semantic_passes": 2,
              "tokens_per_s": 77.76002125250416
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23281338699999998,
              "format_passes": 0,
              "gpu_energy_j": 57.42166589931536,
              "semantic_passes": 0,
              "tokens_per_s": 78.57195945707693
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.1992113855,
              "format_passes": 0,
              "gpu_energy_j": 48.00623218993019,
              "semantic_passes": 0,
              "tokens_per_s": 2550.0287719646167
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7184022445,
              "format_passes": 0,
              "gpu_energy_j": 191.18227220775566,
              "semantic_passes": 0,
              "tokens_per_s": 2856.296187217384
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4195790835,
              "format_passes": 0,
              "gpu_energy_j": 382.46168067551605,
              "semantic_passes": 0,
              "tokens_per_s": 2889.3664002653463
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.294926413,
              "format_passes": 2,
              "gpu_energy_j": 72.2952751727744,
              "semantic_passes": 2,
              "tokens_per_s": 78.94019066369665
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3521652105,
              "format_passes": 2,
              "gpu_energy_j": 91.22506238773705,
              "semantic_passes": 2,
              "tokens_per_s": 78.94150634304829
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.368129974,
              "format_passes": 2,
              "gpu_energy_j": 91.41233270986109,
              "semantic_passes": 2,
              "tokens_per_s": 79.18285182022923
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6196096275,
              "format_passes": 0,
              "gpu_energy_j": 164.29912157509557,
              "semantic_passes": 0,
              "tokens_per_s": 79.20042703642633
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5595331555,
              "format_passes": 0,
              "gpu_energy_j": 144.93390125220964,
              "semantic_passes": 0,
              "tokens_per_s": 79.14366616628246
            }
          }
        }
      },
      "comparison": {
        "format_pass_change": 0,
        "note": "Existing baseline errors do not suppress speed results. Two starts per arm; no independent confirmation claimed.",
        "quality_pass_change": 0,
        "status": "DESCRIPTIVE_COMPARISON",
        "tasks": {
          "code": {
            "e2e_change_pct": -0.275024464225071,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.2384612561617723,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.3613500019767901
          },
          "decode": {
            "e2e_change_pct": -0.32564590986638997,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.187584670844699,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.3511293633635004
          },
          "energy": {
            "e2e_change_pct": -0.34476387678707976,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.9243742892170337,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.3625457851024638
          },
          "filtering": {
            "e2e_change_pct": -0.25114614051162665,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.683661853766761,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.49196567281808434
          },
          "german": {
            "e2e_change_pct": -0.11900080466425988,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.679088178112077,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.11104163376784992
          },
          "ha_sim": {
            "e2e_change_pct": -0.11837721209180252,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.634092966364964,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.044261208865359336
          },
          "jarvis_memory": {
            "e2e_change_pct": 0.1190342172011638,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.4409438853507419,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.3247202164085694
          },
          "long_context": {
            "e2e_change_pct": 0.4221764009485929,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.8062974306400461,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.0766253324231081
          },
          "math": {
            "e2e_change_pct": -0.15609469674746634,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.6057382841061063,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.20401422579114925
          },
          "prefill": {
            "e2e_change_pct": 0.07552406793962518,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.17034740212671373,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.02270065120546505
          },
          "prefill2048": {
            "e2e_change_pct": 0.017465202927136048,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.15956034919519801,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.0005163684794196044
          },
          "prefill4096": {
            "e2e_change_pct": 0.11516972120826363,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.5946632310956268,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.09834791356068129
          },
          "pve_sim": {
            "e2e_change_pct": 0.03580140120544861,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.5946435851158172,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.33039507391983136
          },
          "sorting": {
            "e2e_change_pct": -0.16279338896849627,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.8755908873475695,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.1572142274127497
          },
          "time": {
            "e2e_change_pct": -0.27267945831753737,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.12623199974028,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.4405205028556125
          },
          "tool-call": {
            "e2e_change_pct": -0.057900271918776,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.334946862723374,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.3148908016318952
          },
          "tool-final": {
            "e2e_change_pct": -0.25020917223133043,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.79445887543922,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.5312524085096415
          }
        }
      },
      "complete": true
    }
  }
}
```

</details>
