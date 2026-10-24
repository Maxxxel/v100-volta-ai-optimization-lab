# Public audit excerpt

Original SHA256: `f979a1f3796d6ec1ce3ebdfaad0c8c59955a9c4e7162f22525a067df59ffc01d`

Original file: `RESULTS.json`; 39496 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.5271951815,
              "format_passes": 2,
              "gpu_energy_j": 132.76634021799083,
              "semantic_passes": 2,
              "tokens_per_s": 96.40712068861089,
              "ttft_s": 0.132982294
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.3678393765,
              "format_passes": 0,
              "gpu_energy_j": 376.50744269376025,
              "semantic_passes": 0,
              "tokens_per_s": 97.12448921666939,
              "ttft_s": 0.0600595305
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.204125598,
              "format_passes": 2,
              "gpu_energy_j": 47.89230288545572,
              "semantic_passes": 2,
              "tokens_per_s": 95.2618253044761,
              "ttft_s": 0.067607137
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.229753754,
              "format_passes": 0,
              "gpu_energy_j": 55.90788179824579,
              "semantic_passes": 0,
              "tokens_per_s": 93.69228517503953,
              "ttft_s": 0.1337020865
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1563919835,
              "format_passes": 2,
              "gpu_energy_j": 31.95561540600844,
              "semantic_passes": 2,
              "tokens_per_s": 93.79560037836843,
              "ttft_s": 0.0604171125
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3055132575,
              "format_passes": 0,
              "gpu_energy_j": 74.07971448632092,
              "semantic_passes": 0,
              "tokens_per_s": 96.0193457102595,
              "ttft_s": 0.0763503395
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.399041679,
              "format_passes": 0,
              "gpu_energy_j": 96.94198634191322,
              "semantic_passes": 2,
              "tokens_per_s": 96.22786898272147,
              "ttft_s": 0.10806963650000001
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.2741795495,
              "format_passes": 2,
              "gpu_energy_j": 342.45152338917455,
              "semantic_passes": 2,
              "tokens_per_s": 94.47755756070097,
              "ttft_s": 1.1153696764999999
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.14834442450000002,
              "format_passes": 0,
              "gpu_energy_j": 33.046736720352186,
              "semantic_passes": 0,
              "tokens_per_s": 93.7317146582424,
              "ttft_s": 0.0629642175
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.2762535215,
              "format_passes": 0,
              "gpu_energy_j": 68.26916944533717,
              "semantic_passes": 0,
              "tokens_per_s": 1835.177415448062,
              "ttft_s": 0.276101221
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.9988311755,
              "format_passes": 0,
              "gpu_energy_j": 268.3854798274335,
              "semantic_passes": 0,
              "tokens_per_s": 2052.9990552205245,
              "ttft_s": 0.9985924724999999
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.9843388965,
              "format_passes": 0,
              "gpu_energy_j": 546.0488555131494,
              "semantic_passes": 0,
              "tokens_per_s": 2066.0188359684616,
              "ttft_s": 1.9840016409999999
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.254485732,
              "format_passes": 2,
              "gpu_energy_j": 57.414806345760326,
              "semantic_passes": 2,
              "tokens_per_s": 95.36914580319048,
              "ttft_s": 0.076210028
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35118994000000003,
              "format_passes": 0,
              "gpu_energy_j": 86.06977168645922,
              "semantic_passes": 2,
              "tokens_per_s": 96.1986188609182,
              "ttft_s": 0.07047953900000001
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.315065172,
              "format_passes": 0,
              "gpu_energy_j": 74.5735028931337,
              "semantic_passes": 0,
              "tokens_per_s": 95.85782035135276,
              "ttft_s": 0.0750912985
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.587823124,
              "format_passes": 0,
              "gpu_energy_j": 151.00035745970752,
              "semantic_passes": 0,
              "tokens_per_s": 96.27685789725373,
              "ttft_s": 0.3407153465
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.621851604,
              "format_passes": 0,
              "gpu_energy_j": 158.95090286625623,
              "semantic_passes": 0,
              "tokens_per_s": 95.90295393794341,
              "ttft_s": 0.371669691
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
              "e2e_s": 0.5263267365,
              "format_passes": 2,
              "gpu_energy_j": 133.16661083999628,
              "semantic_passes": 2,
              "tokens_per_s": 96.42903375735305,
              "ttft_s": 0.1322194785
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.3672840815,
              "format_passes": 0,
              "gpu_energy_j": 375.33949535429997,
              "semantic_passes": 0,
              "tokens_per_s": 97.1566041486992,
              "ttft_s": 0.059946889
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2049105205,
              "format_passes": 2,
              "gpu_energy_j": 43.041667583375876,
              "semantic_passes": 2,
              "tokens_per_s": 95.19579691866656,
              "ttft_s": 0.0683256425
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.229733132,
              "format_passes": 0,
              "gpu_energy_j": 54.05898182125925,
              "semantic_passes": 0,
              "tokens_per_s": 93.8380520978629,
              "ttft_s": 0.1338041875
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1568752465,
              "format_passes": 2,
              "gpu_energy_j": 35.36951815925252,
              "semantic_passes": 2,
              "tokens_per_s": 93.94239565519825,
              "ttft_s": 0.061035833
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3055039725,
              "format_passes": 0,
              "gpu_energy_j": 73.03811928872378,
              "semantic_passes": 0,
              "tokens_per_s": 95.8672472555684,
              "ttft_s": 0.0759982985
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3990310385,
              "format_passes": 0,
              "gpu_energy_j": 92.94660945212755,
              "semantic_passes": 2,
              "tokens_per_s": 96.30714304342496,
              "ttft_s": 0.1082462805
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.2739905710000001,
              "format_passes": 2,
              "gpu_energy_j": 338.45168642969315,
              "semantic_passes": 2,
              "tokens_per_s": 94.55508722459948,
              "ttft_s": 1.1153542425
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1492330705,
              "format_passes": 0,
              "gpu_energy_j": 32.33331734153816,
              "semantic_passes": 0,
              "tokens_per_s": 92.98154030359308,
              "ttft_s": 0.063133534
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.276386042,
              "format_passes": 0,
              "gpu_energy_j": 68.19048504238351,
              "semantic_passes": 0,
              "tokens_per_s": 1834.2672912593516,
              "ttft_s": 0.27625691750000003
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.9971664425,
              "format_passes": 0,
              "gpu_energy_j": 268.21686751451995,
              "semantic_passes": 0,
              "tokens_per_s": 2056.3798397737664,
              "ttft_s": 0.996890957
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.9818483255000001,
              "format_passes": 0,
              "gpu_energy_j": 547.8140727232841,
              "semantic_passes": 0,
              "tokens_per_s": 2068.575623447069,
              "ttft_s": 1.9814877284999999
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.254917381,
              "format_passes": 2,
              "gpu_energy_j": 57.98583633592261,
              "semantic_passes": 2,
              "tokens_per_s": 95.20392191981867,
              "ttft_s": 0.0762498675
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3517619075,
              "format_passes": 0,
              "gpu_energy_j": 85.51648016315255,
              "semantic_passes": 2,
              "tokens_per_s": 96.0958528768852,
              "ttft_s": 0.070798825
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.315919635,
              "format_passes": 0,
              "gpu_energy_j": 76.73004085534971,
              "semantic_passes": 0,
              "tokens_per_s": 95.30820524599125,
              "ttft_s": 0.074596917
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.587809322,
              "format_passes": 0,
              "gpu_energy_j": 151.87253939052215,
              "semantic_passes": 0,
              "tokens_per_s": 96.32633520566802,
              "ttft_s": 0.3408720825
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6214066460000001,
              "format_passes": 0,
              "gpu_energy_j": 161.3030732390193,
              "semantic_passes": 0,
              "tokens_per_s": 95.9648768738664,
              "ttft_s": 0.371380207
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
            "e2e_change_pct": -0.16472931287594417,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.3014850159673399,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.02272972015515684,
            "ttft_change_pct": -0.5736218537484516
          },
          "decode": {
            "e2e_change_pct": -0.04059650639836043,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.3102056445694945,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.03306574097721171,
            "ttft_change_pct": -0.18754975115896633
          },
          "energy": {
            "e2e_change_pct": 0.38452918580060835,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -10.12821478574779,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.06931253479397492,
            "ttft_change_pct": 1.062765755041517
          },
          "filtering": {
            "e2e_change_pct": -0.008975696649549114,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.3070470880271263,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.15558049689048392,
            "ttft_change_pct": 0.0763645524709089
          },
          "german": {
            "e2e_change_pct": 0.309007526591043,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 10.683263989346248,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.15650550370982508,
            "ttft_change_pct": 1.0240815464327202
          },
          "ha_sim": {
            "e2e_change_pct": -0.0030391479819869005,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.4060464525541327,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.15840396908145538,
            "ttft_change_pct": -0.4610863583651703
          },
          "jarvis_memory": {
            "e2e_change_pct": -0.0026665134395642553,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -4.121410175869544,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.08238160269111727,
            "ttft_change_pct": 0.16345386708134235
          },
          "long_context": {
            "e2e_change_pct": -0.014831386995173279,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.1680009245968015,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.08206146083813426,
            "ttft_change_pct": -0.001383756464334862
          },
          "math": {
            "e2e_change_pct": 0.599042399466776,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.1588194466858113,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.8003420799294503,
            "ttft_change_pct": 0.26890908316299367
          },
          "prefill": {
            "e2e_change_pct": 0.04797061021355464,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.11525613039229388,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.04959325354862987,
            "ttft_change_pct": 0.056391094337104875
          },
          "prefill2048": {
            "e2e_change_pct": -0.16666810576538849,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.06282467778137013,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.16467540716325058,
            "ttft_change_pct": -0.17039138055389147
          },
          "prefill4096": {
            "e2e_change_pct": -0.12551137330386597,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.3232709293888636,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.1237543159866128,
            "ttft_change_pct": -0.12670919459184526
          },
          "pve_sim": {
            "e2e_change_pct": 0.1696161889343184,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.9945692174305298,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.17324668474306693,
            "ttft_change_pct": 0.052275928831835294
          },
          "sorting": {
            "e2e_change_pct": 0.16286557069373764,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.6428407005914183,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.1068268809363837,
            "ttft_change_pct": 0.4530194217076122
          },
          "time": {
            "e2e_change_pct": 0.2712019848388536,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.8918287039652713,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.5733649099749827,
            "ttft_change_pct": -0.6583738860235555
          },
          "tool-call": {
            "e2e_change_pct": -0.002347985207873382,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.5776025603431822,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.05139065554786715,
            "ttft_change_pct": 0.04600203706996986
          },
          "tool-final": {
            "e2e_change_pct": -0.07155372714933161,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.4798093816065006,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.06456833015076047,
            "ttft_change_pct": -0.07788743796168784
          }
        }
      },
      "complete": true
    }
  }
}
```

</details>
