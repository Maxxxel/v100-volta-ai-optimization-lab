# HBM17 — Speculative decoding memory traffic

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| PARTIAL | True | True | P2 |


## Theory and Volta implications

MTP proposes tokens with model-compatible prediction heads. State rollback and target verification must be tested; do not assume identical decisions.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://docs.nvidia.com/cuda/volta-tuning-guide/index.html
- https://github.com/ggml-org/llama.cpp

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Relevanter OmniCoder2-/SM70-Modell- oder numerischer Komponentenpfad; kein Beweis vollständiger Achsenabdeckung.

- [Original audit hash and public excerpt](../audits/audit-005e431f9699e2f9139e.md)
- [Original audit hash and public excerpt](../audits/audit-058f7fb472328b4ccdee.md)
- [Original audit hash and public excerpt](../audits/audit-0f287160bf817b3ca016.md)
- [Original audit hash and public excerpt](../audits/audit-0ff1930c5d4878017f54.md)
- [Original audit hash and public excerpt](../audits/audit-126955c25fb6d48bafda.md)
- [Original audit hash and public excerpt](../audits/audit-14791a89af65ec81443c.md)
- [Original audit hash and public excerpt](../audits/audit-1e481b9ad01b4b62af21.md)
- [Original audit hash and public excerpt](../audits/audit-1f940596d115e34ae02f.md)
- [Original audit hash and public excerpt](../audits/audit-21267142b49cd147290a.md)
- [Original audit hash and public excerpt](../audits/audit-22d741ba21637e69bc9a.md)
- [Original audit hash and public excerpt](../audits/audit-29320e8e583d52eb5f20.md)
- [Original audit hash and public excerpt](../audits/audit-2cc154e4c127f0906ae0.md)
- [Original audit hash and public excerpt](../audits/audit-32922590be12d0046a69.md)
- [Original audit hash and public excerpt](../audits/audit-3bbcbd54e7cb734a5ce0.md)
- [Original audit hash and public excerpt](../audits/audit-4074703750eba42f8b7f.md)
- [Original audit hash and public excerpt](../audits/audit-429e93ed0d4b5e650ef5.md)
- [Original audit hash and public excerpt](../audits/audit-4376616d031747b32c87.md)
- [Original audit hash and public excerpt](../audits/audit-483d9caa91ea1c956079.md)
- [Original audit hash and public excerpt](../audits/audit-4af664a242392bba07e2.md)
- [Original audit hash and public excerpt](../audits/audit-4ed8d00dfd5d86541176.md)
- [Original audit hash and public excerpt](../audits/audit-4f9c259520d274f056b6.md)
- [Original audit hash and public excerpt](../audits/audit-5a6acf8414af5ba4fef9.md)
- [Original audit hash and public excerpt](../audits/audit-5cd1753822f1c6a3c06d.md)
- [Original audit hash and public excerpt](../audits/audit-62ba042a766f67beec9f.md)
- [Original audit hash and public excerpt](../audits/audit-642fa8e7d42cda1f1762.md)
- [Original audit hash and public excerpt](../audits/audit-683c5d2a873df7e2c3ce.md)
- [Original audit hash and public excerpt](../audits/audit-74d034ef6a5873b4a5e9.md)
- [Original audit hash and public excerpt](../audits/audit-7ac0039875dbca1d0b67.md)
- [Original audit hash and public excerpt](../audits/audit-7c91d45dc1aa187fe880.md)
- [Original audit hash and public excerpt](../audits/audit-81a482bba6bcc81336a6.md)
- [Original audit hash and public excerpt](../audits/audit-8788e59c2be22318680e.md)
- [Original audit hash and public excerpt](../audits/audit-8b0a5f586ab7c4916cc8.md)
- [Original audit hash and public excerpt](../audits/audit-90c23d1af2a59b1df673.md)
- [Original audit hash and public excerpt](../audits/audit-943484dd7722dbde7820.md)
- [Original audit hash and public excerpt](../audits/audit-9570ac8fc6dfdcbfd5ed.md)
- [Original audit hash and public excerpt](../audits/audit-9a720eae0135df096db9.md)
- [Original audit hash and public excerpt](../audits/audit-9dda8d7330e18ec39f99.md)
- [Original audit hash and public excerpt](../audits/audit-b27b25417f2e056a1b90.md)
- [Original audit hash and public excerpt](../audits/audit-b43d241215ca8c84c3c2.md)
- [Original audit hash and public excerpt](../audits/audit-c70de178e95e5c46203d.md)
- [Original audit hash and public excerpt](../audits/audit-c7ca0d0405f4d0cdcb9f.md)
- [Original audit hash and public excerpt](../audits/audit-c7cd773e3f897f934e45.md)
- [Original audit hash and public excerpt](../audits/audit-cad113d219a201e0f5e0.md)
- [Original audit hash and public excerpt](../audits/audit-cf094fc512d83c5c3636.md)
- [Original audit hash and public excerpt](../audits/audit-d409fb639593d5c459a5.md)
- [Original audit hash and public excerpt](../audits/audit-d87732dab7205ef6b52e.md)
- [Original audit hash and public excerpt](../audits/audit-dffb404b82747d32d666.md)
- [Original audit hash and public excerpt](../audits/audit-e5c8f2e9455ada3d921a.md)
- [Original audit hash and public excerpt](../audits/audit-f15d4e3c65d3f340c4d2.md)
- [Original audit hash and public excerpt](../audits/audit-f28dcaeb906ada4b945b.md)
- [Original audit hash and public excerpt](../audits/audit-f342d89e541599ff11aa.md)
- [Original audit hash and public excerpt](../audits/audit-f681d1b3ad53e12ab335.md)
- [Original audit hash and public excerpt](../audits/audit-f6ede40a69a9cd5a74b3.md)
- [Original audit hash and public excerpt](../audits/audit-f966ff96cd7e62ab7c38.md)
- [Original audit hash and public excerpt](../audits/audit-faa39053df3ce18fb628.md)
- [Original audit hash and public excerpt](../audits/audit-fb076ec1a01a891d9edb.md)

