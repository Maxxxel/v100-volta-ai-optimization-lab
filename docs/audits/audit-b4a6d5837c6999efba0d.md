# Public audit excerpt

Original SHA256: `b4a6d5837c6999efba0d25def905ae4eb34f3ceaf30889fe7f601cde21f0b747`

Original file: `RESULTS.json`; 39794 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.6660579,
              "format_passes": 2,
              "gpu_energy_j": 175.17549313803812,
              "semantic_passes": 2,
              "tokens_per_s": 79.36046722438883,
              "ttft_s": 0.124198894
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6582598195,
              "format_passes": 0,
              "gpu_energy_j": 459.6893908645376,
              "semantic_passes": 0,
              "tokens_per_s": 79.6312883499462,
              "ttft_s": 0.0632424405
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23792553049999998,
              "format_passes": 2,
              "gpu_energy_j": 55.095357581972394,
              "semantic_passes": 2,
              "tokens_per_s": 78.17952618991343,
              "ttft_s": 0.07159670800000001
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2416542115,
              "format_passes": 0,
              "gpu_energy_j": 58.88084920637512,
              "semantic_passes": 0,
              "tokens_per_s": 77.50053221323301,
              "ttft_s": 0.125498947
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.182426286,
              "format_passes": 2,
              "gpu_energy_j": 38.282700063807276,
              "semantic_passes": 2,
              "tokens_per_s": 77.5033734280341,
              "ttft_s": 0.0662696365
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.357791629,
              "format_passes": 0,
              "gpu_energy_j": 90.95256268482417,
              "semantic_passes": 0,
              "tokens_per_s": 78.8725535627351,
              "ttft_s": 0.07879248750000001
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.46875183750000005,
              "format_passes": 0,
              "gpu_energy_j": 119.54754042431429,
              "semantic_passes": 2,
              "tokens_per_s": 79.09180127082817,
              "ttft_s": 0.1147389695
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0806863015000001,
              "format_passes": 2,
              "gpu_energy_j": 287.3230525693856,
              "semantic_passes": 2,
              "tokens_per_s": 77.85040916888664,
              "ttft_s": 0.823764693
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.233725299,
              "format_passes": 0,
              "gpu_energy_j": 55.857584675868694,
              "semantic_passes": 0,
              "tokens_per_s": 78.12010753230302,
              "ttft_s": 0.067281095
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.198873679,
              "format_passes": 0,
              "gpu_energy_j": 50.07884970430816,
              "semantic_passes": 0,
              "tokens_per_s": 2553.083998589262,
              "ttft_s": 0.198713967
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7187498625,
              "format_passes": 0,
              "gpu_energy_j": 189.47431065510776,
              "semantic_passes": 0,
              "tokens_per_s": 2854.182376141381,
              "ttft_s": 0.718520079
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4181580205,
              "format_passes": 0,
              "gpu_energy_j": 380.28764184092444,
              "semantic_passes": 0,
              "tokens_per_s": 2891.8557284136623,
              "ttft_s": 1.417830395
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.29506583249999996,
              "format_passes": 2,
              "gpu_energy_j": 75.97345995679584,
              "semantic_passes": 2,
              "tokens_per_s": 78.55625288544172,
              "ttft_s": 0.078609738
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3527571505,
              "format_passes": 2,
              "gpu_energy_j": 89.93720808238022,
              "semantic_passes": 2,
              "tokens_per_s": 78.86808044538637,
              "ttft_s": 0.073792423
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.369594348,
              "format_passes": 2,
              "gpu_energy_j": 95.65111698759685,
              "semantic_passes": 2,
              "tokens_per_s": 78.76267792221051,
              "ttft_s": 0.07751057350000001
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6198329840000001,
              "format_passes": 0,
              "gpu_energy_j": 162.5815197344578,
              "semantic_passes": 0,
              "tokens_per_s": 78.98147512179723,
              "ttft_s": 0.31882054800000004
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.561382786,
              "format_passes": 0,
              "gpu_energy_j": 143.748701450312,
              "semantic_passes": 0,
              "tokens_per_s": 78.74765451734407,
              "ttft_s": 0.256569218
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
              "e2e_s": 0.8399372155,
              "format_passes": 2,
              "gpu_energy_j": 199.62873976416915,
              "semantic_passes": 2,
              "tokens_per_s": 65.88472958327807,
              "ttft_s": 0.1265559415
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.9106427865,
              "format_passes": 0,
              "gpu_energy_j": 478.53698254112805,
              "semantic_passes": 0,
              "tokens_per_s": 68.84625715650249,
              "ttft_s": 0.065811379
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.27455191,
              "format_passes": 2,
              "gpu_energy_j": 58.16722520921914,
              "semantic_passes": 2,
              "tokens_per_s": 64.86881157185113,
              "ttft_s": 0.074125132
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.26769603399999997,
              "format_passes": 0,
              "gpu_energy_j": 64.09302620538247,
              "semantic_passes": 0,
              "tokens_per_s": 64.37972218865929,
              "ttft_s": 0.1278487325
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.203809858,
              "format_passes": 2,
              "gpu_energy_j": 43.1274931480158,
              "semantic_passes": 2,
              "tokens_per_s": 66.28836395034183,
              "ttft_s": 0.06801224950000001
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.41870416899999996,
              "format_passes": 0,
              "gpu_energy_j": 94.69809046585243,
              "semantic_passes": 0,
              "tokens_per_s": 65.27184370875104,
              "ttft_s": 0.08161911050000001
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5434861129999999,
              "format_passes": 0,
              "gpu_energy_j": 126.42253752441945,
              "semantic_passes": 2,
              "tokens_per_s": 65.70572062812457,
              "ttft_s": 0.11728237650000001
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1323480385,
              "format_passes": 2,
              "gpu_energy_j": 292.90512502194497,
              "semantic_passes": 2,
              "tokens_per_s": 65.52194656490957,
              "ttft_s": 0.827046486
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2679295465,
              "format_passes": 0,
              "gpu_energy_j": 56.5700505927885,
              "semantic_passes": 0,
              "tokens_per_s": 65.7993336340776,
              "ttft_s": 0.070302424
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.2008415005,
              "format_passes": 0,
              "gpu_energy_j": 49.29200388222166,
              "semantic_passes": 0,
              "tokens_per_s": 2528.1795370101895,
              "ttft_s": 0.20063421650000002
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.72032897,
              "format_passes": 0,
              "gpu_energy_j": 189.91950510876035,
              "semantic_passes": 0,
              "tokens_per_s": 2848.1743378616075,
              "ttft_s": 0.7200830069999999
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4205570905,
              "format_passes": 0,
              "gpu_energy_j": 384.81466844664465,
              "semantic_passes": 0,
              "tokens_per_s": 2886.9395835541127,
              "ttft_s": 1.420219756
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3427025855,
              "format_passes": 2,
              "gpu_energy_j": 80.74829622875097,
              "semantic_passes": 2,
              "tokens_per_s": 65.10728855760098,
              "ttft_s": 0.0815121095
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4098078665,
              "format_passes": 2,
              "gpu_energy_j": 91.91833124930595,
              "semantic_passes": 2,
              "tokens_per_s": 66.00555293265987,
              "ttft_s": 0.076468108
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.42934033400000005,
              "format_passes": 2,
              "gpu_energy_j": 99.15123711829139,
              "semantic_passes": 2,
              "tokens_per_s": 65.9081835194387,
              "ttft_s": 0.080315893
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7098068975,
              "format_passes": 0,
              "gpu_energy_j": 169.27767778093033,
              "semantic_passes": 0,
              "tokens_per_s": 65.39208076103007,
              "ttft_s": 0.345908043
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5904863730000001,
              "format_passes": 0,
              "gpu_energy_j": 143.3183524426475,
              "semantic_passes": 0,
              "tokens_per_s": 66.22048109914479,
              "ttft_s": 0.25770214
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
            "e2e_change_pct": 26.105735777625338,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 13.959285164884271,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -16.98041621026323,
            "ttft_change_pct": 1.8978007163252153
          },
          "decode": {
            "e2e_change_pct": 15.219748077602135,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.100071059100108,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -13.543710540068133,
            "ttft_change_pct": 4.0620483328754675
          },
          "energy": {
            "e2e_change_pct": 15.394051837576983,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 5.575547127861613,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -17.025831783282964,
            "ttft_change_pct": 3.5314808049554225
          },
          "filtering": {
            "e2e_change_pct": 10.776481956740058,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 8.852075113147361,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -16.92996118849024,
            "ttft_change_pct": 1.8723547537016438
          },
          "german": {
            "e2e_change_pct": 11.72176031693153,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 12.655306642774722,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -14.470350104316399,
            "ttft_change_pct": 2.629579837819085
          },
          "ha_sim": {
            "e2e_change_pct": 17.024584999443903,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.1181113214011855,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -17.243907087610754,
            "ttft_change_pct": 3.5874270373809525
          },
          "jarvis_memory": {
            "e2e_change_pct": 15.943249609128184,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 5.750847801388037,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -16.924738629819092,
            "ttft_change_pct": 2.2166897707757593
          },
          "long_context": {
            "e2e_change_pct": 4.780456357066165,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.9427861435557414,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -15.836092238426168,
            "ttft_change_pct": 0.39838961634157677
          },
          "math": {
            "e2e_change_pct": 14.634379609885539,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.2755043402863153,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -15.771578262524443,
            "ttft_change_pct": 4.490606165075062
          },
          "prefill": {
            "e2e_change_pct": 0.9894831281318073,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.571213849224684,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.9754658128300453,
            "ttft_change_pct": 0.9663384657808249
          },
          "prefill2048": {
            "e2e_change_pct": 0.21970195507341472,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.234962962584917,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.21049945266272685,
            "ttft_change_pct": 0.21752043480469663
          },
          "prefill4096": {
            "e2e_change_pct": 0.16916803101774125,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.1904216986398541,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.16999965839397113,
            "ttft_change_pct": 0.16852234289983503
          },
          "pve_sim": {
            "e2e_change_pct": 16.144449052738107,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 6.2848740529527936,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -17.12017036690041,
            "ttft_change_pct": 3.6921271764065677
          },
          "sorting": {
            "e2e_change_pct": 16.172802144233223,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.2027848197278654,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -16.308914126080943,
            "ttft_change_pct": 3.6259617061226157
          },
          "time": {
            "e2e_change_pct": 16.165286705087833,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.6592569338718794,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -16.32054006018877,
            "ttft_change_pct": 3.619273311143778
          },
          "tool-call": {
            "e2e_change_pct": 14.515831816397817,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.118646484181765,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -17.20579963822019,
            "ttft_change_pct": 8.496157217570532
          },
          "tool-final": {
            "e2e_change_pct": 5.184267798336095,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.2993759271023855,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -15.907995603145475,
            "ttft_change_pct": 0.44156583117467285
          }
        }
      },
      "complete": true
    }
  }
}
```

</details>
