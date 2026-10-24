# Public audit excerpt

Original SHA256: `facf6f4c7f2f381132be4e91565d114ba630a6f4cb2675298948be9fceb1f3a6`

Original file: `RESULTS.json`; 39672 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.6667667239999999,
              "format_passes": 2,
              "gpu_energy_j": 176.663377482516,
              "semantic_passes": 2,
              "tokens_per_s": 79.19261154188116,
              "ttft_s": 0.1237693895
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.658722596,
              "format_passes": 0,
              "gpu_energy_j": 448.4863813298527,
              "semantic_passes": 0,
              "tokens_per_s": 79.60308776170223,
              "ttft_s": 0.063195013
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.237994698,
              "format_passes": 2,
              "gpu_energy_j": 57.66419311321799,
              "semantic_passes": 2,
              "tokens_per_s": 78.21247352905098,
              "ttft_s": 0.0717477975
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.24210777849999998,
              "format_passes": 0,
              "gpu_energy_j": 62.30805541773267,
              "semantic_passes": 0,
              "tokens_per_s": 77.44310325494808,
              "ttft_s": 0.125881802
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.18292365249999998,
              "format_passes": 2,
              "gpu_energy_j": 38.97118947074458,
              "semantic_passes": 2,
              "tokens_per_s": 77.15258140435813,
              "ttft_s": 0.0662673335
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3583966205,
              "format_passes": 0,
              "gpu_energy_j": 89.78772197277956,
              "semantic_passes": 0,
              "tokens_per_s": 78.86435786162308,
              "ttft_s": 0.07934796250000001
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.470132529,
              "format_passes": 0,
              "gpu_energy_j": 116.75875434783566,
              "semantic_passes": 2,
              "tokens_per_s": 78.93817036640947,
              "ttft_s": 0.11539173
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0777638495000001,
              "format_passes": 2,
              "gpu_energy_j": 284.8260216234163,
              "semantic_passes": 2,
              "tokens_per_s": 78.01933325962582,
              "ttft_s": 0.821335218
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2334818195,
              "format_passes": 0,
              "gpu_energy_j": 54.32074882637221,
              "semantic_passes": 0,
              "tokens_per_s": 78.26101279081888,
              "ttft_s": 0.06732672
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.197821646,
              "format_passes": 0,
              "gpu_energy_j": 49.013637228458684,
              "semantic_passes": 0,
              "tokens_per_s": 2566.600857918817,
              "ttft_s": 0.197689199
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7161940175,
              "format_passes": 0,
              "gpu_energy_j": 187.6606824643784,
              "semantic_passes": 0,
              "tokens_per_s": 2864.542113044327,
              "ttft_s": 0.715986459
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.411912821,
              "format_passes": 0,
              "gpu_energy_j": 379.23582628999554,
              "semantic_passes": 0,
              "tokens_per_s": 2904.6050776114066,
              "ttft_s": 1.4115855965000002
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.295523306,
              "format_passes": 2,
              "gpu_energy_j": 72.25827229626324,
              "semantic_passes": 2,
              "tokens_per_s": 78.59601877571754,
              "ttft_s": 0.0791820835
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3532347255,
              "format_passes": 2,
              "gpu_energy_j": 85.917373799672,
              "semantic_passes": 2,
              "tokens_per_s": 78.79110132592652,
              "ttft_s": 0.073957999
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.374681491,
              "format_passes": 2,
              "gpu_energy_j": 95.75979887847265,
              "semantic_passes": 2,
              "tokens_per_s": 77.4731260467833,
              "ttft_s": 0.0777146345
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.62021276,
              "format_passes": 0,
              "gpu_energy_j": 161.28452017095293,
              "semantic_passes": 0,
              "tokens_per_s": 78.85079245139161,
              "ttft_s": 0.3184813855
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5611545265,
              "format_passes": 0,
              "gpu_energy_j": 140.8139526352868,
              "semantic_passes": 0,
              "tokens_per_s": 78.74468119338954,
              "ttft_s": 0.256482212
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
              "e2e_s": 0.679762669,
              "format_passes": 2,
              "gpu_energy_j": 179.99419778174894,
              "semantic_passes": 2,
              "tokens_per_s": 77.56742715953253,
              "ttft_s": 0.125361029
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6910267815,
              "format_passes": 0,
              "gpu_energy_j": 449.92991458386905,
              "semantic_passes": 0,
              "tokens_per_s": 78.09168518609735,
              "ttft_s": 0.0646342895
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.24525177050000002,
              "format_passes": 2,
              "gpu_energy_j": 59.02122179958957,
              "semantic_passes": 2,
              "tokens_per_s": 75.67797530648808,
              "ttft_s": 0.073400944
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.248925351,
              "format_passes": 0,
              "gpu_energy_j": 61.3036527836206,
              "semantic_passes": 0,
              "tokens_per_s": 74.09150426762162,
              "ttft_s": 0.1274001245
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.18987604200000002,
              "format_passes": 2,
              "gpu_energy_j": 43.49408493511753,
              "semantic_passes": 2,
              "tokens_per_s": 74.26634617256809,
              "ttft_s": 0.068630481
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.36710551199999997,
              "format_passes": 0,
              "gpu_energy_j": 92.24346429701573,
              "semantic_passes": 0,
              "tokens_per_s": 76.72349027262314,
              "ttft_s": 0.0803542175
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4823058045,
              "format_passes": 0,
              "gpu_energy_j": 117.52938409467329,
              "semantic_passes": 2,
              "tokens_per_s": 76.99636985869017,
              "ttft_s": 0.1186287915
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0946338115,
              "format_passes": 2,
              "gpu_energy_j": 284.8558862087579,
              "semantic_passes": 2,
              "tokens_per_s": 75.74543095864497,
              "ttft_s": 0.83054496
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2412787535,
              "format_passes": 0,
              "gpu_energy_j": 57.634093463196194,
              "semantic_passes": 0,
              "tokens_per_s": 75.48189842366438,
              "ttft_s": 0.069013463
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.200425482,
              "format_passes": 0,
              "gpu_energy_j": 49.21728899181076,
              "semantic_passes": 0,
              "tokens_per_s": 2532.585210124749,
              "ttft_s": 0.2002931195
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.724572861,
              "format_passes": 0,
              "gpu_energy_j": 188.82815713099032,
              "semantic_passes": 0,
              "tokens_per_s": 2831.429835142849,
              "ttft_s": 0.7243384855
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.439249373,
              "format_passes": 0,
              "gpu_energy_j": 385.25130535408937,
              "semantic_passes": 0,
              "tokens_per_s": 2849.226707468416,
              "ttft_s": 1.4389454325000002
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3040868575,
              "format_passes": 2,
              "gpu_energy_j": 71.17478542934487,
              "semantic_passes": 2,
              "tokens_per_s": 76.02764575073876,
              "ttft_s": 0.080396253
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3632364225,
              "format_passes": 2,
              "gpu_energy_j": 88.53161139674543,
              "semantic_passes": 2,
              "tokens_per_s": 76.65221085934692,
              "ttft_s": 0.076204734
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.37917095349999996,
              "format_passes": 2,
              "gpu_energy_j": 97.0203093907862,
              "semantic_passes": 2,
              "tokens_per_s": 76.78302527360475,
              "ttft_s": 0.0795357525
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.632182346,
              "format_passes": 0,
              "gpu_energy_j": 162.59429106323628,
              "semantic_passes": 0,
              "tokens_per_s": 77.0978594268073,
              "ttft_s": 0.325706701
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.56976938,
              "format_passes": 0,
              "gpu_energy_j": 146.85468887155412,
              "semantic_passes": 0,
              "tokens_per_s": 76.75481204841341,
              "ttft_s": 0.257135498
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
            "e2e_change_pct": 1.9490992174948651,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.8854050832140201,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -2.0521919289012924,
            "ttft_change_pct": 1.2859718436277978
          },
          "decode": {
            "e2e_change_pct": 1.94753393833913,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.3218678011439158,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -1.8986733028866554,
            "ttft_change_pct": 2.2775159489246466
          },
          "energy": {
            "e2e_change_pct": 3.049258055320214,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.3533298796138302,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -3.2405294299016063,
            "ttft_change_pct": 2.3041076626777235
          },
          "filtering": {
            "e2e_change_pct": 2.8159246027694262,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.611994833377861,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -4.327821131202314,
            "ttft_change_pct": 1.2061493209320373
          },
          "german": {
            "e2e_change_pct": 3.800705597653664,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 11.605741384332813,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -3.740944475549335,
            "ttft_change_pct": 3.5660820727002607
          },
          "ha_sim": {
            "e2e_change_pct": 2.42995915749713,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.735053602296156,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -2.7146199462580345,
            "ttft_change_pct": 1.2681548061174164
          },
          "jarvis_memory": {
            "e2e_change_pct": 2.5893284869892508,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.6600188149848307,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -2.45990057624339,
            "ttft_change_pct": 2.8052803264150716
          },
          "long_context": {
            "e2e_change_pct": 1.5652744344530012,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.010485202570809093,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -2.9145369563899792,
            "ttft_change_pct": 1.1213134172459283
          },
          "math": {
            "e2e_change_pct": 3.3394180397844586,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 6.099593080748167,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -3.5510840813965716,
            "ttft_change_pct": 2.5053099274700896
          },
          "prefill": {
            "e2e_change_pct": 1.316254339527645,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.41550020538738686,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -1.3253189598654624,
            "ttft_change_pct": 1.3171789420827196
          },
          "prefill2048": {
            "e2e_change_pct": 1.1699125230405727,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.6221200153812445,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -1.1559361529612011,
            "ttft_change_pct": 1.1665062090231437
          },
          "prefill4096": {
            "e2e_change_pct": 1.9361359705366565,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.5862106497010808,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -1.9065714155031,
            "ttft_change_pct": 1.9382342854615597
          },
          "pve_sim": {
            "e2e_change_pct": 2.897758425861685,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.4994641201439451,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -3.267815679453079,
            "ttft_change_pct": 1.5333891788790854
          },
          "sorting": {
            "e2e_change_pct": 2.8314591624146512,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.0427345267429518,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -2.7146345597225285,
            "ttft_change_pct": 3.0378526060446776
          },
          "time": {
            "e2e_change_pct": 1.1982077065023633,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.316325354769421,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.8907614916194628,
            "ttft_change_pct": 2.3433398506171876
          },
          "tool-call": {
            "e2e_change_pct": 1.929916114592678,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.8120871680028952,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -2.2231013412641665,
            "ttft_change_pct": 2.2686774891589323
          },
          "tool-final": {
            "e2e_change_pct": 1.5352016411116054,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.289870515823835,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -2.526988635701244,
            "ttft_change_pct": 0.25471006153052755
          }
        }
      },
      "complete": true
    }
  }
}
```

</details>