| Original variant | Signed historical state | Reviewed scoped status | Hardware coverage in this variant |
|---|---|---|---|
| off | BLOCKED | PARTIAL | False |
| ngram_simple | BLOCKED | PARTIAL | True |
| ngram_mod | BLOCKED | PARTIAL | True |


### Recorded model-specific variant coverage

```json
[
  {
    "levels": [
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "off"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "ngram_simple"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "ngram_mod"
      }
    ],
    "model": "omnicoder2"
  },
  {
    "levels": [
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "off"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "ngram_simple"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "ngram_mod"
      }
    ],
    "model": "qwen35"
  },
  {
    "levels": [
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "off"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "ngram_simple"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "ngram_mod"
      }
    ],
    "model": "qwen38"
  }
]
```

Historical states and window signatures are evidence links, not qualification of every model/variant.

## Available results

Values, baseline/candidate comparisons, model/engine identity and limits are in the linked audit excerpts and profile records. Missing measurements are **NOT MEASURED**. Existing native screens are not HumanEval, BFCL or full-agent qualifications.


### Variant ngram_simple

```json
[
  {
    "metrics": {
      "A": {
        "accepted_tokens": 0,
        "checkpoint_events": 0,
        "draft_tokens": 0,
        "families": 4,
        "median_spec_E2E_s": 3.565292737,
        "peak_device_VRAM_mib": 7364.5,
        "peak_process_VRAM_mib": 7122.0,
        "restore_events": 0,
        "spec_request_GPU_j_sum": 24003.916776212467,
        "spec_requests": 24
      },
      "B": {
        "acceptance_percent": 72.76720351390922,
        "accepted_tokens": 2982,
        "checkpoint_events": 180,
        "draft_tokens": 4098,
        "families": 4,
        "median_spec_E2E_s": 2.245261201,
        "peak_device_VRAM_mib": 7368.5,
        "peak_process_VRAM_mib": 7126.0,
        "restore_events": 30,
        "spec_request_GPU_j_sum": 14635.21042551419,
        "spec_requests": 24
      }
    }
  }
]
```

