# Public audit excerpt

Original SHA256: `7d979d8fc4bb544dbc4948100f239e29fdab25d8fbac96b31e71468e20f24f1f`

Original file: `RESULTS.json`; 43097 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.6658883845,
              "format_passes": 2,
              "gpu_energy_j": 176.75557345426142,
              "semantic_passes": 2,
              "tokens_per_s": 79.32913664554869,
              "ttft_s": 0.1238558865
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6579586750000002,
              "format_passes": 0,
              "gpu_energy_j": 447.06894518507625,
              "semantic_passes": 0,
              "tokens_per_s": 79.62799859926817,
              "ttft_s": 0.0627649495
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2379118975,
              "format_passes": 2,
              "gpu_energy_j": 57.19549808294329,
              "semantic_passes": 2,
              "tokens_per_s": 78.26728540974912,
              "ttft_s": 0.071767393
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.241519389,
              "format_passes": 0,
              "gpu_energy_j": 61.70287842238608,
              "semantic_passes": 0,
              "tokens_per_s": 77.31107484710137,
              "ttft_s": 0.1251035465
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1818939605,
              "format_passes": 2,
              "gpu_energy_j": 39.194309743650074,
              "semantic_passes": 2,
              "tokens_per_s": 77.58453723903091,
              "ttft_s": 0.06586729499999999
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.357298871,
              "format_passes": 0,
              "gpu_energy_j": 87.3838831841004,
              "semantic_passes": 0,
              "tokens_per_s": 78.95747561449522,
              "ttft_s": 0.07860569449999999
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4696588035,
              "format_passes": 0,
              "gpu_energy_j": 115.88720270455653,
              "semantic_passes": 2,
              "tokens_per_s": 79.05442408899454,
              "ttft_s": 0.11544502449999999
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.072666687,
              "format_passes": 2,
              "gpu_energy_j": 286.5490130231947,
              "semantic_passes": 2,
              "tokens_per_s": 78.07776365594864,
              "ttft_s": 0.816466554
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23313172599999998,
              "format_passes": 0,
              "gpu_energy_j": 53.524816995466715,
              "semantic_passes": 0,
              "tokens_per_s": 78.39028565277432,
              "ttft_s": 0.06723209150000001
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.1968060035,
              "format_passes": 0,
              "gpu_energy_j": 47.31738694673085,
              "semantic_passes": 0,
              "tokens_per_s": 2579.908757035233,
              "ttft_s": 0.196625472
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7115703664999999,
              "format_passes": 0,
              "gpu_energy_j": 187.46320573493642,
              "semantic_passes": 0,
              "tokens_per_s": 2883.1835360452305,
              "ttft_s": 0.711313785
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.405809562,
              "format_passes": 0,
              "gpu_energy_j": 376.5843758011191,
              "semantic_passes": 0,
              "tokens_per_s": 2917.2135694920885,
              "ttft_s": 1.405471243
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.29480611700000003,
              "format_passes": 2,
              "gpu_energy_j": 71.17538907802555,
              "semantic_passes": 2,
              "tokens_per_s": 78.68876751778951,
              "ttft_s": 0.07873886
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3531477275,
              "format_passes": 2,
              "gpu_energy_j": 85.86539124386861,
              "semantic_passes": 2,
              "tokens_per_s": 78.70631323342243,
              "ttft_s": 0.0736060345
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3689781775,
              "format_passes": 2,
              "gpu_energy_j": 92.8027686398564,
              "semantic_passes": 2,
              "tokens_per_s": 78.87509820719957,
              "ttft_s": 0.0772964995
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.618971021,
              "format_passes": 0,
              "gpu_energy_j": 156.4895585199033,
              "semantic_passes": 0,
              "tokens_per_s": 79.01305699607116,
              "ttft_s": 0.317584756
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5585260750000001,
              "format_passes": 0,
              "gpu_energy_j": 142.5677642209763,
              "semantic_passes": 0,
              "tokens_per_s": 78.84440581470335,
              "ttft_s": 0.2540756405
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
              "e2e_s": 0.665867922,
              "format_passes": 2,
              "gpu_energy_j": 176.2650339880212,
              "semantic_passes": 2,
              "tokens_per_s": 79.30162412452793,
              "ttft_s": 0.1236100525
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6582394835,
              "format_passes": 0,
              "gpu_energy_j": 447.2985267863472,
              "semantic_passes": 0,
              "tokens_per_s": 79.5929407903497,
              "ttft_s": 0.0625265525
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23779237749999999,
              "format_passes": 2,
              "gpu_energy_j": 53.99583500421113,
              "semantic_passes": 2,
              "tokens_per_s": 78.2905557743733,
              "ttft_s": 0.07168482600000001
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2411852055,
              "format_passes": 0,
              "gpu_energy_j": 59.87920286719409,
              "semantic_passes": 0,
              "tokens_per_s": 77.62469648012912,
              "ttft_s": 0.125185923
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.18173089250000002,
              "format_passes": 2,
              "gpu_energy_j": 40.829064940572,
              "semantic_passes": 2,
              "tokens_per_s": 77.57230390350654,
              "ttft_s": 0.06565645449999999
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.357707706,
              "format_passes": 0,
              "gpu_energy_j": 90.03321383819994,
              "semantic_passes": 0,
              "tokens_per_s": 78.82190903666643,
              "ttft_s": 0.078542372
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.46965588599999997,
              "format_passes": 0,
              "gpu_energy_j": 112.72456317784514,
              "semantic_passes": 2,
              "tokens_per_s": 78.9023726352972,
              "ttft_s": 0.11474277499999999
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0740350625000001,
              "format_passes": 2,
              "gpu_energy_j": 286.65538111103695,
              "semantic_passes": 2,
              "tokens_per_s": 78.01212508728344,
              "ttft_s": 0.81757484
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2334765085,
              "format_passes": 0,
              "gpu_energy_j": 56.00514434412595,
              "semantic_passes": 0,
              "tokens_per_s": 78.19206546656466,
              "ttft_s": 0.067183205
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.197753741,
              "format_passes": 0,
              "gpu_energy_j": 47.8266185822931,
              "semantic_passes": 0,
              "tokens_per_s": 2567.7083097119053,
              "ttft_s": 0.1976196975
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7115960305,
              "format_passes": 0,
              "gpu_energy_j": 188.77111085921956,
              "semantic_passes": 0,
              "tokens_per_s": 2883.115782712919,
              "ttft_s": 0.7113618865
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.405546364,
              "format_passes": 0,
              "gpu_energy_j": 378.6181533607024,
              "semantic_passes": 0,
              "tokens_per_s": 2917.6699190295844,
              "ttft_s": 1.405228851
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.29506325099999997,
              "format_passes": 2,
              "gpu_energy_j": 71.09454199183216,
              "semantic_passes": 2,
              "tokens_per_s": 78.62326756565642,
              "ttft_s": 0.078789236
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3532426315,
              "format_passes": 2,
              "gpu_energy_j": 83.42230526206163,
              "semantic_passes": 2,
              "tokens_per_s": 78.71102860275762,
              "ttft_s": 0.073690632
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.36853906550000004,
              "format_passes": 2,
              "gpu_energy_j": 90.76477018982858,
              "semantic_passes": 2,
              "tokens_per_s": 78.9840675407548,
              "ttft_s": 0.077283905
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6188154435,
              "format_passes": 0,
              "gpu_energy_j": 159.24880489137547,
              "semantic_passes": 0,
              "tokens_per_s": 78.98973106553393,
              "ttft_s": 0.3175216025
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5587837760000001,
              "format_passes": 0,
              "gpu_energy_j": 142.98071652127055,
              "semantic_passes": 0,
              "tokens_per_s": 78.70363962872597,
              "ttft_s": 0.254072625
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
            "e2e_change_pct": -0.003072962447803196,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.2775241858877786,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.03468148297602891,
            "ttft_change_pct": -0.1984839049212206
          },
          "decode": {
            "e2e_change_pct": 0.016937002365269294,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.051352616580402355,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.04402698741041711,
            "ttft_change_pct": -0.3798250486921839
          },
          "energy": {
            "e2e_change_pct": -0.050237084086979245,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -5.5942568663220555,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.029731917367969984,
            "ttft_change_pct": -0.11504806925338729
          },
          "filtering": {
            "e2e_change_pct": -0.13836715196393623,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.9555761446136253,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.405661974882654,
            "ttft_change_pct": 0.06584665447515459
          },
          "german": {
            "e2e_change_pct": -0.08965003541169247,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.170899315778298,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.015767749553863286,
            "ttft_change_pct": -0.320098920108991
          },
          "ha_sim": {
            "e2e_change_pct": 0.11442381523785183,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.031829849582146,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.17169568400424717,
            "ttft_change_pct": -0.08055714080611454
          },
          "jarvis_memory": {
            "e2e_change_pct": -0.0006211956378288086,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.7290671039616354,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.1923376907106089,
            "ttft_change_pct": -0.6082977616761687
          },
          "long_context": {
            "e2e_change_pct": 0.12756763275898475,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.03712038185721411,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.08406819764260609,
            "ttft_change_pct": 0.13574175140063094
          },
          "math": {
            "e2e_change_pct": 0.14789171165834336,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.633976327035949,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.2528632018100718,
            "ttft_change_pct": -0.07271304359171005
          },
          "prefill": {
            "e2e_change_pct": 0.48155924267829775,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.0762040518753402,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.4729022795886828,
            "ttft_change_pct": 0.5056443043147452
          },
          "prefill2048": {
            "e2e_change_pct": 0.003606670711464588,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.6976863108446141,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.0023499486406008963,
            "ttft_change_pct": 0.006762346100175343
          },
          "prefill4096": {
            "e2e_change_pct": -0.01872216601126464,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.5400589324123795,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.01564333658214956,
            "ttft_change_pct": -0.017246315156382863
          },
          "pve_sim": {
            "e2e_change_pct": 0.08722139235664006,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.11358854126495288,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.08323926552578076,
            "ttft_change_pct": 0.06397857423894315
          },
          "sorting": {
            "e2e_change_pct": 0.02687373940415405,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.8452510917562956,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.005991094159374377,
            "ttft_change_pct": 0.11493283203567461
          },
          "time": {
            "e2e_change_pct": -0.11900758006209156,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.1960535013096028,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.13815429207957308,
            "ttft_change_pct": -0.016293752086415925
          },
          "tool-call": {
            "e2e_change_pct": -0.025134860069653264,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.7632143623954377,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.02952161506468709,
            "ttft_change_pct": -0.01988555773124734
          },
          "tool-final": {
            "e2e_change_pct": 0.046139475225026594,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.2896533466388629,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.17853668186453842,
            "ttft_change_pct": -0.001186851283363488
          }
        }
      },
      "complete": true,
      "numerical_results": [
        {
          "begin_ns": 339484793656476,
          "end_ns": 339485704297566,
          "model": "omnicoder2",
          "passed": true,
          "reference": "existing CPU reference backend",
          "returncode": 0
        },
        {
          "begin_ns": 339529942039417,
          "end_ns": 339530548773127,
          "model": "omnicoder2",
          "passed": true,
          "reference": "existing CPU reference backend",
          "returncode": 0
        }
      ]
    }
  }
}
```
