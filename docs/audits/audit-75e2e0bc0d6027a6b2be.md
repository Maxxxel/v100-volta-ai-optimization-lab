# Public audit excerpt

Original SHA256: `75e2e0bc0d6027a6b2beb878cfcebb3bc93430ec5409bc63469779670e2bd1ba`

Original file: `RESULTS.json`; 39798 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 1.764095235,
              "format_passes": 2,
              "gpu_energy_j": 479.2402252446663,
              "semantic_passes": 2,
              "tokens_per_s": 35.39747617848492,
              "ttft_s": 0.5210234309999999
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.7814329659999997,
              "format_passes": 0,
              "gpu_energy_j": 1066.7198079941813,
              "semantic_passes": 0,
              "tokens_per_s": 35.42462298458554,
              "ttft_s": 0.194796325
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5799391030000001,
              "format_passes": 2,
              "gpu_energy_j": 142.97328687663605,
              "semantic_passes": 2,
              "tokens_per_s": 34.942252212972285,
              "ttft_s": 0.2078835835
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.924290039,
              "format_passes": 0,
              "gpu_energy_j": 242.8989698497968,
              "semantic_passes": 0,
              "tokens_per_s": 34.985963959785664,
              "ttft_s": 0.5240890810000001
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.468141656,
              "format_passes": 2,
              "gpu_energy_j": 108.786855783949,
              "semantic_passes": 2,
              "tokens_per_s": 34.12195358640925,
              "ttft_s": 0.204341385
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9892648310000001,
              "format_passes": 0,
              "gpu_energy_j": 265.7469357522423,
              "semantic_passes": 0,
              "tokens_per_s": 35.28992030526994,
              "ttft_s": 0.2241107655
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1453173845,
              "format_passes": 0,
              "gpu_energy_j": 293.547924544947,
              "semantic_passes": 2,
              "tokens_per_s": 35.344922278353586,
              "ttft_s": 0.353108663
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.793207229,
              "format_passes": 2,
              "gpu_energy_j": 1024.72587158797,
              "semantic_passes": 2,
              "tokens_per_s": 34.35473273365053,
              "ttft_s": 3.2109555690000002
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.574465891,
              "format_passes": 2,
              "gpu_energy_j": 141.93346107424236,
              "semantic_passes": 2,
              "tokens_per_s": 34.99680329387278,
              "ttft_s": 0.202998591
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7247492165,
              "format_passes": 0,
              "gpu_energy_j": 189.24322639977868,
              "semantic_passes": 0,
              "tokens_per_s": 697.8281313016279,
              "ttft_s": 0.7246209885
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.748125623,
              "format_passes": 0,
              "gpu_energy_j": 734.7784610854956,
              "semantic_passes": 0,
              "tokens_per_s": 745.5834432004972,
              "ttft_s": 2.747866738
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.467336519,
              "format_passes": 0,
              "gpu_energy_j": 1472.0727162003127,
              "semantic_passes": 0,
              "tokens_per_s": 749.4074530415236,
              "ttft_s": 5.4670214825
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.846092762,
              "format_passes": 0,
              "gpu_energy_j": 224.77126272102805,
              "semantic_passes": 2,
              "tokens_per_s": 35.23883890875482,
              "ttft_s": 0.22174793850000002
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.989523241,
              "format_passes": 0,
              "gpu_energy_j": 263.1163605099655,
              "semantic_passes": 2,
              "tokens_per_s": 34.95489529161206,
              "ttft_s": 0.2170504755
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0132581605,
              "format_passes": 0,
              "gpu_energy_j": 271.5974488159144,
              "semantic_passes": 2,
              "tokens_per_s": 35.30398981459216,
              "ttft_s": 0.2201404715
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7061539665,
              "format_passes": 0,
              "gpu_energy_j": 463.03587142234176,
              "semantic_passes": 0,
              "tokens_per_s": 35.047961136527746,
              "ttft_s": 1.0279458345
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7795557199999998,
              "format_passes": 0,
              "gpu_energy_j": 467.6994430396154,
              "semantic_passes": 0,
              "tokens_per_s": 35.025925800106194,
              "ttft_s": 1.0940412865
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
              "e2e_s": 1.766932122,
              "format_passes": 2,
              "gpu_energy_j": 484.1760241759545,
              "semantic_passes": 2,
              "tokens_per_s": 35.37421738501124,
              "ttft_s": 0.5230471569999999
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.7843703709999996,
              "format_passes": 0,
              "gpu_energy_j": 1070.0696966869573,
              "semantic_passes": 0,
              "tokens_per_s": 35.38623509859952,
              "ttft_s": 0.19472672000000002
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5808852105,
              "format_passes": 2,
              "gpu_energy_j": 147.96948471387407,
              "semantic_passes": 2,
              "tokens_per_s": 35.00586315314801,
              "ttft_s": 0.209447618
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9270642875,
              "format_passes": 0,
              "gpu_energy_j": 245.96491530102622,
              "semantic_passes": 0,
              "tokens_per_s": 34.85785519616024,
              "ttft_s": 0.525400933
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.46882854350000003,
              "format_passes": 2,
              "gpu_energy_j": 112.34378758005792,
              "semantic_passes": 2,
              "tokens_per_s": 34.088726829090874,
              "ttft_s": 0.204811733
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.990869079,
              "format_passes": 0,
              "gpu_energy_j": 265.5028950538048,
              "semantic_passes": 0,
              "tokens_per_s": 35.26017565443105,
              "ttft_s": 0.225070992
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1469634735,
              "format_passes": 0,
              "gpu_energy_j": 292.87321586184646,
              "semantic_passes": 2,
              "tokens_per_s": 35.27921297633247,
              "ttft_s": 0.353195329
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.8007306135,
              "format_passes": 2,
              "gpu_energy_j": 1021.5677152501717,
              "semantic_passes": 2,
              "tokens_per_s": 34.353258157897585,
              "ttft_s": 3.2184906294999998
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5753459670000001,
              "format_passes": 2,
              "gpu_energy_j": 144.6413968325213,
              "semantic_passes": 2,
              "tokens_per_s": 34.98269285604718,
              "ttft_s": 0.203666309
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7272138674999999,
              "format_passes": 0,
              "gpu_energy_j": 190.07779625932275,
              "semantic_passes": 0,
              "tokens_per_s": 695.4098149271196,
              "ttft_s": 0.7270803705
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.7440286305,
              "format_passes": 0,
              "gpu_energy_j": 736.497831897267,
              "semantic_passes": 0,
              "tokens_per_s": 746.6864064193859,
              "ttft_s": 2.7438021519999998
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.4683526664999995,
              "format_passes": 0,
              "gpu_energy_j": 1476.9134815875168,
              "semantic_passes": 0,
              "tokens_per_s": 749.2742777396576,
              "ttft_s": 5.468002212
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8490458275,
              "format_passes": 0,
              "gpu_energy_j": 225.38044022968649,
              "semantic_passes": 2,
              "tokens_per_s": 35.217685349459444,
              "ttft_s": 0.2243069
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9858982035,
              "format_passes": 0,
              "gpu_energy_j": 258.55637211201224,
              "semantic_passes": 2,
              "tokens_per_s": 35.10931413166011,
              "ttft_s": 0.216814006
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0154827924999998,
              "format_passes": 0,
              "gpu_energy_j": 271.51843008040015,
              "semantic_passes": 2,
              "tokens_per_s": 35.222009253565574,
              "ttft_s": 0.220480345
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.707636765,
              "format_passes": 0,
              "gpu_energy_j": 461.49093665917627,
              "semantic_passes": 0,
              "tokens_per_s": 34.97537448954709,
              "ttft_s": 1.0281933985
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.780480407,
              "format_passes": 0,
              "gpu_energy_j": 468.0795762394581,
              "semantic_passes": 0,
              "tokens_per_s": 35.03949652295837,
              "ttft_s": 1.094231881
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
            "e2e_change_pct": 0.16081257653870473,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.0299216700285108,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.06570749099851225,
            "ttft_change_pct": 0.38841362587396233
          },
          "decode": {
            "e2e_change_pct": 0.07767967927532204,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.31403641965503937,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.10836498105490922,
            "ttft_change_pct": -0.035732193612980634
          },
          "energy": {
            "e2e_change_pct": 0.16313911152148197,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.49449743122221,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.1820459075964065,
            "ttft_change_pct": 0.7523607557977208
          },
          "filtering": {
            "e2e_change_pct": 0.30014912883855605,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.26223073450058,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.36617188473835327,
            "ttft_change_pct": 0.2503108817869082
          },
          "german": {
            "e2e_change_pct": 0.14672642162825156,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.2696337902926365,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.0973764800254795,
            "ttft_change_pct": 0.23017755311778298
          },
          "ha_sim": {
            "e2e_change_pct": 0.162165675937187,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.09183198961322248,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.0842865344596544,
            "ttft_change_pct": 0.4284606756206788
          },
          "jarvis_memory": {
            "e2e_change_pct": 0.1437233925091208,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.22984617729676637,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.1859087466755116,
            "ttft_change_pct": 0.024543719563174804
          },
          "long_context": {
            "e2e_change_pct": 0.19833834657072558,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.3081952379034081,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.004292205572886676,
            "ttft_change_pct": 0.2346672303019881
          },
          "math": {
            "e2e_change_pct": 0.15319899993855302,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.9078910200481136,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.04031921917871939,
            "ttft_change_pct": 0.32892740620056315
          },
          "prefill": {
            "e2e_change_pct": 0.3400694949216243,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.44100382107259417,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.3465489948072942,
            "ttft_change_pct": 0.33940253443265345
          },
          "prefill2048": {
            "e2e_change_pct": -0.14908315928904292,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.23399853191550246,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.14793290126644543,
            "ttft_change_pct": -0.1479178718455043
          },
          "prefill4096": {
            "e2e_change_pct": 0.01858578663429533,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.328840099672445,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.017770746918177593,
            "ttft_change_pct": 0.0179390094430687
          },
          "pve_sim": {
            "e2e_change_pct": 0.34902384615835835,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.27102108218099996,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.060029104109105,
            "ttft_change_pct": 1.1539956210235403
          },
          "sorting": {
            "e2e_change_pct": -0.36634182501227297,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.7330691216293825,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.44176599231613434,
            "ttft_change_pct": -0.10894677814239362
          },
          "time": {
            "e2e_change_pct": 0.21955233984023437,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.029094063975465545,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.2322133035306373,
            "ttft_change_pct": 0.15438937587630708
          },
          "tool-call": {
            "e2e_change_pct": 0.08690883291393448,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.3336533643537809,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.20710661797955776,
            "ttft_change_pct": 0.024083370124294845
          },
          "tool-final": {
            "e2e_change_pct": 0.051961677266287865,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.08127724022337635,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.03874479415513221,
            "ttft_change_pct": 0.017421143274187756
          }
        }
      },
      "complete": true
    }
  }
}
```
