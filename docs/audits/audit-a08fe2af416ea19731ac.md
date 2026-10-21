# Public audit excerpt

Original SHA256: `a08fe2af416ea19731ac19f95f693f04c972a161af01c8e7942416aa84b7b0c2`

Original file: `RESULTS.json`; 39661 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.672095349,
              "format_passes": 2,
              "gpu_energy_j": 175.67881944530407,
              "semantic_passes": 2,
              "tokens_per_s": 78.42616690200208,
              "ttft_s": 0.1237183875
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6590662445,
              "format_passes": 0,
              "gpu_energy_j": 456.1723222416589,
              "semantic_passes": 0,
              "tokens_per_s": 79.59715068021748,
              "ttft_s": 0.063040549
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.24122017099999998,
              "format_passes": 2,
              "gpu_energy_j": 59.52070073018553,
              "semantic_passes": 2,
              "tokens_per_s": 76.72201073627011,
              "ttft_s": 0.0716435205
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2421858025,
              "format_passes": 0,
              "gpu_energy_j": 58.270057602488365,
              "semantic_passes": 0,
              "tokens_per_s": 77.4472020604745,
              "ttft_s": 0.125982496
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.18272584050000001,
              "format_passes": 2,
              "gpu_energy_j": 38.226817855230955,
              "semantic_passes": 2,
              "tokens_per_s": 77.5107074288199,
              "ttft_s": 0.06661262500000001
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35792550749999996,
              "format_passes": 0,
              "gpu_energy_j": 88.66600116438929,
              "semantic_passes": 0,
              "tokens_per_s": 78.78589728949655,
              "ttft_s": 0.0786633375
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.46878409899999995,
              "format_passes": 0,
              "gpu_energy_j": 113.94383117419149,
              "semantic_passes": 2,
              "tokens_per_s": 79.1261165044742,
              "ttft_s": 0.11483182650000001
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0790911395,
              "format_passes": 2,
              "gpu_energy_j": 286.1977087114801,
              "semantic_passes": 2,
              "tokens_per_s": 77.86376407898464,
              "ttft_s": 0.8221777375
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.233764221,
              "format_passes": 0,
              "gpu_energy_j": 52.78716864468898,
              "semantic_passes": 0,
              "tokens_per_s": 78.24797784612463,
              "ttft_s": 0.0676193945
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.1986707035,
              "format_passes": 0,
              "gpu_energy_j": 48.64481430536203,
              "semantic_passes": 0,
              "tokens_per_s": 2555.839529104838,
              "ttft_s": 0.198479093
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7174281849999999,
              "format_passes": 0,
              "gpu_energy_j": 189.97334607988157,
              "semantic_passes": 0,
              "tokens_per_s": 2859.796431635439,
              "ttft_s": 0.7171412475
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4181291599999999,
              "format_passes": 0,
              "gpu_energy_j": 380.9931988277741,
              "semantic_passes": 0,
              "tokens_per_s": 2891.7898272579882,
              "ttft_s": 1.417819621
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.294773331,
              "format_passes": 2,
              "gpu_energy_j": 72.42893231850508,
              "semantic_passes": 2,
              "tokens_per_s": 78.741254885856,
              "ttft_s": 0.0788393735
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.352502459,
              "format_passes": 2,
              "gpu_energy_j": 90.62001777040905,
              "semantic_passes": 2,
              "tokens_per_s": 78.81448864622368,
              "ttft_s": 0.073338479
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.369314963,
              "format_passes": 2,
              "gpu_energy_j": 93.83063271110714,
              "semantic_passes": 2,
              "tokens_per_s": 78.9014415947023,
              "ttft_s": 0.0777823885
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.620023406,
              "format_passes": 0,
              "gpu_energy_j": 161.27904645708634,
              "semantic_passes": 0,
              "tokens_per_s": 79.03633435837325,
              "ttft_s": 0.318476022
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.560920054,
              "format_passes": 0,
              "gpu_energy_j": 146.2824303825167,
              "semantic_passes": 0,
              "tokens_per_s": 78.79522735149723,
              "ttft_s": 0.2564438325
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
              "e2e_s": 0.666578139,
              "format_passes": 2,
              "gpu_energy_j": 177.22861355196892,
              "semantic_passes": 2,
              "tokens_per_s": 79.21730023102192,
              "ttft_s": 0.123762842
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.658121619,
              "format_passes": 0,
              "gpu_energy_j": 458.8829903398994,
              "semantic_passes": 0,
              "tokens_per_s": 79.6268948390108,
              "ttft_s": 0.0629478825
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2377814785,
              "format_passes": 2,
              "gpu_energy_j": 56.58328337740317,
              "semantic_passes": 2,
              "tokens_per_s": 78.33095936534681,
              "ttft_s": 0.0717985085
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.24165939949999998,
              "format_passes": 0,
              "gpu_energy_j": 62.552825358267434,
              "semantic_passes": 0,
              "tokens_per_s": 77.4344977576321,
              "ttft_s": 0.12541526800000002
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1823178155,
              "format_passes": 2,
              "gpu_energy_j": 42.74646137349657,
              "semantic_passes": 2,
              "tokens_per_s": 77.25095667683503,
              "ttft_s": 0.0658405435
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3580725295,
              "format_passes": 0,
              "gpu_energy_j": 91.837883754248,
              "semantic_passes": 0,
              "tokens_per_s": 78.7976206523411,
              "ttft_s": 0.078817019
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.47185983,
              "format_passes": 0,
              "gpu_energy_j": 116.73137845244842,
              "semantic_passes": 2,
              "tokens_per_s": 78.52537827145164,
              "ttft_s": 0.115230159
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0791453364999999,
              "format_passes": 2,
              "gpu_energy_j": 287.3380250233297,
              "semantic_passes": 2,
              "tokens_per_s": 78.02899073821429,
              "ttft_s": 0.822772088
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.233366716,
              "format_passes": 0,
              "gpu_energy_j": 57.57611872371297,
              "semantic_passes": 0,
              "tokens_per_s": 78.24561762861055,
              "ttft_s": 0.06719463049999999
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.198942001,
              "format_passes": 0,
              "gpu_energy_j": 48.913618790293626,
              "semantic_passes": 0,
              "tokens_per_s": 2551.3331079616382,
              "ttft_s": 0.198780114
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.716831693,
              "format_passes": 0,
              "gpu_energy_j": 190.38073684399382,
              "semantic_passes": 0,
              "tokens_per_s": 2861.884058659998,
              "ttft_s": 0.7166052525
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4167351835,
              "format_passes": 0,
              "gpu_energy_j": 382.54445446535783,
              "semantic_passes": 0,
              "tokens_per_s": 2894.5580874747366,
              "ttft_s": 1.4164098885
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.295172983,
              "format_passes": 2,
              "gpu_energy_j": 69.60708877660974,
              "semantic_passes": 2,
              "tokens_per_s": 78.59663552351134,
              "ttft_s": 0.07884404049999999
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.356246281,
              "format_passes": 2,
              "gpu_energy_j": 85.66567367427993,
              "semantic_passes": 2,
              "tokens_per_s": 78.07397142967852,
              "ttft_s": 0.0744005845
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.369112071,
              "format_passes": 2,
              "gpu_energy_j": 94.87482948171356,
              "semantic_passes": 2,
              "tokens_per_s": 78.98387493612888,
              "ttft_s": 0.07784838699999999
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.619564817,
              "format_passes": 0,
              "gpu_energy_j": 161.37053700807198,
              "semantic_passes": 0,
              "tokens_per_s": 78.99206500481442,
              "ttft_s": 0.3183184325
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.561480387,
              "format_passes": 0,
              "gpu_energy_j": 147.3948557088073,
              "semantic_passes": 0,
              "tokens_per_s": 78.85244024630155,
              "ttft_s": 0.2567443945
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
            "e2e_change_pct": -0.8208969171128788,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.8821747047015993,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 1.008761948047776,
            "ttft_change_pct": 0.035932007277406086
          },
          "decode": {
            "e2e_change_pct": -0.05693717795364206,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.5942202027777732,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.03736837127854553,
            "ttft_change_pct": -0.14699507137858614
          },
          "energy": {
            "e2e_change_pct": -1.4255410257544288,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -4.935118902746161,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 2.097114783145382,
            "ttft_change_pct": 0.21633219433987438
          },
          "filtering": {
            "e2e_change_pct": -0.21735502022254272,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 7.349860171746547,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.01640382415942776,
            "ttft_change_pct": -0.4502435004938854
          },
          "german": {
            "e2e_change_pct": -0.22329901391259233,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 11.823227178840767,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.3351159608798615,
            "ttft_change_pct": -1.1590618144833753
          },
          "ha_sim": {
            "e2e_change_pct": 0.04107614487354194,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.577338041870126,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.014880027070662827,
            "ttft_change_pct": 0.19536610686015088
          },
          "jarvis_memory": {
            "e2e_change_pct": 0.6561082183805134,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.4464222850252293,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.7592161217574556,
            "ttft_change_pct": 0.3468833616436351
          },
          "long_context": {
            "e2e_change_pct": 0.005022467335336067,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.3984365622574426,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.2121996813075233,
            "ttft_change_pct": 0.07228978271867081
          },
          "math": {
            "e2e_change_pct": -0.17004526967366873,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 9.072185915593355,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.0030163303628372162,
            "ttft_change_pct": -0.6281688902138982
          },
          "prefill": {
            "e2e_change_pct": 0.13655636952027983,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.5525861055696524,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.17631862610631988,
            "ttft_change_pct": 0.15166383292573027
          },
          "prefill2048": {
            "e2e_change_pct": -0.08314309536081588,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.21444627497424484,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.07299914782274985,
            "ttft_change_pct": -0.0747405064021267
          },
          "prefill4096": {
            "e2e_change_pct": -0.09829686458178166,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.4071609788197206,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.09572826457353578,
            "ttft_change_pct": -0.09942960861309968
          },
          "pve_sim": {
            "e2e_change_pct": 0.13557942933446476,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.896017035687227,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.18366403044286495,
            "ttft_change_pct": 0.005919631007711423
          },
          "sorting": {
            "e2e_change_pct": 1.0620697542424784,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -5.46716301544018,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.9395699055653739,
            "ttft_change_pct": 1.4482240625688592
          },
          "time": {
            "e2e_change_pct": -0.05493738957985661,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.1128527437530567,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.1044763438544205,
            "ttft_change_pct": 0.0848501843061733
          },
          "tool-call": {
            "e2e_change_pct": -0.0739631755127701,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.05672810758463598,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.05601139516174802,
            "ttft_change_pct": -0.04948237515978171
          },
          "tool-final": {
            "e2e_change_pct": 0.09989534087864183,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.760464071715039,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.0726095941688154,
            "ttft_change_pct": 0.11720383253901456
          }
        }
      },
      "complete": true
    }
  }
}
```
