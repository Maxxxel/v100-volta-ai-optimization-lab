# Public audit excerpt

Original SHA256: `13dd3428ed47ffaa776fef50798c6a767bcf8b77e51b7e7590e8c3c57920dafd`

Original file: `RESULTS.json`; 40907 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
          "format_passes": 14,
          "quality_attempts": 24,
          "quality_passes": 16,
          "tasks": {
            "code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.7341366315,
              "format_passes": 2,
              "gpu_energy_j": 179.79883289709755,
              "semantic_passes": 2,
              "tokens_per_s": 70.6871278912152,
              "ttft_s": 0.125770766
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.855185182,
              "format_passes": 0,
              "gpu_energy_j": 468.330459281535,
              "semantic_passes": 0,
              "tokens_per_s": 70.9387037779355,
              "ttft_s": 0.0645255
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.25971725349999997,
              "format_passes": 2,
              "gpu_energy_j": 60.78131791748996,
              "semantic_passes": 2,
              "tokens_per_s": 69.75168874623967,
              "ttft_s": 0.073274825
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.25709501300000004,
              "format_passes": 0,
              "gpu_energy_j": 62.37463394305834,
              "semantic_passes": 0,
              "tokens_per_s": 69.09085846863383,
              "ttft_s": 0.1267931115
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1981526735,
              "format_passes": 2,
              "gpu_energy_j": 40.91871006531978,
              "semantic_passes": 2,
              "tokens_per_s": 69.08280112956223,
              "ttft_s": 0.0678140225
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3982396295,
              "format_passes": 0,
              "gpu_energy_j": 90.70904873150954,
              "semantic_passes": 0,
              "tokens_per_s": 69.60730573479145,
              "ttft_s": 0.08213556550000001
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5148548959999999,
              "format_passes": 0,
              "gpu_energy_j": 121.56612441679567,
              "semantic_passes": 2,
              "tokens_per_s": 70.30893938175308,
              "ttft_s": 0.1165534875
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1130878755,
              "format_passes": 2,
              "gpu_energy_j": 293.32000097131424,
              "semantic_passes": 2,
              "tokens_per_s": 69.542164739503,
              "ttft_s": 0.8254153639999999
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2556608585,
              "format_passes": 0,
              "gpu_energy_j": 58.12269429326721,
              "semantic_passes": 0,
              "tokens_per_s": 69.54097969435905,
              "ttft_s": 0.068721002
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.2001015035,
              "format_passes": 0,
              "gpu_energy_j": 47.59688017623169,
              "semantic_passes": 0,
              "tokens_per_s": 2536.775616649038,
              "ttft_s": 0.1999573475
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.719895791,
              "format_passes": 0,
              "gpu_energy_j": 189.16955010418752,
              "semantic_passes": 0,
              "tokens_per_s": 2849.8839612325073,
              "ttft_s": 0.719676642
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.422035335,
              "format_passes": 0,
              "gpu_energy_j": 380.70819259356085,
              "semantic_passes": 0,
              "tokens_per_s": 2884.0673193527664,
              "ttft_s": 1.4217116220000001
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.324359569,
              "format_passes": 2,
              "gpu_energy_j": 74.92284052442301,
              "semantic_passes": 2,
              "tokens_per_s": 69.7113525959723,
              "ttft_s": 0.08043686
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.38791763349999997,
              "format_passes": 2,
              "gpu_energy_j": 92.3373463098589,
              "semantic_passes": 2,
              "tokens_per_s": 70.40635168867567,
              "ttft_s": 0.075394109
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.40627657100000003,
              "format_passes": 0,
              "gpu_energy_j": 97.33371045118278,
              "semantic_passes": 0,
              "tokens_per_s": 70.4044017353202,
              "ttft_s": 0.07957525
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6727928575,
              "format_passes": 0,
              "gpu_energy_j": 164.54645941321343,
              "semantic_passes": 0,
              "tokens_per_s": 70.45705625268597,
              "ttft_s": 0.33428309050000005
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5703034339999999,
              "format_passes": 0,
              "gpu_energy_j": 142.43095036031914,
              "semantic_passes": 0,
              "tokens_per_s": 70.30135612779017,
              "ttft_s": 0.25719979950000005
            }
          }
        },
        "B": {
          "format_passes": 14,
          "quality_attempts": 24,
          "quality_passes": 16,
          "tasks": {
            "code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.668834447,
              "format_passes": 2,
              "gpu_energy_j": 175.01507617513764,
              "semantic_passes": 2,
              "tokens_per_s": 79.27616485752226,
              "ttft_s": 0.12637890899999998
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6593135445,
              "format_passes": 0,
              "gpu_energy_j": 456.27682365008786,
              "semantic_passes": 0,
              "tokens_per_s": 79.57651158437679,
              "ttft_s": 0.063098035
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23863795450000003,
              "format_passes": 2,
              "gpu_energy_j": 54.071484399351306,
              "semantic_passes": 2,
              "tokens_per_s": 78.20405701062452,
              "ttft_s": 0.07244215849999999
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.241596107,
              "format_passes": 0,
              "gpu_energy_j": 57.14759125788479,
              "semantic_passes": 0,
              "tokens_per_s": 77.58152779509658,
              "ttft_s": 0.1255367565
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.18224430349999998,
              "format_passes": 2,
              "gpu_energy_j": 40.22922871372709,
              "semantic_passes": 2,
              "tokens_per_s": 77.52118802373184,
              "ttft_s": 0.06609787
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35795318249999997,
              "format_passes": 0,
              "gpu_energy_j": 91.6449820191968,
              "semantic_passes": 0,
              "tokens_per_s": 78.91910482898155,
              "ttft_s": 0.079180379
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4695462245,
              "format_passes": 0,
              "gpu_energy_j": 117.75913416530796,
              "semantic_passes": 2,
              "tokens_per_s": 79.04313115319977,
              "ttft_s": 0.11525250349999999
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0801132645,
              "format_passes": 2,
              "gpu_energy_j": 290.9636907574421,
              "semantic_passes": 2,
              "tokens_per_s": 77.96766268896957,
              "ttft_s": 0.8235243240000001
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2353802475,
              "format_passes": 0,
              "gpu_energy_j": 56.15061280842254,
              "semantic_passes": 0,
              "tokens_per_s": 77.36388178798707,
              "ttft_s": 0.0672693645
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.19892978,
              "format_passes": 0,
              "gpu_energy_j": 49.067923836696025,
              "semantic_passes": 0,
              "tokens_per_s": 2551.913126162306,
              "ttft_s": 0.1987956105
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7169450225,
              "format_passes": 0,
              "gpu_energy_j": 190.21446298590172,
              "semantic_passes": 0,
              "tokens_per_s": 2862.041260112545,
              "ttft_s": 0.7166935329999999
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.420036279,
              "format_passes": 0,
              "gpu_energy_j": 383.8755830492298,
              "semantic_passes": 0,
              "tokens_per_s": 2888.1981155792355,
              "ttft_s": 1.4197523455
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.29626916000000003,
              "format_passes": 2,
              "gpu_energy_j": 72.27917453196358,
              "semantic_passes": 2,
              "tokens_per_s": 78.33271357542412,
              "ttft_s": 0.079234003
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35384306099999996,
              "format_passes": 2,
              "gpu_energy_j": 87.48234574175316,
              "semantic_passes": 2,
              "tokens_per_s": 78.71755409702504,
              "ttft_s": 0.0743127775
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3691743495,
              "format_passes": 0,
              "gpu_energy_j": 93.83037696136253,
              "semantic_passes": 0,
              "tokens_per_s": 78.89519611306449,
              "ttft_s": 0.077589518
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6203151105,
              "format_passes": 0,
              "gpu_energy_j": 162.48200685150397,
              "semantic_passes": 0,
              "tokens_per_s": 78.97637066407884,
              "ttft_s": 0.31953032849999996
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.535261874,
              "format_passes": 0,
              "gpu_energy_j": 139.7613388703841,
              "semantic_passes": 0,
              "tokens_per_s": 78.70353866195632,
              "ttft_s": 0.255781258
            }
          }
        }
      },
      "comparison": {
        "format_pass_change": 0,
        "note": "Descriptive paired comparison; actual fresh starts per arm: {'A': 2, 'B': 2}. Quality and speed remain separate.",
        "quality_pass_change": 0,
        "status": "DESCRIPTIVE_COMPARISON",
        "tasks": {
          "code": {
            "e2e_change_pct": -8.89509959019119,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.6606161146205842,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 12.150779388752731,
            "ttft_change_pct": 0.4835328744041911
          },
          "decode": {
            "e2e_change_pct": -10.558063928089311,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.573745822541329,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 12.17643873713965,
            "ttft_change_pct": -2.212249420771639
          },
          "energy": {
            "e2e_change_pct": -8.116249003842146,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -11.039302450215349,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 12.117797312599876,
            "ttft_change_pct": -1.136360953437976
          },
          "filtering": {
            "e2e_change_pct": -6.028473994553929,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -8.38007753271195,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 12.289135660859362,
            "ttft_change_pct": -0.9908700757769395
          },
          "german": {
            "e2e_change_pct": -8.028339824544439,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.6850026564670495,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 12.21488815768157,
            "ttft_change_pct": -2.5306749794999917
          },
          "ha_sim": {
            "e2e_change_pct": -10.116132101313147,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.0317970486688033,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 13.377617472609371,
            "ttft_change_pct": -3.5979377289366954
          },
          "jarvis_memory": {
            "e2e_change_pct": -8.80027981709237,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.1316209756224955,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 12.422590709302362,
            "ttft_change_pct": -1.1162119880797294
          },
          "long_context": {
            "e2e_change_pct": -2.96244454061525,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.8033240849820378,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 12.115668215143337,
            "ttft_change_pct": -0.22910162355541663
          },
          "math": {
            "e2e_change_pct": -7.932622584070681,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.3929629533246075,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 11.249341220113095,
            "ttft_change_pct": -2.1123636992371075
          },
          "prefill": {
            "e2e_change_pct": -0.585564565735508,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.0906304258129236,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.5967224461603804,
            "ttft_change_pct": -0.5809924038925329
          },
          "prefill2048": {
            "e2e_change_pct": -0.4098882834001727,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.5523684341051105,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.4265892592616227,
            "ttft_change_pct": -0.41450685292633294
          },
          "prefill4096": {
            "e2e_change_pct": -0.1405770975444698,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.8319732848645067,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.14322814862020028,
            "ttft_change_pct": -0.137811105267871
          },
          "pve_sim": {
            "e2e_change_pct": -8.660268320926267,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.5285181046995406,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 12.367226654486018,
            "ttft_change_pct": -1.4954052159669162
          },
          "sorting": {
            "e2e_change_pct": -8.783971017909398,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -5.257894841176913,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 11.804620192649695,
            "ttft_change_pct": -1.434238714857683
          },
          "time": {
            "e2e_change_pct": -9.132257222875895,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.599301283780121,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 12.060033419025062,
            "ttft_change_pct": -2.4954140891797483
          },
          "tool-call": {
            "e2e_change_pct": -7.799985748213734,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.2546320164356417,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 12.091499225910528,
            "ttft_change_pct": -4.413254041038639
          },
          "tool-final": {
            "e2e_change_pct": -6.144371208538068,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.8743197901730735,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 11.951664942128692,
            "ttft_change_pct": -0.5515328949546983
          }
        }
      },
      "complete": true
    }
  }
}
```
