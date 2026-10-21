# Public audit excerpt

Original SHA256: `9de95af06dcc3290e44fd619da2eadc3fa738a4cd2237a361f0bc2ad8a875dcb`

Original file: `RESULTS.json`; 45155 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.666649026,
              "format_passes": 2,
              "gpu_energy_j": 177.05584432728838,
              "semantic_passes": 2,
              "tokens_per_s": 79.20811778789789,
              "ttft_s": 0.123690326
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6579598365,
              "format_passes": 0,
              "gpu_energy_j": 446.4047652878281,
              "semantic_passes": 0,
              "tokens_per_s": 79.62939134902203,
              "ttft_s": 0.062910012
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.238077915,
              "format_passes": 2,
              "gpu_energy_j": 53.78604590075842,
              "semantic_passes": 2,
              "tokens_per_s": 78.16896826961221,
              "ttft_s": 0.071698387
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.243729061,
              "format_passes": 0,
              "gpu_energy_j": 59.82333838708364,
              "semantic_passes": 0,
              "tokens_per_s": 77.63993819978529,
              "ttft_s": 0.12779075550000002
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.18295048749999998,
              "format_passes": 2,
              "gpu_energy_j": 40.9932208162231,
              "semantic_passes": 2,
              "tokens_per_s": 77.51867595702714,
              "ttft_s": 0.066823831
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.358224776,
              "format_passes": 0,
              "gpu_energy_j": 90.18218608090842,
              "semantic_passes": 0,
              "tokens_per_s": 78.87566742544847,
              "ttft_s": 0.0792226745
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.46972016650000004,
              "format_passes": 0,
              "gpu_energy_j": 117.42978262358828,
              "semantic_passes": 2,
              "tokens_per_s": 78.93315663853997,
              "ttft_s": 0.1149764615
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.07552454,
              "format_passes": 2,
              "gpu_energy_j": 287.90520987792195,
              "semantic_passes": 2,
              "tokens_per_s": 78.1009576506664,
              "ttft_s": 0.8194227700000001
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.234597075,
              "format_passes": 0,
              "gpu_energy_j": 54.36915435450082,
              "semantic_passes": 0,
              "tokens_per_s": 78.15288052790245,
              "ttft_s": 0.06822342449999999
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.19813120750000002,
              "format_passes": 0,
              "gpu_energy_j": 47.422517939199864,
              "semantic_passes": 0,
              "tokens_per_s": 2562.7527255044633,
              "ttft_s": 0.197946603
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.714520104,
              "format_passes": 0,
              "gpu_energy_j": 187.60033103199578,
              "semantic_passes": 0,
              "tokens_per_s": 2871.3594673389052,
              "ttft_s": 0.7142260455
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4085319164999999,
              "format_passes": 0,
              "gpu_energy_j": 379.75709095509774,
              "semantic_passes": 0,
              "tokens_per_s": 2911.6033520317096,
              "ttft_s": 1.408198955
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2954843585,
              "format_passes": 2,
              "gpu_energy_j": 69.03082727063664,
              "semantic_passes": 2,
              "tokens_per_s": 78.59910417314198,
              "ttft_s": 0.07915312299999999
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.353765153,
              "format_passes": 2,
              "gpu_energy_j": 84.52699280233638,
              "semantic_passes": 2,
              "tokens_per_s": 78.79592697441414,
              "ttft_s": 0.0745212975
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.368852885,
              "format_passes": 2,
              "gpu_energy_j": 90.82172698185781,
              "semantic_passes": 2,
              "tokens_per_s": 78.9376137617644,
              "ttft_s": 0.0774359075
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6198604405,
              "format_passes": 0,
              "gpu_energy_j": 159.84101252881433,
              "semantic_passes": 0,
              "tokens_per_s": 78.78785837817433,
              "ttft_s": 0.317754326
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.561076578,
              "format_passes": 0,
              "gpu_energy_j": 144.31196060024996,
              "semantic_passes": 0,
              "tokens_per_s": 78.70079546156242,
              "ttft_s": 0.255670117
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
              "e2e_s": 0.6653439865,
              "format_passes": 2,
              "gpu_energy_j": 172.8573244360424,
              "semantic_passes": 2,
              "tokens_per_s": 79.38692136971437,
              "ttft_s": 0.123638937
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.657480528,
              "format_passes": 0,
              "gpu_energy_j": 444.7954606174095,
              "semantic_passes": 0,
              "tokens_per_s": 79.63385986318579,
              "ttft_s": 0.062910754
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2375879455,
              "format_passes": 2,
              "gpu_energy_j": 55.805355252360975,
              "semantic_passes": 2,
              "tokens_per_s": 78.40975879734961,
              "ttft_s": 0.071726679
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.241484307,
              "format_passes": 0,
              "gpu_energy_j": 61.877197525387885,
              "semantic_passes": 0,
              "tokens_per_s": 77.55821588083279,
              "ttft_s": 0.125360706
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.183764986,
              "format_passes": 2,
              "gpu_energy_j": 39.53073710527919,
              "semantic_passes": 2,
              "tokens_per_s": 77.28488971740884,
              "ttft_s": 0.067247975
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.357605684,
              "format_passes": 0,
              "gpu_energy_j": 90.21228224027021,
              "semantic_passes": 0,
              "tokens_per_s": 78.84156232466472,
              "ttft_s": 0.0785318385
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.469057551,
              "format_passes": 0,
              "gpu_energy_j": 114.89703994893816,
              "semantic_passes": 2,
              "tokens_per_s": 79.08310484300628,
              "ttft_s": 0.114952838
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0697519995,
              "format_passes": 2,
              "gpu_energy_j": 282.7046204565156,
              "semantic_passes": 2,
              "tokens_per_s": 77.84843869445204,
              "ttft_s": 0.81277904
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23335444849999998,
              "format_passes": 0,
              "gpu_energy_j": 52.98871129270592,
              "semantic_passes": 0,
              "tokens_per_s": 78.39854236004808,
              "ttft_s": 0.06742609199999999
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.198779915,
              "format_passes": 0,
              "gpu_energy_j": 47.03215311697614,
              "semantic_passes": 0,
              "tokens_per_s": 2555.329763162315,
              "ttft_s": 0.1985903375
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7102783895,
              "format_passes": 0,
              "gpu_energy_j": 189.29757083862035,
              "semantic_passes": 0,
              "tokens_per_s": 2888.3699031893443,
              "ttft_s": 0.710023787
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.3899075745,
              "format_passes": 0,
              "gpu_energy_j": 377.2007189085122,
              "semantic_passes": 0,
              "tokens_per_s": 2950.6089978972477,
              "ttft_s": 1.389556742
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.29513271399999996,
              "format_passes": 2,
              "gpu_energy_j": 71.39608460161512,
              "semantic_passes": 2,
              "tokens_per_s": 78.69952811447942,
              "ttft_s": 0.0790987145
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3561645655,
              "format_passes": 2,
              "gpu_energy_j": 86.06642071330091,
              "semantic_passes": 2,
              "tokens_per_s": 78.47205214872369,
              "ttft_s": 0.075709671
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3690002325,
              "format_passes": 2,
              "gpu_energy_j": 89.16748189540488,
              "semantic_passes": 2,
              "tokens_per_s": 78.95816499815619,
              "ttft_s": 0.0776078995
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.618726816,
              "format_passes": 0,
              "gpu_energy_j": 159.17623380513396,
              "semantic_passes": 0,
              "tokens_per_s": 78.9777008268878,
              "ttft_s": 0.31713453599999997
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.561135348,
              "format_passes": 0,
              "gpu_energy_j": 143.65823745760923,
              "semantic_passes": 0,
              "tokens_per_s": 78.5671334068593,
              "ttft_s": 0.2554614925
            }
          }
        }
      },
      "change_exercised": false,
      "comparison": {
        "format_pass_change": 0,
        "note": "Descriptive paired comparison; actual fresh starts per arm: {'A': 2, 'B': 2}. Quality and speed remain separate.",
        "quality_pass_change": 0,
        "status": "DESCRIPTIVE_COMPARISON",
        "tasks": {
          "code": {
            "e2e_change_pct": -0.19576110503458644,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.3712969810163353,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.22573896061421905,
            "ttft_change_pct": -0.04154649895579121
          },
          "decode": {
            "e2e_change_pct": -0.02890953625340753,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.36050347029360497,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.005611639230274079,
            "ttft_change_pct": 0.0011794624995342673
          },
          "energy": {
            "e2e_change_pct": -0.20580216354800784,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.7543368689500367,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.30803851332270593,
            "ttft_change_pct": 0.03945974405255015
          },
          "filtering": {
            "e2e_change_pct": -0.9210038354843464,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.4332071624202376,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.10525809376896733,
            "ttft_change_pct": -1.9015847355249638
          },
          "german": {
            "e2e_change_pct": 0.44520160133489917,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.567623333380854,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.3015869875639954,
            "ttft_change_pct": 0.6347196705917657
          },
          "ha_sim": {
            "e2e_change_pct": -0.1728222170763627,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.03337262121234641,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.0432390645898284,
            "ttft_change_pct": -0.8720180230724184
          },
          "jarvis_memory": {
            "e2e_change_pct": -0.14106601062869872,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.156814581500699,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.18996858969289043,
            "ttft_change_pct": -0.020546379399577486
          },
          "long_context": {
            "e2e_change_pct": -0.536718622896315,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.8063547455815399,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.3233237642793596,
            "ttft_change_pct": -0.8107817165002751
          },
          "math": {
            "e2e_change_pct": -0.529685419138326,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.5390188208447295,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.3143349681883123,
            "ttft_change_pct": -1.1687078240993243
          },
          "prefill": {
            "e2e_change_pct": 0.32741308559378623,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.8231634235959517,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.2896480127901224,
            "ttft_change_pct": 0.32520613652560204
          },
          "prefill2048": {
            "e2e_change_pct": -0.5936452279304949,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.9047104540210515,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.5924174957517181,
            "ttft_change_pct": -0.5883653398635391
          },
          "prefill4096": {
            "e2e_change_pct": -1.3222520400019477,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.6731597927917998,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 1.3396620744484222,
            "ttft_change_pct": -1.3238337476255357
          },
          "pve_sim": {
            "e2e_change_pct": -0.11900613006560201,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.4263783652851876,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.12776728487415845,
            "ttft_change_pct": -0.06873828591702491
          },
          "sorting": {
            "e2e_change_pct": 0.6782500988727902,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.82122640345721,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.4110299074159274,
            "ttft_change_pct": 1.5946763406796682
          },
          "time": {
            "e2e_change_pct": 0.03994749830953381,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.821419985532069,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.02603478292848571,
            "ttft_change_pct": 0.2221088453053799
          },
          "tool-call": {
            "e2e_change_pct": -0.18288382770249578,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.4158999703286592,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.24095393963146083,
            "ttft_change_pct": -0.1950532059790122
          },
          "tool-final": {
            "e2e_change_pct": 0.010474506030799802,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.4529930436269036,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.1698357099432446,
            "ttft_change_pct": -0.0815990943517142
          }
        }
      },
      "complete": true,
      "numerical_results": [
        {
          "begin_ns": 422121923689996,
          "end_ns": 422123735022939,
          "model": "omnicoder2",
          "passed": true,
          "reference": "existing CPU reference backend",
          "returncode": 0
        },
        {
          "begin_ns": 422168251279398,
          "end_ns": 422169812063566,
          "model": "omnicoder2",
          "passed": true,
          "reference": "existing CPU reference backend",
          "returncode": 0
        }
      ]
    }
  }
}
```
