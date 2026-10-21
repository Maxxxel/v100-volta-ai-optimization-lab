# Public audit excerpt

Original SHA256: `706dabd92ee818792bba0a0cf6f68810e5ec70574420221275bba59d6ce552e9`

Original file: `RESULTS.json`; 39698 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.665774112,
              "format_passes": 2,
              "gpu_energy_j": 175.97105986626207,
              "semantic_passes": 2,
              "tokens_per_s": 79.32628060535237,
              "ttft_s": 0.12363998749999999
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6593022425,
              "format_passes": 0,
              "gpu_energy_j": 457.58579949246547,
              "semantic_passes": 0,
              "tokens_per_s": 79.59368375836308,
              "ttft_s": 0.06317861599999999
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23790016349999998,
              "format_passes": 2,
              "gpu_energy_j": 55.12406698624826,
              "semantic_passes": 2,
              "tokens_per_s": 78.30511215513962,
              "ttft_s": 0.07181789250000001
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.241925013,
              "format_passes": 0,
              "gpu_energy_j": 62.61186857381155,
              "semantic_passes": 0,
              "tokens_per_s": 77.17026512237135,
              "ttft_s": 0.1252738835
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1822231365,
              "format_passes": 2,
              "gpu_energy_j": 42.46933202342712,
              "semantic_passes": 2,
              "tokens_per_s": 77.43536281993303,
              "ttft_s": 0.0659800165
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35803109899999996,
              "format_passes": 0,
              "gpu_energy_j": 88.65421288363487,
              "semantic_passes": 0,
              "tokens_per_s": 78.73903516367841,
              "ttft_s": 0.0786396095
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4694064525,
              "format_passes": 0,
              "gpu_energy_j": 114.60377299564787,
              "semantic_passes": 2,
              "tokens_per_s": 78.95910170979371,
              "ttft_s": 0.11476299400000001
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.080653128,
              "format_passes": 2,
              "gpu_energy_j": 287.72693457195123,
              "semantic_passes": 2,
              "tokens_per_s": 77.97354518920005,
              "ttft_s": 0.824117091
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23378600300000002,
              "format_passes": 0,
              "gpu_energy_j": 53.91241709129275,
              "semantic_passes": 0,
              "tokens_per_s": 78.37277397935043,
              "ttft_s": 0.06785482749999999
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.1988737765,
              "format_passes": 0,
              "gpu_energy_j": 49.41006917105501,
              "semantic_passes": 0,
              "tokens_per_s": 2552.8193981877466,
              "ttft_s": 0.198748837
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7192350545,
              "format_passes": 0,
              "gpu_energy_j": 189.06727671618557,
              "semantic_passes": 0,
              "tokens_per_s": 2852.4686274631313,
              "ttft_s": 0.718976343
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4165708635,
              "format_passes": 0,
              "gpu_energy_j": 381.4530386417921,
              "semantic_passes": 0,
              "tokens_per_s": 2894.992754376091,
              "ttft_s": 1.416282044
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.295378477,
              "format_passes": 2,
              "gpu_energy_j": 70.74461379954083,
              "semantic_passes": 2,
              "tokens_per_s": 78.58383354551276,
              "ttft_s": 0.07903639600000001
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3532819025,
              "format_passes": 2,
              "gpu_energy_j": 86.20491736145604,
              "semantic_passes": 2,
              "tokens_per_s": 78.67965283420256,
              "ttft_s": 0.073690715
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.36915718399999997,
              "format_passes": 2,
              "gpu_energy_j": 94.56120954695426,
              "semantic_passes": 2,
              "tokens_per_s": 78.84627925203328,
              "ttft_s": 0.07740265199999999
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6200001945,
              "format_passes": 0,
              "gpu_energy_j": 163.2995961473176,
              "semantic_passes": 0,
              "tokens_per_s": 78.96616668524834,
              "ttft_s": 0.31839886100000003
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5622449995,
              "format_passes": 0,
              "gpu_energy_j": 144.12132653583132,
              "semantic_passes": 0,
              "tokens_per_s": 78.63132058183535,
              "ttft_s": 0.25593340099999995
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
              "e2e_s": 0.6667560695,
              "format_passes": 2,
              "gpu_energy_j": 177.68342727000558,
              "semantic_passes": 2,
              "tokens_per_s": 79.21563681107392,
              "ttft_s": 0.1239275585
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6587990335,
              "format_passes": 0,
              "gpu_energy_j": 459.33499788254187,
              "semantic_passes": 0,
              "tokens_per_s": 79.57635830547176,
              "ttft_s": 0.0629147105
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2382081935,
              "format_passes": 2,
              "gpu_energy_j": 57.71427458426653,
              "semantic_passes": 2,
              "tokens_per_s": 78.01649487913987,
              "ttft_s": 0.071560445
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.242585405,
              "format_passes": 0,
              "gpu_energy_j": 57.81623234821342,
              "semantic_passes": 0,
              "tokens_per_s": 77.08914060271846,
              "ttft_s": 0.125932243
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.18242904,
              "format_passes": 2,
              "gpu_energy_j": 40.14366650506081,
              "semantic_passes": 2,
              "tokens_per_s": 77.57086335401915,
              "ttft_s": 0.066349402
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3577610325,
              "format_passes": 0,
              "gpu_energy_j": 88.27128529936977,
              "semantic_passes": 0,
              "tokens_per_s": 78.86308228200843,
              "ttft_s": 0.0787520065
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4696874775,
              "format_passes": 0,
              "gpu_energy_j": 118.46345240375257,
              "semantic_passes": 2,
              "tokens_per_s": 78.91660383326735,
              "ttft_s": 0.1148828995
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9909487885,
              "format_passes": 2,
              "gpu_energy_j": 257.37033237819395,
              "semantic_passes": 2,
              "tokens_per_s": 77.3191607996833,
              "ttft_s": 0.732252746
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.235220134,
              "format_passes": 0,
              "gpu_energy_j": 57.500038254193385,
              "semantic_passes": 0,
              "tokens_per_s": 77.74499636172285,
              "ttft_s": 0.067958522
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.1991525745,
              "format_passes": 0,
              "gpu_energy_j": 47.9814703037801,
              "semantic_passes": 0,
              "tokens_per_s": 2548.6521611694557,
              "ttft_s": 0.199026655
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6228999740000001,
              "format_passes": 0,
              "gpu_energy_j": 159.52574194040312,
              "semantic_passes": 0,
              "tokens_per_s": 3294.430879360447,
              "ttft_s": 0.6226767205
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.2210438495,
              "format_passes": 0,
              "gpu_energy_j": 323.2528829857033,
              "semantic_passes": 0,
              "tokens_per_s": 3359.1663214925456,
              "ttft_s": 1.2207133125
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.29564612850000005,
              "format_passes": 2,
              "gpu_energy_j": 75.09810485148324,
              "semantic_passes": 2,
              "tokens_per_s": 78.51577555348265,
              "ttft_s": 0.07914368599999999
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3538508075,
              "format_passes": 2,
              "gpu_energy_j": 89.73585408586604,
              "semantic_passes": 2,
              "tokens_per_s": 78.58611717401402,
              "ttft_s": 0.0739188425
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3700443365,
              "format_passes": 2,
              "gpu_energy_j": 89.56234839319725,
              "semantic_passes": 2,
              "tokens_per_s": 78.62298726269256,
              "ttft_s": 0.0774608255
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.620295033,
              "format_passes": 0,
              "gpu_energy_j": 165.21548688273333,
              "semantic_passes": 0,
              "tokens_per_s": 79.01589782222393,
              "ttft_s": 0.3189430335
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5609680635000001,
              "format_passes": 0,
              "gpu_energy_j": 147.08775019053496,
              "semantic_passes": 0,
              "tokens_per_s": 78.7489760645192,
              "ttft_s": 0.256067399
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
            "e2e_change_pct": 0.14749109079206235,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.9730960335437633,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.13947936728421206,
            "ttft_change_pct": 0.23258737388662798
          },
          "decode": {
            "e2e_change_pct": -0.030326542513536836,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.3822667556590664,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.021767371571745908,
            "ttft_change_pct": -0.41771332882631906
          },
          "energy": {
            "e2e_change_pct": 0.12947868360755344,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.698868823783364,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.36858037496700913,
            "ttft_change_pct": -0.35847264663190215
          },
          "filtering": {
            "e2e_change_pct": 0.2729738408653093,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -7.659308586110436,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.10512406498053295,
            "ttft_change_pct": 0.5255361146363935
          },
          "german": {
            "e2e_change_pct": 0.11299525623080786,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -5.476105715727808,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.17498534151794143,
            "ttft_change_pct": 0.5598445098903504
          },
          "ha_sim": {
            "e2e_change_pct": -0.07543101723683776,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.4319338831282882,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.1575420857928611,
            "ttft_change_pct": 0.14292670158795318
          },
          "jarvis_memory": {
            "e2e_change_pct": 0.05986815871474871,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.367846718494394,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.053822644389456276,
            "ttft_change_pct": 0.10448097929545153
          },
          "long_context": {
            "e2e_change_pct": -8.300937384599882,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -10.550490255254875,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.8392389853878135,
            "ttft_change_pct": -11.14700156121382
          },
          "math": {
            "e2e_change_pct": 0.613437494801583,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 6.654535924118421,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.8010149261693633,
            "ttft_change_pct": 0.15281816168495332
          },
          "prefill": {
            "e2e_change_pct": 0.1401884174508261,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.8913112068901903,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.16324057319719865,
            "ttft_change_pct": 0.1397834594624392
          },
          "prefill2048": {
            "e2e_change_pct": -13.394102511726224,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -15.624879825252957,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 15.494026740282818,
            "ttft_change_pct": -13.3939904195151
          },
          "prefill4096": {
            "e2e_change_pct": -13.802840298218522,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -15.257489064267837,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 16.03366939052979,
            "ttft_change_pct": -13.808600647626367
          },
          "pve_sim": {
            "e2e_change_pct": 0.09061306792508272,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 6.153812733048891,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.08660558916445682,
            "ttft_change_pct": 0.13574758646635043
          },
          "sorting": {
            "e2e_change_pct": 0.1610342890405958,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.095980638325791,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.11888163816080599,
            "ttft_change_pct": 0.3095742794733347
          },
          "time": {
            "e2e_change_pct": 0.2403183625975469,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -5.286376070808219,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.28319914580492433,
            "ttft_change_pct": 0.07515698557720718
          },
          "tool-call": {
            "e2e_change_pct": 0.04755458185585759,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.173236664766364,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.06297777777894975,
            "ttft_change_pct": 0.170909059878821
          },
          "tool-final": {
            "e2e_change_pct": -0.22711380290362237,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.058282230677455,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.14962928488704286,
            "ttft_change_pct": 0.052356589439472856
          }
        }
      },
      "complete": true
    }
  }
}
```
