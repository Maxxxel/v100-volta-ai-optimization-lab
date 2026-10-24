# Public audit excerpt

Original SHA256: `15357beaac0b3905a2ce246be1c8d96651fd7d82b0f005f86df485e7967b7246`

Original file: `RESULTS.json`; 40885 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.665723465,
              "format_passes": 2,
              "gpu_energy_j": 174.09536983381776,
              "semantic_passes": 2,
              "tokens_per_s": 79.30517547056556,
              "ttft_s": 0.12346028049999999
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6595474835,
              "format_passes": 0,
              "gpu_energy_j": 447.2559714337516,
              "semantic_passes": 0,
              "tokens_per_s": 79.54430529941453,
              "ttft_s": 0.063047483
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2374911615,
              "format_passes": 2,
              "gpu_energy_j": 55.333081653908465,
              "semantic_passes": 2,
              "tokens_per_s": 78.31397818171143,
              "ttft_s": 0.071426692
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.241639991,
              "format_passes": 0,
              "gpu_energy_j": 54.46574540442871,
              "semantic_passes": 0,
              "tokens_per_s": 77.47787755395098,
              "ttft_s": 0.1254633265
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.18164752550000002,
              "format_passes": 2,
              "gpu_energy_j": 41.62108603675486,
              "semantic_passes": 2,
              "tokens_per_s": 77.71998446316954,
              "ttft_s": 0.06584357199999999
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3577558965,
              "format_passes": 0,
              "gpu_energy_j": 89.7995650238712,
              "semantic_passes": 0,
              "tokens_per_s": 78.92136447081938,
              "ttft_s": 0.07895901899999999
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.470085278,
              "format_passes": 0,
              "gpu_energy_j": 118.2957639722483,
              "semantic_passes": 2,
              "tokens_per_s": 78.83120674149075,
              "ttft_s": 0.1148292475
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.074094048,
              "format_passes": 2,
              "gpu_energy_j": 285.3186442571681,
              "semantic_passes": 2,
              "tokens_per_s": 78.00343645418724,
              "ttft_s": 0.817667536
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23340481400000002,
              "format_passes": 0,
              "gpu_energy_j": 52.984305547031894,
              "semantic_passes": 0,
              "tokens_per_s": 78.20538632504112,
              "ttft_s": 0.067113729
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.198321737,
              "format_passes": 0,
              "gpu_energy_j": 47.78879578575195,
              "semantic_passes": 0,
              "tokens_per_s": 2560.7154564814273,
              "ttft_s": 0.198173101
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.713841878,
              "format_passes": 0,
              "gpu_energy_j": 186.78306219383052,
              "semantic_passes": 0,
              "tokens_per_s": 2873.950459427995,
              "ttft_s": 0.7136059905000001
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4095420095,
              "format_passes": 0,
              "gpu_energy_j": 376.3096234432274,
              "semantic_passes": 0,
              "tokens_per_s": 2909.5667523702577,
              "ttft_s": 1.4092044124999998
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2952174895,
              "format_passes": 2,
              "gpu_energy_j": 73.69122090573266,
              "semantic_passes": 2,
              "tokens_per_s": 78.61621703001168,
              "ttft_s": 0.07894288199999999
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3529598305,
              "format_passes": 2,
              "gpu_energy_j": 88.30559179150634,
              "semantic_passes": 2,
              "tokens_per_s": 78.8481283324939,
              "ttft_s": 0.07390936449999999
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3702103945,
              "format_passes": 2,
              "gpu_energy_j": 92.70334209867177,
              "semantic_passes": 2,
              "tokens_per_s": 78.67900825660965,
              "ttft_s": 0.07787986
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.619237907,
              "format_passes": 0,
              "gpu_energy_j": 155.7681752877358,
              "semantic_passes": 0,
              "tokens_per_s": 78.94633071635693,
              "ttft_s": 0.318089564
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5598907215,
              "format_passes": 0,
              "gpu_energy_j": 141.71125265318278,
              "semantic_passes": 0,
              "tokens_per_s": 78.83572843509799,
              "ttft_s": 0.255415553
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
              "e2e_s": 0.675451351,
              "format_passes": 2,
              "gpu_energy_j": 178.90901554866866,
              "semantic_passes": 2,
              "tokens_per_s": 78.01642337353125,
              "ttft_s": 0.1241993385
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6865053845,
              "format_passes": 0,
              "gpu_energy_j": 448.9496515477034,
              "semantic_passes": 0,
              "tokens_per_s": 78.25840154168368,
              "ttft_s": 0.0634800745
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.24171227750000002,
              "format_passes": 2,
              "gpu_energy_j": 54.23570979408015,
              "semantic_passes": 2,
              "tokens_per_s": 76.91206024615104,
              "ttft_s": 0.07252153650000001
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.244075898,
              "format_passes": 0,
              "gpu_energy_j": 59.08007873847772,
              "semantic_passes": 0,
              "tokens_per_s": 76.26612015915686,
              "ttft_s": 0.1259995115
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1851206165,
              "format_passes": 2,
              "gpu_energy_j": 39.26956983207677,
              "semantic_passes": 2,
              "tokens_per_s": 76.28522352900018,
              "ttft_s": 0.0671206
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.36348093,
              "format_passes": 0,
              "gpu_energy_j": 91.326169862287,
              "semantic_passes": 0,
              "tokens_per_s": 77.37584597117069,
              "ttft_s": 0.07911441550000001
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.476139932,
              "format_passes": 0,
              "gpu_energy_j": 116.41614366192854,
              "semantic_passes": 2,
              "tokens_per_s": 77.71373443611515,
              "ttft_s": 0.11578281300000001
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0829188665,
              "format_passes": 2,
              "gpu_energy_j": 286.7520421201706,
              "semantic_passes": 2,
              "tokens_per_s": 76.52698838227897,
              "ttft_s": 0.821535542
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2370209735,
              "format_passes": 0,
              "gpu_energy_j": 56.270855643961895,
              "semantic_passes": 0,
              "tokens_per_s": 76.93981577387657,
              "ttft_s": 0.067960168
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.1984085255,
              "format_passes": 0,
              "gpu_energy_j": 49.10659625215175,
              "semantic_passes": 0,
              "tokens_per_s": 2558.4193752696647,
              "ttft_s": 0.1982729855
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.714284203,
              "format_passes": 0,
              "gpu_energy_j": 188.0034077851418,
              "semantic_passes": 0,
              "tokens_per_s": 2872.0703355183105,
              "ttft_s": 0.714054273
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4133407660000001,
              "format_passes": 0,
              "gpu_energy_j": 380.21677766661196,
              "semantic_passes": 0,
              "tokens_per_s": 2901.6118375838096,
              "ttft_s": 1.413017214
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2996244015,
              "format_passes": 2,
              "gpu_energy_j": 70.46028578199733,
              "semantic_passes": 2,
              "tokens_per_s": 77.36427444270456,
              "ttft_s": 0.07983925350000001
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35843051,
              "format_passes": 2,
              "gpu_energy_j": 86.85678762968341,
              "semantic_passes": 2,
              "tokens_per_s": 77.54192462703656,
              "ttft_s": 0.07467235
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.374300502,
              "format_passes": 2,
              "gpu_energy_j": 89.91236100528589,
              "semantic_passes": 2,
              "tokens_per_s": 77.62835356689578,
              "ttft_s": 0.0779835945
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6268534565,
              "format_passes": 0,
              "gpu_energy_j": 159.43085275368267,
              "semantic_passes": 0,
              "tokens_per_s": 77.68946852071892,
              "ttft_s": 0.3204627795
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5658159185,
              "format_passes": 0,
              "gpu_energy_j": 143.88924131373352,
              "semantic_passes": 0,
              "tokens_per_s": 77.44883554460817,
              "ttft_s": 0.25592189200000004
            }
          }
        }
      },
      "comparison": {
        "format_pass_change": 0,
        "note": "Descriptive paired comparison; actual fresh starts per arm: {'A': 2, 'B': 2}. Quality and speed remain separate.",
        "quality_pass_change": 0,
        "status": "DESCRIPTIVE_COMPARISON",
        "tasks": {
          "code": {
            "e2e_change_pct": 1.4612502805500416,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.764947579849908,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.625054215424604,
            "ttft_change_pct": 0.5986200557838606
          },
          "decode": {
            "e2e_change_pct": 1.624412755165383,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.37868250445542984,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.6165880799267174,
            "ttft_change_pct": 0.6861360349627255
          },
          "energy": {
            "e2e_change_pct": 1.7773781446599246,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.983211176800237,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.7901247875666937,
            "ttft_change_pct": 1.532822631629105
          },
          "filtering": {
            "e2e_change_pct": 1.0080727904016484,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 8.471991523820787,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.5640043752493393,
            "ttft_change_pct": 0.4273639277370789
          },
          "german": {
            "e2e_change_pct": 1.9119946668362253,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -5.649819427108438,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.8460643605111349,
            "ttft_change_pct": 1.9394877301006863
          },
          "ha_sim": {
            "e2e_change_pct": 1.6002625130736359,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.70001362257155,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.9583017982667261,
            "ttft_change_pct": 0.19680652314084668
          },
          "jarvis_memory": {
            "e2e_change_pct": 1.2879905590236218,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.5889159909062367,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.4175506776651248,
            "ttft_change_pct": 0.8304204031294615
          },
          "long_context": {
            "e2e_change_pct": 0.8216057538380506,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.5023849271169611,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.8927987522388334,
            "ttft_change_pct": 0.47305363484555496
          },
          "math": {
            "e2e_change_pct": 1.549308018985407,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 6.202874724879948,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.6182651996686226,
            "ttft_change_pct": 1.261200968284748
          },
          "prefill": {
            "e2e_change_pct": 0.043761466248137815,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.757551105300493,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.08966561302041764,
            "ttft_change_pct": 0.050402652779801826
          },
          "prefill2048": {
            "e2e_change_pct": 0.06196400262188373,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.653349172552331,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.06541949613351195,
            "ttft_change_pct": 0.06281932970964021
          },
          "prefill4096": {
            "e2e_change_pct": 0.269502893450313,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.038281771173999,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.2734054745424763,
            "ttft_change_pct": 0.27056411874526454
          },
          "pve_sim": {
            "e2e_change_pct": 1.4927679276264705,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -4.384423387242309,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.5924737091193242,
            "ttft_change_pct": 1.135468426399755
          },
          "sorting": {
            "e2e_change_pct": 1.549943939017151,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.6406709161109867,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.6566071168477414,
            "ttft_change_pct": 1.0323258834135984
          },
          "time": {
            "e2e_change_pct": 1.1048062293129268,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.0106585482271075,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.3353684966226131,
            "ttft_change_pct": 0.13319810795757725
          },
          "tool-call": {
            "e2e_change_pct": 1.2298261159260582,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.3513644293394087,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.5920463740787816,
            "ttft_change_pct": 0.7460840494597276
          },
          "tool-final": {
            "e2e_change_pct": 1.0582774052990018,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.536920053823132,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.7592187172236096,
            "ttft_change_pct": 0.19824125588780994
          }
        }
      },
      "complete": true
    }
  }
}
```

</details>
