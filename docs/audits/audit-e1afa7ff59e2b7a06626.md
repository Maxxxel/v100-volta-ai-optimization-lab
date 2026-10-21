# Public audit excerpt

Original SHA256: `e1afa7ff59e2b7a066260ac38fa77144159bc53069dc2e374f93f591f0a846d3`

Original file: `RESULTS.json`; 38366 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{}
```

## Selected aggregate measurements

```json
{
  "models": {
    "qwen38": {
      "arms": {
        "A": {
          "format_passes": 12,
          "quality_attempts": 24,
          "quality_passes": 20,
          "tasks": {
            "code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.7632378329999998,
              "format_passes": 2,
              "gpu_energy_j": 481.31630922974307,
              "semantic_passes": 2,
              "tokens_per_s": 35.402855718532464,
              "ttft_s": 0.5203915585
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.782205922,
              "format_passes": 0,
              "gpu_energy_j": 1069.3507969344948,
              "semantic_passes": 0,
              "tokens_per_s": 35.40747689229907,
              "ttft_s": 0.1949096415
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5811629945000001,
              "format_passes": 2,
              "gpu_energy_j": 146.5386343475701,
              "semantic_passes": 2,
              "tokens_per_s": 34.97067527829001,
              "ttft_s": 0.209411089
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9243577955,
              "format_passes": 0,
              "gpu_energy_j": 240.59940116719724,
              "semantic_passes": 0,
              "tokens_per_s": 35.00771388939348,
              "ttft_s": 0.5244313805
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4667132845,
              "format_passes": 2,
              "gpu_energy_j": 110.34153376631733,
              "semantic_passes": 2,
              "tokens_per_s": 34.23898550195382,
              "ttft_s": 0.20382290749999998
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.989413425,
              "format_passes": 0,
              "gpu_energy_j": 264.6567684498791,
              "semantic_passes": 0,
              "tokens_per_s": 35.278431511528275,
              "ttft_s": 0.224033306
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.144341588,
              "format_passes": 0,
              "gpu_energy_j": 300.22265803337916,
              "semantic_passes": 2,
              "tokens_per_s": 35.34269027157053,
              "ttft_s": 0.352083685
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.792547404,
              "format_passes": 2,
              "gpu_energy_j": 1015.190463933181,
              "semantic_passes": 2,
              "tokens_per_s": 34.391656427438576,
              "ttft_s": 3.210893251
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5735861955,
              "format_passes": 2,
              "gpu_energy_j": 143.65651812759123,
              "semantic_passes": 2,
              "tokens_per_s": 34.937831317299114,
              "ttft_s": 0.201479604
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7254033280000001,
              "format_passes": 0,
              "gpu_energy_j": 189.43974962882987,
              "semantic_passes": 0,
              "tokens_per_s": 697.1128090278003,
              "ttft_s": 0.725273811
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.7435564230000002,
              "format_passes": 0,
              "gpu_energy_j": 736.5264111511112,
              "semantic_passes": 0,
              "tokens_per_s": 746.8312002275491,
              "ttft_s": 2.7433012555
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8467171705000001,
              "format_passes": 0,
              "gpu_energy_j": 225.47018809066924,
              "semantic_passes": 2,
              "tokens_per_s": 35.24022357325242,
              "ttft_s": 0.2223962015
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.985761935,
              "format_passes": 0,
              "gpu_energy_j": 263.0111449657861,
              "semantic_passes": 2,
              "tokens_per_s": 35.07465466194729,
              "ttft_s": 0.215953448
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.014897915,
              "format_passes": 0,
              "gpu_energy_j": 276.2504052355805,
              "semantic_passes": 2,
              "tokens_per_s": 35.27199765021829,
              "ttft_s": 0.22104416799999999
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.708868596,
              "format_passes": 0,
              "gpu_energy_j": 454.97534833432417,
              "semantic_passes": 0,
              "tokens_per_s": 35.02798017836221,
              "ttft_s": 1.030169275
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.777176369,
              "format_passes": 0,
              "gpu_energy_j": 467.2473540286721,
              "semantic_passes": 0,
              "tokens_per_s": 35.112693551465625,
              "ttft_s": 1.0930795805
            }
          }
        },
        "B": {
          "format_passes": 12,
          "quality_attempts": 24,
          "quality_passes": 20,
          "tasks": {
            "code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.761597616,
              "format_passes": 2,
              "gpu_energy_j": 480.3849207840396,
              "semantic_passes": 2,
              "tokens_per_s": 35.43774559818826,
              "ttft_s": 0.519938628
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.775414176,
              "format_passes": 0,
              "gpu_energy_j": 1065.659475857845,
              "semantic_passes": 0,
              "tokens_per_s": 35.464116202555,
              "ttft_s": 0.19426967
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.578735555,
              "format_passes": 2,
              "gpu_energy_j": 150.15815767567284,
              "semantic_passes": 2,
              "tokens_per_s": 35.049092601905784,
              "ttft_s": 0.207775499
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.924164553,
              "format_passes": 0,
              "gpu_energy_j": 244.1850275330014,
              "semantic_passes": 0,
              "tokens_per_s": 34.99390060803958,
              "ttft_s": 0.5240604375
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.463859829,
              "format_passes": 2,
              "gpu_energy_j": 111.06827117448135,
              "semantic_passes": 2,
              "tokens_per_s": 34.31290943299781,
              "ttft_s": 0.20151939149999998
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.993207823,
              "format_passes": 0,
              "gpu_energy_j": 266.2090451161981,
              "semantic_passes": 0,
              "tokens_per_s": 35.19910507196376,
              "ttft_s": 0.226061146
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.146987036,
              "format_passes": 0,
              "gpu_energy_j": 295.1618342114788,
              "semantic_passes": 2,
              "tokens_per_s": 35.3123982966473,
              "ttft_s": 0.3540339335
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.7966222125,
              "format_passes": 2,
              "gpu_energy_j": 1026.0019489404065,
              "semantic_passes": 2,
              "tokens_per_s": 34.36787925780628,
              "ttft_s": 3.214636053
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5732057765,
              "format_passes": 2,
              "gpu_energy_j": 141.59149275536623,
              "semantic_passes": 2,
              "tokens_per_s": 34.99466631968817,
              "ttft_s": 0.20169417550000002
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7268106320000001,
              "format_passes": 0,
              "gpu_energy_j": 187.80138005127003,
              "semantic_passes": 0,
              "tokens_per_s": 695.8021972249039,
              "ttft_s": 0.7266823185
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.7499800199999997,
              "format_passes": 0,
              "gpu_energy_j": 739.5917033705155,
              "semantic_passes": 0,
              "tokens_per_s": 745.0786869360928,
              "ttft_s": 2.749716853
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8467495174999999,
              "format_passes": 0,
              "gpu_energy_j": 223.5878301320239,
              "semantic_passes": 2,
              "tokens_per_s": 35.24777508926873,
              "ttft_s": 0.222555842
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9882086875,
              "format_passes": 0,
              "gpu_energy_j": 261.0261939241886,
              "semantic_passes": 2,
              "tokens_per_s": 35.03053360541978,
              "ttft_s": 0.2174348535
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.014029107,
              "format_passes": 0,
              "gpu_energy_j": 275.2874109512378,
              "semantic_passes": 2,
              "tokens_per_s": 35.3696745652473,
              "ttft_s": 0.222333308
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.704053605,
              "format_passes": 0,
              "gpu_energy_j": 457.00617089982813,
              "semantic_passes": 0,
              "tokens_per_s": 35.141850396490696,
              "ttft_s": 1.0277115884999999
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.775608397,
              "format_passes": 0,
              "gpu_energy_j": 464.4007481590434,
              "semantic_passes": 0,
              "tokens_per_s": 35.14220837359308,
              "ttft_s": 1.0922431205
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
            "e2e_change_pct": -0.09302301534723778,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.1935085987827767,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.09855103196527715,
            "ttft_change_pct": -0.08703648101162642
          },
          "decode": {
            "e2e_change_pct": -0.17957102654021506,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.34519271760320436,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.15996426525450858,
            "ttft_change_pct": -0.32834265923166184
          },
          "energy": {
            "e2e_change_pct": -0.41768652219306146,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.4700130066162007,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.22423737314691827,
            "ttft_change_pct": -0.7810426887183586
          },
          "filtering": {
            "e2e_change_pct": -0.02090559531608971,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.4902889817719922,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.03945782177476875,
            "ttft_change_pct": -0.07073241872872504
          },
          "german": {
            "e2e_change_pct": -0.6113936746105164,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.6586254362777932,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.21590572839775835,
            "ttft_change_pct": -1.1301555984329248
          },
          "ha_sim": {
            "e2e_change_pct": 0.38349974885372173,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.5865244540734338,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.22485818151692927,
            "ttft_change_pct": 0.9051511296271242
          },
          "jarvis_memory": {
            "e2e_change_pct": 0.23117642736585342,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.6856901657761325,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.08570930704615565,
            "ttft_change_pct": 0.5539161804671622
          },
          "long_context": {
            "e2e_change_pct": 0.10744251991952058,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.064971095703382,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.06913644791277651,
            "ttft_change_pct": 0.11656575623728571
          },
          "math": {
            "e2e_change_pct": -0.06632290019956688,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.4374741913143807,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.16267467168438188,
            "ttft_change_pct": 0.1064978765791258
          },
          "prefill": {
            "e2e_change_pct": 0.19400296988987265,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.8648499487409089,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.1880056980625766,
            "ttft_change_pct": 0.19420355162940162
          },
          "prefill2048": {
            "e2e_change_pct": 0.23413394913800456,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.41618225402311193,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.2346598924793497,
            "ttft_change_pct": 0.2338641258278651
          },
          "pve_sim": {
            "e2e_change_pct": 0.003820283930311419,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.8348589117637029,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.021428683619473254,
            "ttft_change_pct": 0.0717820263670399
          },
          "sorting": {
            "e2e_change_pct": 0.24820926971582669,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.7547022548629045,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.12579184870886717,
            "ttft_change_pct": 0.6859837218250897
          },
          "time": {
            "e2e_change_pct": -0.08560545717545276,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.348594704692462,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.2769248172378669,
            "ttft_change_pct": 0.5832047104721738
          },
          "tool-call": {
            "e2e_change_pct": -0.28176484788068334,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.44635881327173,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.3250835975944222,
            "ttft_change_pct": -0.23857113191423363
          },
          "tool-final": {
            "e2e_change_pct": -0.0882282719571692,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.6092288902408649,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.08405741383581411,
            "ttft_change_pct": -0.07652324816252998
          }
        }
      },
      "complete": true
    }
  }
}
```
