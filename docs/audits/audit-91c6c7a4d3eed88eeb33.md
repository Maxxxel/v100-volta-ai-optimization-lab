# Public audit excerpt

Original SHA256: `91c6c7a4d3eed88eeb334247a9aa90ea69368fd7bc0fdb4ab7e9ef8841925079`

Original file: `RESULTS.json`; 46619 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.6669007515,
              "format_passes": 2,
              "gpu_energy_j": 179.67882820022874,
              "semantic_passes": 2,
              "tokens_per_s": 79.22592037365294,
              "ttft_s": 0.12409856699999999
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6608398580000001,
              "format_passes": 0,
              "gpu_energy_j": 461.12036988596174,
              "semantic_passes": 0,
              "tokens_per_s": 79.49175544386202,
              "ttft_s": 0.06335333400000001
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.238138045,
              "format_passes": 2,
              "gpu_energy_j": 58.421773212192114,
              "semantic_passes": 2,
              "tokens_per_s": 78.24025781608094,
              "ttft_s": 0.071910573
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.241762394,
              "format_passes": 0,
              "gpu_energy_j": 58.23525495132088,
              "semantic_passes": 0,
              "tokens_per_s": 77.54178955064852,
              "ttft_s": 0.1256524805
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.182453875,
              "format_passes": 2,
              "gpu_energy_j": 38.88832577541746,
              "semantic_passes": 2,
              "tokens_per_s": 77.47806815900658,
              "ttft_s": 0.066238457
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35850408300000003,
              "format_passes": 0,
              "gpu_energy_j": 87.48998547837951,
              "semantic_passes": 0,
              "tokens_per_s": 78.72121916974791,
              "ttft_s": 0.07896244699999999
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.470388863,
              "format_passes": 0,
              "gpu_energy_j": 118.90576607125239,
              "semantic_passes": 2,
              "tokens_per_s": 78.96255130560209,
              "ttft_s": 0.1157669975
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0826364585000001,
              "format_passes": 2,
              "gpu_energy_j": 290.32136147648424,
              "semantic_passes": 2,
              "tokens_per_s": 77.84340936791742,
              "ttft_s": 0.8256521515
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2339034665,
              "format_passes": 0,
              "gpu_energy_j": 57.20553741060838,
              "semantic_passes": 0,
              "tokens_per_s": 78.19266786236855,
              "ttft_s": 0.06766206550000001
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.20025141899999999,
              "format_passes": 0,
              "gpu_energy_j": 49.43747695385939,
              "semantic_passes": 0,
              "tokens_per_s": 2535.3252556967977,
              "ttft_s": 0.2001024985
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.721851763,
              "format_passes": 0,
              "gpu_energy_j": 191.50244232588818,
              "semantic_passes": 0,
              "tokens_per_s": 2841.9242102786257,
              "ttft_s": 0.7216195835
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4269774195,
              "format_passes": 0,
              "gpu_energy_j": 381.444264693098,
              "semantic_passes": 0,
              "tokens_per_s": 2873.8336450092406,
              "ttft_s": 1.426652245
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.296563173,
              "format_passes": 2,
              "gpu_energy_j": 71.97743505922303,
              "semantic_passes": 2,
              "tokens_per_s": 78.22099198405948,
              "ttft_s": 0.079225171
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3563792815,
              "format_passes": 2,
              "gpu_energy_j": 89.07175688001796,
              "semantic_passes": 2,
              "tokens_per_s": 78.82636328712766,
              "ttft_s": 0.07721355099999999
            },
            "template-diagnostic-code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0319513790000001,
              "format_passes": 0,
              "gpu_energy_j": 282.31163525079603,
              "semantic_passes": 0,
              "tokens_per_s": 79.4452061560018
            },
            "template-diagnostic-energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.6036456815,
              "format_passes": 0,
              "gpu_energy_j": 157.99676893677872,
              "semantic_passes": 0,
              "tokens_per_s": 78.80567814354356
            },
            "template-diagnostic-filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.7267715015,
              "format_passes": 0,
              "gpu_energy_j": 194.35288068963177,
              "semantic_passes": 0,
              "tokens_per_s": 78.66384065664138
            },
            "template-diagnostic-german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.7227184925,
              "format_passes": 0,
              "gpu_energy_j": 192.32907258422068,
              "semantic_passes": 0,
              "tokens_per_s": 79.24121804210279
            },
            "template-diagnostic-ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.829656247,
              "format_passes": 0,
              "gpu_energy_j": 213.00293303332103,
              "semantic_passes": 0,
              "tokens_per_s": 73.99739946839728
            },
            "template-diagnostic-jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.2204183044999999,
              "format_passes": 0,
              "gpu_energy_j": 324.37292162149197,
              "semantic_passes": 0,
              "tokens_per_s": 76.54114677209233
            },
            "template-diagnostic-long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.7969663040000001,
              "format_passes": 0,
              "gpu_energy_j": 486.461463482442,
              "semantic_passes": 0,
              "tokens_per_s": 75.28630601340797
            },
            "template-diagnostic-math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.599971517,
              "format_passes": 0,
              "gpu_energy_j": 157.31109818932185,
              "semantic_passes": 0,
              "tokens_per_s": 78.99466195592836
            },
            "template-diagnostic-pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0380278745,
              "format_passes": 0,
              "gpu_energy_j": 269.2946370458882,
              "semantic_passes": 0,
              "tokens_per_s": 72.22001703579798
            },
            "template-diagnostic-sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.727840598,
              "format_passes": 0,
              "gpu_energy_j": 198.6070320201066,
              "semantic_passes": 0,
              "tokens_per_s": 79.28618746864105
            },
            "template-diagnostic-time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8245761819999999,
              "format_passes": 0,
              "gpu_energy_j": 217.22172604060017,
              "semantic_passes": 0,
              "tokens_per_s": 75.74180534165114
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.369826651,
              "format_passes": 2,
              "gpu_energy_j": 95.88390852216108,
              "semantic_passes": 2,
              "tokens_per_s": 78.88993929896014,
              "ttft_s": 0.078265221
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.621910266,
              "format_passes": 0,
              "gpu_energy_j": 164.62309376533807,
              "semantic_passes": 0,
              "tokens_per_s": 78.73412163259286,
              "ttft_s": 0.32011781
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5629874735,
              "format_passes": 0,
              "gpu_energy_j": 147.05883463888313,
              "semantic_passes": 0,
              "tokens_per_s": 78.68014711499507,
              "ttft_s": 0.257887066
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
              "e2e_s": 0.6669859094999999,
              "format_passes": 2,
              "gpu_energy_j": 179.69955384150802,
              "semantic_passes": 2,
              "tokens_per_s": 79.24088791457761,
              "ttft_s": 0.124320191
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6615888965,
              "format_passes": 0,
              "gpu_energy_j": 464.15887326339816,
              "semantic_passes": 0,
              "tokens_per_s": 79.47927085273199,
              "ttft_s": 0.063062277
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23800109949999998,
              "format_passes": 2,
              "gpu_energy_j": 59.39544448145558,
              "semantic_passes": 2,
              "tokens_per_s": 78.35813887358138,
              "ttft_s": 0.07207498100000001
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2424899695,
              "format_passes": 0,
              "gpu_energy_j": 60.51920997369435,
              "semantic_passes": 0,
              "tokens_per_s": 77.11781199885861,
              "ttft_s": 0.1257963175
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1825438395,
              "format_passes": 2,
              "gpu_energy_j": 40.70440635983209,
              "semantic_passes": 2,
              "tokens_per_s": 77.43133169067949,
              "ttft_s": 0.06620681249999999
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3590536265,
              "format_passes": 0,
              "gpu_energy_j": 91.78669147079938,
              "semantic_passes": 0,
              "tokens_per_s": 78.59844673446719,
              "ttft_s": 0.07910634799999999
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4700817245,
              "format_passes": 0,
              "gpu_energy_j": 118.42341495075348,
              "semantic_passes": 2,
              "tokens_per_s": 79.02707426110996,
              "ttft_s": 0.115747247
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.086175393,
              "format_passes": 2,
              "gpu_energy_j": 291.79525181846384,
              "semantic_passes": 2,
              "tokens_per_s": 77.53170077415403,
              "ttft_s": 0.828183372
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23389674,
              "format_passes": 0,
              "gpu_energy_j": 58.66959982193798,
              "semantic_passes": 0,
              "tokens_per_s": 78.19619960501086,
              "ttft_s": 0.067636947
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.20043261099999998,
              "format_passes": 0,
              "gpu_energy_j": 48.790236016893175,
              "semantic_passes": 0,
              "tokens_per_s": 2533.127384866616,
              "ttft_s": 0.200270365
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7231748565,
              "format_passes": 0,
              "gpu_energy_j": 189.0015693578926,
              "semantic_passes": 0,
              "tokens_per_s": 2836.840429823719,
              "ttft_s": 0.7228802990000001
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4280844990000001,
              "format_passes": 0,
              "gpu_energy_j": 383.9053504924503,
              "semantic_passes": 0,
              "tokens_per_s": 2871.551532321015,
              "ttft_s": 1.4277739455
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2969074895,
              "format_passes": 2,
              "gpu_energy_j": 70.682802606547,
              "semantic_passes": 2,
              "tokens_per_s": 78.18493825316841,
              "ttft_s": 0.07946646
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35542869099999996,
              "format_passes": 2,
              "gpu_energy_j": 91.82928209379898,
              "semantic_passes": 2,
              "tokens_per_s": 78.755851044732,
              "ttft_s": 0.076037758
            },
            "template-diagnostic-code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.6209867155,
              "format_passes": 0,
              "gpu_energy_j": 431.6758391819236,
              "semantic_passes": 0,
              "tokens_per_s": 73.80214290735177
            },
            "template-diagnostic-energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5766746315,
              "format_passes": 0,
              "gpu_energy_j": 157.31982126797158,
              "semantic_passes": 0,
              "tokens_per_s": 79.04059258123053
            },
            "template-diagnostic-filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.855191596,
              "format_passes": 0,
              "gpu_energy_j": 227.72735728115623,
              "semantic_passes": 0,
              "tokens_per_s": 74.56284920523477
            },
            "template-diagnostic-german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.6976578689999999,
              "format_passes": 0,
              "gpu_energy_j": 186.22056846425227,
              "semantic_passes": 0,
              "tokens_per_s": 79.30981257620412
            },
            "template-diagnostic-ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.7916353955,
              "format_passes": 0,
              "gpu_energy_j": 207.0110333430123,
              "semantic_passes": 0,
              "tokens_per_s": 75.00997668957842
            },
            "template-diagnostic-jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.2009017885,
              "format_passes": 0,
              "gpu_energy_j": 319.83432725274776,
              "semantic_passes": 0,
              "tokens_per_s": 75.94870897717094
            },
            "template-diagnostic-long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.769097213,
              "format_passes": 0,
              "gpu_energy_j": 474.82853615534475,
              "semantic_passes": 0,
              "tokens_per_s": 75.27058997884781
            },
            "template-diagnostic-math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5733594455,
              "format_passes": 0,
              "gpu_energy_j": 151.8436415628488,
              "semantic_passes": 0,
              "tokens_per_s": 79.18879656448905
            },
            "template-diagnostic-pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.740654286,
              "format_passes": 0,
              "gpu_energy_j": 194.2166484711784,
              "semantic_passes": 0,
              "tokens_per_s": 74.74004354075252
            },
            "template-diagnostic-sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.7058702859999999,
              "format_passes": 0,
              "gpu_energy_j": 191.02013559842192,
              "semantic_passes": 0,
              "tokens_per_s": 78.66575305482345
            },
            "template-diagnostic-time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.135392735,
              "format_passes": 0,
              "gpu_energy_j": 302.9246058346115,
              "semantic_passes": 0,
              "tokens_per_s": 74.03320622159055
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.36934206999999997,
              "format_passes": 2,
              "gpu_energy_j": 96.08238736698459,
              "semantic_passes": 2,
              "tokens_per_s": 78.88818494880302,
              "ttft_s": 0.07772955200000001
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6229814765,
              "format_passes": 0,
              "gpu_energy_j": 161.76620351932416,
              "semantic_passes": 0,
              "tokens_per_s": 78.720344048076,
              "ttft_s": 0.32092262250000003
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5639304254999999,
              "format_passes": 0,
              "gpu_energy_j": 147.20679098360029,
              "semantic_passes": 0,
              "tokens_per_s": 78.6806783082109,
              "ttft_s": 0.25874624599999996
            }
          }
        }
      },
      "change_exercised": false,
      "complete": true,
      "template": {
        "arms": {
          "A": {
            "format_passes": 18,
            "questions": 24,
            "semantic_passes": 18,
            "starts": 2
          },
          "B": {
            "format_passes": 18,
            "questions": 24,
            "semantic_passes": 18,
            "starts": 2
          }
        },
        "change_exercised": false,
        "note": "Await independent native source/render/grammar replay. Actual copied template only; original12 common quality precedes12diagnostic+12timed candidate requests. E2E is ordinary buffered generation, no invented TTFT. Different prompt/output work is intentional; no token/s or unchanged-kernel speed claim.",
        "original_quality": {
          "A": {
            "attempts": 24,
            "passes": 18
          },
          "B": {
            "attempts": 24,
            "passes": 18
          }
        }
      }
    }
  }
}
```