### Variant ngram_mod

```json
[
  {
    "metrics": {
      "A": {
        "accepted_tokens": 0,
        "checkpoint_events": 0,
        "draft_tokens": 0,
        "families": 4,
        "median_spec_E2E_s": 3.5644605140000003,
        "peak_device_VRAM_mib": 7364.5,
        "peak_process_VRAM_mib": 7122.0,
        "restore_events": 0,
        "spec_request_GPU_j_sum": 24246.033049203117,
        "spec_requests": 24
      },
      "B": {
        "acceptance_percent": 92.95513533555803,
        "accepted_tokens": 5014,
        "checkpoint_events": 86,
        "draft_tokens": 5394,
        "families": 4,
        "median_spec_E2E_s": 0.8961498960000001,
        "peak_device_VRAM_mib": 9200.5,
        "peak_process_VRAM_mib": 8958.0,
        "restore_events": 16,
        "spec_request_GPU_j_sum": 8459.989473976157,
        "spec_requests": 24
      }
    }
  },
  {
    "actual_ngram_draft": {
      "CUDA_unchanged": true,
      "acceptance_percent": 100.0,
      "accepted_tokens": 288,
      "draft_tokens": 288,
      "extra_model_weights": false
    },
    "memory_saved_vs_R244_device_mib": 1834,
    "native_metrics": {
      "decode": {
        "comparison": {
          "A0": {
            "e2e_reduction_percent": 61.80540420278828,
            "tokens_per_second_gain_percent": 177.24425377984625
          },
          "C": {
            "e2e_reduction_percent": 61.89174750831992,
            "tokens_per_second_gain_percent": 177.83756091987692
          }
        },
        "median_e2e_s": 0.640423883,
        "range_percent": 4.9364597166342765,
        "tokens_per_second": 221.2932937677187
      },
      "prefill": {
        "comparison": {
          "A0": {
            "e2e_reduction_percent": 9.078868702731723,
            "tokens_per_second_gain_percent": 0.1596222789308932
          },
          "C": {
            "e2e_reduction_percent": 1.8037862837381624,
            "tokens_per_second_gain_percent": -7.791552615427344
          }
        },
        "median_e2e_s": 0.194769109,
        "range_percent": 0.2639828269687341,
        "tokens_per_second": 2608.7136200679815
      },
      "prefill2048": {
        "comparison": {
          "A0": {
            "e2e_reduction_percent": 3.246472035875936,
            "tokens_per_second_gain_percent": 0.595010195718082
          },
          "C": {
            "e2e_reduction_percent": -5.62291298535984,
            "tokens_per_second_gain_percent": -8.015416525014253
          }
        },
        "median_e2e_s": 0.706923485,
        "range_percent": 0.465525204612492,
        "tokens_per_second": 2904.148905697407
      },
      "prefill4096": {
        "comparison": {
          "A0": {
            "e2e_reduction_percent": 1.4783317913268479,
            "tokens_per_second_gain_percent": 0.1987315161487313
          },
          "C": {
            "e2e_reduction_percent": -6.9306951301038255,
            "tokens_per_second_gain_percent": -8.309417302159316
          }
        },
        "median_e2e_s": 1.40354557,
        "range_percent": 0.3852594540268557,
        "tokens_per_second": 2923.865984716804
      }
    },
    "native_request_energy": [
      {
        "GPU_j": 54.79170416832652,
        "e2e_s": 0.19439814,
        "telemetry_time_coverage": 1.0
      },
      {
        "GPU_j": 162.17123809335143,
        "e2e_s": 0.706226268,
        "telemetry_time_coverage": 1.0
      },
      {
        "GPU_j": 348.0189843178038,
        "e2e_s": 1.40354557,
        "telemetry_time_coverage": 1.0
      },
      {
        "GPU_j": 158.0071851614689,
        "e2e_s": 0.664468276,
        "telemetry_time_coverage": 1.0
      },
      {
        "GPU_j": 55.37292287568168,
        "e2e_s": 0.194769109,
        "telemetry_time_coverage": 1.0
      },
      {
        "GPU_j": 161.8162461448869,
        "e2e_s": 0.709517175,
        "telemetry_time_coverage": 1.0
      },
      {
        "GPU_j": 334.3651005103456,
        "e2e_s": 1.401294528,
        "telemetry_time_coverage": 1.0
      },
      {
        "GPU_j": 137.39011057877642,
        "e2e_s": 0.632854009,
        "telemetry_time_coverage": 1.0
      },
      {
        "GPU_j": 55.12688814841488,
        "e2e_s": 0.194912297,
        "telemetry_time_coverage": 1.0
      },
      {
        "GPU_j": 194.9806353248372,
        "e2e_s": 0.706923485,
        "telemetry_time_coverage": 1.0
      },
      {
        "GPU_j": 391.88347499717787,
        "e2e_s": 1.40670182,
        "telemetry_time_coverage": 1.0
      },
      {
        "GPU_j": 117.78352424134457,
        "e2e_s": 0.640423883,
        "telemetry_time_coverage": 1.0
      }
    ],
    "peak_device_vram_mib": 7356.5,
    "peak_process_vram_mib": 7114.0
  }
]
```

