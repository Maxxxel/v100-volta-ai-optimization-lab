# Public audit excerpt

Original SHA256: `b5b72880a82c7c178bfd48d06cbdfa1b0fddda1cce229a5df18e2ca8f51ac67b`

Original file: `RESULTS.json`; 39665 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.666164508,
              "format_passes": 2,
              "gpu_energy_j": 174.5870394399696,
              "semantic_passes": 2,
              "tokens_per_s": 79.2729109940654,
              "ttft_s": 0.12364768200000001
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.658771509,
              "format_passes": 0,
              "gpu_energy_j": 451.0587435875814,
              "semantic_passes": 0,
              "tokens_per_s": 79.59852463451648,
              "ttft_s": 0.06310712
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23790376800000002,
              "format_passes": 2,
              "gpu_energy_j": 58.21489660544928,
              "semantic_passes": 2,
              "tokens_per_s": 78.23453152781448,
              "ttft_s": 0.0717101845
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2416052645,
              "format_passes": 0,
              "gpu_energy_j": 59.25228597702963,
              "semantic_passes": 0,
              "tokens_per_s": 77.48337602219034,
              "ttft_s": 0.125467339
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1821863245,
              "format_passes": 2,
              "gpu_energy_j": 42.93871647171785,
              "semantic_passes": 2,
              "tokens_per_s": 77.44602568683713,
              "ttft_s": 0.0659367275
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3579958295,
              "format_passes": 0,
              "gpu_energy_j": 90.69521023158379,
              "semantic_passes": 0,
              "tokens_per_s": 78.72071806341634,
              "ttft_s": 0.0784752825
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.46884500949999997,
              "format_passes": 0,
              "gpu_energy_j": 118.46328688229535,
              "semantic_passes": 2,
              "tokens_per_s": 79.08532872013092,
              "ttft_s": 0.1148527485
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0784175315,
              "format_passes": 2,
              "gpu_energy_j": 288.1227274906771,
              "semantic_passes": 2,
              "tokens_per_s": 77.84574729595745,
              "ttft_s": 0.8214610360000001
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23354676200000002,
              "format_passes": 0,
              "gpu_energy_j": 57.319405745539996,
              "semantic_passes": 0,
              "tokens_per_s": 78.2068489136706,
              "ttft_s": 0.067303478
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.19849035599999998,
              "format_passes": 0,
              "gpu_energy_j": 48.83346437335872,
              "semantic_passes": 0,
              "tokens_per_s": 2557.499618760072,
              "ttft_s": 0.19834433550000002
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7168362445,
              "format_passes": 0,
              "gpu_energy_j": 186.52116969687518,
              "semantic_passes": 0,
              "tokens_per_s": 2862.0686290082544,
              "ttft_s": 0.716610368
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4157863735,
              "format_passes": 0,
              "gpu_energy_j": 382.46780617990885,
              "semantic_passes": 0,
              "tokens_per_s": 2896.644588137807,
              "ttft_s": 1.415391331
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.29510061249999997,
              "format_passes": 2,
              "gpu_energy_j": 72.79658209816478,
              "semantic_passes": 2,
              "tokens_per_s": 78.60952141413935,
              "ttft_s": 0.07877840550000001
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.352667083,
              "format_passes": 2,
              "gpu_energy_j": 87.43275847488914,
              "semantic_passes": 2,
              "tokens_per_s": 78.85305930207443,
              "ttft_s": 0.0736523595
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.36901103,
              "format_passes": 2,
              "gpu_energy_j": 92.45429048941389,
              "semantic_passes": 2,
              "tokens_per_s": 78.85868996365744,
              "ttft_s": 0.0773373825
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6194964675,
              "format_passes": 0,
              "gpu_energy_j": 161.28673961629346,
              "semantic_passes": 0,
              "tokens_per_s": 78.95766315938755,
              "ttft_s": 0.31803818100000003
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5603052799999999,
              "format_passes": 0,
              "gpu_energy_j": 142.80919965178282,
              "semantic_passes": 0,
              "tokens_per_s": 78.8037592460097,
              "ttft_s": 0.25563900100000003
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
              "e2e_s": 1.9990380135,
              "format_passes": 2,
              "gpu_energy_j": 281.737758126871,
              "semantic_passes": 2,
              "tokens_per_s": 24.151193087337703,
              "ttft_s": 0.210473418
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.010580377,
              "format_passes": 0,
              "gpu_energy_j": 733.9094566974691,
              "semantic_passes": 0,
              "tokens_per_s": 26.063969718007513,
              "ttft_s": 0.1425049135
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.647625028,
              "format_passes": 2,
              "gpu_energy_j": 92.35593346786484,
              "semantic_passes": 2,
              "tokens_per_s": 27.20920135375323,
              "ttft_s": 0.1705129745
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5712948554999999,
              "format_passes": 0,
              "gpu_energy_j": 93.39450896617353,
              "semantic_passes": 0,
              "tokens_per_s": 25.378928535361176,
              "ttft_s": 0.2184251965
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5019365925,
              "format_passes": 2,
              "gpu_energy_j": 69.69998213607462,
              "semantic_passes": 2,
              "tokens_per_s": 25.423315344482106,
              "ttft_s": 0.14684854149999998
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0050736375,
              "format_passes": 0,
              "gpu_energy_j": 146.0473176777184,
              "semantic_passes": 0,
              "tokens_per_s": 26.496663551926773,
              "ttft_s": 0.176788291
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.4212342575,
              "format_passes": 0,
              "gpu_energy_j": 198.3921607876847,
              "semantic_passes": 2,
              "tokens_per_s": 24.03316907524856,
              "ttft_s": 0.2572093685
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 2.2487339635000003,
              "format_passes": 2,
              "gpu_energy_j": 397.30882977613226,
              "semantic_passes": 2,
              "tokens_per_s": 21.679265620896928,
              "ttft_s": 1.327406564
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.6381211655,
              "format_passes": 0,
              "gpu_energy_j": 90.22947838823083,
              "semantic_passes": 0,
              "tokens_per_s": 26.718078090721832,
              "ttft_s": 0.15144859449999998
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.33719532350000003,
              "format_passes": 0,
              "gpu_energy_j": 61.905770528727494,
              "semantic_passes": 0,
              "tokens_per_s": 1508.2393775006049,
              "ttft_s": 0.33706394250000005
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.1691688545,
              "format_passes": 0,
              "gpu_energy_j": 233.67424851116678,
              "semantic_passes": 0,
              "tokens_per_s": 1753.9078073181895,
              "ttft_s": 1.1689482725
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.272138129,
              "format_passes": 0,
              "gpu_energy_j": 473.5049735235699,
              "semantic_passes": 0,
              "tokens_per_s": 1804.6528031068933,
              "ttft_s": 2.2718674095
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8159694965,
              "format_passes": 2,
              "gpu_energy_j": 116.64760419407813,
              "semantic_passes": 2,
              "tokens_per_s": 25.789913011911736,
              "ttft_s": 0.159056151
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9891679065000001,
              "format_passes": 2,
              "gpu_energy_j": 142.64587470640507,
              "semantic_passes": 2,
              "tokens_per_s": 26.912089376820923,
              "ttft_s": 0.1736836095
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0466961320000001,
              "format_passes": 2,
              "gpu_energy_j": 152.31711830652787,
              "semantic_passes": 2,
              "tokens_per_s": 26.52444829622003,
              "ttft_s": 0.17938181800000003
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.710526326,
              "format_passes": 0,
              "gpu_energy_j": 253.70293336694866,
              "semantic_passes": 0,
              "tokens_per_s": 24.746193868324973,
              "ttft_s": 0.7249219835
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4481214119999999,
              "format_passes": 0,
              "gpu_energy_j": 220.03886299995588,
              "semantic_passes": 0,
              "tokens_per_s": 23.591109007748912,
              "ttft_s": 0.4239045845
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
            "e2e_change_pct": 200.08173499090108,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 61.373810467611655,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -69.53411602464587,
            "ttft_change_pct": 70.22026987938195
          },
          "decode": {
            "e2e_change_pct": 202.06573658964385,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 62.708176513812994,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -67.25571254281095,
            "ttft_change_pct": 125.81431936681628
          },
          "energy": {
            "e2e_change_pct": 172.22142526132666,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 58.64656445893222,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -65.22098257330316,
            "ttft_change_pct": 137.78069417740798
          },
          "filtering": {
            "e2e_change_pct": 136.4579499880889,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 57.62178188767238,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -67.24596960244357,
            "ttft_change_pct": 74.08928749178301
          },
          "german": {
            "e2e_change_pct": 175.50728293000935,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 62.32432607058347,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -67.17285991241886,
            "ttft_change_pct": 122.71129773615166
          },
          "ha_sim": {
            "e2e_change_pct": 180.75009669910136,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 61.03090483477236,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -66.34092751722434,
            "ttft_change_pct": 125.27894818346148
          },
          "jarvis_memory": {
            "e2e_change_pct": 203.13520005591533,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 67.47143018647319,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -69.61109037012703,
            "ttft_change_pct": 123.9470729775352
          },
          "long_context": {
            "e2e_change_pct": 108.52164378041738,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 37.89569231014174,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -72.15099555987854,
            "ttft_change_pct": 61.59093442382088
          },
          "math": {
            "e2e_change_pct": 173.23057705248766,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 57.41523697714113,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -65.83665182544965,
            "ttft_change_pct": 125.02342969556489
          },
          "prefill": {
            "e2e_change_pct": 69.87995300890088,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 26.769155789201825,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -41.026799517888875,
            "ttft_change_pct": 69.93877927005383
          },
          "prefill2048": {
            "e2e_change_pct": 63.101247107769545,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 25.28028260326827,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -38.71887663553538,
            "ttft_change_pct": 63.12187552664603
          },
          "prefill4096": {
            "e2e_change_pct": 60.48594417411943,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 23.80257001313155,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -37.69850776663397,
            "ttft_change_pct": 60.511609739398644
          },
          "pve_sim": {
            "e2e_change_pct": 176.5055245352973,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 60.237748575587105,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -67.19238007309258,
            "ttft_change_pct": 101.90323730276565
          },
          "sorting": {
            "e2e_change_pct": 180.48206203015553,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 63.149232844315705,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -65.87058306295425,
            "ttft_change_pct": 135.8154045288936
          },
          "time": {
            "e2e_change_pct": 183.64900962445486,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 64.74856656216332,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -66.36458415877311,
            "ttft_change_pct": 131.9471026834921
          },
          "tool-call": {
            "e2e_change_pct": 176.1155899569355,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 57.299312994060394,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -68.65890797911385,
            "ttft_change_pct": 127.93552057826668
          },
          "tool-final": {
            "e2e_change_pct": 158.45221590630024,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 54.078913358862835,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -70.06347256340634,
            "ttft_change_pct": 65.82156198458935
          }
        }
      },
      "complete": true
    }
  }
}
```
