# Public audit excerpt

Original SHA256: `75eaa00ae12a5049e21dac5c5b5df87c00c50c30eba5b323e90d5bb3fe8ac4a6`

Original file: `RESULTS.json`; 43306 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{}
```

## Selected aggregate measurements

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
              "e2e_s": 1.762565419,
              "format_passes": 2,
              "gpu_energy_j": 478.03627097425243,
              "semantic_passes": 2,
              "tokens_per_s": 35.41401570030746,
              "ttft_s": 0.520078519
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.7832698875000004,
              "format_passes": 0,
              "gpu_energy_j": 1065.9003028126685,
              "semantic_passes": 0,
              "tokens_per_s": 35.39091789992607,
              "ttft_s": 0.1949343155
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5802209435000001,
              "format_passes": 2,
              "gpu_energy_j": 148.92215388702533,
              "semantic_passes": 2,
              "tokens_per_s": 34.95987390923873,
              "ttft_s": 0.208320221
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.924570874,
              "format_passes": 0,
              "gpu_energy_j": 243.0658983395718,
              "semantic_passes": 0,
              "tokens_per_s": 34.93974432618158,
              "ttft_s": 0.5238259275
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.46511004499999997,
              "format_passes": 2,
              "gpu_energy_j": 107.47131133899325,
              "semantic_passes": 2,
              "tokens_per_s": 34.27253460070812,
              "ttft_s": 0.2024470155
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.988138015,
              "format_passes": 0,
              "gpu_energy_j": 267.9073782312515,
              "semantic_passes": 0,
              "tokens_per_s": 35.29178152181616,
              "ttft_s": 0.2229980895
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.148622964,
              "format_passes": 0,
              "gpu_energy_j": 296.90796755214075,
              "semantic_passes": 2,
              "tokens_per_s": 35.17289525396524,
              "ttft_s": 0.35250599400000004
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.795297632,
              "format_passes": 2,
              "gpu_energy_j": 1025.6654618278308,
              "semantic_passes": 2,
              "tokens_per_s": 34.35079288325481,
              "ttft_s": 3.2130345545
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.573477867,
              "format_passes": 2,
              "gpu_energy_j": 144.35918745979473,
              "semantic_passes": 2,
              "tokens_per_s": 34.825484149663296,
              "ttft_s": 0.2001853445
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.726965239,
              "format_passes": 0,
              "gpu_energy_j": 186.15827864541026,
              "semantic_passes": 0,
              "tokens_per_s": 695.7176556539735,
              "ttft_s": 0.726800946
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.751302861,
              "format_passes": 0,
              "gpu_energy_j": 734.0012261610882,
              "semantic_passes": 0,
              "tokens_per_s": 744.7447450784505,
              "ttft_s": 2.751040603
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.472420817,
              "format_passes": 0,
              "gpu_energy_j": 1474.0154448435758,
              "semantic_passes": 0,
              "tokens_per_s": 748.7196030265925,
              "ttft_s": 5.472078075500001
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8470545995000001,
              "format_passes": 0,
              "gpu_energy_j": 226.37416622696765,
              "semantic_passes": 2,
              "tokens_per_s": 35.20442804867804,
              "ttft_s": 0.2221175105
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9849087409999999,
              "format_passes": 0,
              "gpu_energy_j": 257.92651581783247,
              "semantic_passes": 2,
              "tokens_per_s": 35.10181746377657,
              "ttft_s": 0.21569171199999998
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0148212024999999,
              "format_passes": 0,
              "gpu_energy_j": 273.8402577125179,
              "semantic_passes": 2,
              "tokens_per_s": 35.22811264446883,
              "ttft_s": 0.21998494549999997
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7081539700000001,
              "format_passes": 0,
              "gpu_energy_j": 461.7310894049181,
              "semantic_passes": 0,
              "tokens_per_s": 35.00688701134956,
              "ttft_s": 1.029332797
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7788582145,
              "format_passes": 0,
              "gpu_energy_j": 465.6153224583703,
              "semantic_passes": 0,
              "tokens_per_s": 35.07657210827447,
              "ttft_s": 1.0941825
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
              "e2e_s": 1.77039693,
              "format_passes": 2,
              "gpu_energy_j": 485.17053145512455,
              "semantic_passes": 2,
              "tokens_per_s": 35.19379186361218,
              "ttft_s": 0.5201588335
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.8019127815,
              "format_passes": 0,
              "gpu_energy_j": 1072.9039050935626,
              "semantic_passes": 0,
              "tokens_per_s": 35.21323505969572,
              "ttft_s": 0.195063217
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5837532585,
              "format_passes": 2,
              "gpu_energy_j": 147.789538781401,
              "semantic_passes": 2,
              "tokens_per_s": 34.79591415109684,
              "ttft_s": 0.21012509899999998
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9268992659999999,
              "format_passes": 0,
              "gpu_energy_j": 246.35560588498444,
              "semantic_passes": 0,
              "tokens_per_s": 34.80062615483521,
              "ttft_s": 0.5245519085
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.466244493,
              "format_passes": 2,
              "gpu_energy_j": 110.93322709960071,
              "semantic_passes": 2,
              "tokens_per_s": 34.098872447580945,
              "ttft_s": 0.20227701050000002
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9961739814999999,
              "format_passes": 0,
              "gpu_energy_j": 265.91802901979725,
              "semantic_passes": 0,
              "tokens_per_s": 35.04738924517109,
              "ttft_s": 0.2257156105
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1500110719999999,
              "format_passes": 0,
              "gpu_energy_j": 300.14987749119086,
              "semantic_passes": 2,
              "tokens_per_s": 35.133057613236545,
              "ttft_s": 0.3530167385
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.802288172,
              "format_passes": 2,
              "gpu_energy_j": 1023.3794881702388,
              "semantic_passes": 2,
              "tokens_per_s": 34.17229365973839,
              "ttft_s": 3.2169927555
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.576194179,
              "format_passes": 2,
              "gpu_energy_j": 148.23467872031154,
              "semantic_passes": 2,
              "tokens_per_s": 34.808919467073,
              "ttft_s": 0.20270733000000002
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7242365319999999,
              "format_passes": 0,
              "gpu_energy_j": 186.25860061587179,
              "semantic_passes": 0,
              "tokens_per_s": 698.2941931179103,
              "ttft_s": 0.724104044
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.7558815255,
              "format_passes": 0,
              "gpu_energy_j": 738.1382115360759,
              "semantic_passes": 0,
              "tokens_per_s": 743.4650357127276,
              "ttft_s": 2.755635783
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.480775883,
              "format_passes": 0,
              "gpu_energy_j": 1478.7148614111738,
              "semantic_passes": 0,
              "tokens_per_s": 747.5662452532783,
              "ttft_s": 5.480457144
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8497186590000001,
              "format_passes": 0,
              "gpu_energy_j": 225.71693081107398,
              "semantic_passes": 2,
              "tokens_per_s": 35.085176315534,
              "ttft_s": 0.22265227399999998
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.989844605,
              "format_passes": 0,
              "gpu_energy_j": 262.5104622828884,
              "semantic_passes": 2,
              "tokens_per_s": 34.89519735252165,
              "ttft_s": 0.21608395549999998
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0197380795,
              "format_passes": 0,
              "gpu_energy_j": 276.3815565928146,
              "semantic_passes": 2,
              "tokens_per_s": 35.090624395116144,
              "ttft_s": 0.2217491885
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7137037789999998,
              "format_passes": 0,
              "gpu_energy_j": 467.79448860417654,
              "semantic_passes": 0,
              "tokens_per_s": 34.85700723045109,
              "ttft_s": 1.0319798850000002
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7822843124999999,
              "format_passes": 0,
              "gpu_energy_j": 468.64338516729885,
              "semantic_passes": 0,
              "tokens_per_s": 34.90188209646553,
              "ttft_s": 1.0944796955
            }
          }
        }
      },
      "change_exercised": true,
      "comparison": {
        "format_pass_change": 0,
        "note": "Existing baseline errors do not suppress speed results. Two starts per arm; no independent confirmation claimed.",
        "quality_pass_change": 0,
        "status": "DESCRIPTIVE_COMPARISON",
        "tasks": {
          "code": {
            "e2e_change_pct": 0.4443245575783017,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.4924098680487718,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.6218550264362466,
            "ttft_change_pct": 0.01544276432612346
          },
          "decode": {
            "e2e_change_pct": 0.4927719817609644,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.6570597890265262,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.5020577333788911,
            "ttft_change_pct": 0.06612560732026651
          },
          "energy": {
            "e2e_change_pct": 0.6087879177012034,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.7605417166364314,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.46899413472587526,
            "ttft_change_pct": 0.8663959702692514
          },
          "filtering": {
            "e2e_change_pct": 0.2518348852940333,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.3534220834289235,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.3981659683815364,
            "ttft_change_pct": 0.13859203256028074
          },
          "german": {
            "e2e_change_pct": 0.24390958918121264,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.221246412158929,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.5067093961693359,
            "ttft_change_pct": -0.08397505864934374
          },
          "ha_sim": {
            "e2e_change_pct": 0.813243330183977,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.7425511102337468,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.6924906199308634,
            "ttft_change_pct": 1.2186297228344634
          },
          "jarvis_memory": {
            "e2e_change_pct": 0.12084975170318923,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.0918905160336667,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.11326233010119369,
            "ttft_change_pct": 0.14488959299794324
          },
          "long_context": {
            "e2e_change_pct": 0.184189507064203,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.22287712150491634,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.5196364000186748,
            "ttft_change_pct": 0.1231919835551265
          },
          "math": {
            "e2e_change_pct": 0.47365594320312177,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.6846169812338117,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.04756483074036533,
            "ttft_change_pct": 1.2598252416025524
          },
          "prefill": {
            "e2e_change_pct": -0.3753559116187799,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.0538906844173237,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.37034240010982433,
            "ttft_change_pct": -0.3710647344149276
          },
          "prefill2048": {
            "e2e_change_pct": 0.1664180474240995,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.5636210441533729,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.1718319429817594,
            "ttft_change_pct": 0.1670342486035592
          },
          "prefill4096": {
            "e2e_change_pct": 0.15267586831124724,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.31881732203264956,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.15404401977080484,
            "ttft_change_pct": 0.15312406702518988
          },
          "pve_sim": {
            "e2e_change_pct": 0.3145085926659963,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.2903314573601601,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.3387407202842474,
            "ttft_change_pct": 0.24075702037007485
          },
          "sorting": {
            "e2e_change_pct": 0.5011493750160634,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.777229630897459,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.5886308065619184,
            "ttft_change_pct": 0.18185376543351506
          },
          "time": {
            "e2e_change_pct": 0.4845067276765036,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.9280223811959143,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.3902799185986794,
            "ttft_change_pct": 0.8019835157310862
          },
          "tool-call": {
            "e2e_change_pct": 0.32490098067678996,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.3131884203580357,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.42814369883812375,
            "ttft_change_pct": 0.25716541896996237
          },
          "tool-final": {
            "e2e_change_pct": 0.19260096010309535,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.6503357090872575,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.4980247535868343,
            "ttft_change_pct": 0.02716141959864249
          }
        }
      },
      "complete": true,
      "numerical_results": [
        {
          "begin_ns": 352403405927921,
          "end_ns": 352404115751819,
          "model": "qwen38",
          "passed": true,
          "reference": "existing CPU reference backend",
          "returncode": 0
        },
        {
          "begin_ns": 352505424218756,
          "end_ns": 352505931429978,
          "model": "qwen38",
          "passed": true,
          "reference": "existing CPU reference backend",
          "returncode": 0
        }
      ]
    }
  }
}
```
