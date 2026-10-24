# Public audit excerpt

Original SHA256: `11386ddb4ace54fbdc1d10c2f61481597ff6be44e42bb86be2f7b718d8dade53`

Original file: `RESULTS.json`; 39783 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 1.7664493545,
              "format_passes": 2,
              "gpu_energy_j": 478.81002367351755,
              "semantic_passes": 2,
              "tokens_per_s": 35.41173727660142,
              "ttft_s": 0.5238828225000001
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.7799614525000003,
              "format_passes": 0,
              "gpu_energy_j": 1066.463107360339,
              "semantic_passes": 0,
              "tokens_per_s": 35.425836072459745,
              "ttft_s": 0.194570499
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5799136865000001,
              "format_passes": 2,
              "gpu_energy_j": 147.0869545641275,
              "semantic_passes": 2,
              "tokens_per_s": 34.89743618490772,
              "ttft_s": 0.207417449
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.924460227,
              "format_passes": 0,
              "gpu_energy_j": 245.49645753815608,
              "semantic_passes": 0,
              "tokens_per_s": 34.98041413420579,
              "ttft_s": 0.5242127735
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4645912715,
              "format_passes": 2,
              "gpu_energy_j": 107.84221748606484,
              "semantic_passes": 2,
              "tokens_per_s": 34.14743385437499,
              "ttft_s": 0.2009888915
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9876760005,
              "format_passes": 0,
              "gpu_energy_j": 265.3004135647095,
              "semantic_passes": 0,
              "tokens_per_s": 35.31249229269828,
              "ttft_s": 0.22303871949999998
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1438258664999998,
              "format_passes": 0,
              "gpu_energy_j": 295.5724625073264,
              "semantic_passes": 2,
              "tokens_per_s": 35.30259461478548,
              "ttft_s": 0.3506400875
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.7933333840000003,
              "format_passes": 2,
              "gpu_energy_j": 1011.814532505346,
              "semantic_passes": 2,
              "tokens_per_s": 34.4210369854012,
              "ttft_s": 3.2122273385
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.573374975,
              "format_passes": 2,
              "gpu_energy_j": 142.20653797749105,
              "semantic_passes": 2,
              "tokens_per_s": 34.957158429548244,
              "ttft_s": 0.20141876250000001
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7253469995,
              "format_passes": 0,
              "gpu_energy_j": 189.27292032940994,
              "semantic_passes": 0,
              "tokens_per_s": 697.1810599892076,
              "ttft_s": 0.725218564
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.749629467,
              "format_passes": 0,
              "gpu_energy_j": 738.3584579770943,
              "semantic_passes": 0,
              "tokens_per_s": 745.1745817848555,
              "ttft_s": 2.7493663935
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.462800808,
              "format_passes": 0,
              "gpu_energy_j": 1480.0437357288051,
              "semantic_passes": 0,
              "tokens_per_s": 750.0343611852032,
              "ttft_s": 5.462445078
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8453099589999999,
              "format_passes": 0,
              "gpu_energy_j": 223.92836973509893,
              "semantic_passes": 2,
              "tokens_per_s": 35.228626255821666,
              "ttft_s": 0.22080840899999998
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.983314337,
              "format_passes": 0,
              "gpu_energy_j": 259.074533602762,
              "semantic_passes": 2,
              "tokens_per_s": 35.08675220916338,
              "ttft_s": 0.2137182365
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0187996395,
              "format_passes": 0,
              "gpu_energy_j": 274.6417948955526,
              "semantic_passes": 2,
              "tokens_per_s": 35.25649715932927,
              "ttft_s": 0.224545835
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7057964165000001,
              "format_passes": 0,
              "gpu_energy_j": 463.55831310673943,
              "semantic_passes": 0,
              "tokens_per_s": 35.0123680821279,
              "ttft_s": 1.026728881
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.777143165,
              "format_passes": 0,
              "gpu_energy_j": 466.2693216838167,
              "semantic_passes": 0,
              "tokens_per_s": 35.11618702815993,
              "ttft_s": 1.0937614245
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
              "e2e_s": 1.7647750725,
              "format_passes": 2,
              "gpu_energy_j": 482.74322498210995,
              "semantic_passes": 2,
              "tokens_per_s": 35.35376766949727,
              "ttft_s": 0.5201639805
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.7828055065,
              "format_passes": 0,
              "gpu_energy_j": 1066.322243988504,
              "semantic_passes": 0,
              "tokens_per_s": 35.38418331821178,
              "ttft_s": 0.193564291
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5813142755,
              "format_passes": 2,
              "gpu_energy_j": 148.07712600797936,
              "semantic_passes": 2,
              "tokens_per_s": 34.91959644249869,
              "ttft_s": 0.20897886
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.928699323,
              "format_passes": 0,
              "gpu_energy_j": 247.08966548995457,
              "semantic_passes": 0,
              "tokens_per_s": 34.9670093345586,
              "ttft_s": 0.5282683930000001
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4675050865,
              "format_passes": 2,
              "gpu_energy_j": 108.8036012949116,
              "semantic_passes": 2,
              "tokens_per_s": 34.230825279720634,
              "ttft_s": 0.2045280645
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.994188497,
              "format_passes": 0,
              "gpu_energy_j": 268.34639819064034,
              "semantic_passes": 0,
              "tokens_per_s": 35.28427147624648,
              "ttft_s": 0.2289256495
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1462340995,
              "format_passes": 0,
              "gpu_energy_j": 299.7000545142673,
              "semantic_passes": 2,
              "tokens_per_s": 35.26415140853682,
              "ttft_s": 0.35219494549999997
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.7982866885,
              "format_passes": 2,
              "gpu_energy_j": 1019.2164178832002,
              "semantic_passes": 2,
              "tokens_per_s": 34.29412193497637,
              "ttft_s": 3.215067794
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.573409183,
              "format_passes": 2,
              "gpu_energy_j": 146.67525346423486,
              "semantic_passes": 2,
              "tokens_per_s": 34.84356163463531,
              "ttft_s": 0.2002933895
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.725920311,
              "format_passes": 0,
              "gpu_energy_j": 188.04224657968774,
              "semantic_passes": 0,
              "tokens_per_s": 696.6271537139694,
              "ttft_s": 0.7257845545
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.7450637865000003,
              "format_passes": 0,
              "gpu_energy_j": 734.566879316731,
              "semantic_passes": 0,
              "tokens_per_s": 746.4110704785585,
              "ttft_s": 2.7448409555
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.465454995,
              "format_passes": 0,
              "gpu_energy_j": 1474.1706238022512,
              "semantic_passes": 0,
              "tokens_per_s": 749.6814968930976,
              "ttft_s": 5.4650185355000005
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.848380793,
              "format_passes": 0,
              "gpu_energy_j": 228.1148700669064,
              "semantic_passes": 2,
              "tokens_per_s": 35.16157881073096,
              "ttft_s": 0.22262857549999998
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9858290885000001,
              "format_passes": 0,
              "gpu_energy_j": 261.3453651333849,
              "semantic_passes": 2,
              "tokens_per_s": 35.092165825190285,
              "ttft_s": 0.216346759
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0145699635,
              "format_passes": 0,
              "gpu_energy_j": 274.6267420493805,
              "semantic_passes": 2,
              "tokens_per_s": 35.234836088487356,
              "ttft_s": 0.21990321699999998
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7063304425,
              "format_passes": 0,
              "gpu_energy_j": 460.40906665367527,
              "semantic_passes": 0,
              "tokens_per_s": 35.03921242774605,
              "ttft_s": 1.02816492
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7791720325,
              "format_passes": 0,
              "gpu_energy_j": 466.9235161580392,
              "semantic_passes": 0,
              "tokens_per_s": 35.101523921791355,
              "ttft_s": 1.0956543485
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
            "e2e_change_pct": -0.09478233812562076,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.8214534187100275,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.1637016751009579,
            "ttft_change_pct": -0.7098614118045576
          },
          "decode": {
            "e2e_change_pct": 0.07524029109129415,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.01320846177077506,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.11757733582565821,
            "ttft_change_pct": -0.5171431461457154
          },
          "energy": {
            "e2e_change_pct": 0.2415168037252391,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.6731878070261876,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.06350110499107053,
            "ttft_change_pct": 0.7527867146799094
          },
          "filtering": {
            "e2e_change_pct": 0.45854822913868887,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.6489739069049039,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.038320871776309495,
            "ttft_change_pct": 0.7736590378982999
          },
          "german": {
            "e2e_change_pct": 0.6271781625583062,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.8914725895459163,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.2442099330253411,
            "ttft_change_pct": 1.7608799041513246
          },
          "ha_sim": {
            "e2e_change_pct": 0.6593757969924452,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.1481266029718773,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.07991737376643604,
            "ttft_change_pct": 2.639420641042567
          },
          "jarvis_memory": {
            "e2e_change_pct": 0.21054192517686587,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.3964738027104184,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.10889626291818999,
            "ttft_change_pct": 0.4434341809248954
          },
          "long_context": {
            "e2e_change_pct": 0.13057920300105774,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.73154566771505,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.36871361684618353,
            "ttft_change_pct": 0.08842635345125416
          },
          "math": {
            "e2e_change_pct": 0.005966078306784972,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.1424121213408096,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.32496003684588937,
            "ttft_change_pct": -0.558723023630936
          },
          "prefill": {
            "e2e_change_pct": 0.07903961833373163,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.6502112122433235,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.07944941522748383,
            "ttft_change_pct": 0.07804412739771394
          },
          "prefill2048": {
            "e2e_change_pct": -0.16604711852252763,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.5135146241503352,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.1659327523949372,
            "ttft_change_pct": -0.16459930588731408
          },
          "prefill4096": {
            "e2e_change_pct": 0.048586560141705704,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.39682016043005586,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.04704641685323585,
            "ttft_change_pct": 0.047111823794177
          },
          "pve_sim": {
            "e2e_change_pct": 0.36327905134736493,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.8695712100972317,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.1903209185729393,
            "ttft_change_pct": 0.824319376351279
          },
          "sorting": {
            "e2e_change_pct": 0.2557423811873072,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.8765166915652101,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.015429230937735738,
            "ttft_change_pct": 1.2299008933662092
          },
          "time": {
            "e2e_change_pct": -0.41516269107395587,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.005480901469434585,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.06143852222194601,
            "ttft_change_pct": -2.067559168933153
          },
          "tool-call": {
            "e2e_change_pct": 0.03130654952925305,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.6793636019507665,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.07667103680386589,
            "ttft_change_pct": 0.13986545295203712
          },
          "tool-final": {
            "e2e_change_pct": 0.11416455015880178,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.14030399252089598,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.04175597526239194,
            "ttft_change_pct": 0.1730655294289063
          }
        }
      },
      "complete": true
    }
  }
}
```

</details>
