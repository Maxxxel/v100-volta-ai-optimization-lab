# Public audit excerpt

Original SHA256: `5d8fbe2a68a7b4aa02d0e2de9db2573bb748a4637c6794083a81633f81918150`

Original file: `RESULTS.json`; 39830 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.66679442,
              "format_passes": 2,
              "gpu_energy_j": 180.47991883582176,
              "semantic_passes": 2,
              "tokens_per_s": 79.28136848841508,
              "ttft_s": 0.124446538
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.658473939,
              "format_passes": 0,
              "gpu_energy_j": 457.9971139440447,
              "semantic_passes": 0,
              "tokens_per_s": 79.62377622970268,
              "ttft_s": 0.06323197450000001
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23831703399999998,
              "format_passes": 2,
              "gpu_energy_j": 59.44989322368391,
              "semantic_passes": 2,
              "tokens_per_s": 78.22866246582836,
              "ttft_s": 0.07214040699999999
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.241856546,
              "format_passes": 0,
              "gpu_energy_j": 61.584863943657055,
              "semantic_passes": 0,
              "tokens_per_s": 77.6538220716851,
              "ttft_s": 0.1258893295
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.18328514099999998,
              "format_passes": 2,
              "gpu_energy_j": 39.253628535144095,
              "semantic_passes": 2,
              "tokens_per_s": 77.44067846881555,
              "ttft_s": 0.067030421
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.358095917,
              "format_passes": 0,
              "gpu_energy_j": 86.66294804230607,
              "semantic_passes": 0,
              "tokens_per_s": 78.86051480453466,
              "ttft_s": 0.0791093195
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.470111623,
              "format_passes": 0,
              "gpu_energy_j": 118.42252459324848,
              "semantic_passes": 2,
              "tokens_per_s": 79.05556422704302,
              "ttft_s": 0.1158794265
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.081134383,
              "format_passes": 2,
              "gpu_energy_j": 289.2102972188533,
              "semantic_passes": 2,
              "tokens_per_s": 77.65629184369769,
              "ttft_s": 0.8235727415
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.233806727,
              "format_passes": 0,
              "gpu_energy_j": 56.26296190376295,
              "semantic_passes": 0,
              "tokens_per_s": 78.28875286376021,
              "ttft_s": 0.067724331
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.1998697405,
              "format_passes": 0,
              "gpu_energy_j": 47.9545190523059,
              "semantic_passes": 0,
              "tokens_per_s": 2540.9188658998396,
              "ttft_s": 0.1996890965
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7195269885,
              "format_passes": 0,
              "gpu_energy_j": 190.47622785908675,
              "semantic_passes": 0,
              "tokens_per_s": 2851.152883242123,
              "ttft_s": 0.7193051385
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4229629209999999,
              "format_passes": 0,
              "gpu_energy_j": 381.9436488576898,
              "semantic_passes": 0,
              "tokens_per_s": 2882.039240647102,
              "ttft_s": 1.4226011425
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2952308655,
              "format_passes": 2,
              "gpu_energy_j": 71.97652075570645,
              "semantic_passes": 2,
              "tokens_per_s": 78.64381598915352,
              "ttft_s": 0.079018484
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.358125541,
              "format_passes": 2,
              "gpu_energy_j": 89.30939087362269,
              "semantic_passes": 2,
              "tokens_per_s": 77.59163621933274,
              "ttft_s": 0.07446504600000001
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3692313995,
              "format_passes": 2,
              "gpu_energy_j": 93.02353644979168,
              "semantic_passes": 2,
              "tokens_per_s": 78.91837140575949,
              "ttft_s": 0.077737255
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6202557805,
              "format_passes": 0,
              "gpu_energy_j": 162.88254611484655,
              "semantic_passes": 0,
              "tokens_per_s": 79.00293699179929,
              "ttft_s": 0.31888845
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.561030374,
              "format_passes": 0,
              "gpu_energy_j": 145.77871868129805,
              "semantic_passes": 0,
              "tokens_per_s": 78.80777332448915,
              "ttft_s": 0.25654347899999996
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
              "e2e_s": 0.667318233,
              "format_passes": 2,
              "gpu_energy_j": 178.93984034310836,
              "semantic_passes": 2,
              "tokens_per_s": 79.14872161742343,
              "ttft_s": 0.124040682
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6611431835000001,
              "format_passes": 0,
              "gpu_energy_j": 458.80769911096274,
              "semantic_passes": 0,
              "tokens_per_s": 79.48463957242889,
              "ttft_s": 0.0631680825
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2381202305,
              "format_passes": 2,
              "gpu_energy_j": 53.779223469649835,
              "semantic_passes": 2,
              "tokens_per_s": 78.23550042740953,
              "ttft_s": 0.0718876095
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2428120385,
              "format_passes": 0,
              "gpu_energy_j": 56.60612831649826,
              "semantic_passes": 0,
              "tokens_per_s": 77.33752771099515,
              "ttft_s": 0.12630793899999998
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1830597745,
              "format_passes": 2,
              "gpu_energy_j": 41.5276654736919,
              "semantic_passes": 2,
              "tokens_per_s": 77.20729883815685,
              "ttft_s": 0.06646866400000001
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.358527013,
              "format_passes": 0,
              "gpu_energy_j": 91.1836831964593,
              "semantic_passes": 0,
              "tokens_per_s": 78.67669205198995,
              "ttft_s": 0.078876257
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.47078005450000004,
              "format_passes": 0,
              "gpu_energy_j": 118.38951087445108,
              "semantic_passes": 2,
              "tokens_per_s": 78.97412746038798,
              "ttft_s": 0.11615168149999999
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.081985789,
              "format_passes": 2,
              "gpu_energy_j": 290.20453133073994,
              "semantic_passes": 2,
              "tokens_per_s": 77.84827869779224,
              "ttft_s": 0.8250220450000001
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2338547185,
              "format_passes": 0,
              "gpu_energy_j": 56.258904765265775,
              "semantic_passes": 0,
              "tokens_per_s": 78.16519384867462,
              "ttft_s": 0.0674958045
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.1994483615,
              "format_passes": 0,
              "gpu_energy_j": 49.96254724881687,
              "semantic_passes": 0,
              "tokens_per_s": 2545.7801425700945,
              "ttft_s": 0.1992679315
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7197648565,
              "format_passes": 0,
              "gpu_energy_j": 190.77816546425902,
              "semantic_passes": 0,
              "tokens_per_s": 2850.2202197036745,
              "ttft_s": 0.7195423485000001
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.419437577,
              "format_passes": 0,
              "gpu_energy_j": 384.6805497385602,
              "semantic_passes": 0,
              "tokens_per_s": 2889.091823409073,
              "ttft_s": 1.419140762
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2955413925,
              "format_passes": 2,
              "gpu_energy_j": 68.31879448987239,
              "semantic_passes": 2,
              "tokens_per_s": 78.52812946449197,
              "ttft_s": 0.07900839700000001
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3540978715,
              "format_passes": 2,
              "gpu_energy_j": 90.0390571686103,
              "semantic_passes": 2,
              "tokens_per_s": 78.67838296078739,
              "ttft_s": 0.074456722
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.375059269,
              "format_passes": 2,
              "gpu_energy_j": 95.03725194392777,
              "semantic_passes": 2,
              "tokens_per_s": 77.37329163935081,
              "ttft_s": 0.0776510705
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6211317145,
              "format_passes": 0,
              "gpu_energy_j": 162.71326848263266,
              "semantic_passes": 0,
              "tokens_per_s": 78.790073647014,
              "ttft_s": 0.31884205200000004
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5620280185,
              "format_passes": 0,
              "gpu_energy_j": 144.18435004686944,
              "semantic_passes": 0,
              "tokens_per_s": 78.71949660511669,
              "ttft_s": 0.257129163
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
            "e2e_change_pct": 0.07855689614200134,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.8533240166815337,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.1673115304651085,
            "ttft_change_pct": -0.3261287991796147
          },
          "decode": {
            "e2e_change_pct": 0.16094582116916722,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.17698477615670782,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.17474260059257007,
            "ttft_change_pct": -0.10104381605229307
          },
          "energy": {
            "e2e_change_pct": -0.08258054269002502,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -9.538570124420287,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.008740992579481244,
            "ttft_change_pct": -0.3504242774787558
          },
          "filtering": {
            "e2e_change_pct": 0.3950658006998786,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -8.084349478653973,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.4073133198749246,
            "ttft_change_pct": 0.33252182823007015
          },
          "german": {
            "e2e_change_pct": -0.12295950384760834,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 5.793189122661202,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.3013656843834145,
            "ttft_change_pct": -0.8380627655613204
          },
          "ha_sim": {
            "e2e_change_pct": 0.1203856228274125,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 5.21645669374915,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.23309859566645885,
            "ttft_change_pct": -0.29460814664192814
          },
          "jarvis_memory": {
            "e2e_change_pct": 0.14218569958650562,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.02787790490939024,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.10301206177109057,
            "ttft_change_pct": 0.23494679618560887
          },
          "long_context": {
            "e2e_change_pct": 0.07875117223055117,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.34377548844128913,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.2472263992220558,
            "ttft_change_pct": 0.17597759456686735
          },
          "math": {
            "e2e_change_pct": 0.0205261416623026,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.007211028996512159,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.15782473288418197,
            "ttft_change_pct": -0.33743633436554843
          },
          "prefill": {
            "e2e_change_pct": -0.21082681097491784,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.187359682036917,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.19131963383385298,
            "ttft_change_pct": -0.21091036385153528
          },
          "prefill2048": {
            "e2e_change_pct": 0.03305894063763137,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.15851721160482501,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.03271180384364358,
            "ttft_change_pct": 0.032977659591693076
          },
          "prefill4096": {
            "e2e_change_pct": -0.24774672255847285,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.7165719050587382,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.2447080755356934,
            "ttft_change_pct": -0.24324319702984099
          },
          "pve_sim": {
            "e2e_change_pct": 0.10518107565551382,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -5.0818325579373935,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.14710187089282956,
            "ttft_change_pct": -0.012765367657507909
          },
          "sorting": {
            "e2e_change_pct": -1.1246529607336742,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.8170095975910563,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 1.4005977891517585,
            "ttft_change_pct": -0.011178399057198973
          },
          "time": {
            "e2e_change_pct": 1.5783786286572177,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.1647376255395034,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -1.9578201360297198,
            "ttft_change_pct": -0.11086640504607281
          },
          "tool-call": {
            "e2e_change_pct": 0.14122141663781562,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.10392619482663124,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.26943725498127513,
            "ttft_change_pct": -0.014549915495509769
          },
          "tool-final": {
            "e2e_change_pct": 0.17782361637339594,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.0936909370936498,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.11201524373615213,
            "ttft_change_pct": 0.22829814356732925
          }
        }
      },
      "complete": true
    }
  }
}
```
