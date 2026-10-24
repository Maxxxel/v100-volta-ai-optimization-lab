# Public audit excerpt

Original SHA256: `54c9c1f289d2493eee4b2aae313b007122e6500879d3c61909b1ea53ba89b470`

Original file: `RESULTS.json`; 39611 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.6738349825,
              "format_passes": 2,
              "gpu_energy_j": 171.8539175493217,
              "semantic_passes": 2,
              "tokens_per_s": 78.34576686957863,
              "ttft_s": 0.12488290249999999
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.658717253,
              "format_passes": 0,
              "gpu_energy_j": 445.0000523785392,
              "semantic_passes": 0,
              "tokens_per_s": 79.5877492366321,
              "ttft_s": 0.0627316665
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23742037700000002,
              "format_passes": 2,
              "gpu_energy_j": 53.04686383665788,
              "semantic_passes": 2,
              "tokens_per_s": 78.38833591823601,
              "ttft_s": 0.0714646495
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.241792038,
              "format_passes": 0,
              "gpu_energy_j": 59.58218112926602,
              "semantic_passes": 0,
              "tokens_per_s": 77.46430361831833,
              "ttft_s": 0.125580959
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.18214036649999998,
              "format_passes": 2,
              "gpu_energy_j": 42.464235665828994,
              "semantic_passes": 2,
              "tokens_per_s": 77.52313865478025,
              "ttft_s": 0.0659993555
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35881203500000003,
              "format_passes": 0,
              "gpu_energy_j": 91.02008390975695,
              "semantic_passes": 0,
              "tokens_per_s": 78.62400889280784,
              "ttft_s": 0.0789723575
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.47074554599999996,
              "format_passes": 0,
              "gpu_energy_j": 114.04887469559023,
              "semantic_passes": 2,
              "tokens_per_s": 78.85720197893477,
              "ttft_s": 0.1157213775
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0748346805,
              "format_passes": 2,
              "gpu_energy_j": 283.66264971558564,
              "semantic_passes": 2,
              "tokens_per_s": 78.0930977730583,
              "ttft_s": 0.818632106
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.234298184,
              "format_passes": 0,
              "gpu_energy_j": 55.25871589373591,
              "semantic_passes": 0,
              "tokens_per_s": 77.84286866200291,
              "ttft_s": 0.067274782
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.19682769,
              "format_passes": 0,
              "gpu_energy_j": 46.61960924145178,
              "semantic_passes": 0,
              "tokens_per_s": 2579.6831518709464,
              "ttft_s": 0.196651005
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7116823005,
              "format_passes": 0,
              "gpu_energy_j": 188.14483972645314,
              "semantic_passes": 0,
              "tokens_per_s": 2882.7530146810286,
              "ttft_s": 0.711436888
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.407612761,
              "format_passes": 0,
              "gpu_energy_j": 378.7163015345759,
              "semantic_passes": 0,
              "tokens_per_s": 2913.5956757099266,
              "ttft_s": 1.4072543645
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.29473578899999997,
              "format_passes": 2,
              "gpu_energy_j": 72.66144945999439,
              "semantic_passes": 2,
              "tokens_per_s": 78.66293339373075,
              "ttft_s": 0.07858357399999999
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35261588200000005,
              "format_passes": 2,
              "gpu_energy_j": 86.87238310671913,
              "semantic_passes": 2,
              "tokens_per_s": 78.8452777555033,
              "ttft_s": 0.0735221505
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3690051085,
              "format_passes": 2,
              "gpu_energy_j": 91.05212301031528,
              "semantic_passes": 2,
              "tokens_per_s": 78.91712429164274,
              "ttft_s": 0.077523468
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6187689194999999,
              "format_passes": 0,
              "gpu_energy_j": 156.5484747938377,
              "semantic_passes": 0,
              "tokens_per_s": 79.05668609444763,
              "ttft_s": 0.3167642905
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.559327975,
              "format_passes": 0,
              "gpu_energy_j": 143.79552499113368,
              "semantic_passes": 0,
              "tokens_per_s": 78.86140064117964,
              "ttft_s": 0.2546600825
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
              "e2e_s": 0.5659235515,
              "format_passes": 2,
              "gpu_energy_j": 144.8834807040717,
              "semantic_passes": 2,
              "tokens_per_s": 79.26897413592238,
              "ttft_s": 0.086539822
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.657474236,
              "format_passes": 0,
              "gpu_energy_j": 449.72552791493706,
              "semantic_passes": 0,
              "tokens_per_s": 79.62197745128906,
              "ttft_s": 0.062248667
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2380301515,
              "format_passes": 2,
              "gpu_energy_j": 57.587080390564914,
              "semantic_passes": 2,
              "tokens_per_s": 78.21072112480772,
              "ttft_s": 0.0717887045
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.20902272,
              "format_passes": 0,
              "gpu_energy_j": 47.98953934390541,
              "semantic_passes": 0,
              "tokens_per_s": 77.61131206291931,
              "ttft_s": 0.093017654
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1823742935,
              "format_passes": 2,
              "gpu_energy_j": 40.7444802955996,
              "semantic_passes": 2,
              "tokens_per_s": 77.69035372920317,
              "ttft_s": 0.066481673
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3584736605,
              "format_passes": 0,
              "gpu_energy_j": 89.38175610153536,
              "semantic_passes": 0,
              "tokens_per_s": 78.6625700457954,
              "ttft_s": 0.07874053
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.46815952250000004,
              "format_passes": 0,
              "gpu_energy_j": 117.84797930398622,
              "semantic_passes": 2,
              "tokens_per_s": 79.1533264806636,
              "ttft_s": 0.11434506950000001
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.46903392,
              "format_passes": 2,
              "gpu_energy_j": 400.55014367380784,
              "semantic_passes": 2,
              "tokens_per_s": 78.02977111645957,
              "ttft_s": 1.2127001455
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2330155975,
              "format_passes": 0,
              "gpu_energy_j": 52.79553361662664,
              "semantic_passes": 0,
              "tokens_per_s": 78.35502664343153,
              "ttft_s": 0.0670436545
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.2980242105,
              "format_passes": 0,
              "gpu_energy_j": 78.44495570730444,
              "semantic_passes": 0,
              "tokens_per_s": 1700.7032380762607,
              "ttft_s": 0.2978941825
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.1095779155,
              "format_passes": 0,
              "gpu_energy_j": 308.0901419663649,
              "semantic_passes": 0,
              "tokens_per_s": 1847.8793134630655,
              "ttft_s": 1.1093064465
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.1987093924999996,
              "format_passes": 0,
              "gpu_energy_j": 622.3320337559912,
              "semantic_passes": 0,
              "tokens_per_s": 1864.3596466956033,
              "ttft_s": 2.1983717025000002
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3005729345,
              "format_passes": 2,
              "gpu_energy_j": 70.19068293187024,
              "semantic_passes": 2,
              "tokens_per_s": 77.16450265334385,
              "ttft_s": 0.0801320885
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.352851162,
              "format_passes": 2,
              "gpu_energy_j": 87.5274873023709,
              "semantic_passes": 2,
              "tokens_per_s": 78.73901178005053,
              "ttft_s": 0.0734171195
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.369350544,
              "format_passes": 2,
              "gpu_energy_j": 93.30155416890969,
              "semantic_passes": 2,
              "tokens_per_s": 78.88447337128154,
              "ttft_s": 0.0777446935
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6574554025,
              "format_passes": 0,
              "gpu_energy_j": 171.51706125233477,
              "semantic_passes": 0,
              "tokens_per_s": 79.19794152967566,
              "ttft_s": 0.356307598
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5928289795,
              "format_passes": 0,
              "gpu_energy_j": 150.9921515389201,
              "semantic_passes": 0,
              "tokens_per_s": 78.8469961658806,
              "ttft_s": 0.2884186875
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
            "e2e_change_pct": -16.014518955314106,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -15.693815555592172,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 1.1783754288609005,
            "ttft_change_pct": -30.703226568584906
          },
          "decode": {
            "e2e_change_pct": -0.0749384500433603,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.0619044899298435,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.04300688860439106,
            "ttft_change_pct": -0.7699452715798749
          },
          "energy": {
            "e2e_change_pct": 0.25683326246255245,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 8.5588783681676,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.2265831916798855,
            "ttft_change_pct": 0.4534479666061797
          },
          "filtering": {
            "e2e_change_pct": -13.552686958203308,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -19.456558262293033,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.18977572602385528,
            "ttft_change_pct": -25.930129264262103
          },
          "german": {
            "e2e_change_pct": 0.12843226600185442,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -4.04989126323374,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.21569698715055985,
            "ttft_change_pct": 0.7307912271961703
          },
          "ha_sim": {
            "e2e_change_pct": -0.0943041110647247,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.7999629728378763,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.04904500995381866,
            "ttft_change_pct": -0.29355524811324196
          },
          "jarvis_memory": {
            "e2e_change_pct": -0.5493463553662425,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.33111976644771,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.3755199199280801,
            "ttft_change_pct": -1.1893290848529636
          },
          "long_context": {
            "e2e_change_pct": 36.67533683567257,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 41.206515583006585,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.0810912339305081,
            "ttft_change_pct": 48.13737900233293
          },
          "math": {
            "e2e_change_pct": -0.547416321417149,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -4.457545270950625,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.6579382160907032,
            "ttft_change_pct": -0.3435574120478124
          },
          "prefill": {
            "e2e_change_pct": 51.413762209981726,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 68.26600862530437,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -34.073173411129765,
            "ttft_change_pct": 51.483681713195416
          },
          "prefill2048": {
            "e2e_change_pct": 55.90916265873891,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 63.75157693099753,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -35.89879868124846,
            "ttft_change_pct": 55.92478619129457
          },
          "prefill4096": {
            "e2e_change_pct": 56.20129721884495,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 64.32670873534441,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -36.01172385590758,
            "ttft_change_pct": 56.21708185506931
          },
          "pve_sim": {
            "e2e_change_pct": 1.9804671566370446,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.4003815592537623,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -1.9048752388711843,
            "ttft_change_pct": 1.9705320351044442
          },
          "sorting": {
            "e2e_change_pct": 0.06672416417135008,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.7540994873445728,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.13477785668064568,
            "ttft_change_pct": -0.14285626751354696
          },
          "time": {
            "e2e_change_pct": 0.09361266064964457,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.4704873255284365,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.04137368239690575,
            "ttft_change_pct": 0.285365845604324
          },
          "tool-call": {
            "e2e_change_pct": 6.2521697164849455,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 9.561630337318562,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.17867614012971877,
            "ttft_change_pct": 12.483511773875279
          },
          "tool-final": {
            "e2e_change_pct": 5.989509911425417,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 5.004763916144239,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.018265558539320992,
            "ttft_change_pct": 13.256339457912492
          }
        }
      },
      "complete": true
    }
  }
}
```

</details>
