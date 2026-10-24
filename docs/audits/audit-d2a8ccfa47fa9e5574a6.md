# Public audit excerpt

Original SHA256: `d2a8ccfa47fa9e5574a6cb59b851e2d2ebeb2bd37df17c7c7445ccb5ae456b5c`

Original file: `RESULTS.json`; 43136 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.6664138310000001,
              "format_passes": 2,
              "gpu_energy_j": 178.31360448636786,
              "semantic_passes": 2,
              "tokens_per_s": 79.28437707519689,
              "ttft_s": 0.124038503
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.658495435,
              "format_passes": 0,
              "gpu_energy_j": 458.6114265297641,
              "semantic_passes": 0,
              "tokens_per_s": 79.61286839372451,
              "ttft_s": 0.0630749055
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.238473743,
              "format_passes": 2,
              "gpu_energy_j": 57.61780485556707,
              "semantic_passes": 2,
              "tokens_per_s": 78.1908050032717,
              "ttft_s": 0.0721754825
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.241575107,
              "format_passes": 0,
              "gpu_energy_j": 59.24747888637666,
              "semantic_passes": 0,
              "tokens_per_s": 77.57083007561803,
              "ttft_s": 0.12551928699999998
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.182852687,
              "format_passes": 2,
              "gpu_energy_j": 40.829879832360845,
              "semantic_passes": 2,
              "tokens_per_s": 77.4900206934597,
              "ttft_s": 0.0666991025
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.357530021,
              "format_passes": 0,
              "gpu_energy_j": 88.92441248379959,
              "semantic_passes": 0,
              "tokens_per_s": 78.8939866770925,
              "ttft_s": 0.07862992199999999
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.474517798,
              "format_passes": 0,
              "gpu_energy_j": 116.50364470108447,
              "semantic_passes": 2,
              "tokens_per_s": 78.44659656872028,
              "ttft_s": 0.11755466149999999
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.081155943,
              "format_passes": 2,
              "gpu_energy_j": 287.73908232438555,
              "semantic_passes": 2,
              "tokens_per_s": 77.7341907834913,
              "ttft_s": 0.8238173925000001
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2335685755,
              "format_passes": 0,
              "gpu_energy_j": 56.76864956684416,
              "semantic_passes": 0,
              "tokens_per_s": 78.28975374475213,
              "ttft_s": 0.0674753865
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.199185115,
              "format_passes": 0,
              "gpu_energy_j": 47.50731303123024,
              "semantic_passes": 0,
              "tokens_per_s": 2549.75867815369,
              "ttft_s": 0.198951151
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7187933635,
              "format_passes": 0,
              "gpu_energy_j": 190.70294163833816,
              "semantic_passes": 0,
              "tokens_per_s": 2854.0936733581043,
              "ttft_s": 0.718576607
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4196865535,
              "format_passes": 0,
              "gpu_energy_j": 379.910169911745,
              "semantic_passes": 0,
              "tokens_per_s": 2888.5909050749055,
              "ttft_s": 1.4193692565
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.29640936399999995,
              "format_passes": 2,
              "gpu_energy_j": 73.10279871624694,
              "semantic_passes": 2,
              "tokens_per_s": 78.22377986495121,
              "ttft_s": 0.07894527300000001
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.353864984,
              "format_passes": 2,
              "gpu_energy_j": 86.2217152561712,
              "semantic_passes": 2,
              "tokens_per_s": 78.81025180132292,
              "ttft_s": 0.0746785745
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.37366054849999997,
              "format_passes": 2,
              "gpu_energy_j": 93.81406331707791,
              "semantic_passes": 2,
              "tokens_per_s": 77.65417007549544,
              "ttft_s": 0.077375695
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6204636875,
              "format_passes": 0,
              "gpu_energy_j": 163.61861982723042,
              "semantic_passes": 0,
              "tokens_per_s": 78.87372584783742,
              "ttft_s": 0.3186982425
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5608615290000001,
              "format_passes": 0,
              "gpu_energy_j": 148.18468224725686,
              "semantic_passes": 0,
              "tokens_per_s": 78.70505263020837,
              "ttft_s": 0.255861561
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
              "e2e_s": 0.6528363815,
              "format_passes": 2,
              "gpu_energy_j": 174.18310546607444,
              "semantic_passes": 2,
              "tokens_per_s": 79.28180964468652,
              "ttft_s": 0.1104507255
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.657810314,
              "format_passes": 0,
              "gpu_energy_j": 463.67332980928495,
              "semantic_passes": 0,
              "tokens_per_s": 79.62335192682536,
              "ttft_s": 0.06273903950000001
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23968463550000002,
              "format_passes": 2,
              "gpu_energy_j": 57.83589413418528,
              "semantic_passes": 2,
              "tokens_per_s": 77.59711053920284,
              "ttft_s": 0.072037026
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2272424155,
              "format_passes": 0,
              "gpu_energy_j": 53.722352136584306,
              "semantic_passes": 0,
              "tokens_per_s": 77.0424741045839,
              "ttft_s": 0.1104352895
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.18205789849999998,
              "format_passes": 2,
              "gpu_energy_j": 41.34339845126401,
              "semantic_passes": 2,
              "tokens_per_s": 77.70277077436752,
              "ttft_s": 0.066172981
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.358066567,
              "format_passes": 0,
              "gpu_energy_j": 90.92165057189456,
              "semantic_passes": 0,
              "tokens_per_s": 78.80797970843466,
              "ttft_s": 0.07882828049999999
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4683391415,
              "format_passes": 0,
              "gpu_energy_j": 118.07303442476602,
              "semantic_passes": 2,
              "tokens_per_s": 79.03668333833781,
              "ttft_s": 0.11408303450000001
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.073880542,
              "format_passes": 2,
              "gpu_energy_j": 290.1716594023193,
              "semantic_passes": 2,
              "tokens_per_s": 78.04301921605673,
              "ttft_s": 0.817541875
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23359407100000001,
              "format_passes": 0,
              "gpu_energy_j": 55.527612461813185,
              "semantic_passes": 0,
              "tokens_per_s": 78.28366345742512,
              "ttft_s": 0.0674777025
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.1989459775,
              "format_passes": 0,
              "gpu_energy_j": 48.84078075598036,
              "semantic_passes": 0,
              "tokens_per_s": 2553.0150367755373,
              "ttft_s": 0.19874237700000003
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.720225755,
              "format_passes": 0,
              "gpu_energy_j": 192.61989314456514,
              "semantic_passes": 0,
              "tokens_per_s": 2848.4798649620943,
              "ttft_s": 0.72000504
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4202295275,
              "format_passes": 0,
              "gpu_energy_j": 388.9395093129981,
              "semantic_passes": 0,
              "tokens_per_s": 2887.582158375698,
              "ttft_s": 1.4198428129999998
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.295168242,
              "format_passes": 2,
              "gpu_energy_j": 73.14670629561317,
              "semantic_passes": 2,
              "tokens_per_s": 78.64022625651316,
              "ttft_s": 0.07897671249999999
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35360089250000004,
              "format_passes": 2,
              "gpu_energy_j": 86.96862067368373,
              "semantic_passes": 2,
              "tokens_per_s": 78.86930742720281,
              "ttft_s": 0.07462753550000001
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.36901111,
              "format_passes": 2,
              "gpu_energy_j": 93.01632896943988,
              "semantic_passes": 2,
              "tokens_per_s": 78.92727642205399,
              "ttft_s": 0.077527634
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.621419586,
              "format_passes": 0,
              "gpu_energy_j": 164.9440711352999,
              "semantic_passes": 0,
              "tokens_per_s": 79.03273661814214,
              "ttft_s": 0.3198352475
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.558766137,
              "format_passes": 0,
              "gpu_energy_j": 145.64913813700537,
              "semantic_passes": 0,
              "tokens_per_s": 78.85489792914746,
              "ttft_s": 0.2541832125
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
            "e2e_change_pct": -2.0373901123309723,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.316423938706935,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.003238255259208067,
            "ttft_change_pct": -10.954483625136946
          },
          "decode": {
            "e2e_change_pct": -0.041309791124033435,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.1037455646980776,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.01316813891065749,
            "ttft_change_pct": -0.5324875199376855
          },
          "energy": {
            "e2e_change_pct": 0.5077676413205889,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.3785102177441546,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.7592893615099849,
            "ttft_change_pct": -0.19183314777285743
          },
          "filtering": {
            "e2e_change_pct": -5.933016724276985,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -9.325505242827814,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.6811271331234603,
            "ttft_change_pct": -12.017274683849966
          },
          "german": {
            "e2e_change_pct": -0.43466055273228,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.2577029886239321,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.27455158613189923,
            "ttft_change_pct": -0.7887984699644024
          },
          "ha_sim": {
            "e2e_change_pct": 0.15007019508441743,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.2459952585673015,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.1090158734275426,
            "ttft_change_pct": 0.25226846848454
          },
          "jarvis_memory": {
            "e2e_change_pct": -1.3020916235474855,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.3470734994670552,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.752214621702052,
            "ttft_change_pct": -2.953202327922977
          },
          "long_context": {
            "e2e_change_pct": -0.6729279940701383,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.8454107305420955,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.3972877693235288,
            "ttft_change_pct": -0.761760744205231
          },
          "math": {
            "e2e_change_pct": 0.010915637921526944,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.186131103171085,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.0077791627073775516,
            "ttft_change_pct": 0.003432362703104097
          },
          "prefill": {
            "e2e_change_pct": -0.12005791697837775,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.8068683317735266,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.12771242430695828,
            "ttft_change_pct": -0.10493731699997566
          },
          "prefill2048": {
            "e2e_change_pct": 0.19927722941475157,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.0052029034048227,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.19669320766914078,
            "ttft_change_pct": 0.19878646007744916
          },
          "prefill4096": {
            "e2e_change_pct": 0.03824604795061859,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.3767037885167985,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.034921757090466965,
            "ttft_change_pct": 0.03336386904473354
          },
          "pve_sim": {
            "e2e_change_pct": -0.41871889040587806,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.06006278848045277,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.5323782515763265,
            "ttft_change_pct": 0.03982442368648531
          },
          "sorting": {
            "e2e_change_pct": -0.07463058283267987,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.8662613766073024,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.07493393883422073,
            "ttft_change_pct": -0.06834490393223813
          },
          "time": {
            "e2e_change_pct": -1.2442947265009385,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.8503355674317148,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 1.6394565099605574,
            "ttft_change_pct": 0.1963652798207649
          },
          "tool-call": {
            "e2e_change_pct": 0.15406195709075643,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.8100858627636986,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.20160169764451563,
            "ttft_change_pct": 0.35676538128381896
          },
          "tool-final": {
            "e2e_change_pct": -0.3736023762828111,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.7110703156354323,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.19038841082175129,
            "ttft_change_pct": -0.6559596109085075
          }
        }
      },
      "complete": true,
      "numerical_results": [
        {
          "begin_ns": 341611701867387,
          "end_ns": 341612458742939,
          "model": "omnicoder2",
          "passed": true,
          "reference": "existing CPU reference backend",
          "returncode": 0
        },
        {
          "begin_ns": 341657025852215,
          "end_ns": 341657632074481,
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

</details>
