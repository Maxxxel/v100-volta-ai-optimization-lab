# Public audit excerpt

Original SHA256: `fbae23f7521dec8fa494bf55dfe8e3fd05176a702378753e093ca0d697172863`

Original file: `RESULTS.json`; 42842 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{}
```

## Selected aggregate measurements

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
              "e2e_s": 0.5298765165,
              "format_passes": 2,
              "gpu_energy_j": 131.92676989287702,
              "semantic_passes": 2,
              "tokens_per_s": 95.89320128939642,
              "ttft_s": 0.1335548905
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.3662462875,
              "format_passes": 0,
              "gpu_energy_j": 355.8487782220951,
              "semantic_passes": 0,
              "tokens_per_s": 97.0645984105384,
              "ttft_s": 0.057742301499999996
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.205847267,
              "format_passes": 2,
              "gpu_energy_j": 45.14731380881487,
              "semantic_passes": 2,
              "tokens_per_s": 94.86246822156582,
              "ttft_s": 0.068780808
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2300707905,
              "format_passes": 0,
              "gpu_energy_j": 53.977978148425535,
              "semantic_passes": 0,
              "tokens_per_s": 93.89328508822302,
              "ttft_s": 0.13418688
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.157961409,
              "format_passes": 2,
              "gpu_energy_j": 31.141160022160733,
              "semantic_passes": 2,
              "tokens_per_s": 93.7622027924452,
              "ttft_s": 0.061941408
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.30719825700000003,
              "format_passes": 0,
              "gpu_energy_j": 73.051425072851,
              "semantic_passes": 0,
              "tokens_per_s": 95.98965259387714,
              "ttft_s": 0.07789289699999999
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.398770332,
              "format_passes": 0,
              "gpu_energy_j": 95.90353910943182,
              "semantic_passes": 2,
              "tokens_per_s": 96.17449004912599,
              "ttft_s": 0.10754984149999999
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.033571148,
              "format_passes": 2,
              "gpu_energy_j": 270.863155684097,
              "semantic_passes": 2,
              "tokens_per_s": 93.76640030607231,
              "ttft_s": 0.8735832484999999
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.149792484,
              "format_passes": 0,
              "gpu_energy_j": 32.96834203898936,
              "semantic_passes": 0,
              "tokens_per_s": 92.65353428273515,
              "ttft_s": 0.063423195
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.2060254795,
              "format_passes": 0,
              "gpu_energy_j": 49.644964747302936,
              "semantic_passes": 0,
              "tokens_per_s": 2464.3843908495965,
              "ttft_s": 0.205827811
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.756025655,
              "format_passes": 0,
              "gpu_energy_j": 198.76058333973998,
              "semantic_passes": 0,
              "tokens_per_s": 2713.587470620759,
              "ttft_s": 0.7556883705
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4991364919999999,
              "format_passes": 0,
              "gpu_energy_j": 404.39845495358315,
              "semantic_passes": 0,
              "tokens_per_s": 2735.2959862764465,
              "ttft_s": 1.498825805
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.25447138049999996,
              "format_passes": 2,
              "gpu_energy_j": 56.35396480915496,
              "semantic_passes": 2,
              "tokens_per_s": 95.50160172025002,
              "ttft_s": 0.07642502200000001
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3511198165,
              "format_passes": 0,
              "gpu_energy_j": 83.78705658487625,
              "semantic_passes": 2,
              "tokens_per_s": 96.17646676584548,
              "ttft_s": 0.070346324
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3152540065,
              "format_passes": 0,
              "gpu_energy_j": 75.00759484737951,
              "semantic_passes": 0,
              "tokens_per_s": 95.77831228161958,
              "ttft_s": 0.075111073
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5521332865,
              "format_passes": 0,
              "gpu_energy_j": 137.55030534462074,
              "semantic_passes": 0,
              "tokens_per_s": 95.99167371982034,
              "ttft_s": 0.3047832145
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5259439275,
              "format_passes": 0,
              "gpu_energy_j": 130.753643631717,
              "semantic_passes": 0,
              "tokens_per_s": 95.6869639182598,
              "ttft_s": 0.27498714700000004
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
              "e2e_s": 0.526893752,
              "format_passes": 2,
              "gpu_energy_j": 131.86473591919395,
              "semantic_passes": 2,
              "tokens_per_s": 96.35050352706875,
              "ttft_s": 0.1325035245
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.3678788355,
              "format_passes": 0,
              "gpu_energy_j": 358.3408334162334,
              "semantic_passes": 0,
              "tokens_per_s": 96.97658343753852,
              "ttft_s": 0.0579018465
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2049472235,
              "format_passes": 2,
              "gpu_energy_j": 46.95182681659246,
              "semantic_passes": 2,
              "tokens_per_s": 94.8542007453639,
              "ttft_s": 0.0678628845
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2303555435,
              "format_passes": 0,
              "gpu_energy_j": 54.80381770748199,
              "semantic_passes": 0,
              "tokens_per_s": 93.73795703905877,
              "ttft_s": 0.1343440505
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1581775405,
              "format_passes": 2,
              "gpu_energy_j": 32.84690640604909,
              "semantic_passes": 2,
              "tokens_per_s": 92.71820545558398,
              "ttft_s": 0.0611149465
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3072723625,
              "format_passes": 0,
              "gpu_energy_j": 73.63450658677945,
              "semantic_passes": 0,
              "tokens_per_s": 95.81855298067526,
              "ttft_s": 0.0777430905
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.398398182,
              "format_passes": 0,
              "gpu_energy_j": 93.76132874822444,
              "semantic_passes": 2,
              "tokens_per_s": 96.13205103401386,
              "ttft_s": 0.107071765
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0310349545,
              "format_passes": 2,
              "gpu_energy_j": 268.7270291041069,
              "semantic_passes": 2,
              "tokens_per_s": 94.109082798296,
              "ttft_s": 0.8716091509999999
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1488139805,
              "format_passes": 0,
              "gpu_energy_j": 30.309098693506016,
              "semantic_passes": 0,
              "tokens_per_s": 93.73472239206228,
              "ttft_s": 0.063446279
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.2058169165,
              "format_passes": 0,
              "gpu_energy_j": 50.285534110774876,
              "semantic_passes": 0,
              "tokens_per_s": 2466.230393652485,
              "ttft_s": 0.2056708925
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7567786489999999,
              "format_passes": 0,
              "gpu_energy_j": 199.24750767428156,
              "semantic_passes": 0,
              "tokens_per_s": 2710.5356805413967,
              "ttft_s": 0.7565658390000001
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.499557133,
              "format_passes": 0,
              "gpu_energy_j": 404.86405682065606,
              "semantic_passes": 0,
              "tokens_per_s": 2734.7335697771964,
              "ttft_s": 1.499174602
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.254897732,
              "format_passes": 2,
              "gpu_energy_j": 58.885369586385494,
              "semantic_passes": 2,
              "tokens_per_s": 95.33705023748357,
              "ttft_s": 0.076474759
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3519219425,
              "format_passes": 0,
              "gpu_energy_j": 83.25746281210661,
              "semantic_passes": 2,
              "tokens_per_s": 96.01392238208467,
              "ttft_s": 0.0706736745
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3146299635,
              "format_passes": 0,
              "gpu_energy_j": 74.55858377417508,
              "semantic_passes": 0,
              "tokens_per_s": 95.9689447346432,
              "ttft_s": 0.0749268905
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.55053692,
              "format_passes": 0,
              "gpu_energy_j": 138.62089786840238,
              "semantic_passes": 0,
              "tokens_per_s": 96.17184478066059,
              "ttft_s": 0.3034118245
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.524901943,
              "format_passes": 0,
              "gpu_energy_j": 130.98865922779237,
              "semantic_passes": 0,
              "tokens_per_s": 95.8414782137883,
              "ttft_s": 0.274635438
            }
          }
        }
      },
      "change_exercised": false,
      "comparison": {
        "format_pass_change": 0,
        "note": "Existing baseline errors do not suppress speed results. Two starts per arm; no independent confirmation claimed.",
        "quality_pass_change": 0,
        "status": "DESCRIPTIVE_COMPARISON",
        "tasks": {
          "code": {
            "e2e_change_pct": -0.5629169074527263,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.04702152090394485,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.476887027988826,
            "ttft_change_pct": -0.7872163992377335
          },
          "decode": {
            "e2e_change_pct": 0.11949148663286113,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.700312983112994,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.09067669824132096,
            "ttft_change_pct": 0.27630523178920896
          },
          "energy": {
            "e2e_change_pct": -0.4372384987749167,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.9969443484924705,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.008715223583066756,
            "ttft_change_pct": -1.3345634148409502
          },
          "filtering": {
            "e2e_change_pct": 0.12376755840286524,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.5299564514728692,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.1654304128546613,
            "ttft_change_pct": 0.1171280679601372
          },
          "german": {
            "e2e_change_pct": 0.1368255078048719,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 5.477465780576285,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -1.113452228903189,
            "ttft_change_pct": -1.3342633412530724
          },
          "ha_sim": {
            "e2e_change_pct": 0.02412302098444563,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.7981795199025532,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.1782479762957201,
            "ttft_change_pct": -0.19232369801316374
          },
          "jarvis_memory": {
            "e2e_change_pct": -0.09332439505554957,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.2337135637538696,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.04412710178183232,
            "ttft_change_pct": -0.44451622924985834
          },
          "long_context": {
            "e2e_change_pct": -0.2453816077304105,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.788636820905031,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.36546405866610954,
            "ttft_change_pct": -0.22597703234232824
          },
          "math": {
            "e2e_change_pct": -0.6532393841602979,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -8.066051190376644,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 1.166915129246826,
            "ttft_change_pct": 0.03639677881253078
          },
          "prefill": {
            "e2e_change_pct": -0.1012316537285396,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.2903007721578375,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.07490725918175567,
            "ttft_change_pct": -0.07623775389613563
          },
          "prefill2048": {
            "e2e_change_pct": 0.09959900104183905,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.2449803307878584,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.11246330226695189,
            "ttft_change_pct": 0.11611512552713865
          },
          "prefill4096": {
            "e2e_change_pct": 0.028058886048376586,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.11513443272832546,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.020561449366784945,
            "ttft_change_pct": 0.023271350068587715
          },
          "pve_sim": {
            "e2e_change_pct": 0.16754398831111406,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.491972811146905,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.17230232771223708,
            "ttft_change_pct": 0.0650794709617486
          },
          "sorting": {
            "e2e_change_pct": 0.22844794349565767,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.6320711030505799,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.16900639961804353,
            "ttft_change_pct": 0.4653413019847452
          },
          "time": {
            "e2e_change_pct": -0.19794926856862016,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.5986208118231917,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.19903509310448264,
            "ttft_change_pct": -0.24521351199443542
          },
          "tool-call": {
            "e2e_change_pct": -0.28912701679688624,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.7783279877855209,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.18769446750781515,
            "ttft_change_pct": -0.449955881674724
          },
          "tool-final": {
            "e2e_change_pct": -0.19811703216212617,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.1797392329175196,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.1614789404965178,
            "ttft_change_pct": -0.12790015963910495
          }
        }
      },
      "complete": true,
      "numerical_results": [
        {
          "begin_ns": 346954476317084,
          "end_ns": 346955282976738,
          "model": "qwen35",
          "passed": true,
          "reference": "existing CPU reference backend",
          "returncode": 0
        },
        {
          "begin_ns": 346994389681529,
          "end_ns": 346994846293294,
          "model": "qwen35",
          "passed": true,
          "reference": "existing CPU reference backend",
          "returncode": 0
        }
      ]
    }
  }
}
```
