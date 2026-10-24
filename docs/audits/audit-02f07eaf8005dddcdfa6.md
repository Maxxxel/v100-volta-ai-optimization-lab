# Public audit excerpt

Original SHA256: `02f07eaf8005dddcdfa6f09282dfdf1810bef220901cc7bfeec4ce462f6ba608`

Original file: `RESULTS.json`; 39776 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 1.7650295445,
              "format_passes": 2,
              "gpu_energy_j": 481.92215256995496,
              "semantic_passes": 2,
              "tokens_per_s": 35.34117612910319,
              "ttft_s": 0.5199672280000001
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.7826528895,
              "format_passes": 0,
              "gpu_energy_j": 1068.616038683364,
              "semantic_passes": 0,
              "tokens_per_s": 35.391700008234324,
              "ttft_s": 0.194285577
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5808914445,
              "format_passes": 2,
              "gpu_energy_j": 147.31997649859812,
              "semantic_passes": 2,
              "tokens_per_s": 34.92132633490986,
              "ttft_s": 0.208591413
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.924593421,
              "format_passes": 0,
              "gpu_energy_j": 244.95186957132447,
              "semantic_passes": 0,
              "tokens_per_s": 35.00971865848527,
              "ttft_s": 0.5246964525
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4659705255,
              "format_passes": 2,
              "gpu_energy_j": 110.20692002759529,
              "semantic_passes": 2,
              "tokens_per_s": 34.262872732804794,
              "ttft_s": 0.2032438925
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9883057435,
              "format_passes": 0,
              "gpu_energy_j": 265.7715332008554,
              "semantic_passes": 0,
              "tokens_per_s": 35.29323416581162,
              "ttft_s": 0.223256883
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1457973285,
              "format_passes": 0,
              "gpu_energy_j": 299.0157586317889,
              "semantic_passes": 2,
              "tokens_per_s": 35.24343724757891,
              "ttft_s": 0.351306524
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.7987688745000003,
              "format_passes": 2,
              "gpu_energy_j": 1018.2432254437322,
              "semantic_passes": 2,
              "tokens_per_s": 34.34900471887137,
              "ttft_s": 3.2165016175
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.572505612,
              "format_passes": 2,
              "gpu_energy_j": 143.2153512973727,
              "semantic_passes": 2,
              "tokens_per_s": 34.977603123496166,
              "ttft_s": 0.200824622
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7251064414999999,
              "format_passes": 0,
              "gpu_energy_j": 188.06810372666126,
              "semantic_passes": 0,
              "tokens_per_s": 697.4849369244458,
              "ttft_s": 0.7249596475
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.7468476070000003,
              "format_passes": 0,
              "gpu_energy_j": 730.8272775210808,
              "semantic_passes": 0,
              "tokens_per_s": 745.9216115435739,
              "ttft_s": 2.7466134440000003
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.467499817,
              "format_passes": 0,
              "gpu_energy_j": 1472.1095309291436,
              "semantic_passes": 0,
              "tokens_per_s": 749.3884792604513,
              "ttft_s": 5.46717196
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.848520084,
              "format_passes": 0,
              "gpu_energy_j": 225.70070468757962,
              "semantic_passes": 2,
              "tokens_per_s": 35.19701494022931,
              "ttft_s": 0.22336527550000002
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.984502941,
              "format_passes": 0,
              "gpu_energy_j": 266.8512781534746,
              "semantic_passes": 2,
              "tokens_per_s": 35.11007183579041,
              "ttft_s": 0.215472632
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.013913317,
              "format_passes": 0,
              "gpu_energy_j": 273.55077245098096,
              "semantic_passes": 2,
              "tokens_per_s": 35.252461341273666,
              "ttft_s": 0.219644691
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.706094862,
              "format_passes": 0,
              "gpu_energy_j": 461.11388836232027,
              "semantic_passes": 0,
              "tokens_per_s": 35.03648460219128,
              "ttft_s": 1.0282697625
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7799155500000001,
              "format_passes": 0,
              "gpu_energy_j": 468.2576785643049,
              "semantic_passes": 0,
              "tokens_per_s": 35.03894605787595,
              "ttft_s": 1.0939810474999998
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
              "e2e_s": 1.8248084310000001,
              "format_passes": 2,
              "gpu_energy_j": 489.0242414431162,
              "semantic_passes": 2,
              "tokens_per_s": 35.312136783807944,
              "ttft_s": 0.5787296335000001
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.7957868374999997,
              "format_passes": 0,
              "gpu_energy_j": 1075.1854598476677,
              "semantic_passes": 0,
              "tokens_per_s": 35.32437717404182,
              "ttft_s": 0.20303059499999998
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5893450375,
              "format_passes": 2,
              "gpu_energy_j": 149.38944348134305,
              "semantic_passes": 2,
              "tokens_per_s": 34.96833574425027,
              "ttft_s": 0.21753909700000001
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0029796515,
              "format_passes": 0,
              "gpu_energy_j": 252.53103314141887,
              "semantic_passes": 0,
              "tokens_per_s": 35.012385634099644,
              "ttft_s": 0.6030743359999999
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.46551094849999997,
              "format_passes": 2,
              "gpu_energy_j": 110.9609793175403,
              "semantic_passes": 2,
              "tokens_per_s": 34.33608408043216,
              "ttft_s": 0.2033129505
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9938123675,
              "format_passes": 0,
              "gpu_energy_j": 269.7699413841314,
              "semantic_passes": 0,
              "tokens_per_s": 35.33434958116415,
              "ttft_s": 0.2296514235
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.2752293005,
              "format_passes": 0,
              "gpu_energy_j": 318.0339242281326,
              "semantic_passes": 2,
              "tokens_per_s": 35.30038782268908,
              "ttft_s": 0.4819960705
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 14.1371018115,
              "format_passes": 2,
              "gpu_energy_j": 3741.341984114524,
              "semantic_passes": 2,
              "tokens_per_s": 34.59190216249846,
              "ttft_s": 13.558898397
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5725331494999999,
              "format_passes": 2,
              "gpu_energy_j": 142.55537670066136,
              "semantic_passes": 2,
              "tokens_per_s": 34.98278479707628,
              "ttft_s": 0.20088083350000002
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.989634842,
              "format_passes": 0,
              "gpu_energy_j": 781.8272009324352,
              "semantic_passes": 0,
              "tokens_per_s": 168.9785432944576,
              "ttft_s": 2.9895103195
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 12.419346470499999,
              "format_passes": 0,
              "gpu_energy_j": 3314.196738844826,
              "semantic_passes": 0,
              "tokens_per_s": 164.92023869738156,
              "ttft_s": 12.41909274
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 25.062413072,
              "format_passes": 0,
              "gpu_energy_j": 6719.830173815133,
              "semantic_passes": 0,
              "tokens_per_s": 163.44341495897714,
              "ttft_s": 25.062051805000003
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8465258775,
              "format_passes": 0,
              "gpu_energy_j": 225.47728597733465,
              "semantic_passes": 2,
              "tokens_per_s": 35.24643984281728,
              "ttft_s": 0.222304188
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9851802775,
              "format_passes": 0,
              "gpu_energy_j": 263.9922654415725,
              "semantic_passes": 2,
              "tokens_per_s": 35.06447299682704,
              "ttft_s": 0.21514903200000002
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0211614325,
              "format_passes": 0,
              "gpu_energy_j": 275.3881605057495,
              "semantic_passes": 2,
              "tokens_per_s": 35.27138825013107,
              "ttft_s": 0.2273097415
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.6387297535,
              "format_passes": 0,
              "gpu_energy_j": 695.6016686676455,
              "semantic_passes": 0,
              "tokens_per_s": 35.01103379610619,
              "ttft_s": 1.9588164090000002
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.028500335,
              "format_passes": 0,
              "gpu_energy_j": 800.2863078398743,
              "semantic_passes": 0,
              "tokens_per_s": 35.02619504374759,
              "ttft_s": 2.34370653
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
            "e2e_change_pct": 3.386849057925234,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.4737004379831387,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.0821685876812972,
            "ttft_change_pct": 11.301174830964534
          },
          "decode": {
            "e2e_change_pct": 0.3472152582769894,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.614759738436832,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.19022209777105337,
            "ttft_change_pct": 4.501115386449905
          },
          "energy": {
            "e2e_change_pct": 1.4552793090758076,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.4047429492799468,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.13461518869464228,
            "ttft_change_pct": 4.289574470642288
          },
          "filtering": {
            "e2e_change_pct": 8.477913504426727,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.094143997903842,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.007617815042704201,
            "ttft_change_pct": 14.93775746463617
          },
          "german": {
            "e2e_change_pct": -0.09862791203518739,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.68422136264783,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.21367545038706304,
            "ttft_change_pct": 0.033977896777392935
          },
          "ha_sim": {
            "e2e_change_pct": 0.5571781846070101,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.504453142562201,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.11649659297123804,
            "ttft_change_pct": 2.8642075505461717
          },
          "jarvis_memory": {
            "e2e_change_pct": 11.296236147577975,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 6.360255286666305,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.16159199998031504,
            "ttft_change_pct": 37.20100185216031
          },
          "long_context": {
            "e2e_change_pct": 272.149564202185,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 267.4310705562627,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.7071455071699262,
            "ttft_change_pct": 321.5417869908781
          },
          "math": {
            "e2e_change_pct": 0.004809996517529669,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.46082671356996174,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.014814261462725575,
            "ttft_change_pct": 0.027990342737971297
          },
          "prefill": {
            "e2e_change_pct": 312.3028938779605,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 315.71493806772526,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -75.77316235106566,
            "ttft_change_pct": 312.3692028665637
          },
          "prefill2048": {
            "e2e_change_pct": 352.1308877438572,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 353.4856375485011,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -77.89040615727654,
            "ttft_change_pct": 352.1601963002698
          },
          "prefill4096": {
            "e2e_change_pct": 358.3889146932183,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 356.476235812006,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -78.18976145452963,
            "ttft_change_pct": 358.40979556457927
          },
          "pve_sim": {
            "e2e_change_pct": -0.23502172047585868,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.09898892896866851,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.14042356339565298,
            "ttft_change_pct": -0.4750458627128862
          },
          "sorting": {
            "e2e_change_pct": 0.06879984526120264,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.0713880524333863,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.12987395519049594,
            "ttft_change_pct": -0.15018148569326817
          },
          "time": {
            "e2e_change_pct": 0.7148654010626698,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.671680813878095,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.05368960956846358,
            "ttft_change_pct": 3.489749952572252
          },
          "tool-call": {
            "e2e_change_pct": 54.66489069703322,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 50.85246535039873,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.07264086672524872,
            "ttft_change_pct": 90.49635420938485
          },
          "tool-final": {
            "e2e_change_pct": 70.14854075520604,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 70.90724711521683,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.03639097508039146,
            "ttft_change_pct": 114.23648383634367
          }
        }
      },
      "complete": true
    }
  }
}
```

</details>
