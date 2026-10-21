# Public audit excerpt

Original SHA256: `9570ac8fc6dfdcbfd5ed4bea7fcacf79758c410cd838b83e7fd32c2e96babab2`

Original file: `RESULTS.json`; 48195 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{}
```

## Selected aggregate measurements

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
              "e2e_s": 0.6675256350000001,
              "format_passes": 2,
              "gpu_energy_j": 179.28727855453113,
              "semantic_passes": 2,
              "tokens_per_s": 79.13026297063345,
              "ttft_s": 0.124125972
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6627909585,
              "format_passes": 0,
              "gpu_energy_j": 462.2280789848471,
              "semantic_passes": 0,
              "tokens_per_s": 79.39415431670511,
              "ttft_s": 0.0631594455
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23798889750000002,
              "format_passes": 2,
              "gpu_energy_j": 54.729569512065325,
              "semantic_passes": 2,
              "tokens_per_s": 78.19282295489982,
              "ttft_s": 0.0716917255
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.241925728,
              "format_passes": 0,
              "gpu_energy_j": 59.24276059633844,
              "semantic_passes": 0,
              "tokens_per_s": 77.3752876335554,
              "ttft_s": 0.125608642
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.18231847950000002,
              "format_passes": 2,
              "gpu_energy_j": 38.68803313681562,
              "semantic_passes": 2,
              "tokens_per_s": 77.4523398784799,
              "ttft_s": 0.0661056065
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.357926046,
              "format_passes": 0,
              "gpu_energy_j": 88.68974284035644,
              "semantic_passes": 0,
              "tokens_per_s": 78.85390129796276,
              "ttft_s": 0.07889710050000001
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.470863254,
              "format_passes": 0,
              "gpu_energy_j": 122.34912976673425,
              "semantic_passes": 2,
              "tokens_per_s": 78.81652327365614,
              "ttft_s": 0.115633581
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0862096095,
              "format_passes": 2,
              "gpu_energy_j": 289.6726031322004,
              "semantic_passes": 2,
              "tokens_per_s": 77.71112026768924,
              "ttft_s": 0.8287822505
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23362405149999999,
              "format_passes": 0,
              "gpu_energy_j": 56.108866061721564,
              "semantic_passes": 0,
              "tokens_per_s": 78.29699977792475,
              "ttft_s": 0.06757315650000001
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.200446085,
              "format_passes": 0,
              "gpu_energy_j": 49.13225282359183,
              "semantic_passes": 0,
              "tokens_per_s": 2536.357746025051,
              "ttft_s": 0.20028204700000002
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7219430339999999,
              "format_passes": 0,
              "gpu_energy_j": 190.68983580264774,
              "semantic_passes": 0,
              "tokens_per_s": 2842.3710252700953,
              "ttft_s": 0.7216761174999999
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4237750985,
              "format_passes": 0,
              "gpu_energy_j": 387.6974300065333,
              "semantic_passes": 0,
              "tokens_per_s": 2880.807664701916,
              "ttft_s": 1.4233823289999998
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2961020525,
              "format_passes": 2,
              "gpu_energy_j": 76.47261893291693,
              "semantic_passes": 2,
              "tokens_per_s": 78.31539009657976,
              "ttft_s": 0.07901377200000001
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35403001450000005,
              "format_passes": 2,
              "gpu_energy_j": 90.68561969835196,
              "semantic_passes": 2,
              "tokens_per_s": 78.64106080244252,
              "ttft_s": 0.07423497500000001
            },
            "spec-branch": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.5281299365,
              "format_passes": 0,
              "gpu_energy_j": 1004.759836581559,
              "semantic_passes": 0,
              "tokens_per_s": 79.3613394266066
            },
            "spec-code": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.596643735,
              "format_passes": 0,
              "gpu_energy_j": 1020.9938268860737,
              "semantic_passes": 0,
              "tokens_per_s": 79.28340241828275
            },
            "spec-repeat": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.409715843,
              "format_passes": 0,
              "gpu_energy_j": 968.5417190317714,
              "semantic_passes": 0,
              "tokens_per_s": 79.43842333255716
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.369291723,
              "format_passes": 2,
              "gpu_energy_j": 96.55257261576419,
              "semantic_passes": 2,
              "tokens_per_s": 78.88297067179565,
              "ttft_s": 0.07772135399999999
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6230630675,
              "format_passes": 0,
              "gpu_energy_j": 162.6638069591046,
              "semantic_passes": 0,
              "tokens_per_s": 78.87387267874455,
              "ttft_s": 0.321183741
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5624497165,
              "format_passes": 0,
              "gpu_energy_j": 147.63514440591297,
              "semantic_passes": 0,
              "tokens_per_s": 78.69085962263935,
              "ttft_s": 0.25748241
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
              "e2e_s": 0.6720510005,
              "format_passes": 2,
              "gpu_energy_j": 179.87712088809343,
              "semantic_passes": 2,
              "tokens_per_s": 78.47932951085112,
              "ttft_s": 0.124133755
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6746258059999999,
              "format_passes": 0,
              "gpu_energy_j": 466.4236450488654,
              "semantic_passes": 0,
              "tokens_per_s": 78.84263999078794,
              "ttft_s": 0.063662835
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.240593228,
              "format_passes": 2,
              "gpu_energy_j": 60.89403237684391,
              "semantic_passes": 2,
              "tokens_per_s": 77.25453208118901,
              "ttft_s": 0.0723725185
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.244030739,
              "format_passes": 0,
              "gpu_energy_j": 63.50013855867756,
              "semantic_passes": 0,
              "tokens_per_s": 76.26012221314163,
              "ttft_s": 0.126091016
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.184333104,
              "format_passes": 2,
              "gpu_energy_j": 43.42928050360737,
              "semantic_passes": 2,
              "tokens_per_s": 76.70842835800815,
              "ttft_s": 0.0670701935
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3612723725,
              "format_passes": 0,
              "gpu_energy_j": 93.14622858143758,
              "semantic_passes": 0,
              "tokens_per_s": 78.05069758220702,
              "ttft_s": 0.0794182695
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.47395222699999995,
              "format_passes": 0,
              "gpu_energy_j": 122.29766799177015,
              "semantic_passes": 2,
              "tokens_per_s": 78.13421091212643,
              "ttft_s": 0.115592359
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.090646142,
              "format_passes": 2,
              "gpu_energy_j": 291.67559696378083,
              "semantic_passes": 2,
              "tokens_per_s": 77.03666612426161,
              "ttft_s": 0.8310020874999999
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.235335539,
              "format_passes": 0,
              "gpu_energy_j": 56.817032255348266,
              "semantic_passes": 0,
              "tokens_per_s": 77.455872496405,
              "ttft_s": 0.06752696650000001
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.20017086750000002,
              "format_passes": 0,
              "gpu_energy_j": 49.50567920900006,
              "semantic_passes": 0,
              "tokens_per_s": 2540.388432465942,
              "ttft_s": 0.199914319
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.722485406,
              "format_passes": 0,
              "gpu_energy_j": 191.29115814999759,
              "semantic_passes": 0,
              "tokens_per_s": 2839.8022715516863,
              "ttft_s": 0.7222439295
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.427315158,
              "format_passes": 0,
              "gpu_energy_j": 385.64607255705374,
              "semantic_passes": 0,
              "tokens_per_s": 2873.5361413218598,
              "ttft_s": 1.4269697959999998
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2984131225,
              "format_passes": 2,
              "gpu_energy_j": 73.8274769232293,
              "semantic_passes": 2,
              "tokens_per_s": 77.70937335133112,
              "ttft_s": 0.0796329935
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.356193788,
              "format_passes": 2,
              "gpu_energy_j": 91.60843685334565,
              "semantic_passes": 2,
              "tokens_per_s": 78.1272203243127,
              "ttft_s": 0.0746463485
            },
            "spec-branch": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.65160478,
              "format_passes": 0,
              "gpu_energy_j": 425.63239368161305,
              "semantic_passes": 0,
              "tokens_per_s": 190.9101988204619
            },
            "spec-code": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.8904220144999999,
              "format_passes": 0,
              "gpu_energy_j": 187.56072155844345,
              "semantic_passes": 0,
              "tokens_per_s": 497.71482221221436
            },
            "spec-repeat": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.3554572464999999,
              "format_passes": 0,
              "gpu_energy_j": 341.20141418366205,
              "semantic_passes": 0,
              "tokens_per_s": 221.1429554132967
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.372960504,
              "format_passes": 2,
              "gpu_energy_j": 97.41607478552098,
              "semantic_passes": 2,
              "tokens_per_s": 78.10709161474972,
              "ttft_s": 0.0785775425
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6275148155,
              "format_passes": 0,
              "gpu_energy_j": 164.90606234219297,
              "semantic_passes": 0,
              "tokens_per_s": 77.88973603791686,
              "ttft_s": 0.32155074100000003
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5654777195,
              "format_passes": 0,
              "gpu_energy_j": 148.03573414351598,
              "semantic_passes": 0,
              "tokens_per_s": 77.98449415447418,
              "ttft_s": 0.25742743199999996
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
            "e2e_change_pct": 0.6779313426666933,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.32899285343488405,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.8226100044984141,
            "ttft_change_pct": 0.006270242943196003
          },
          "decode": {
            "e2e_change_pct": 0.7117459617819843,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.9076830800138103,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.6946535682175847,
            "ttft_change_pct": 0.7970138053222886
          },
          "energy": {
            "e2e_change_pct": 1.0943075611331787,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 11.263495985327655,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.1999705833002139,
            "ttft_change_pct": 0.9496116814764033
          },
          "filtering": {
            "e2e_change_pct": 0.8701062997317877,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 7.186326091971895,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.441242358535877,
            "ttft_change_pct": 0.3840293090661806
          },
          "german": {
            "e2e_change_pct": 1.1050029078374157,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 12.255074715287018,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.9604764964350032,
            "ttft_change_pct": 1.459160653794167
          },
          "ha_sim": {
            "e2e_change_pct": 0.9349212043652244,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 5.024803994643334,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.01859730785,
            "ttft_change_pct": 0.6605680014818649
          },
          "jarvis_memory": {
            "e2e_change_pct": 0.6560233727646025,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.042061414790783846,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.8656971066342001,
            "ttft_change_pct": -0.0356488138164579
          },
          "long_context": {
            "e2e_change_pct": 0.40844165446503045,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.6914681643767073,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.8678991386359525,
            "ttft_change_pct": 0.2678432119728402
          },
          "math": {
            "e2e_change_pct": 0.7325818934357464,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.2621288636410766,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.0742777934090286,
            "ttft_change_pct": -0.06835554588899839
          },
          "prefill": {
            "e2e_change_pct": -0.13730250705569214,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.760043279002498,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.1589163219269052,
            "ttft_change_pct": -0.18360507369890033
          },
          "prefill2048": {
            "e2e_change_pct": 0.0751267031409597,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.3153405344436866,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.09037362453991893,
            "ttft_change_pct": 0.07867961627539
          },
          "prefill4096": {
            "e2e_change_pct": 0.2486389531415334,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.5291129862390331,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.2524126643077662,
            "ttft_change_pct": 0.25203818586960747
          },
          "pve_sim": {
            "e2e_change_pct": 0.7804977981366923,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.458940005713673,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.7738156504121241,
            "ttft_change_pct": 0.7836880638985244
          },
          "sorting": {
            "e2e_change_pct": 0.6111836317200137,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.017600318620815,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.6533997289541404,
            "ttft_change_pct": 0.554150520021035
          },
          "spec-branch": {
            "e2e_change_pct": -53.18752966228799,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -57.63839494921299,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 140.5581863912664
          },
          "spec-code": {
            "e2e_change_pct": -75.24297428085409,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -81.62959298877601,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 527.7667292662019
          },
          "spec-repeat": {
            "e2e_change_pct": -60.24720801052395,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -64.77163477018284,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 178.3828607568337
          },
          "time": {
            "e2e_change_pct": 0.9934641833280411,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.89433367373144,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.9835824518755643,
            "ttft_change_pct": 1.1016129492545934
          },
          "tool-call": {
            "e2e_change_pct": 0.7144939625232993,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.3784599198837677,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.2477346520515131,
            "ttft_change_pct": 0.11426481267617916
          },
          "tool-final": {
            "e2e_change_pct": 0.5383597699795573,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.2713376541981116,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.8976461453751305,
            "ttft_change_pct": -0.02135213819073334
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
            "median_e2e_s": 3.561589696,
            "restore_events": 0,
            "starts": 2
          },
          "B": {
            "acceptance_pct": 96.84376643871647,
            "accepted_n": 3682,
            "checkpoint_events": 96,
            "draft_n": 3802,
            "median_e2e_s": 1.5149384425,
            "restore_events": 10,
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
