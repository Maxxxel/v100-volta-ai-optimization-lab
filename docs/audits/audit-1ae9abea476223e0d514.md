# Public audit excerpt

Original SHA256: `1ae9abea476223e0d514096f62fab927195842e9b614cccbdb5d0f03e5447d38`

Original file: `RESULTS.json`; 39843 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 1.761608502,
              "format_passes": 2,
              "gpu_energy_j": 479.6253741275725,
              "semantic_passes": 2,
              "tokens_per_s": 35.43253386906348,
              "ttft_s": 0.519753437
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.7830029265,
              "format_passes": 0,
              "gpu_energy_j": 1067.5633365827475,
              "semantic_passes": 0,
              "tokens_per_s": 35.39179843898458,
              "ttft_s": 0.194299098
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.580305318,
              "format_passes": 2,
              "gpu_energy_j": 143.7656760511699,
              "semantic_passes": 2,
              "tokens_per_s": 34.99366790253606,
              "ttft_s": 0.2087819165
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9253967615,
              "format_passes": 0,
              "gpu_energy_j": 244.73368852658572,
              "semantic_passes": 0,
              "tokens_per_s": 34.978881730930894,
              "ttft_s": 0.525126684
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.46610016600000004,
              "format_passes": 2,
              "gpu_energy_j": 109.16099067404008,
              "semantic_passes": 2,
              "tokens_per_s": 34.261850585422756,
              "ttft_s": 0.20336864300000002
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9892804820000001,
              "format_passes": 0,
              "gpu_energy_j": 270.9517022305947,
              "semantic_passes": 0,
              "tokens_per_s": 35.325251344166574,
              "ttft_s": 0.2248656525
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.145445198,
              "format_passes": 0,
              "gpu_energy_j": 300.9583968968569,
              "semantic_passes": 2,
              "tokens_per_s": 35.30559491799505,
              "ttft_s": 0.352321228
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.794749283,
              "format_passes": 2,
              "gpu_energy_j": 1021.8976502838045,
              "semantic_passes": 2,
              "tokens_per_s": 34.37622373179891,
              "ttft_s": 3.212865105
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.574117718,
              "format_passes": 2,
              "gpu_energy_j": 143.74713854867957,
              "semantic_passes": 2,
              "tokens_per_s": 34.9559417607097,
              "ttft_s": 0.202218615
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7249749945,
              "format_passes": 0,
              "gpu_energy_j": 188.61598090366363,
              "semantic_passes": 0,
              "tokens_per_s": 697.5452834742778,
              "ttft_s": 0.724844752
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.7482055704999997,
              "format_passes": 0,
              "gpu_energy_j": 731.9852312283069,
              "semantic_passes": 0,
              "tokens_per_s": 745.5544271899734,
              "ttft_s": 2.7479501795
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.470404255,
              "format_passes": 0,
              "gpu_energy_j": 1469.6301098780518,
              "semantic_passes": 0,
              "tokens_per_s": 748.9845628517121,
              "ttft_s": 5.4700661955
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8475403825000001,
              "format_passes": 0,
              "gpu_energy_j": 229.5257214009467,
              "semantic_passes": 2,
              "tokens_per_s": 35.26968709109762,
              "ttft_s": 0.223678698
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9856428795000001,
              "format_passes": 0,
              "gpu_energy_j": 261.72760779546275,
              "semantic_passes": 2,
              "tokens_per_s": 35.096555439751825,
              "ttft_s": 0.21627561350000002
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0146751815,
              "format_passes": 0,
              "gpu_energy_j": 271.71271763880077,
              "semantic_passes": 2,
              "tokens_per_s": 35.21913240410156,
              "ttft_s": 0.2195607985
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7067516010000001,
              "format_passes": 0,
              "gpu_energy_j": 457.52757128233304,
              "semantic_passes": 0,
              "tokens_per_s": 34.995143836967905,
              "ttft_s": 1.0284216745
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7774648595,
              "format_passes": 0,
              "gpu_energy_j": 466.68315940608403,
              "semantic_passes": 0,
              "tokens_per_s": 35.08810449839292,
              "ttft_s": 1.093557258
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
              "e2e_s": 1.7635070165000002,
              "format_passes": 2,
              "gpu_energy_j": 479.1724987452195,
              "semantic_passes": 2,
              "tokens_per_s": 35.39769130127418,
              "ttft_s": 0.5204512084999999
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.7852333585,
              "format_passes": 0,
              "gpu_energy_j": 1068.3812111826487,
              "semantic_passes": 0,
              "tokens_per_s": 35.37780862333672,
              "ttft_s": 0.19557821949999998
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.580618335,
              "format_passes": 2,
              "gpu_energy_j": 146.12078331162337,
              "semantic_passes": 2,
              "tokens_per_s": 35.006415805038515,
              "ttft_s": 0.2092319835
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.924397745,
              "format_passes": 0,
              "gpu_energy_j": 247.90140776545854,
              "semantic_passes": 0,
              "tokens_per_s": 34.967932967253404,
              "ttft_s": 0.52397556
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.465549394,
              "format_passes": 2,
              "gpu_energy_j": 108.67594520769907,
              "semantic_passes": 2,
              "tokens_per_s": 34.22421643846127,
              "ttft_s": 0.20254322549999998
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.989844136,
              "format_passes": 0,
              "gpu_energy_j": 270.0371372464581,
              "semantic_passes": 0,
              "tokens_per_s": 35.26077328644455,
              "ttft_s": 0.2240908375
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1591985519999999,
              "format_passes": 0,
              "gpu_energy_j": 296.1154521504336,
              "semantic_passes": 2,
              "tokens_per_s": 35.14242440635581,
              "ttft_s": 0.362364174
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.80438906,
              "format_passes": 2,
              "gpu_energy_j": 1020.8901455170733,
              "semantic_passes": 2,
              "tokens_per_s": 34.31819642551139,
              "ttft_s": 3.2215819134999997
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5739070575,
              "format_passes": 2,
              "gpu_energy_j": 142.03560674963398,
              "semantic_passes": 2,
              "tokens_per_s": 34.97424712609415,
              "ttft_s": 0.20219127399999998
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7270108719999999,
              "format_passes": 0,
              "gpu_energy_j": 187.36515922911806,
              "semantic_passes": 0,
              "tokens_per_s": 695.621075497621,
              "ttft_s": 0.7268679295
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.7466982150000003,
              "format_passes": 0,
              "gpu_energy_j": 732.3729847270331,
              "semantic_passes": 0,
              "tokens_per_s": 745.9577040866704,
              "ttft_s": 2.746471083
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.463743813,
              "format_passes": 0,
              "gpu_energy_j": 1485.7089451606107,
              "semantic_passes": 0,
              "tokens_per_s": 749.9063659900987,
              "ttft_s": 5.46342128
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8477699745,
              "format_passes": 0,
              "gpu_energy_j": 229.40004660624766,
              "semantic_passes": 2,
              "tokens_per_s": 35.21598635233997,
              "ttft_s": 0.22303287300000002
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9857487840000001,
              "format_passes": 0,
              "gpu_energy_j": 265.36867723415764,
              "semantic_passes": 2,
              "tokens_per_s": 35.08255039032716,
              "ttft_s": 0.216107875
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.014371841,
              "format_passes": 0,
              "gpu_energy_j": 277.7117492714448,
              "semantic_passes": 2,
              "tokens_per_s": 35.257247647910575,
              "ttft_s": 0.220192313
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7080639684999999,
              "format_passes": 0,
              "gpu_energy_j": 461.302225214537,
              "semantic_passes": 0,
              "tokens_per_s": 35.045384449095636,
              "ttft_s": 1.029702871
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.77841424,
              "format_passes": 0,
              "gpu_energy_j": 469.54309206981804,
              "semantic_passes": 0,
              "tokens_per_s": 35.07964316608859,
              "ttft_s": 1.093968043
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
            "e2e_change_pct": 0.1077716472101864,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.09442273215356511,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.09833495938521564,
            "ttft_change_pct": 0.13425048308048915
          },
          "decode": {
            "e2e_change_pct": 0.058959298825178585,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.07661134209790976,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.03952841128427309,
            "ttft_change_pct": 0.6583260103451227
          },
          "energy": {
            "e2e_change_pct": 0.053940053673628974,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.6381568432337401,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.036429169237006676,
            "ttft_change_pct": 0.2155679991566739
          },
          "filtering": {
            "e2e_change_pct": -0.10795547829459684,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.2943535718126897,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.031301068346645256,
            "ttft_change_pct": -0.21920881857147023
          },
          "german": {
            "e2e_change_pct": -0.11816601670123772,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.4443395606305689,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.10984271520202427,
            "ttft_change_pct": -0.4058725513549466
          },
          "ha_sim": {
            "e2e_change_pct": 0.05697615693986968,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.3375380101352077,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.1825268193956564,
            "ttft_change_pct": -0.34456796375338383
          },
          "jarvis_memory": {
            "e2e_change_pct": 1.200699433199759,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.609174157078952,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.4621661581351133,
            "ttft_change_pct": 2.850508343482505
          },
          "long_context": {
            "e2e_change_pct": 0.25402935164084983,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.09859155331763958,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.16880069998451708,
            "ttft_change_pct": 0.2713095077173877
          },
          "math": {
            "e2e_change_pct": -0.03669291042502909,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.1906545175965233,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.05236696384769424,
            "ttft_change_pct": -0.013520515903053809
          },
          "prefill": {
            "e2e_change_pct": 0.28082037524672643,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.6631578451374298,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.2758542021921273,
            "ttft_change_pct": 0.27911873465562564
          },
          "prefill2048": {
            "e2e_change_pct": -0.05484871714764861,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.052972858219479946,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.05409087277732372,
            "ttft_change_pct": -0.05382544818440804
          },
          "prefill4096": {
            "e2e_change_pct": -0.12175410974266665,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.0940736158361108,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.12307371661666178,
            "ttft_change_pct": -0.12147778952777966
          },
          "pve_sim": {
            "e2e_change_pct": 0.027089210702002653,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.054754122514888426,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.15225748563901798,
            "ttft_change_pct": -0.2887288802083332
          },
          "sorting": {
            "e2e_change_pct": 0.010744713141308537,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.3911675078390529,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.03990434174860891,
            "ttft_change_pct": -0.07755775017140865
          },
          "time": {
            "e2e_change_pct": -0.029895330597473624,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.207858242623284,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.10822311967166875,
            "ttft_change_pct": 0.2876262540099983
          },
          "tool-call": {
            "e2e_change_pct": 0.07689270654445135,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.8250112494039508,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.143564525300377,
            "ttft_change_pct": 0.12457890880439582
          },
          "tool-final": {
            "e2e_change_pct": 0.05341205452957798,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.6128210555901958,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.024114532333097127,
            "ttft_change_pct": 0.03756410530815213
          }
        }
      },
      "complete": true
    }
  }
}
```

</details>
