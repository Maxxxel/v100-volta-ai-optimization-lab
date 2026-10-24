# Public audit excerpt

Original SHA256: `b8f24ee279ecd44dd1d14bd0d243697e10363cae95aa0c8ccbc05d4bd6e67fd8`

Original file: `RESULTS.json`; 118742 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.6662498889999999,
              "format_passes": 2,
              "gpu_energy_j": 175.0781246610166,
              "semantic_passes": 2,
              "tokens_per_s": 79.23398900689563,
              "ttft_s": 0.12350655899999999
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.658396129,
              "format_passes": 0,
              "gpu_energy_j": 447.1250047030744,
              "semantic_passes": 0,
              "tokens_per_s": 79.59782425018177,
              "ttft_s": 0.062741312
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.237457876,
              "format_passes": 2,
              "gpu_energy_j": 58.33830649744908,
              "semantic_passes": 2,
              "tokens_per_s": 78.43753972878584,
              "ttft_s": 0.07166753149999999
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.24265767249999998,
              "format_passes": 0,
              "gpu_energy_j": 58.24938659941927,
              "semantic_passes": 0,
              "tokens_per_s": 77.07163855887799,
              "ttft_s": 0.1258845415
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.182527303,
              "format_passes": 2,
              "gpu_energy_j": 41.4201342128206,
              "semantic_passes": 2,
              "tokens_per_s": 77.35015565117251,
              "ttft_s": 0.06608807850000001
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.357869122,
              "format_passes": 0,
              "gpu_energy_j": 90.21280018791867,
              "semantic_passes": 0,
              "tokens_per_s": 78.80206855797995,
              "ttft_s": 0.07865528899999999
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4735779805,
              "format_passes": 0,
              "gpu_energy_j": 113.07443253868183,
              "semantic_passes": 2,
              "tokens_per_s": 78.21049007037698,
              "ttft_s": 0.1155319195
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0811714535,
              "format_passes": 2,
              "gpu_energy_j": 282.22476555989124,
              "semantic_passes": 2,
              "tokens_per_s": 77.95140895444851,
              "ttft_s": 0.824594271
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23334014349999999,
              "format_passes": 0,
              "gpu_energy_j": 57.05200182720634,
              "semantic_passes": 0,
              "tokens_per_s": 78.24726508776325,
              "ttft_s": 0.0671538435
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.196920625,
              "format_passes": 0,
              "gpu_energy_j": 49.612993303859085,
              "semantic_passes": 0,
              "tokens_per_s": 2577.667692023748,
              "ttft_s": 0.1967943485
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7140658639999999,
              "format_passes": 0,
              "gpu_energy_j": 189.989635904686,
              "semantic_passes": 0,
              "tokens_per_s": 2873.202335599791,
              "ttft_s": 0.7138261564999999
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.410040463,
              "format_passes": 0,
              "gpu_energy_j": 380.7341401226798,
              "semantic_passes": 0,
              "tokens_per_s": 2908.3739511954946,
              "ttft_s": 1.4097469235
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2951085685,
              "format_passes": 2,
              "gpu_energy_j": 68.69805093287023,
              "semantic_passes": 2,
              "tokens_per_s": 78.57447725194577,
              "ttft_s": 0.0787501545
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.353491985,
              "format_passes": 2,
              "gpu_energy_j": 88.06766891242958,
              "semantic_passes": 2,
              "tokens_per_s": 78.72649355099935,
              "ttft_s": 0.073996576
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.36870254199999997,
              "format_passes": 2,
              "gpu_energy_j": 92.83558587436198,
              "semantic_passes": 2,
              "tokens_per_s": 78.9201186261786,
              "ttft_s": 0.07722829049999999
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6188924499999999,
              "format_passes": 0,
              "gpu_energy_j": 158.44672716341984,
              "semantic_passes": 0,
              "tokens_per_s": 78.9520100685197,
              "ttft_s": 0.31775823999999997
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.559627906,
              "format_passes": 0,
              "gpu_energy_j": 143.73967048014129,
              "semantic_passes": 0,
              "tokens_per_s": 78.76457920561162,
              "ttft_s": 0.2546951125
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
              "e2e_s": 0.666570091,
              "format_passes": 2,
              "gpu_energy_j": 177.26604604159246,
              "semantic_passes": 2,
              "tokens_per_s": 79.23258317147335,
              "ttft_s": 0.1238488895
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.658588403,
              "format_passes": 0,
              "gpu_energy_j": 449.690608279016,
              "semantic_passes": 0,
              "tokens_per_s": 79.59620609444306,
              "ttft_s": 0.062750425
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23761436549999998,
              "format_passes": 2,
              "gpu_energy_j": 57.400674289191294,
              "semantic_passes": 2,
              "tokens_per_s": 78.39495669642156,
              "ttft_s": 0.0717365975
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.242076507,
              "format_passes": 0,
              "gpu_energy_j": 59.25660154373081,
              "semantic_passes": 0,
              "tokens_per_s": 77.11030397840491,
              "ttft_s": 0.1253025755
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.182347124,
              "format_passes": 2,
              "gpu_energy_j": 42.72960421802274,
              "semantic_passes": 2,
              "tokens_per_s": 77.55378202802032,
              "ttft_s": 0.066246708
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35741427400000003,
              "format_passes": 0,
              "gpu_energy_j": 87.97958153603253,
              "semantic_passes": 0,
              "tokens_per_s": 78.8835955876953,
              "ttft_s": 0.0785040415
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4689910655,
              "format_passes": 0,
              "gpu_energy_j": 118.874468169703,
              "semantic_passes": 2,
              "tokens_per_s": 79.08169629289503,
              "ttft_s": 0.114893334
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0814516835,
              "format_passes": 2,
              "gpu_energy_j": 286.6767922926865,
              "semantic_passes": 2,
              "tokens_per_s": 77.08612951904516,
              "ttft_s": 0.8218844055000001
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.233509403,
              "format_passes": 0,
              "gpu_energy_j": 56.703940757345016,
              "semantic_passes": 0,
              "tokens_per_s": 78.21127149972116,
              "ttft_s": 0.067245281
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.19790877499999998,
              "format_passes": 0,
              "gpu_energy_j": 47.36663872179952,
              "semantic_passes": 0,
              "tokens_per_s": 2565.307420222243,
              "ttft_s": 0.19776646650000002
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7146697879999999,
              "format_passes": 0,
              "gpu_energy_j": 187.40898997184797,
              "semantic_passes": 0,
              "tokens_per_s": 2870.743677024461,
              "ttft_s": 0.7144258674999999
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4101396364999998,
              "format_passes": 0,
              "gpu_energy_j": 382.0315789304981,
              "semantic_passes": 0,
              "tokens_per_s": 2908.2873738929293,
              "ttft_s": 1.409800201
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2952083675,
              "format_passes": 2,
              "gpu_energy_j": 75.09326138681739,
              "semantic_passes": 2,
              "tokens_per_s": 78.57459034672186,
              "ttft_s": 0.07883718449999999
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35356034199999997,
              "format_passes": 2,
              "gpu_energy_j": 85.64687026757434,
              "semantic_passes": 2,
              "tokens_per_s": 78.73054740618923,
              "ttft_s": 0.074142176
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3696599685,
              "format_passes": 2,
              "gpu_energy_j": 92.00730258814565,
              "semantic_passes": 2,
              "tokens_per_s": 78.75336844161262,
              "ttft_s": 0.0775989255
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6186963505,
              "format_passes": 0,
              "gpu_energy_j": 160.59328400521747,
              "semantic_passes": 0,
              "tokens_per_s": 78.97958862374925,
              "ttft_s": 0.3176285795
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.560321106,
              "format_passes": 0,
              "gpu_energy_j": 144.57845763062943,
              "semantic_passes": 0,
              "tokens_per_s": 78.69319773275143,
              "ttft_s": 0.2553991695
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
            "e2e_change_pct": 0.04806034571813722,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.2496828971706675,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.0017742832841061151,
            "ttft_change_pct": 0.2771759676342578
          },
          "decode": {
            "e2e_change_pct": 0.011593973034407234,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.573800066861696,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.002032914534977337,
            "ttft_change_pct": 0.014524720171626981
          },
          "energy": {
            "e2e_change_pct": 0.06590200444644978,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.6072324764840218,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.05428909742900556,
            "ttft_change_pct": 0.09636999985134231
          },
          "filtering": {
            "e2e_change_pct": -0.23950015427597338,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.7291425766217117,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.05016815556266874,
            "ttft_change_pct": -0.46230140179681634
          },
          "german": {
            "e2e_change_pct": -0.0987134511049037,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.161433515579559,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.26325270470832773,
            "ttft_change_pct": 0.24002740524524668
          },
          "ha_sim": {
            "e2e_change_pct": -0.1270989789389998,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.475500868207414,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.10345798176016885,
            "ttft_change_pct": -0.1922915825787519
          },
          "jarvis_memory": {
            "e2e_change_pct": -0.9685659361014065,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 5.129396186920521,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 1.1139250268526801,
            "ttft_change_pct": -0.5527351252914925
          },
          "long_context": {
            "e2e_change_pct": 0.025919108305427763,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.5774755712749444,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -1.110024112468555,
            "ttft_change_pct": -0.3286301633788513
          },
          "math": {
            "e2e_change_pct": 0.0725376685988044,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.6100768749806473,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.04599980331800868,
            "ttft_change_pct": 0.13616123103958877
          },
          "prefill": {
            "e2e_change_pct": 0.5018011698876057,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -4.527754591023314,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.4795137806068661,
            "ttft_change_pct": 0.4939765838855026
          },
          "prefill2048": {
            "e2e_change_pct": 0.08457539149357984,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.358308794345331,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.08557206517850746,
            "ttft_change_pct": 0.08401359274090581
          },
          "prefill4096": {
            "e2e_change_pct": 0.007033379722232169,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.3407729097790524,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.0029768284277809087,
            "ttft_change_pct": 0.003779224420474847
          },
          "pve_sim": {
            "e2e_change_pct": 0.03381772359483115,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 9.3091585090185,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.00014393322114170104,
            "ttft_change_pct": 0.11051406889619475
          },
          "sorting": {
            "e2e_change_pct": 0.019337637881644554,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.7487938249647237,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.0051492896571803115,
            "ttft_change_pct": 0.1967658611663481
          },
          "time": {
            "e2e_change_pct": 0.2596745047665161,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.8922045123270772,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.21128983010761937,
            "ttft_change_pct": 0.479921279624862
          },
          "tool-call": {
            "e2e_change_pct": -0.03168555376622528,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.3547498772781275,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.03493078289662499,
            "ttft_change_pct": -0.040804764024360285
          },
          "tool-final": {
            "e2e_change_pct": 0.12386801883319531,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.5835460368639245,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.0906263622304837,
            "ttft_change_pct": 0.2764312958694948
          }
        }
      },
      "complete": true
    },
    "qwen35": {
      "arms": {
        "A": {
          "format_passes": 10,
          "quality_attempts": 24,
          "quality_passes": 14,
          "tasks": {
            "code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5533611625,
              "format_passes": 2,
              "gpu_energy_j": 134.9287257864887,
              "semantic_passes": 2,
              "tokens_per_s": 95.55312896957994,
              "ttft_s": 0.152112413
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.3668898029999998,
              "format_passes": 0,
              "gpu_energy_j": 353.5379585743281,
              "semantic_passes": 0,
              "tokens_per_s": 97.03890002016149,
              "ttft_s": 0.057832219000000004
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2214656525,
              "format_passes": 2,
              "gpu_energy_j": 45.44056757957855,
              "semantic_passes": 2,
              "tokens_per_s": 94.29852685686629,
              "ttft_s": 0.08110740599999999
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2541855685,
              "format_passes": 0,
              "gpu_energy_j": 56.94219543299014,
              "semantic_passes": 0,
              "tokens_per_s": 90.70447116417265,
              "ttft_s": 0.1517457855
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.17828499650000001,
              "format_passes": 2,
              "gpu_energy_j": 33.77176370785004,
              "semantic_passes": 2,
              "tokens_per_s": 91.2592352303576,
              "ttft_s": 0.0768711025
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.32723918799999996,
              "format_passes": 0,
              "gpu_energy_j": 73.23801246533841,
              "semantic_passes": 0,
              "tokens_per_s": 94.7567184293016,
              "ttft_s": 0.09307059000000001
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4177493535,
              "format_passes": 0,
              "gpu_energy_j": 94.29710671669426,
              "semantic_passes": 2,
              "tokens_per_s": 95.80797514037491,
              "ttft_s": 0.1232260235
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0426909850000001,
              "format_passes": 2,
              "gpu_energy_j": 270.50944290665365,
              "semantic_passes": 2,
              "tokens_per_s": 93.11583420500006,
              "ttft_s": 0.8802408225
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.162572909,
              "format_passes": 0,
              "gpu_energy_j": 30.612554708151734,
              "semantic_passes": 0,
              "tokens_per_s": 92.65295741037076,
              "ttft_s": 0.0745902515
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.2055648145,
              "format_passes": 0,
              "gpu_energy_j": 51.59081321501726,
              "semantic_passes": 0,
              "tokens_per_s": 2469.0206034978232,
              "ttft_s": 0.2054195325
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7560883885,
              "format_passes": 0,
              "gpu_energy_j": 198.9626549507311,
              "semantic_passes": 0,
              "tokens_per_s": 2713.3741325298934,
              "ttft_s": 0.7558258234999999
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.500843926,
              "format_passes": 0,
              "gpu_energy_j": 402.0843590721102,
              "semantic_passes": 0,
              "tokens_per_s": 2732.2808733831534,
              "ttft_s": 1.50049066
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.278271653,
              "format_passes": 2,
              "gpu_energy_j": 56.94817421049903,
              "semantic_passes": 2,
              "tokens_per_s": 91.44676261298358,
              "ttft_s": 0.08822895550000001
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.36057500249999996,
              "format_passes": 0,
              "gpu_energy_j": 85.6445416971741,
              "semantic_passes": 2,
              "tokens_per_s": 95.23159190282507,
              "ttft_s": 0.0753598415
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.327178786,
              "format_passes": 0,
              "gpu_energy_j": 75.00953188427727,
              "semantic_passes": 0,
              "tokens_per_s": 95.58621887007729,
              "ttft_s": 0.08320385450000001
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.550423487,
              "format_passes": 0,
              "gpu_energy_j": 139.65029266639877,
              "semantic_passes": 0,
              "tokens_per_s": 96.147271556557,
              "ttft_s": 0.3034537425
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5239012665,
              "format_passes": 0,
              "gpu_energy_j": 135.1813384065091,
              "semantic_passes": 0,
              "tokens_per_s": 95.82999767022729,
              "ttft_s": 0.27406526350000004
            }
          }
        },
        "B": {
          "format_passes": 10,
          "quality_attempts": 24,
          "quality_passes": 14,
          "tasks": {
            "code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5257544814999999,
              "format_passes": 2,
              "gpu_energy_j": 134.09855825281537,
              "semantic_passes": 2,
              "tokens_per_s": 96.49998806696928,
              "ttft_s": 0.13196846
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.3669870335,
              "format_passes": 0,
              "gpu_energy_j": 350.1836521142128,
              "semantic_passes": 0,
              "tokens_per_s": 96.99243348882186,
              "ttft_s": 0.057535515499999995
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2047104155,
              "format_passes": 2,
              "gpu_energy_j": 44.00752907187274,
              "semantic_passes": 2,
              "tokens_per_s": 95.00950809533538,
              "ttft_s": 0.0678266285
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23060135250000002,
              "format_passes": 0,
              "gpu_energy_j": 54.916884457538316,
              "semantic_passes": 0,
              "tokens_per_s": 93.40732445514013,
              "ttft_s": 0.134217398
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.157182694,
              "format_passes": 2,
              "gpu_energy_j": 31.771599541998516,
              "semantic_passes": 2,
              "tokens_per_s": 93.69834761488775,
              "ttft_s": 0.0610882755
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.306653791,
              "format_passes": 0,
              "gpu_energy_j": 69.99238333066388,
              "semantic_passes": 0,
              "tokens_per_s": 95.99260287509927,
              "ttft_s": 0.07740451749999999
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.39877184200000004,
              "format_passes": 0,
              "gpu_energy_j": 93.75942932937372,
              "semantic_passes": 2,
              "tokens_per_s": 96.003482317737,
              "ttft_s": 0.1071281585
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0302121685,
              "format_passes": 2,
              "gpu_energy_j": 271.9153452050978,
              "semantic_passes": 2,
              "tokens_per_s": 94.45815080946628,
              "ttft_s": 0.871342041
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1487414575,
              "format_passes": 0,
              "gpu_energy_j": 32.211228005015016,
              "semantic_passes": 0,
              "tokens_per_s": 93.43394839991228,
              "ttft_s": 0.06306144999999999
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.2051650765,
              "format_passes": 0,
              "gpu_energy_j": 51.57374760535255,
              "semantic_passes": 0,
              "tokens_per_s": 2474.5957024613163,
              "ttft_s": 0.2050158515
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.753230145,
              "format_passes": 0,
              "gpu_energy_j": 197.87859194313887,
              "semantic_passes": 0,
              "tokens_per_s": 2723.5115123509604,
              "ttft_s": 0.7529851855
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4927730225,
              "format_passes": 0,
              "gpu_energy_j": 405.1754312943408,
              "semantic_passes": 0,
              "tokens_per_s": 2747.0126965195586,
              "ttft_s": 1.492476118
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2541002795,
              "format_passes": 2,
              "gpu_energy_j": 59.13812672466163,
              "semantic_passes": 2,
              "tokens_per_s": 95.668068439216,
              "ttft_s": 0.076389409
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3506774655,
              "format_passes": 0,
              "gpu_energy_j": 82.89536848990844,
              "semantic_passes": 2,
              "tokens_per_s": 96.20404239942678,
              "ttft_s": 0.069995275
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3141112295,
              "format_passes": 0,
              "gpu_energy_j": 73.85038761971181,
              "semantic_passes": 0,
              "tokens_per_s": 96.11712220123609,
              "ttft_s": 0.07477777499999999
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.549644767,
              "format_passes": 0,
              "gpu_energy_j": 138.91235618788016,
              "semantic_passes": 0,
              "tokens_per_s": 96.19520656651932,
              "ttft_s": 0.3026376745
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5238976405,
              "format_passes": 0,
              "gpu_energy_j": 129.7134409732859,
              "semantic_passes": 0,
              "tokens_per_s": 95.90428934381524,
              "ttft_s": 0.27349509000000005
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
            "e2e_change_pct": -4.988908306336026,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.6152637467183975,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.990924219436895,
            "ttft_change_pct": -13.242806818139153
          },
          "decode": {
            "e2e_change_pct": 0.007113265442959538,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.9487825504344238,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.04788443740600945,
            "ttft_change_pct": -0.5130418737693709
          },
          "energy": {
            "e2e_change_pct": -7.56561426607677,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.153654507497461,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.7539685530276286,
            "ttft_change_pct": -16.37430927084512
          },
          "filtering": {
            "e2e_change_pct": -9.278345792475617,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.5567841388118193,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 2.979845708019613,
            "ttft_change_pct": -11.551152766611771
          },
          "german": {
            "e2e_change_pct": -11.836275017118448,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -5.922593155496347,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 2.6727293718529666,
            "ttft_change_pct": -20.531547599437637
          },
          "ha_sim": {
            "e2e_change_pct": -6.290627087120127,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -4.431618261364756,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 1.3042710493607501,
            "ttft_change_pct": -16.83246286501463
          },
          "jarvis_memory": {
            "e2e_change_pct": -4.542798532421887,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.5701949996577693,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.20406148556593173,
            "ttft_change_pct": -13.063689424336577
          },
          "long_context": {
            "e2e_change_pct": -1.1967895262852024,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.519723926580018,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 1.4415556880594815,
            "ttft_change_pct": -1.0109485123316886
          },
          "math": {
            "e2e_change_pct": -8.50784524007009,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 5.222279917845518,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.8429207349339274,
            "ttft_change_pct": -15.456177272709704
          },
          "prefill": {
            "e2e_change_pct": -0.19445837604664673,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.03307877624177946,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.22580204294750938,
            "ttft_change_pct": -0.19651539222541592
          },
          "prefill2048": {
            "e2e_change_pct": -0.3780303392399098,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.54485753010316,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.37360788914189147,
            "ttft_change_pct": -0.37583235603749765
          },
          "prefill4096": {
            "e2e_change_pct": -0.5377576815405627,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.7687621148367629,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.5391767471608411,
            "ttft_change_pct": -0.5341280831431594
          },
          "pve_sim": {
            "e2e_change_pct": -8.686250733559264,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.8455183937378123,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 4.616134793199422,
            "ttft_change_pct": -13.419116698032319
          },
          "sorting": {
            "e2e_change_pct": -2.744931548603391,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.2099806394975228,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 1.0211427501852555,
            "ttft_change_pct": -7.118601092068378
          },
          "time": {
            "e2e_change_pct": -3.9940109381052635,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.5453292874214375,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.5554182783193973,
            "ttft_change_pct": -10.127030232715983
          },
          "tool-call": {
            "e2e_change_pct": -0.14147652096829777,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.5284174235720474,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.049855819292932146,
            "ttft_change_pct": -0.268926655271029
          },
          "tool-final": {
            "e2e_change_pct": -0.0006921151430416828,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -4.044861145538048,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.07752444473974052,
            "ttft_change_pct": -0.20804296491955254
          }
        }
      },
      "complete": true
    },
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
              "e2e_s": 1.7607168560000002,
              "format_passes": 2,
              "gpu_energy_j": 480.4039177579756,
              "semantic_passes": 2,
              "tokens_per_s": 35.448518484826785,
              "ttft_s": 0.519468273
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.7736491035,
              "format_passes": 0,
              "gpu_energy_j": 1062.3098296816877,
              "semantic_passes": 0,
              "tokens_per_s": 35.49195253427651,
              "ttft_s": 0.1949298605
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5796072114999999,
              "format_passes": 2,
              "gpu_energy_j": 143.9553165129758,
              "semantic_passes": 2,
              "tokens_per_s": 35.01722645750341,
              "ttft_s": 0.2083069305
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9237402115,
              "format_passes": 0,
              "gpu_energy_j": 243.17169650010152,
              "semantic_passes": 0,
              "tokens_per_s": 35.01781714776861,
              "ttft_s": 0.523902491
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.46483615899999997,
              "format_passes": 2,
              "gpu_energy_j": 110.71120259034491,
              "semantic_passes": 2,
              "tokens_per_s": 34.33228357607926,
              "ttft_s": 0.2026509815
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9877565500000001,
              "format_passes": 0,
              "gpu_energy_j": 261.48856464915735,
              "semantic_passes": 0,
              "tokens_per_s": 35.313222272811345,
              "ttft_s": 0.2231644625
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.144004899,
              "format_passes": 0,
              "gpu_energy_j": 295.474734074347,
              "semantic_passes": 2,
              "tokens_per_s": 35.34966832557419,
              "ttft_s": 0.3518869695
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.7815304010000004,
              "format_passes": 2,
              "gpu_energy_j": 1013.7477184882066,
              "semantic_passes": 2,
              "tokens_per_s": 34.481248226555834,
              "ttft_s": 3.2014334435
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5722809245,
              "format_passes": 2,
              "gpu_energy_j": 143.98039357141985,
              "semantic_passes": 2,
              "tokens_per_s": 34.97452868497621,
              "ttft_s": 0.2005611685
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7215434734999999,
              "format_passes": 0,
              "gpu_energy_j": 188.86334086479235,
              "semantic_passes": 0,
              "tokens_per_s": 700.8904775988731,
              "ttft_s": 0.7213833155
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.7423407775,
              "format_passes": 0,
              "gpu_energy_j": 735.5446973345213,
              "semantic_passes": 0,
              "tokens_per_s": 747.1538429617224,
              "ttft_s": 2.742114569
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.452713694,
              "format_passes": 0,
              "gpu_energy_j": 1472.7513082239057,
              "semantic_passes": 0,
              "tokens_per_s": 751.4249139977288,
              "ttft_s": 5.4523928825
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.846749682,
              "format_passes": 0,
              "gpu_energy_j": 221.83636612326382,
              "semantic_passes": 2,
              "tokens_per_s": 35.22139614915096,
              "ttft_s": 0.222095559
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.984551722,
              "format_passes": 0,
              "gpu_energy_j": 259.23455754895747,
              "semantic_passes": 2,
              "tokens_per_s": 35.11391883683201,
              "ttft_s": 0.21559904600000002
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0160650455,
              "format_passes": 0,
              "gpu_energy_j": 274.4399558031609,
              "semantic_passes": 2,
              "tokens_per_s": 35.21667307037774,
              "ttft_s": 0.2209388115
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.705256227,
              "format_passes": 0,
              "gpu_energy_j": 462.1789311339182,
              "semantic_passes": 0,
              "tokens_per_s": 35.05380230204815,
              "ttft_s": 1.0276355615
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.775093675,
              "format_passes": 0,
              "gpu_energy_j": 465.72837632343936,
              "semantic_passes": 0,
              "tokens_per_s": 35.14760513741109,
              "ttft_s": 1.0923099715000002
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
              "e2e_s": 1.762844876,
              "format_passes": 2,
              "gpu_energy_j": 480.60574971131587,
              "semantic_passes": 2,
              "tokens_per_s": 35.41110726033521,
              "ttft_s": 0.5202518185
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.7802292955,
              "format_passes": 0,
              "gpu_energy_j": 1068.8765016599764,
              "semantic_passes": 0,
              "tokens_per_s": 35.440474942353845,
              "ttft_s": 0.1943430935
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.580109821,
              "format_passes": 2,
              "gpu_energy_j": 145.0518843218631,
              "semantic_passes": 2,
              "tokens_per_s": 35.014112882256086,
              "ttft_s": 0.208788674
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.924974271,
              "format_passes": 0,
              "gpu_energy_j": 243.80157186474284,
              "semantic_passes": 0,
              "tokens_per_s": 34.88389736102127,
              "ttft_s": 0.5235941829999999
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4644535045,
              "format_passes": 2,
              "gpu_energy_j": 110.0907961966582,
              "semantic_passes": 2,
              "tokens_per_s": 34.3067638026825,
              "ttft_s": 0.202050815
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9895885085,
              "format_passes": 0,
              "gpu_energy_j": 264.18410634157664,
              "semantic_passes": 0,
              "tokens_per_s": 35.208030215283344,
              "ttft_s": 0.22270211
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.146635822,
              "format_passes": 0,
              "gpu_energy_j": 297.216864100178,
              "semantic_passes": 2,
              "tokens_per_s": 35.35633144053237,
              "ttft_s": 0.354640495
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.79505011,
              "format_passes": 2,
              "gpu_energy_j": 1015.0732386475554,
              "semantic_passes": 2,
              "tokens_per_s": 34.41051412109344,
              "ttft_s": 3.2138141925
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5741927284999999,
              "format_passes": 2,
              "gpu_energy_j": 142.78437060106864,
              "semantic_passes": 2,
              "tokens_per_s": 34.94055951424666,
              "ttft_s": 0.2021160605
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.725124352,
              "format_passes": 0,
              "gpu_energy_j": 185.26550511650373,
              "semantic_passes": 0,
              "tokens_per_s": 697.4511982554607,
              "ttft_s": 0.7249792385
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.7460277735,
              "format_passes": 0,
              "gpu_energy_j": 736.3606289946196,
              "semantic_passes": 0,
              "tokens_per_s": 746.138728948826,
              "ttft_s": 2.745767573
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.455573499,
              "format_passes": 0,
              "gpu_energy_j": 1474.9180511727711,
              "semantic_passes": 0,
              "tokens_per_s": 751.0191748462496,
              "ttft_s": 5.4552896205
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8459420445,
              "format_passes": 0,
              "gpu_energy_j": 226.82782549096626,
              "semantic_passes": 2,
              "tokens_per_s": 35.24849174501595,
              "ttft_s": 0.2217312165
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9843747279999999,
              "format_passes": 0,
              "gpu_energy_j": 264.8128170265316,
              "semantic_passes": 2,
              "tokens_per_s": 35.08047715102393,
              "ttft_s": 0.21467271599999999
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0151342799999998,
              "format_passes": 0,
              "gpu_energy_j": 275.00294938971695,
              "semantic_passes": 2,
              "tokens_per_s": 35.26092818485722,
              "ttft_s": 0.221045274
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.706231246,
              "format_passes": 0,
              "gpu_energy_j": 467.8572389009813,
              "semantic_passes": 0,
              "tokens_per_s": 35.05544072205927,
              "ttft_s": 1.027931352
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.779927654,
              "format_passes": 0,
              "gpu_energy_j": 467.0714167557827,
              "semantic_passes": 0,
              "tokens_per_s": 35.05916067762781,
              "ttft_s": 1.0953398195
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
            "e2e_change_pct": 0.12086100003803057,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.042012969894633656,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.10553677865998701,
            "ttft_change_pct": 0.1508360646310436
          },
          "decode": {
            "e2e_change_pct": 0.17437212150692716,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.6181503545209965,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.14504018022943876,
            "ttft_change_pct": -0.3010144256477276
          },
          "energy": {
            "e2e_change_pct": 0.08671553597465742,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.7617417928350356,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.008891552993506302,
            "ttft_change_pct": 0.2312661891967327
          },
          "filtering": {
            "e2e_change_pct": 0.1335937836890455,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.25902494974001655,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.38243328012772526,
            "ttft_change_pct": -0.05884835542804279
          },
          "german": {
            "e2e_change_pct": -0.08232029556890508,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.5603826705616655,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.07433170980373216,
            "ttft_change_pct": -0.29615770698845356
          },
          "ha_sim": {
            "e2e_change_pct": 0.1854666010566941,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.030844961054389,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.29788291964789604,
            "ttft_change_pct": -0.20718016427010433
          },
          "jarvis_memory": {
            "e2e_change_pct": 0.22997480188238217,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.5896037207000715,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.01884915834799994,
            "ttft_change_pct": 0.7825028314951687
          },
          "long_context": {
            "e2e_change_pct": 0.3575195110536278,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.13075444069314823,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.20513789117388992,
            "ttft_change_pct": 0.3867251722861065
          },
          "math": {
            "e2e_change_pct": 0.33406739909602745,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.8306846096777343,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.0971254567445845,
            "ttft_change_pct": 0.7752707124859093
          },
          "prefill": {
            "e2e_change_pct": 0.4962803533694604,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.9049942311802681,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.4907013939174587,
            "ttft_change_pct": 0.49847604217290176
          },
          "prefill2048": {
            "e2e_change_pct": 0.1344470399248232,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.11092890249295717,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.1358641225577384,
            "ttft_change_pct": 0.13321850375247468
          },
          "prefill4096": {
            "e2e_change_pct": 0.05244737135468025,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.14712212012757409,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.053995967384234955,
            "ttft_change_pct": 0.05312782960482654
          },
          "pve_sim": {
            "e2e_change_pct": -0.0953809038454434,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.2500636189329404,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.07692936347623025,
            "ttft_change_pct": -0.1640476296061344
          },
          "sorting": {
            "e2e_change_pct": -0.017977115477540995,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.1518193910241568,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.09523769182095965,
            "ttft_change_pct": -0.4296540347400346
          },
          "time": {
            "e2e_change_pct": -0.09160491290615136,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.20514271870815115,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.12566523359842652,
            "ttft_change_pct": 0.04818641834687387
          },
          "tool-call": {
            "e2e_change_pct": 0.05717727251552951,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.2285951142627427,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.004674015095429418,
            "ttft_change_pct": 0.028783599077497612
          },
          "tool-final": {
            "e2e_change_pct": 0.2723224733477858,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.2883741898970449,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.25163722944281375,
            "ttft_change_pct": 0.2773798719276632
          }
        }
      },
      "complete": true
    }
  }
}
```

</details>
