# Public audit excerpt

Original SHA256: `0dde041105eb7affdd81998ff5ab4ce77a83a5adbcceb0eb86bec1feb4b8d8a7`

Original file: `RESULTS.json`; 39937 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 1.7647415335,
              "format_passes": 2,
              "gpu_energy_j": 478.478732715285,
              "semantic_passes": 2,
              "tokens_per_s": 35.37512132140259,
              "ttft_s": 0.5209143365
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.781360132,
              "format_passes": 0,
              "gpu_energy_j": 1068.6692499621263,
              "semantic_passes": 0,
              "tokens_per_s": 35.4025254350112,
              "ttft_s": 0.194438255
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5803707650000001,
              "format_passes": 2,
              "gpu_energy_j": 144.76285689491132,
              "semantic_passes": 2,
              "tokens_per_s": 34.957372784107356,
              "ttft_s": 0.208445606
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.924078759,
              "format_passes": 0,
              "gpu_energy_j": 245.07296995313203,
              "semantic_passes": 0,
              "tokens_per_s": 34.97474439029988,
              "ttft_s": 0.5237136365
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.468912194,
              "format_passes": 2,
              "gpu_energy_j": 109.86064641043585,
              "semantic_passes": 2,
              "tokens_per_s": 34.23689831557195,
              "ttft_s": 0.20595291500000001
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9900257375,
              "format_passes": 0,
              "gpu_energy_j": 267.7355761482197,
              "semantic_passes": 0,
              "tokens_per_s": 35.27489468510228,
              "ttft_s": 0.2245889495
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1457598225,
              "format_passes": 0,
              "gpu_energy_j": 297.1073419811596,
              "semantic_passes": 2,
              "tokens_per_s": 35.30509043666792,
              "ttft_s": 0.35262175100000004
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.7987356534999996,
              "format_passes": 2,
              "gpu_energy_j": 1026.9462504052503,
              "semantic_passes": 2,
              "tokens_per_s": 34.333434353410254,
              "ttft_s": 3.2161264665
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5749469684999999,
              "format_passes": 2,
              "gpu_energy_j": 142.97141956796065,
              "semantic_passes": 2,
              "tokens_per_s": 34.977245326307866,
              "ttft_s": 0.203230832
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.724803555,
              "format_passes": 0,
              "gpu_energy_j": 188.75373240214134,
              "semantic_passes": 0,
              "tokens_per_s": 697.7958640506122,
              "ttft_s": 0.724644557
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.7493388805,
              "format_passes": 0,
              "gpu_energy_j": 737.5611732435823,
              "semantic_passes": 0,
              "tokens_per_s": 745.2543256672127,
              "ttft_s": 2.7490825975
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.4697730149999995,
              "format_passes": 0,
              "gpu_energy_j": 1470.7238636123725,
              "semantic_passes": 0,
              "tokens_per_s": 749.0735202361004,
              "ttft_s": 5.469415640499999
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8511897115,
              "format_passes": 0,
              "gpu_energy_j": 226.380199263157,
              "semantic_passes": 2,
              "tokens_per_s": 35.155704246817706,
              "ttft_s": 0.225370994
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.984510397,
              "format_passes": 0,
              "gpu_energy_j": 265.0687037310125,
              "semantic_passes": 2,
              "tokens_per_s": 35.11498083272512,
              "ttft_s": 0.2155778855
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0158276665,
              "format_passes": 0,
              "gpu_energy_j": 272.7678364110269,
              "semantic_passes": 2,
              "tokens_per_s": 35.243313309318594,
              "ttft_s": 0.2213099685
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.707723846,
              "format_passes": 0,
              "gpu_energy_j": 464.68174419371434,
              "semantic_passes": 0,
              "tokens_per_s": 35.05233558439026,
              "ttft_s": 1.029663489
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.778515391,
              "format_passes": 0,
              "gpu_energy_j": 467.636213226373,
              "semantic_passes": 0,
              "tokens_per_s": 35.07400730553162,
              "ttft_s": 1.0943570459999998
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
              "e2e_s": 1.766974668,
              "format_passes": 2,
              "gpu_energy_j": 485.52352237433865,
              "semantic_passes": 2,
              "tokens_per_s": 35.315325862582014,
              "ttft_s": 0.521039322
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.7919189785,
              "format_passes": 0,
              "gpu_energy_j": 1068.7484495018284,
              "semantic_passes": 0,
              "tokens_per_s": 35.31472624546257,
              "ttft_s": 0.196063156
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5839116165,
              "format_passes": 2,
              "gpu_energy_j": 147.39941477717412,
              "semantic_passes": 2,
              "tokens_per_s": 34.98070717749525,
              "ttft_s": 0.21228470500000002
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9264808680000001,
              "format_passes": 0,
              "gpu_energy_j": 247.2253207378049,
              "semantic_passes": 0,
              "tokens_per_s": 34.899620197139235,
              "ttft_s": 0.525303868
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.46855254550000003,
              "format_passes": 2,
              "gpu_energy_j": 112.3457745398416,
              "semantic_passes": 2,
              "tokens_per_s": 34.14936415306802,
              "ttft_s": 0.20496116749999999
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.99283416,
              "format_passes": 0,
              "gpu_energy_j": 269.15843498357424,
              "semantic_passes": 0,
              "tokens_per_s": 35.254054337574516,
              "ttft_s": 0.22687404449999998
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.149380447,
              "format_passes": 0,
              "gpu_energy_j": 296.7002569657204,
              "semantic_passes": 2,
              "tokens_per_s": 35.22224696621272,
              "ttft_s": 0.35443714449999997
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.8057372865000003,
              "format_passes": 2,
              "gpu_energy_j": 1029.1373752984755,
              "semantic_passes": 2,
              "tokens_per_s": 34.335209329653864,
              "ttft_s": 3.2232105310000003
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5763891545,
              "format_passes": 2,
              "gpu_energy_j": 143.97502980283906,
              "semantic_passes": 2,
              "tokens_per_s": 34.935550431250775,
              "ttft_s": 0.2042411065
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.728515183,
              "format_passes": 0,
              "gpu_energy_j": 191.65179959968611,
              "semantic_passes": 0,
              "tokens_per_s": 694.1788934535061,
              "ttft_s": 0.7283753264999999
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.7480624875,
              "format_passes": 0,
              "gpu_energy_j": 735.6231457865313,
              "semantic_passes": 0,
              "tokens_per_s": 745.5903952814506,
              "ttft_s": 2.747823575
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.475922787,
              "format_passes": 0,
              "gpu_energy_j": 1478.8960305547448,
              "semantic_passes": 0,
              "tokens_per_s": 748.2452172881613,
              "ttft_s": 5.4756057725
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.848914459,
              "format_passes": 0,
              "gpu_energy_j": 223.58314818155873,
              "semantic_passes": 2,
              "tokens_per_s": 35.115890857658925,
              "ttft_s": 0.222379172
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.988067238,
              "format_passes": 0,
              "gpu_energy_j": 266.1278099933635,
              "semantic_passes": 2,
              "tokens_per_s": 35.031447113321384,
              "ttft_s": 0.217262342
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.015634486,
              "format_passes": 0,
              "gpu_energy_j": 273.8595991007979,
              "semantic_passes": 2,
              "tokens_per_s": 35.239052171407195,
              "ttft_s": 0.221067179
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7103217590000002,
              "format_passes": 0,
              "gpu_energy_j": 460.8813292864347,
              "semantic_passes": 0,
              "tokens_per_s": 34.99278696287387,
              "ttft_s": 1.0311496995
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7805413909999999,
              "format_passes": 0,
              "gpu_energy_j": 468.7763623520487,
              "semantic_passes": 0,
              "tokens_per_s": 35.04552670045676,
              "ttft_s": 1.095661678
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
            "e2e_change_pct": 0.12654173189718954,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.4723307803202967,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.16903251942883557,
            "ttft_change_pct": 0.0239934843874412
          },
          "decode": {
            "e2e_change_pct": 0.2792340885663158,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.007411043192728783,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.24800261695963055,
            "ttft_change_pct": 0.8356899726342348
          },
          "energy": {
            "e2e_change_pct": 0.6101016304637552,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.8212944527454145,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.06675099279342955,
            "ttft_change_pct": 1.8417749712603682
          },
          "filtering": {
            "e2e_change_pct": 0.259946349443152,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.878248949724858,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.21479554595824624,
            "ttft_change_pct": 0.3036452345651197
          },
          "german": {
            "e2e_change_pct": -0.07669847459756962,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.2620730995168037,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.2556719995400858,
            "ttft_change_pct": -0.48154089006219314
          },
          "ha_sim": {
            "e2e_change_pct": 0.28367166565708146,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.5314418262318821,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.05907982919242105,
            "ttft_change_pct": 1.0174565601233976
          },
          "jarvis_memory": {
            "e2e_change_pct": 0.31600204762807227,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.13701614127900053,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.23465021454570634,
            "ttft_change_pct": 0.5148274304836997
          },
          "long_context": {
            "e2e_change_pct": 0.18431482573812996,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.21336315239093295,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.005169818507932966,
            "ttft_change_pct": 0.2202669756239395
          },
          "math": {
            "e2e_change_pct": 0.25083809099168963,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.7019656361468396,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.11920577126104392,
            "ttft_change_pct": 0.4971069055112576
          },
          "prefill": {
            "e2e_change_pct": 0.5120874441627121,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.5353694788776018,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.5183422234849577,
            "ttft_change_pct": 0.5148413058458923
          },
          "prefill2048": {
            "e2e_change_pct": -0.04642545191693159,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.2627615887816015,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.04509462107946671,
            "ttft_change_pct": -0.04579791458958482
          },
          "prefill4096": {
            "e2e_change_pct": 0.1124319415656938,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.5556561054432141,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.11057698951607575,
            "ttft_change_pct": 0.11317720953887278
          },
          "pve_sim": {
            "e2e_change_pct": -0.26730263174710167,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.2355546512912263,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.11324873164042515,
            "ttft_change_pct": -1.3275097859310026
          },
          "sorting": {
            "e2e_change_pct": 0.36128018666317097,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.39955915105911455,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.23788627367236082,
            "ttft_change_pct": 0.7813679478732904
          },
          "time": {
            "e2e_change_pct": -0.019017054405057188,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.4002534551492465,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.012090628012184634,
            "ttft_change_pct": -0.10970563217084228
          },
          "tool-call": {
            "e2e_change_pct": 0.15212723099728986,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.8178532844826614,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.1698848893336269,
            "ttft_change_pct": 0.1443394386493546
          },
          "tool-final": {
            "e2e_change_pct": 0.11391523572144013,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.2438111278443289,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.08120145732640749,
            "ttft_change_pct": 0.11921447435905286
          }
        }
      },
      "complete": true
    }
  }
}
```
