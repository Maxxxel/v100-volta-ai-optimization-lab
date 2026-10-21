# Public audit excerpt

Original SHA256: `6df5b60d87a67f761a8b400449440ca137cf0d84723c13f831dfb3f6318689b7`

Original file: `RESULTS.json`; 39630 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.6685270975,
              "format_passes": 2,
              "gpu_energy_j": 172.26446367175973,
              "semantic_passes": 2,
              "tokens_per_s": 79.07509327271302,
              "ttft_s": 0.1246940125
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.660764978,
              "format_passes": 0,
              "gpu_energy_j": 444.69058042429185,
              "semantic_passes": 0,
              "tokens_per_s": 79.50310382752706,
              "ttft_s": 0.0631347515
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2396497835,
              "format_passes": 2,
              "gpu_energy_j": 54.872486995776654,
              "semantic_passes": 2,
              "tokens_per_s": 77.59423347898552,
              "ttft_s": 0.0720666015
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2432773435,
              "format_passes": 0,
              "gpu_energy_j": 60.4223277301129,
              "semantic_passes": 0,
              "tokens_per_s": 77.0225672948425,
              "ttft_s": 0.1263678505
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1830577065,
              "format_passes": 2,
              "gpu_energy_j": 41.43027707646455,
              "semantic_passes": 2,
              "tokens_per_s": 77.2119457013215,
              "ttft_s": 0.0664622935
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3608019885,
              "format_passes": 0,
              "gpu_energy_j": 88.43073605013284,
              "semantic_passes": 0,
              "tokens_per_s": 78.00621847288386,
              "ttft_s": 0.0786749625
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.471922905,
              "format_passes": 0,
              "gpu_energy_j": 117.87751443088436,
              "semantic_passes": 2,
              "tokens_per_s": 78.62732544355781,
              "ttft_s": 0.115750542
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.075477853,
              "format_passes": 2,
              "gpu_energy_j": 285.5521521964333,
              "semantic_passes": 2,
              "tokens_per_s": 77.79569892520706,
              "ttft_s": 0.818335858
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.234858259,
              "format_passes": 0,
              "gpu_energy_j": 52.51303779724367,
              "semantic_passes": 0,
              "tokens_per_s": 77.88197565338376,
              "ttft_s": 0.06782637350000001
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.198527316,
              "format_passes": 0,
              "gpu_energy_j": 47.206153000498006,
              "semantic_passes": 0,
              "tokens_per_s": 2557.1018933191986,
              "ttft_s": 0.198370895
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7131926835,
              "format_passes": 0,
              "gpu_energy_j": 188.9347961187736,
              "semantic_passes": 0,
              "tokens_per_s": 2876.6356587695736,
              "ttft_s": 0.712956232
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.408997083,
              "format_passes": 0,
              "gpu_energy_j": 377.6518395661633,
              "semantic_passes": 0,
              "tokens_per_s": 2910.7681892241444,
              "ttft_s": 1.40863706
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.297900167,
              "format_passes": 2,
              "gpu_energy_j": 73.2774208951796,
              "semantic_passes": 2,
              "tokens_per_s": 78.03899606178322,
              "ttft_s": 0.0799967415
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.355116559,
              "format_passes": 2,
              "gpu_energy_j": 88.89595179049479,
              "semantic_passes": 2,
              "tokens_per_s": 78.34594606001295,
              "ttft_s": 0.07422682850000001
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.37042991449999996,
              "format_passes": 2,
              "gpu_energy_j": 93.41434177691488,
              "semantic_passes": 2,
              "tokens_per_s": 78.61714863202482,
              "ttft_s": 0.07782364
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.619837865,
              "format_passes": 0,
              "gpu_energy_j": 158.60758405757616,
              "semantic_passes": 0,
              "tokens_per_s": 78.79848856763829,
              "ttft_s": 0.31773235
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5611269525,
              "format_passes": 0,
              "gpu_energy_j": 142.90239688310766,
              "semantic_passes": 0,
              "tokens_per_s": 78.588207213196,
              "ttft_s": 0.255408187
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
              "e2e_s": 0.670561023,
              "format_passes": 2,
              "gpu_energy_j": 172.00822575629584,
              "semantic_passes": 2,
              "tokens_per_s": 78.79882103707385,
              "ttft_s": 0.1248113405
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.671344265,
              "format_passes": 0,
              "gpu_energy_j": 445.53809216142014,
              "semantic_passes": 0,
              "tokens_per_s": 79.01400970834308,
              "ttft_s": 0.0634331065
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.240898801,
              "format_passes": 2,
              "gpu_energy_j": 57.57900221911683,
              "semantic_passes": 2,
              "tokens_per_s": 77.42657033692676,
              "ttft_s": 0.07292720450000001
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.242578503,
              "format_passes": 0,
              "gpu_energy_j": 60.53635601132432,
              "semantic_passes": 0,
              "tokens_per_s": 77.15731908252835,
              "ttft_s": 0.1259054495
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1840686375,
              "format_passes": 2,
              "gpu_energy_j": 42.62911442564843,
              "semantic_passes": 2,
              "tokens_per_s": 76.98579198428733,
              "ttft_s": 0.0671394315
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.359400847,
              "format_passes": 0,
              "gpu_energy_j": 87.61080747370957,
              "semantic_passes": 0,
              "tokens_per_s": 78.4213179470652,
              "ttft_s": 0.0787988355
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.473194791,
              "format_passes": 0,
              "gpu_energy_j": 112.71602239454432,
              "semantic_passes": 2,
              "tokens_per_s": 78.35005110850047,
              "ttft_s": 0.115781716
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0774899549999999,
              "format_passes": 2,
              "gpu_energy_j": 284.0310001895789,
              "semantic_passes": 2,
              "tokens_per_s": 77.3675589652128,
              "ttft_s": 0.8189304265
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.234546683,
              "format_passes": 0,
              "gpu_energy_j": 52.78730243768371,
              "semantic_passes": 0,
              "tokens_per_s": 77.87930340369095,
              "ttft_s": 0.06753698450000001
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.198521406,
              "format_passes": 0,
              "gpu_energy_j": 47.5593470027339,
              "semantic_passes": 0,
              "tokens_per_s": 2557.90801129226,
              "ttft_s": 0.198383366
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.713556261,
              "format_passes": 0,
              "gpu_energy_j": 187.4229899577016,
              "semantic_passes": 0,
              "tokens_per_s": 2875.354506652504,
              "ttft_s": 0.7133663155000001
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4087537725,
              "format_passes": 0,
              "gpu_energy_j": 380.6890076174618,
              "semantic_passes": 0,
              "tokens_per_s": 2910.939677828973,
              "ttft_s": 1.408470893
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2983405315,
              "format_passes": 2,
              "gpu_energy_j": 71.13580977952077,
              "semantic_passes": 2,
              "tokens_per_s": 77.84192894634495,
              "ttft_s": 0.079920045
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.355949037,
              "format_passes": 2,
              "gpu_energy_j": 88.08804695401784,
              "semantic_passes": 2,
              "tokens_per_s": 78.2420740496189,
              "ttft_s": 0.07471381099999999
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.37224914249999996,
              "format_passes": 2,
              "gpu_energy_j": 93.9571001828161,
              "semantic_passes": 2,
              "tokens_per_s": 78.22957981435789,
              "ttft_s": 0.078201903
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.62342518,
              "format_passes": 0,
              "gpu_energy_j": 156.65786217740464,
              "semantic_passes": 0,
              "tokens_per_s": 78.3481436183971,
              "ttft_s": 0.31921570099999996
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5621654515,
              "format_passes": 0,
              "gpu_energy_j": 142.03705838884366,
              "semantic_passes": 0,
              "tokens_per_s": 78.2623233863987,
              "ttft_s": 0.255647135
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
            "e2e_change_pct": 0.3042397993448631,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.14874682218389834,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.34937958869850627,
            "ttft_change_pct": 0.09409272959277626
          },
          "decode": {
            "e2e_change_pct": 0.6370128910557993,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.19058459397085503,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.6151887104244524,
            "ttft_change_pct": 0.47256858213815534
          },
          "energy": {
            "e2e_change_pct": 0.5211844891986006,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.932372071177471,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.21607680692427023,
            "ttft_change_pct": 1.1941773055581306
          },
          "filtering": {
            "e2e_change_pct": -0.287260823365576,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.1887187824354486,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.17495104671079176,
            "ttft_change_pct": -0.3659166458639729
          },
          "german": {
            "e2e_change_pct": 0.5522471680262209,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.8936261926785667,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.2928999068473104,
            "ttft_change_pct": 1.0188303236932317
          },
          "ha_sim": {
            "e2e_change_pct": -0.3883408475172434,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.9271986336950033,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.5321363890055109,
            "ttft_change_pct": 0.1574490740939405
          },
          "jarvis_memory": {
            "e2e_change_pct": 0.26951139402737745,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -4.378690932922913,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.35264373230701196,
            "ttft_change_pct": 0.026932055316009063
          },
          "long_context": {
            "e2e_change_pct": 0.18708911526046368,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.532705495354846,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.550338856658239,
            "ttft_change_pct": 0.07265580436046637
          },
          "math": {
            "e2e_change_pct": -0.1326655495645146,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.5222791366574331,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.003431152934152415,
            "ttft_change_pct": -0.4266614667228219
          },
          "prefill": {
            "e2e_change_pct": -0.002976920314579079,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.7481948428040175,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.03152467154976524,
            "ttft_change_pct": 0.006286708541591857
          },
          "prefill2048": {
            "e2e_change_pct": 0.050978860048833674,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.8001734948397843,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.04453647486305501,
            "ttft_change_pct": 0.05751874821959824
          },
          "prefill4096": {
            "e2e_change_pct": -0.01726834660878973,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.8042243498105339,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.005891523944212551,
            "ttft_change_pct": -0.011796296201371792
          },
          "pve_sim": {
            "e2e_change_pct": 0.14782284428864756,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.922607113482234,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.25252389879830694,
            "ttft_change_pct": -0.09587453008945701
          },
          "sorting": {
            "e2e_change_pct": 0.23442387545775656,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.9088207282835326,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.132581219090111,
            "ttft_change_pct": 0.6560734303769689
          },
          "time": {
            "e2e_change_pct": 0.49111260424405945,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.5810225663179125,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.4929825418637179,
            "ttft_change_pct": 0.4860515390953335
          },
          "tool-call": {
            "e2e_change_pct": 0.5787505414823313,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.229274055056384,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.5715147046946534,
            "ttft_change_pct": 0.4668555153417575
          },
          "tool-final": {
            "e2e_change_pct": 0.18507380466632473,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.6055451225019159,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.41467268226800247,
            "ttft_change_pct": 0.09355534088655304
          }
        }
      },
      "complete": true
    }
  }
}
```
