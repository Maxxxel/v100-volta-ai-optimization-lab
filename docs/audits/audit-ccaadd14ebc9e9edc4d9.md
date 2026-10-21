# Public audit excerpt

Original SHA256: `ccaadd14ebc9e9edc4d96d603c8d9f869b43bfd9dcf1ab1cc8234acdc03a2a8d`

Original file: `RESULTS.json`; 39765 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.667407638,
              "format_passes": 2,
              "gpu_energy_j": 176.0656887560262,
              "semantic_passes": 2,
              "tokens_per_s": 79.13258113757948,
              "ttft_s": 0.1240615615
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6588727085000001,
              "format_passes": 0,
              "gpu_energy_j": 445.7022736045077,
              "semantic_passes": 0,
              "tokens_per_s": 79.58652743556752,
              "ttft_s": 0.06287089900000001
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2382854095,
              "format_passes": 2,
              "gpu_energy_j": 56.38610944525169,
              "semantic_passes": 2,
              "tokens_per_s": 78.09916221708212,
              "ttft_s": 0.0717836365
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.24143748850000002,
              "format_passes": 0,
              "gpu_energy_j": 59.22697567189129,
              "semantic_passes": 0,
              "tokens_per_s": 77.56147025100061,
              "ttft_s": 0.1253489015
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.182823858,
              "format_passes": 2,
              "gpu_energy_j": 40.736932019106604,
              "semantic_passes": 2,
              "tokens_per_s": 77.23780574104572,
              "ttft_s": 0.0662680165
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.36128417749999997,
              "format_passes": 0,
              "gpu_energy_j": 91.49020436991005,
              "semantic_passes": 0,
              "tokens_per_s": 78.3208991350856,
              "ttft_s": 0.080333398
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4700706045,
              "format_passes": 0,
              "gpu_energy_j": 117.93452347570107,
              "semantic_passes": 2,
              "tokens_per_s": 78.94321335108629,
              "ttft_s": 0.115367418
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0755986444999999,
              "format_passes": 2,
              "gpu_energy_j": 284.97728627955394,
              "semantic_passes": 2,
              "tokens_per_s": 77.96389518682741,
              "ttft_s": 0.8189999434999999
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.233573321,
              "format_passes": 0,
              "gpu_energy_j": 55.6244020458434,
              "semantic_passes": 0,
              "tokens_per_s": 78.2790846303264,
              "ttft_s": 0.06748232000000001
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.1984751985,
              "format_passes": 0,
              "gpu_energy_j": 47.46363713611313,
              "semantic_passes": 0,
              "tokens_per_s": 2565.6686132754658,
              "ttft_s": 0.1983149085
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7126961940000001,
              "format_passes": 0,
              "gpu_energy_j": 187.33260394056828,
              "semantic_passes": 0,
              "tokens_per_s": 2878.4474425081835,
              "ttft_s": 0.7124664599999999
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4066400135000001,
              "format_passes": 0,
              "gpu_energy_j": 379.2250228448539,
              "semantic_passes": 0,
              "tokens_per_s": 2915.5851055475123,
              "ttft_s": 1.406254479
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.29544266500000005,
              "format_passes": 2,
              "gpu_energy_j": 69.79035750820213,
              "semantic_passes": 2,
              "tokens_per_s": 78.6503630109345,
              "ttft_s": 0.07922528100000001
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3532130955,
              "format_passes": 2,
              "gpu_energy_j": 85.16426790124541,
              "semantic_passes": 2,
              "tokens_per_s": 78.80432940910364,
              "ttft_s": 0.07402641400000001
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.369986159,
              "format_passes": 2,
              "gpu_energy_j": 92.44789539690983,
              "semantic_passes": 2,
              "tokens_per_s": 78.80072391539163,
              "ttft_s": 0.078056596
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6194667495,
              "format_passes": 0,
              "gpu_energy_j": 158.49499857806336,
              "semantic_passes": 0,
              "tokens_per_s": 78.93188463824396,
              "ttft_s": 0.3179502245
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.55952426,
              "format_passes": 0,
              "gpu_energy_j": 142.59486315362142,
              "semantic_passes": 0,
              "tokens_per_s": 78.79159966874572,
              "ttft_s": 0.25506719450000004
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
              "e2e_s": 0.6671014854999999,
              "format_passes": 2,
              "gpu_energy_j": 175.8698346036387,
              "semantic_passes": 2,
              "tokens_per_s": 79.19389191275016,
              "ttft_s": 0.12412375
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.658453001,
              "format_passes": 0,
              "gpu_energy_j": 445.33469666698835,
              "semantic_passes": 0,
              "tokens_per_s": 79.6088812220053,
              "ttft_s": 0.06291606250000001
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23798044200000001,
              "format_passes": 2,
              "gpu_energy_j": 58.25945368915119,
              "semantic_passes": 2,
              "tokens_per_s": 78.2032290450405,
              "ttft_s": 0.0717269625
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2419220465,
              "format_passes": 0,
              "gpu_energy_j": 58.51829243289746,
              "semantic_passes": 0,
              "tokens_per_s": 77.59658953808278,
              "ttft_s": 0.1258937115
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.18303688299999998,
              "format_passes": 2,
              "gpu_energy_j": 41.140072996974844,
              "semantic_passes": 2,
              "tokens_per_s": 76.98296058467062,
              "ttft_s": 0.0661093025
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3583535245,
              "format_passes": 0,
              "gpu_energy_j": 86.65252442534305,
              "semantic_passes": 0,
              "tokens_per_s": 78.76015023079803,
              "ttft_s": 0.07894704599999999
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4695891555,
              "format_passes": 0,
              "gpu_energy_j": 113.9503756011855,
              "semantic_passes": 2,
              "tokens_per_s": 79.075383511032,
              "ttft_s": 0.11544301600000001
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0742562260000001,
              "format_passes": 2,
              "gpu_energy_j": 286.89985496683306,
              "semantic_passes": 2,
              "tokens_per_s": 77.91752188070637,
              "ttft_s": 0.8175063455
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.236665441,
              "format_passes": 0,
              "gpu_energy_j": 53.14418632045728,
              "semantic_passes": 0,
              "tokens_per_s": 77.73399514705679,
              "ttft_s": 0.0693806795
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.1982508615,
              "format_passes": 0,
              "gpu_energy_j": 48.0646575140924,
              "semantic_passes": 0,
              "tokens_per_s": 2560.5415529882202,
              "ttft_s": 0.1981210115
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.714066469,
              "format_passes": 0,
              "gpu_energy_j": 188.5560799532264,
              "semantic_passes": 0,
              "tokens_per_s": 2873.1281236201967,
              "ttft_s": 0.7137897705
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4092615355,
              "format_passes": 0,
              "gpu_energy_j": 382.0141232805229,
              "semantic_passes": 0,
              "tokens_per_s": 2910.0161533596984,
              "ttft_s": 1.40892974
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.29530720200000005,
              "format_passes": 2,
              "gpu_energy_j": 73.53883956415288,
              "semantic_passes": 2,
              "tokens_per_s": 78.58001697375585,
              "ttft_s": 0.0788978975
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.353140874,
              "format_passes": 2,
              "gpu_energy_j": 87.15443597475496,
              "semantic_passes": 2,
              "tokens_per_s": 78.81498852338666,
              "ttft_s": 0.073983602
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3689196815,
              "format_passes": 2,
              "gpu_energy_j": 90.22240279450999,
              "semantic_passes": 2,
              "tokens_per_s": 78.95953888852355,
              "ttft_s": 0.0775850135
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6186409355,
              "format_passes": 0,
              "gpu_energy_j": 157.7548958160778,
              "semantic_passes": 0,
              "tokens_per_s": 79.0236542902693,
              "ttft_s": 0.317490975
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5596519424999999,
              "format_passes": 0,
              "gpu_energy_j": 142.33268005429167,
              "semantic_passes": 0,
              "tokens_per_s": 78.84739830248702,
              "ttft_s": 0.2551947325
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
            "e2e_change_pct": -0.04587189036636685,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.11123925040209537,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.07747854839221802,
            "ttft_change_pct": 0.050127129828214656
          },
          "decode": {
            "e2e_change_pct": -0.02530076586645391,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.08247140732459135,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.028087400164400478,
            "ttft_change_pct": 0.07183530173475727
          },
          "energy": {
            "e2e_change_pct": -0.12798412653124425,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.3223505972129974,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.13324960857981072,
            "ttft_change_pct": -0.0789511409052035
          },
          "filtering": {
            "e2e_change_pct": 0.20069708437178146,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.1965548315683527,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.04527929520741214,
            "ttft_change_pct": 0.43463484201335945
          },
          "german": {
            "e2e_change_pct": 0.11651925647471195,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.9896203712129292,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.3299487264429968,
            "ttft_change_pct": -0.23950316967764618
          },
          "ha_sim": {
            "e2e_change_pct": -0.8111766809937193,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -5.287647981424826,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.5608351034821935,
            "ttft_change_pct": -1.7257479884020488
          },
          "jarvis_memory": {
            "e2e_change_pct": -0.10242057158883489,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.378271058462756,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.16742434762302416,
            "ttft_change_pct": 0.06552803322685818
          },
          "long_context": {
            "e2e_change_pct": -0.12480663738877462,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.6746392712130511,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.05948048902625347,
            "ttft_change_pct": -0.18236851074946436
          },
          "math": {
            "e2e_change_pct": 1.3238326991976912,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -4.458862718815427,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.6963411565730437,
            "ttft_change_pct": 2.8131212738388145
          },
          "prefill": {
            "e2e_change_pct": -0.11303024342359524,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.2662754357735118,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.19983330117991915,
            "ttft_change_pct": -0.09777227615743733
          },
          "prefill2048": {
            "e2e_change_pct": 0.19226635578188933,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.6531036172679583,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.18479819396499675,
            "ttft_change_pct": 0.18573653277658142
          },
          "prefill4096": {
            "e2e_change_pct": 0.18636765447024306,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.7354737339708706,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.19100633273293477,
            "ttft_change_pct": 0.19024017629458712
          },
          "pve_sim": {
            "e2e_change_pct": -0.04585085908292985,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 5.371060114587034,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.08944146534819453,
            "ttft_change_pct": -0.4132310998051447
          },
          "sorting": {
            "e2e_change_pct": -0.02044700519888698,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.3368580774008496,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.013526051630585734,
            "ttft_change_pct": -0.05783341065260794
          },
          "time": {
            "e2e_change_pct": -0.2882479449724529,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.4072939603925536,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.20153999257981337,
            "ttft_change_pct": -0.604154580350913
          },
          "tool-call": {
            "e2e_change_pct": -0.1333104643092775,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.46695654034851763,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.11626436191907175,
            "ttft_change_pct": -0.14444069058990872
          },
          "tool-final": {
            "e2e_change_pct": 0.022819832691434172,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.18386573929194405,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.07081799833470459,
            "ttft_change_pct": 0.05000172611377973
          }
        }
      },
      "complete": true
    }
  }
}
```
