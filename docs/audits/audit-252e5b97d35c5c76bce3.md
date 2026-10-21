# Public audit excerpt

Original SHA256: `252e5b97d35c5c76bce3d18cee0b28539588fba5ac68ff3cbcd96fbc49453814`

Original file: `RESULTS.json`; 39513 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{}
```

## Selected aggregate measurements

```json
{
  "models": {
    "qwen35": {
      "arms": {
        "A": {
          "format_passes": 10,
          "quality_attempts": 24,
          "quality_passes": 14,
          "tasks": {
            "code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.526949416,
              "format_passes": 2,
              "gpu_energy_j": 133.37357179172056,
              "semantic_passes": 2,
              "tokens_per_s": 96.54295414607142,
              "ttft_s": 0.13330352350000002
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.3667812394999999,
              "format_passes": 0,
              "gpu_energy_j": 354.59291640395594,
              "semantic_passes": 0,
              "tokens_per_s": 97.07687892728596,
              "ttft_s": 0.058191588
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.20514118250000002,
              "format_passes": 2,
              "gpu_energy_j": 44.076764601350675,
              "semantic_passes": 2,
              "tokens_per_s": 95.11007813140111,
              "ttft_s": 0.0684264805
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2302725115,
              "format_passes": 0,
              "gpu_energy_j": 55.118402938755835,
              "semantic_passes": 0,
              "tokens_per_s": 93.90847463372276,
              "ttft_s": 0.13440493
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1578743645,
              "format_passes": 2,
              "gpu_energy_j": 31.217946185977375,
              "semantic_passes": 2,
              "tokens_per_s": 94.05245526096039,
              "ttft_s": 0.062126505
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.306833895,
              "format_passes": 0,
              "gpu_energy_j": 72.59786874549297,
              "semantic_passes": 0,
              "tokens_per_s": 95.98575182325439,
              "ttft_s": 0.07758438200000001
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3990068315,
              "format_passes": 0,
              "gpu_energy_j": 95.88648524854814,
              "semantic_passes": 2,
              "tokens_per_s": 96.20293004516799,
              "ttft_s": 0.107972739
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0316713425000001,
              "format_passes": 2,
              "gpu_energy_j": 272.8054880272048,
              "semantic_passes": 2,
              "tokens_per_s": 94.36787887052593,
              "ttft_s": 0.8727253005
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.14902770450000002,
              "format_passes": 0,
              "gpu_energy_j": 32.13124258179838,
              "semantic_passes": 0,
              "tokens_per_s": 93.70555418390177,
              "ttft_s": 0.06362633200000001
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.2065183585,
              "format_passes": 0,
              "gpu_energy_j": 50.57842481891954,
              "semantic_passes": 0,
              "tokens_per_s": 2457.7749592429664,
              "ttft_s": 0.206370326
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7570555905,
              "format_passes": 0,
              "gpu_energy_j": 200.757455202121,
              "semantic_passes": 0,
              "tokens_per_s": 2709.606344218523,
              "ttft_s": 0.7568166245
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4993693705,
              "format_passes": 0,
              "gpu_energy_j": 404.7137201713093,
              "semantic_passes": 0,
              "tokens_per_s": 2734.9642419171323,
              "ttft_s": 1.4990275055
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2545127515,
              "format_passes": 2,
              "gpu_energy_j": 55.543749418049046,
              "semantic_passes": 2,
              "tokens_per_s": 95.73194207799261,
              "ttft_s": 0.076873044
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3525707345,
              "format_passes": 0,
              "gpu_energy_j": 84.981384663876,
              "semantic_passes": 2,
              "tokens_per_s": 95.88616440019877,
              "ttft_s": 0.0709857495
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3149676505,
              "format_passes": 0,
              "gpu_energy_j": 75.06091295174679,
              "semantic_passes": 0,
              "tokens_per_s": 95.96653362470039,
              "ttft_s": 0.0753164515
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5502144365,
              "format_passes": 0,
              "gpu_energy_j": 137.90366783688597,
              "semantic_passes": 0,
              "tokens_per_s": 96.20655440333431,
              "ttft_s": 0.302924401
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5255379585,
              "format_passes": 0,
              "gpu_energy_j": 133.78933104042534,
              "semantic_passes": 0,
              "tokens_per_s": 95.81718201635461,
              "ttft_s": 0.27484461299999996
            }
          }
        },
        "B": {
          "format_passes": 10,
          "quality_attempts": 24,
          "quality_passes": 14,
          "tasks": {
            "code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.525880833,
              "format_passes": 2,
              "gpu_energy_j": 132.99398906577918,
              "semantic_passes": 2,
              "tokens_per_s": 96.60804953411943,
              "ttft_s": 0.132528973
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.3671068835,
              "format_passes": 0,
              "gpu_energy_j": 354.62718608411876,
              "semantic_passes": 0,
              "tokens_per_s": 97.02196059336242,
              "ttft_s": 0.058347554999999995
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.20523141150000002,
              "format_passes": 2,
              "gpu_energy_j": 45.290005201298676,
              "semantic_passes": 2,
              "tokens_per_s": 95.02982953060351,
              "ttft_s": 0.06840884650000001
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2300796785,
              "format_passes": 0,
              "gpu_energy_j": 53.93627791104386,
              "semantic_passes": 0,
              "tokens_per_s": 94.07366388259729,
              "ttft_s": 0.13438150999999998
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.156703237,
              "format_passes": 2,
              "gpu_energy_j": 34.77928333796609,
              "semantic_passes": 2,
              "tokens_per_s": 94.1407906298536,
              "ttft_s": 0.06104869
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.306359194,
              "format_passes": 0,
              "gpu_energy_j": 73.3192194067193,
              "semantic_passes": 0,
              "tokens_per_s": 96.02920060484264,
              "ttft_s": 0.0772109305
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3979379155,
              "format_passes": 0,
              "gpu_energy_j": 92.77703765855216,
              "semantic_passes": 2,
              "tokens_per_s": 96.30615974186162,
              "ttft_s": 0.107134422
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.033361798,
              "format_passes": 2,
              "gpu_energy_j": 274.68613945027585,
              "semantic_passes": 2,
              "tokens_per_s": 93.89983729395223,
              "ttft_s": 0.873587746
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1488966725,
              "format_passes": 0,
              "gpu_energy_j": 30.9800221629612,
              "semantic_passes": 0,
              "tokens_per_s": 93.73023257546505,
              "ttft_s": 0.063527064
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.2057616855,
              "format_passes": 0,
              "gpu_energy_j": 49.15863617343885,
              "semantic_passes": 0,
              "tokens_per_s": 2466.954019684821,
              "ttft_s": 0.20560266700000002
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.753223596,
              "format_passes": 0,
              "gpu_energy_j": 200.42682836674868,
              "semantic_passes": 0,
              "tokens_per_s": 2723.7797682751925,
              "ttft_s": 0.75293575
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4963203065,
              "format_passes": 0,
              "gpu_energy_j": 406.3156858096295,
              "semantic_passes": 0,
              "tokens_per_s": 2740.4842170772017,
              "ttft_s": 1.496011492
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.25541895400000003,
              "format_passes": 2,
              "gpu_energy_j": 57.59021043934169,
              "semantic_passes": 2,
              "tokens_per_s": 95.27261685562917,
              "ttft_s": 0.076932851
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3515956885,
              "format_passes": 0,
              "gpu_energy_j": 83.56843714115846,
              "semantic_passes": 2,
              "tokens_per_s": 96.02245552592774,
              "ttft_s": 0.07039208250000001
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.31481486550000004,
              "format_passes": 0,
              "gpu_energy_j": 74.98125916921947,
              "semantic_passes": 0,
              "tokens_per_s": 95.95216468576696,
              "ttft_s": 0.0750500305
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5509386925,
              "format_passes": 0,
              "gpu_energy_j": 138.70502368691052,
              "semantic_passes": 0,
              "tokens_per_s": 96.11688086680664,
              "ttft_s": 0.304040722
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.523789187,
              "format_passes": 0,
              "gpu_energy_j": 130.72005827888566,
              "semantic_passes": 0,
              "tokens_per_s": 95.91425365423369,
              "ttft_s": 0.273812819
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
            "e2e_change_pct": -0.2027866371143272,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.28460115511801387,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.06742634780940726,
            "ttft_change_pct": -0.5810427809134544
          },
          "decode": {
            "e2e_change_pct": 0.023825612364958282,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.009664513468110592,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.05657200203631474,
            "ttft_change_pct": 0.2680232751166578
          },
          "energy": {
            "e2e_change_pct": 0.04398385487516254,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.7525627412108733,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.08437444524725946,
            "ttft_change_pct": -0.025770724829243807
          },
          "filtering": {
            "e2e_change_pct": -0.0837412154598427,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.1447011609271094,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.17590451715761013,
            "ttft_change_pct": -0.01742495606376071
          },
          "german": {
            "e2e_change_pct": -0.7418097952185287,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 11.407980303292398,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.09392138530366356,
            "ttft_change_pct": -1.7348714530134868
          },
          "ha_sim": {
            "e2e_change_pct": -0.1547094397768567,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.9936251210833413,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.04526586578001979,
            "ttft_change_pct": -0.4813488106407915
          },
          "jarvis_memory": {
            "e2e_change_pct": -0.26789416010286615,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.242842390078182,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.10730410876795826,
            "ttft_change_pct": -0.7764154246378774
          },
          "long_context": {
            "e2e_change_pct": 0.16385601018087392,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.6893744831421911,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.4959755185510284,
            "ttft_change_pct": 0.09882210353084897
          },
          "math": {
            "e2e_change_pct": -0.08792459122929364,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.5828692771730064,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.0263361033166154,
            "ttft_change_pct": -0.15601716597464232
          },
          "prefill": {
            "e2e_change_pct": -0.3663950292341567,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.8071033262973333,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.37347033776771177,
            "ttft_change_pct": -0.3719812895968233
          },
          "prefill2048": {
            "e2e_change_pct": -0.5061708212826477,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.16468969236507203,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.52308056064716,
            "ttft_change_pct": -0.512789277397796
          },
          "prefill4096": {
            "e2e_change_pct": -0.20335642837516765,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.3958268668633469,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.2018298841157895,
            "ttft_change_pct": -0.20119800930497034
          },
          "pve_sim": {
            "e2e_change_pct": 0.3560538694659554,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.684412814644533,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.47980351426406553,
            "ttft_change_pct": 0.07779970310528572
          },
          "sorting": {
            "e2e_change_pct": -0.276553299689708,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.6626553312894643,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.14213846865345214,
            "ttft_change_pct": -0.8363185627841996
          },
          "time": {
            "e2e_change_pct": -0.048508156236803934,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.10611885653258879,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.014972864383766549,
            "ttft_change_pct": -0.35373546508626896
          },
          "tool-call": {
            "e2e_change_pct": 0.13163158796907215,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.5810982859226099,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.09320938379283605,
            "ttft_change_pct": 0.3685147173073
          },
          "tool-final": {
            "e2e_change_pct": -0.33275836154468275,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.294108758651525,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.10130921807167681,
            "ttft_change_pct": -0.37540994118010484
          }
        }
      },
      "complete": true
    }
  }
}
```
