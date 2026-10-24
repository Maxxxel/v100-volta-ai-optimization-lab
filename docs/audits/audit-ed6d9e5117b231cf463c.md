# Public audit excerpt

Original SHA256: `ed6d9e5117b231cf463cf542b3df0840d59407ab3357606476118ac94de2298e`

Original file: `RESULTS.json`; 39720 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.666876561,
              "format_passes": 2,
              "gpu_energy_j": 178.48114728358667,
              "semantic_passes": 2,
              "tokens_per_s": 79.2493559120973,
              "ttft_s": 0.12425407699999999
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6593284750000001,
              "format_passes": 0,
              "gpu_energy_j": 454.9213480127404,
              "semantic_passes": 0,
              "tokens_per_s": 79.59158906065562,
              "ttft_s": 0.063315198
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23820353049999998,
              "format_passes": 2,
              "gpu_energy_j": 57.887939695667995,
              "semantic_passes": 2,
              "tokens_per_s": 78.21902180301743,
              "ttft_s": 0.071979399
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.241880714,
              "format_passes": 0,
              "gpu_energy_j": 58.54960907484101,
              "semantic_passes": 0,
              "tokens_per_s": 77.45222388465149,
              "ttft_s": 0.12569091500000001
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1829317925,
              "format_passes": 2,
              "gpu_energy_j": 43.18282045047363,
              "semantic_passes": 2,
              "tokens_per_s": 77.33088262282583,
              "ttft_s": 0.066523255
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.358695381,
              "format_passes": 0,
              "gpu_energy_j": 87.52539774632562,
              "semantic_passes": 0,
              "tokens_per_s": 78.6914687442655,
              "ttft_s": 0.079043647
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.469888751,
              "format_passes": 0,
              "gpu_energy_j": 117.13663097291231,
              "semantic_passes": 2,
              "tokens_per_s": 78.98955756288318,
              "ttft_s": 0.1154067605
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.079106151,
              "format_passes": 2,
              "gpu_energy_j": 287.9298735932283,
              "semantic_passes": 2,
              "tokens_per_s": 77.91775338974546,
              "ttft_s": 0.822309696
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.234205618,
              "format_passes": 0,
              "gpu_energy_j": 58.78312029641668,
              "semantic_passes": 0,
              "tokens_per_s": 78.20334554025526,
              "ttft_s": 0.067906821
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.19878823099999998,
              "format_passes": 0,
              "gpu_energy_j": 47.55171895099344,
              "semantic_passes": 0,
              "tokens_per_s": 2553.8525470832633,
              "ttft_s": 0.1986593735
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.719422237,
              "format_passes": 0,
              "gpu_energy_j": 189.54694768670106,
              "semantic_passes": 0,
              "tokens_per_s": 2851.667517916525,
              "ttft_s": 0.7191995520000001
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4168305345,
              "format_passes": 0,
              "gpu_energy_j": 380.5839064146307,
              "semantic_passes": 0,
              "tokens_per_s": 2894.468977822896,
              "ttft_s": 1.416507621
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2957170485,
              "format_passes": 2,
              "gpu_energy_j": 71.93373607933486,
              "semantic_passes": 2,
              "tokens_per_s": 78.62689970126131,
              "ttft_s": 0.0794731845
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35401074499999996,
              "format_passes": 2,
              "gpu_energy_j": 87.31696193242846,
              "semantic_passes": 2,
              "tokens_per_s": 78.7913555061755,
              "ttft_s": 0.0747700815
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.37042232799999997,
              "format_passes": 2,
              "gpu_energy_j": 91.98632677456594,
              "semantic_passes": 2,
              "tokens_per_s": 78.65884809719734,
              "ttft_s": 0.07802866750000001
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6196072225,
              "format_passes": 0,
              "gpu_energy_j": 162.19383391257293,
              "semantic_passes": 0,
              "tokens_per_s": 79.02167778560974,
              "ttft_s": 0.318417857
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.561530239,
              "format_passes": 0,
              "gpu_energy_j": 146.2281403808572,
              "semantic_passes": 0,
              "tokens_per_s": 78.78009695002304,
              "ttft_s": 0.2564241325
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
              "e2e_s": 0.6671068475,
              "format_passes": 2,
              "gpu_energy_j": 177.839020552911,
              "semantic_passes": 2,
              "tokens_per_s": 79.19269696458397,
              "ttft_s": 0.1241144465
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6588510520000002,
              "format_passes": 0,
              "gpu_energy_j": 455.56156797701885,
              "semantic_passes": 0,
              "tokens_per_s": 79.624826311001,
              "ttft_s": 0.06347632950000001
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23817617200000002,
              "format_passes": 2,
              "gpu_energy_j": 54.33984519962239,
              "semantic_passes": 2,
              "tokens_per_s": 78.27390511493743,
              "ttft_s": 0.07204502
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2420667595,
              "format_passes": 0,
              "gpu_energy_j": 60.52549105424198,
              "semantic_passes": 0,
              "tokens_per_s": 77.39542225676374,
              "ttft_s": 0.125726411
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.18291647049999998,
              "format_passes": 2,
              "gpu_energy_j": 43.095263965574155,
              "semantic_passes": 2,
              "tokens_per_s": 77.56851679590994,
              "ttft_s": 0.06686534
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35863858849999997,
              "format_passes": 0,
              "gpu_energy_j": 88.60682883020729,
              "semantic_passes": 0,
              "tokens_per_s": 78.71977103523068,
              "ttft_s": 0.0791698265
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.469695838,
              "format_passes": 0,
              "gpu_energy_j": 118.43819234013436,
              "semantic_passes": 2,
              "tokens_per_s": 79.06316262320406,
              "ttft_s": 0.1154701735
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.081287092,
              "format_passes": 2,
              "gpu_energy_j": 285.2865539291531,
              "semantic_passes": 2,
              "tokens_per_s": 78.00605665005922,
              "ttft_s": 0.8248766865
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.233965928,
              "format_passes": 0,
              "gpu_energy_j": 57.917202117491215,
              "semantic_passes": 0,
              "tokens_per_s": 78.18603967748777,
              "ttft_s": 0.067689995
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.199569297,
              "format_passes": 0,
              "gpu_energy_j": 47.79194200954714,
              "semantic_passes": 0,
              "tokens_per_s": 2544.3585830997986,
              "ttft_s": 0.19943252350000001
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7175791825,
              "format_passes": 0,
              "gpu_energy_j": 190.88035398916583,
              "semantic_passes": 0,
              "tokens_per_s": 2858.920299064234,
              "ttft_s": 0.7173388705
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4124076225,
              "format_passes": 0,
              "gpu_energy_j": 383.7035244372311,
              "semantic_passes": 0,
              "tokens_per_s": 2903.660233555165,
              "ttft_s": 1.4120212515000001
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2960468595,
              "format_passes": 2,
              "gpu_energy_j": 74.1651019650326,
              "semantic_passes": 2,
              "tokens_per_s": 78.57710919378323,
              "ttft_s": 0.07963503899999999
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3539462535,
              "format_passes": 2,
              "gpu_energy_j": 89.32905506062133,
              "semantic_passes": 2,
              "tokens_per_s": 78.732480922484,
              "ttft_s": 0.074504231
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.369730515,
              "format_passes": 2,
              "gpu_energy_j": 94.117854064358,
              "semantic_passes": 2,
              "tokens_per_s": 78.88176605600407,
              "ttft_s": 0.078146389
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6204072135,
              "format_passes": 0,
              "gpu_energy_j": 164.3666713229436,
              "semantic_passes": 0,
              "tokens_per_s": 78.87252181394209,
              "ttft_s": 0.31883693550000003
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.561303145,
              "format_passes": 0,
              "gpu_energy_j": 145.63931671030144,
              "semantic_passes": 0,
              "tokens_per_s": 78.78371445350619,
              "ttft_s": 0.25627814000000004
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
            "e2e_change_pct": 0.034532102860929115,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.35977286141902765,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.07149452113677235,
            "ttft_change_pct": -0.1123749846856037
          },
          "decode": {
            "e2e_change_pct": -0.02877206093868656,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.1407320116048938,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.04175975217688421,
            "ttft_change_pct": 0.2544910307316961
          },
          "energy": {
            "e2e_change_pct": -0.01148534614182628,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -6.1292464625600225,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.0701661957090538,
            "ttft_change_pct": 0.09116636275332546
          },
          "filtering": {
            "e2e_change_pct": 0.07691621912444546,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.3747142135061914,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.07333763323871256,
            "ttft_change_pct": 0.028240704588711196
          },
          "german": {
            "e2e_change_pct": -0.008375799411686202,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.20275767998964023,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.3072953068997686,
            "ttft_change_pct": 0.5142337066939895
          },
          "ha_sim": {
            "e2e_change_pct": -0.01583307257586597,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.2355626043722534,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.035966149084276644,
            "ttft_change_pct": 0.15963269002505776
          },
          "jarvis_memory": {
            "e2e_change_pct": -0.04105503687616974,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.1111480297935517,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.09318327965350814,
            "ttft_change_pct": 0.05494738759259654
          },
          "long_context": {
            "e2e_change_pct": 0.20210625228842538,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.918042866163149,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.11332880694348013,
            "ttft_change_pct": 0.3121683366360317
          },
          "math": {
            "e2e_change_pct": -0.10234169532176152,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.4730728388677505,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.022129312560648096,
            "ttft_change_pct": -0.3192992939545891
          },
          "prefill": {
            "e2e_change_pct": 0.3929136026166624,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.5051827018099475,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.37175067113047744,
            "ttft_change_pct": 0.38918375024474816
          },
          "prefill2048": {
            "e2e_change_pct": -0.2561853672588099,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.7034702055285669,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.2543347393109796,
            "ttft_change_pct": -0.258715608877369
          },
          "prefill4096": {
            "e2e_change_pct": -0.31216944386089907,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.8196925750196371,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.3175454911658049,
            "ttft_change_pct": -0.3167204633062748
          },
          "pve_sim": {
            "e2e_change_pct": 0.11152924786477225,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.1019741324665784,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.06332502956017949,
            "ttft_change_pct": 0.20365926069061402
          },
          "sorting": {
            "e2e_change_pct": -0.018217384898866484,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.3043554009013256,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.07472213583999965,
            "ttft_change_pct": -0.3555573227508102
          },
          "time": {
            "e2e_change_pct": -0.18676330979702227,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.3172218790906474,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.2833984531928069,
            "ttft_change_pct": 0.15086955060457097
          },
          "tool-call": {
            "e2e_change_pct": 0.129112600846093,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.3396547562602779,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.18875323309677228,
            "ttft_change_pct": 0.1316127506002296
          },
          "tool-final": {
            "e2e_change_pct": -0.040441989447337345,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.4026746623612576,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.004591900268224869,
            "ttft_change_pct": -0.05693399391727416
          }
        }
      },
      "complete": true
    }
  }
}
```

</details>
