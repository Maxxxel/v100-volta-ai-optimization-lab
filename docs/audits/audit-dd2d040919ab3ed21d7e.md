# Public audit excerpt

Original SHA256: `dd2d040919ab3ed21d7ef6218c85b5c30b233602f961de26a35a69be6c1c35a0`

Original file: `RESULTS.json`; 43134 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 3.118112163,
              "format_passes": 2,
              "gpu_energy_j": 690.2604213932964,
              "semantic_passes": 2,
              "tokens_per_s": 14.63460128391114,
              "ttft_s": 0.17981994299999998
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 8.815778114499999,
              "format_passes": 0,
              "gpu_energy_j": 1992.4650891376518,
              "semantic_passes": 0,
              "tokens_per_s": 14.654264931047377,
              "ttft_s": 0.1494328105
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.056008953,
              "format_passes": 2,
              "gpu_energy_j": 232.58021655371977,
              "semantic_passes": 2,
              "tokens_per_s": 14.584872936908507,
              "ttft_s": 0.1645963215
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8001803045,
              "format_passes": 0,
              "gpu_energy_j": 173.09881072143327,
              "semantic_passes": 0,
              "tokens_per_s": 14.552028025121704,
              "ttft_s": 0.1816432765
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.771403762,
              "format_passes": 2,
              "gpu_energy_j": 163.20364194621595,
              "semantic_passes": 2,
              "tokens_per_s": 14.543457477099157,
              "ttft_s": 0.1525039805
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.6713699665,
              "format_passes": 0,
              "gpu_energy_j": 369.63165021836886,
              "semantic_passes": 0,
              "tokens_per_s": 14.613420320487336,
              "ttft_s": 0.16585990350000002
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 2.151075809,
              "format_passes": 0,
              "gpu_energy_j": 474.37500682263516,
              "semantic_passes": 2,
              "tokens_per_s": 14.626921024441973,
              "ttft_s": 0.236763308
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 2.2613729725000002,
              "format_passes": 2,
              "gpu_energy_j": 531.7324288548539,
              "semantic_passes": 2,
              "tokens_per_s": 14.562841395235669,
              "ttft_s": 0.88797657
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.055160477,
              "format_passes": 0,
              "gpu_energy_j": 231.16739391142733,
              "semantic_passes": 0,
              "tokens_per_s": 14.584226149815281,
              "ttft_s": 0.1637200215
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.2557961595,
              "format_passes": 0,
              "gpu_energy_j": 59.78557758335215,
              "semantic_passes": 0,
              "tokens_per_s": 1982.2588688195856,
              "ttft_s": 0.255669384
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.776560658,
              "format_passes": 0,
              "gpu_energy_j": 203.40314559056037,
              "semantic_passes": 0,
              "tokens_per_s": 2641.37095938289,
              "ttft_s": 0.7763044815
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4783484420000002,
              "format_passes": 0,
              "gpu_energy_j": 396.9587789880472,
              "semantic_passes": 0,
              "tokens_per_s": 2773.8103022828636,
              "ttft_s": 1.4780358580000001
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.331326479,
              "format_passes": 2,
              "gpu_energy_j": 291.7306432603084,
              "semantic_passes": 2,
              "tokens_per_s": 14.602035297621834,
              "ttft_s": 0.1670294015
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.672955145,
              "format_passes": 2,
              "gpu_energy_j": 370.45903968171706,
              "semantic_passes": 2,
              "tokens_per_s": 14.61148591191468,
              "ttft_s": 0.1672042915
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.737852321,
              "format_passes": 2,
              "gpu_energy_j": 385.48513861188246,
              "semantic_passes": 2,
              "tokens_per_s": 14.62022246535907,
              "ttft_s": 0.16463040899999998
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.556481715,
              "format_passes": 0,
              "gpu_energy_j": 581.3440402962334,
              "semantic_passes": 0,
              "tokens_per_s": 14.628590072557024,
              "ttft_s": 0.919611607
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.9557437575,
              "format_passes": 0,
              "gpu_energy_j": 445.1075720560584,
              "semantic_passes": 0,
              "tokens_per_s": 14.616900398669634,
              "ttft_s": 0.3135591495
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
              "e2e_s": 0.566645775,
              "format_passes": 2,
              "gpu_energy_j": 149.2402113922698,
              "semantic_passes": 2,
              "tokens_per_s": 79.28230928538912,
              "ttft_s": 0.08733561349999999
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.656765686,
              "format_passes": 0,
              "gpu_energy_j": 462.60336747787994,
              "semantic_passes": 0,
              "tokens_per_s": 79.67727598447044,
              "ttft_s": 0.062802736
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23833014749999998,
              "format_passes": 2,
              "gpu_energy_j": 59.1281470072172,
              "semantic_passes": 2,
              "tokens_per_s": 78.26070856043151,
              "ttft_s": 0.0721865455
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2092610035,
              "format_passes": 0,
              "gpu_energy_j": 49.81337418040094,
              "semantic_passes": 0,
              "tokens_per_s": 77.4023774566388,
              "ttft_s": 0.092975912
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.182484663,
              "format_passes": 2,
              "gpu_energy_j": 43.32571161814246,
              "semantic_passes": 2,
              "tokens_per_s": 77.46084204027028,
              "ttft_s": 0.066284337
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3578611355,
              "format_passes": 0,
              "gpu_energy_j": 90.24308257620916,
              "semantic_passes": 0,
              "tokens_per_s": 78.86397163342568,
              "ttft_s": 0.0788936015
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4680485435,
              "format_passes": 0,
              "gpu_energy_j": 118.655310984887,
              "semantic_passes": 2,
              "tokens_per_s": 79.10062719061477,
              "ttft_s": 0.11399361
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.4751468884999999,
              "format_passes": 2,
              "gpu_energy_j": 412.3317974232526,
              "semantic_passes": 2,
              "tokens_per_s": 78.1618732581203,
              "ttft_s": 1.219222968
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2334589205,
              "format_passes": 0,
              "gpu_energy_j": 57.801415648889474,
              "semantic_passes": 0,
              "tokens_per_s": 78.23720094533456,
              "ttft_s": 0.0672876015
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.2999514345,
              "format_passes": 0,
              "gpu_energy_j": 79.55693943619826,
              "semantic_passes": 0,
              "tokens_per_s": 1689.4915300025846,
              "ttft_s": 0.299818698
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.1179329505,
              "format_passes": 0,
              "gpu_energy_j": 316.6517493884319,
              "semantic_passes": 0,
              "tokens_per_s": 1834.0695816608522,
              "ttft_s": 1.1176857055
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.216810821,
              "format_passes": 0,
              "gpu_energy_j": 635.408554991586,
              "semantic_passes": 0,
              "tokens_per_s": 1849.09306397634,
              "ttft_s": 2.2165067680000003
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2954766425,
              "format_passes": 2,
              "gpu_energy_j": 75.28496109233157,
              "semantic_passes": 2,
              "tokens_per_s": 78.61271751107121,
              "ttft_s": 0.0792177815
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35286572650000003,
              "format_passes": 2,
              "gpu_energy_j": 91.88788256377825,
              "semantic_passes": 2,
              "tokens_per_s": 78.85389522482254,
              "ttft_s": 0.0738655215
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.368829159,
              "format_passes": 2,
              "gpu_energy_j": 91.30866352185274,
              "semantic_passes": 2,
              "tokens_per_s": 78.94472515436632,
              "ttft_s": 0.0774465
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6580118454999999,
              "format_passes": 0,
              "gpu_energy_j": 178.143448289525,
              "semantic_passes": 0,
              "tokens_per_s": 79.07117724360491,
              "ttft_s": 0.3568286205
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5928203125,
              "format_passes": 0,
              "gpu_energy_j": 156.4796058615137,
              "semantic_passes": 0,
              "tokens_per_s": 78.91141709650483,
              "ttft_s": 0.28875894199999996
            }
          }
        }
      },
      "change_exercised": true,
      "comparison": {
        "format_pass_change": 0,
        "note": "Existing baseline errors do not suppress speed results. Two starts per arm; no independent confirmation claimed.",
        "quality_pass_change": 0,
        "status": "DESCRIPTIVE_COMPARISON",
        "tasks": {
          "code": {
            "e2e_change_pct": -81.82728056662278,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -78.37914404957085,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 441.74560514026314,
            "ttft_change_pct": -51.43163097321191
          },
          "decode": {
            "e2e_change_pct": -81.20681277952097,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -76.78236020295357,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 443.71390417312256,
            "ttft_change_pct": -57.97259263888368
          },
          "energy": {
            "e2e_change_pct": -77.43104858884658,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -74.57731019286406,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 436.5882095714719,
            "ttft_change_pct": -56.1432814280725
          },
          "filtering": {
            "e2e_change_pct": -73.84826865605514,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -71.2225786111464,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 431.90096475224084,
            "ttft_change_pct": -48.81400853832319
          },
          "german": {
            "e2e_change_pct": -76.34381993070964,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -73.45297500626822,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 432.6164164349772,
            "ttft_change_pct": -56.535995465377376
          },
          "ha_sim": {
            "e2e_change_pct": -78.58875397591393,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -75.58567224346295,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 439.66812631032076,
            "ttft_change_pct": -52.43359013530357
          },
          "jarvis_memory": {
            "e2e_change_pct": -78.24118789576328,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -74.98702307702918,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 440.7879557046594,
            "ttft_change_pct": -51.85334629637799
          },
          "long_context": {
            "e2e_change_pct": -34.767643089446196,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -22.45502153945059,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 436.72131101895724,
            "ttft_change_pct": 37.303506555358766
          },
          "math": {
            "e2e_change_pct": -77.87455789059089,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -74.99586136657477,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 436.45082119304277,
            "ttft_change_pct": -58.90081073560084
          },
          "prefill": {
            "e2e_change_pct": 17.26189911776217,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 33.07045386536773,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -14.76937969213582,
            "ttft_change_pct": 17.26812702767728
          },
          "prefill2048": {
            "e2e_change_pct": 43.959514171010206,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 55.67691859880814,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -30.56372581269877,
            "ttft_change_pct": 43.97517110043889
          },
          "prefill4096": {
            "e2e_change_pct": 49.951848834836454,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 60.06915292600665,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -33.3374361449835,
            "ttft_change_pct": 49.96299014012149
          },
          "pve_sim": {
            "e2e_change_pct": -77.80584648763679,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -74.19367391407164,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 438.3682199691334,
            "ttft_change_pct": -52.572552623317634
          },
          "sorting": {
            "e2e_change_pct": -78.90763972037038,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -75.19620991224171,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 439.6706105059617,
            "ttft_change_pct": -55.823190399392345
          },
          "time": {
            "e2e_change_pct": -78.77672604610228,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -76.31331162320502,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 439.96938378616835,
            "ttft_change_pct": -52.95735431234942
          },
          "tool-call": {
            "e2e_change_pct": -74.2610384561268,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -69.35662259498712,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 440.5249367944285,
            "ttft_change_pct": -61.19789944104087
          },
          "tool-final": {
            "e2e_change_pct": -69.68824212136083,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -64.84454192978633,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 439.8642321164548,
            "ttft_change_pct": -7.9092597168816
          }
        }
      },
      "complete": true,
      "numerical_results": [
        {
          "begin_ns": 340793460732267,
          "end_ns": 340794268830127,
          "model": "omnicoder2",
          "passed": true,
          "reference": "existing CPU reference backend",
          "returncode": 0
        },
        {
          "begin_ns": 340896462749712,
          "end_ns": 340897068709465,
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
