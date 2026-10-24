# Public audit excerpt

Original SHA256: `a8cddc0f5be2ee2e67d61d3e26cce530295fc59318284d24c72e19acc2f7d993`

Original file: `RESULTS.json`; 39459 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.5269934475,
              "format_passes": 2,
              "gpu_energy_j": 131.20989210290443,
              "semantic_passes": 2,
              "tokens_per_s": 96.45209602236147,
              "ttft_s": 0.13297514900000001
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.3669281175,
              "format_passes": 0,
              "gpu_energy_j": 355.3704241213698,
              "semantic_passes": 0,
              "tokens_per_s": 97.00799110588883,
              "ttft_s": 0.0575269145
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2049523345,
              "format_passes": 2,
              "gpu_energy_j": 46.16176475237462,
              "semantic_passes": 2,
              "tokens_per_s": 94.7088041648745,
              "ttft_s": 0.067663319
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.229594939,
              "format_passes": 0,
              "gpu_energy_j": 53.46303739932145,
              "semantic_passes": 0,
              "tokens_per_s": 93.99134348322582,
              "ttft_s": 0.133826947
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.157321148,
              "format_passes": 2,
              "gpu_energy_j": 32.53942048818202,
              "semantic_passes": 2,
              "tokens_per_s": 93.48355292751052,
              "ttft_s": 0.0610330905
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.30749010649999997,
              "format_passes": 0,
              "gpu_energy_j": 70.83181327591947,
              "semantic_passes": 0,
              "tokens_per_s": 95.79691367791288,
              "ttft_s": 0.07781261
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4040124075,
              "format_passes": 0,
              "gpu_energy_j": 91.35650354408618,
              "semantic_passes": 2,
              "tokens_per_s": 94.91394040036819,
              "ttft_s": 0.10888872150000001
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.028579794,
              "format_passes": 2,
              "gpu_energy_j": 276.0038657917404,
              "semantic_passes": 2,
              "tokens_per_s": 93.82887138189184,
              "ttft_s": 0.8687057060000001
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.149317963,
              "format_passes": 0,
              "gpu_energy_j": 32.06412047325399,
              "semantic_passes": 0,
              "tokens_per_s": 93.35668925193289,
              "ttft_s": 0.06363614749999999
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.2052701675,
              "format_passes": 0,
              "gpu_energy_j": 49.27275421554122,
              "semantic_passes": 0,
              "tokens_per_s": 2472.7027343530444,
              "ttft_s": 0.2051398525
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.755498513,
              "format_passes": 0,
              "gpu_energy_j": 198.55002677114774,
              "semantic_passes": 0,
              "tokens_per_s": 2715.1201264230085,
              "ttft_s": 0.7552949855
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4982689965,
              "format_passes": 0,
              "gpu_energy_j": 403.40371205422633,
              "semantic_passes": 0,
              "tokens_per_s": 2736.9845439337632,
              "ttft_s": 1.4979177305
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.254274778,
              "format_passes": 2,
              "gpu_energy_j": 59.45504651238983,
              "semantic_passes": 2,
              "tokens_per_s": 95.40141329881806,
              "ttft_s": 0.0760592775
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35130885599999995,
              "format_passes": 0,
              "gpu_energy_j": 85.1356740593267,
              "semantic_passes": 2,
              "tokens_per_s": 95.88426724598105,
              "ttft_s": 0.0697244335
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.314569769,
              "format_passes": 0,
              "gpu_energy_j": 74.84099586472877,
              "semantic_passes": 0,
              "tokens_per_s": 95.89911907153657,
              "ttft_s": 0.0746902585
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5506182245,
              "format_passes": 0,
              "gpu_energy_j": 136.1323355808587,
              "semantic_passes": 0,
              "tokens_per_s": 96.19676990795719,
              "ttft_s": 0.3035311265
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.524351146,
              "format_passes": 0,
              "gpu_energy_j": 136.10664666097978,
              "semantic_passes": 0,
              "tokens_per_s": 95.72642722266826,
              "ttft_s": 0.2738784575
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
              "e2e_s": 0.5269640959999999,
              "format_passes": 2,
              "gpu_energy_j": 133.9142046105561,
              "semantic_passes": 2,
              "tokens_per_s": 96.22630108712207,
              "ttft_s": 0.132070739
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.3674581419999998,
              "format_passes": 0,
              "gpu_energy_j": 357.1185025355005,
              "semantic_passes": 0,
              "tokens_per_s": 96.97095630092363,
              "ttft_s": 0.057693839999999996
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.205176853,
              "format_passes": 2,
              "gpu_energy_j": 45.925001318386045,
              "semantic_passes": 2,
              "tokens_per_s": 94.72135880189728,
              "ttft_s": 0.067933536
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2298703835,
              "format_passes": 0,
              "gpu_energy_j": 55.21922568090048,
              "semantic_passes": 0,
              "tokens_per_s": 94.05275689348579,
              "ttft_s": 0.13412636649999998
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.157557349,
              "format_passes": 2,
              "gpu_energy_j": 33.60153754554531,
              "semantic_passes": 2,
              "tokens_per_s": 92.87641073348595,
              "ttft_s": 0.06062665
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.307335653,
              "format_passes": 0,
              "gpu_energy_j": 73.03140608752909,
              "semantic_passes": 0,
              "tokens_per_s": 95.83594740770602,
              "ttft_s": 0.077743369
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.398818309,
              "format_passes": 0,
              "gpu_energy_j": 95.52342860831214,
              "semantic_passes": 2,
              "tokens_per_s": 95.9948689892194,
              "ttft_s": 0.10716033650000001
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.911761632,
              "format_passes": 2,
              "gpu_energy_j": 237.24331060913892,
              "semantic_passes": 2,
              "tokens_per_s": 92.93215317243653,
              "ttft_s": 0.750303003
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.148372631,
              "format_passes": 0,
              "gpu_energy_j": 30.31653669047541,
              "semantic_passes": 0,
              "tokens_per_s": 93.7426921211057,
              "ttft_s": 0.063026206
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.20652778900000002,
              "format_passes": 0,
              "gpu_energy_j": 48.689793676883966,
              "semantic_passes": 0,
              "tokens_per_s": 2457.655594212477,
              "ttft_s": 0.206395059
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6341320055,
              "format_passes": 0,
              "gpu_energy_j": 167.75047288962494,
              "semantic_passes": 0,
              "tokens_per_s": 3236.095587733317,
              "ttft_s": 0.63388366
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.2550967125,
              "format_passes": 0,
              "gpu_energy_j": 335.2349072153745,
              "semantic_passes": 0,
              "tokens_per_s": 3267.8109152371617,
              "ttft_s": 1.2547768179999998
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2544667275,
              "format_passes": 2,
              "gpu_energy_j": 59.23178169740813,
              "semantic_passes": 2,
              "tokens_per_s": 95.3759801757156,
              "ttft_s": 0.0762512535
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.351344892,
              "format_passes": 0,
              "gpu_energy_j": 84.55903441360311,
              "semantic_passes": 2,
              "tokens_per_s": 96.12461937648523,
              "ttft_s": 0.0703979965
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.314830254,
              "format_passes": 0,
              "gpu_energy_j": 73.39397963551541,
              "semantic_passes": 0,
              "tokens_per_s": 95.87188606730805,
              "ttft_s": 0.0748811975
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.550835238,
              "format_passes": 0,
              "gpu_energy_j": 136.82169751276757,
              "semantic_passes": 0,
              "tokens_per_s": 95.94375952254049,
              "ttft_s": 0.30388426
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5238121735,
              "format_passes": 0,
              "gpu_energy_j": 133.65290194757486,
              "semantic_passes": 0,
              "tokens_per_s": 95.8055151259312,
              "ttft_s": 0.27331762449999997
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
            "e2e_change_pct": -0.005569613842315579,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.0610584036840462,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.23410059972885922,
            "ttft_change_pct": -0.680134601691651
          },
          "decode": {
            "e2e_change_pct": 0.03877486264376451,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.4919031791834394,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.03817706618084449,
            "ttft_change_pct": 0.2901693954053375
          },
          "energy": {
            "e2e_change_pct": 0.1095466907208964,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.512899442338588,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.013256040062481489,
            "ttft_change_pct": 0.39935522524399136
          },
          "filtering": {
            "e2e_change_pct": 0.11996976118013869,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.284864397923859,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.0653394323179679,
            "ttft_change_pct": 0.2237363301727191
          },
          "german": {
            "e2e_change_pct": 0.1501393824052233,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.2640933410262862,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.6494641838178272,
            "ttft_change_pct": -0.6659346539235167
          },
          "ha_sim": {
            "e2e_change_pct": -0.0502303965997597,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.1053741389356793,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.04074633335722222,
            "ttft_change_pct": -0.08898429187762513
          },
          "jarvis_memory": {
            "e2e_change_pct": -1.2856284617942193,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.561169596661641,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 1.1388512417581653,
            "ttft_change_pct": -1.5872947869995824
          },
          "long_context": {
            "e2e_change_pct": -11.357228936581665,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -14.043482714060385,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.9556954019041664,
            "ttft_change_pct": -13.629783041853315
          },
          "math": {
            "e2e_change_pct": -0.6330999840923335,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -5.450278245543383,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.4134710348726589,
            "ttft_change_pct": -0.9584827554181996
          },
          "prefill": {
            "e2e_change_pct": 0.6126664752685196,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.183129597560395,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.6085300886159439,
            "ttft_change_pct": 0.6118784257193477
          },
          "prefill2048": {
            "e2e_change_pct": -16.064427052022534,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -15.512238594166949,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 19.18793412638651,
            "ttft_change_pct": -16.074689734584503
          },
          "prefill4096": {
            "e2e_change_pct": -16.230215306334006,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -16.898407922852343,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 19.394569563058695,
            "ttft_change_pct": -16.23192699767567
          },
          "pve_sim": {
            "e2e_change_pct": 0.075489005047924,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.37551869534769855,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.02665906323924272,
            "ttft_change_pct": 0.2524031338583477
          },
          "sorting": {
            "e2e_change_pct": 0.010257640644306676,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.6773184708935953,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.250668996497172,
            "ttft_change_pct": 0.9660358158377846
          },
          "time": {
            "e2e_change_pct": 0.08280674930336573,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.933454001372148,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.028397554109127476,
            "ttft_change_pct": 0.25564110211240276
          },
          "tool-call": {
            "e2e_change_pct": 0.039412698371377175,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.5063910267663063,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.2630133898038234,
            "ttft_change_pct": 0.11634177491841591
          },
          "tool-final": {
            "e2e_change_pct": -0.10278846610931591,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.8028103502665926,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.0826186723536182,
            "ttft_change_pct": -0.20477441165668298
          }
        }
      },
      "complete": true
    }
  }
}
```

</details>
