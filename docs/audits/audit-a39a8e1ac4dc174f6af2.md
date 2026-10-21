# Public audit excerpt

Original SHA256: `a39a8e1ac4dc174f6af2c63a034fc4845e17fedce86e6b4e6cac53c95cfce3a2`

Original file: `RESULTS.json`; 39701 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.665799755,
              "format_passes": 2,
              "gpu_energy_j": 177.16354007173862,
              "semantic_passes": 2,
              "tokens_per_s": 79.32615413435373,
              "ttft_s": 0.12365884099999999
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6588645755,
              "format_passes": 0,
              "gpu_energy_j": 457.33449412254606,
              "semantic_passes": 0,
              "tokens_per_s": 79.57752492859217,
              "ttft_s": 0.06297755699999999
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23775099249999998,
              "format_passes": 2,
              "gpu_energy_j": 57.48898525879166,
              "semantic_passes": 2,
              "tokens_per_s": 78.23801733114907,
              "ttft_s": 0.07154914000000001
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2424777355,
              "format_passes": 0,
              "gpu_energy_j": 58.375736838503244,
              "semantic_passes": 0,
              "tokens_per_s": 77.03806689524595,
              "ttft_s": 0.1255539625
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1819127075,
              "format_passes": 2,
              "gpu_energy_j": 40.60603689749996,
              "semantic_passes": 2,
              "tokens_per_s": 77.54180879878183,
              "ttft_s": 0.0658358875
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3578451545,
              "format_passes": 0,
              "gpu_energy_j": 87.5677004363239,
              "semantic_passes": 0,
              "tokens_per_s": 78.96725505556122,
              "ttft_s": 0.0792027325
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4691101595,
              "format_passes": 0,
              "gpu_energy_j": 116.55616603472225,
              "semantic_passes": 2,
              "tokens_per_s": 79.05540240869558,
              "ttft_s": 0.114923851
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.078790046,
              "format_passes": 2,
              "gpu_energy_j": 291.76958772504497,
              "semantic_passes": 2,
              "tokens_per_s": 78.01687874253375,
              "ttft_s": 0.8224032299999999
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23405227350000002,
              "format_passes": 0,
              "gpu_energy_j": 56.53609272568733,
              "semantic_passes": 0,
              "tokens_per_s": 78.00409985544346,
              "ttft_s": 0.0674071035
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.19833476449999998,
              "format_passes": 0,
              "gpu_energy_j": 49.3807803532783,
              "semantic_passes": 0,
              "tokens_per_s": 2559.677729029257,
              "ttft_s": 0.19819127549999999
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.720231818,
              "format_passes": 0,
              "gpu_energy_j": 188.96716924341507,
              "semantic_passes": 0,
              "tokens_per_s": 2848.488552637997,
              "ttft_s": 0.719988262
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4197514249999998,
              "format_passes": 0,
              "gpu_energy_j": 380.88503719735263,
              "semantic_passes": 0,
              "tokens_per_s": 2888.586839531392,
              "ttft_s": 1.4194095789999999
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.29546364049999996,
              "format_passes": 2,
              "gpu_energy_j": 72.12315382387717,
              "semantic_passes": 2,
              "tokens_per_s": 78.50164854294626,
              "ttft_s": 0.07888606100000001
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3527638335,
              "format_passes": 2,
              "gpu_energy_j": 87.61988030583782,
              "semantic_passes": 2,
              "tokens_per_s": 78.8106761744273,
              "ttft_s": 0.07357013200000001
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.36959108549999997,
              "format_passes": 2,
              "gpu_energy_j": 94.11087767885107,
              "semantic_passes": 2,
              "tokens_per_s": 78.77319729955914,
              "ttft_s": 0.0775839095
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6194336145,
              "format_passes": 0,
              "gpu_energy_j": 162.0900052127447,
              "semantic_passes": 0,
              "tokens_per_s": 79.05507753282816,
              "ttft_s": 0.31847981999999997
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.560137452,
              "format_passes": 0,
              "gpu_energy_j": 144.62914279581753,
              "semantic_passes": 0,
              "tokens_per_s": 78.83520982341368,
              "ttft_s": 0.2557112625
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
              "e2e_s": 0.6657476415,
              "format_passes": 2,
              "gpu_energy_j": 172.01026840310212,
              "semantic_passes": 2,
              "tokens_per_s": 79.35807890458241,
              "ttft_s": 0.12399188
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6593109670000001,
              "format_passes": 0,
              "gpu_energy_j": 460.14197673194326,
              "semantic_passes": 0,
              "tokens_per_s": 79.65399558590269,
              "ttft_s": 0.064717845
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2375106155,
              "format_passes": 2,
              "gpu_energy_j": 57.375847754911945,
              "semantic_passes": 2,
              "tokens_per_s": 78.36779496081844,
              "ttft_s": 0.071568184
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2422289555,
              "format_passes": 0,
              "gpu_energy_j": 60.20792665405024,
              "semantic_passes": 0,
              "tokens_per_s": 77.4707486706319,
              "ttft_s": 0.1259847765
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1823162345,
              "format_passes": 2,
              "gpu_energy_j": 36.8880238033054,
              "semantic_passes": 2,
              "tokens_per_s": 77.37309737547268,
              "ttft_s": 0.06593148
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.358304516,
              "format_passes": 0,
              "gpu_energy_j": 90.46903475044454,
              "semantic_passes": 0,
              "tokens_per_s": 78.76163823410674,
              "ttft_s": 0.078952466
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4688393025,
              "format_passes": 0,
              "gpu_energy_j": 117.70661686646304,
              "semantic_passes": 2,
              "tokens_per_s": 79.12812666973963,
              "ttft_s": 0.1149730115
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.276421541,
              "format_passes": 2,
              "gpu_energy_j": 346.04422333579043,
              "semantic_passes": 2,
              "tokens_per_s": 78.27678768048914,
              "ttft_s": 1.020845675
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.233517153,
              "format_passes": 0,
              "gpu_energy_j": 50.561165955072795,
              "semantic_passes": 0,
              "tokens_per_s": 78.19819521423116,
              "ttft_s": 0.0672418685
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.25784763200000005,
              "format_passes": 0,
              "gpu_energy_j": 60.85715481148358,
              "semantic_passes": 0,
              "tokens_per_s": 1966.5348647431856,
              "ttft_s": 0.2577178295
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.9143635215,
              "format_passes": 0,
              "gpu_energy_j": 245.78060302679725,
              "semantic_passes": 0,
              "tokens_per_s": 2242.863344195801,
              "ttft_s": 0.914132881
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.8125747295,
              "format_passes": 0,
              "gpu_energy_j": 502.08278006850844,
              "semantic_passes": 0,
              "tokens_per_s": 2261.924944650113,
              "ttft_s": 1.8122232770000002
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2950710635,
              "format_passes": 2,
              "gpu_energy_j": 71.4761679326912,
              "semantic_passes": 2,
              "tokens_per_s": 78.67202091963252,
              "ttft_s": 0.0789251415
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3525462195,
              "format_passes": 2,
              "gpu_energy_j": 86.58408692733644,
              "semantic_passes": 2,
              "tokens_per_s": 78.90724453346559,
              "ttft_s": 0.0736397385
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.369749184,
              "format_passes": 2,
              "gpu_energy_j": 90.39774080322081,
              "semantic_passes": 2,
              "tokens_per_s": 79.03255006577058,
              "ttft_s": 0.07870416699999999
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.657208114,
              "format_passes": 0,
              "gpu_energy_j": 172.32522488169337,
              "semantic_passes": 0,
              "tokens_per_s": 79.05915134749787,
              "ttft_s": 0.3557850855
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.645290843,
              "format_passes": 0,
              "gpu_energy_j": 170.82740329595396,
              "semantic_passes": 0,
              "tokens_per_s": 78.76031280058257,
              "ttft_s": 0.34061914449999997
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
            "e2e_change_pct": -0.007827203240706737,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.9087653512397615,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.04024494894157016,
            "ttft_change_pct": 0.26932081629327254
          },
          "decode": {
            "e2e_change_pct": 0.026909460036272925,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.6138794789104507,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.09609579762519527,
            "ttft_change_pct": 2.76334631398929
          },
          "energy": {
            "e2e_change_pct": -0.1011045200999483,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.1967985751886503,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.16587540699053438,
            "ttft_change_pct": 0.026616672122115048
          },
          "filtering": {
            "e2e_change_pct": -0.10259911058927429,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.1386153130979144,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.5616467193735541,
            "ttft_change_pct": 0.3431305483488911
          },
          "german": {
            "e2e_change_pct": 0.2218245253702289,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -9.156306249683455,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.21757478439399236,
            "ttft_change_pct": 0.14519816414717557
          },
          "ha_sim": {
            "e2e_change_pct": 0.12836879142372748,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.3132471215575388,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.2603823842044606,
            "ttft_change_pct": -0.31598215377227623
          },
          "jarvis_memory": {
            "e2e_change_pct": -0.057738463879930535,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.9870355819683319,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.0919915133289484,
            "ttft_change_pct": 0.042776586036952224
          },
          "long_context": {
            "e2e_change_pct": 18.31973660980555,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 18.60188240794043,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.3331444966071073,
            "ttft_change_pct": 24.129579962860802
          },
          "math": {
            "e2e_change_pct": -0.22863289982099078,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -10.56834047518076,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.24882712466063328,
            "ttft_change_pct": -0.2451299513262728
          },
          "prefill": {
            "e2e_change_pct": 30.00627129088107,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 23.240569258123102,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -23.172560262538113,
            "ttft_change_pct": 30.03490130926576
          },
          "prefill2048": {
            "e2e_change_pct": 26.954058214073505,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 30.065240438776364,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -21.261282861092212,
            "ttft_change_pct": 26.964970020580694
          },
          "prefill4096": {
            "e2e_change_pct": 27.66845643419589,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 31.820032564933264,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -21.694410786104,
            "ttft_change_pct": 27.67444322002848
          },
          "pve_sim": {
            "e2e_change_pct": -0.13286812527443237,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.8970571264339089,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.2170303170041743,
            "ttft_change_pct": 0.04954043782208206
          },
          "sorting": {
            "e2e_change_pct": -0.0616882966263721,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.1821442518363812,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.12253207779178155,
            "ttft_change_pct": 0.09461244408259795
          },
          "time": {
            "e2e_change_pct": 0.04277659992424354,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.945491708515525,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.3292398621642434,
            "ttft_change_pct": 1.4439302005011534
          },
          "tool-call": {
            "e2e_change_pct": 6.098232097153966,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 6.314528558077881,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.005153134747115651,
            "ttft_change_pct": 11.713541379168092
          },
          "tool-final": {
            "e2e_change_pct": 15.20223129090108,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 18.11409512197846,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.09500453287163424,
            "ttft_change_pct": 33.20459223026988
          }
        }
      },
      "complete": true
    }
  }
}
```
