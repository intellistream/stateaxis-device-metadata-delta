# Adaptive metadata upload component evidence

Date: 2026-10-13 UTC

Evidence label: `component_npu_matched`

## Question and treatment

The earlier implementation minimized bytes but submitted one ACL H2D operation
per changed row/range. This campaign tests whether ACL submission fan-out, not
payload volume, is the limiting cost and whether batch-aware coalescing removes
the regression.

- Control: two contiguous asynchronous H2D copies per step (slots and complete
  block table).
- Row-sparse baseline: one copy per changed slot row and block range.
- Adaptive candidate: zero copies for unchanged data; one aggregate slot copy
  when more than one row changes; one aggregate block-table copy when more than
  one range changes; a single B1 range remains sparse.
- Timing boundary: host delta planning, `aclrtMemcpyAsync` submission and
  `aclrtSynchronizeStream`.
- Exactness: final candidate slot and block-table buffers copied D2H and compared
  with the host workload after every cell.

`decode_128_steps` models the metadata cadence implied by the current StateAxis
deployment: every decode step changes the slot and one block entry changes once
per 128 steps. It is a component workload, not a model-serving trace.

## Frozen environment

- Parent StateAxis commit: `5610586f00d24713cec712ae1a19fc87d2bf9a5c`
- Candidate StateAxis commit: `ce4c9832a` (local commit identity at capture;
  replace with the merged commit only if GitHub creates a different merge SHA)
- Source: `native/tests/device_metadata_delta_npu_benchmark.cpp`
- Dirty state during final runs: source changes committed; evidence repository
  changes uncommitted while raw files were copied
- Hardware: 2 x Ascend 910B2, physical IDs 4 and 5 exposed as logical devices
  0 and 1; 65,536 MiB HBM each; no other NPU processes
- CANN: 9.1.0; `npu-smi`: 25.2.1
- Host: Linux 5.15.0-25-generic, aarch64
- Compiler: GCC 11.4.0, `-O3 -std=c++20`
- Model: N/A (metadata component; no model weights loaded)
- Graph mode: N/A
- Blocks per sequence: 32
- Warmup/repetitions: 200/2,000 per cell

## Results

Decode-128 median timing (control/candidate microseconds and speedup):

| Device | Batch | Control us | Adaptive us | Speedup | Candidate calls/step | Candidate bytes/step |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 30.810 | 16.050 | 1.9196x | 1.008 | 4.032 |
| 0 | 8 | 30.811 | 16.400 | 1.8787x | 1.008 | 40.192 |
| 0 | 32 | 32.970 | 17.840 | 1.8481x | 1.008 | 160.768 |
| 1 | 1 | 30.580 | 15.970 | 1.9148x | 1.008 | 4.032 |
| 1 | 8 | 30.800 | 16.430 | 1.8746x | 1.008 | 40.192 |
| 1 | 32 | 33.111 | 17.810 | 1.8591x | 1.008 | 160.768 |

Retained row-sparse negative baseline on device 0:

| Batch | Control us | Row-sparse us | Speedup | Candidate calls/step |
|---:|---:|---:|---:|---:|
| 1 | 30.820 | 16.080 | 1.9167x | 1.008 |
| 8 | 29.901 | 117.531 | 0.2544x | 8.064 |
| 32 | 33.290 | 489.113 | 0.0681x | 32.256 |

The adaptive policy also caps fragmented-four B32 at two calls, improving the
device-0 result from 0.0137x to 0.8200x. It does not make that adversarial cell
positive: planning overhead remains measured and the payload falls back to the
control bytes. This negative is retained and bounds the claim.

## Reproduce

From the matching StateAxis checkout:

```bash
g++ -std=c++20 -O3 -Wall -Wextra -Werror \
  -I native/include \
  -I /usr/local/Ascend/cann-9.1.0/aarch64-linux/include \
  native/tests/device_metadata_delta_npu_benchmark.cpp \
  -L /usr/local/Ascend/cann-9.1.0/aarch64-linux/lib64 -lascendcl \
  -o /tmp/stateaxis-device-metadata-delta-benchmark

source /usr/local/Ascend/ascend-toolkit/set_env.sh
/tmp/stateaxis-device-metadata-delta-benchmark 0 row_sparse
/tmp/stateaxis-device-metadata-delta-benchmark 0 adaptive_coalesced
/tmp/stateaxis-device-metadata-delta-benchmark 1 adaptive_coalesced
```

The CPU contract and complete Native Engine binary were also built successfully
with CANN 9.1.0, ATB 9.1.0 ABI 1 and the installed vLLM-Ascend custom operator
headers. `stateaxis_device_metadata_delta_test` passed.

## Claim boundary and next gate

This establishes exact matched component behavior and a positive result for the
decode-128 metadata cadence. It does **not** establish end-to-end throughput,
online latency, AgentX performance, or a Qwen3.5-35B result. Promotion remains
blocked on an identity-bound full-model artifact and alternating 3+3 on/off
service runs with activation telemetry, output exactness, lifecycle cleanup,
TTFT/TPOT/throughput and HBM recorded.