## Decision and remaining research

VRAM, NVML-GPU-Energie, Akzeptanz und Checkpoints gemessen. Keine gemessenen HBM-Bytes/Token, Transaktionszähler oder HBM-interne elektrische Energie; kein separater additiver HBM-Speedup. R370 max32 spart1834MiB GPU-Speicher, ohne gemessene physische HBM-Transaktionen.

**Remaining scope:** A new traffic optimization needs actual reused/avoided tensor reads plus equivalent verification and rollback; hardware-counter metrics must be eligible on SM70.

**Reopening condition:** A new traffic optimization needs actual reused/avoided tensor reads plus equivalent verification and rollback; hardware-counter metrics must be eligible on SM70.

**Next action:** Retain S01/S02/S03 measured scopes; do not add an independent HBM speedup for the same MTP treatment.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Related sprint records

[R159](../experiments/R159.md), [R171](../experiments/R171.md), [R172](../experiments/R172.md), [R173](../experiments/R173.md), [R174](../experiments/R174.md), [R175](../experiments/R175.md), [R176](../experiments/R176.md), [R177](../experiments/R177.md), [R178](../experiments/R178.md), [R179](../experiments/R179.md), [R180](../experiments/R180.md), [R181](../experiments/R181.md), [R182](../experiments/R182.md), [R183](../experiments/R183.md), [R184](../experiments/R184.md), [R185](../experiments/R185.md), [R186](../experiments/R186.md), [R200](../experiments/R200.md), [R201](../experiments/R201.md), [R202](../experiments/R202.md), [R203](../experiments/R203.md), [R204](../experiments/R204.md), [R205](../experiments/R205.md), [R206](../experiments/R206.md), [R207](../experiments/R207.md), [R208](../experiments/R208.md), [R209](../experiments/R209.md), [R210](../experiments/R210.md), [R211](../experiments/R211.md), [R212](../experiments/R212.md), [R213](../experiments/R213.md), [R214](../experiments/R214.md), [R215](../experiments/R215.md), [R216](../experiments/R216.md), [R217](../experiments/R217.md), [R218](../experiments/R218.md), [R219](../experiments/R219.md), [R220](../experiments/R220.md), [R235](../experiments/R235.md), [R236](../experiments/R236.md), [R244](../experiments/R244.md), [R245](../experiments/R245.md), [R246](../experiments/R246.md), [R369](../experiments/R369.md), [R370](../experiments/R370.md)
