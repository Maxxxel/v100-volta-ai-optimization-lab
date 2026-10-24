# Public audit excerpt

Original SHA256: `e85dccde79ca45a94d6b89d5584c1a6c955c2c5433833da3e0cb0fc30eaa8fc7`

Original file: `RESULTS.json`; 39685 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.666551794,
              "format_passes": 2,
              "gpu_energy_j": 178.5755238514285,
              "semantic_passes": 2,
              "tokens_per_s": 79.3299357415022,
              "ttft_s": 0.12446165949999999
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.659602221,
              "format_passes": 0,
              "gpu_energy_j": 460.00082343437015,
              "semantic_passes": 0,
              "tokens_per_s": 79.66997809417481,
              "ttft_s": 0.0654219785
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.239220835,
              "format_passes": 2,
              "gpu_energy_j": 55.24955450705039,
              "semantic_passes": 2,
              "tokens_per_s": 78.11788465549841,
              "ttft_s": 0.0727220355
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2420260135,
              "format_passes": 0,
              "gpu_energy_j": 59.13822400873439,
              "semantic_passes": 0,
              "tokens_per_s": 77.57952490975703,
              "ttft_s": 0.1259816755
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1828017905,
              "format_passes": 2,
              "gpu_energy_j": 42.105498873951134,
              "semantic_passes": 2,
              "tokens_per_s": 77.67393875440605,
              "ttft_s": 0.0668935755
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.358060535,
              "format_passes": 0,
              "gpu_energy_j": 92.58369955974874,
              "semantic_passes": 0,
              "tokens_per_s": 78.97533102830091,
              "ttft_s": 0.0794375495
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.468961922,
              "format_passes": 0,
              "gpu_energy_j": 118.88965471836156,
              "semantic_passes": 2,
              "tokens_per_s": 79.188004083103,
              "ttft_s": 0.11534235600000001
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.2783401935,
              "format_passes": 2,
              "gpu_energy_j": 346.71906989078855,
              "semantic_passes": 2,
              "tokens_per_s": 78.10332184232303,
              "ttft_s": 1.0222176375
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.233901367,
              "format_passes": 0,
              "gpu_energy_j": 56.03594399859687,
              "semantic_passes": 0,
              "tokens_per_s": 78.2677944997177,
              "ttft_s": 0.0677927485
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.258608116,
              "format_passes": 0,
              "gpu_energy_j": 62.16474909257129,
              "semantic_passes": 0,
              "tokens_per_s": 1961.200092746706,
              "ttft_s": 0.258478564
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.9157373719999999,
              "format_passes": 0,
              "gpu_energy_j": 247.792398159057,
              "semantic_passes": 0,
              "tokens_per_s": 2239.6174991828357,
              "ttft_s": 0.915481447
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.813218368,
              "format_passes": 0,
              "gpu_energy_j": 500.3828177092245,
              "semantic_passes": 0,
              "tokens_per_s": 2261.0440482863205,
              "ttft_s": 1.8129309894999999
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2956919025,
              "format_passes": 2,
              "gpu_energy_j": 74.04099214967815,
              "semantic_passes": 2,
              "tokens_per_s": 78.58129459593547,
              "ttft_s": 0.079305122
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3536329825,
              "format_passes": 2,
              "gpu_energy_j": 91.10673234890226,
              "semantic_passes": 2,
              "tokens_per_s": 78.81398062622688,
              "ttft_s": 0.0744613495
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3697839885,
              "format_passes": 2,
              "gpu_energy_j": 93.20979298704178,
              "semantic_passes": 2,
              "tokens_per_s": 78.88253479258115,
              "ttft_s": 0.0781784465
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.657619416,
              "format_passes": 0,
              "gpu_energy_j": 171.38255908426103,
              "semantic_passes": 0,
              "tokens_per_s": 79.0647378796379,
              "ttft_s": 0.356018944
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6462428929999999,
              "format_passes": 0,
              "gpu_energy_j": 170.62057304820223,
              "semantic_passes": 0,
              "tokens_per_s": 78.86811307965722,
              "ttft_s": 0.34199095150000003
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
              "e2e_s": 0.6678446785000001,
              "format_passes": 2,
              "gpu_energy_j": 183.6712010589274,
              "semantic_passes": 2,
              "tokens_per_s": 79.07758801149792,
              "ttft_s": 0.1240508975
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6599342049999999,
              "format_passes": 0,
              "gpu_energy_j": 464.935861341007,
              "semantic_passes": 0,
              "tokens_per_s": 79.65318893799858,
              "ttft_s": 0.06538638999999999
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23819493,
              "format_passes": 2,
              "gpu_energy_j": 58.1045452671548,
              "semantic_passes": 2,
              "tokens_per_s": 78.37442926493028,
              "ttft_s": 0.0722752995
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.242014059,
              "format_passes": 0,
              "gpu_energy_j": 60.828113799374556,
              "semantic_passes": 0,
              "tokens_per_s": 77.66594514366247,
              "ttft_s": 0.12611663550000002
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.182624443,
              "format_passes": 2,
              "gpu_energy_j": 41.107395107243136,
              "semantic_passes": 2,
              "tokens_per_s": 77.48732065494991,
              "ttft_s": 0.06642157000000001
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.361957313,
              "format_passes": 0,
              "gpu_energy_j": 93.30108327828148,
              "semantic_passes": 0,
              "tokens_per_s": 78.74300398562816,
              "ttft_s": 0.0825045435
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4707570835,
              "format_passes": 0,
              "gpu_energy_j": 121.77360035056213,
              "semantic_passes": 2,
              "tokens_per_s": 78.71930297634749,
              "ttft_s": 0.1150029135
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.2767289355,
              "format_passes": 2,
              "gpu_energy_j": 342.59112098349965,
              "semantic_passes": 2,
              "tokens_per_s": 78.23565093004333,
              "ttft_s": 1.0210453605
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23376701449999998,
              "format_passes": 0,
              "gpu_energy_j": 58.65172788477923,
              "semantic_passes": 0,
              "tokens_per_s": 78.16671533534443,
              "ttft_s": 0.067428062
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.258798466,
              "format_passes": 0,
              "gpu_energy_j": 63.24850206970278,
              "semantic_passes": 0,
              "tokens_per_s": 1959.6696528432433,
              "ttft_s": 0.25866873
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.9135919735,
              "format_passes": 0,
              "gpu_energy_j": 248.10945419113466,
              "semantic_passes": 0,
              "tokens_per_s": 2244.730437195678,
              "ttft_s": 0.9133491515000001
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.811379004,
              "format_passes": 0,
              "gpu_energy_j": 498.0188717590779,
              "semantic_passes": 0,
              "tokens_per_s": 2263.394965263902,
              "ttft_s": 1.8110622415
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.29534702749999997,
              "format_passes": 2,
              "gpu_energy_j": 75.68429238104247,
              "semantic_passes": 2,
              "tokens_per_s": 78.82924725587485,
              "ttft_s": 0.0796212035
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.354115187,
              "format_passes": 2,
              "gpu_energy_j": 89.59754203822952,
              "semantic_passes": 2,
              "tokens_per_s": 78.66541136961382,
              "ttft_s": 0.0744543335
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3697077085,
              "format_passes": 2,
              "gpu_energy_j": 93.65534261102667,
              "semantic_passes": 2,
              "tokens_per_s": 78.91090988185968,
              "ttft_s": 0.0782530065
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.657845384,
              "format_passes": 0,
              "gpu_energy_j": 170.2733361774196,
              "semantic_passes": 0,
              "tokens_per_s": 79.0910844851835,
              "ttft_s": 0.3564768765
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.646154008,
              "format_passes": 0,
              "gpu_energy_j": 173.32218449718448,
              "semantic_passes": 0,
              "tokens_per_s": 78.83624949670656,
              "ttft_s": 0.3417848865
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
            "e2e_change_pct": 0.19396609710424784,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.853513794946738,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.3180989971132142,
            "ttft_change_pct": -0.33003095222265966
          },
          "decode": {
            "e2e_change_pct": 0.020003829580295118,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.0728324070795825,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.02107337867770509,
            "ttft_change_pct": -0.05439838539890163
          },
          "energy": {
            "e2e_change_pct": -0.4288526958782679,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 5.167445756942857,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.3284070102041792,
            "ttft_change_pct": -0.6143062373439756
          },
          "filtering": {
            "e2e_change_pct": -0.00493934508407623,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.857525431251662,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.11139567302838049,
            "ttft_change_pct": 0.1071266908178492
          },
          "german": {
            "e2e_change_pct": -0.09701628168681253,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.3704831753590283,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.240258318876041,
            "ttft_change_pct": -0.7056066243610881
          },
          "ha_sim": {
            "e2e_change_pct": 1.0883014515967293,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.774848836181774,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.29417672537452866,
            "ttft_change_pct": 3.8608869726022954
          },
          "jarvis_memory": {
            "e2e_change_pct": 0.38279472506939083,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.425733037102651,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.5918839755875482,
            "ttft_change_pct": -0.2942912835940392
          },
          "long_context": {
            "e2e_change_pct": -0.1260429741779867,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.190574521496368,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.1694282453023721,
            "ttft_change_pct": -0.11467978608420415
          },
          "math": {
            "e2e_change_pct": -0.05743980966131934,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.668046435066486,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.12914528257675917,
            "ttft_change_pct": -0.5379432285445684
          },
          "prefill": {
            "e2e_change_pct": 0.07360557856583849,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.7433561511165152,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.07803588777722803,
            "ttft_change_pct": 0.07357128461917828
          },
          "prefill2048": {
            "e2e_change_pct": -0.23428098116322627,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.1279522836185487,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.22829514480520174,
            "ttft_change_pct": -0.23291520619969086
          },
          "prefill4096": {
            "e2e_change_pct": -0.10144194612526913,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.47242748281582925,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.10397484203650276,
            "ttft_change_pct": -0.10307882709398308
          },
          "pve_sim": {
            "e2e_change_pct": -0.11663322434066759,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.2194465304331557,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.3155364914950054,
            "ttft_change_pct": 0.39856379011684595
          },
          "sorting": {
            "e2e_change_pct": 0.1363573319974387,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.6565080008501876,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.18850622114576776,
            "ttft_change_pct": -0.009422337960718341
          },
          "time": {
            "e2e_change_pct": -0.02062825930062573,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.47800730986156115,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.035971320334904355,
            "ttft_change_pct": 0.09537155486967208
          },
          "tool-call": {
            "e2e_change_pct": 0.034361515871061954,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.6472204130737014,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.03332282665087227,
            "ttft_change_pct": 0.1286258800879958
          },
          "tool-final": {
            "e2e_change_pct": -0.013754116441777597,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.5834031035747431,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.040401097105591255,
            "ttft_change_pct": -0.060254518166702464
          }
        }
      },
      "complete": true
    }
  }
}
```

</details>
