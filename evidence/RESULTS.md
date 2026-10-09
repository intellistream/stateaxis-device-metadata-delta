# Verified Ascend results

> **Append-only evidence ledger — not current repository status.** Entries retain
> accepted, rejected, invalid and superseded runs in historical order. Use
> [`NATIVE_ENGINE_STATUS.md`](NATIVE_ENGINE_STATUS.md) for current capability and
> default-state classification, and [`README.md`](README.md) for fact precedence.

## Qwen3.8 r476 producer-hinted rendezvous result

r476 adds a producer-declared finite-arrival identity and target to r475's
bounded rendezvous policy while retaining the numerically qualified two-row
physical prefill wave. Its short NPU4-7 gate passed 14/14 exact B3/B4 responses,
all-rank replay and zero observers. The formal Native transaction completed 64
warmup plus 192 measured requests, released NPU4-7, preserved the protected
container identity and restored r113 on the documented runtime cpusets.

Relative to r472, throughput changes are +1.90%, +15.43%, +1.87% and +8.84%
for max16/c1, max16/c4, max64/c1 and max64/c4. Mean TTFT changes by -27.9,
-675.1, -73.1 and -681.3 ms. Explicit releases number 128 and collection-window
expirations fall from 160 to 32. This removes r475's isolated-request regression
while retaining its B2+B2 burst formation.

r476 remains diagnostic: it matches r472 content on 177/192 measured requests,
with all 15 differences at c4, and matches the pinned vLLM responses on 147/192.
Its Native/vLLM throughput ratios are 0.7143x, 0.4104x, 0.8741x and 0.5682x.
The validated A/B artifact is
`/data/statecentric-builds/qwen38-r472-r476-native-prefill-arrival-analysis-r001.json`
(SHA-256 `057edbc11f10c8dd4d80d7192327b7452175ed00ca23787167d6eef87e1dd001`),
and the vLLM split artifact is
`/data/statecentric-builds/qwen38-r476-tp2pp2-vllm-derived-r001.json`
(SHA-256 `51ddabcd4566af2af151ca37f69adb8b825b03b4e24ec60711aefb46c9f9865e`).

## Qwen3.8 r474 rejection and r475 cohort-delay result

r474 tested three/four-sequence physical prefill waves on NPU4-7. The B3/B4
gate returned all 14 responses deterministically, but each repeated the same
token error. The candidate was rejected, r113 was restored, and Qwen-specific
manifest, plan, Rust assembly and executor admission now require an enabled
maximum width of exactly two. Generic backend capability remains separate from
this model-specific numerical qualification.

r475 retains that width and changes only the cohort wait from 20 to 125 ms.
Its short gate passed 14/14 exact responses, all-rank replay and zero observers.
The full Native arm completed all 64 warmup and 192 measured requests, released
NPU4-7 and restored r113 on the documented runtime cpusets. At c4, max16 output
throughput rose 14.930 -> 17.368 tokens/s and mean TTFT fell 2539.5 -> 1847.7
ms; max64 rose 35.063 -> 38.018 tokens/s and TTFT fell 2524.9 -> 1851.8 ms.
The scheduler changed the staggered prefill from B1+B3 (three physical waves)
to B2+B2 (two waves).

The fixed wait is not promotion-ready. At c1, max16 throughput fell 6.41% and
TTFT rose 97.9 ms; max64 throughput fell 1.83% and TTFT rose 58.7 ms. Content
matches r472 on 177/192 measured requests, with 15 deterministic c4 differences.
Both r472 and r475 match 147/192 against the same separately supervised vLLM
responses, but not on the same request set. The bounded exact short gate remains
valid; equal-output and default-promotion claims remain closed. Primary derived
evidence is `/data/statecentric-builds/qwen38-r472-r475-native-prefill-cohort-analysis-r001.json`
(SHA-256 `dcf5186615dd9bb715ff3ac7e6aac522835fe1473f1aa7bd62aec977795457ce`).
The candidate-to-vLLM derived record is
`/data/statecentric-builds/qwen38-r475-tp2pp2-vllm-derived-r002.json`
(SHA-256 `91a505a2ee35da88803216f85647a5123cf045b47aa380e06ed903ddcf32278f`).

## Qwen3.8 r472 observer-free graph and matched-workload result

r471 completed full-engine NPU4-7 B1-B4 exactness, cold capture/replay, B2/B3
shape coverage, cancellation recovery and normal drain, but retained diagnostic
MLP/logit observers and is correctness-only evidence. Observer-free r472 keeps
the same executable plan and uses qualified ordinary MLP and sampling providers.
Its short gate produced ten exact B1/B4 responses, all-rank replay and zero
observer records. The complete Native comparison arm later produced 256/256
successful requests, exactly 6,584 batches and 256 prefills, restored r113, and
left NPU4-7 idle.

The pinned vLLM-HUST and r472 arms use identical BF16 TP2×PP2 model/workload
bindings. Because the external NPU0-3 manager twice replaced the protected
SageMate container between sequential arms, the comparison is explicitly
derived from complete vLLM r006 and separately supervised Native r001 evidence.
Native/vLLM output throughput is 10.514/15.000, 14.930/41.997, 17.390/20.267
and 35.063/67.164 tokens/s for max16/c1, max16/c4, max64/c1 and max64/c4.
Single-concurrency TPOT is close (47.052/45.536 and 45.899/44.041 ms), while c4
Native TPOT rises to 101.806 and 72.298 ms. Client TTFT observations are
0.79-0.82 s at Native c1 and about 2.52 s at c4; they diagnose prefill/pipeline
bubbles but do not authorize a cross-runtime TTFT speedup claim.

Graph absence is not the cause: every Native rank records three first replays.
The retained c4 telemetry instead shows B3 prefill around 2.975 s, B4 decode
worker execution around 63.55 ms, and late B1 decode submission waits around
0.626 s median. Exact content matches 147/192 measured requests; the other 45
differ only in content, with token counts and finish reasons unchanged. r472
therefore remains opt-in and equal-quality/performance-promotion gates remain
closed. The validated derived artifact is
`/data/statecentric-builds/qwen38-r472-tp2pp2-vllm-split-analysis-r001.json`.

## Qwen3.8 resumable-prefill scheduling screen, r436–r463

The worker/provider path now supports an identity-owned prefill cursor, four-rank
`Begin/Advance/Finish/Cancel`, protocol safe points, repeated decode completions,
and deferred state-control frames. r441 passed the 88-request B1–B4 shape gate;
r443 passed ten all-subset cancellation cycles with 562 submitted, 280 canceled
and 282 exact completed requests. r444 then found a real control-frame race:
an Evict arriving after nested completion was rejected as a non-ExecuteBatch.
r447 defers that frame to the top-level loop; r451 completed all 256 long-gate
requests and observed four deferred kind-4 frames. Graph execution remained
fully accounted and four-rank packed leases drained in every accepted gate.

Three scheduling policies were screened against the complete frozen r444 r399
a1 raw SSE arm. This is a same-host provisional diagnostic rather than ABBA:

| c4 cell | Policy | Output tok/s | Mean TTFT ms | Mean TPOT ms | Mean E2E ms | Semantic SSE gap P95 ms |
|---|---|---:|---:|---:|---:|---:|
| max16 | r399 | 20.991 | 1725.260 | 77.309 | 2884.898 | 2071.055 |
| max16 | r451 unbounded | 16.199 | 2428.719 | 81.538 | 3651.790 | 259.623 |
| max16 | r453 total cap 2 | 18.011 | 2106.957 | 83.892 | 3365.342 | 2527.563 |
| max16 | r459 cadence 4 | 17.533 | 2188.049 | 83.553 | 3441.346 | 820.022 |
| max64 | r399 | 46.874 | 1699.535 | 57.097 | 5296.625 | 2018.280 |
| max64 | r451 unbounded | 39.794 | 2462.339 | 58.129 | 6124.471 | 265.796 |
| max64 | r453 total cap 2 | 42.709 | 2100.326 | 58.807 | 5805.144 | 2517.042 |
| max64 | r459 cadence 4 | 42.187 | 2174.858 | 58.469 | 5858.398 | 812.627 |

r459 preserves a 59.74–60.41% c4 gap reduction but loses 10.00–16.47%
throughput and adds 26.82–27.97% TTFT versus r399. It therefore fails the 5%
regression guard and did not proceed to ABBA. r463 completed 256/256 requests,
recorded 32 prefills, 352 waves, 120 nested decodes and 264 cadence-skipped
waves, with zero unaccounted graph executions and symmetric lease retirement.
Evidence is under `/data/statecentric-builds/qwen38-prefill-continuation-r441-shape-gate`,
`r443-cancel-gate`, `r451-long-gate`, `r456-shape-gate`, `r457-long-gate`,
`r462-shape-gate`, and `r463-long-gate`. Stable default r153 and post-run r113
remain unchanged.

## Issue #15 controlled-cold pipelined loader closure

The identity-bound candidate completed matched Qwen2.5-14B control/candidate
3+3 in both controlled cold and fully resident warm cache states. All 12 serving
runs were exact. Cold process-to-Ready median fell from 344.168 to 53.895 s
(-84.340%), while TPOT P50 changed +0.043%, output-token throughput changed
+0.024%, and peak HBM remained 44,687 MiB. Warm Ready fell from 324.809 to
36.392 s (-88.796%), TPOT P50 changed -0.685%, and peak HBM remained 44,688
MiB. The candidate uses two bounded 64-MiB pinned slots and exact loaded-byte
SHA-256; the serial policy remains the unbound default.

A separate real-device MiniMax-M2.5 layer-0 EP8 1+1 loaded 32 files and
3,628,597,248 bytes across all eight physical ranks. Both arms passed every
source digest, D2H arena digest and transactional Ready check. Candidate process
elapsed was 9.352 versus 20.666 s control (-54.748% diagnostic); this is a
multi-rank loader acceptance cell, not full-model MiniMax serving evidence.
Short-read, bit-flip, digest, duplicate/overlap/OOB, stale-plan, pinned/copy,
rank, cancel and event faults all fail closed. The compact release evidence is
`benchmarks/issue15_weight_loader_20260815_r5_result.json`; full raw directories,
including the earlier negative and failed-cache-domain runs, remain append-only.

## Issue #11 production session lifecycle r2 1+1

The cancellation-safe default-off Native session adapter passed a fresh matched real-NPU correctness
gate on physical NPU3. Control and candidate each completed 14/14 exact agent
state-tree requests under the same official `.23` image, model, artifact,
oracle, capacity and timing boundary. Control close returned the expected
disabled fallback and left five retained states. Candidate created five unique
generation-bound holder edges, applied one close with zero fallback, reclaimed
all five states, and ended with zero active session, holder, protected-state and
executor-state gauges. Peak HBM was 53,533 MiB in both arms. This is one run per arm,
so the observed +2.1298% request/s and +1.2168% P99-latency point estimates are
diagnostic only; r1 had different directions, and performance and speedup claims remain false.

## Issue #11 acceptance boundary audit

No new NPU run was performed. R2 remains accepted as a default-off production-
authority correctness gate: one fresh process per arm, 14/14 exact requests,
candidate close authority 1, fallback 0, five states reclaimed and no remaining
session/executor state. Its preregistration and result explicitly deny
performance and capacity claims.

The checked-in issue contract remains incomplete. There is no repeated hard-
pressure A/B proving soft-protected eviction and admission liveness, nor
recomputed-token, forced-eviction, close-to-reclaim or 20%-target evidence with
the TPOT P99 guard. The machine boundary is in
`results/issue11-session-lifecycle-acceptance-audit-20260814/`.

## Issue #12 acceptance boundary audit

No new NPU run was performed. R3/R4 remain accepted default-off production-
authority correctness evidence. R3 uses a four-request synthetic fixture with
max batch one and fixture concurrency two; all 24 requests are exact, candidate
authority applies 12 times and fallback is zero.

The R3 preregistration explicitly denies performance/speedup claims. Its
descriptive wall-time delta of -0.251% therefore cannot reject the issue's 15%
high-fan-out/public-agent-trace target. Program completion tails, NPU/state/
preemption/fairness metrics, degradation cells and scheduler CPU P99 budget are
unrun. The machine boundary is in
`results/issue12-program-aware-acceptance-audit-20260814/`.

## Issue #8 existing-evidence boundary audit

No new NPU run was performed. The preserved capacity-17 R8 directories contain
three cold runs per arm under one matched model/prompt/oracle/image/NPU identity.
All 384 responses are exact. Atomic control versus K1089 candidate median
request throughput is 7.011813/6.908211 request/s (-1.4775%); hot TPOT P95 is
35.479/40.250 ms (+13.4469%), cold TTFT P50 is 1357.383/1390.265 ms (+2.4224%),
and peak HBM is 43,922/43,940 MiB. Candidate prefill batches double from four
to eight per run, proving treatment activation. These source runs explicitly
classify themselves as correctness smoke with no formal performance claim.

The separate warm 3+3 directories contain a four-token seed, 64 retained-
decision hits with zero executor batches, and one stale-generation rejection
per run; they do not exercise chunking. Their stale Qwen2.5-7B label is rejected
by the frozen 48-layer, hidden-5120, 29,540,067,328-byte model manifest. This
audit supports the existing negative/default-off classification of the V181 and
V208 implementations, but not closure of Issue #8's unrun multi-length,
concurrency, fault, blocking and starvation matrix. Normalized evidence and
source hashes are in `results/issue8-chunked-prefill-evidence-audit-20260814/`.

## Issue #15 acceptance boundary audit

No new NPU run was performed. The R8 3+3 remains an accepted single-rank,
uncontrolled warm-page-cache positive: loader median falls 55.69%, process-to-
ready falls 5.76%, all 192 requests are exact, and steady-state throughput
changes -0.14%. The serial loader remains default.

This does not complete the checked-in issue contract. R8 explicitly forbids a
cold-cache claim and does not provide the required controlled cold-cache and
TP/EP multi-rank A/B, specified fault-injection matrix, overlap ratio or full
resource telemetry. The original ≥20% cold process-to-ready or ≥40% critical-
path-overlap gate is therefore unproven. The machine-readable boundary is in
`results/issue15-weight-loader-acceptance-audit-20260814/`.

## V208-matched mixed baseline closure

The exact mixed P2177/O32 workload now has both runtimes on physical NPU4:
four c32 cohorts each submit 31 hot requests and one 20-ms-delayed cold request.
Native V208 reaches 20.342782 request/s and 650.969011 output token/s; pinned
vLLM-HUST reaches 16.704700 request/s and 534.550404 output token/s, making
Native 21.7788% faster. HUST completes 128/128 requests and all 4,096 oracle
tokens. Its scored cache counters exactly prove 278,656 queried and 269,824 hit
prompt tokens. Stable-hot and unique-cold cache salts preserve identical prompt
token IDs. vLLM's required final-token recomputation yields 2,176 hot cached
tokens versus Native's 2,177 reused state tokens; the comparison records this
engine constraint explicitly. This is an accepted matched single-lifecycle
point estimate, not a formal 3+3 or cross-runtime TTFT result.

## V264 cache-capacity online negative

The accepted V263 engine with 548 instead of 528 physical KV blocks completes
128/128 exact independent-cold requests at 3.135377 request/s and 100.332078
output token/s. This is only +0.01951% over V263 and -7.11441% versus the fixed
HUST baseline. B30 is observed, but decode/prefill counts remain 465/24 and
peak HBM rises 383 MiB to 65,096 MiB. V264 is therefore rejected despite clean
provenance, exact output, state recycling and teardown.

## V262 odd-suffix component rejection

The composed length-bound layout, P2048 prefix TFA, exact suffix TFA and merge
chain reduces P50 by 14.06%/12.97%/9.83% at suffix 130/145/161, below the 20%
all-point gate. S130 mean error is 0.004170 and S145 is nonfinite, so composed
correctness also fails despite the earlier standalone suffix oracle pass. The
two-way prefix K/V allocation totals 768 MiB over 48 layers and is 384 MiB
incremental over one copy. V262 is rejected with no online or HUST metric.

## V263 independent-cold c32/o32 baseline closure

The matched physical-NPU4 cell uses 128 unique 2,206-token prompt rows, ten
warmups, client concurrency 32 and 32 output tokens. Native r10 completes
128/128 requests and all 4,096 frozen-oracle output tokens at 3.134766 request/s
and 100.312511 output token/s. The immutable HUST arm reaches 3.375526 request/s
and 108.016844 output token/s, so Native is 7.1325% slower. Native/HUST peak HBM
is 64,713/53,463 MiB. Native provenance, exactness, state recycling and cleanup
pass; HUST validates prompt identity and output length but binds no token oracle.
This is a real accepted negative, not an invalid lifecycle and not evidence
about the distinct shared-prefix or mixed forced-state workloads.

## V265--V270 independent-cold prefill screens

V265 has no valid performance result because its component correctness oracle
used an invalid prompt/oracle pairing. Corrected V266 completes 14 fresh-worker
B1/P2177 lifecycles with every output equal to frozen token 51741. Its five
measured medians are 378.572 ms control and 361.077 ms candidate, a 4.6212%
reduction that misses the preregistered 10% gate. It is a valid component
negative with request/s and output-token/s N/A.

Representative-shape V267 completes 14 B16/P2177 lifecycles with all 224 rows
exact. Its five measured medians are 4,241.385 ms control and 4,181.359 ms
candidate, only +1.4153%. It is rejected below the same 10% gate and produces
no full-engine throughput row.

V268 tests one packed QKV AddMM followed by three two-dimensional device
compactions per layer. All 14 fresh lifecycles and 224 output rows are exact,
but the five-sample median grows from 4,235.865 ms control to 14,357.974 ms
candidate, a -238.9620% change. The mechanism is rejected as a valid negative;
component-only request/s and output-token/s remain N/A.

V269 keeps packed output zero-copy through downstream consumers. Its worker,
artifact and resident-plan identities pass, but CANN rejects the packed-row-
stride Q/K view at `aclnnApplyRotaryPosEmbV2GetWorkspaceSize` with status
561103 before a complete request. No timing JSON exists, so V269 is N/A and
the full paired campaign was not started.

V270 replaces V268's three DMA compactions with a fixed-shape PTO compactor
while retaining compact-buffer ACLNN RoPE. All 14 lifecycles and 224 rows are
exact with empty stderr. The measured control/candidate medians are 4,244.304/
4,310.832 ms, so candidate is 1.5675% slower. This is a valid component
negative, not an identity or correctness rejection.

## V100 physical-B32 preregistration: software boundary only

The current-source inventory confirms that B32 is supported by the generic
revision-10 resident-plan compiler at a minimum 10-GiB workspace. Historical
same-backend B32 diagnostics reached 14.5589, 14.7287 and 14.6888 request/s,
but their scheduler/state identities are stale and they are not current
comparison evidence. V100 therefore freezes a new B16/B32/B16 Native-only
screen instead of replaying or relabeling any historical result.

The preparer, preregistration and four focused contracts are checked in. The
related suite passes 53 tests and 54 subtests; full discovery passes 451 tests
with six expected skips. No carrier, artifact, model, request, NPU lifecycle or
throughput sample exists yet. `formal_gate_open=false`, `performance_claim=false`,
and TTFT comparison is forbidden.

## Standalone PTO SwiGLU v6 device noncompletion

The clean-pushed v6 lifecycle crossed the earlier carrier boundary on physical
NPU7. The ACLNN arm completed 20 warmups and 200 measured iterations, and its
442,368-byte BF16 output matched the independent CPU oracle exactly: zero
mismatches, zero nonfinite values, and zero maximum absolute error. Its
device-event median was 0.246100 ms, but this value is control-only diagnostic
evidence.

The PTO arm then entered its first warmup and produced no output while holding
116 MiB on NPU7 at 100% AICore utilization for more than 65 seconds. The
lifecycle was interrupted, its exact container was removed, and NPU7 returned
to the no-process baseline. Since no PTO sample or output exists, v6 provides
neither PTO correctness nor an eligible latency comparison. The v6 failure
audit freezes raw-manifest SHA-256 `6814b6f1...2c39`.

Fresh v7 repairs only the exposed kernel boundary: its 768-element tiles stay
below the pinned official SwiGLU's 1,024-element tile size, it replaces the
custom two-stage event schedule with sequential official `PtoSetWaitFlag`
synchronization, and every arm has a 30-second TERM plus five-second KILL
deadline. `formal_gate_open=false`, `performance_claim=false`, production
integration and TTFT comparison remain prohibited.

v7 also timed out at its first PTO warmup under the enforced 30-second
deadline, with empty PTO stdout/stderr and complete exact-container cleanup.
That excludes the old double-buffer schedule and an actual element count above
1,024, but v7 still instantiated a 768-wide static PTO tile unlike the pinned
official helper's 1,024-wide tile plus runtime mask. Fresh v8 changes only
that static tile capacity. It has no result until its clean-pushed lifecycle
completes.

v8 also timed out before its first PTO warmup completed, so the official
1,024-element static capacity alone does not repair the device noncompletion.
Fresh v9 adds two separately named, 1-warmup/1-iteration PTO diagnostics
before the unchanged candidate: exact gate copy isolates launch and GM/UB
transport; exact BF16-to-FP32-to-BF16 gate copy additionally isolates vector
cast. Each has its own bitwise gate-input oracle and 30-second deadline. Only
the final full-SwiGLU arm may enter the existing mechanism comparison.

v9 localized two faults. The PTO copy arm returned in 0.007840 ms but had
220,995/221,184 bit mismatches: all six output chunks per core repeated that
core's final loaded chunk, proving a missing MTE3-to-MTE2 UB reuse dependency.
The following cast-copy arm timed out before a result. Fresh v10 orders reuse
through MTE3-to-MTE2 and selects the official `TCVT<false>` variant for
BF16/FP32 conversions, avoiding saturation-control register mutation that is
irrelevant to these non-saturating conversions.

## Official-derived PTO SwiGLU software readiness

The pinned Huawei PTO-ISA `dispatch_mega_combine` source has been adapted into
a standalone dense-Qwen BF16 SwiGLU component without copying its MoE routing,
INT8 dynamic quantization, communication, or GMM2 coupling. Static contracts
accept the exact `[16,27648] -> [16,13824]` geometry, complete 48-AIV
partition, row boundaries, 54-KiB double-buffered UB footprint, upstream
source/commit, license, vector helper dependency, arithmetic instruction
sequence, stable ABI, and default-off boundary.

On the new server, a no-device BiSheng/CMake build completed and produced a
shared object containing `.aicore_binary` and
`StatecentricQwen14bSwiGluPtoLaunch`. This generated shared object is an
ignored local build product, not a frozen artifact or result. No ACL context,
NPU kernel, model, request, oracle, profiler, or comparison ran. Therefore
correctness, numerical error, latency, throughput, HBM, and integration fields
are all n/a; every claim gate remains false.

## PTO-online v6 explicit-prefill-cohort diagnostic

The v5 arrival-skew failure has a fresh, identity-changing repair. The
shared-prefix client assigns each consecutive 16-request subgroup a stable
prefill cohort identifier. Scheduler-plan v10 with policy
`explicit-prefill-persistent-decode-cohort-v3` refuses to release an incomplete
tagged group even after starvation thresholds, prevents inter-group mixing,
and clears the tag after prefill so the established persistent decode cohort
takes over. Untagged workloads retain the prior v9 bounded-release behavior.

The active preregistration, scripts, auditor, artifacts, carrier, lock, unit,
and result paths use fresh v6/v27 names. Rust 113/113 and the selected Python
137/137 tests pass. Clean pushed `d982ba6` produced the candidate/control pair
inside a no-device build container, after which that container was removed.
Both Native state audits accept scheduler-plan v10; pair-readiness SHA-256 is
`2b14c717...0611`, carrier identity is `d92f1740...b809`, and the frozen
identity-lock SHA-256 is `cdc73531...9b81`.

The unique v6 submission then ran on stable-idle NPU7. Candidate and control
each produced 128/128 exact rows, 4,096/4,096 exact output tokens, 8 B16
append batches, 248 B16 decode batches, four co-resident c32 cycle pairs, zero
state-slot wait, and no capacity-timing violation. Candidate measured
7.486679 request/s and control measured 7.541568 request/s, a candidate point
estimate of -0.7278%.

The frozen controller's first independent audit rejected before inspecting
either arm because it ran before their required manifests were created. A
manifest-complete re-audit verified nearly every runtime, oracle, identity,
carrier and scheduling check, but exposed two additional static auditor
errors: it required 256 rows in `decode_timing.jsonl`, although that file
contains only the 248 decode batches, and it interpreted the control
artifact's canonical all-zero operator-library digest as a present PTO
artifact. These are audit/lifecycle defects, not authorization to rewrite the
original audit or rerun v6.

The corrected auditor and manifest ordering passed tests and were clean-pushed
as `390959c`. Device-free re-audit v3 SHA-256 `f1d031a9...cd8d` accepts both
arms, every one-factor check, all 248 B16 decode timing rows per arm, the
canonical absent control library, and the complete evidence manifests with no
violations. Both peak HBM values are 40,580 MiB. The admitted diagnostic is
negative: PTO is 0.7278% slower at the point estimate, so the default remains
ACLNN and PTO remains default-off.

`formal_gate_open=false`, `performance_claim=false`, production integration
and TTFT comparison remain prohibited.

## PTO-online v5 candidate cohort rejection

The sole v5 submission ran from clean pushed `f436f62` on physical NPU7.
Carrier identity, two post-create stability probes, Native CTest, frozen host
toolchain, runtime binary identity, model/oracle byte validation, worker
startup, and health all passed. The candidate served 128 requests and every
output matched the independent oracle; reuse and state-leak validation also
passed.

The lifecycle is rejected. The scheduler produced 12 append batches with
sizes 2, 3, 6, 10, 13, 14, and 16 (only four B16 batches), followed by 253
decode batches, rather than the preregistered 8 B16 append and 248 B16 decode
batches. Candidate post-validation returned 1, the control arm never started,
and the independent audit rejected the incomplete pair. Cleanup removed the
exact container and restored NPU7, port 18087, and scoped processes.

The raw candidate request rate and timings are invalid for comparison because
the physical cohort contract failed. There is no PTO-versus-ACLNN result:
`formal_gate_open=false`, `performance_claim=false`, production integration
and TTFT comparison remain prohibited. v5 is immutable.

## PTO online-worker readiness (software evidence only)

The fixed-B16 PTO Gate/Up path is now reachable from the Native protocol worker
through a default-off schema-4 policy. Smaller real decode buckets retain fused
ACLNN Gate/Up fallback; ACLNN SwiGLU remains unchanged. The environment is a
path hint only and is rejected unless the configuration selects PTO.

Execution-artifact v3 is 424 bytes and binds the canonical decode plan plus the
exact PTO shared-library SHA-256. Python and C++ mutation tests reject missing
plan/library, non-PTO artifacts carrying a library, and byte substitution at
the configured path. Runtime validation occurs before `dlopen` and ACL
initialization, so these changes invalidate old resident and continuation state
before device execution.

Focused results are Python 23/23, Rust configuration 5/5, Rust launch binding
4/4, direct C++ codec/artifact executables, and an isolated Release build with
worker/inspector plus 3/3 selected CTest. No device was initialized and no
online request ran. Correctness, request/s, output token/s, P50/P95/P99, TPOT,
error rate, state hit/reuse, HBM and TTFT are all n/a. All formal, performance
and production-integration gates remain false.
The trace contract also distinguishes B16 PTO's 533 workspace requests from
the 581-request fused-ACLNN fallback; this is a derived call-count invariant,
not a measured latency result.

## Repaired isolated hybrid v3 lifecycle (accepted correctness)

The fresh v3 namespace and two-phase timeout are now bound into carrier
identity `414cfbab...fc370`. The identity covers compiler, isolated runner,
stage runner, component runner, independent auditor and submitter bytes, so it
invalidates `b36314e8...ab070` and all executed v2 custody. Model, weights,
physical B16, zero warmups, PTO/ACL operator split, v21/v7 artifact identity
and the frozen independent oracle remain unchanged.

The sole lifecycle ran from clean pushed `0bd7a7e` on physical NPU7. The
project-owned carrier passed Native CTest 30/30, validated 48/48 packs and
started exactly one worker. It completed naturally in 354.112 seconds with
worker/carrier exit 0, empty stderr, `Result=success`, and no restart.

The zero-warmup physical-B16 step used PTO fused Gate/Up, ACLNN SwiGLU and the
existing eager ACL/CANN remainder. All 16 rows generated token 264, every
decision certificate passed, and generation `[525,264]` matched the frozen
independent oracle. Raw logits SHA-256 is `d2c09d74...5609`; they are finite
and preserve all greedy decisions, while full-logit bit parity is false
(cosine 0.999941, maximum absolute error 0.25). Result and producer-summary
SHA-256 values are `0a3c2d54...d728` and `d8058ead...d41`.

Automatic independent audit `825af0b2...602d` accepts with no violations; a
fresh re-audit is byte-identical. Sampled peak HBM usage was 90% and runtime
peak ACL allocation was 58,372,862,016 bytes. The unit is collected, exact
container absent, start/final ports identical, scoped processes empty, and
NPU7 returned to 5% HBM/0% AICore.

The retained 33.381834-ms step is raw single-arm diagnostic data. There was no
control, repeat, online request or vLLM lifecycle, so request/s, output
token/s, P50/P95/P99, TPOT, error rate, state hit/reuse, comparative HBM and
TTFT are n/a. Correctness and lifecycle gates pass; formal, performance and
production-integration gates remain false.

## Plan-bound hybrid single-step result (execution correct, lifecycle rejected)

Native now embeds an optional canonical `DecodeExecutionPlan` identity in the
candidate binary. A PTO candidate refuses a zero-plan binary, requires an
execution-artifact record in-process, and validates that record's plan leaf
before ACL initialization. The v21 preparer and v7 freezer bind plan
`1a51f092...879c`; the single-step runner is fixed to physical NPU7, B16, one
decode step and zero warmups. Its independent auditor checks all 16 physical
rows, raw logits, frozen oracle, artifact/runtime binding, HBM samples, ports,
processes and cleanup.

Native CTest passes 30/30 and focused Python identity/plan/artifact tests pass
27/27. Clean-pushed parent `81c44c7` generated v21 artifact/config/plan
`58db9e6e...9831` / `cedcad09...cf38` / `1d3a2dc4...bd9b`, executor
`5d8b21e4...e2fe`, and pack-lock v7. Runtime binding independently observes
plan `1a51f092...879c`; v7 invalidates v20/v6 artifact/executor/plan while
preserving the exact model and weight leaves. This was the software readiness
state before either hardware lifecycle.

The sole admitted hardware namespace then terminated before candidate output
or accelerator execution. Worker exit was 137 with zero-byte stdout/stderr;
the shared container ID and name disappeared during the lifecycle. Ninety
NPU7 samples remained exactly 5% HBM with no observed accelerator execution,
and final device inspection found no NPU7 process. Ports before/after were
byte-identical and host candidate/docker-exec process sets were empty.
Independent rejected audit `ad555d9a...b3f6` classifies this as
`pre-output container-lifecycle termination`; bundle tree
`ebf00599...29fc` preserves the incomplete lifecycle.

There are no logits or generated tokens, so correctness is not established.
There is likewise no latency, throughput, TPOT, comparative HBM or vLLM
sample. The failure-path runner now tolerates missing logits and treats a
confirmed absent container plus clean host/NPU/ports as effective resource
release. Per the one-lifecycle preregistration, the run was not retried.

A later, separately authorized isolated v2 lifecycle ran once from clean
pushed `677d0a4` on physical NPU7. Its in-container Native CTest passed 30/30,
all 48 weight packs validated, and the physical-B16, zero-warmup hybrid
full-model step completed. PTO supplied fused Gate/Up, ACLNN supplied SwiGLU,
and the existing ACL/CANN path supplied the remaining operators. All 16 rows
generated token 264, every decision certificate passed, and the two-token
generation `[525,264]` matched the frozen independent oracle. The raw logits
are finite with cosine similarity 0.999941 to the frozen logits and identical
top-10 ordering; they are not bitwise equal (`max_abs_error=0.25`), so the
claim is greedy-decision parity, not full-logit parity.

The result is not an accepted lifecycle. Cold load/residency crossed the
300-second wrapper. TERM did not stop `docker exec`; the worker completed and
wrote result/logits, after which GNU `timeout` returned 124. Consequently the
producer summary and final inner custody records were never emitted.
Independent audit `fac99040...ab466` independently rebinds the frozen oracle
manifest and raw-logits digest, and reports
`execution_correctness_observed=true` and
`timeout-after-completed-correct-output`, but rejects lifecycle and correctness
gates. Outer carrier custody proves exact container removal, empty NPU7/scoped
processes and unchanged ports. Sampled peak HBM usage was 90%; runtime peak
ACL allocation was 58,372,862,016 bytes. The retained 33.112582-ms step time
has no control and is not performance evidence.

The repair replaces TERM-only 300 seconds with TERM at 900 seconds and KILL at
910 seconds. It also closes a transitive identity gap: carrier
`b36314e8...ab070` binds compiler, isolated runner, stage runner, component
runner, auditor and submitter and invalidates executed carrier
`800a85a6...2247`. No second hardware lifecycle ran. Request/s, output
token/s, P50/P95/P99, TPOT, error rate, state hit/reuse and vLLM comparison
remain n/a; all formal, performance and production gates remain false.

## vLLM execution-parity decode-plan readiness (software only)

Deterministic extraction and independent recomputation accept plan identity
`1a51f092...879c`. It binds pinned sources, reference metadata, Qwen2.5-14B
BF16 geometry, physical B16, operator/backend order, paged-KV block 128,
stable addresses, workspace lifetime and replay ordering. Reference
`piecewise` graph and Native `full_decode_only_target` are explicitly distinct.

Artifact v2 binds the plan and rejects legacy/absent/mutated candidate identity.
Focused Python tests pass 25/25 and the C++ identity test passes. No NPU,
correctness, latency, throughput, HBM, vLLM or TTFT result exists; all gates
remain false.

## Balanced N192 PTO Gate/Up diagnostic (mixed, mechanism rejected)

Fresh physical-NPU7 component audit `8d7b7436...aff1` accepts all six exact
outputs and zero custody violations. ACLNN/PTO medians are
29.129528/31.819345 ms. N192 is 1.98559% faster than the accepted
32.463947-ms N256 PTO predecessor, below the preregistered 3% component
threshold, and remains 9.23399% slower than paired ACLNN.

Matched-profile audit `d4cd7640...8959` accepts 96 target tasks per arm.
ACLNN/PTO task medians are 231.13/288.31 us; AICore medians are
221.7025/282.371 us. Against N256 PTO, task time improves 4.45718%, but
block-mean AICore time regresses 4.75314%. The 24x6 geometry therefore removes
enough task tail to pass the task threshold while the extra 33.3% tile-level
invocations increase average work. Because component and AICore thresholds
fail, the preregistered combined mechanism gate remains false.

This is real-hardware, state-free component evidence only. It has no online
request, vLLM, state-reuse, HBM-peak or TTFT result. Every formal, performance
and production-integration gate remains false.

## Balanced N192 PTO readiness (software evidence only)

Raw profile evidence strongly supports static N-tail imbalance but does not
directly expose per-core completion. AICore time is a block mean, and the old
5/4.5 max/mean ratio predicts 299.5094 us of the measured 301.76-us task.
This accounts for about 93.01% of task-minus-average-core. Host launch, Task
Wait, task counts and stream synchronization do not support an outer-envelope
explanation.

The selected source changes only `baseN=256` to 192 and its derived sizes and
partition: 144 tiles map as 24x6. L1/L0B/L0C use 352/48/24 KiB against
512/64/128-KiB limits. N192 increases tile-level invocations by 33.3%, so the
idealized 271.81-us estimate is a causal prediction, not measured evidence.
BiSheng compiles outer kernel `4a8118c2...caab`; embedded AICore
`b473038d...c008` passes the N192 E2/E3 audit with no E0 or N256
specialization. Focused tests pass 12/12.

No NPU execution, correctness sample, component latency, profile counter, HBM
measurement, online request, vLLM comparison or TTFT result belongs to N192.
Hardware remains blocked until fresh v20/v6 identities are generated from
clean pushed source and shown to invalidate v19/v5. All gates remain false.

That offline identity chain now accepts from clean pushed `1d1b3e0`.
Lowering closure/project-kernel root are `81e681f7...9cf` /
`b5307105...7384`; v20 execution artifact/config/plan are
`8290984d...6449` / `aa1ad4f...395` / `ddde3d39...4e685`. Pack-lock v6
`d8bcc56c...e570` explicitly invalidates v5 artifact/executor/plan while
preserving model and weight identities. This changes no hardware or
performance statement.

## PTO unit-flag phase readiness (software evidence only)

The one-variable source change compiles under the fixed BiSheng/CANN 9.0
environment. Kernel SHA-256 is
`d7465d87ea906c2e7bb6e48b165a725091fcb402d25d12ee1e0f691c5c719d9d`;
embedded AICore SHA-256 is
`99d977671109048c91aed4add17a8e845c9fb10ed380173d09e48b1b8eac22bd`.
The fail-closed fatbin audit accepts machine `0x1029`, all four required
Partial/Final specializations, and absence of Unspecified/E0. Focused Python,
CMake reproducibility, host partition/event, and shell contract tests pass.

The readiness audit also exposed and repaired a state-identity gap: dynamic PTO
code previously changed only the component identity while the global
project-kernel root remained ACLNN-only. The new lowering closure covers PTO
source, compiler, kernel, phase evidence and runtime libraries; it is an
external leaf of the project-kernel root and therefore changes the executor,
execution artifact, config and resident plan. Clean pushed `faf22d9`
generated accepted v19 artifact/config/plan `8cbbdf0e...a2be` /
`d2e6ccb5...db7a` / `7d989452...2ac9`. Lowering closure
`1bf434dc...32ae` independently reproduces project-kernel root
`eedbbc61...2051`. Pack-lock v5 `72134401...3aa` invalidates the prior v4
artifact/executor/plan while preserving model and weight leaves. No NPU
lifecycle, correctness sample, component
latency, profile counter, HBM value, online request, vLLM comparison or TTFT
measurement belongs to this candidate. Every formal/performance/integration
gate remains false.

Fresh physical-NPU7 component v1 completed the alternating ACL/PTO, PTO/ACL,
ACL/PTO sequence. ACLNN measured 29.177047, 28.928725 and 29.109997 ms; PTO
measured 32.463947, 32.600519 and 32.452208 ms. All six logits have SHA-256
`d2c09d74...5609` and match the independent oracle. Audit
`be517e516288daa99614722c93116c074f596e186abfed2eeafceb8c3224c21e`
accepts the first PTO smoke, identity `e64dce70...2835`, exits and cleanup.
Medians are 29.109997/32.463947 ms, leaving PTO 11.521643% slower
(0.896687x); the component gate fails. Relative to the preceding PTO median
32.495188 ms, the change is only -0.096140%. Peak ACL allocation is identical
at 58,372,862,016 bytes; minimum free HBM after execution is
6,391,644,160/6,391,775,232 bytes for ACLNN/PTO.

The sole matched profile also accepts exact logits and 96 target tasks per arm
under audit `9c4660db...d499`. ACLNN/PTO task medians are 231.44/301.76 us
and AICore medians are 221.974/269.5585 us. Against the preceding PTO trace,
task changes +0.009943% and AICore -0.105061%; neither passes the required 1%
reduction. PTO remains 30.383685%/21.436970% above ACLNN. PTO Cube/MAC/MTE1/
MTE2 are 89.2665%/0.090/0.233/0.648, effectively unchanged; FIX rises from
0.003 to 0.012. The emitted phase mechanism is observable but not
critical-path improving. NPU7 ends at 5% HBM, 0% AICore/AIVector and no device
process. All gates remain false.

The first versioned phase-threshold re-audit produced rejected audit
`d5115521...2192` without hardware work. Its only violations were
`run_commit` and both metadata parents because it equated clean runtime commit
`a040701` with the later documentation commit. The preserved raw thresholds
are nevertheless the same. A versioned auditor repair uses Git ancestry and
exact runtime-parent equality, matching the already accepted component
provenance model; v1 is never overwritten. Fresh v2
`c5498dc2cad9209a9521b3653b5acc9176d25a0931eab0d6ed4b0c7c7d4b514e`
accepts with no violations, exact correctness, task threshold 298.7127 us and
AICore threshold 267.14358 us both failed, and every gate false.

## Double-accumulator PTO readiness (software evidence only)

The active candidate allocates two 16-KiB FP32 accumulators at L0C addresses
0 and 16,384. Host tests accept the four/five-N-tile alternation, per-buffer
reuse waits and final two-store drain. BiSheng/CANN 9.0 emits an AICore fat
object with SHA-256 `e8c3c5a0...074be`; component identity v3 binds this
schedule and makes the prior single-accumulator closure stale.

No NPU lifecycle, correctness sample, latency, task time, utilization, HBM or
online result existed at the readiness boundary.

The offline closure is accepted: v18 execution artifact/config/resident plan
are `184b1754...944c`, `1cfa6909...d994`, and `a96ed44e...1460`.
Pack-lock v4 `a20a2f2a...81d6` explicitly invalidates pack-lock v3
`b29bc35a...b3a0` and its `b37aa129...f906` plan while preserving model and
weight leaves. This is derived readiness evidence only.

Fresh physical-NPU7 component v1 then completed three independent lifecycles
per arm. ACLNN measured 29.186767, 29.068646 and 29.054246 ms; PTO measured
32.381628, 32.590020 and 32.495188 ms. All six saved-logit SHA-256 values are
`d2c09d74...5609`, all frozen decisions are exact, every exit is zero, stderr
is empty, and six worker identities are unique. Independent audit SHA-256
`d2143a1a...1e9b` accepts with no violations.

The 29.068646/32.495188-ms medians mean PTO is 11.78776% slower
(0.894552x). Relative to the preceding cached-left PTO median
32.512021 ms, the change improves only 0.05177%. Peak ACL allocation is equal
at 58,372,862,016 bytes; minimum post-execution free HBM is
6,391,848,960/6,391,783,424 bytes for ACLNN/PTO. NPU7 and scoped host/container
processes are empty after each run and at suite end. Correctness passes, but
the component threshold, formal gate, performance claim and production
integration remain false. This is state-free component evidence, not online,
vLLM or TTFT evidence.

The sole matched profile pair also completed with exact outputs. Independent
audit SHA-256 `95c9345cc46773b0541269d72b54db41902a44a3c86ef7cee248ef8cf0e8bbca`
accepts 96 target tasks per arm and no violations. ACLNN/PTO task medians are
231.12/301.73 us; AICore medians are 221.7665/269.842 us; task-minus-AICore
is 9.3535/31.888 us. Cube utilization is 88.0835%/89.4015%; FIX, MAC, MTE1
and MTE2 ratios are respectively 0.004/0.003, 0.121/0.090, 0.300/0.233 and
0.988/0.648.

The candidate changes the preceding accepted PTO profile's task/AICore values
by only -0.0795%/+0.1169%, with effectively identical pipe ratios; its
task-minus-AICore interval shrinks only 1.7107%. Thus double accumulation does
not move the measured critical path. The aggregated trace cannot prove
whether FIX and Cube overlapped, but it does show that removing the
source-level immediate wait yielded neither an AICore reduction nor a
meaningful outer-task reduction. The accepted non-profile 3+3 result remains
the performance decision. Every formal, performance, integration and
production gate remains closed.

## Cross-N PTO reuse v2 audit-bound measurement

Fresh v2 executed the preregistered alternating physical-NPU7 3+3 component
suite. ACLNN elapsed times were 29.173159, 29.274670 and 29.160449 ms; PTO
elapsed times were 32.496681, 32.512021 and 32.876034 ms. Every process exited
zero, all six saved-logit files have SHA-256 `d2c09d74...5609`, and the first
PTO exact-correctness smoke passed. Medians are 29.173159 and 32.512021 ms,
so the candidate is 11.44498% slower. Peak ACL
allocation is identical at 58,372,862,016 bytes; final NPU7 and scoped-process
cleanup are empty.

These numbers are an accepted negative component result. The original
independent audit rejected only because it equated the lock's clean generation
commit `343b68f` with clean runtime commit `7333967`. A tracked lock cannot
exist in the commit from which its bytes are generated, so this equality is
self-referential. The rejected audit remains immutable. A schema-2 auditor now
preregisters a Git provenance-chain check: all runs share a clean pushed
runtime commit, its exact tracked lock blob matches the preserved copy, and
the generation commit is its ancestor. It retains every identity, output,
lifecycle and cleanup check. Clean-pushed versioned re-audit
`independent_audit_v2.json` accepts with no violations; its SHA-256 is
`951f495eb9b1af040b659995a226978f75654a1e71c248267bca3416e2c38241`.
Correctness passes, but the 32.512021-ms PTO median is 11.44498% above ACLNN,
so `component_performance_gate=false`, `formal_gate_open=false`,
`performance_claim=false`, and production integration remains forbidden.

The first clean-pushed lifecycle is retained as a pre-execution negative
event, not a component result. It stopped at the pack/resident-plan admission
check before ACL or any NPU task. The config bytes, semantic digest, accepted
weight root, and layer/global manifests still matched, but the historical
pack lock expected resident plan `24da1fad...ff52`; the current v8 plan is
`b1d64713...79abb`. An independent runtime-binding audit also rejects the old
execution artifact because both executor binary and compiler/build identities
changed. Cleanup passed with no NPU7 or scoped process residue. The required
repair is a full fresh artifact/config/plan/lock chain, not a one-field lock
update. No latency, throughput, task, or utilization measurement exists for
this attempt.

The offline repair is now complete but remains non-hardware readiness
evidence. Clean `343b68f` produced one v17 execution object. Runtime-binding
and independent audits accept artifact `05571008...d4bb`, config
`846483a7...547a`, resident plan `b37aa129...f906`, executor
`ad8ffea8...dea`, and compiler/build `55f7c04b...42f`. Pack-lock v3
`b29bc35a...b3a0` keeps the identical model, accepted weight root, and
layer/global packs while rejecting the old config, artifact closure, and plan.
This does not add a component measurement.

The first matched cross-N profile attempt adds no measurement either. Its
`Restart=no` unit failed with Bash exit 2 while parsing a multiline binary
conditional, before the runner initialized its output, invoked `msprof`,
started a worker, initialized ACL, or submitted an NPU task. Exact failure
custody, source-audit identity, process/device snapshots, and successful
cleanup are preserved under
`.benchmarks/qwen14b-pto-gate-up-cross-n-reuse-profile-npu7-v1`.
All profile fields are n/a. The fixed launcher precomputes the compared
digests and passes a syntax contract; fresh v2 was the only eligible retry.

Fresh matched profile v2 then completed and independently re-audits byte for
byte to accepted audit SHA-256
`e10c2f000b0b8f6f1eef6720a29ec0a34049e1126c9f239c26c19ff63b1e924b`.
Both arms select 96 Gate/Up tasks and reproduce logits SHA-256
`d2c09d74...5609`; all oracle decisions are exact. ACLNN task/AICore medians
are 230.92/221.6205 us, while cross-N PTO reports 301.97/269.527 us, making
PTO 30.768%/21.616% higher. Task-minus-AICore is 9.2995 us for ACLNN and
32.443 us for PTO. The summed target-task delta is 6.82126 ms across warmup
plus measured passes, or 3.41063 ms per 48-layer pass.

The mechanism did not improve its own profiler signature. Relative to the old
24-core PTO profile, task time rises 0.72 us (0.239%) and AICore time rises
0.503 us (0.187%); MTE1 remains 0.233, MTE2 changes 0.646 to 0.648, and Cube
utilization changes 89.3295% to 89.389%. ACLNN remains stable at 230.92 us
task time, 221.6205 us AICore, and 88.1745% Cube utilization. Thus the
source-level left-load reduction is not on the measured critical path. Static
geometry says it saves 13.125 MiB of left loads per layer beside an unchanged
270-MiB right operand, only a 4.575% modeled reduction in combined operand
bytes; the trace does not directly measure these bytes. Peak ACL allocation
and workspace remain identical at 58,372,862,016 and 5,147,681,280 bytes.
NPU7 and scoped processes are empty after both arms.

This is an accepted negative `real-hardware-component-profile`, not online or
profiler-timed performance evidence. The paired non-profile result remains
32.512021 versus 29.173159 ms; component, integration, performance, formal,
and production gates stay closed.

## PTO-ISA 24-core Gate/Up device profile (accepted diagnostic)

Fresh profile v2 from clean pushed `aa49114` completed one ACLNN and one PTO
process on physical NPU7. Both used the immutable artifact identity
`5a394d90...49e55`, physical B16, the same BF16 inputs/weights/config,
batch synchronization, frozen oracle and ACLNN SwiGLU. Each selected exactly
96 target tasks and produced saved logits SHA-256
`d2c09d74...5609`; all frozen decisions were exact. Independent audit
`3f168c19...b634` accepts with no violations.

ACLNN's target MatMul used 22 blocks; its median task duration/AICore time was
230.91/221.625 us. PTO used 24 blocks and measured 301.25/269.024 us, making
the task 30.46% longer and reported AICore time 21.39% longer. The summed
target-task delta is 6.765 ms across warmup plus measured passes, or 3.382 ms
per 48-layer pass. This is close to, but does not replace, the immutable
unprofiled 3.447-ms residual.

PTO's median Cube utilization is 89.3295%, slightly above ACLNN's 88.0765%, so
low aggregate Cube utilization is rejected. PTO's MAC/MTE1/MTE2 ratios are
0.090/0.233/0.646 versus ACLNN's 0.121/0.301/0.988. MTE2 is PTO's dominant
reported pipe, but it is less active than ACLNN; the trace does not show
greater MTE2 saturation. PTO's task-minus-AICore interval is 32.226 us versus
9.285 us. These task-aggregated facts support missing overlap, pipeline
bubbles, or task-tail work in the project kernel. They do not distinguish
those causes or provide per-core end times, so the static 12x5+12x4 tail is
not directly confirmed.

The implementation loops N outside K, reloading the shared input activation
for every one of a core's four or five N tiles and completing a store at each
tile boundary. Cross-N left-activation reuse plus right-load/compute/store
overlap is the next source-supported hypothesis; it is not implemented in this
milestone. Both arms report 55,668.70 MiB peak ACL allocation and 4,909.21 MiB
workspace peak. All exits are zero, application stderr is empty, and NPU7,
worker, profiler and scoped docker-exec cleanup is empty. This is
`real-hardware-component-profile`, not online or profiler-timed performance
evidence. `formal_gate_open=false`, `performance_claim=false`, and production
integration remains forbidden.

The clean v1 run produced a complete ACLNN application/profile/export and
passed exact decisions, saved-logit SHA-256 and target-task selection, but it
is rejected as paired evidence. Its host cleanup detector selected the
detector's own `awk` process because the program text contained `docker` and
`exec`; PTO never started. Actual NPU7 and container cleanup passed. The
immutable v1 bundle is retained, while fresh v2 restricts host residue matches
to processes whose executable name is exactly `timeout`, `sudo`, or `docker`.

## PTO-ISA 24-core Gate/Up component gate (negative)

NPU7 reports 24 AICore/Cube cores. The rejected-but-correct v3 kernel used only
18 uniform blocks for 108 256-column output tiles. A new project-owned
candidate preserves all tile, buffering, accumulation, layout and activation
choices while assigning five contiguous tiles to cores 0--11 and four to
cores 12--23. This reduces the ideal critical-path tile count from six to five
without changing arithmetic or output coverage.

BiSheng compiles the new AICore fat object; its SHA-256 is
`d190a60e1f0601c24be4c87291ecd702d490c25b93d33c46428df10c9a94a578`.
Executable host tests prove all 108 tiles are covered exactly once and source
contracts bind the device mapping. Python identity tests prove a partition
change changes the component digest.

The fresh NPU7 3+3 suite completed all six independent lifecycles. All 96
frozen greedy decisions were exact, all logits were finite, and saved logits
were bit-identical across arms. ACLNN times were
29.099351/29.123701/29.068831 ms (median 29.099351 ms); PTO times were
32.546557/32.590717/32.429687 ms (median 32.546557 ms). Thus the balanced
partition improves the old 18-core PTO median by 5.3444% (1.05646x), but
remains 11.8463% slower than paired ACLNN (0.894084x).

Independent audit accepted the complete bundle with zero violations under
artifact identity
`5a394d90b8f687c5849e08beb72cf5102e079dec6cba9379a009c6a90c949e55`.
Correctness passes, while component integration, production integration,
performance claim and formal gates remain closed. NPU7 returned to 3,415 MiB
idle HBM with no NPU or scoped worker/docker-exec process. This state-free B16
component result provides no online, vLLM, TPOT, TTFT, or state-graph claim.

## PTO-ISA Gate/Up component gate (negative)

The fresh v3 gate ran three independent ACLNN control and three independent
PTO-ISA candidate lifecycles on physical NPU7. Every process exited cleanly;
all 96 frozen greedy decisions were exact, all logits were finite, and every
saved logits file had the same SHA-256
`d2c09d7487a035a34ecfffa714f21230ce4c98ef81b82068d9ac6725538c5609`.
The independent auditor accepted the bundle with zero violations under
artifact identity
`1b36bea118f9371749115801fb92831356ba662d721144abe87a76502345836e`.

ACLNN elapsed times were 29.085/29.117/29.014 ms (median 29.085 ms); PTO-ISA
times were 34.489/34.384/34.356 ms (median 34.384 ms). Thus the candidate
achieved only 0.8459x of ACLNN performance and increased latency by 18.22%.
Correctness passes, but `component_integration_gate_open=false`,
`performance_claim=false`, and `formal_gate_open=false`. This is a
state-free physical-B16 component result, not online serving, vLLM, decode
TPOT, TTFT, or state-center performance evidence. NPU7 returned to its idle
HBM baseline with no NPU or scoped worker/docker-exec process.

### Readiness and rejected pre-execution attempts

The official `cann/pto-isa` source is pinned as a submodule at
`2d60f21c4e22645f5aa3fc22c2a4a8818eaa4d81`. A project-owned Ascend 910B2
kernel now compiles the exact Qwen physical-B16 Gate/Up shape with BF16 inputs,
FP32 accumulation, direct output-major/DN weight access and BF16 output.
BiSheng emits a fat object with a non-empty `.aicore_binary` section and the
stable host launch symbol. The native full-model component probe can load it
only through a component override; protocol-worker mode rejects that override
before resident config/state admission.

Focused contracts and identity tests pass. The artifact identity binds 4,560
PTO indexed entries, the exact PTO commit, project sources, compiler and flags,
kernel ELF, native probe and 37 resolved runtime/loader libraries. This is
compilation, isolation and provenance readiness for the measured gate above.

The first clean invocation did not reach hardware: the inherited historical
component runner passed a 220-byte schema-3 execution config to the current
256-byte schema-4 worker. It exited 2 before ACL initialization and failure
cleanup left NPU7 and all scoped processes empty. The repair selects the
already accepted fused schema-4 config, while a new lock binds its exact hash,
semantic identity, current revision-10 resident plan, 48 layer packs and
global pack. This is a fail-closed configuration correction, not a timing
result; all component performance fields remain n/a.

The fresh schema-4 v2 invocation also stopped before hardware. An over-escaped
`awk` slash in runtime-closure parsing yielded no dependency leaves, so the
identity builder rejected the invocation. Cleanup again left NPU7 and scoped
processes empty. The parser now uses `ldd` fields rather than slash regexes and
has an explicit nonempty-closure gate. This is runner validation evidence, not
a component timing sample.

## Revision-10 workflow-cohort c32/o32 diagnostic

One Native and one pinned-vLLM lifecycle ran sequentially on NPU4 from clean
`1fc7a2a`. Both completed 128 real online requests and all 4,096 frozen-oracle
tokens with zero failures. Native client concurrency was 32 over physical B16.
It formed exactly eight B16 append and 248 B16 decode batches, kept two B16
cohorts resident in each client cycle, incurred zero state-slot wait, recycled
all branches, and recorded hit rate 1.0 plus 262,144 effective reused tokens.

Native/vLLM measured 10.3568/15.0274 request/s and
331.4176/480.8767 output token/s. Wall P50/P95/P99 was
2568.33/3148.80/3152.25 ms versus 2089.60/2173.75/2183.95 ms; TPOT was
66.68/79.34/79.37 ms versus 45.75/49.63/56.80 ms. Peak HBM was
40,548/53,461 MiB. Thus Native request throughput remains 31.08% lower and
TPOT P50 45.75% higher, although peak HBM is 24.15% lower. vLLM does not expose
an equivalent hit/reuse counter in this evidence, so those fields remain n/a.

The first offline comparison was rejected by an auditor bug on an expected
optional null workflow marker. Both serving lifecycles had already exited zero
and were not rerun. Auditor revision `workflow-marker-null-v2`, committed in
`8419592` with source SHA `17c88e30...94fe`, re-audits the same immutable
records with zero violations. The result is an accepted diagnostic only:
`formal_gate_open=false`, one lifecycle per runtime, and no cross-runtime TTFT
comparison. It proves that workflow/resource-state scheduling repaired the
fragmentation, not that Native decode now matches vLLM.

## Scheduler-plan v9 workflow-cohort repair (software-only)

The rejected revision-10 c32/o32 lifecycle was traced to a precise resource
model error. Its online source state contains 2,048 tokens (16 blocks), and
each 129-token branch append needs two blocks. Thirty-two co-resident branches
therefore require 80 blocks. The former projection used a 2,177-token source
and one private block per branch (50-block minimum), while runtime admission
independently overcharged each append as three blocks by including future
decode output. That combination reproduces the observed B16/B5/B2/B1 waves.

The repaired Rust runtime charges the immediate append as exactly 129 tokens
and two blocks, then charges decode growth at subsequent quanta. A new bounded
workflow-cohort policy forms compatible B16 append batches, releases partial
work after a configured bound, honors existing deadline/starvation guards, and
prevents decode starvation with a two-prefill-batch limit. Unit tests show 32
online append requests forming two B16 plans under the exact block budgets;
the full Rust and related contract suites pass.

Scheduler-plan identity is now v9 and binds both new policy names and every
cohort parameter. The arena-80 physical layout and source/private-block
projection also change their existing identity inputs, so the rejected v8
state chain cannot be reused. No NPU or baseline lifecycle belongs to this
software result yet; request/s, token/s, latency, TPOT, HBM, error rate, hit
rate, effective reuse, and any decode-speed conclusion remain unavailable.

The fresh software chain was then generated from clean pushed `899e542`.
Artifact/config remain byte-identical because the C++ execution object did not
change (`803484fa...c8abb` / `55b10efb...2b552`), while resident plan,
cache layout, scheduler plan, Rust server, and aggregate compatibility are
`18f50e06...5407`, `bf559b24...5e9e`, `0f2e98f2...efe9`,
`721ce770...6dff`, and `c0b91ada...32bb`. Independent recomputation reports
zero mismatches. This is identity/readiness evidence, not an online result.

## Open runtime-state graph contract (software-only, non-performance)

The Rust control plane now has a generic `RuntimeStateGraph` whose nodes are
not required to contain tokens or KV and whose type namespace is extensible.
Each node binds its type/schema, canonical payload SHA-256, and exact upstream
handle/generation/identity edges into an independently recomputed SHA-256.
Insertion fails closed for an edited identity, a missing or mismatched
dependency, or a stale generation. Replacing an upstream object invalidates
the full live dependent closure; tests cover a weights -> execution -> Qwen
continuation chain and independent execution, placement, and workflow nodes.

This is a lifecycle/identity contract, not evidence that all state classes are
materialized by the Qwen adapter. The current physical implementation remains
weighted toward continuation descriptors and paged `MODEL_KV`; the three new
root nodes materialize their identity/lifecycle boundary, not every possible
execution, placement, or application payload. No NPU,
online request, or baseline ran, so all performance metrics are n/a and no
decode-speed claim follows.

The contract is now wired into the Native serving actor. Actual spawn creates
execution, placement, and workflow/deployment roots; completion publishes or
advances continuation nodes before handle visibility; admission checks both
the resident map and exact graph payload; and every eviction/cancel/abandoned
response path invalidates the graph projection. Runtime tests observe three
roots plus two live continuations, reject a resident-map entry after its graph
node is removed without dispatching a batch, and preserve generation-safe slot
reuse. This remains mock-worker/software evidence, not a real online or NPU
result.

Existing diagnostic timing files were also re-aggregated without generating a
new run. Median B16 decode preparation/H2D is 0.216--0.233 ms, or about
0.60--0.62% of 36.16--38.63 ms median executor time. Persistent cohort
metadata is therefore a bounded small optimization, not evidence explaining
the vLLM gap. No performance table or claim changes.

The next software-readiness repair extends the frozen execution chain through
the actual Rust launch boundary. Scheduler-plan domain v8 binds the Rust
service binary and the content of every resolved ELF dependency; it also binds
the schema-v3 digest, physical-layout digest, resident plan, and aggregate
state-compatibility digest. This contract was preregistered before the fresh
clean-parent generation below. It contains no NPU, request, token, or
performance evidence.

That single clean-parent generation has now completed. The C++ artifact/config/
resident identities are `803484fa...c8abb`, `55b10efb...2b552`, and
`26e04362...6407`; the Rust service/ELF-closure identities are
`e689b37c...570e` and `77f0485e...fb64`. Schema v3, cache-layout,
scheduler-v8, and aggregate identities are `a130e3e4...d94`,
`d96def03...acb2`, `8d226273...8e0`, and `a91d5de4...ceb1`.
Generator-internal and external recomputation both pass. A pre-v3 fixture exits
1 with schema and aggregate mismatches. NPU4 remained empty and no service,
request, token, HBM allocation, baseline, or performance measurement ran.

## State-graph c32/B16 deployment projection (software-only, non-performance)

The revision-10 Qwen adapter now validates why its logical and physical
capacities exist instead of accepting an unproven tuple of allocator constants.
For one retained 2,177-token workflow source and client concurrency 32, the plan
derives 33 continuation descriptors and 50 physical 128-token blocks: 18 for
the source and one private partial-tail COW block per branch. The configured
arena is 64 blocks and physical execution remains B16; client c32 is not
physical B32.

The workflow facts, capacities and cohort are committed to resident-plan
identity domain v7. Native tests create the source and all 32 branches in two
B16 reservations, observe 33 active descriptors, 50 used/17 shared/14 free
blocks and 32 COW copies, then reclaim every branch and the source. Undersized
descriptor and block configurations fail closed. This is software contract
evidence only: no NPU or online lifecycle ran, so request/s, output token/s,
latency, TPOT, HBM, error rate, state-hit rate and effective reuse are all n/a.
It does not show that the c32 capacity wave has been removed online or that one
decode token executes faster.

As a fail-closed check, the runtime-binding auditor was run against the frozen
v3/domain-v6 artifact and the current worker. It exits nonzero and reports both
executor-binary and compiler/build mismatches before ACL. A new artifact chain
must therefore be generated from a clean pushed commit; the historical v3
object cannot be reused or relabeled.

## Revision-10 paged MODEL_KV integration (software-only, non-performance)

The production Qwen worker now places the MODEL_KV component of each inference
continuation in a project-owned block pool. Forks share immutable prefix
blocks; an append to a shared partial tail plans a private block and copies only
valid tokens. Logical continuation descriptors remain distinct and
generation-tagged. A shadow Reserve/Commit/Abort transaction spans allocator
planning, COW copies, ACL execution, synchronization, D2H result checks and
publication, so an unsuccessful cohort leaves previous state visible.

Native protocol v2 reports logical descriptor capacity separately from total,
used, free and shared physical blocks, block geometry and committed COW count.
Rust enforces both worker-reported budgets. Executor revision 10, resident
identity domain v6, cache-layout v2 and scheduler-plan identity v7 invalidated
the former fixed-row interpretation. Cross-language goldens, 24 native CTests,
89 Rust tests and the repository contract suite cover the software boundary.
No NPU process or online request was run for this milestone, so it establishes
no correctness, HBM, latency, throughput, capacity or decode-speed result.

## Inference-state schema v3 contract (software-only, non-performance)

The state-center abstraction represents a versioned inference
continuation rather than equating state with a KV-backed token prefix. Its
known component classes cover token/position progress, model KV, sampler/RNG,
constraint machines, speculative decoding, workflow state and execution
cursors. The generic Rust center can own, lease and evict non-KV
continuations, while only token/position plus KV continuations participate in
token-prefix matching. The current native Qwen2.5 executor declares exactly
that two-component subset and rejects other valid component classes before
dispatch.

The descriptor and continuation graph-node SHA-256 are mandatory in serialized
records and native HTTP handles; old schema-v2 objects cannot be implicitly
upgraded. Their canonical schema material is
SHA-256 hashed by a project binary and used by the native launcher as
`state_schema_digest`, so the aggregate state compatibility identity changes
from the former slot/KV-only schema. Unit and contract coverage verifies
non-KV lifecycle management, prefix-index separation, unknown/unsupported
component rejection, lineage-sensitive generations and failure to deserialize
pre-v3 handles. This milestone ran
no NPU process and adds no online correctness or performance evidence. The
final software validation passes 100 Rust library tests plus every binary
target, 234 repository benchmark/document tests with six expected environment
skips, and all 25 native CTests; strict formatting and Clippy with warnings
denied also pass.

## Qwen2.5-14B independent two-token oracle (non-performance)

`results/20260717-qwen14b-generation-oracle-2-v1/` records the first
clean-commit real-Ascend correctness reference for the configuration-driven
Qwen2 dense expansion target. Qwen2.5-14B-Instruct BF16 runs on one Ascend
910B2 with the fixed four-token prompt `[1397, 64424, 44378, 5942]`; independent
Transformers/Torch-NPU eager execution emits greedy tokens `[525, 264]`.

The first token covers embedding, all 48 decoder layers, final norm and LM
head. The second token additionally exercises checkpoint-created KV state and
one decode step. The pinned model manifest covers 579 tensors and fully hashes
all shard payloads; its serving execution sidecar separately binds structural
semantics and the accepted-weight root. This is an offline oracle only. It
does not execute the project-owned native candidate, compare with vLLM, or
support a latency/throughput claim.

## Qwen2.5-14B configuration-driven native end-to-end gate (non-performance)

`results/20260717-qwen14b-native-config-driven-e2e-v1/` records the first
clean-commit real-Ascend execution of the project-owned resident C++/ACL engine
on the complete Qwen2.5-14B-Instruct BF16 model. Both 7B and 14B now consume
the same strict binary execution record and immutable resident-plan path; the
14B run derives all 48 layers, hidden/intermediate geometry, GQA heads, packed
offsets, buffers, attention scale, and paged-KV capacity from configuration.
There is no model-name dispatch, Torch, Transformers, or vLLM in the candidate
execution.

On one Ascend 910B2, the fixed four-token prefill selects token `525`; the
incremental decode step selects `264`; a real batch-shaped decode of four
physical state rows produces `[264, 264, 264, 264]`; and two-token generation
reproduces `[525, 264]`. Resident weights occupy 29,540,558,848 bytes, four
all-layer paged-KV states occupy 3,221,225,472 bytes, peak live ACL allocation
is 33,034,781,296 bytes, and 31,763,554,304 bytes of HBM remain free after the
gate.

This artifact is labeled `real-hardware-component-probe`, not `real-online`.
It deliberately records `performance_claim=false`: it has no request server,
arrival stream, timing repetitions, or paired vLLM-HUST run. It also records
`tensor_tolerance_parity=false`. Embedding is bit-exact and greedy decisions
match the independent oracle, but BF16 intermediate differences accumulate
beyond the current element-wise tolerance. The accepted claim is therefore
configuration-driven full-model execution with scoped token-level parity, not
full tensor equivalence or a performance advantage.

## Qwen2.5-14B vLLM control baseline c4/o32 (partial)

`results/qwen14b-vllm-control-c4-o32-v1-suite.json` records the first formal
Qwen2.5-14B BF16 control-group baseline cell for pinned vLLM-HUST +
vLLM-Ascend-HUST on one Ascend 910B2. It covers concurrency 4, output length
32, 128 measured requests per lifecycle, 10 warmup requests, and three clean
service lifecycles for each workload. Both workloads use batch-invariant
`PIECEWISE` execution and an isolated compilation cache per lifecycle.

The `shared_prefix` control keeps the frozen 2,177-token prompt unchanged and
validates the returned prompt token IDs against
`a1a3b1e05988a4c0732495d4e665956b28fe9ea73f57b8a2699cf1c13c605e8b`.
Across three lifecycles it reports median 3.368 request/s, 107.778 output
token/s, P95 wall latency 1209.51 ms, P99 wall latency 1221.55 ms, TPOT P50
34.49 ms and peak HBM 53,466 MiB.

The `independent_cold` control inserts per-request identity before the common
body. The source prompt remains the frozen 2,177-token manifest, but measured
requests are 2,215 tokens and all 128 measured prompt token-ID hashes differ
within each lifecycle. Across three lifecycles it reports median 1.823
request/s, 58.333 output token/s, P95 wall latency 2280.14 ms, P99 wall latency
2331.25 ms, TPOT P50 43.80 ms and peak HBM 53,466 MiB.

This is `real-online` baseline evidence only. The shared-prefix and
independent/cold workloads now have native formal c4/o32 counterparts below,
but the full control matrix is still missing. Native and vLLM TTFT remain
non-comparable, so this result must not be used to claim TTFT acceleration.

`benchmarks/summarize_vllm_control_suite.py` now provides a reusable control
suite summarizer for future vLLM baseline cells. It requires both
`shared_prefix` and `independent_cold` workloads to have at least three clean
`real-online` lifecycles, 128 measured requests per lifecycle, complete raw and
warmup records, empty client stderr, NPU cleanup snapshots, no correctness
oracle, `ttft_cross_runtime_comparable=false`, the frozen 2,177-token prompt
SHA-256, and the expected prompt hash cardinality: one for shared-prefix and
128 for independent/cold.

`results/qwen14b-vllm-control-v5-c4-o1-suite.json` records the formal vLLM
control baseline cell at concurrency 4 and output length 1 from clean commit
`2094b8c`. Both workloads use Qwen2.5-14B BF16, the frozen 2,177-token prompt
source, greedy fixed-length generation, batch-invariant `PIECEWISE` execution,
an isolated compilation cache per lifecycle, 128 measured requests and 10
warmups. Across three `shared_prefix` lifecycles it reports median 43.268
request/s and output token/s, P95 wall latency 94.30 ms, P99 wall latency
101.77 ms and peak HBM 53,466 MiB. Across three `independent_cold` lifecycles
it reports median 3.629 request/s and output token/s, P95 wall latency
1281.44 ms, P99 wall latency 1291.36 ms and peak HBM 53,464 MiB. TPOT is null
for output length 1. This is a vLLM baseline cell only; together with the
native c4/o1 shared-prefix-extension and independent/cold cells below, it fills
the paired c4/o1 control evidence without making a TTFT acceleration or broad
serving-performance claim.

`results/qwen14b-vllm-control-v6-c4-o128-suite.json` records the formal vLLM
control baseline cell at concurrency 4 and output length 128 from clean commit
`a15b32c`. Both workloads use the same Qwen2.5-14B BF16 model, frozen
2,177-token prompt source, greedy fixed-length generation, batch-invariant
`PIECEWISE` execution, isolated compilation caches, 128 measured requests and
10 warmups. Across three `shared_prefix` lifecycles it reports median 0.850
request/s, 108.809 output token/s, P95 wall latency 5002.66 ms, P99 wall
latency 5084.27 ms, TPOT P50 35.81 ms and peak HBM 53,466 MiB. Across three
`independent_cold` lifecycles it reports median 0.705 request/s, 90.228 output
token/s, P95 wall latency 5968.67 ms, P99 wall latency 6144.58 ms, TPOT P50
38.01 ms and peak HBM 53,466 MiB. This is a vLLM baseline cell only; together
with the native c4/o128 shared-prefix-extension and independent/cold cells
below, it fills the c4/o128 paired control evidence without making a TTFT
acceleration or broad serving-performance claim.

`results/qwen14b-vllm-control-v2-c1-o1-suite.json` records the next formal
vLLM control baseline cell at concurrency 1 and output length 1 from clean
commit `9e690e8`. Both workloads again use Qwen2.5-14B BF16, the frozen
2,177-token prompt source, greedy fixed-length generation, batch-invariant
`PIECEWISE` execution, an isolated compilation cache per lifecycle, 128
measured requests and 10 warmups. Across three `shared_prefix` lifecycles it
reports median 20.842 request/s and output token/s, P95 wall latency 49.49 ms,
P99 wall latency 52.95 ms and peak HBM 53,466 MiB. Across three
`independent_cold` lifecycles it reports median 2.863 request/s and output
token/s, P95 wall latency 353.64 ms, P99 wall latency 357.41 ms and peak HBM
53,465 MiB. TPOT is null for output length 1. This is a vLLM baseline cell
only; the matching native shared-prefix-extension c1/o1 formal cell is recorded
below, but the full control matrix is still incomplete.

`results/qwen14b-vllm-control-v3-c1-o32-suite.json` records the formal vLLM
control baseline cell at concurrency 1 and output length 32 from clean commit
`5e9876a`. Both workloads use Qwen2.5-14B BF16, the frozen 2,177-token prompt
source, greedy fixed-length generation, batch-invariant `PIECEWISE` execution,
an isolated compilation cache per lifecycle, 128 measured requests and 10
warmups. Across three `shared_prefix` lifecycles it reports median 0.898
request/s, 28.724 output token/s, P95 wall latency 1190.16 ms, P99 wall
latency 1238.39 ms, TPOT P50 33.01 ms and peak HBM 53,467 MiB. Across three
`independent_cold` lifecycles it reports median 0.708 request/s, 22.661 output
token/s, P95 wall latency 1513.91 ms, P99 wall latency 1542.75 ms, TPOT P50
32.65 ms and peak HBM 53,466 MiB. The control client has no correctness oracle
and keeps `ttft_cross_runtime_comparable=false`; this is a vLLM baseline cell
only. Together with the native c1/o32 shared-prefix-extension and
independent/cold cells below, this fills the paired c1/o32 control evidence, but
the full control matrix and broad serving-performance conclusion remain
incomplete.

`results/qwen14b-vllm-control-v4-c1-o128-suite.json` records the formal vLLM
control baseline cell at concurrency 1 and output length 128 from clean commit
`6926aea`. Both workloads use the same Qwen2.5-14B BF16 model, frozen
2,177-token prompt source, greedy fixed-length generation, batch-invariant
`PIECEWISE` execution, isolated compilation caches, 128 measured requests and
10 warmups. Across three accepted `shared_prefix` lifecycles
(`r1d`, `r2`, `r3`) it reports median 0.229 request/s, 29.275 output token/s,
P95 wall latency 4785.15 ms, P99 wall latency 4872.70 ms, TPOT P50 33.50 ms
and peak HBM 54,865 MiB. Across three `independent_cold` lifecycles
(`r1`, `r2`, `r3`) it reports median 0.212 request/s, 27.152 output token/s,
P95 wall latency 4980.83 ms, P99 wall latency 5046.63 ms, TPOT P50 33.81 ms
and peak HBM 53,466 MiB. The earlier `shared_prefix` attempts `r1`, `r1b` and
`r1c` are retained as failed provenance and are not included in the suite. This
is a vLLM baseline cell only; together with the native c1/o128
shared-prefix-extension and independent/cold cells below, it fills the paired
c1/o128 control evidence without making a TTFT acceleration or broad serving
performance claim.

`benchmarks/audit_qwen14b_control_c1.py` now audits the completed c1 paired
control evidence for output lengths 1, 32 and 128. It checks native
shared-prefix-extension, native independent/cold, and vLLM
shared-prefix/independent-cold lifecycles for clean parent commits, 128 raw
requests per lifecycle, correct prompt hash cardinality, exact native oracle
validation, vLLM control-oracle absence, NPU 0 cleanup and
`ttft_cross_runtime_comparable=false`. The passing audit covers the completed
c1 paired cells and does not replace the broader control matrix.

## Qwen2.5-14B native control c4/o32 (partial)

`results/qwen14b-native-control-v2-c4-o32-suite.json` records native
C++/ACL control evidence for Qwen2.5-14B BF16 at concurrency 4 and output
length 32. It uses a 512 MiB resident workspace, which produces state
compatibility digest
`146733780ed6a30a4cf72ccfeff889acc34ccd036b8a63ef7c93c00610f1b0bc`;
the failed 256 MiB attempt is retained in
`results/qwen14b-native-control-prefix-extension-v1-c4-o32-r1/` and fails
closed with `workspace arena capacity exceeded`. That workspace change is part
of the resident plan identity, so states from the failed 256 MiB plan are not
compatible with the accepted 512 MiB runs.

The shared-prefix-extension workload seeds a 2,048-token state, extends the
remaining 129 prompt tokens, and checks the 32 generated tokens against the
frozen Qwen2.5-14B greedy oracle. Across three clean lifecycles, all 128
requests per lifecycle are exact, temporary branches are recycled, hit rate is
1.0, effective reuse is 262,144 tokens per lifecycle, median throughput is
0.723 request/s and 23.122 output token/s, P95 wall latency is 5596.49 ms,
TPOT P50 is 32.36 ms, and peak HBM is 58,342 MiB.

The mixed hot/cold workload uses the same frozen 2,177-token prompt and oracle,
with 96 exact-hot and 32 forced-cold requests per lifecycle. Across three clean
lifecycles, all outputs are exact, temporary states are recycled, hit rate is
0.75, effective reuse is 208,992 tokens per lifecycle, median throughput is
2.429 request/s and 77.731 output token/s, P95 wall latency is 1655.20 ms, and
peak HBM is 58,342 MiB.

This remains `real-online-smoke`, not a final performance claim: the native
control workloads are not yet a full matrix, and the mixed workload is not a
fully independent/cold prompt family with separate per-prompt greedy oracles.
Do not compare native internal TTFT with vLLM SSE TTFT.
`benchmarks/audit_qwen14b_control_c4_o32.py` verifies this boundary by checking
that the native c4/o32 control lifecycles remain `real-online-smoke` with
`performance_claim=false`, raw request records, clean parent metadata, empty
stderr captures, zero native client exit codes, NPU 0 cleanup snapshots, and
the retained 256 MiB workspace failure evidence.

The native shared-prefix-extension launcher now has a separate formal entry
path for future reruns: when writing to `results/`, it requires at least 128
measured requests, the frozen 2,177-token prompt, a 2,048-token retained prefix
with 129 extension tokens, the 512 MiB resident workspace, the frozen 10 ms
batch window, `real-online` evidence, and `--claim-eligible`. Existing v2
artifacts above were produced before that formal entry point and remain
smoke-labeled; they must not be retroactively upgraded.

`results/qwen14b-native-control-prefix-extension-v3-c4-o32-r{1,2,3}` is
retained only as failed provenance: those runs were launched with 14B labels
but defaulted to non-14B execution artifacts, with `kv_bytes_per_token=57344`
instead of the Qwen2.5-14B value 196,608. Each directory has a `FAILED.txt`
marker and the derived v3 suite has `qwen14b-native-control-prefix-extension-v3-c4-o32-suite.FAILED.txt`.

`results/qwen14b-native-control-prefix-extension-v4-c4-o32-suite.json` records
the first formal native Qwen2.5-14B shared-prefix-extension c4/o32 cell from
clean commit `8d4e0b0`. The run metadata records explicit 14B artifact paths
for layers, global pack, execution config, operator fixture, full oracle and
decode oracle; `kv_bytes_per_token=196608`; and parent `dirty=false`. Across
three lifecycles, all 128 requests per lifecycle are exact, `hit_rate=1`,
effective reuse is 262,144 tokens per lifecycle, stderr is empty, native client
exit code is 0, and NPU 0 has no residual process after shutdown. Suite median:
0.718 request/s, 22.976 output token/s, P95 wall latency 5650.17 ms, P99 wall
latency 5659.90 ms, TPOT P50 32.54 ms and peak HBM 58,343 MiB. This is one
native shared-prefix-extension control cell only; it is not a full matrix.

`results/qwen14b-native-independent-cold-v2-c04-o032-r01/` is retained only as
failed provenance. The client-side run reached real online request execution
and wrote a passing `result.json`, but the launcher failed while writing
`run_metadata.json` because three deployment-limit jq bindings were missing.
The metadata file is zero bytes, so this directory must not be aggregated or
used for claims.

`results/qwen14b-native-independent-cold-v3-c04-o032-suite.json` records the
formal native Qwen2.5-14B independent/cold c4/o32 paired-control cell from
clean commit `a77987d`. The run metadata records explicit 14B artifact paths,
`kv_bytes_per_token=196608`, `max_prefill_rows=9216`, `max_decode_batch=32`,
`state_capacity=33`, and parent `dirty=false`. Across three lifecycles, all
128 requests per lifecycle are exact against the frozen 128-row per-prompt
oracle family, `hit_rate=0`, `effective_reused_tokens=0`, temporary states are
recycled, stderr is empty, native client exit code is 0, and NPU 0 has no
residual process after shutdown. Suite median: 1.759 request/s, 56.303 output
token/s, P95 wall latency 2293.21 ms, P99 wall latency 2347.53 ms, TPOT P50
47.59 ms and peak HBM 59,931 MiB. This completes the native c4/o32 paired
control cells for shared-prefix-extension and independent/cold, but not the
full control matrix.

`benchmarks/summarize_native_prefix_extension_suite.py` now accepts
one-token shared-prefix-extension cells where TPOT is null. This preserves the
same formal checks as the c4/o32 summary while allowing output length 1 to be
summarized without inventing post-first-token timing.

`results/qwen14b-native-control-prefix-extension-v8-c4-o1-suite.json` records
the native Qwen2.5-14B shared-prefix-extension c4/o1 formal cell from clean
commit `2094b8c`. The three lifecycles use explicit 14B artifact paths,
`kv_bytes_per_token=196608`, 512 MiB workspace, `max_prefill_rows=9216`,
`max_decode_batch=32`, `state_capacity=33`, 128 measured requests, all exact
outputs, `hit_rate=1`, 262,144 effective reused tokens per lifecycle, empty
stderr, client exit code 0, and no NPU 0 residual process after shutdown. Suite
median: 0.875 request/s and output token/s, P95 wall latency 4614.13 ms, P99
wall latency 4632.79 ms and peak HBM 59,930 MiB. TPOT is null for output
length 1.

`results/qwen14b-native-independent-cold-v4-c04-o001-suite.json` records the
native Qwen2.5-14B independent/cold c4/o1 formal cell from clean commit
`2094b8c`. It reuses the frozen 128-row independent/cold prompt family and the
o32 oracle family while requesting one output token. Across three lifecycles,
all 128 requests per lifecycle are exact, `hit_rate=0`,
`effective_reused_tokens=0`, temporary states are recycled, stderr is empty,
client exit code is 0, and NPU 0 has no residual process after shutdown. Suite
median: 3.275 request/s and output token/s, P95 wall latency 1239.55 ms, P99
wall latency 1243.57 ms and peak HBM 59,930 MiB. Together with the vLLM c4/o1
baseline above, this fills c4/o1 paired control evidence only; the full control
matrix remains incomplete.

`results/qwen14b-native-control-prefix-extension-v9-c4-o128-suite.json`
records the native Qwen2.5-14B shared-prefix-extension c4/o128 formal cell
from clean commit `a15b32c`. The three lifecycles use explicit 14B artifact
paths, `kv_bytes_per_token=196608`, 512 MiB workspace,
`max_prefill_rows=9216`, `max_decode_batch=32`, `state_capacity=33`, 128
measured requests, all exact outputs, `hit_rate=1`, 262,144 effective reused
tokens per lifecycle, empty stderr, client exit code 0, and no NPU 0 residual
process after shutdown. Suite median: 0.461 request/s, 58.980 output token/s,
P95 wall latency 8777.19 ms, P99 wall latency 8802.45 ms, TPOT P50 32.48 ms
and peak HBM 59,930 MiB.

`results/qwen14b-native-independent-cold-v5-c04-o128-suite.json` records the
native Qwen2.5-14B independent/cold c4/o128 formal cell from clean commit
`a15b32c`. It uses the frozen 128-row independent/cold prompt family and the
o128 oracle family. Across three lifecycles, all 128 requests per lifecycle are
exact, `hit_rate=0`, `effective_reused_tokens=0`, temporary states are
recycled, stderr is empty, client exit code is 0, and NPU 0 has no residual
process after shutdown. Suite median: 0.743 request/s, 95.108 output token/s,
P95 wall latency 5419.21 ms, P99 wall latency 5491.16 ms, TPOT P50 36.18 ms
and peak HBM 59,930 MiB. Together with the vLLM c4/o128 baseline above, this
fills c4/o128 paired control evidence only; higher-concurrency control cells
remain incomplete, and TTFT remains cross-runtime non-comparable.

`benchmarks/audit_qwen14b_control_c4.py` now audits the completed c4 paired
control evidence for output lengths 1, 32 and 128. It checks native
shared-prefix-extension, native independent/cold, and vLLM
shared-prefix/independent-cold lifecycles for clean parent commits, 128 raw
requests per lifecycle, correct prompt hash cardinality, exact native oracle
validation, vLLM control-oracle absence, NPU 0 cleanup and
`ttft_cross_runtime_comparable=false`. The passing audit covers the completed
c4 paired cells and does not replace the broader control matrix.

`results/qwen14b-native-control-prefix-extension-v10-c16-o1-suite.json`
records the first native Qwen2.5-14B shared-prefix-extension c16/o1 formal
cell from clean commit `cc48750`. The first attempt,
`results/qwen14b-native-control-prefix-extension-v10-c16-o1-r1/`, is retained
as failed provenance: `state_capacity=33` and `max_decode_batch=32` made the
resident plan require 67,513,972,992 bytes while only 65,071,603,712 bytes were
free. The accepted lifecycles (`r1b`, `r2`, `r3`) use the same frozen 512 MiB
workspace and 14B artifacts, but reduce `state_capacity` to 17 and
`max_decode_batch` to 16 for the c16 cell. That execution-plan change produces
state compatibility digest
`79bcec636a1af50400b02aef04646da575c50465f5fc75116d59956dc6511d1f`, so older
states are invalid by construction. Across the three accepted lifecycles, all
128 requests are exact, `hit_rate=1`, effective reuse is 262,144 tokens per
lifecycle, stderr is empty, client exit code is 0, and NPU 0 has no residual
process after shutdown. Suite median: 2.450 request/s and output token/s, P95
wall latency 6560.21 ms, P99 wall latency 6561.92 ms, TPOT null and peak HBM
54,854 MiB.

`results/qwen14b-native-independent-cold-v6-c16-o1-suite.json` records the
matching native Qwen2.5-14B independent/cold c16/o1 formal cell from the same
clean commit and resident-plan identity. It uses the frozen 128-row
independent/cold prompt family and the existing o32 oracle family while
requesting one output token. Across three lifecycles, all 128 requests are
exact, `hit_rate=0`, `effective_reused_tokens=0`, temporary states are
recycled, stderr is empty, client exit code is 0, and NPU 0 has no residual
process after shutdown. Suite median: 3.263 request/s and output token/s, P95
wall latency 4946.24 ms, P99 wall latency 4948.65 ms, TPOT null and peak HBM
54,854 MiB.

`results/qwen14b-vllm-control-v8-c16-o1-suite.json` records the matching
formal vLLM control baseline cell at concurrency 16 and output length 1 from
clean commit `3f1d649`. This suite was restarted as a new v8 series with
explicit capacity provenance `max_model_len=4096`, `max_num_seqs=64` and
`gpu_memory_utilization=0.9`; the earlier accepted v7 `r1c` lifecycle is not
mixed into this suite. The three `shared_prefix` and three `independent_cold`
lifecycles are all `real-online`, `parent.dirty=false`, batch-invariant
`PIECEWISE`, 128 measured requests, 10 warmups, stderr empty, NPU 0 clean after
shutdown and `ttft_cross_runtime_comparable=false`. Suite median:
shared-prefix 91.635 request/s and output token/s, P95 wall 195.05 ms, TPOT
null and peak HBM 59,707 MiB; independent/cold 3.648 request/s and output
token/s, P95 wall 4608.73 ms, TPOT null and peak HBM 59,705 MiB. Together with
the native c16/o1 cells above this fills c16/o1 paired control evidence.
`benchmarks/audit_qwen14b_control_c16.py` audits this completed c16 evidence
boundary and now defaults to output lengths 1, 32 and 128. The three c32
controls, the full control matrix and any TTFT acceleration conclusion remain
incomplete.

`results/qwen14b-native-control-prefix-extension-v11-c16-o32-suite.json`
records native Qwen2.5-14B shared-prefix-extension c16/o32 formal evidence
from clean commit `7be22d2`. The three lifecycles use explicit 14B artifact
paths, `kv_bytes_per_token=196608`, 512 MiB workspace, `state_capacity=17`,
`max_decode_batch=16`, `max_prefill_rows=36864`, the frozen 2,177-token prompt,
a 2,048-token retained prefix and the frozen o32 greedy oracle. All 128
requests per lifecycle are exact, `hit_rate=1`,
`effective_reused_tokens=262144`, temporary branches are recycled, stderr is
empty, and NPU 0 has no residual process after shutdown. Suite median: 2.064
request/s, 66.034 output token/s, P95 wall latency 7813.17 ms, P99 wall latency
7814.66 ms, TPOT P50 39.43 ms and peak HBM 54,912 MiB.

`results/qwen14b-native-independent-cold-v7-c16-o32-suite.json` records the
matching native Qwen2.5-14B independent/cold c16/o32 formal evidence from the
same clean commit and resident-plan identity. It uses the frozen 128-row
independent/cold prompt family and the frozen o32 oracle family. Across three
lifecycles, all 128 requests are exact, `hit_rate=0`,
`effective_reused_tokens=0`, temporary states are recycled, stderr is empty,
and NPU 0 has no residual process after shutdown. Suite median: 2.598
request/s, 83.142 output token/s, P95 wall latency 6210.90 ms, P99 wall latency
6213.19 ms, TPOT P50 113.93 ms and peak HBM 54,856 MiB.

`results/qwen14b-vllm-control-v10-c16-o32-suite.json` records the matching
formal vLLM control baseline cell at concurrency 16 and output length 32 from
clean commit `93e336e`. The six accepted lifecycles are
`results/qwen14b-vllm-control-shared_prefix-v10-c16-o32-r{1,2,3}` and
`results/qwen14b-vllm-control-independent_cold-v10-c16-o32-r{1,2,3}`. They use
the same Qwen2.5-14B BF16 model, physical NPU 0, frozen prompt manifest, greedy
fixed-length output, batch-invariant `PIECEWISE`, 128 measured requests, 10
warmups, and explicit capacity `max_model_len=4096`, `max_num_seqs=64`,
`gpu_memory_utilization=0.9`. All six lifecycles are `real-online`,
`parent.dirty=false`, `all_validation_passed=true`, stderr empty, failed
requests total 0, and `ttft_cross_runtime_comparable=false`. Suite median:
shared-prefix 11.555 request/s, 369.771 output token/s, P50/P95/P99 wall
1374.63/1421.53/1424.43 ms, TPOT P50/P95/P99
39.41/41.35/41.61 ms and peak HBM 59,707 MiB; independent/cold 3.021 request/s,
96.668 output token/s, P50/P95/P99 wall 5230.64/6984.92/8557.93 ms, TPOT
P50/P95/P99 135.28/146.75/148.28 ms and peak HBM 59,826 MiB. Together with the
native c16/o32 suites above, this completes c16/o32 paired control evidence
only. The later v12 evidence below completes c16/o128 artifact coverage; no c32
control cell is complete.

The older v9 continuation artifacts remain provenance, not a suite.
`results/qwen14b-vllm-control-shared_prefix-v9-c16-o32-r1`, `r2b`, `r3`,
`results/qwen14b-vllm-control-independent_cold-v9-c16-o32-r1`, `r2c` and `r3`
are accepted individual real-online lifecycles, but they were launched from
multiple parent commits and `benchmarks/summarize_vllm_control_suite.py`
correctly refused to aggregate them. The original `shared_prefix` r2 remains a
preflight failure because NPU 0 was occupied by an external
`poy-118-21rc-npu0` vLLM service. The later `independent_cold` r2 completed
requests and wrote `result.json`, but the old cleanup gate marked it `FAILED`
after detecting an unrelated external Qwen2.5-3B `VLLMEngineCore` on NPU 0; it
is retained as failure provenance and must not be summarized.
`results/qwen14b-vllm-control-c16-o32-blocked-npu0-external-v1/` records a
later blocked preflight snapshot from clean commit `4aa7d08`: NPU 0 was still
occupied by an external `VLLMEngineCore` process using 57,417 MiB HBM. The
directory contains `BLOCKED.txt`, parent commit/status, host process, port and
NPU snapshots. It is not an accepted lifecycle and is not part of any suite.

`results/qwen14b-native-control-c16-o128-blocked-npu0-external-v1/` records a
blocked native c16/o128 formal-control preflight from clean commit `798ed12`.
The intended first lifecycle was
`qwen14b-native-control-prefix-extension-v12-c16-o128-r1`, but NPU 0 was
occupied by an external `VLLMEngineCore` process, PID 582823, using 28,365 MiB
HBM. Ports 18092, 18083 and 38073 were free, no native worker was launched, and
no c16/o128 lifecycle output directory was consumed. This directory is BLOCKED
provenance only and is not a partial or completed control cell.
`scripts/run_qwen14b_native_control_c16_o128.sh` is the fixed continuation
entrypoint for the native side of this cell once NPU 0 is exclusively
available; it fixes physical NPU 0, Qwen2.5-14B BF16 artifacts, 512 MiB
workspace, `state_capacity=17`, `max_decode_batch=16`, `max_prefill_rows=36864`,
the frozen 2,177-token prompt, o128 greedy oracle, 128 measured requests and
both native shared-prefix-extension plus independent/cold lifecycle names.

After NPU 0 became available, clean commit `18cf2f2` completed the native
c16/o128 control-side formal evidence. The shared-prefix-extension suite is
`results/qwen14b-native-control-prefix-extension-v12-c16-o128-suite.json` with
lifecycles `r1`, `r2` and `r3`; all three are `real-online`,
`parent.dirty=false`, 128 measured requests, exact against the frozen o128
oracle, `hit_rate=1`, `effective_reused_tokens=262144`, temporary branches
recycled, empty stderr, client exit 0 and NPU 0 clean after shutdown. Suite
median: 1.379 request/s, 176.515 output token/s, P50/P95/P99 wall
11597.62/11726.91/11727.86 ms, TPOT P50/P95/P99 39.67/40.64/40.65 ms and peak
HBM 54,856 MiB. The independent/cold suite is
`results/qwen14b-native-independent-cold-v8-c16-o128-suite.json` with
lifecycles `r01`, `r02` and `r03`; all three are `real-online`,
`parent.dirty=false`, 128 measured requests, exact against the frozen o128
oracle family, `hit_rate=0`, `effective_reused_tokens=0`, temporary states
recycled, empty stderr, client exit 0 and NPU 0 clean after shutdown. Suite
median: 1.596 request/s, 204.297 output token/s, P50/P95/P99 wall
10032.61/10114.84/10119.06 ms, TPOT P50/P95/P99 58.38/75.66/76.62 ms and peak
HBM 54,856 MiB.

Clean commit `71f236b` completed the matching fresh v12 vLLM baseline:
`results/qwen14b-vllm-control-shared_prefix-v12-c16-o128-r{1,2,3}`,
`results/qwen14b-vllm-control-independent_cold-v12-c16-o128-r{1,2,3}` and
`results/qwen14b-vllm-control-v12-c16-o128-suite.json`. All six lifecycles are
`real-online`, `parent.dirty=false`, 128 measured requests, 10 warmups,
capacity `4096/64/0.9`, zero failed requests, validation passed, and scoped
cleanup complete. Shared-prefix median is 3.073 request/s, 393.302 output
token/s, P50/P95/P99 wall 5188.65/5257.54/5260.24 ms, TPOT P50/P95/P99
39.81/40.05/40.07 ms, and peak HBM 59,707 MiB. Independent/cold median is
1.709 request/s, 218.799 output token/s, P50/P95/P99 wall
9283.61/11025.66/12613.45 ms, TPOT P50/P95/P99 64.88/67.71/68.26 ms, and peak
HBM 59,707 MiB. The c16/o128 paired evidence audit passes and TTFT remains
cross-runtime incomparable.

This milestone does not pass a native performance-dominance gate. On the
shared-prefix control, native reaches 44.9% of vLLM request/output throughput
(1.379 versus 3.073 request/s), although TPOT P50 is similar (39.67 versus
39.81 ms) and native uses 4,851 MiB less peak HBM. The main measured gap is
therefore before or around steady decode, in prefix-extension prefill and
scheduling, rather than per-output-token decode time. The v12 independent/cold
numbers remain historical diagnostics because those prompts were 2,204 tokens
and did not share the native per-row token-ID root.

Clean commit `a6eaa3d` resolves that independent/cold input mismatch without
rerunning the unrelated shared-prefix control. The frozen v2 family at
`results/qwen14b-independent-cold-prompt-family-v2/manifest.json` adds ten
negative-ordinal warmup rows while preserving all 128 measured rows from v1
byte-for-byte. Its measured token-ID root is
`a8bf4c823f36e5ac7ae310b1225761c726018d5bd83270db5b9335da1be69574`,
the same root implied by the native v1 family; its independent warmup root is
`1a1f8d888e3fb81de53b8011167993f0a37de2b932f8b613a0881944f20bc286`.
The three `qwen14b-vllm-independent-cold-token-parity-v13-c16-o128-r{1,2,3}`
lifecycles pass the cold-only suite auditor with 128 measured plus ten warmup
requests, direct frozen token-ID input, exact returned prompt-ID validation,
zero failed requests, empty client stderr, clean parents and clean NPU 0
shutdown. The suite median is 1.712 request/s, 219.118 output token/s, P50/P95/
P99 wall 9273.57/11022.40/12600.04 ms, TPOT P50/P95/P99 64.84/67.62/68.09 ms,
and peak HBM 59,707 MiB.

The shutdown auditor records teardown diagnostics separately from request
errors. All three pinned-vLLM lifecycles emit the existing Python resource
tracker warning for one leaked semaphore. In `r3` only, after all 138 HTTP 200
responses, the explicit shutdown trigger and EngineCore's "request processing
complete" marker, the stopped manager caused an `AsyncLLM output_handler`
`EngineDeadError`. It is classified as a shutdown transport race rather than an
inference failure; no such error occurred before shutdown, and the port and NPU
0 were clean afterward. This warning is retained in the raw server log and suite
summary rather than silently discarded.

The strict measured-input comparison still fails the throughput dominance
gate: native reaches 93.24% of vLLM throughput (1.596 versus 1.712 request/s),
or 6.76% less. Native nevertheless has 8.23% lower P95 wall latency
(10114.84 versus 11022.40 ms), 9.96% lower TPOT P50 (58.38 versus 64.84 ms),
and uses 4,851 MiB less peak HBM. This combination points to native request
dispatch/batch-boundary idle time rather than a steady-decode kernel deficit as
the next independent/cold optimization target. vLLM remains an oracle-free
baseline and TTFT remains cross-runtime incomparable.

The v11 continuation remains partial provenance only: shared-prefix v11 `r1`,
`r2` and `r3` are accepted,
and independent/cold `r1`, `r2b` and `r3` are accepted, but they were launched
from multiple clean parent commits. `benchmarks/summarize_vllm_control_suite.py`
therefore rejected `results/qwen14b-vllm-control-v11-c16-o128-suite.json` with
`lifecycles were not launched from one parent commit`; the retained marker is
`results/qwen14b-vllm-control-v11-c16-o128-suite.FAILED.txt`. The shared-prefix
`r3` lifecycle reports 3.049 request/s, 390.242 output token/s, P95 wall
latency 5404.31 ms, TPOT P50 39.73 ms, zero failed requests and validation
passed. The independent/cold v11 `r1` lifecycle reports 1.713 request/s,
219.250 output token/s, P95 wall latency 11038.27 ms, TPOT P50 64.81 ms, zero
failed requests and validation passed. The independent/cold v11 `r2` directory is
failed provenance: an external GitHub runner Qwen2.5-3B `VLLMEngineCore`, PID
1106197, was present on NPU 0 with about 6,045 MiB HBM after `r1`; the next
engine startup saw 54.73 GiB free versus 54.86 GiB required by the fixed
`gpu_memory_utilization=0.9` capacity and exited with code 1. The runbook now
uses a fresh v12 lifecycle set for the formal same-parent suite, leaving all
v11 directories as partial/failure evidence.

`results/qwen14b-vllm-control-c16-o128-blocked-npu0-external-v1/` records the
earlier blocked continuation attempt from clean commit `900e27d`. Before
launching any new lifecycle, the preflight found NPU 0 occupied by an external
`VLLMEngineCore` process, PID 899695, using about 6,045 MiB HBM. Ports 18092,
18083 and 38073 were free. The runbook was not launched, no lifecycle name was
consumed, and the directory is BLOCKED provenance only.

`benchmarks/audit_qwen14b_control_progress.py` reports the current paired
control matrix boundary without upgrading diagnostic evidence into conclusions.
It now reports 12 total control cells, 9 completed evidence cells (all c1, c4,
and c16 outputs), no partial cells, and three missing c32 cells. The c16 audit
defaults to output lengths 1, 32 and 128. Completion here means artifact and
contract coverage; it does not mean native performance dominance, and the cold
input-token mismatch above remains an explicit comparison debt. The progress
audit also reports the retained
known-invalid c16/o32 vLLM directories `shared_prefix` r2 and
`independent_cold` r2, plus the c16/o128 v11 `independent_cold` r2 failure, so
their presence cannot be confused with accepted coverage. The same progress
report now lists historical native
independent/cold runs whose `run_metadata.json` still contains the legacy
four-token 7B `model.prompt_token_ids` fallback. Those runs remain bound to
their prompt-family and oracle-family SHA-256 values for actual input identity,
but the legacy model field is provenance debt and future native independent/cold
results must not reproduce it. The script is a progress audit only; completed
cells remain bounded by their per-concurrency audits and no TTFT speedup or full
control-matrix conclusion is claimed.

`results/qwen14b-vllm-control-c16-o128-v12-blocked-npu0-external-v1/` records
the first fresh v12 preflight from clean commit `1a7e12e`. NPU 0 was occupied
by an external `VLLMEngineCore` process, PID 1232869, using 57,417 MiB HBM.
The v12 runbook was not launched, no v12 lifecycle directory was consumed, and
the directory is BLOCKED provenance only.

`results/` still retains failed or partial vLLM c16/o1 provenance from the old
v7 attempts: `qwen14b-vllm-control-shared_prefix-v7-c16-o1-r1` completed client
requests but failed the cleanup gate, `r1b` stopped before server launch
because NPU 0 was occupied, `r1c` is one accepted shared-prefix lifecycle, `r2`
failed during torch_npu preflight with a device startup timeout while NPU 0
became occupied by an external vLLM process, `r2b` and `r2c` were preflight
rejections with NPU 0 already occupied, and `r2d` reached server startup but
failed KV-cache admission at `gpu_memory_utilization=0.8`. These directories
remain provenance only and are not part of the v8 suite.

`results/qwen14b-native-control-prefix-extension-v5-c1-o1-suite.json` records
the matching native Qwen2.5-14B shared-prefix-extension c1/o1 formal cell from
clean commit `204054e`. The three lifecycles use explicit 14B artifact paths,
`kv_bytes_per_token=196608`, a 512 MiB workspace, `max_prefill_rows=2304`, the
frozen 2,177-token prompt, a 2,048-token retained prefix and 129 extension
tokens. All 128 requests per lifecycle are exact, `hit_rate=1`,
`effective_reused_tokens=262144`, temporary branches are recycled, client
stderr is empty, client exit code is 0, and NPU 0 has no residual process after
shutdown. Suite median: 0.246 request/s and output token/s, P95 wall latency
4095.82 ms, P99 wall latency 4132.71 ms, TPOT null and peak HBM 58,343 MiB.
Together with the vLLM c1/o1 baseline above and the existing native
independent/cold c1/o1 declared cell, this fills more of the control matrix,
but it is still not the full control matrix or a broad serving-performance
conclusion.

`results/qwen14b-native-control-prefix-extension-v6-c1-o32-suite.json` records
the native Qwen2.5-14B shared-prefix-extension c1/o32 formal cell from clean
commit `4301101`. The suite uses the three clean lifecycles
`results/qwen14b-native-control-prefix-extension-v6-c1-o32-r1`,
`results/qwen14b-native-control-prefix-extension-v6-c1-o32-r2`, and
`results/qwen14b-native-control-prefix-extension-v6-c1-o32-r3b`; the earlier
`results/qwen14b-native-control-prefix-extension-v6-c1-o32-r3` directory is
retained as a failed non-sample with a `Connection refused` client stderr and
no NPU 0 residual process. The accepted lifecycles are all `real-online`,
`parent.dirty=false`, use explicit 14B artifact paths,
`kv_bytes_per_token=196608`, a 512 MiB workspace, `max_prefill_rows=2304`, and
the frozen 2,177-token prompt with a 2,048-token retained prefix plus 129
extension tokens. All 128 requests per lifecycle are exact, `hit_rate=1`,
`effective_reused_tokens=262144`, temporary branches are recycled, client
stderr is empty, client exit code is 0, and NPU 0 has no residual native worker
after shutdown. Suite median: 0.200 request/s, 6.400 output token/s, P95 wall
latency 5051.00 ms, P99 wall latency 5083.50 ms, TPOT P50 30.60 ms, TPOT P95
30.94 ms, TPOT P99 31.10 ms and peak HBM 58,343 MiB. Together with the
existing native independent/cold c1/o32 declared cell, this completes the
native-side c1/o32 controls. The matching vLLM c1/o32 control baseline is now
recorded above, so c1/o32 has paired control evidence; the full control matrix
and broad serving-performance conclusion remain incomplete.

`results/qwen14b-native-control-prefix-extension-v7-c1-o128-suite.json` records
the native Qwen2.5-14B shared-prefix-extension c1/o128 formal cell from clean
commit `14f5fc4`. The three lifecycles use explicit 14B artifact paths,
`kv_bytes_per_token=196608`, a 512 MiB workspace, `max_prefill_rows=2304`, and
the frozen 2,177-token prompt with a 2,048-token retained prefix plus 129
extension tokens. All 128 requests per lifecycle are exact, `hit_rate=1`,
`effective_reused_tokens=262144`, temporary branches are recycled, client
stderr is empty, client exit code is 0, and NPU 0 has no residual native worker
after shutdown. Suite median: 0.125 request/s, 16.048 output token/s, P95 wall
latency 8089.68 ms, P99 wall latency 8337.81 ms, TPOT P50 30.69 ms, TPOT P95
31.22 ms, TPOT P99 33.34 ms and peak HBM 58,472 MiB. Together with the
existing native independent/cold c1/o128 declared cell, this completes the
native-side c1/o128 controls, but the matching vLLM c1/o128 control baseline is
still missing.

## Qwen2.5-14B native independent/cold c1/o1, c1/o32 and c1/o128 (partial)

`results/qwen14b-independent-cold-prompt-family-v1/manifest.json` freezes 128
Qwen2.5-14B independent/cold measured prompts. Each prompt embeds request
identity before the first 128-token physical cache block, contains 2,206 prompt
tokens, and has a unique complete token-ID SHA-256 and first-cache-block
token-ID SHA-256. The source prompt remains the frozen 2,177-token exact prompt
with token-ID SHA-256
`a1a3b1e05988a4c0732495d4e665956b28fe9ea73f57b8a2699cf1c13c605e8b`.

`results/qwen14b-independent-cold-oracle-family-o32-v1/manifest.json` and
`results/qwen14b-independent-cold-oracle-family-o128-v1/manifest.json` freeze
separate Torch-NPU eager BF16 greedy oracles for those 128 prompts at output
lengths 32 and 128. The oracles are reference-only and record
`formal_serving_runtime_uses_torch=false` and `performance_claim=false`; the
native candidate path below does not use Torch, vLLM or SGLang as an execution
backend.

`results/qwen14b-native-independent-cold-v1-c01-o001-suite.json` and
`results/qwen14b-native-independent-cold-v1-c01-o032-suite.json` and
`results/qwen14b-native-independent-cold-v1-c01-o128-suite.json` record three
clean native C++/ACL service lifecycles each for the independent/cold cells at
concurrency 1 and output lengths 1, 32 and 128. Each lifecycle has 128
measured requests, all outputs exact against the per-prompt oracle,
`hit_rate=0`, `effective_reused_tokens=0`, temporary states recycled, empty
client stderr, client exit code 0, and no NPU 0 native worker residual in the
captured post-run snapshots. The run metadata binds the same prompt-family
SHA-256 `dbfbf8564bc2b9312cdcd7c582fce063732f96f9b3547aaed14e2678a7702b97`
and the matching oracle-family SHA-256 for the requested output length.

For output length 1, the median throughput is 3.122 request/s and 3.122 output
token/s. Median P50/P95/P99 end-to-end wall latency is
319.18/328.73/331.57 ms, and peak HBM is 58,343 MiB. TPOT is null by
definition because there is no post-first output token.

For output length 32, the median throughput is 0.781 request/s and 24.977
output token/s. Median P50/P95/P99 end-to-end wall latency is
1281.09/1292.76/1297.11 ms, median TPOT P50/P95/P99 is
30.77/30.98/31.11 ms, and peak HBM is 58,343 MiB.

For output length 128, the median throughput is 0.238 request/s and 30.401
output token/s. Median P50/P95/P99 end-to-end wall latency is
4210.40/4223.63/4233.35 ms, median TPOT P50/P95/P99 is
30.61/30.71/30.76 ms, and peak HBM is 58,343 MiB. The resident state
compatibility digest is
`146733780ed6a30a4cf72ccfeff889acc34ccd036b8a63ef7c93c00610f1b0bc`,
with the same recorded weight, RoPE, state-schema, physical-cache-layout and
compiled-plan digests across all three lifecycles.

This is `real-online` evidence only for the declared native independent/cold
c=1,o={1,32,128} cells. It is not an exact-hot matrix result, not a vLLM
comparison, and not a full performance conclusion. Native internal TTFT and
vLLM SSE TTFT remain non-comparable.

## Exact retained-state latency

The first verified result is deliberately narrow: Qwen2.5-7B-Instruct BF16 on
one Ascend 910B2, a 2177-token exact repeated prompt, greedy decoding, and one
output token. Each runtime receives the same prompt and produces output token
ID `16`.

| Runtime | Warm median | Warm IQR | Warm p95 |
|---|---:|---:|---:|
| State-centric engine | 2.824 ms | 0.530 ms | 3.469 ms |
| vLLM-HUST + vLLM-Ascend-HUST | 33.553 ms | 0.796 ms | 34.276 ms |

The derived speedup is **11.88x at the median** and **9.88x at p95**. This is a
`derived-artifact` from two `real-online` runs with 20 warm repetitions each.
The parity checker also verifies full-prompt reuse and a single retained state
handle on the candidate path.

The result supports only the claim that explicit retained state can remove
repeat tokenization, block-granularity suffix work, repeat next-token selection,
and generic request-path overhead for this workload. It does **not** establish
superiority for cold inference, sustained decoding, concurrency, or mixed
hot/cold workloads.

Evidence:

- `results/20260713-exact-state-v1/statecentric/result.json`
- `results/20260713-exact-state-v1/statecentric/run_metadata.json`
- `results/20260713-exact-state-v1/vllm-hust-ascend/result.json`
- `results/20260713-exact-state-v1/vllm-hust-ascend/run_metadata.json`
- `results/20260713-exact-state-v1/comparison.json`

Re-run the parity and speedup gates with:

```bash
python3 benchmarks/compare_results.py \
  --candidate results/20260713-exact-state-v1/statecentric/result.json \
  --baseline results/20260713-exact-state-v1/vllm-hust-ascend/result.json \
  --output results/20260713-exact-state-v1/comparison.json
```

## Request-microbatch diagnostic (non-claim)

`results/20260714-request-microbatch-smoke/` records an
`existing-server-probe` from the first dirty-worktree integration of the Rust
dispatcher and Python batch executor. Eight exact-hot requests at concurrency
4 requested 32 output tokens each; all completed with identical token IDs and
the runtime trace showed measured batches of four.

The probe observed 2.70 request/s, 86.55 output token/s, and P95 request latency
of 1.485 s. It has no paired vLLM run, no clean-commit repetition, and no
TTFT/TPOT event instrumentation. These numbers are retained as negative
debugging evidence and support no performance-superiority claim.

A later ephemeral dirty-worktree probe validated the step protocol on the same
device: 8/8 exact-hot requests at concurrency 4 produced identical 32-token
sequences. An initial implementation that split and restacked KV every token
observed about 59 output token/s; keeping stable batches in batched-cache form
restored about 83 output token/s. A staggered smoke also completed a late
resident one-token request during an already-running cold 32-token decode.
These are mechanism/optimization diagnostics without a paired baseline,
clean-commit repetitions, or claim status.

## Project-owned paged-cache diagnostic (negative, non-claim)

`results/20260714-native-paged-attention-v1/` separates the underlying Ascend
operator from its first Transformers integration. Direct block-table fused
attention was bit-identical to contiguous attention and measured 0.183 ms
median versus 0.186 ms at batch 4 and sequence length 603. This is a component
measurement only.

The corrected full-model path also preserved every greedy token, but did not
preserve performance. At batch 4, a 562-token prompt and 32 output tokens, the
project-owned paged path took 2054 ms median decode time versus 1486 ms for the
contiguous DynamicCache reference (0.724x). A public NPU scatter-update operator
was about 4x faster than advanced assignment when indices were precomputed, but
constructing those indices inside every Transformers layer worsened the full
path to 2137 ms versus 1459 ms (0.683x).

The first smoke file is intentionally retained as invalid evidence: it exposed
an incorrect BNSD physical-block write layout and failed token parity. The bug
was fixed and covered by `benchmarks/test_paged_cache.py` before later probes.
No paged-cache result in this directory is a serving result or evidence of
superiority over vLLM. It motivates the fixed-model native executor decision in
`docs/NATIVE_EXECUTOR_DECISION.md`.

## Native AscendCL runtime gate (non-claim)

`results/20260714-native-ascendcl-smoke-v1/` records the first project-owned
C++ runtime probe. On one 910B2 it initialized AscendCL context/stream state,
allocated HBM, and round-tripped 16 KiB with exact bytes and matching checksum.
The captured dynamic dependencies include `libascendcl.so` and CANN/driver
libraries but no Torch, Python or vLLM runtime. This proves native-runtime Gate
1 only; it is not a model, serving or performance result.

## Native ACLNN RMSNorm parity gate (non-claim)

`results/20260714-native-rmsnorm-v1/` records a project-owned C++ call to
`aclnnRmsNorm` at batch 4 and Qwen hidden size 3584. All 14,336 BF16 output
elements were bit-identical to the deterministic Torch CPU formula oracle;
maximum output error was zero and maximum reverse-RMS error was 1.19209e-7.
The executable links AscendCL, opapi and nnopbase, with no Torch, Python or vLLM
runtime dependency. This proves native operator-interface Gate 2 only and does
not support model, serving or performance claims.

## Native Qwen weight identity gate (derived, non-claim)

`results/20260714-native-qwen-manifest-v1/` fixes native executor v1 to one
content-addressed Qwen2.5-7B-Instruct BF16 artifact. A standard-library exporter
parsed all safetensors headers without Torch, validated 339 BF16 tensors and
15,231,233,024 tensor bytes, and fully hashed the config, index and four weight
shards. The resulting model identity is
`4be7e32003f50430a1412610275186ea6af130ff58d874b9d7bbd2947a9faec8`.
This is model-identity evidence only; execution parity is established
separately below.

`results/20260714-native-qwen-layer0-pack-v1/` advances the same gate from
identity to conversion. It directly copies the 12 layer-0 BF16 tensor ranges
into a 4 KiB-aligned 466,124,800-byte pack without importing Torch. The pack and
every tensor are SHA-256 addressed. The large binary remains reproducibly local
under `.benchmarks/`.

`results/20260714-native-q-projection-v1/` is the first real-weight execution
segment from that pack. A project-owned C++ executable directly runs ACLNN
RMSNorm, matmul and bias addition on one 910B2. RMSNorm is bit-exact for all
14,336 BF16 elements. The Q projection is bit-exact for 11,046/14,336 elements;
all elements pass the pre-run `atol=0.015625`, `rtol=0.015625` gate, with
maximum absolute error 0.125 and mean absolute error 0.000451941. The candidate
links no Torch, Python or vLLM runtime. The input activation is deterministic
and synthetic, so this proves only a partial-layer numerical gate; full decoder
layer, model, serving and performance claims remain unproven.

## Native complete decoder-layer parity gate (non-claim)

`results/20260714-native-decoder-layer-v1/` extends the real-weight path through
one complete Qwen2.5 decoder layer: both RMSNorms, biased Q/K/V projections,
NeoX RoPE, explicitly masked causal GQA attention, O projection, both residual
adds and the SiLU-gated MLP. The project-owned C++ executable directly invokes
ACLNN on one 910B2 and links no Torch, Python or vLLM runtime. For the
deterministic 4-token synthetic activation, every recorded intermediate and the
final output have zero elements outside the pre-run `atol=0.015625`,
`rtol=0.015625` gate. The final output has 12,580/14,336 bit-exact BF16 elements,
maximum absolute error 0.015625 and mean absolute error 0.000218319.

This is a real-hardware component probe with real layer-0 weights. It does not
establish 28-layer numerical accumulation, embedding/final-norm/LM-head
correctness, greedy-token parity, KV-cache correctness, serving behavior or a
performance advantage.

## Native real-weight layer paged-attention gate (non-performance)

`results/20260715-native-model-paged-layer0-v1/` replaces synthetic K/V at the
layer boundary. Native RMSNorm, real Qwen layer-0 weights, biased Q/K/V
projections, and RoPE generate the page contents on one 910B2. Scatter preserves
the projected K/V bit-for-bit, and paged incremental attention reproduces all
3,584 BF16 elements of the prompt-attention last-token output exactly.

This is one four-token decoder layer, not a 28-layer decode or serving run. It
supports no latency, throughput, or generated-token claim.

## Native full-model layout and oracle gates (non-claim)

`results/20260714-native-qwen-all-weights-v1/` records validated 4 KiB-aligned
native layouts for all 28 decoder layers plus embedding, final norm, and LM
head. The 339 tensors contain exactly 15,231,233,024 bytes, matching the frozen
model manifest. Every pack was reread and SHA-256 checked. Embedding and LM-head
hashes differ and cannot be treated as tied weights. This is a derived layout
gate; no model execution occurs.

`results/20260714-native-qwen-full-model-oracle-v1/` freezes a real Torch/NPU
reference run on one 910B2 for token IDs `[1397, 64424, 44378, 5942]`. It
records the embedding, all 28 layer outputs, final norm, and logits; the greedy
next-token ID is `525`. Torch is used only to create this offline reference.
The artifact is not candidate-serving or performance evidence; the composed
native token gate is reported separately below.

## Native composed full-token gate and hidden-state negative

`results/20260714-native-full-token-chain-v1/` connects native embedding,
28 decoder-layer executions, final RMSNorm, and LM head on one 910B2. Each
decoder layer consumes the preceding native output. Embedding is bit-exact, and
the final native greedy token is `525`, equal to the frozen oracle. Neither
candidate executable links Torch, Python, or vLLM.

This result also rejects a stronger claim. The PFA-based native hidden state
already exceeds the frozen eager-oracle tolerance in 6,429/14,336 elements at
layer 0, growing to 11,391/14,336 at layer 27. The final logits select the same
token but are not numerically equal. The path is multi-process and intentionally
synchronized for diagnosis, so its elapsed time is not serving performance.
It proves a composed greedy-token gate only; attention-boundary diagnosis and
the single-process HBM-resident executor remain open.

`results/20260714-native-layer0-boundary-v1/` localizes that diagnosis. Native
RMSNorm and Q/K/V have zero tolerance failures, RoPE has one Q-element failure,
and the first large divergence is PFA attention output at 2,139/14,336 elements.
Changing `inner_precise` does not change the output, while sparse mode 3 is
rejected by this API contract with status 561103. These are numerical and API
boundary findings, not serving-performance results.

## Native single-process resident full-model gate (non-performance)

`results/20260714-native-resident-full-model-v1/` consolidates embedding, all
28 layers, final norm, LM head, and argmax into one project-owned C++ process,
context, and stream. All aligned weight packs—15,231,491,072 bytes—are resident
in HBM before execution. AscendCL reports 15,658,102,784 HBM bytes in use after
loading weights and 17,866,403,840 after allocating correctness workspaces. The
final greedy token remains `525`.

The probe synchronizes and copies every layer output for diagnosis, so no
elapsed time is a serving metric. It proves only one fixed full-model token plus
weight residency; KV cache, batched prefill/decode, concurrency, and performance
remain unproven.

## Native paged-KV HBM lifecycle gate (non-performance)

`results/20260715-native-paged-kv-hbm-v1/` connects the project-owned native
allocator to a real BF16 key/value arena on one 910B2. ACLNN scatter writes a
129-token parent; a same-namespace fork shares its full block, performs
device-to-device COW for the one-token partial block, and appends one child
token. Device-to-host verification proves the full parent sequence, child COW
prefix, child append, and parent isolation bit-for-bit. Parent and child
eviction return all eight logical blocks to the arena.

The arena remains allocated and reusable, so this does not prove lower
process-level HBM residency. It is a functional component gate only: no
model-generated K/V, paged attention, batched decode, serving request, latency,
or throughput claim is supported.

## Native allocator-to-paged-attention gate (non-performance)

`results/20260715-native-paged-attention-v1/` composes the project allocator,
ACLNN scatter, and ACLNN incremental paged attention on one 910B2. Four
heterogeneous contexts of 129, 257, 385, and 603 tokens consume 14 physical
pages. The block-S-H cache write is bit-exact to its expected layout, and all
14,336 BF16 attention outputs are bit-exact to contiguous attention over the
same inputs.

The inputs are deterministic synthetic Q/K/V. This proves the native
allocator-to-operator contract only; it does not prove model-generated cache,
multi-layer decode, token parity, continuous batching, serving behavior, or a
performance advantage.

## Native 28-layer paged-decode token gate (non-performance)

`results/20260715-native-qwen-paged-decode-v1/` keeps the full Qwen2.5-7B BF16
weight set and one 128-token K/V page per layer resident on one 910B2. The
four-token prompt populates all 28 caches with `aclnnScatterPaKvCache`; the
project-owned C++ executor then performs one incremental step through
`aclnnIncreFlashAttentionV4`. Prompt token `525` and decoded token `264` both
match their frozen Torch/NPU offline oracles. Neither Torch nor vLLM executes
in the candidate process.

The strict per-layer and logits BF16 tolerance does not pass, consistent with
the already documented prompt-attention divergence. The result therefore
proves generated-token correctness for this fixed one-step sequence, not tensor
parity. It is not continuous batching, serving, latency, throughput, or a vLLM
comparison.

`results/20260715-native-workspace-lifecycle-v1/` repeats this gate after making
ACLNN workspaces transient at layer boundaries. Generated tokens are unchanged,
while live ACL allocations after execution are 15.24 GB rather than retaining
the 20.10 GB cumulative allocation traffic. The observed allocation peak is
15.33 GB. This removes one long-running-process memory-growth mechanism, but a
repeated-request soak is still required before claiming stable service memory.

`results/20260715-native-workspace-arena-v1/` removes the remaining per-layer
device allocator calls by reserving a 256 MiB bump arena once. The prompt and
decode tokens remain correct, and peak workspace use is 87,839,744 bytes.
Resetting the arena after each synchronized layer changes only its offset; it
does not allocate or release HBM. This is the memory substrate for the planned
resident loop, not evidence that the loop or batching already exists.

`results/20260715-native-generation-oracle-128-v1/` freezes the 128 greedy
output token IDs for the same fixed prompt using Torch/NPU eager attention.
This is an offline correctness reference only; it records no timing and does
not execute in the candidate path. It diagnoses numerical-path differences;
formal output parity is evaluated against the pinned baseline below.

`results/20260715-vllm-generation-oracle-128-v1/` records the corresponding
parent-pinned vLLM graph-mode sequence, which is the formal same-spec output
oracle. The current native paged path matches its first 90 tokens. At index 90,
vLLM reports an exact log-probability tie between its selected token `1447` and
the native-selected token `9844`; the autoregressive suffix then diverges.
Therefore the native 128-token correctness gate remains failed. The much
earlier eager-oracle divergence is diagnostic and must not force the candidate
to reproduce a non-baseline attention path.

`results/20260715-native-fia-taskgraph-diagnostic-v1/` tests a narrower
hypothesis on one 910B2: whether the earlier FIA mismatch was caused merely by
executing the attention operator outside an ACL graph. The native C++ process
uses the public model-RI APIs to capture one FIA task group per layer, update
its sequence-length metadata, and replay it without Torch or vLLM. The path
executes successfully, but the first mismatch remains index 34: vLLM selects
token `13`, while native FIA selects `315`. This is the same boundary as direct
FIA and ATB, so attention task-group capture alone is rejected as the cause.
The failed diagnostic contains no performance claim; full-model graph
execution remains distinct and untested.

## Native batch-four full-model decode gate (non-performance)

`results/20260715-native-qwen-batched-decode-v1/` executes one real tensor
batch of four Qwen2.5-7B BF16 rows through all 28 native decoder layers on one
Ascend 910B2. Each row uses a distinct block-table row, slot mapping, and two
physical cache blocks. All four rows decode input token `525` to token `264`,
matching the frozen parent-pinned vLLM oracle. The candidate process calls
ACLNN/AscendCL directly and executes neither Torch nor vLLM.

This clean-commit component gate proves fixed-shape batch-four full-model decode
and token parity only. It has no timing claim and does not prove a long-running
worker, Rust/native protocol integration, continuous batching, heterogeneous
sequence support, request/output-token throughput, tail latency, 128-token
parity, or superiority over vLLM. Intermediate tensors still fail the strict
BF16 tolerance gate, and the separately recorded 128-token run remains failed
at the exact-logit tie at output index 90.

## Native protocol-to-resident-NPU gate (non-performance)

`results/20260715-native-protocol-npu-v1/` connects the Rust asynchronous
protocol client to one long-running C++/CANN model process on a 910B2. Four
pre-seeded physical states execute two successive full-model tensor batches.
All rows produce token `536` after input `264`, then token `315` after input
`536`, matching the frozen parent-pinned vLLM oracle. A replay of the stale
context is rejected for all four states without emitting tokens. Protocol
shutdown waits for process exit and leaves no model process or NPU allocation.

This is a decode-only process-boundary component result. State creation occurs
before the handshake, and the worker supports only four fixed states, exact
hits and one decode step per dispatch. It does not establish cold prefill,
dynamic membership, cancellation, eviction, continuous batching, HTTP serving,
throughput, tail latency, 128-token parity or superiority over vLLM. The two
single-run executor durations are retained only as diagnostic telemetry and
carry no performance claim.

`results/20260715-native-protocol-prefill-v1/` advances that boundary from
pre-seeded decode state to protocol-driven state creation. Four cold four-token
items execute as one real prefill tensor batch, allocate four distinct physical
KV rows and return generation-tagged state IDs plus token `525`. Three
successive decode batches return `264`, `536` and `315` on every row. A fifth
cohort is rejected atomically at capacity, existing states remain valid, and a
stale-context replay emits no token.

This remains fixed-shape component evidence. Capacity is four, prompt length is
four, membership is fixed after creation, and every decode dispatch performs
one step. There is no cancellation, eviction/reuse, continuous batching, HTTP
serving or performance claim. The recorded single-run durations are diagnostic
only.

`results/20260715-native-dynamic-cohorts-v1/` then changes membership between
decode steps. After one batch-four prefill, Rust selects cohorts of sizes
`1,3,2,2,4` and reorders the final state rows as `[4,2,3,1]`. Each sequence
still emits `264`, `536` and `315` in order. This proves that per-dispatch
block-table reconstruction and slot mapping follow Rust-selected state IDs; it
does not yet prove arrival-time continuous admission or any performance claim.

`results/20260715-native-eviction-reuse-v1/` closes the next lifecycle
component boundary. State 2 generation 1 is evicted, its stale handle is
rejected, and a one-row cold prefill reuses the same physical ID at generation
2. The replacement context at length 4 then decodes in one cohort beside state
1 at length 7, producing oracle tokens `264` and `44378`. This proves logical
generation safety and heterogeneous decode metadata; the resident HBM arena is
not released, and no serving or performance claim follows.

`results/20260715-native-full-buckets-v1/` scales this component boundary to
32 resident states. One real tensor prefill creates all 32, and 63 subsequent
decode dispatches cover every required cohort bucket `1/2/4/8/16/32`. All
states preserve the seven-token oracle sequence. The same run rejects a 33rd
state atomically and repeats generation-safe eviction, stale-handle rejection,
physical-slot reuse and heterogeneous-context decode.

This clean-commit run calls ACLNN/AscendCL directly and executes neither Torch
nor vLLM. It proves capacity and batch-bucket correctness only: arrivals are
scripted, prompts are fixed at four tokens and each dispatch performs one
decode step. It is not real-online evidence and carries no throughput, tail,
HBM-pressure, 128-token parity or vLLM-superiority claim.

`results/20260715-native-arrival-runtime-v1/` connects the reusable Rust native
runtime actor to that 32-state executor. After setup, 16 resident continuations
enter the first decode batch. The probe waits until that native request is
observably in flight before submitting the other 16 continuations. The actor
accepts those arrivals during NPU execution and the following cohort grows to
32; the complete decode-size trace is `16,32,32,32,32,32,16`. All 64
submissions complete and every continuation matches the six-token oracle.

This proves arrival admission and state-aware rebatching at native one-token
quantum boundaries. It does not prove an HTTP service, `real-online` workload,
operator interruption, throughput, TTFT/TPOT, tails, HBM pressure, policy
superiority, 128-token parity or superiority over vLLM.

`results/20260715-native-http-arrival-v1/` crosses the same mechanism through
the live `native_state_engine` HTTP token service. Thirty-two cold requests
create states; sixteen continuations begin decode; after `/metrics` reports the
native request in flight, sixteen more HTTP requests arrive. All 64 requests
complete with oracle parity and the scheduler again emits
`16,32,32,32,32,32,16`. The record preserves 64 raw request rows and all eight
batch plans in separately hashed artifacts and confirms graceful process exit.

This is a `real-online-smoke`, not a performance comparison. It does not report
request/s, output token/s, TTFT/TPOT or tails; it does not cover general prompt
lengths, state pressure, cancellation, policy ablation, 128-token parity or
vLLM. Raw non-streaming HTTP latencies are retained only for traceability.

`results/20260715-native-http-cancel-v1/` adds explicit cancellation to the
live native service. Request 9001 resumes a resident generation-1 state and is
cancelled only after `/metrics` shows native execution in flight. The current
one-token ACLNN quantum is allowed to retire; the actor then evicts the
undeliverable advanced state and returns `409 Conflict`. Request 9002 replays
the old handle and receives `StaleState`, also with no output token. The record
preserves 66 raw HTTP rows and eleven batch plans.

This proves cancellation at the documented quantum boundary and generation
invalidation, not in-operator interruption or cancellation latency. No
performance, HBM-pressure, full-matrix or vLLM comparison claim follows.

`results/20260715-native-http-pressure-v1/` extends the native HTTP lifecycle
smoke to a full 32-state arena and sustained generation churn. After 32 cold
requests fill physical IDs 1–32, the client performs 64 cycles. Each cycle
resumes one state, cancels only after a native batch is observably in flight,
confirms the old generation returns `StaleState`, and issues a cold replacement.
The replacement must return token `525`, reuse the same physical ID, and advance
the generation by exactly one. Rotation covers every slot twice; all 32 finish
at generation 3. The record contains 224 raw HTTP rows, 16 executor snapshots,
and the most recent 128 scheduler plans as separately hashed artifacts.

Across all post-setup snapshots, live native allocation and peak live
allocation remain exactly 16,038,438,176 bytes, workspace capacity remains
268,435,456 bytes with a 104,617,472-byte peak, and HBM use ranges from
16,595,841,024 to 16,596,590,592 bytes. The 749,568-byte observed range is below
the pre-registered 67,108,864-byte guard. All 64 cancellations are accepted,
all 64 stale handles are rejected, all 64 replacement prefills pass token
parity, and explicit shutdown leaves no model or HTTP process.

This is `real-online-smoke` evidence for capacity, generation safety, slot
reuse, and observed memory boundedness under this fixed 64-cycle workload. It
does not establish request/s, output token/s, TTFT/TPOT, tail latency, SLA,
general prompt lengths, 128-token parity, policy superiority, the complete
90-cell matrix, or superiority over vLLM.

## Native device-side greedy selection (component diagnostic)

`results/20260715-native-host-argmax-buckets-v1/` and
`results/20260715-native-device-argmax-buckets-v1/` isolate one avoidable
native decode cost. The baseline copies every BF16 logit to the host and scans
on the CPU. The optimized path casts BF16 logits to exactly representing FP32
on the NPU, executes ArgMax there, and copies back one INT32 token per row.
Both clean-commit runs pass the same 63-dispatch token, capacity, eviction,
generation-reuse and heterogeneous-state gates.

Paired median executor-time ratios are 1.02x, 1.04x, 1.10x, 1.17x and 1.33x
for batch sizes 1, 2, 4, 8 and 16. The single batch-32 observations are
69,516,037 ns and 22,175,710 ns (3.13x). Because that largest bucket has only
one sample and the workload uses short scripted contexts, these are component
optimization diagnostics, not serving throughput or latency claims. In
particular, no reciprocal executor latency is reported as request/s or output
token/s.

`results/20260715-native-http-pressure-device-argmax-v1/` then repeats the
64-cycle real-online lifecycle gate with the optimized executor. All 64
cancellations, stale-generation rejections and same-slot replacements pass.
Live native allocation remains fixed at 16,057,902,496 bytes and observed HBM
drift is 491,520 bytes, below the preregistered 67,108,864-byte guard. This
confirms bounded memory for the added device buffer under the fixed pressure
smoke; it adds no concurrency, full-matrix, long-output or vLLM claim.

## Native exact replay and continuation semantics

`results/20260715-native-http-exact-replay-v1/` validates the corrected native
state contract through a clean-commit live HTTP service. One cold request
creates a four-token physical state and retains deterministic token `525` as
the pending decision. Sixty-four exact requests at client concurrency 32 all
return `525`, preserve the same source handle, report four reused tokens and
zero prefill/decode executor time. The runtime's retained-decision counter
increases by 64 while its executor-batch counter increases by zero. A forged
generation is rejected with `409 StaleState` by the Rust registry.

This proves immutable exact/one-token replay and generation validation, not
throughput or a vLLM advantage. The run is a small `real-online-smoke` with no
independent lifecycle repetitions. Mutating generation now uses the separate
`continue` input kind.

`results/20260715-native-http-pressure-semantic-split-v1/` reruns the full
32-slot, 64-cycle cancellation and replacement gate under that split. All
cancellations, stale-generation rejections and replacement token checks pass;
live allocation remains fixed at 16,057,902,496 bytes and observed HBM drift is
749,568 bytes below the 67,108,864-byte guard. It remains lifecycle and memory
smoke evidence, not a formal matrix cell.

## Native 2,177-token cold-prefill gate

The native ACLNN executor now supports uniform variable-length prefill instead
of only the original four-token fixture. A real single-910B2 component probe
reconstructed the exact 2,177 Qwen token IDs used by
`benchmarks/state_reuse.py`, ran all 28 layers without Torch or vLLM in the
candidate process, emitted greedy token `16` matching the pinned-vLLM result,
and retained a 2,177-token state. The measured executor duration is a diagnostic
for one cold prefill, not a serving-latency or throughput claim. The eager
32-state by 4,096-token KV reservation raises live allocation to roughly
23.6 GB, so paged/demand-backed allocation remains an explicit follow-on gate.

`results/20260715-native-http-exact-replay-2177-v1/` records the corresponding
clean-commit live HTTP smoke. The native cold seed emits token `16`; 64 exact
replays at client concurrency 32 all reuse 2,177 tokens, preserve the source
handle, and increase the retained-decision counter by 64 with zero additional
executor batches. One forged generation is rejected with HTTP 409. This proves
the long-prompt exact/one-token service semantics only; reciprocal request
latency is deliberately not reported as throughput.

## Native immutable KV fork gate

The native protocol can combine state reuse and state creation on the first
decode step of a longer exact request. In the real NPU component probe, source
state 1 was forked in one batch to states 2, 3 and 4. All branches emitted
token `264` at context length 5; the source then independently emitted `264`
from its original context, and executor statistics reported four active
states. Torch and vLLM were absent. This proves source immutability, branch
identity and batched fork execution only. The implementation currently copies
the full valid KV range on device, so the result is not evidence of efficient
copy-on-write or serving throughput.

The clean live HTTP record
`results/20260715-native-http-exact-fork-output32-c8-v1/` runs eight concurrent
32-token exact requests. All eight outputs exactly equal the first 32 tokens of
the pinned-vLLM oracle, their branch IDs are distinct, and the source remains
unchanged and replayable. Thirty-one continuation steps execute as 31 decode
batches with maximum batch size 8. This is one correctness/batching smoke cell,
not a formal throughput or latency comparison.

`results/20260715-native-http-exact-fork-output32-c32-v1/` repeats the gate at
the maximum required concurrency. All 32 requests produce the exact 32-token
oracle sequence and distinct branches, the source remains replayable, and the
executor reaches batch size 32 for each of 31 decode positions. It fills 33
states including the source. The four-token seed makes this a full-cohort
mechanism gate, not the formal 2,177-token workload or a comparative result.

`results/20260715-vllm-long-prompt-oracle-128-v1/` freezes the pinned baseline's
128 greedy tokens for the exact 2,177-token historical prompt. The matching
native record is `results/20260715-native-http-long-exact-output128-c32-v2/`.
All 32 concurrent native requests reproduce all 128 tokens, receive distinct
branches and preserve the source; the 127 continuation positions reach decode
batch size 32. This is the maximum exact correctness/batching cell, not a
throughput or latency comparison.

## Closed-loop exact c32/o128 diagnostic repetitions

`results/20260715-native-exact-throughput-c32-o128-r64-v1/` and
`results/20260715-vllm-exact-throughput-c32-o128-r64-v4/` are matched
single-lifecycle real-online cells: one 910B2, Qwen2.5-7B-Instruct BF16, the
same 2,177-token prompt, concurrency 32, 64 requests and 128 greedy output
tokens. Both retain raw rows and pass complete token parity.

The native run measures 7.881 request/s and 1008.714 output token/s; the pinned
vLLM run measures 0.6916 request/s and 88.519 output token/s. The observed
single-run ratio is 11.40x. Native versus vLLM P95 wall latency is 4068.93 ms
versus 46,452.07 ms, and P95 TPOT is 32.000 ms versus 356.198 ms. Peak sampled
board HBM is 26,388 MiB versus 53,546 MiB. These are real measurements for one
lifecycle, but they do not alone establish a repeated result.

Three preceding baseline directories ending in `v1`, `v2` and `v3` are marked
`FAILED`: vLLM's fixed 20-second subprocess preflight timed out before service
startup and no requests ran. The valid v4 lifecycle first records a successful
unbounded equivalent NPU allocation probe, then disables only the duplicate
timeout guard; graph mode and serving configuration remain unchanged.

Two further clean service lifecycles per system are retained in the matching
directories ending in native `v2`/`v3` and vLLM `v5`/`v6`. Native output
throughput across the three runs is 1008.714, 598.331 and 650.052 token/s;
vLLM output throughput is 88.519, 86.885 and 91.440 token/s. The deterministic
paired aggregate in
`results/20260715-exact-throughput-c32-o128-r64-diagnostic-v1/aggregate.json`
reports a lifecycle-median ratio of 7.344x and a paired-bootstrap 95% interval
of [6.887x, 11.395x]. The corresponding P95 wall-latency ratio interval is
[0.0876, 0.1465], where lower is better. All 384 measured outputs have exact
token parity.

The first native lifecycle is substantially faster than the next two. It is
not removed or averaged away; this variability remains an investigation item.
More importantly, all six runs contain only 64 measured requests. The frozen
core contract requires 512 requests per lifecycle, and the derived artifact
therefore records `acceptance.status = not-evaluated` and a failed formal
request-count eligibility flag. This diagnostic is evidence that a formal run
is worthwhile, not evidence that the exact c32/o128 core gate has passed.

The first 512-request tagged baseline attempt is retained at
`results/20260715-vllm-exact-c32-o128-r512-formal-r1/` with a `FAILED` marker.
Its server returned all 514 HTTP responses, but the client exited during final
validation before the old harness wrote raw rows, and stderr was not captured.
It is inadmissible. The harness now writes failure rows and validation metadata
before exiting, captures client stderr, and records an NPU snapshot in failure
cleanup. Replacement lifecycles use new prompt tags and result directories.

The shorter tagged diagnostic in
`results/20260715-vllm-exact-c32-o128-r64-tagged-diagnostic-v1/` then failed
between its first cold and second prefix-hot warmup. A row-preserving repeat at
`results/20260715-vllm-exact-warmup-divergence-repeat-v2/` reproduces the exact
same prompt at concurrency 1: both outputs contain 128 tokens and first diverge
at generated-token index 53. A different suffix-tag control in
`results/20260715-vllm-exact-warmup-divergence-v2/` stays stable across two
warmups and one measured request, showing prompt-specific rather than universal
divergence. Before any valid baseline lock or formal candidate run, the frozen
protocol was amended to put a fixed-format identity prefix before the shared
long body and to require cold-seed/hot-verification token parity before timing.

That first unaligned-prefix smoke is retained at
`results/20260715-vllm-exact-prefix-prompt-smoke-r00/`: its 2,193-token prompt
has a 17-token cache tail and cold/hot outputs first diverge at generated-token
index 18. Before any valid formal baseline or candidate lifecycle, the protocol
was further frozen to insert neutral prefix padding until the tagged prompt has
the historical one-token cache tail. This controls a measured correctness
confounder; it does not admit any failed run.

The subsequent block-aligned smoke at
`results/20260715-vllm-exact-aligned-prefix-smoke-r00/` proves a 2,433-token
prompt with `mod 128 = 1`, yet its cold/hot outputs first diverge at generated
token 54. This falsifies block alignment as a sufficient control. Before any
valid formal baseline lock or candidate run, lifecycle identity was therefore
removed from model tokens entirely: the historical 2,177-token prompt remains
byte-for-byte fixed, while the unique tag lives in the manifest, result
metadata and native state namespace. Clean services prevent cross-lifecycle
cache leakage. None of the failed tagged runs is admitted.

The final metadata-only control at
`results/20260715-vllm-exact-metadata-tag-smoke-r00/` restores the historical
2,177-token prompt and original SHA while retaining a unique manifest tag. Its
cold seed, prefix-hot verification and measured request reproduce the same
128-token sequence, and the NPU is clean after shutdown. This is the required
correctness smoke for the revised identity protocol, not a formal performance
cell.

The first full metadata-only replacement lifecycle at
`results/20260715-vllm-exact-c32-o128-r512-formal-r01-v2/` is also retained
with `FAILED`. All 512 measured requests returned successfully, but 16 rows
did not reproduce the cold-seed oracle. The 16 rows all produced the same
alternative 128-token sequence, while the other 496 reproduced the oracle;
the first token difference is at generated-token index 29. Consequently its
observed 3.853 request/s and 493.136 output token/s are diagnostic only and
cannot enter a baseline lock or candidate comparison.
That retained result's top-level `all_outputs_exact: true` reflects a harness
bug: the field was hard-coded even when `validation.passed` was false. The
harness now derives it from the complete request/error/oracle validation; the
raw failed artifact is intentionally not rewritten after the run.

Two single-factor follow-ups show that this is not explained solely by prefix
caching or ACL graph replay. With graph mode retained and prefix caching
disabled,
`results/20260715-vllm-exact-c32-o128-r128-no-prefix-diagnostic-v2/`
contains 4 oracle mismatches among 128 measured requests. With both prefix
caching and graph capture disabled,
`results/20260715-vllm-exact-c32-o128-r128-eager-no-prefix-diagnostic-v1/`
still contains 3 mismatches, at ordinals 13, 45 and 77. Those ordinals are one
32-request cohort apart, which is consistent with a batch-slot-dependent
execution effect but does not by itself identify the faulty operator. Eager
mode remains inadmissible for baseline performance. The formal exact
c32/o128 baseline is therefore not established; the correctness gate is not
relaxed and r02/r03 have not been started.

The pinned vLLM-Ascend batch-invariance feature was then tested using its
official AArch64 custom OPP and Torch extension packages. Package identities
are frozen by SHA-256, and both the official matrix-multiply and fused-attention
operator examples pass on the reserved 910B2. Enabling those operators with
the former full-and-piecewise graph configuration fails during ACL graph
capture before health readiness. The retained startup evidence is
`results/20260715-vllm-exact-c32-o128-r128-batch-invariant-full-graph-failed-v1/`;
it contains a `DIAGNOSTIC_ONLY` marker and no request-level performance result.

Using the configuration documented by the pinned backend—batch invariance plus
`PIECEWISE` graph mode—starts successfully. In
`results/20260715-vllm-exact-c32-o128-r128-batch-invariant-piecewise-diagnostic-v1/`,
both warmups and all 128 measured c32/o128 requests reproduce the same complete
128-token oracle. Observed throughput is 1.066 request/s and 136.466 output
token/s; wall-latency median/P95/P99 are 29,950.16/30,081.18/30,097.41 ms,
TTFT median/P95/P99 are 765.60/1,093.68/1,131.22 ms, and TPOT
median/P95/P99 are 228.939/230.621/230.992 ms. Peak sampled board HBM is
53,518 MiB.

This 128-request run is a protocol-selection diagnostic, not a formal baseline
or performance gate. The former non-invariant 512-request run remains visible
with its higher but inadmissible 493.136 output token/s. Since exact token
parity is a pre-existing hard gate, the formal baseline is amended before any
valid candidate lifecycle to require the correctness-preserving official
batch-invariant `PIECEWISE` mode. Three clean 512-request lifecycles are still
required before the exact c32/o128 baseline can be locked.

The first two 512-request replacements using that mode are retained at
`results/20260715-vllm-exact-c32-o128-r512-formal-bi-piecewise-r01-v1/` and
`results/20260715-vllm-exact-c32-o128-r512-formal-bi-piecewise-r02-v1/`.
Both launch from parent commit `53d2c47`, return 512/512 successful requests,
match all 65,536 generated tokens to their cold-seed oracle, retain two matching
warmups and leave NPU 7 empty after scoped shutdown.

They nevertheless fail the pre-registered cross-lifecycle stability gate.
r01 measures 9.918 request/s and 1269.547 output token/s with P95 TPOT
24.397 ms; r02 measures 1.090 request/s and 139.518 output token/s with P95
TPOT 231.954 ms. Both logs name the same container-global compilation-cache
directory, and its files predate both services. The available evidence does not
prove which cached dispatch or generated artifact caused the different steady
states, so r01 is not treated as an optimization and r02 is not silently chosen
as the baseline. Neither enters a baseline aggregate.

Before any candidate formal lifecycle, the replacement protocol now creates a
fresh project-local compilation-cache directory for every service lifecycle,
requires that directory to be absent before launch, and retains a canonical
SHA-256 listing of its files. The two correct but uncontrolled-cache runs remain
formal-attempt evidence for correctness and instability only.

A 128-request attribution diagnostic using a fresh project-local cache is
retained at
`results/20260715-vllm-exact-c32-o128-r128-bi-isolated-cache-d01-v1/`.
It passes 128/128 oracle checks and measures 137.007 output token/s, matching
the slow state of the uncontrolled-cache r02 rather than the anomalous fast
r01. It remains diagnostic because it is below the 512-request eligibility
floor.

The subsequent three 512-request fresh-cache lifecycles are retained at
`results/20260715-vllm-exact-c32-o128-r512-formal-bi-isolated-r01-v1/` through
`r03-v1/`. All three pass 512/512 complete-sequence parity, use caches absent at
launch, retain cache file hashes and leave NPU 7 empty. Their output throughput
is 138.244, 141.130 and 139.167 token/s; P95 TPOT is 230.583, 226.722 and
231.711 ms; peak sampled HBM is 53,518 MiB in every run. Throughput, wall-tail
and TPOT stability are within the frozen 15% ceiling.

They do not form a baseline lock. P95 TTFT is 849.649, 802.062 and 941.420 ms,
whose `2 * max_relative_delta` is 21.60%. Request rows show that the excess is
concentrated in each lifecycle's first 32-request cohort; the two serial
warmups did not exercise the concurrency-32 graph/scheduler shape. The three
directories therefore carry `UNSTABLE_BASELINE.md`. Before any formal
candidate lifecycle, both baseline and native exact runners now retain two
shape-matched concurrent warmup cohorts and an entirely new three-lifecycle
baseline series is required. No performance comparison uses these unstable
runs.

## Shape-warmed engineering baseline and native diagnostics

Two replacement baseline lifecycles with two concurrency-32 warmup cohorts are
retained locally as
`results/20260715-vllm-exact-c32-o128-r512-formal-bi-shaped-r01-v1/` and
`results/20260715-vllm-exact-c32-o128-r512-formal-bi-shaped-r02-v1/`. Both pass
all 512 complete-sequence oracle checks. Their output throughput is 136.929 and
138.335 token/s, and P95 TPOT is 233.431 and 233.828 ms. They are accepted as a
stable engineering baseline so development does not repeatedly remeasure the
same vLLM path. They do not satisfy the pre-registered three-lifecycle formal
lock, which is explicitly deferred until a publication-grade comparison needs
to be frozen.

Against the second shape-warmed lifecycle, the local 128-request native exact
diagnostic `.benchmarks/native-exact-shaped-c32-o128-r128-d02/` measures
694.341 output token/s and P95 TPOT 49.134 ms, corresponding to an observed
5.019x throughput ratio and 4.759x lower P95 TPOT for this exact-hot workload.
All 128 native outputs are exact and the serving path contains neither Torch
nor vLLM. This is an engineering diagnostic, not a formal superiority claim:
the request counts and lifecycle counts are unmatched.

## Native shared-prefix extension correctness smoke

Commit `8ba6aa1` adds a real `prefix_extension` request path rather than
relabelling an exact-state hit. The runtime forks one immutable source state,
forces each suffix prompt token through native decode, ignores intermediate
argmax decisions, and starts returned generation from the decision after the
last suffix token. The source remains unchanged and temporary branches are
generation-safely recycled. The first implementation still performs a full
device-to-device K/V copy; paged reference sharing and last-block copy-on-write
remain future work.

The clean NPU 7 record is
`results/20260715-native-prefix-extension-p2048-e129-c4-o32-r4-smoke-v1/`.
It retains a 2,048-token prefix of the fixed 2,177-token prompt, executes the
remaining 129 prompt tokens on four concurrent branches, and generates 32
tokens per branch. All 4/4 sequences match the pinned vLLM oracle, every row
reports a prefix hit with 2,048 reused tokens, the executor has one active
source state both before and after the cohort, and NPU 7 is empty after scoped
shutdown. The observed 22.429 output token/s and 26,388 MiB peak sampled HBM
are recorded but carry no performance claim because this is a four-request
correctness smoke.

## Native mixed hot/cold correctness smoke

The native diagnostic client now submits deterministic concurrency cohorts
containing three exact-state requests and one explicitly cold prefill. This is
real execution-path mixing: the hot requests fork the resident source and the
cold request performs full native prefill. Cohorts are bounded to one
2,177-token cold request because the current executor's aggregate prefill-row
limit is 2,304; exceeding that budget is rejected by the client rather than
silently changing the prompt or concurrency.

`results/20260715-native-mixed-hot-cold-c4-o32-r16-smoke-v1/` records four such
cohorts on NPU 7. All 12 exact-hot rows report 2,177 reused tokens, all four
forced-cold rows report zero reused tokens, and all 16 generated 32-token
sequences match the pinned oracle. Active executor states are one before and
after the measured interval, showing that every temporary hot branch and cold
state was recycled. The observed 80.800 output token/s and 26,388 MiB sampled
peak HBM are diagnostic only. Because both classes intentionally use the same
oracle prompt, this does not yet establish the formal independent-cold mixed
workload or any vLLM comparison.

## MiniMax-M2.5 real-weight Q/K/V and Q/K norm component gate

`results/20260716-minimax-m25-w8a8-attention-component-v1/` is a clean-commit
real Ascend 910B2 component-correctness record for the native MiniMax port. Its
tensor manifest binds 16 layer-0 attention tensors ranged from four shards of
the pinned `Eco-Tech/MiniMax-M2.5-w8a8-QuaRot` revision. Source shard digests
are recorded as repository metadata; each downloaded tensor range has its own
locally recomputed SHA-256.

The direct C++ candidate dynamically quantizes one four-token BF16 activation
and reuses it for the real checkpoint Q, K, and V W8A8 projections. It then
applies the checkpoint Q/K RMSNorm weights. CPU int32-accumulator projection
oracles consume the actual NPU quantized activations and scales; FP32 RMSNorm
oracles consume the actual projection outputs. Q, K, V, Q-norm, and K-norm all
report zero elements outside the declared tolerances. The maximum absolute
errors are 0.007607, 0.003893, 0.005656, 0.015431, and 0.014949 respectively.

This record contains neither Torch, Transformers, nor vLLM execution. It proves
only the real-weight attention front-half component contract. Partial RoPE,
GQA attention, reusable K/V state materialization, O projection, MoE,
collectives, full-model correctness, and performance remain unproven.

The clean-commit successor
`results/20260716-minimax-m25-w8a8-attention-state-v3/` adds model-semantic
partial RoPE and paged state. It presents strided views of the first 64
dimensions of each 128-wide Q/K head to `aclnnApplyRotaryPosEmbV2`, using theta
5,000,000 and half rotation. Q and K have zero out-of-tolerance elements versus
CPU formulas; all 14,336 unrotated Q/K tail elements remain bit-identical.

The project-owned `PagedKvAllocator` creates a generation-tagged state under a
namespace containing model revision, weight identity, RoPE configuration, and
KV dtype. It assigns one 128-token physical page for the four-token fixture.
`aclnnScatterPaKvCache` then writes rotated K and V directly from NPU operator
outputs into the HBM page. Reading the assigned slots back yields zero K or V
element mismatches. The declared GQA state occupies 4,096 bytes per token per
layer for eight BF16 K heads plus eight BF16 V heads.

This is state materialization correctness, not yet a reusable-state serving
result: attention has not consumed the page, and state fork/reuse behavior is
covered only by the separate generic allocator tests. GQA aggregation, O
projection, MoE, collectives, full-model correctness, and performance remain
unproven for MiniMax.

## MiniMax-M2.5 real-weight attention sublayer component gate

`results/20260716-minimax-m25-w8a8-attention-sublayer-v4/` is a clean-commit
real Ascend 910B2 component record for the layer-0 attention sublayer. The
direct C++/ACLNN chain now executes input RMSNorm, dynamically quantized real
Q/K/V projections, full-vector Q/K RMSNorm, 64-of-128 partial RoPE, causal GQA,
real O W8A8 projection, and paged K/V state materialization. It does not call
Torch, Transformers, or vLLM.

An earlier diagnostic fixture became proportional across token rows after
RMSNorm and was rejected as a meaningful attention test. The accepted fixture
uses position-dependent non-proportional rows: all four normalized input rows
and all four attention output rows are distinct, and six future-token entries
are masked. The causal GQA result has maximum absolute error 0.000252 and mean
absolute error 0.00000865 versus a stable-softmax CPU oracle. The real O
projection has maximum absolute error 0.099957 and mean absolute error
0.00003797; all elements satisfy the declared absolute-plus-relative gate.
Every preceding projection, normalization, RoPE, and state comparison also has
zero out-of-tolerance elements.

The CPU oracle for each stage consumes the immediately preceding real NPU
output, which localizes operator-contract errors but is not an independent
end-to-end framework oracle. The attention operator consumes contiguous Q/K/V;
the same rotated K and V are separately materialized into the verified paged
state for future decode. Residual/post-attention normalization, MoE routing and
experts, inter-device communication, full-model correctness, state reuse during
decode, and performance remain unproven.

## MiniMax-M2.5 attention residual and post-norm component gate

`results/20260716-minimax-m25-w8a8-attention-residual-v5/` extends the
clean-commit native layer-0 path through `aclnnAddRmsNorm`. It adds the real O
projection to the original deterministic hidden row, materializes the BF16
attention residual, and applies the checkpoint post-attention RMSNorm weight.
The residual and normalized output both have zero out-of-tolerance elements.

The residual comparison uses the FP32 addition formula. The RMSNorm oracle is
separately evaluated from the actual materialized BF16 residual, matching the
fused operator boundary rather than silently treating an unrounded sum as its
input. Input, Q, K, and post-attention rstd maximum errors are all below the
explicit `1e-5` gate; the post-attention value is `1.36e-7`.

This proves the real-weight attention-side path through the input expected by
the MoE router. It does not prove MiniMax routing, expert execution, a complete
decoder layer, multi-device communication, full-model correctness, or
performance.

## MiniMax-M2.5 real-weight FP32 router component gate

`results/20260716-minimax-m25-w8a8-router-v6/` is a clean-commit real Ascend
910B2 record for the layer-0 router. The direct C++/ACLNN process first runs the
accepted real-weight attention path through post-attention normalization, then
casts that actual activation to FP32 and computes all 256 router logits. It
uses the checkpoint BF16 gate and FP32 correction bias from pinned revision
`9118343f43b8177306a312fcc0c8b766012796b8`.

The native chain applies sigmoid, adds correction bias for expert selection
only, and selects eight experts per token with `aclnnTopk`. Router logits have
maximum absolute error `6.68e-6` against a CPU FP32 oracle. Sigmoid, biased
selection scores, Top-8 values, and all 32 expert IDs have zero elements or IDs
outside their gates. The four non-degenerate token rows choose four distinct
expert sets, and the minimum score margin between the eighth and ninth experts
is `9.82e-4`. Selected unbiased sigmoid scores normalize to one with maximum
error `1.20e-7`.

The parent commit is `4d84473299c4c96313583ef50f6ad70d84de7f54` and the
record reports Torch, Transformers, and vLLM as absent from the candidate
runtime. vLLM sources were used only to cross-check checkpoint routing
semantics. This gate proves FP32 logits and Top-8 selection; routed-score gather
and normalization are still host-audited. It does not prove expert execution,
MoE output, inter-device communication, a complete decoder layer, full-model
correctness, or performance.

## MiniMax-M2.5 router-selected W8A8 expert component gate

`results/20260716-minimax-m25-w8a8-selected-experts-v7/` is a clean-commit
real Ascend 910B2 record for the experts reached by the accepted four-token
layer-0 route. The formal router selects 32 token-expert paths spanning 26
unique experts. A provenance-checked ranged fetch materializes 234 real
checkpoint tensors—`w1`, `w3`, and `w2` weight, scale, and offset for every
selected expert—without treating this subset as the full 256-expert model.

For each of the 26 experts, the direct C++ candidate dynamically quantizes the
real post-attention normalized activation, executes W8A8 `w1` and `w3`, applies
native `aclnnSwiGlu` as `silu(w1) * w3`, dynamically quantizes the intermediate,
and executes W8A8 `w2`. Gate, up, SwiGLU, and down comparisons all report zero
out-of-tolerance elements. Their maximum absolute errors are `0.031249`,
`0.0154862`, `0.062336`, and `0.203133`; mean absolute errors across all
experts are `0.00337776`, `0.00111426`, `0.0016118`, and `0.00528652`.

The parent commit is `5c74fba84c55e50d5bc0086c8e00a4c9b4d7c53b`; Torch,
Transformers, and vLLM are absent from the candidate runtime, and NPU 7 is free
after the run. Expert dispatch and routed weighted aggregation are still
host-audited. This record does not prove native grouped expert execution,
complete 256-expert coverage, EP/TP communication, a complete decoder layer,
full-model correctness, or performance.

## MiniMax-M2.5 NPU-routed aggregation and layer residual gate

`results/20260716-minimax-m25-w8a8-layer0-moe-v8/` extends the same real
attention, router, and 26 selected-expert chain through the MoE update and
layer output. For each of the eight route ranks, the candidate casts expert
outputs to FP32, multiplies by the selected unbiased normalized router weight,
sums all ranks with `aclnnSum`, casts the result to BF16, and adds it to the
materialized attention residual on NPU.

The aggregated MoE update has maximum absolute error `0.0472622` and mean
absolute error `0.0014939`; the resulting layer output has maximum absolute
error `0.046875` and mean absolute error `0.00160362`. Both comparisons contain
zero out-of-tolerance elements. The parent commit is
`82e8be7ddef30c0c0608c5d59a61bc8cd98b8099`, the candidate runtime contains no
Torch, Transformers, or vLLM, and NPU 7 is free after the run.

This gate still uses 32 host-directed device-to-device row copies to gather the
already-computed expert outputs into route-rank tensors. It therefore proves
NPU route weighting, aggregation, and residual correctness, but not native
grouped token dispatch, all 256 experts, TP/EP communication, independent
full-layer framework parity, full-model correctness, or performance.

## MiniMax-M2.5 NPU route-gather gate

`results/20260716-minimax-m25-w8a8-npu-route-gather-v9/` removes the 32
route-dependent host-directed row copies from v8. The candidate first
materializes the 26 complete expert-output matrices into a route-independent
device table. It then converts every `(expert ID, token ID)` route to a linear
table index and invokes `aclnnIndexSelect` once to gather all 32 expert rows on
NPU. FP32 weighting, Top-8 summation, BF16 conversion, and residual addition
remain on NPU.

The MoE update and layer-output errors are unchanged from v8 and both contain
zero out-of-tolerance elements. The record reports zero host-gathered route
rows, 26 host-materialized expert matrices, and 32 NPU-gathered rows. Its parent
commit is `10befee4a425915cb2be88fc316fd0c594d34ac4`; Torch,
Transformers, and vLLM remain absent, and NPU 7 is free after the run.

This is native route gather and aggregation evidence, not grouped expert
execution: the 26 expert gate/up/down paths are still launched independently
over four rows each, including rows that do not route to that expert. It does
not prove routed-row-only grouped matmul, all 256 experts, TP/EP communication,
independent full-layer framework parity, full-model correctness, or
performance.

## MiniMax-M2.5 grouped routed-expert gate

`results/20260716-minimax-m25-w8a8-grouped-moe-v10/` is the clean-commit
successor to v9. It preserves the same real layer-0 activation, accepted Top-8
routes, 26 selected checkpoint experts, and direct ACLNN candidate boundary,
but replaces independently issued full expert matrices with grouped execution
of the 32 actual token-expert paths.

The NPU gathers routed inputs in expert-major order, runs fused grouped W8A8
gate/up + SwiGLU + requant, runs the grouped W8A8 NZ-weight down projection,
restores router order, and performs FP32 route weighting/sum plus the BF16
residual. No host route rows or full expert output matrices are materialized.
The grouped down projection, weighted MoE output, and final layer residual all
have zero elements outside their declared tolerances. The down projection's
maximum/mean absolute errors are `0.114952/0.00363919`; the weighted output's
are `0.0472622/0.00149566`; the layer residual's are
`0.03125/0.00159112`.

Relative to v9's `26 * 4 = 104` expert rows, v10 executes 32 routed rows and
therefore removes 72 unused rows in this fixture. This is a count derived from
the executed shapes, not a measured speedup. The record does not establish
all-256-expert coverage, TP8/EP8 communication, a complete decoder layer,
full-model correctness, or performance superiority.

## MiniMax-M2.5 independent complete layer-0 oracle gate

`results/20260716-minimax-m25-w8a8-layer0-oracle-v11/` advances v10 from
operator-local comparisons to an independent checkpoint-to-layer-output gate.
The offline NumPy oracle reconstructs the deterministic input and reads raw
attention, router, and selected-expert checkpoint tensors. It independently
recomputes RMSNorm, dynamic W8A8 projections, partial RoPE, causal GQA,
selection-only-bias Top-8 routing, routed experts, weighted aggregation, and
the final residual. It does not read candidate intermediates.

The native candidate and oracle select the same 32 route IDs. Independent
post-attention normalization has maximum/mean absolute error
`0.03125/0.00100973`; route weights `0.000129819/0.0000194306`; MoE update
`0.125/0.0140035`; and final layer output `0.09375/0.0140545`. Every comparison
passes the frozen gate (`atol=0.125`, `rtol=0.03` for accumulated BF16 layer
values). The formal run's parent is clean commit
`c8993716c4c70446ec0e58e5ef8f95c77da6ba40`; the candidate path uses no Torch,
Transformers, or vLLM, and NPU 7 is free after the run.

This proves the complete MiniMax layer-0 path only for the four-token fixture
and its 26 selected experts. It does not prove loading all 256 experts, TP8/EP8
communication, later layers, full-model correctness, or performance.

## MiniMax-M2.5 all-expert artifact and loader gates

`results/20260716-minimax-m25-w8a8-all-experts-layer0-v12/` is a clean-commit
artifact-validation record for every layer-0 routed expert. It verifies 2,304
checkpoint tensors covering expert IDs 0 through 255, with total exact size
3,636,461,568 bytes and ordered manifest SHA-256
`c750f31970d023410e447b4f60531a925b599cdc1bfce3e5b9b88524a2722ba0`.
All 768 offset tensors are byte-zero. The frozen contiguous EP8 plan assigns
32 experts, 288 tensors, and 454,557,696 bytes to each rank. This record proves
artifact identity, completeness, and planned placement only; it contains no
candidate execution or communication result.

`results/20260716-minimax-m25-w8a8-all-expert-loader-v13/` is the corresponding
clean-commit real-910B2 loader gate. Rather than reading the earlier
26-selected-expert pack, the native candidate resolves those same 26 experts
from the complete 256-expert artifact, executes the 32 routed token-expert
paths, and passes the independent checkpoint-to-layer-output oracle. All
comparisons contain zero out-of-gate elements; independent MoE output has
maximum/mean absolute error `0.125/0.0140035`, and final layer output
`0.09375/0.0140545`. The run used clean parent
`9469554ce31c7491b5cd8136f3bdff9263756011` and left NPU 7 free.

The distinction is deliberate: v12 establishes all-256 artifact and EP8
placement integrity, while v13 establishes that the candidate loader can use
that artifact for the actually routed experts. Neither result claims that all
256 experts executed, that eight ranks communicated, that a full model ran, or
that performance exceeds a baseline.

## Native eight-rank HCCL All-to-All gate

`results/20260716-native-hccl-alltoall-v14/` is a clean-commit real-online
communication correctness record on all eight Ascend 910B2 devices. The
project-owned C++/AscendCL candidate calls `HcclCommInitAll`, creates one
thread and stream per rank, and invokes `HcclAlltoAll` directly. Each rank
sends 256 `uint32` values to every peer; each value encodes source rank,
destination rank, and element position so direction errors cannot pass a
checksum-only test.

All eight ranks report `exact=true`, zero mismatched elements, and identical
expected/observed checksums. The run used clean parent
`4abc4a9f8a6ecbb0c03e00e5e10a866733883c06`, CANN 9.0.0, and HCCL library
SHA-256 `1188f6acb2df4de12b887ab3d0a270c59d0b745e11f692929a6a6635c8cf3e4c`.
All devices are free after teardown. The candidate links neither Torch nor
vLLM.

The first dirty-tree development attempt failed before communication with
HCCL error 15 because devices had not been set before `HcclCommInitAll`.
Following the vendor single-process/multi-device contract fixed the
initialization order; the superseded failure is recorded in formal metadata.
This gate does not prove variable-count Top-8 expert dispatch, per-rank expert
residency, result combine, overlap, throughput, or full-model execution.

## MiniMax-M2.5 route-shaped EP8 dispatch/combine gate

`results/20260716-minimax-m25-ep-roundtrip-v15/` replaces v14's uniform
message sizes with the exact destination-rank counts induced by the accepted
MiniMax layer-0 router fixture. The 32 Top-8 paths map to the frozen contiguous
EP8 placement as `[2,6,4,8,1,3,4,4]`. Every source rank sends one synthetic
payload per path; each payload contains 1,536 `uint32` words, equal in bytes to
one 3,072-element BF16 hidden row.

The first `HcclAlltoAllV` dispatches variable path counts to the owning expert
ranks. A second variable collective sends every payload back to its source.
All eight ranks report zero forward word mismatches, zero roundtrip mismatches,
and matching checksums. The formal run used clean parent
`dfa4ccfa77132c698a8b1c6f2e7c638fa6d1d755`; all devices are free afterward,
and the candidate links no Torch, Transformers, or vLLM runtime.

The first dirty-tree attempt underallocated receive buffers on ranks 1 and 3
by assuming each rank's total send and receive volumes were equal. The accepted
run instead sizes each rank from its route-derived receive volume; formal
metadata records the superseded failure and correction. This is real EP8
communication and model-shaped routing evidence, but the payload is synthetic:
it does not prove resident expert weights, distributed W8A8 expert execution,
communication/computation overlap, throughput, or full-model correctness.

## MiniMax-M2.5 all-expert EP8 HBM residency gate

`results/20260716-minimax-m25-ep-residency-v16/` turns the v12 placement plan
into physical eight-device residency. Before launch, the harness rechecks the
SHA-256 and size of every one of the 2,304 tensors in the 3,636,461,568-byte
layer-0 expert artifact. Eight project-owned C++/AscendCL threads then allocate
one 454,557,696-byte contiguous HBM arena per 910B2 and load the rank's frozen
32-expert range: `0–31`, `32–63`, through `224–255`.

Every rank loads 288 tensors and copies each tensor back for byte comparison.
All ranks report zero mismatched tensors and identical host/device-roundtrip
byte sums. A synchronization latch holds every arena until all eight ranks
report loaded, establishing simultaneous rather than sequential residency.
The formal run used clean parent
`d7b8581007b74d8e7afec0050e1f1ba95702972b`; Torch, Transformers, and vLLM
are absent, and all devices are free after teardown.

The tensors are resident in checkpoint source layout. This gate does not yet
perform the gate/up interleave and FRACTAL_NZ transformation required by the
accepted grouped W8A8 operators, connect HCCL dispatch to expert computation,
or establish distributed layer correctness, overlap, throughput, or full-model
execution.

## MiniMax-M2.5 real-weight distributed EP8 MoE gate

`results/20260716-minimax-m25-ep-execution-v17/` connects the previously
separate route-shaped communication and real grouped-expert paths. Rank 0
loads the independent oracle's four-token, 3,072-wide BF16 post-attention
activation and accepted 32 Top-8 expert IDs. `HcclAlltoAllV` dispatches the
activation rows to their contiguous expert owners with rank counts
`[2,6,4,8,1,3,4,4]`.

Across the eight ranks, 26 unique real checkpoint experts execute the same
shared native grouped core used by the single-device layer gate: dynamic input
quantization, fused grouped W8A8 gate/up plus SwiGLU and requantization, then
grouped W8A8 FRACTAL_NZ down projection. Every rank executes exactly its routed
row count, and all local down-projection comparisons report zero mismatches.
HCCL sends the resulting 32 BF16 rows back to rank 0, where NPU IndexSelect
restores router order and NPU FP32 multiply/sum applies the accepted route
weights.

The final BF16 MoE update contains zero mismatched elements, zero maximum
absolute error, and zero mean absolute error against the independent NumPy
checkpoint-to-MoE oracle. The formal run used clean parent
`5f93b0794e0adb641db7639930cdc2721e48f276`; the candidate uses no Torch,
Transformers, or vLLM, and all eight devices are free after teardown.

This is the complete distributed MoE sublayer for one four-token fixture, not
a complete distributed decoder layer. It starts from an independently frozen
post-attention activation; attention and TP8 are not distributed. Selected
weights are transformed into grouped operator layouts during each run rather
than loaded as a persistent prepacked serving artifact. No latency, throughput,
overlap, later-layer, full-model, or baseline-superiority claim follows.

## MiniMax-M2.5 prepacked distributed EP8 MoE gate

`results/20260716-minimax-m25-ep-prepacked-execution-v18/` replaces v17's
per-run checkpoint transpose, gate/up interleave, and FRACTAL_NZ conversion
with a deterministic persistent execution artifact. The offline artifact
contains all 256 layer-0 experts split into eight contiguous 32-expert rank
packs. Its 32 files total 3,628,597,248 bytes; the manifest SHA-256 is
`d143f61e5e5296def6fb72a4156c24b77aee8762662bc12fbc901c487d3bf710`.

Each rank loads all four execution-layout files for its 32 experts directly
into HBM. The grouped operators receive all 32 local groups; repeated
cumulative boundaries encode experts with zero routed rows, so the accepted
fixture's 26 selected experts execute without selecting or transforming
weights for that request. HCCL dispatch/combine and rank-0 reorder/weight/sum
are unchanged from v17. Every rank's down comparison has zero mismatches, and
the final BF16 MoE update again has zero mismatches and zero absolute error
against the independent NumPy oracle.

The formal real-online run used clean parent
`ee07ae9987e1032015ec9cf1da1ad9c68d982e7a`; the candidate is project-owned
C++/AscendCL/ACLNN/HCCL with no Torch, Transformers, or vLLM candidate path,
and all eight devices are free after teardown. This result proves direct NPU
execution from the persistent prepacked artifact. The probe still loads once
per process rather than serving repeated requests in a long-lived runtime;
distributed attention/TP8, full-layer/model correctness, latency, throughput,
and baseline superiority remain unproven.

## MiniMax-M2.5 TP8 head-sharded attention component gate

`results/20260716-minimax-m25-tp-attention-v19/` is a clean-commit real-online
component run across all eight Ascend 910B2 devices. MiniMax's 48 query heads
and 8 KV heads are divided evenly into 6 query heads and 1 KV head per rank.
Every rank executes real W8A8 Q/K/V projections, Q/K RMSNorm, 64-of-128 partial
RoPE, and causal GQA. All per-rank component comparisons have zero out-of-gate
elements. Four token-wise BF16 `HcclAllGather` calls reconstruct the full
6,144-wide attention rows with zero communication mismatches.

Head-sharded and full 48-head FlashAttention kernels are not bit-identical:
16,548 BF16 elements differ, with maximum/mean absolute error
`0.029541/0.000691363`. This remains inside the pre-existing attention
component absolute tolerance of `0.03125`. After a rank-0 full-width O
projection and AddRMSNorm, 1 of 12,288 elements exceeds the stricter independent
post-attention layer tolerance; maximum/mean absolute error is
`0.421875/0.00381055`, so `strict_independent_parity=false` is recorded rather
than hidden behind a newly fitted threshold.

The formal run used clean parent
`f4ac51196f90c5cc6065645307b4fa8205544445`; Torch, Transformers, and vLLM are
absent from the candidate path, and all devices are free after teardown. This
proves the TP8 attention components and exact collective assembly only. O is
not yet row-sharded, QKV layouts are prepared per run, TP attention is not yet
connected to the prepacked EP8 MoE path, and no full-layer/model, serving,
performance, or baseline-superiority claim follows.

Later seeded validation found that v19's per-rank `RunRmsNorm` changed the
model semantics: it normalized each Q/K shard independently rather than
reducing across the complete checkpoint dimensions. Because its local oracle
made the same assumption, zero local mismatches did not validate the global
model operation. v19 is therefore superseded as TP model-semantic evidence.

## MiniMax-M2.5 complete TP8-to-EP8 layer diagnostic

`results/20260716-minimax-m25-tp8-ep8-complete-layer-v20/` connects the v19
head-sharded TP8 attention path to the v18 persistent prepacked EP8 MoE path.
After TP head assembly, rank 0 executes the current full-width O projection,
AddRMSNorm, and real router. The normalized BF16 activation is broadcast to
all ranks, `HcclAlltoAllV` dispatches actual routed rows, all ranks execute
their resident 32-expert packs, and a second collective combines outputs for
NPU route reorder, FP32 weighting/sum, and layer residual.

The complete dataflow executes successfully. All 32 Top-8 expert IDs match the
independent oracle, route counts remain `[2,6,4,8,1,3,4,4]`, every local down
comparison is zero, and internal NPU MoE aggregation and residual comparisons
are zero. The TP numerical difference nevertheless propagates: 2 router
weights exceed the single-device router tolerance (maximum/mean error
`0.000851199/0.000120787`), while independent MoE and final-layer comparisons
reject 63 and 70 of 12,288 elements. Final-layer maximum/mean absolute error is
`0.625/0.0284426`.

The formal clean-parent run is intentionally labeled
`real-online-exploratory-strict-rejection`; candidate exit status 3 is an
expected and checked part of the record. The parent is
`783029211353b657b4298ef85c4baffaffc957d0`, and all devices are free after
teardown. This result proves complete distributed dataflow and route-semantic
stability, but `complete_layer_parity=false` means it is not accepted
complete-layer correctness. No threshold was fitted to v20, and no full-model,
serving, performance, or baseline-superiority claim follows.

## MiniMax-M2.5 accepted TP8-to-EP8 layer gate

`results/20260716-minimax-m25-tp8-ep8-complete-layer-v21/` fixes the TP Q/K
normalization semantics that caused v20's rejection. Each rank performs BF16
to FP32 cast, square, and hidden-dimension reduction on NPU. HCCL AllReduce
forms the global per-token Q/K sum of squares, after which mean, epsilon,
reciprocal square root, local gamma multiplication, and BF16 materialization
remain on device. There is no host normalization fallback.

With global normalization, the assembled 6-head/rank TP attention is
element-identical to the full 48-head NPU attention. The complete downstream
router, broadcast, prepacked EP8 execution, combine, route weighting, and
residual path executes unchanged. Independent router IDs and weights, MoE
update, and final layer all report zero out-of-gate elements. Final-layer
maximum/mean absolute error is `0.09375/0.0140545`, matching the accepted
single-device oracle envelope.

The formal real-online run used clean parent
`71af7e5586344252d32ccf60422f76944481d012`, returned status 0, and released
all eight devices. This is accepted strict correctness for the seed-0 layer-0
fixture. O remains rank-0 full-width, QKV weights are still prepared per run,
and multi-fixture/length calibration, later layers, full-model generation,
serving, performance, and baseline superiority remain unproven.

## MiniMax-M2.5 Phase A v1 calibration rejection

`results/20260716-minimax-m25-phase-a-calibration-v22/` ran from clean parent
`5540b125a84b2cd7f9ffa34e095895e39a07599c`. Calibration seeds 0 and 1 passed
the registered hard invariants. Seed 2 was rejected before seeds 3–15 or any
holdout candidate ran because one exact Top-8 expert ID differed from the v1
NumPy layer oracle. The oracle selected expert 222 for token 3 rank 7; both the
TP8 path and the complete 48-head native NPU comparison selected expert 225.
Their route counts therefore differed by one path between EP ranks 6 and 7.

This was not a TP collective or local-shard error: gathered TP attention was
element-identical to complete native NPU attention, and their route IDs had
zero differences. A separate Torch/NPU diagnostic using the checkpoint's W8A8
projections, Prompt Flash Attention, AddRMSNorm, FP32 router, and Top-K also
selected expert 225. Against that NPU reference, the native layer output's
maximum/mean absolute error was `0.0625/0.00292962`; against the v1 NumPy route
it was `4.203125/0.256799` because the selected expert changed.

Protocol v1 remains rejected; no tolerance was widened after seeing the
failure. Protocol v2 keeps the same pre-frozen inputs and calibration/holdout
split but obtains exact attention and route semantics from the independent
real NPU reference. This is rejection and oracle-correction evidence, not an
accepted multi-fixture layer, full-model, serving, performance, or baseline
result.

The successor independent NPU reference cohort was generated on one real
Ascend 910B2 from clean parent
`1fc80f7baae7f1f95de0563d0455b704334a555b`. Its root manifest SHA-256 is
`7b667663dac563d0b3aa4c6f11833fd2d3fa044a39d03a38c2c96d1ae573b5b5`.
It contains 32 distinct inputs, preserves calibration seeds 0–15 and holdout
seeds 16–31, and includes seven fixtures with a zero-route EP rank. The
reference uses Torch/NPU only offline; it is not linked into or callable from
the candidate executor. No candidate holdout was run during reference
generation.

## MiniMax-M2.5 Phase A v2 calibration rejection

`results/20260716-minimax-m25-phase-a-npu-calibration-v23/` ran from clean
parent `b3b22a50c14edb21837712cdb2856651c62788fc`. Seeds 0–10 passed every v2
hard invariant, including seed 2 that rejected the old NumPy oracle. Seed 11
stopped the run before seeds 12–15 or any holdout candidate executed.

The seed-11 candidate and independent NPU oracle selected the same eight
experts for every token and produced identical EP route counts
`[2,8,5,5,5,1,4,2]`. At token 2, only experts 16 and 94 exchanged positions 2
and 3 in the sorted Top-8 output. TP8 and complete native NPU attention and
routes remained element-identical. Because route weights stay paired with
their expert IDs and MoE aggregation is a sum, the permutation has no model
semantic effect: final-layer maximum/mean error against the NPU oracle was
`0.015625/0.00176074`.

V2 is nevertheless recorded as rejected because its hard invariant demanded
positional order. V3 changes the invariant before further candidate execution:
the eight-expert set must match exactly for each token, and continuous weights
are compared after alignment by expert ID. A changed expert is still rejected.
No v2 threshold, holdout, full-model, serving, performance, or baseline claim
is accepted.

## MiniMax-M2.5 Phase A v3 calibration

`results/20260716-minimax-m25-phase-a-npu-calibration-v24/` completed seeds
0–15 from clean parent `ff6e4e77c70551c8bd821884798ddbaf7dd2a5c7`.
Every candidate cell returned status 0; all TP/full-head attention, collective,
per-token expert-set, expert-aligned router-weight, grouped expert, and complete
layer gates passed. Seed 11 reports two positional Top-K differences while its
expert-set mismatch and aligned-weight mismatch remain zero. Seeds 1, 6, 9,
and 14 exercise an EP rank with zero routed rows.

The calibration retained all raw boundary tensors and computed 196,608 BF16
comparisons for each hidden-state family plus 512 router weights. Historical
tolerance mismatches are zero across all four families. Pooled p99.9 absolute
error is `0.0078125` for post-attention, `6.47315e-5` for router weights, and
`0.03515625` for both MoE update and layer output. The summary SHA-256 is
`3e66ce8477551f10abde2155d092677edc1b23409f71da905889c5fe260589bc`.

Protocol v3 now freezes the pre-registered derived envelopes before holdout.
No seed 16–31 candidate was executed, so this is calibration evidence only—not
Phase A acceptance, full-model correctness, serving, performance, or baseline
superiority.

## MiniMax-M2.5 Phase A v3 holdout rejection

`results/20260716-minimax-m25-phase-a-holdout-v25/` executed the frozen v3
holdout from clean parent `52f1947250f3f107debba4536f9f599bd64ced7a`.
Seeds 16–19 passed the registered hard gates. Seed 20 was rejected and the
runner stopped before seeds 21–31. No threshold or fixture was changed after
the holdout began.

The failure is a real Top-8 boundary discontinuity at token 2: the native path
selected expert 68 while the independent NPU reference selected expert 42;
the other 31 route positions match. Candidate TP8 and complete native 48-head
attention select identical routes, all collectives and rank-local expert
checks pass, and no rank reports an error. A diagnostic FP32 reconstruction
places the eighth/ninth biased-score margin at only `1.7166e-5` for the
candidate post-attention tensor and `4.7684e-6` for the reference tensor. The
post-attention maximum/mean error is only `0.015625/4.82372e-5`, but the
discrete expert change amplifies final-layer maximum/mean error to
`5.10156/0.287102`.

V3 therefore remains a strict rejection, not an excuse to widen a continuous
tolerance. It establishes that TP assembly and EP execution are not the
failing mechanisms, while exact cross-runtime expert identity is unstable at
a genuine routing tie. Phase A, later layers, full-model generation, serving,
performance, and baseline superiority remain unaccepted.

## MiniMax-M2.5 post-rejection unseen-fixture diagnostic

`results/20260716-minimax-m25-phase-a-post-rejection-v26/` executes the 11
holdout fixtures that v25 intentionally did not reach after its strict stop.
This clean-parent real-online run is failure characterization only: it does
not fit a threshold, replace the rejected v3 record, or constitute a second
holdout attempt.

All 11 fixtures pass TP/full-head route identity, collective assembly, EP
dispatch/combine, rank-local expert, and error-free-rank invariants. Ten also
match the independent reference expert set. Seed 29 exposes a second Top-8
boundary discontinuity: token 1 selects expert 49 in the native path and 126
in the independent reference. Diagnostic FP32 reconstructions place the
respective eighth/ninth margins at `7.82013e-5` and `1.60217e-4`. Its layer
maximum/mean/p99.9 absolute errors are `1.08301/0.0364438/0.58648`; the other
ten fixtures have no changed expert set.

Combined with v25 seed 20, two of the 64 v3 holdout tokens change one boundary
expert across the two independent NPU implementations. This is evidence that
cross-runtime exact expert-set identity is not a robust layer-local oracle at
genuine near ties; it is not evidence that arbitrary route changes are safe.
A successor protocol must be registered before new fixtures run and must
retain final full-model greedy-token identity as the model-semantic hard gate.

## MiniMax-M2.5 row-parallel O v27 rejection

`results/20260716-minimax-m25-row-parallel-o-v27/` is the first clean-parent
real-online attempt to remove the rank-0 complete O projection. The intended
path derives one global per-token dynamic quantization scale with HCCL MAX,
computes an INT8×INT8 local INT32 accumulator on each rank, then uses INT32
HCCL SUM before one dequantization.

All eight ranks complete their local TP attention, but the installed
910B2/CANN 9.0 stack rejects the requested generic
`aclnnMatmul(INT8, INT8 -> INT32)` signature during workspace construction
with status `161002`. No partial matmul or INT32 AllReduce executes. The
candidate returns strict status 3, every device is released, and the result is
preserved rather than reported as distributed-O evidence.

The rejection narrows the implementation choice: the next candidate must use
a supported quantized-matmul output path and communicate a supported partial
representation while retaining the global activation scale. It does not
invalidate the row-sharding dataflow, but it provides no correctness or
performance evidence for that dataflow.

`results/20260716-minimax-m25-row-parallel-o-v28/` replaces the unsupported
generic Matmul signature with the checkpoint path's already validated
QuantMatmulV5, BF16 partial output, FP32 cast, and FP32 HCCL SUM. The clean
eight-card run is still rejected at workspace construction with status
`161002` on every rank. The remaining incompatibility is the TP8 local O input
width: `6144 / 8 = 768`, while this INT8 kernel requires K to be a multiple of
`4 * 128 = 512`; the original complete 6,144-wide O satisfies that constraint.
No partial output or collective executes.

V28 is preserved as a second strict operator-shape rejection. V29 will
zero-pad each 768-wide activation shard and its matching input-major weight
rows to 1,024. Padding does not change the mathematical partial dot product,
but adds 33.3% local O matmul work. This is an implementation tradeoff to be
measured later, not performance evidence.

`results/20260716-minimax-m25-row-parallel-o-v29/` verifies the zero-padding
plan in host tests and reports logical/padded K as `768/1024`, but the formal
NPU run still rejects QuantMatmulV5 workspace construction on all ranks. The
next remaining call-shape difference from the accepted complete-O projection
is the activation scale view: row-parallel manual quantization used `[4,1]`
for broadcast, whereas the accepted projection passes `[4]` to QuantMatmulV5.
V29 is preserved as rejected; v30 will use distinct `[4,1]` and `[4]` tensor
views over the same global-scale storage. No partial or collective executed.

`results/20260716-minimax-m25-row-parallel-o-v30/` crosses the operator gate.
All eight ranks execute the padded QuantMatmulV5 partial, cast it to FP32, and
complete HCCL SUM. Activation/weight padding and its CPU dot-product oracle
have zero mismatches; every rank receives a collective result identical to the
host sum of all eight local partials. There are no rank errors.

V30 is nevertheless a strict numerical rejection. The generic manual
shared-scale quantization differs from the accepted complete DynamicQuant on
five ranks, and the resulting post-attention normalization has 2,346
out-of-gate elements with maximum/mean absolute error
`3.28125/0.0839792`. This proves the distributed partial and communication
dataflow, but not O projection semantics. V31 will use the already present
attention AllGather on every rank, run the accepted full-token DynamicQuant,
and slice its INT8 output for the local padded O shard. It retains distributed
O while removing the unverified manual rounding reconstruction.

## MiniMax-M2.5 accepted row-parallel O v31

`results/20260716-minimax-m25-row-parallel-o-v31/` is the first accepted
eight-card row-parallel O component gate. Every rank consumes the existing
BF16 attention AllGather, runs the already validated complete-token
DynamicQuant over `[4,6144]`, slices its own 768-wide INT8 activation, pads
activation and input-major O weights to K=1,024, computes a BF16
QuantMatmulV5 partial, casts to FP32, and HCCL-sums all eight partials. The
candidate path does not execute a rank-0 complete O projection.

All full-quantized slice, activation/weight padding, padding-oracle, local
partial, collective reconstruction, output cast, and per-rank AddRMSNorm gates
pass with zero mismatches and no rank errors. The collective maximum absolute
difference from the host sum is `1.86265e-9`. Against the independent
post-attention oracle, there are zero out-of-gate elements; maximum/mean
absolute error is `0.03125/0.00112828`. All eight devices are free after the
run.

This proves row-parallel O component correctness on the frozen seed-0 layer-0
fixture. It is not a performance result: full-token DynamicQuant is currently
replicated on every rank, K padding adds 33.3% local O work, and audit-only
AllGather/D2H paths remain in the probe. Integration with the rejected
multi-fixture layer protocol, later layers, a persistent worker, full-model
tokens, serving, and baseline comparison remains pending.

## MiniMax-M2.5 row-parallel O complete-layer v32 rejection

`results/20260716-minimax-m25-row-parallel-o-complete-layer-v32/` connects the
accepted v31 O component to the real router, prepacked EP8 experts, combine,
weighted MoE sum, and final residual. All ranks complete without error;
full-quantized slices, padding, collective reconstruction, post-attention,
route IDs/expert sets, expert-aligned router weights, and local expert outputs
pass their existing gates. Route counts remain `[2,6,4,8,1,3,4,4]`.

The complete layer is nevertheless strictly rejected: independently rounding
eight local O partials to BF16 before FP32 AllReduce propagates to one MoE and
one final-layer element outside the frozen tolerance, with maximum error
`0.203125`. V32 does not weaken the accepted v31 component claim, but it shows
that BF16 partial materialization is insufficient for the stricter complete
layer. The next gate tests FP32 QuantMatmulV5 partial output; if the installed
operator does not support that combination, a lower-level INT32/FP32 partial
kernel is required. No threshold is changed.

## MiniMax-M2.5 row-parallel O FP32-partial v33 rejection

`results/20260716-minimax-m25-row-parallel-o-v33/` tests the specific follow-up
predicted by v32: direct FP32 local output from QuantMatmulV5, followed by FP32
HCCL reduction. The formal run starts from clean commit `827fa249` and reaches
all eight 910B2 ranks, but every rank rejects the operator signature during
`aclnnQuantMatmulV5GetWorkspaceSize` with status `161002`. No local partial or
collective is executed, so v33 is strictly rejected.

This result narrows the implementation choice: the installed CANN runtime does
not provide the tested INT8-plus-scale QuantMatmulV5 FP32-output path even
though its headers permit constructing it. The next gate needs a lower-level
supported accumulator path that retains more precision than the v32 BF16
partial. The frozen complete-layer tolerance remains unchanged.

## MiniMax-M2.5 row-parallel O INT32-accumulator v34 rejection

`results/20260716-minimax-m25-row-parallel-o-int32-v34/` tests the
mathematically exact integer route from clean commit `70c4d574`: pad each
rank-local K from 768 to 1,024, compute INT8-by-INT8 into INT32, HCCL-sum the
integer accumulators, then apply the common per-token activation scale and
per-output weight scale once. O weight offsets are all zero and the worst-case
full-width accumulator bound is `99,096,576`, so the route neither changes the
projection semantics nor risks INT32 overflow.

The installed generic `aclnnMatmul` nevertheless rejects the padded
INT8-to-INT32 signature during workspace negotiation with status `161002` on
all eight ranks. No local matmul, collective, or dequantization executes; v34
is strictly rejected. Because both QuantMatmulV5 FP32 output and generic
Matmul INT32 output are now excluded, the next implementation replaces only
the local integer matmul with a project-owned AscendC/Cube kernel while
retaining INT32 reduction and single post-collective dequantization. No
tolerance is changed.

## Project-owned AscendC INT32 kernel single-card v36 acceptance

`results/20260716-ascendc-row-parallel-int8-o-single-card-v36/` is the first
accepted real-device gate for the project-owned fixed-shape AscendC local O
kernel. From clean commit `c0c82c3`, the runner builds and loads an
`ascend910b2` fatbin whose audited and resolved shared-library SHA-256 are
identical. Its dependency trees contain no Torch, Python, Transformers, vLLM,
or unresolved library.

Four cases execute on one 910B2: two repeated deterministic inputs, a K=777
one-hot input-major layout witness, and the signed `-128 x 127` endpoint. All
49,152 INT32 outputs match the independent CPU oracle exactly; maximum error,
remaining sentinels and repeat differences are zero. The probe process and NPU
allocation are absent after completion.

This accepts only fixed-shape single-card component correctness. The recorded
`815.048 ms` covers four correctness cases, transfers, synchronization and
CPU-oracle work; it is explicitly not performance evidence. TP8 local-shard
parity, INT32 HCCL reduction, one-time dequantization, the frozen complete
layer, persistent execution and full-model tokens remain unproved.

## Project-owned AscendC TP8 row-parallel O v37 acceptance

`results/20260716-minimax-m25-row-parallel-o-ascendc-int32-v37/` is the first
accepted eight-card component gate that replaces the local O GEMM with the
project-owned AscendC kernel. The clean-commit runner resolves and hashes the
audited `ascend910b2` library, then executes one local fixed-shape kernel per
rank, exact INT32 HCCL SUM, and one post-collective dequantization.

All eight preparation, launch and synchronization status arrays contain only
zero. Quantized slicing, K padding, every local accumulator, the collective
accumulator, dequantization, O output and post-attention gates pass with zero
out-of-gate elements. The independent post-attention maximum absolute error is
`0.03125`; all rank errors are empty, no probe PID remains and all eight NPUs
are released.

V37 is fixed seed-0/layer-0 component correctness only. It is not a timing
result, does not make the scalar AIV kernel a high-performance implementation,
and does not supersede the v32 complete-layer rejection. The next frozen gate
must connect this O path to router, EP8 MoE and residual without changing v32
tolerances.

## Project-owned AscendC complete MiniMax layer v38 acceptance

`results/20260716-minimax-m25-row-parallel-o-complete-layer-v38/` connects the
accepted v37 TP8 O path to the frozen seed-0 router, prepacked EP8 MoE and
residual contract. The formal run starts from clean commit `248c0be`, loads the
same audited `ascend910b2` kernel with SHA-256
`338c0248b72a2aa59668844581b5d762430ded6c3cb58b29a876cd9fc31c9c22`, and
executes neither Torch, Transformers nor vLLM.

All eight preparation, launch and synchronization statuses are zero. The
frozen route counts remain `[2,6,4,8,1,3,4,4]`; router IDs, expert sets,
router weights, expert-local outputs, NPU MoE aggregation and residual gates
all report zero out-of-gate elements. The independent MoE and final-layer
oracles also report zero out-of-gate elements, with maximum absolute errors
`0.125` and `0.09375`. No v32 numerical tolerance was changed. All rank error
strings are empty, no probe PID remains, and all eight NPUs are released.

V38 therefore supersedes the v32 rejection only for this exact AscendC
accumulator route and frozen fixture. It proves fixed seed-0/layer-0 complete
layer correctness, not multi-fixture stability, later layers, persistent
62-layer execution, full-token correctness, serving, latency, throughput or a
baseline advantage. The current scalar AIV kernel remains a correctness
bootstrap and is not performance evidence.

## Qwen2.5-14B native exact-hot matrix v1

`results/qwen14b-native-exact-hot-v1-suite.json` records a clean-commit
native-only exact-hot matrix from commit `42a0ac6`. The native candidate uses
the Qwen2.5-14B BF16 C++/ACL resident executor, the frozen 2,177-token v3
prompt, and independent greedy oracle manifests for output lengths 1, 32 and
128. Each cell has three independent service lifecycles, 128 measured
requests per lifecycle, shape-matched warmup cohorts, raw request records,
HBM samples, process snapshots and run metadata.

All 36 lifecycle runs report `all_outputs_exact=true`, `hit_rate=1`, and
2,177 reused tokens per measured request, for 278,656 effective reused tokens
per 128-request lifecycle; no `FAILED` marker is present. The suite is
real-online native exact-state evidence only. It is not an independent/cold or
shared-prefix control, and it does not make TTFT speedup claims because native
and vLLM TTFT semantics remain different. The checked-in audit gate
`benchmarks/audit_qwen14b_exact_hot_matrix.py` validates the tracked native
suite, vLLM suite, derived comparison, raw request records, clean provenance,
stderr captures and native exit codes.

| concurrency | output | lifecycles | request/s mean | output token/s mean | wall P95 ms mean | TPOT P50 ms mean |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 1 | 3 | 803.19 | 803.19 | 1.25 | n/a |
| 1 | 32 | 3 | 0.95 | 30.29 | 1069.50 | 33.96 |
| 1 | 128 | 3 | 0.25 | 32.11 | 4023.07 | 31.35 |
| 4 | 1 | 3 | 1469.41 | 1469.41 | 3.59 | n/a |
| 4 | 32 | 3 | 2.84 | 90.78 | 1441.93 | 45.26 |
| 4 | 128 | 3 | 0.88 | 113.02 | 4574.56 | 35.61 |
| 16 | 1 | 3 | 1458.39 | 1458.39 | 14.35 | n/a |
| 16 | 32 | 3 | 5.70 | 182.26 | 2854.80 | 90.20 |
| 16 | 128 | 3 | 2.43 | 310.83 | 6658.55 | 51.83 |
| 32 | 1 | 3 | 1345.80 | 1345.80 | 22.88 | n/a |
| 32 | 32 | 3 | 6.90 | 220.93 | 4814.19 | 148.45 |
| 32 | 128 | 3 | 3.47 | 444.38 | 9486.61 | 72.51 |

## Qwen2.5-14B vLLM exact-hot baseline matrix v1

`results/qwen14b-vllm-exact-hot-v1-suite.json` records the matched
vLLM-HUST + vLLM-Ascend-HUST exact-hot baseline from clean commit `de145c3`.
It uses the same Qwen2.5-14B BF16 checkpoint, the same frozen 2,177-token v3
prompt token IDs, greedy decoding, fixed output lengths, one physical Ascend
910B2, and the same independent oracle manifests as the native matrix. Each
cell has three independent service lifecycles and 128 measured requests per
lifecycle. The vLLM launcher uses batch-invariant `PIECEWISE` execution and a
unique recorded compilation cache per lifecycle.

All 36 lifecycle runs report exact output-token parity with the frozen oracle,
zero failed measured requests, complete raw request records and clean parent
provenance. vLLM TTFT is measured from its SSE stream and remains marked
`ttft_cross_runtime_comparable=false`; no native-vs-vLLM TTFT acceleration
claim is made.

| concurrency | output | lifecycles | request/s mean | output token/s mean | wall P95 ms mean | TPOT P50 ms mean |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 1 | 3 | 21.37 | 21.37 | 48.43 | n/a |
| 1 | 32 | 3 | 0.92 | 29.43 | 1118.96 | 32.36 |
| 1 | 128 | 3 | 0.22 | 28.59 | 4744.47 | 34.35 |
| 4 | 1 | 3 | 43.34 | 43.34 | 95.42 | n/a |
| 4 | 32 | 3 | 3.34 | 106.92 | 1238.65 | 34.63 |
| 4 | 128 | 3 | 0.85 | 109.33 | 4899.52 | 35.75 |
| 16 | 1 | 3 | 92.03 | 92.03 | 197.46 | n/a |
| 16 | 32 | 3 | 11.73 | 375.26 | 1406.64 | 39.06 |
| 16 | 128 | 3 | 3.11 | 397.93 | 5236.65 | 39.19 |
| 32 | 1 | 3 | 147.39 | 147.39 | 252.69 | n/a |
| 32 | 32 | 3 | 20.50 | 656.15 | 1612.26 | 43.87 |
| 32 | 128 | 3 | 5.48 | 701.09 | 5901.81 | 44.45 |

`results/qwen14b-native-vs-vllm-exact-hot-v1-comparison.json` is a
derived-artifact comparison for this exact-hot retained-state workload only.
It shows that the native state-centric path is much faster for one-token
retained-state requests and remains close at low-concurrency long decode, while
the vLLM baseline has higher sustained decode throughput for high-concurrency
32/128-token outputs. This is not a general serving-performance conclusion:
independent/cold and shared-prefix control groups are still required before
separating state reuse benefit from ordinary inference throughput.

| concurrency | output | native/vLLM request/s | native/vLLM output token/s | vLLM/native wall P95 |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 1 | 37.58x | 37.58x | 38.76x |
| 1 | 32 | 1.03x | 1.03x | 1.05x |
| 1 | 128 | 1.12x | 1.12x | 1.18x |
| 4 | 1 | 33.90x | 33.90x | 26.54x |
| 4 | 32 | 0.85x | 0.85x | 0.86x |
| 4 | 128 | 1.03x | 1.03x | 1.07x |
| 16 | 1 | 15.85x | 15.85x | 13.76x |
| 16 | 32 | 0.49x | 0.49x | 0.49x |
| 16 | 128 | 0.78x | 0.78x | 0.79x |
| 32 | 1 | 9.13x | 9.13x | 11.04x |
| 32 | 32 | 0.34x | 0.34x | 0.33x |
| 32 | 128 | 0.63x | 0.63x | 0.62x |

## Qwen2.5-14B native cold-prefill dispatch milestone

`results/qwen14b-native-independent-cold-dispatch-v10-c16-o128-suite.json`
records three clean-parent native C++/ACL lifecycles for the frozen
independent/cold `c=16,o=128` token-parity workload. The scheduler plan uses a
25 ms admission window, eight-request long-prefill microbatches, a 17,648-token
compute budget and a 4 GiB new-KV budget. Cold admission now charges all 2,206
uncached prompt tokens plus 128 requested output tokens per request. These
parameters are bound by scheduler-plan identity v2; the resulting state
compatibility digest is
`e54ff5cdcf2984c39c08c834342a98cecfe11e9ff186fa4f7347b5356b93b387`,
so states created under the previous execution plan cannot be reused.

All three lifecycles produce 128/128 exact oracle outputs, recycle every
temporary state, report zero cancellations, exit with status zero and leave no
candidate process or NPU 0 allocation. Each run records exactly 16 prefill
batches with eight requests per batch and 1,016 decode batches. Median
throughput is 1.656 request/s and 211.943 output token/s; median wall P95 is
9,773.28 ms, TPOT P50 is 48.91 ms, and peak HBM is 54,857 MiB.

Against the earlier single-prefill native suite, request throughput improves
3.74% (1.656 versus 1.596 request/s). Against the frozen token-parity vLLM
baseline, native remains 3.27% lower in request/output throughput (1.656 versus
1.712 request/s), so the dominance gate is not met. Native has 11.33% lower
wall P95, 24.58% lower TPOT P50 and uses 4,850 MiB less peak HBM for this cell.
TTFT is not compared because the runtimes retain different measurement
semantics. This result closes only the long-prefill batching milestone; it does
not justify c32 expansion or a general serving-performance claim.

## Qwen2.5-14B native prefill-position-cache milestone

`results/qwen14b-native-independent-cold-dispatch-v11-c16-o128-suite.json`
records three clean-parent native C++/ACL lifecycles for the same frozen
independent/cold `c=16,o=128` token-parity workload after adding a bounded host
prefill-position cache. The cache computes one sequence-row BF16 RoPE table,
duplicates the exact bytes across batch rows, and reuses the causal mask for an
unchanged execution shape. Device tensor shapes and H2D contents are unchanged.
The resident execution plan now explicitly binds `executor_plan_revision=2`;
the resulting state compatibility digest is
`36546c41f14dec0cd3a66bfc75f5794336b0fb2e54e6c52aa3cf346d67e189c5`,
which differs from v10 and strictly invalidates states created under the older
execution plan.

All three lifecycles produce 128/128 exact oracle outputs, record exactly 16
eight-request prefill batches, recycle every temporary state, exit with status
zero and empty stderr, and leave no candidate process or NPU 0 allocation. The
three request-throughput values are 1.7142, 1.7126 and 1.7001 request/s. Median
throughput is 1.7126 request/s and 219.212 output token/s; median wall P95 is
9,432.90 ms, TPOT P50 is 48.11 ms, and peak HBM is 54,857 MiB. Median measured
prefill execution falls from 36,511.97 ms in v10 to 34,166.00 ms in v11, a
6.43% reduction. End-to-end request throughput improves 3.43% over v10.

Against the frozen token-parity vLLM baseline, the native median point estimate
is only 0.043% higher (1.7126 versus 1.7119 request/s). This technically passes
a strict median point-estimate comparison, but the margin is too small to claim
stable or statistically robust throughput superiority, and the third native
lifecycle is below the vLLM median. Native has 14.42% lower wall P95, 25.80%
lower TPOT P50, and uses 4,850 MiB less peak HBM for this cell. TTFT remains
incomparable across the two runtimes. This milestone establishes throughput
parity plus a latency and memory advantage; the next milestone must widen the
throughput margin or characterize its variance before c32 expansion.

## Qwen2.5-14B native batch-end c16/o128 formal milestone

`results/qwen14b-native-independent-cold-batch-sync-v18-c16-o128-suite.json`
records three independent clean-parent, real-online native C++/ACL lifecycles
for the frozen independent/cold `c=16,o=128` token-parity workload. Every
lifecycle serves 128 measured 2,206-token requests, produces 128/128 exact outputs against
the frozen independent greedy oracle, uses 16 eight-request prefill batches,
recycles all temporary states, records client status zero and empty client stderr,
and leaves no candidate process or NPU 0 allocation. The three request rates
are 1.74556, 1.73422 and 1.74013 request/s.

This execution uses configuration schema 2, `decode_sync_policy=batch_end`,
executor-plan revision 6 and a 5 GiB non-overlapping workspace. The complete
execution-config SHA-256 is
`883d7eec99ec06911efd204711ed243204f843c5240ca544179b4cddb8ff93cc`;
the resulting state-compatibility digest is
`946dfc700b6e21ebd2ae6ee90ba39a49a7b363184a621b9dd2450fc7c32ac668`.
These identities bind the execution policy and physical state contract, so
states from earlier revisions are not reusable.

The native median is 1.74013 request/s and 222.736 output token/s. Against the
frozen same-token vLLM median of 1.71186 request/s and 219.118 output token/s,
the derived comparison reports a 1.6514% throughput advantage and therefore
passes the predeclared 1.5% admission threshold. Native median wall P50/P95/P99
is 9,183.16/9,294.46/9,300.26 ms, 0.97%/15.68%/26.19% below vLLM; native TPOT
P50/P95/P99 is 46.80/55.27/55.29 ms, 27.82%/18.26%/18.80% below vLLM. Native
peak HBM is 59,466 MiB, 241 MiB below the maximum of the three vLLM lifecycles.

This is a narrowly admitted result for one independent/cold cell, with only
0.151 percentage points of headroom over the engineering threshold. It is not
a full-matrix or general serving-performance claim. Native and vLLM TTFT remain
explicitly incomparable and no TTFT acceleration is claimed. The strict formal
runner itself returned zero and generated the suite only after all three
lifecycle launchers completed; the lifecycle directories preserve client exit
codes but do not contain separate launcher-exit-code files.

## Qwen2.5-14B production append c1/o32 milestone

`results/qwen14b-native-append-v1-c1-o32-suite.json` aggregates three
independent real-online native C++/ACL lifecycles from clean commit `ec8db8f`.
Every lifecycle serves 128 requests with the frozen 2177-token input split into
a 2048-token live source state and a 129-token append. All 384 outputs exactly
match the independent 32-token greedy oracle, hit rate is 1, each lifecycle
records 262,144 effectively reused tokens, temporary branches are recycled,
launcher exit is zero, stderr is empty, and no candidate process or NPU 7
allocation remains after shutdown.

The three native request rates are 0.999112, 0.996394, and 0.990681 request/s.
Median native performance is 0.996394 request/s and 31.884608 output token/s,
with wall P50/P95/P99 of 999.52/1024.31/1046.18 ms, TPOT P50/P95/P99 of
29.52/30.08/30.19 ms, and peak HBM of 50,655 MiB. The execution identity binds
the schema-v3 append plan, weights, RoPE semantics, state schema, physical KV
layout, and 5 GiB workspace; all three lifecycle identities are identical.

Against the frozen same-token vLLM shared-prefix c1/o32 suite, native median
request and output-token throughput are 11.00% higher. Native wall
P50/P95/P99 are 9.48%/13.93%/15.52% lower, TPOT P50/P95/P99 are
10.56%/15.42%/18.44% lower, and peak HBM is 2,812 MiB lower. Both sides use
Qwen2.5-14B BF16, fixed 32-token greedy generation, 128 measured requests per
lifecycle, three clean service lifecycles, identical prompt token IDs, and the
same physical Ascend 910B2 specification. This admits only the production
append `c=1,o=32` milestone; it is not a full-matrix or ordinary-serving claim.
TTFT remains cross-runtime incomparable and no TTFT speedup is claimed.

### Production append c1/o1 diagnostic boundary

The clean-parent diagnostic
`.benchmarks/qwen14b-native-append-production-c1-o1-smoke-r01` served 128
requests with 128/128 exact `[51741]` outputs, complete branch recycling, zero
launcher/client exits, empty stderr, and no host/container/NPU7 residue. With
the historical 10 ms scheduler window it reached 11.934 request/s and wall P50
82.13 ms. The zero-window A/B in `...-r02-bw0` remained exact and clean and
improved to 14.577 request/s with wall P50 67.98 ms; non-executor P50 fell from
13.75 to 2.00 ms. B1 cannot form a larger physical batch, so production append
formal runs now require a zero scheduler window. Scheduler-plan identity binds
the change and invalidates states from the older online plan.

Two further dirty diagnostics were rejected. Device-side FP32 cast plus ArgMax
reduced throughput to 14.148 request/s and was removed. Deferring all 48 layer
synchronizations overflowed 5 GiB and 6 GiB workspaces; a 10 GiB run was exact
but reached only 14.988 request/s while increasing peak HBM from 50,655 to
55,776 MiB, so that implementation and executor revision were also removed.
All failed and rejected runs preserved nonzero exits where applicable and
showed zero candidate-process and NPU7 residue.

This c1/o1 performance point is not compared as a formal paired result against
the frozen exact-repeat vLLM shared-prefix suite. Native explicitly reuses
2,048 tokens and computes a 129-token suffix. Repeated identical vLLM prompts
can reuse 17 complete 128-token blocks, or 2,176 tokens, and compute only the
one-token tail. The existing vLLM 20.842 request/s point is therefore a useful
upper-bound diagnostic but not an equal-reuse append control. The c1/o1
correctness gate passes; the performance milestone remains unadmitted until a
frozen prompt/oracle family with one common 2,048-token prefix and distinct
129-token suffixes is measured on both runtimes. TTFT remains incomparable.

## Qwen2.5-14B equal-reuse c1/o1 formal milestone

`results/qwen14b-equal-reuse-v3-c1-o1-suite.json` admits the previously missing
equal-reuse comparison from clean commit `8166493`. Both runtimes serve the
same 128 measured 2,177-token rows: every row has one frozen common 2,048-token
prefix and a distinct 129-token suffix, so each side may reuse exactly 2,048
tokens per request. Outputs are fixed to one greedy token and are checked
against the frozen independent oracle. The prompt-family SHA-256 is
`944c51b10cd76e671fdf32d5108776cedc1b2f16900f44ff56651fc4e54731fe`;
the oracle SHA-256 is
`7439e2af8af9eb17b421d5b1e2ebcaa60ed2fc12960907cf85cd6407135097a3`.

The three native C++/ACL lifecycle rates are 14.75843, 14.00968 and 12.69867
request/s; the three vLLM-HUST/vLLM-Ascend-HUST baseline rates are 9.80412,
9.76997 and 9.71630 request/s. Median throughput is therefore 14.00968 versus
9.76997 request/s, a 43.40% native advantage. Median-lifecycle wall
P50/P95/P99 is 69.97/84.39/91.29 ms for native and
100.75/104.62/106.34 ms for vLLM, or 30.55%/19.34%/14.15% lower for native.
Maximum peak HBM is 50,668 MiB for native and 53,466 MiB for vLLM.

All 384 native measured outputs are exact, with zero errors, hit rate 1,
262,144 effectively reused tokens per lifecycle, complete temporary-state
recycling, and identical weight/RoPE/state-schema/physical-KV/execution-plan
identity across runs. All six lifecycles come from the same clean parent and
physical NPU 0, retain raw requests, and pass scoped process, port, NPU and
credential scans. Full-host process tables and process argv are forbidden from
admitted provenance. Because output length is one, TPOT is not reported; native
and vLLM TTFT remain incomparable and no TTFT speedup is claimed. This result
admits only the equal-reuse `c=1,o=1` stateful workload. It does not establish
ordinary independent/cold performance or justify automatic expansion to c4.

## Qwen2.5-14B equal-reuse c1/o32 formal milestone

`results/qwen14b-equal-reuse-o32-v1-c1-o32-suite.json` admits the next
equal-reuse cell from clean commit `59e5955`. It reuses the same frozen
128-row prompt family as c1/o1: every 2,177-token row shares exactly the first
2,048 tokens and has a distinct 129-token suffix. Both runtimes generate a
fixed 32-token greedy continuation from identical token IDs. The independent
Torch-NPU eager BF16 oracle is schema v2 and binds its exporter SHA, clean
parent, container image, model identity, prompt-family SHA and all 130
measured/warmup output hashes. Its SHA-256 is
`714fd3073baa6e4c66d2c3ea1147b898d5b18e8c84242cef605490d5f3323a94`.

The three native C++/ACL lifecycle rates are 1.01620, 1.02388 and 1.02355
request/s; the three vLLM-HUST/vLLM-Ascend-HUST baseline rates are 0.84821,
0.86561 and 0.84250 request/s. Median request throughput is 1.02355 versus
0.84821 request/s and median output throughput is 32.75347 versus 27.14280
token/s, a 20.67% native advantage. Median-lifecycle wall P50/P95/P99 is
975.82/983.64/987.02 ms for native and 1,169.45/1,244.68/1,312.06 ms for
vLLM, or 16.56%/20.97%/24.77% lower for native. TPOT P50/P95/P99 is
29.22/29.48/29.62 ms for native and 33.36/35.68/37.46 ms for vLLM, or
12.40%/17.38%/20.94% lower. Maximum peak HBM is 50,667 MiB for native and
53,467 MiB for vLLM.

All 384 native requests match every one of the 32 independent oracle tokens,
with zero errors, hit rate 1, exactly 2,048 reused tokens per request and full
temporary-state recycling. The auditor recomputes all oracle output hashes and
the family output root, requires positive TPOT for long-output cells, and
verifies all six raw request sets, state/runtime identities and scoped cleanup
evidence. A first vLLM diagnostic attempt was rejected before measurement
because recently released oracle HBM left less free memory than the fixed 0.8
capacity required; its failure provenance remains diagnostic-only. No formal
capacity parameter was changed. This result admits only equal-reuse
`c=1,o=32`; it does not establish c4/o128 or ordinary independent/cold
performance. TTFT remains cross-runtime incomparable and no TTFT speedup is
claimed.

## Qwen2.5-14B equal-reuse revision-8 c16/o32 formal milestone

`results/qwen14b-equal-reuse-rev8-c16-o32-v1-suite.json` admits the B16
32-token cell from clean commit `e4d436c`. The runner interleaves three native
C++/ACL and three vLLM-HUST/vLLM-Ascend-HUST service lifecycles as
N1/V1/N2/V2/N3/V3 on physical NPU0. Both runtimes consume the same 128-row,
2,177-token family, reuse the common 2,048-token prefix, and generate exactly
32 greedy tokens against the frozen schema-v2 oracle with SHA-256
`f83312ed1a422ca3f259ac299bfe40709f6a409f801a80130005974eb562ca09`.

Native lifecycle throughput is 10.596448/10.452038/10.584210 request/s; vLLM
is 9.833254/9.953551/9.992763 request/s. Median request throughput is
10.584210 versus 9.953551 request/s and median output throughput is 338.694723
versus 318.513632 token/s, a 6.34% native advantage. Median wall
P50/P95/P99 is 1,504.59/1,569.90/1,576.03 ms for native and
1,596.11/1,648.57/1,655.11 ms for vLLM. TPOT P50/P95/P99 is
37.94/38.22/38.24 ms and 37.19/44.19/44.79 ms respectively: native P50 is
2.02% higher while P95/P99 are 13.52%/14.63% lower. Peak HBM is 50,667 MiB
for native and 53,467 MiB for vLLM.

All 384 requests per runtime, 768 requests total, match every frozen oracle
token. Each native lifecycle records eight B16 append batches, 248 B16 decode
batches, 256 total batches, 4,096 completed items, the required
`{16:8}`/`{2064:8}`/`{16:248}` histograms, and the exact 4-append/124-decode
bounded tail over 64 request IDs. The execution, scheduler, weights, RoPE,
schema, physical KV layout and state-compatibility identities match the
admitted c16/o1 profile. All launcher/client exits, stderr, scoped port/process
and NPU0 cleanup checks pass. A second strict aggregation is byte-identical;
the suite SHA-256 is
`06474aa67205d0f2644791a38dfc93b85f9d090b72041f62b57a8ce8c6b418dd`.
All three vLLM server logs retain the known post-request scoped-shutdown
EngineCore transport race; it occurs after all outputs complete, while client
and launcher exits, failed-request counts, ports and residue gates pass.
This result admits only equal-reuse `c=16,o=32`; c16/o128, c32 and pooled COW
remain closed. Native and vLLM TTFT are not compared.

## Qwen2.5-14B equal-reuse revision-8 c16/o1 formal milestone

`results/qwen14b-equal-reuse-rev8-c16-o1-v1-suite.json` admits the physical
B16 one-token cell from clean commit `2fb3018`. Both runtimes use the same
Qwen2.5-14B BF16 model, 128 frozen 2,177-token rows, exactly 2,048 reusable
prefix tokens, distinct 129-token suffixes, greedy fixed-length output, the
schema-v2 independent oracle with SHA-256
`71807a4136d40556a297bc47ed105c3c2e8a30a1726ce2c69a163c73d198a732`,
and physical NPU0.

Native lifecycle throughput is 47.3076/46.6302/47.5202 request/s; vLLM is
41.9910/29.2042/42.2839 request/s. The preregistered medians are
47.3076/41.9910 request/s and output token/s, so native is 12.66% higher on the
declared metric. Median-lifecycle wall P50/P95/P99 is
329.57/395.33/398.88 ms for native and 367.14/432.69/440.36 ms for vLLM.
Output length one has no TPOT. Peak HBM is 50,667 versus 53,465 MiB. The vLLM
r2 slow point is retained; this result does not claim low variance.

All 384 requests per runtime emit oracle token `51741` exactly. Each native
lifecycle records eight B16 append batches, 128 append requests, 16,512 append
rows, histograms `{16:8}` and `{2064:8}`, zero decode batches, hit rate 1 and
262,144 effective reused tokens. All six client and launcher exits are zero,
stderr and scoped residue are empty, and NPU0 is released after every run.
Independent verification covers 768 raw requests and 768 output tokens; a
second aggregation is byte-identical. Suite SHA-256 is
`8d795e28010d6911d6523fb40dac161ddb96efce4fbfa427fe3c3cd49a49decb`.
The vLLM server logs retain the known post-request EngineCore transport race
during scoped shutdown. It occurs after all 128 responses are validated in
each lifecycle; launcher/client status, port release and residue checks pass.

Native state compatibility remains exact across the three runs:
execution-config `90f2ff93...3a06e57`, compiled plan
`7bfbd67b...64753`, scheduler plan `c22eab01...f7884`, and final state
compatibility `170d04b2...72b4df`. This admits only equal-reuse `c=16,o=1`;
c16 long output, c32, pooled-block COW, broad serving superiority and TTFT
speedup remain unproven.

## Qwen2.5-14B equal-reuse revision-8 c4/o1 formal milestone

`results/qwen14b-equal-reuse-rev8-c4-o1-v3-suite.json` admits the first
fixed-row B4 append cell from clean commit `9674a2e`. Both runtimes consume the
same frozen 128-row, 2,177-token family, reuse only the common 2,048-token
prefix, and generate exactly one greedy token. The schema-v2 independent oracle
contains both warmups and all measured rows; its SHA-256 is
`71807a4136d40556a297bc47ed105c3c2e8a30a1726ce2c69a163c73d198a732`.

Native lifecycle throughput is 33.31991, 33.90263 and 33.75012 request/s;
vLLM-HUST/vLLM-Ascend-HUST baseline throughput is 19.60171, 19.98204 and
20.02518 request/s. Median throughput is therefore 33.75012 versus 19.98204
request/s, a 68.90% native advantage. Median-lifecycle wall P50/P95/P99 is
116.07/119.60/191.99 ms for native and 197.82/204.91/212.09 ms for vLLM,
41.33%/41.63%/9.48% lower for native. Maximum peak HBM is 50,667 MiB for
native and 53,465 MiB for vLLM, a 2,798 MiB reduction.

All 384 outputs on each runtime match the same independent oracle. Every native
lifecycle reports hit rate 1, exactly 262,144 effective reused tokens, complete
temporary-branch recycling, and 32 worker-completed B4 append batches covering
128 requests and 16,512 suffix rows. All six runs use physical NPU0, share one
clean parent, retain raw request records, preserve start/end result-tree and Git
provenance, and leave scoped processes, port and NPU0 empty. vLLM additionally
records internal API-server shutdown and EngineCore resource teardown before
the bounded fallback cleanup. Because output length is one, TPOT is null. TTFT
remains cross-runtime incomparable and no TTFT claim is made. This result admits
only equal-reuse `c=4,o=1`; it does not justify c16/c32, longer c4 output, COW,
or a broad ordinary-serving claim.

## Qwen2.5-14B equal-reuse revision-8 c4/o32 formal milestone

`results/qwen14b-equal-reuse-rev8-c4-o32-v1-suite.json` admits the fixed-row
B4 long-output cell from clean commit `ebf8aa1`. Both runtimes consume the same
128-row, 2,177-token suffix family, reuse only the common 2,048-token prefix,
and generate exactly 32 greedy tokens. The schema-v2 independent oracle binds
the clean producer, exporter blob, container identity, model index, all eight
weight shards and tokenizer root; its SHA-256 is
`f83312ed1a422ca3f259ac299bfe40709f6a409f801a80130005974eb562ca09`.

Native lifecycle throughput is 3.71005, 3.70914 and 3.71171 request/s;
vLLM-HUST/vLLM-Ascend-HUST baseline throughput is 2.99820, 3.01348 and
3.02893 request/s. Median request throughput is therefore 3.71005 versus
3.01348 request/s and median output throughput is 118.72151 versus 96.43127
token/s, a 23.12% native advantage. Median-lifecycle wall P50/P95/P99 is
1075.91/1078.82/1149.66 ms for native and 1323.94/1344.73/1364.26 ms for
vLLM, or 18.73%/19.77%/15.73% lower for native. TPOT P50/P95/P99 is
30.95/31.04/31.08 ms for native and 35.03/36.34/36.80 ms for vLLM, or
11.66%/14.59%/15.54% lower. Maximum peak HBM is 50,667 MiB for native and
53,467 MiB for vLLM, a 2,800 MiB reduction.

All 384 requests on each runtime match every one of the 32 independent oracle
tokens. Every native lifecycle reports zero errors, hit rate 1, exactly 262,144
effective reused tokens, full temporary-branch recycling, 32 worker-completed
B4 append batches and 992 worker-completed B4 decode batches. Its bounded plan
tail contains the expected four complete cohorts, or 4 append and 124 decode
plans. All six lifecycles use physical NPU0 and one clean parent, retain raw
requests, preserve Git/results-tree/container identities, and leave scoped
processes, port and NPU0 empty. The paired suite is byte-identical under a
second aggregation and has SHA-256
`a97986fc6d9822e73840d5e9365764050836e787a8fdde10dbb347e1d44fa811`.
This result admits only equal-reuse `c=4,o=32`; it does not justify c4/o128,
c16/c32, pooled-block COW or a broad ordinary-serving claim. TTFT remains
cross-runtime incomparable and no TTFT speedup is claimed.

## Qwen2.5-14B equal-reuse revision-8 c4/o128 formal milestone

`results/qwen14b-equal-reuse-rev8-c4-o128-v1-suite.json` admits the fixed-row
B4 128-token cell from clean commit `daf5e05`. Both runtimes consume the same
128-row, 2,177-token suffix family, reuse only the common 2,048-token prefix,
and generate exactly 128 greedy tokens. The schema-v2 independent oracle has
SHA-256 `7b35be08ae08dbdec5d898be9d72a325bcfb1a824991d39713523f62fe8e9fb8`
and binds the clean producer, exporter blob, immutable container, tokenizer and
all eight model shards.

Native lifecycle throughput is 0.989276/0.985482/0.989141 request/s; vLLM is
0.842956/0.807483/0.778033 request/s. Median native/vLLM throughput is
0.989141/0.807483 request/s and 126.610000/103.357883 output token/s, so native
is 22.50% higher on the declared admission metric. Median-lifecycle wall
P50/P95/P99 is 4041.13/4049.86/4133.15 ms for native and
4943.26/5221.71/5250.52 ms for vLLM. TPOT P50/P95/P99 is
30.89/30.96/31.11 ms and 36.92/39.14/39.35 ms respectively. Peak HBM is
50,667 MiB for native and 53,467 MiB for vLLM.

All 384 requests per runtime match the independent oracle for all 128 output
tokens. Each native lifecycle records 32 worker-completed B4 append batches,
4,064 B4 decode batches, 4,096 total batches, 16,384 completed items, 262,144
effective reused tokens and the exact one-append/127-decode bounded plan tail.
All six lifecycles use physical NPU0 and one clean parent, preserve raw request,
Git/results-tree/container and teardown provenance, and leave the scoped port,
candidate processes and NPU0 empty. Independent verification covers 768 raw
requests and 98,304 output tokens. A second aggregation is byte-identical; the
suite SHA-256 is
`c380557b42f0cef302a50c30bae69f6e9757f11d399aa8ac2565d9191b644e38`.
This result admits only equal-reuse `c=4,o=128`; it does not justify c16/c32,
pooled-block COW or a broad ordinary-serving claim. TTFT remains cross-runtime
incomparable and no TTFT speedup is claimed.

## Qwen2.5-14B equal-reuse c1/o128 formal milestone

`results/qwen14b-equal-reuse-o128-v1-c1-o128-suite.json` admits the third c1
equal-reuse cell from clean commit `bf8309c`. Both runtimes consume the frozen
128-row, 2,177-token suffix family with exactly 2,048 common-prefix tokens and
one distinct 129-token suffix per row, then generate exactly 128 greedy tokens.
The schema-v2 independent Torch-NPU eager BF16 oracle contains 130 measured and
warmup rows, binds the exporter, clean parent, container image, model and prompt
family, and has SHA-256
`b1f6094a50ea4cf0be46abbc46b312c26d69946c7a8d04de8099e44eeabe7be5`.

The three native C++/ACL lifecycle rates are 0.26463, 0.26409 and 0.26514
request/s; the three vLLM-HUST/vLLM-Ascend-HUST baseline rates are 0.21517,
0.21927 and 0.21532 request/s. Median request throughput is 0.26463 versus
0.21532 request/s and median output throughput is 33.87325 versus 27.56068
token/s, a 22.90% native advantage. Median-lifecycle wall P50/P95/P99 is
3,775.06/3,809.59/3,851.60 ms for native and
4,539.44/4,846.22/5,007.60 ms for vLLM. TPOT P50/P95/P99 is
29.17/29.41/29.68 ms for native and 34.65/37.04/38.34 ms for vLLM. Maximum
peak HBM is 50,667 MiB for native and 53,467 MiB for vLLM.

All 384 native requests match all 128 independent oracle tokens, with zero
errors, hit rate 1, exactly 2,048 reused tokens per request and complete
temporary-state recycling. The paired auditor also checks every vLLM output
against the same oracle, recomputes every oracle row hash and family root, and
rejects capacity drift. All six lifecycles use physical NPU0 and the same clean
parent. Native is pinned to scheduler batch 1, zero batch window, state
capacity 17, max decode batch 16, max prefill rows 2,304 and a 5 GiB workspace;
vLLM retains max model length 4,096, max sequences 64 and memory utilization
0.8. Scoped cleanup and credential scans pass, and a second aggregation is
byte-identical to the admitted suite. This result admits only equal-reuse
`c=1,o=128`; it does not establish c4/COW or ordinary independent/cold
performance. TTFT remains cross-runtime incomparable and no TTFT speedup is
claimed.

## Qwen2.5-14B equal-reuse revision-8 c16/o128 formal milestone

`results/qwen14b-equal-reuse-rev8-c16-o128-v1-suite.json` admits the physical
B16 128-token cell from clean commit `56a0e29`. Both runtimes use the same
Qwen2.5-14B BF16 model, 128 frozen 2,177-token rows, exactly 2,048 reusable
prefix tokens, distinct 129-token suffixes, greedy fixed-length output, the
schema-v2 independent oracle with SHA-256
`7b35be08ae08dbdec5d898be9d72a325bcfb1a824991d39713523f62fe8e9fb8`,
and physical NPU0.

Native lifecycle throughput is 3.079362/3.098560/3.064707 request/s; vLLM is
2.849336/2.963693/2.970951 request/s. The preregistered medians are
3.079362/2.963693 request/s and 394.158301/379.352732 output token/s, so native
is 3.90% higher on the declared metric. Median-lifecycle wall P50/P95/P99 is
5,188.15/5,276.92/5,279.44 ms for native and
5,354.60/5,532.43/5,544.12 ms for vLLM. TPOT P50/P95/P99 is
38.28/38.47/38.48 ms versus 38.74/40.45/41.10 ms. Peak HBM is 50,667 versus
53,467 MiB.

All 384 requests per runtime match all 128 independent oracle tokens. Every
native lifecycle records eight B16 append batches, 1,016 B16 decode batches,
1,024 total batches, 16,384 completed items, hit rate 1, 262,144 effective
reused tokens, complete temporary-branch recycling, and the exact
one-append/127-decode bounded plan tail. The execution, scheduler, weight,
RoPE, state-schema and physical-KV identities match the admitted c16/o1 and
c16/o32 profiles.

All six lifecycles share one clean parent and frozen tree, use physical NPU0,
retain raw request and process identities, exit with zero launcher/client
status, and leave client stderr, scoped ports, candidate processes and NPU0
empty. vLLM r1/r2 retain the known EngineDeadError only after shutdown begins
and request processing is complete; r3 retains only the resource-tracker
warning. Independent verification covers 768 raw requests and 98,304 output
tokens. A second aggregation is byte-identical; the suite SHA-256 is
`ec3ace3e6c61b6cd779c2ce70bcec7a8d76103aa1b85fd12c689e20661da3ae6`.
This result admits only equal-reuse `c=16,o=128`; c32, pooled-block COW and
broad ordinary-serving superiority remain unproven. TTFT remains
cross-runtime incomparable and no TTFT speedup is claimed.

## Qwen2.5-14B equal-reuse c32/o1 physical-B16 diagnostic

The clean-parent diagnostic pair under `.benchmarks/` uses the same frozen
2,048/129 prompt family, schema-v2 o1 oracle, Qwen2.5-14B BF16 model, and
physical NPU0. Client concurrency is 32 on both runtimes. Native deliberately
retains the admitted c16 physical plan (`17/16/2304`, 5 GiB workspace), so this
is c32 client concurrency over physical B16, not a physical-B32 result.

Native measures 49.797098 request/s and vLLM measures 48.654164 request/s, a
single-lifecycle native point estimate of +2.35%. Wall P50/P95/P99 is
628.30/669.17/674.59 ms versus 607.54/755.18/801.86 ms: native P50 is 3.42%
higher, while P95/P99 are 11.39%/15.87% lower. Peak HBM is 50,666 versus
53,465 MiB. Output length is one, so TPOT is null.

Independent revalidation confirms all 256 raw rows and tokens match the frozen
oracle. Native reports exactly eight B16 append batches, `{16:8}` and
`{2064:8}` histograms, 16,512 append rows, zero decode, eight retained plans
covering request IDs 60000--60127, hit rate 1, 262,144 effective reused tokens,
and complete temporary-branch recycling. Its compiled, scheduler and state
compatibility identities exactly match the c16 profile. Both client and
launcher exit codes are zero; stderr, scoped ports, candidate processes and
NPU0 are empty after teardown. The comparison manifest is
`.benchmarks/qwen14b-equal-reuse-rev8-c32-o1-b16-diagnostic-r1-comparison.json`
with SHA-256
`b376f43084e56c7ad6c64bdb80d9241c862ff5dcdd9b3d32e6823258939bfe11`.
This is `performance_claim=false`; it admits only preregistration of a separate
formal c32/o1 3+3 runner. It does not establish physical-B32 performance,
pooled COW, broad serving superiority, or TTFT acceleration.

## Qwen2.5-14B equal-reuse c32/o1 formal v1 rejected lifecycle

The first formal native lifecycle launched from clean parent `d566bfb` on
physical NPU0 and is retained at
`results/qwen14b-native-equal-reuse-rev8-c32-o1-b16-v1-r1`. All 128 o1 outputs
matched the frozen schema-v2 oracle, every request reported the expected
2,048-token prefix reuse, temporary branches were recycled, and the run
observed 48.977082 request/s with peak HBM 50,666 MiB. These are diagnostic
facts from a rejected native-only lifecycle, not a performance comparison.

The physical gate rejected the run because client thread startup skew formed
nine append cohorts: `{1:1,15:1,16:7}` and `{129:1,1935:1,2064:7}`, rather than
eight B16/2,064-row cohorts. `client_exit_code.txt` and
`launcher_exit_code.txt` are both 1, `FAILED` records the incomplete probe, and
`client_stderr.txt` preserves the complete violation list. Port, host process,
container process and NPU0 cleanup snapshots are empty/clean. No V1 lifecycle
ran, no suite was generated, and `performance_claim=false`.

The result/raw/stderr/failure-provenance SHA-256 values are respectively
`02cf356f15ba14bd62b23e5680c093730df2ec9c81c89a23e17e224b1224c58f`,
`92f696bdbc76cd4d7092942a4e6b3d6e37dfd7acac49fcadbf5469fa9dd9b0fc`,
`f59d7f56a1df0997864d0d4c13b4287094ba9835f83803114b670b0a35b7f943`
and `d22318939105811f09e581f3acfb45da650c9868c1df8e4d3d00c7e3658226c1`.
The v2 runner preserves this directory, gives all six new lifecycles unique
names, and applies the same cyclic start barrier and throughput interval
semantics to native and vLLM. Physical B16/state identity gates remain strict.

## Qwen2.5-14B equal-reuse c32/o1 formal v2 rejected lifecycle

The v2 native lifecycle launched from clean parent `b8fac25` and is retained at
`results/qwen14b-native-equal-reuse-rev8-c32-o1-b16-v2-r1`. The cyclic barrier
worked: telemetry contains exactly eight B16 append batches, `{16:8}` and
`{2064:8}` histograms, 16,512 rows, zero decode, eight retained plans and all
128 unique request IDs. All 128 outputs match the frozen oracle, reuse and
branch recycling pass, throughput is observed at 48.432230 request/s, and peak
HBM is 50,666 MiB.

The lifecycle nevertheless remains rejected because the auditor expected each
plan to contain one predetermined contiguous ordinal range. Barrier release
legitimately produced a different B16 partition, so all eight plan indexes were
flagged even though cardinality, global coverage, phase, trace and reuse were
correct. Client/launcher exit codes are 1, V1 did not run, no suite exists, and
`performance_claim=false`; process, port and NPU0 cleanup passed.

The result/raw/stderr/failure-provenance SHA-256 values are respectively
`fd9c544fd4d321a52d77cc3370f48ed24c24c37545bbce93b0b91d608e95f369`,
`7963f9422da70cc596502b6881e96065bef7edc2c01d0497667b075402d1267f`,
`1f871847bd237ae0314a0330a738d4640c4888f1ccdb7e05b5f010f09570e292`
and `5a5319ae5c0c6b5ce7367fe1432e8c7370a7c33ce59b75539e058d7de2ea77ab`.
The v3 auditor removes only contiguous-ordinal membership: every plan must
still contain 16 unique measured IDs, all plans must cover 60000--60127 exactly
once, and trace IDs, phase and reuse must match. All physical and identity gates
remain unchanged.

## Qwen2.5-14B equal-reuse c32/o1 formal v3 interrupted pair

Native N1 from clean parent `3acf273` passes every lifecycle gate at
`results/qwen14b-native-equal-reuse-rev8-c32-o1-b16-v3-r1`: 128/128 oracle
outputs are exact, request start and throughput interval policies are frozen,
eight B16 append cohorts cover all IDs, the c16/B16 state identity is
unchanged, all branches recycle, and cleanup is empty. It records 47.970137
request/s, wall P50/P95/P99 511.26/686.48/692.10 ms, and peak HBM 50,667 MiB.
The result/raw/metadata SHA-256 values are
`507846255003a57e26de5dbd469c027adeab2e10213d3a28d6a05f6c44a3ae99`,
`c835efb23855f03ecd14823364b3d37205bc97eb64c5e44e2dab11c9ba1c0df6`
and `d0271003faaf725dfd6b48072dcce7678f633b9fe60ff544d237a64b6125cbb7`.

V1 at `results/qwen14b-vllm-equal-reuse-c32-o1-v3-r1` never served a request.
The fixed container exited 137 during baseline startup and Docker reported an
OCI `setns` failure. Container PID capture consequently failed, so the harness
correctly marked residue as unproven and rejected the lifecycle. Host-side
port, NPU0 and related-process checks were empty. The server-log,
failure-provenance and FAILED-note SHA-256 values are
`28f98ddd7e61fec97070d3b537b4d440d4d1bbf6e33682b7cf2e6bbe81d6f995`,
`43825e1945e21c2b112315b17f9ae1e92097094466d2f128556b6559a1b4883e`
and `e6d97b5cf26063c7214999c912c4b57ec00adc39055b3d5d526fcde62e6aea8e`.
No paired comparison or suite exists. The same container ID/image was restarted
and passed exec/top/NPU0 preflight; v4 uses six new names and checks container
running state before each V lifecycle.

## Qwen2.5-14B equal-reuse c32/o1 over physical B16 formal milestone

`results/qwen14b-equal-reuse-rev8-c32-o1-b16-v4-suite.json` admits the
client-c32/o1 cell from clean parent `f04ec39`. Both runtimes use physical
Ascend 910B2 NPU0, Qwen2.5-14B BF16, the frozen 128-row prompt family with
2,048 reusable and 129 distinct suffix tokens, greedy fixed one-token output,
and schema-v2 independent oracle SHA-256
`71807a4136d40556a297bc47ed105c3c2e8a30a1726ce2c69a163c73d198a732`.
The common cyclic concurrency barrier and first-request-start to
last-request-completion interval are frozen in both clients.

Native lifecycle throughput is 48.409884, 48.577381 and 48.191669 request/s;
vLLM throughput is 41.772527, 41.507125 and 40.387499 request/s. The
preregistered medians are 48.409884 and 41.507125 request/s and output token/s,
so native is 16.63% higher on the declared metric. Median-lifecycle wall
P50/P95/P99 is 517.15/705.85/711.49 ms for native and
672.61/811.90/819.60 ms for vLLM. Output length is one, so TPOT is null. Peak
HBM is 50,667 versus 53,465 MiB. TTFT remains cross-runtime incomparable and
no TTFT acceleration is claimed.

All 384 requests per runtime, 768 total, match the frozen oracle with zero
errors. Every native lifecycle records exactly eight B16 append cohorts,
`{16:8}` and `{2064:8}` histograms, 16,512 append rows, zero decode batches,
complete 128-request plan coverage, hit rate 1, 262,144 effective reused
tokens, and complete temporary-branch recycling. Client concurrency is 32,
but native physical batch size is 16. This result must not be described as a
physical-B32 execution result.

The native execution-config, compiled-plan, scheduler-plan and state-
compatibility identities remain respectively
`90f2ff9360a55af30f7429aeb27c5d0a3c215badb6ca2161a4ab95b2c6a06e57`,
`7bfbd67b631322180959076eebda3c5ec944e02182f6476f5eab485f1ee64753`,
`c22eab01e78287c993cdbdb9288735861213eae54521cc736bc2d5291cbf7884`
and `170d04b298a6736cf7807c215b824d229d8a0755d2f6add7894567f1de72b4df`.
Thus this admission preserves the c16/B16 state identity; a real B32 plan must
change the relevant execution and compatibility identities and invalidate old
state.

All six lifecycles have independent process and artifact identities, zero
client/launcher exit status, empty client stderr, and empty scoped port and
process residue after teardown. NPU0 is clean after each lifecycle. A fresh
aggregation is byte-identical to the checked suite; both have SHA-256
`974f7d89a3a55d779bae762aa47d15c5f07df2e3d230ee5b608e5357cf96d691`.
This formal result admits only equal-reuse c32/o1 over physical B16.
c32/o{32,128}, physical B32, pooled-block COW, and broad ordinary-serving
superiority remain unproven.

## Qwen2.5-14B equal-reuse c32/o32 capacity-aware diagnostic

One clean-parent diagnostic lifecycle per runtime was run from commit
`cf9a5b97ceddefd7ef13cecaf29610809dbaa1fe` on the same physical Ascend 910B2
NPU0. The candidate remained the project-owned Rust + C++/ACL runtime; the
pinned vLLM-HUST + vLLM-Ascend-HUST container was an independent baseline.
Both used Qwen2.5-14B BF16, the frozen 2,048-token reusable prefix plus
129-token suffix, the schema-v2 o32 greedy oracle, fixed 32-token output, and a
synchronized 32-client start. The native physical execution plan remained B16.
The prompt-family SHA-256 is
`944c51b10cd76e671fdf32d5108776cedc1b2f16900f44ff56651fc4e54731fe` and the
oracle SHA-256 is
`f83312ed1a422ca3f259ac299bfe40709f6a409f801a80130005974eb562ca09`.
Both launchers used fixed container
`146ccf6b514125dc36f8dbcf782fd16f8439d8fb75f5ee7518e6f68ba75c3e14`, image
`sha256:105834a38766a6b1b89a7eeb313a37351d098a69e8cdee87ad0ca3a6e090ce13`.

| Metric | Native | vLLM | Native delta |
|---|---:|---:|---:|
| Request/s | 10.582119 | 14.971981 | -29.32% |
| Output token/s | 338.627800 | 479.103388 | -29.32% |
| Wall P50 ms | 2,286.137 | 2,094.129 | +9.17% |
| Wall P95 ms | 3,056.688 | 2,193.949 | +39.32% |
| Wall P99 ms | 3,061.214 | 2,198.488 | +39.24% |
| TPOT P50 ms | 38.189 | 48.923 | -21.94% |
| TPOT P95 ms | 38.317 | 49.600 | -22.75% |
| TPOT P99 ms | 38.338 | 57.228 | -33.01% |
| Peak HBM MiB | 50,667 | 53,467 | -5.24% |

All 256 raw requests and 8,192 generated tokens match the frozen oracle. Both
clients and launchers exited zero with empty client stderr, and scoped port,
process and NPU cleanup checks passed. Native reports zero errors, hit rate 1,
262,144 effective reused tokens, eight physical B16 append batches, 248 B16
decode batches, 256 total batches and 4,096 completed items. Its retained plan
tail contains four disjoint B16 cohorts, each with one append followed by 31
decode steps, and all temporary branches are recycled.
The vLLM server log records an `EngineDeadError` and semaphore cleanup warning
after all two warmups and 128 measured HTTP 200 responses completed, during
shutdown. It caused no failed request or measured residue, but is retained in
the artifact and is not described as an error-free server log.

The native state identity changed as required by the capacity-aware scheduler:
compiled plan `7bfbd67b631322180959076eebda3c5ec944e02182f6476f5eab485f1ee64753`,
scheduler-plan v5 `3b940c29c318fe15c19452f2d88f217bccbf1a83f9798043dd157899898cc136`,
scheduler implementation
`74824e64b7e88cfd605625b9af7a3a7624398e67b9bd58de397580da4792427c`, and
state compatibility
`981f1c52feaba56661972df4cac2a4f102b8a247125c29d1d34cad459d894945`.
The old scheduler-plan v4 and state identities are rejected.

Authoritative diagnostic artifacts are
`.benchmarks/qwen14b-native-equal-reuse-rev8-c32-o32-b16-diagnostic-r1`,
`.benchmarks/qwen14b-vllm-equal-reuse-c32-o32-diagnostic-r1`, and
`.benchmarks/qwen14b-equal-reuse-rev8-c32-o32-b16-diagnostic-r1-comparison.json`.
Their result/raw SHA-256 values are respectively
`2f428c3f07001b5cf17c387f05b6af32d0db50c86bbc967d377210b98a758f70`,
`eef3f26faecf3c893313af54fe7b95d3662292e3219bfeb33cad7790659ce9fc`,
`2c6d23c7ad4d6318d6601bab0fa965467096234c008c2d7e6b8f4547289fc0ad`, and
`28c648dca29c48ef3677c9f69a6546db70fac91c6c611e9975d48d92dbf51707`.
The comparison was independently regenerated byte-identically at SHA-256
`d4a6a72ff69dffd6bf5781665ead03affa4514e181f27f8db1bf4185ef753f62`.

The auditor accepted the diagnostic evidence but rejected formal admission:
`performance_claim=false`, `native_faster_point_estimate=false`, and
`formal_gate_open=false`. Lower native TPOT and HBM do not compensate for the
29.32% request-throughput deficit under the preregistered rule. The result is
not copied into `results/` or the paper's formal performance table. It suggests
that two long-lived B16 branch waves serialize c32 service; the next isolated
milestone will add queue, state-slot-wait and wave execution timing before any
capacity or B32 change. Cross-runtime TTFT remains incomparable and is not
reported.

## Qwen2.5-14B equal-reuse c32/o32 capacity-wave profiling diagnostic

The follow-up profiling pair ran from clean commit
`5fbe5a3f8a1db3bd57ddf97bbe120b28e2a3a369` on physical NPU0. It retained the
same Qwen2.5-14B BF16 model, frozen 2,048/129 token family, schema-v2 o32 greedy
oracle, 128 measured requests, synchronized client concurrency 32, fixed output
length 32, physical B16 native plan and pinned vLLM baseline. This is a
single-lifecycle diagnostic, not a formal suite.

| Metric | Native | vLLM | Native delta |
|---|---:|---:|---:|
| Request/s | 10.668870 | 15.017500 | -28.96% |
| Output token/s | 341.403850 | 480.559990 | -28.96% |
| Wall P50 ms | 2,263.002 | 2,096.810 | +7.93% |
| Wall P95 ms | 3,027.119 | 2,188.281 | +38.33% |
| Wall P99 ms | 3,032.741 | 2,195.405 | +38.14% |
| TPOT P50 ms | 37.993 | 45.824 | -17.09% |
| TPOT P95 ms | 38.125 | 49.562 | -23.08% |
| TPOT P99 ms | 38.151 | 57.061 | -33.14% |
| Peak HBM MiB | 50,667 | 53,467 | -2,800 MiB |

Both runtimes produced 128/128 exact rows and all 8,192 output tokens matched
the frozen oracle. Native reports zero errors, hit rate 1, 262,144 effective
reused tokens, eight B16 append batches, 248 B16 decode batches, 256 total
batches, 4,096 completed batch items, zero timing drops and complete branch
recycling. Both client and launcher exits are zero; client stderr, scoped ports,
candidate processes and NPU0 are empty after teardown. The vLLM log retains a
post-request forced-process shutdown warning and one resource-tracker semaphore
warning; all requests completed first and no measured residue remained.

The complete timeline shows eight strictly non-overlapping B16 waves. Each
contains one append and 31 decode batches and releases tracked states from 17
to the retained source state before the next append. Cyclic c32 admission forms
four pairs: each even wave has queue/active depth 32 and zero state-slot wait;
the following odd wave has depth 16 and waits
1,531.571/1,476.007/1,479.646/1,481.968 ms. Median batch enqueue-to-start is
0.074 ms, executor time is 37.465 ms, and post-executor state release is
0.225 ms. The throughput deficit is therefore attributed to physical state
capacity serializing each pair of long-lived B16 waves, rather than actor queue
dispatch or state-release bookkeeping. This attribution does not establish
that increasing capacity or physical batch size is safe or faster.

Scheduler-plan v6 is
`10717c4f446d62d53c53d8aa2fb1d6052563e942dc562a91bbaa58b0178a5fc2`,
the native server digest is
`31e08c2a127d1f51bfca82d0b367ac7bd8d113ad571290688267dee12823ff2b`,
and final state compatibility is
`c83f0e720b0c9e7cd0ac4c9d39a5e807b8ad203e752f5f8a1b5b1a0981b46dc2`.
The telemetry policy `native-capacity-wave-timing-v1` and server binary are
bound into the scheduler and state identity, so the earlier v5 state cannot be
reused.

The native result/raw/metadata SHA-256 values are
`88cc0b21e6988dd2f371a6f1bbd319d01383822cf65fb563db02a1e24f13c4b6`,
`3621e8a114c2bf77e14053cc51451fdd91738c4a2555c5df8a0a62aa341f97a1`, and
`0113c7cf3ca15ac9af4d8a4ecdc4816fd6e378472d2ec4519680d27fd3e3949e`.
The vLLM values are
`fea80107041e4e36aeb477af7975df0a50aecb715a6b4530da125d61fd7d1e82`,
`b224d097de1999cde580f55503154702a0a68ead40f1fb320c5d89cce7d5e43b`, and
`6fe995cd98721dfdf796a9dec1829adbba5b363a00729f2a866ebce1c8c7a717`.
The comparison artifact is
`.benchmarks/qwen14b-equal-reuse-rev8-c32-o32-b16-wave-v3-r1-comparison.json`;
an absolute-path re-audit reproduced it byte-for-byte at SHA-256
`6becffbad4fe3f7c5145a29f2e1b778c3362def4e409e811eb3c7c25c861316e`.

The independent auditor sets `profiling_only=true`,
`performance_claim=false`, `native_faster_point_estimate=false`, and
`formal_gate_open=false`. Lower native TPOT and HBM do not override the 28.96%
throughput loss. The result stays outside `results/` and the paper's formal
table; physical B32, capacity changes, c32/o128, COW and cross-runtime TTFT
comparison remain closed.

## Qwen2.5-14B physical-B16 fused gate-up component gate

The state-free component suite
`.benchmarks/qwen14b-fused-gate-up-component-v1` ran from clean pushed parent
`2f0b2d9f8e13fe0da4d03b35c1278e2c3eebaca4` on physical Ascend 910B2 NPU0.
It alternated three independent control and candidate processes in the frozen
order separate/fused, fused/separate, separate/fused. Each process performed
one same-policy warmup and timed only the second complete physical-B16
RMSNorm-through-48-layers-through-LM-head decode.

Control elapsed times are 30.069466, 30.280157 and 30.081396 ms, with a
30.081396 ms median. Fused gate-up plus `aclnnSwiGlu` times are 29.123649,
29.020769 and 29.088939 ms, with a 29.088939 ms median. The independently
recomputed speedup is 1.034118x and latency reduction is 3.2992%, above the
preregistered 1.5% admission threshold. Peak ACL allocation is exactly
58,372,862,144 bytes in both arms; minimum post-execution free HBM differs by
only 335,872 bytes (0.320 MiB).

All 96 physical rows select frozen token 264, contain finite logits and retain
the independently recomputed top-1 margin certificate. Within-arm complete
logit tensors are deterministic: control SHA-256 is
`adc3afd7f20ac370ab4b8dad071b6f95ff172a47bf46b46179d3d0a34045001d`
and fused SHA-256 is
`d2c09d7487a035a34ecfffa714f21230ce4c98ef81b82068d9ac6725538c5609`.
All six generation sequences equal frozen `[525,264]`.

The oracle lock is
`92324fe13768766c0eadbe3d1abbab68ba872608707f1e8bab4535dd21bb9257`,
the execution config is
`90f2ff9360a55af30f7429aeb27c5d0a3c215badb6ca2161a4ab95b2c6a06e57`,
and resident plan identity is
`18d61bbd12deb7e56faabad33ca3dbffe31b7ee37cb3960d66d7db65c83557ec`.
The runner rehashed all 48 layer packs and the global pack before launch. Six
unique `(worker PID,/proc start ticks)` identities and non-overlapping windows
were audited. Every process/probe exited zero; final host docker-exec, exact
host/container worker evidence is empty, while the non-empty NPU snapshot
explicitly reports `No running processes found in NPU 0`.

Two independent audit regenerations are byte-identical at SHA-256
`a8ea1b9fa5fa08167cb9138b66306f4ce1cc541ad14aad33f9f89aa506dfa438`
with zero violations. The gate sets `integration_candidate=true` but keeps
`performance_claim=false` and `formal_gate_open=false`. It authorizes only a
separate schema-4/revision-9 production integration milestone with old-state
invalidation; it is not online, native/vLLM, ordinary-serving or TTFT evidence.

## Qwen2.5-14B fused production identity readiness

The separate integration milestone completed without an online or baseline
run. Execution-config schema 4 selects
`fused_gate_up_aclnn_swiglu`; executor-plan revision 9 binds a 360-byte
execution-artifact record covering actual transformed packs, pack layouts,
candidate binary, CANN runtime libraries, compiler/build, lowering and the
ACLNN-only project-kernel root. Schema-3 and revision-8 inputs fail closed, and
Rust validates config SHA, artifact SHA, MLP policy and prefix-extension mode
before spawning the native worker.

The software-only artifact is
`.benchmarks/native-qwen14b-manifest-v5-fused`. Its artifact record SHA-256 is
`427335934fdb4ce536ec647f19737aeb3719058bad7b565939ecf4cfa533ee55`, config
SHA-256 is
`3c49392c68f29a549a92f2ede1e097b04b04c28886b549c1e9b9fc9ce3b9a6d4`, and
resident-plan identity is
`da85aeee4ef98f0e7c4234876fb1b4ef1f628f29b6fa552de1897c59f2adad35`.
Independent audit SHA-256
`d7c47d8201bf8bba70ef6db98343da9ca005c10cab0e71d715267c44f1d24780`
recomputed all 48 pack files, global pack, executor and three CANN library
hashes. A deliberately wrong record exited 2 before ACL initialization; NPU0
was empty both before and after.

This is `hardware_execution=false`, carries no request/s or latency result, and
does not change any formal performance conclusion. It authorizes only a later
single paired c32/o32-over-physical-B16 diagnostic; formal c32/o32 and all other
closed gates remain closed.

That next diagnostic is now preregistered exclusively on physical NPU4 through
`scripts/run_qwen14b_revision9_c32_o32_npu4_diagnostic.sh`. It allows one fresh
native lifecycle and one fresh baseline lifecycle, fixes client concurrency 32
over native physical B16, and requires the same frozen token IDs, independent
greedy oracle and 32-token output. Full request/response rows, process and
container identities, sanitized environments, dependency digests, device/HBM
snapshots and cleanup evidence are mandatory. It remains
`formal_gate_open=false` and is not yet an online result; no formal 3+3, B32,
o128, COW or cross-runtime TTFT comparison is authorized.

## Qwen2.5-14B schema-4/revision-9 NPU4 paired diagnostic attempt

The sole attempt ran from clean pushed parent
`5b5afdb9b4f50991cb380f87af3aaac3d406da04`. Native was configured for client
concurrency 32 over physical B16 with the fused Gate/Up plus ACLNN SwiGLU
artifact, but a remaining results-family admission branch still admitted only
c32/o1. The launcher exited 2 before creating its normal lifecycle directory,
spawning a worker, initializing ACL, or accepting a request. The reconstructed
failure directory clearly labels this boundary and retains the exact stderr,
exit code, sanitized configuration, artifact/dependency identities, container
identity and before/after NPU/port/process snapshots. Native therefore has no
online metric or token-correctness result in this attempt.

After verifying NPU4 cleanup, the paired runner completed the independent
pinned baseline lifecycle. It returned 128/128 successful requests and 4,096
output tokens. An independent per-ordinal audit found zero prompt-token or
output-token violations against the frozen family and greedy oracle. Baseline
request throughput is 15.05555 request/s and output throughput is 481.77755
token/s; wall P50/P95/P99 is 2,064.60/2,225.73/2,230.59 ms, TPOT P50/P95/P99
is 45.90/49.98/56.68 ms, and peak HBM is 53,460 MiB. Failed requests are zero,
so the derived request error rate is 0%. Equivalent vLLM state-hit and
effective-reuse counters are unavailable and remain null.

The paired comparison is rejected because the native arm is absent, with
`performance_claim=false`, `formal_gate_open=false`, and no TTFT comparison.
NPU4, ports 18081/18083, scoped workers and docker-exec processes were empty
after teardown. This satisfies only the reproducible-failure branch of the
milestone acceptance. The next milestone is to fix that admission path and
rerun the identical c32/o32-over-B16 pair; all later gates remain closed.

The v2 readiness repair is intentionally narrower than a runtime change. It
adds one diagnostic-only c32/o32/B16 admission tuple, retains all schema-4 and
revision-9 identity checks, leaves the formal c32/o1 surface unchanged, and
assigns fresh result names so the rejected v1 evidence cannot be overwritten.

The v2 lifecycle reached the next gate but did not reach HTTP readiness. The
native server remained alive for the launcher's complete fixed 60-second wait,
produced no readiness response or request row, and was then cleanly terminated
by the scoped cleanup path (status 143). Therefore native throughput, latency,
TPOT, hit rate and HBM metrics are null. The paired v2 baseline independently
matched all 128 rows and 4,096 output tokens, measuring 14.99742 request/s,
479.91740 output token/s, wall P50/P95/P99
2,086.96/2,201.28/2,215.30 ms, TPOT P50/P95/P99
45.35/52.37/57.00 ms, zero failed requests and 53,461 MiB peak HBM. vLLM reuse
counters remain unavailable rather than synthesized.

The bounded v3 fix exposes and validates a 1--600 second startup timeout,
retains the 60-second launcher default, and preregisters 180 seconds only for
the schema-4/revision-9 diagnostic. Startup waiting does not alter weights,
RoPE, state schema, KV layout, execution plan, lowering, artifact identity or
runtime dependency identity. The rerun must use fresh v3 paths and remains a
single-lifecycle, force-closed diagnostic.

The 180-second v3 allowance was still shorter than the complete fail-closed
startup validation. At the boundary both the Rust parent and resident C++
worker remained alive, no ACL device process or HBM allocation had appeared,
and the HTTP port was not yet bound. Cleanup removed both without residue and
native completed zero requests. The independent baseline was again exact for
128 rows/4,096 tokens and measured 15.06376 request/s, 482.04026 output
token/s, wall P50/P95/P99 2,084.16/2,200.33/2,209.70 ms, TPOT
45.81/49.62/56.73 ms, zero failures and 53,460 MiB peak HBM.

The fresh v4 retry selects 600 seconds, the validated upper bound, solely to
cover content rehash plus normal worker initialization. This is still a
bounded orchestration timeout, not an execution choice, and all formal gates
remain closed.

v4 covered the full pre-ACL rehash and reached HTTP readiness. Its first online
physical-B16 cohort exposed a separate sizing error: the 5-GiB workspace had
only 3,403,264 bytes remaining when the fused path requested another
29,166,592 bytes. The worker failed closed, emitted the exact arena-capacity
error, and caused HTTP 500 responses. Some outstanding requests did not return
after the runtime actor exited; the old client had no lifecycle bound, so the
runner was explicitly interrupted after ten minutes. Cleanup proved NPU4,
port 18081 and all scoped native/client processes empty. No baseline was
started and v4 supplies no paired metric.

v5 uses a 6-GiB workspace and binds it into new resident-plan digest
`aef7c4c35d090caf58d832e26e65f3e815d9af7d7c931bd712c0cd34b6aac2cb`.
The old 5-GiB diagnostic plan digest
`bb28be5c0571bb5dde16ef7b1c44383eb3aefc00d29d777820ad66d22d3a917f`
must not aggregate state or results with v5. Formal revision-8 admission remains
5 GiB. The shared-prefix client is also wrapped in a validated bounded
lifecycle timeout, and INT/TERM now preserve nonzero failure status while the
existing EXIT trap performs scoped cleanup.

v5 then completed the native online workload correctly: 128 rows, 4,096 exact
tokens, eight physical-B16 append batches, 248 B16 decode batches, hit rate
1.0, 262,144 reused tokens and zero request errors. The measured but unadmitted
native values are 10.83019 request/s, 346.56614 token/s, wall P50/P95/P99
2,226.55/2,991.57/2,996.59 ms, TPOT 37.13/37.48/37.51 ms and 51,685 MiB peak
HBM. After clean teardown, an obsolete trace validator rejected the evidence:
it expected 677 workspace calls from separate Gate/Up, while the immutable
fused Gate/Up plus ACLNN SwiGLU path emits 581. Therefore final native
run_metadata was not created.

The v5 baseline independently completed all 128 rows/4,096 exact tokens at
15.04547 request/s and 481.45520 token/s, wall P50/P95/P99
2,090.11/2,162.39/2,170.23 ms, TPOT 45.72/49.48/57.02 ms, zero failures and
53,461 MiB peak HBM. Because native metadata is absent, the paired auditor
rejects the comparison; these values do not authorize a cross-runtime delta.
v6 fixes only the policy-aware trace validation (fused=581, separate=677) and
uses fresh paths with the same v5 execution/state identity.

v6 then completed both clean online lifecycles and all 8,192 raw output tokens
were oracle-exact. Native recorded 10.78797 request/s, 345.21511 token/s, wall
P50/P95/P99 2,248.82/3,020.65/3,028.90 ms, TPOT 37.01/37.35/37.38 ms,
hit rate 1.0, 262,144 reused tokens, zero errors and 51,684 MiB peak HBM over
eight append and 248 decode physical-B16 batches. Baseline recorded 15.02371
request/s, 480.75870 token/s, wall 2,088.81/2,178.26/2,185.33 ms, TPOT
45.63/49.40/56.75 ms, zero failures and 53,461 MiB peak HBM.

The paired auditor rejected only native claim-status provenance: enabling the
additional decode trace unconditionally replaced the shared-prefix diagnostic
status with the dedicated timing-probe status. v6 is therefore retained as a
rejected diagnostic and its -28.20% request-throughput point estimate is not
admitted. v7 makes trace collection metadata-orthogonal for explicit
diagnostic lifecycles, uses fresh paths, and keeps the same execution/state
identity and force-closed formal gate.

The clean-parent v7 rerun passes the paired diagnostic auditor with no
violations. Both runtimes complete 128 requests and 4,096 exact output tokens.
Native measures 10.82076 request/s, 346.26431 token/s, wall P50/P95/P99
2,235.19/3,008.08/3,013.13 ms, TPOT 37.05/37.26/37.29 ms, hit rate 1.0,
262,144 effective reused tokens, zero errors and 51,684 MiB peak HBM. Baseline
measures 15.25484 request/s, 488.15501 token/s, wall
2,057.70/2,133.93/2,146.15 ms, TPOT 45.75/49.55/56.71 ms, zero failures and
53,460 MiB peak HBM; hit/reuse remain unavailable. Native's request-throughput
point estimate is -29.07%. The result is accepted only as a single-lifecycle
diagnostic: `performance_claim=false`, `formal_gate_open=false`, physical batch
is B16 despite client concurrency 32, and TTFT is not compared.

This result does not support the shorthand that Native wins prefill but loses
decode. Exact state reuse directly avoids repeated prefill, but it does not
reduce per-token decode arithmetic. In this diagnostic Native TPOT percentiles
are lower than vLLM's, while overall throughput and tail completion are worse
because concurrency 32 is serialized over 16 available branch slots. The state
abstraction can still enable decode indirectly through KV residency, compatible
cohort formation, future fork/COW, and generation-safe slot reuse. Current
evidence does not isolate a causal decode gain from any of those mechanisms.

## Revision-10 paged continuation-payload NPU4 attempt (rejected)

The first clean-commit NPU4 component lifecycle from `014e4e0` is reproducible
failure evidence, not an online correctness result. The worker started but
failed its pre-ACL execution-object audit with `executor binary identity
mismatch`; the Rust probe then observed EOF. The artifact record expected the
revision-9 executable SHA-256 `ee197491...eee7e` and compiler/build identity
`5d2d74b9...26b48`, while the built revision-10 worker was
`bb960c8c...0579c` with build identity `360dedf3...79bfc1`.

No prompt, child, COW, token or allocator transition executed, so the attempt
establishes none of the planned online payload properties. It does establish
that the worker rejects a stale execution object before continuation creation.
Probe/runner exits are 1, stderr is retained, NPU4 reports no process before or
after, baseline HBM is 3,418/3,419 MiB, and worker, docker-exec and scoped port
snapshots are empty after teardown. `performance_claim=false` and
`formal_gate_open=false` remain closed. A new fast preflight auditor now checks
the execution artifact against the built binary, CANN libraries,
compiler/build, selected lowering and project kernel. A later fresh attempt
must regenerate every dependent identity and use a new lifecycle name.

## Revision-10 v2 execution-object readiness (software only)

The stale revision-9 object has been replaced before any second NPU attempt.
The freshly generated revision-10 artifact/config/resident-plan identities are
`19c24dfb...a3ea`, `c19ad8cf...3d0a`, and `72ad0874...2983`. A lightweight
runtime-binding audit and a full independent recomputation both accept the
worker binary, compiler/build, selected fused lowering, project kernel, loaded
CANN libraries, transformed packs and layouts. The checked-in lock also names
the invalidated revision-9 identities so the runner cannot silently regress.

This row is software readiness only: `hardware_execution=false`,
`performance_claim=false`, and `formal_gate_open=false`. It contains no token,
COW, latency, throughput, HBM, capacity, or decode result. Exactly one fresh
NPU4 component-correctness lifecycle named
`qwen14b-rev10-paged-cow-npu4-correctness-v2` was the next permitted action.

## Revision-10 v2 NPU4 component attempt (rejected)

The sole v2 lifecycle from clean pushed commit `87d7c15` passed the new
execution-object binding but failed before any protocol request, oracle token,
or COW transition. Startup's legacy fixed-row B4 self-test copied a 32-block
prefix to `batch_index * 32`; under the revision-10 64-block shared paged arena,
index 2 begins at invalid block 64. `batched key prefix D2D` returned ACL
507899, after which the Rust probe observed EOF. Probe and runner both exited
1; stderr SHA-256 is `b875c570...d5118` and the result file is empty.

No request/s, output-token/s, latency percentile, TPOT, error rate, state-hit
rate, or peak HBM is defined because zero requests entered the protocol.
Effective reused tokens are zero. NPU4 baseline HBM was 3,418/3,419 MiB before
and after; no NPU process, candidate worker, docker exec, or scoped port
remained. This is reproducible negative component evidence, not an online or
performance result; `formal_gate_open=false`.

## Revision-10 paged startup-fixture repair (software only)

The fixed-row startup path has been replaced with allocator-owned fixture
planning. The B4 contract produces four distinct physical blocks, three
4-token partial-tail COW copies, four physical scatter slots and a 4-by-32
padded block table, all within a 64-block arena. Logical descriptor capacity
and physical block exhaustion are independently rejected. The ACL block-table
scratch now follows maximum logical batch geometry instead of physical arena
size. The full native build and all 25 native CTests pass.

The implementation change produces worker SHA `9d05efb0...1b833` and
compiler/build identity `5ac969fc...05bff`, invalidating v2 before reuse. No
The regenerated artifact/config/resident-plan identities are
`cabff3fe...bcef1`, `72892a8a...0f51b`, and `0f4ce289...e57ea`. Both
runtime-binding and full independent audits pass, while every corresponding v2
identity differs. This is still software readiness: no v3 NPU lifecycle is
claimed yet, and all online/performance metrics remain n/a.

## Revision-10 v3 NPU4 paged continuation-payload gate (passed)

The sole v3 lifecycle from clean pushed `09ec7fc` passes an independently
recomputed audit with no violations. Source prefill returns `51741`; source and
two forked children return `8440`; their next independent decode returns
`21324`, matching the frozen oracle at every position. Allocator state moves
from `(0,0,0,0)` to `(1,18,0,0)`, then `(3,20,17,2)`. One child eviction leaves
19 blocks; generation `2:1` is stale, replacement `2:2` is valid, and final
eviction yields `(0,0,0,2)`. This represents 4,352 immutable shared token-
references across the two children, not a measured throughput saving.

Probe/runner exits are zero and stderr is empty. Peak executor-observed HBM
usage is 35,996.89 MiB, peak live allocation is 35,337.28 MiB, and workspace
peak is 4,909.21 MiB. NPU4 baseline HBM is 3,419/3,421 MiB before/after; no NPU
process, candidate worker, docker exec or scoped port remains. Request/s,
output-token/s, latency percentiles, TPOT, online request error rate, state-hit
rate and effective reused-token performance counters are n/a because this is
not an online service lifecycle. Component operation error rate is zero.
`performance_claim=false` and `formal_gate_open=false` remain closed.

## Domain-v7 c32/B16 preparation failure (software only)

The first attempt to materialize the workflow/resource projection failed
closed after artifact/config compilation.  The extended resident-plan
inspector ignored the declared 64-block physical arena and derived 1,056 blocks
from the 33-descriptor logical capacity because its explicit-argument branch
matched only `argc == 7`, not the full 11-argument invocation.  The generator's
exact field check rejected the plan; resident-plan identity, runtime binding,
and independent artifact audit were therefore not accepted.

The parser now uses the explicit physical-block value for every extended form,
and a regression contract rejects restoration of the old predicate.  A manual
11-argument software probe reports 33 descriptors, 64 physical blocks, minimum
requirements 33/50, physical B16, and client concurrency 32.  These numbers are
parser validation only: no ACL, NPU, request, token, latency, throughput, HBM,
or baseline measurement occurred.  The partial `v8` directory is immutable
failure evidence; a fresh identity chain must use `v9` after a clean push.

That `v9` chain now exists from clean parent `e4b54ea`. Artifact
`ba9b3f84...0054c`, config `5b6f9b08...1e1ab`, and resident plan
`02cc451f...f20e` bind worker `29f17369...a5580`, build
`517973e9...5803`, the fused lowering, project kernel, transformed packs, and
loaded CANN libraries. Independently rerun binding, artifact, and plan audits
match the generator byte for byte. The earlier domain-v6 artifact/config/plan
are all different and are explicitly invalidated by the checked-in lock.

This remains software-only evidence: `hardware_execution=false`, no online
request or token ran, every performance metric is n/a, and
`formal_gate_open=false`.

## Revision-10 c32/o32 paired-diagnostic readiness

The schema-v3 launch chain now has a dedicated NPU4 runner and independent
audit contract. It binds artifact/config/resident plan
`803484fa...c8abb` / `55b10efb...2b552` / `26e04362...6407`, Rust server and
dependency closure `e689b37c...570e` / `77f0485e...fb64`, scheduler
`8d226273...8e0`, and aggregate state identity `a91d5de4...ceb1`. The launcher
also passes c32/source1x2177/private1 explicitly to inspector and worker.

No online lifecycle has run under this readiness change. Throughput, latency,
TPOT, errors, hit/reuse and HBM remain n/a. The only authorized next action is
one Native plus one pinned-vLLM c32/o32 diagnostic on NPU4; its result cannot
open the formal gate.

## Revision-10 state33 c32/o32 paired diagnostic (rejected)

The sole authorized pair ran sequentially on NPU4 from clean pushed
`cd7d506`. Native and vLLM each completed 128 real online requests and 4,096
oracle-exact output tokens with zero errors. Native measured 2.4550 request/s,
78.5612 output token/s, wall P50/P95/P99 11889.57/13035.22/13087.18 ms, TPOT
P50/P95/P99 364.53/373.11/373.82 ms, hit rate 1.0, 262,144 effective reused
tokens, and 40,165 MiB peak HBM. vLLM measured 14.7974 request/s, 473.5168
output token/s, wall 2106.05/2258.70/2267.48 ms, TPOT
46.09/50.10/56.72 ms, zero failed requests, and 53,461 MiB peak HBM; vLLM hit
rate and effective reuse are unavailable rather than synthesized.

The pair is rejected because the intended Native physical execution contract
did not materialize. State33 made every state-slot wait zero, but 128 append
requests formed 44 physical batches (`28xB1 + 8xB2 + 4xB5 + 4xB16`) and decode
formed 1,538 batches, including 1,406 B2 batches. The client correctly exited
one and withheld `run_metadata.json`; the independent paired auditor therefore
keeps every comparison claim closed. This is evidence that logical capacity is
necessary but insufficient: scheduler/workflow cohort formation must be fixed
before a fresh lifecycle can test whether the capacity change helps decode.
Both lifecycles cleaned NPU4, ports, workers and scoped docker exec state.

## Native model-RI graph readiness (software only)

Installed CANN 9.0 exposes and exports public model-RI capture, replay,
destruction, and task-group update APIs. The default-off component uses them
without Torch, vLLM, or SGLang and compiles against the installed runtime. A
historical 7B experiment captured only attention and failed generation parity;
it is not reused as evidence for this fixed-shape 14B chain.

The matched B16 control/candidate, graph identity, alternating NPU7 runner,
independent auditor, protocol rejection, and leaf-mutation contracts are
implemented. Focused historical-fused, graph, and override CTests pass 3/3.
No graph lifecycle has run under this change: component latency, speedup, HBM,
and acceptance are pending; online throughput, TPOT, TTFT, hit/reuse, and vLLM
comparison are n/a. `formal_gate_open=false` and
`performance_claim=false`.

The first clean-pushed runner invocation failed before ACL initialization:
the runtime-library awk loop shadowed the built-in name `index`, so the
fail-closed identity builder received an empty dependency closure. The local
v1 bundle records exit 2, empty candidate-worker evidence, baseline NPU7 HBM,
and no timing result. It is reproducible pre-execution failure evidence, not a
negative graph measurement. A unit contract now freezes the `field` parser and
self-excluding docker-exec filter; the only fresh retry is v2.

The fresh v2 suite passes independent audit. Eager/graph medians are
29.115094/28.979843 ms; graph replay is 0.135251 ms or 0.4645% lower
(1.00467x). The three eager samples span 29.067002--29.164724 ms and graph
samples 28.974823--29.034501 ms. All 96 frozen row decisions pass, all six
full-logit SHA-256 values equal `d2c09d74...5609`, and device ArgMax matches
the independent CPU scan. Coarse sampled HBM peak is 58,982.4 MiB in both arms,
executor-observed peak allocation is 55,668.70 MiB, and workspace peak is
4,909.21 MiB.

The graph artifact identity is `44ab6593...9867`; raw evidence and audit are at
`.benchmarks/qwen14b-native-decode-graph-component-npu7-v2`. All exits are
zero, stderr is empty, and final NPU7/worker/docker-exec/port checks pass. The
literal component threshold passes, but the 0.46% effect is too small to
explain the 31.08% online diagnostic gap and cannot be extrapolated beyond
fixed B16, sequence length 5.
The checked-in evidence lock is
`benchmarks/qwen14b_decode_graph_component_v2_success_lock.json`.

## Online model-RI graph readiness and rejected v5 partial evidence

The protocol worker now has a default-off `acl_model_ri_dynamic` path with
separate B1 and B16 graphs, complete task-group updates for online metadata
progression, and capture/update/replay/rebuild counters. Allocation, COW, H2D,
D2H, and commit remain outside capture; eager behavior is unchanged.

Resident-plan v8 and the scheduler/aggregate compatibility chain bind the
execution policy and independently recomputed graph contract. The latest
Native build and focused C++/shell/Python contracts pass. No online graph
lifecycle has run, so correctness, throughput, latency, TPOT, HBM, and
acceptance remain pending—not projected. The fixed component's 0.4645% gain
is not reused as online evidence.

The clean-push readiness artifact was generated from commit `3f31477`.
Independent audit accepts graph contract `05e23dd5...ad8e6`, resident plan
`7b6c6f88...5ad32`, scheduler `8eff361d...50a0e`, and aggregate compatibility
`185f8b44...af5cd` with no mismatch. The frozen non-hardware lock is
`benchmarks/qwen14b_online_graph_npu7_identity_lock_v1.json`; it binds both the
eager and graph resident plans, prompt/oracle, artifact, readiness, and source
commit. These are readiness identities, not online results.

The first v1 suite command was rejected before ACL initialization because its
outer runner passed a nested `.benchmarks` directory where the generic
launcher permits only the exact repository `.benchmarks` or `results` root.
It exited 2 with no worker, port, or NPU process and baseline HBM unchanged.
The immutable failure is under
`.benchmarks/qwen14b-online-graph-npu7-v1`; it contributes no correctness or
performance sample. The repaired run uses fresh v2 lifecycle names.

The clean-pushed v2 foreground supervisor was externally terminated near its
300-second command boundary while c1/o1 was still loading. The 14B worker
became ready immediately afterward, but no client request ran; the orphaned
server, docker exec, worker, port, and NPU allocation were explicitly cleaned.
NPU7 returned to 3,415 MiB baseline HBM. The controller's original EXIT trap
misrecorded status zero, so a separate immutable postmortem marks external exit
143 and zero requests. v2 contributes no correctness or performance sample.
The signal-aware repair uses fresh v3 names and a detached bounded supervisor.

The detached v3 c1/o1 lifecycle served four real requests: all four frozen
tokens were exact, error rate was zero, hit rate was 1.0, effective reuse was
8,192 tokens, request/output throughput was 10.1251/s, and peak HBM was
40,544 MiB. It then rejected its own artifact because the runner had enabled
decode-timing validation even though o1 has no iterative decode batch or trace.
Normal run metadata was therefore withheld and later arms did not start. This
is positive raw correctness but rejected lifecycle provenance, not an accepted
cell. Fresh v4 disables timing only for o1 and keeps it for every o32 arm.

v4 passed a complete c1/o1 lifecycle but failed c1/o32 correctness. Ordinal 0
produced the retained token twice and shifted the expected sequence by one;
ordinals 1--3 were exact. Counters ended at capture/update/replay/rebuild
1/123/123/0. The pattern proves capture end recorded but did not execute the
first decode quantum; later updated replays were correct. c32 did not start.

The repair explicitly executes after first capture and binds
`first_execution=execute-after-capture-end` into graph contract revision 2.
This changes the binary and graph/resident/scheduler/aggregate identity,
invalidating v12 and lock v1. Fresh readiness uses v13, lock v2, and v5 names.

Clean-push v13 readiness from `affb5ac` passes with no independent-audit
mismatch. Revision-2 graph contract, resident plan, scheduler, and aggregate
identities are `62f8016d...413da`, `0b07dbe2...31b06`,
`4e9d6086...de3b0`, and `ab763615...c5998`. Frozen lock v2 binds both eager
and graph plans plus every prior artifact/provenance leaf.

The detached v5 suite then accepted graph c1/o1 and graph c1/o32. The latter
completed all four 32-token requests exactly with graph capture/update/replay/
rebuild counters 1/123/124/0, establishing the revision-2 first-execution
repair. The next eager c32/o32 lifecycle served 128/128 token-exact requests
with zero errors: 10.046309 request/s, 321.481895 output token/s, wall
P50/P95/P99 2641.139/3184.367/3276.161 ms, median TPOT 68.533 ms, hit rate
1.0, 262,144 effective reused tokens, and 40,545 MiB sampled peak HBM.
It is nevertheless rejected and is not a matched comparison.

The first rejection is a harness error: the runner omitted the revision-10
co-resident contract and inherited `serialized-state17`. More importantly,
the immutable batch trace independently rejects physical B16: append was
8xB16, while decode was 243xB16 plus eleven smaller batches, for 254 decode
and 262 total batches. The two initial append cohorts mixed during decode and
finished unevenly. Since the graph arm admits only B1/B16, it correctly never
started. The repair persists full workflow cohort membership through decode,
changes scheduler/aggregate identity, explicitly selects the co-resident
contract, and requires fresh v14/lock-v3/v6 evidence. v5 remains failed
real-online evidence with `formal_gate_open=false` and no performance claim.

Clean pushed `fb25fa0` produced the sole v14 readiness artifact without
hardware execution. Independent execution-artifact, runtime-binding, and
complete Native state-chain audits all accept with no mismatch. The exact
artifact/config/readiness digests are `f5429c18...ebeef`,
`befc49a8...c65f2`, and `8b2ffde6...cb13`; graph-contract, graph resident,
scheduler, and state-compatibility identities are `62f8016d...413da`,
`0b07dbe2...31b06`, `9641f81d...d8470`, and `b20eea4b...c193`.
`benchmarks/qwen14b_online_graph_npu7_identity_lock_v3.json` freezes those
leaves together with the prompt/oracle and eager control plan. This is
preregistration evidence only: it adds no request, token, latency, throughput,
or HBM sample.

The v6 suite then completed all four real-online producer lifecycles from
clean pushed `a14ef0f`: all 264 requests and 8,324 tokens were exact, both c32
arms satisfied 8 B16 append plus 248 B16 decode, and every process/port/device
cleanup check passed. Its suite controller is still rejected because the
independent auditor raised `KeyError` while reading an obsolete
`run_metadata.configuration` path. The immutable producer records instead
carry physical device and execution mode in `hardware.physical_device` and
`runtime.online_decode_execution`. This is an offline audit-contract failure,
not an execution retry authorization. The corrected auditor must be committed
before writing a fresh re-audit record over the same immutable lifecycles.

Auditor commit `c8476d2` reads the produced metadata schema fail-closed and
rejects legacy-only `configuration` records. Its offline re-audit of the same
immutable v6 lifecycles is accepted with zero violations at
`results/qwen14b-online-graph-npu7-v6-reaudit-v2.json` (SHA-256
`40d2f477...9f89f`; auditor `fc5525c6...1caa5`). All 264 requests and 8,324
tokens are exact. c1/o32 ends at graph capture/update/replay/rebuild
`1/123/124/0`; graph c32 ends at `1/247/248/0`.

For c32/o32, eager versus graph is 10.293308 versus 6.305844 request/s and
329.385851 versus 201.787009 output token/s. Wall P50/P95/P99 is
2579.311/3150.813/3152.973 ms versus
4193.913/5171.297/5174.432 ms. TPOT P50/P95/P99 is
67.150/79.912/79.946 ms versus 119.040/147.021/147.065 ms. Both have zero
errors, hit rate 1.0, 262,144 reused tokens, and strict 8xB16 append plus
248xB16 decode; peak HBM is 40,544/40,552 MiB. Graph is 38.7384% lower in
request throughput and fails the 1% default-integration gate. The online graph
capability remains default-off; formal and performance-claim gates remain
closed.

## Attention-only online graph update readiness

An offline re-aggregation of the immutable v6 server logs exposes a stronger
cause than host descriptor overhead alone. Across 248 B16 decode batches,
revision-2 graph versus eager median total executor time is 64.848 versus
33.488 ms, host-visible layer submission is 12.227 versus 6.401 ms, and final
synchronization wall time is 52.650 versus 26.637 ms. Preparation/H2D and
workspace allocator time are effectively unchanged. Since synchronization
contains queued device work, this evidence says full-task-group update adds an
approximately execution-sized cost; it does not prove that arithmetic ran
twice.

The default-off revision-3 candidate therefore changes only the update scope:
48 one-task groups around per-layer FIA calls replace the complete-chain task
group. Exact workspace addresses/sizes are retained, every other task remains
pure replay, and the graph recipe/update policy changes state compatibility
identity. Focused Python and shell contracts plus all 28 Native CTests pass.
No revision-3 NPU request has run yet, so correctness and performance remain
pending rather than projected.

Clean pushed `1e4c10a` produced the sole v15 execution bundle and frozen lock
v4 without opening an ACL device. Execution-config, execution-artifact,
readiness, and graph-contract SHA-256 values are
`b92134ce...b73f`, `86f28322...370b`, `0927abb9...c9ac`, and
`c709f1e8...f5d`; fresh eager/graph resident-plan identities are
`d2c67e9d...df635` and `d19fa58e...165b3`. All independent readiness audits
accept. These values establish an execution boundary only and add no latency,
throughput, correctness, or HBM observation.

The first v7 suite controller adds no hardware result. Its systemd service
reached the host build gate but exited 127 because `cargo` was absent from the
service PATH. No lifecycle directory was created, NPU7 stayed at idle HBM
with no process, and port 18087 remained empty. This is retained as
pre-execution custody failure evidence; fresh v8 names are required.

v8 proves the new graph path is online-correct at c1. c1/o1 returns 4/4 exact
tokens; c1/o32 returns all four 32-token sequences exactly with zero errors
and graph counters `1/123/124/0`. Its last replay rows are about 30.2 ms
total, about 1.0 ms task update, and about 29.0 ms final synchronization,
eliminating the old roughly execution-sized full-chain update cost at B1.
The suite nevertheless stops before c32 because its generic trace validator
expected schema 1 and 581 allocations on every row. That post-execution
contract failure is retained; it is not a c32 performance result.

## Revision-3 attention-only online graph result

Fresh v9 from clean pushed `4ba5bbe` completes all four NPU7 lifecycles and
passes the independent audit with zero violations. Every one of 264 requests
and 8,324 output tokens is exact. Eager/graph c32/o32 request throughput is
10.342022/9.829925 request/s and output throughput is
330.944695/314.557590 token/s. Wall P50/P95/P99 is
2568.555/3146.591/3149.315 ms versus
2691.692/3276.073/3279.324 ms; TPOT P50/P95/P99 is
66.961/79.909/79.942 ms versus 71.161/85.261/85.311 ms.

Both arms have zero errors, hit rate 1.0, 262,144 effective reused tokens,
40,544 MiB sampled peak HBM, and exactly eight B16 append plus 248 B16 decode
batches. Graph ends at capture/update/replay/rebuild `1/247/248/0` with 48
attention task groups. Median task update is 0.998 ms and total executor is
35.386 ms, down from revision-2 graph's 64.848 ms; eager is 33.484 ms.
The residual graph final-sync wall is 33.985 ms versus eager 27.134 ms.
Graph throughput remains 4.9516% lower, so the 1% default-integration gate
fails. `formal_gate_open=false`, `performance_claim=false`, and no TTFT or
vLLM claim is made. The tracked audit is
`results/qwen14b-online-graph-npu7-v9-attention-update.json` (SHA-256
`e6817227...7caa`).

## Revision-3 device-side causal diagnosis readiness

The accepted v9 host trace leaves one unresolved observation: graph final-sync
wall time is 33.985 ms versus eager's 27.134 ms, but that interval includes
queued device work. A fresh NPU7 diagnostic is preregistered to separate the
same-stream device interval from host waiting and to compare complete CANN task
traces over identical 128-request c32/o32 physical-B16 workloads.

The implementation adds optional ACL timeline events, timing schema 3, a
bounded in-container msprof attach path, fail-closed DB/CSV validation, and an
independent four-lifecycle auditor. Device-event and profiler modes are
separate scheduler telemetry identities; the rebuilt worker also changes the
execution artifact. No new artifact, request, NPU sample, task trace, latency,
throughput, or result exists yet. All formal, performance, default-integration,
vLLM, TTFT, and later-model gates remain closed.

The event-only eager and graph producers later completed, but the first
profiler producer failed before the client window: installed CANN 9.0.0
reported `Argument --dynamic=off, but --pid is set` and exited 255. Cleanup
left NPU7, port 18087, the worker, and docker-exec scope empty. The failure
contributes no profiled request or task sample. The retry changes only the
profiler CLI to explicit `--dynamic=on --pid` and uses fresh v2 profiler
lifecycle names while retaining the immutable event producers.
The v2 retry then completed profile-eager online execution and export, but
failed when the host summarizer encountered the container-root 0700 trace
directory. This is a post-execution evidence-custody failure, not an accepted
task trace. The v2 directory remains immutable; fresh v3 profiles add a
recorded ownership handoff after export.

## Accepted revision-3 device-side causal diagnosis

The final offline audit of the two immutable event-only v1 producers and two
profiled v3 producers passes every correctness, B16-shape, graph-counter,
identity, trace, custody, and cleanup check. Every arm serves 128 requests and
4,096 exact oracle tokens with zero errors, hit rate 1.0, 262,144 effective
reused tokens, eight B16 append batches, and 248 B16 decode batches. Graph
finishes at capture/update/replay/rebuild `1/247/248/0` with 48 groups.

Event-only eager/graph reaches 10.265483/9.833467 request/s and
328.495458/314.670956 output token/s. Device interval median is
32.898791/34.983792 ms, proving that graph's residual is device-visible rather
than final-sync accounting. Graph remains 4.2084% lower in request throughput.

Raw profiler TASK count is 200,153/307,985, but named compute count is
identical: 74,705 AI-core, 12,336 mixed-AIC, and 100,148 AI-vector rows in
each arm. The graph-only rows are the model-RI control envelope: 248 model
executes and notify pairs, 95,232 near-zero NOPs, and 11,856 update copies.
The notify wait spans internal stream-5 compute and is not additive. Thus the
accepted causal branch is
`model_ri_control_envelope_without_duplicate_compute`, not duplicated model
arithmetic.

The current CANN contract offers no safe removal: 48 single-operator FIA
groups are required to update per-layer host-backed sequence lengths, and the
capture mode does not change execution scheduling. No execution repair is
integrated. The tracked audit is
`results/qwen14b-online-graph-device-profile-npu7-v3.json`; raw DB/CSV,
request/response, logs, and lifecycle records remain under the hash-bound
directories recorded by its custody manifest. Graph remains default-off with
`formal_gate_open=false`, `performance_claim=false`, and no TTFT/vLLM claim.

## Isolated carrier readiness after the hybrid failure

No new accelerator result is reported. Hybrid v1 still exited 137 after its
externally owned shared container disappeared, with empty stdout/stderr, no
logits, and no observed NPU7 execution. The repair freezes a project-owned
NPU7-only carrier at identity `800a85a6...2247`, adds live-inspect equality,
exact-owned cleanup, disconnect-resilient non-restarting custody, and records
the carrier identity in candidate metadata.

Six software tests pass: deterministic create arguments, tag/content-ID
binding, NPU7 isolation, live-inspect normalization, ordinary mutation
rejection, and rejection of a rehashed mutation that adds NPU4. No container
was created, no model or ACL code ran, and no NPU was consumed. Correctness,
latency, throughput, HBM and comparative fields remain unavailable.

Before the fresh v2 diagnostic, readiness is strengthened without adding a
hardware sample. Carrier identity `800a85a6...2247` now includes exact
compiler, runner, and submitter source digests and invalidates
`5c70fbe7...09a5`. The isolated path also requires the complete Native CTest
suite inside the accepted live container before candidate execution. This
changes admission/custody only; no decode result or performance field exists
yet.

## PTO-online NPU7 v1 resource-race rejection

The frozen v1 PTO-online diagnostic was submitted exactly once from clean,
pushed commit `ae5a9ea4b9c7b0ae79dd355564d30488a96f5061`. Host readiness observed
NPU7 and port 18087 free, but the isolated supervisor then found an external
process (`PID 2392721`) on NPU7 and rejected admission. The project container
was never created, CTest never started, neither candidate nor control started,
no request was issued, and port 18087 remained unused.

The immutable raw custody is
`results/qwen14b-native-pto-online-npu7-v1-controller/`; its evidence-manifest
SHA-256 is `cdfc407475043faa5903cc644171ee735331fb113fa4cc5a88ea65984b3fafe5`.
The independent accepted post-hoc audit is
`results/qwen14b-native-pto-online-npu7-v1-preflight-resource-race-audit/audit.json`
with SHA-256
`dde113734d2ae7afb8c76a682f4d762fbd4714ae7a3d56a68ba0e7d45ff5854a`.
It classifies `diagnostic_hardware_execution=false`,
both `diagnostic_arms_started` values as false, and
`eligible_for_comparison=false`.

The raw controller's legacy `hardware_execution=true` means only that a
hardware-scoped submission reached the isolated supervisor. It is not evidence
that project code executed on the NPU. Correctness, latency, throughput,
under-load HBM, and the PTO-versus-ACLNN comparison are unavailable.
`formal_gate_open=false`, `performance_claim=false`, and the TTFT boundary is
unchanged. The v1 namespace is immutable and must not be retried.

## One-command new-server recovery gate

No new accelerator result is reported. A tracked recovery contract and
fail-closed bootstrap now reconstruct the repository/submodule state and audit
the untracked Qwen2.5-14B packs, full-model/decode oracles, historical PTO v1
metadata, pinned container bytes, host runtime paths, disk, NPU7, and port
18087. The report distinguishes software readiness from hardware idleness and
preserves the fresh-v2 requirement after the immutable v1 resource race.

Five contract tests cover oracle tampering, layer/global pack verification,
busy-device classification, authority/milestone preservation, and the
non-executing wrapper boundary. This is software-only recovery evidence: no
container was started, no model code ran, no NPU was consumed, and no
correctness or performance value changed. `formal_gate_open=false`,
`performance_claim=false`, and the TTFT boundary remains closed.
The recovered portable Tectonic path also rebuilds the paper with a fixed
default `SOURCE_DATE_EPOCH`; two consecutive builds produced the same PDF
SHA-256. This is artifact reproducibility only.

## PTO-online v2 software and preregistration repair

No new accelerator result is reported. A fresh v2 preregistration and runner
namespace replace hard-coded v1 paths without modifying or retrying the v1
custody. The auditor now receives the exact carrier explicitly, and the new
artifact-build container is required to be non-privileged with no NPU device
grant. Contract tests cover fresh names, phase-qualified execution evidence,
post-carrier stability probes, carrier binding, and the device-free build
boundary.

At preparation time NPU7 remained owned by an external
`g4c_b4_epoch_runner`, so no project container, CTest, model execution, or
request began. This entry is software-only lifecycle preparation and adds no
correctness, latency, throughput, HBM, or comparison value.
`formal_gate_open=false`, `performance_claim=false`, and TTFT comparison
remains forbidden.

## PTO-online v2 carrier-inspect rejection

The v2 unit was submitted exactly once from clean pushed lock commit
`d6efa80d72eb88de8cf7ac590ccd21738426515d`. Four host probes observed NPU7
free before submission. The isolated carrier was created and started, but live
audit rejected the daemon response because `ImageManifestDescriptor` was
null. Native CTest, the diagnostic stage runner, candidate, control, model
execution, and requests never started.

Cleanup removed the exact v2 container with exit zero; subsequent inspect
returned `no such object`, NPU7 was free before and after, and port 18087
remained unused. The accepted independent audit is
`results/qwen14b-native-pto-online-npu7-v2-carrier-rejection-audit/audit.json`.
It classifies `diagnostic_hardware_execution=false`, correctness and
performance unavailable, and comparison ineligible. v2 is immutable and must
not be retried.

The uniquely evidenced v3 repair permits frozen architecture/OS fallback only
under exact image content-ID equality. It is software lifecycle repair, not a
result. Formal, performance-claim, production-integration, later-milestone,
and TTFT gates remain closed.

## PTO-online v3 host-toolchain rejection

v3 passed exact carrier audit, two stability probes, and Native CTest. It then
entered the candidate stage but exited 127 at the host-side Cargo build because
the transient service PATH omitted `/home/shuhao/.cargo/bin`. No worker,
model, ACL/NPU process, request, or candidate result started; control was not
entered. Cleanup removed the exact container and released NPU7/port 18087.

The accepted independent audit is
`results/qwen14b-native-pto-online-npu7-v3-host-toolchain-rejection-audit/audit.json`.
Under the frozen phase semantics it records diagnostic-stage execution true,
while separately recording `model_execution_started=false`, correctness and
performance unavailable, and comparison ineligible. v3 is immutable.

Fresh v4 binds Cargo/Rustc paths and executable bytes and injects the fixed
toolchain directory into systemd PATH. This is lifecycle repair only; formal,
performance, production, TTFT, and later-milestone gates remain closed.

## PTO-online v4 binary-plan rejection

v4 passed carrier, stability, CTest, Cargo, and resident-plan inspection. The
candidate worker then rejected before ACL/NPU initialization because the
generic launcher rebuilt the executor with an all-zero decode-plan identity
and empty project-kernel closure. Candidate emitted no request/result; control
did not start. Cleanup removed the exact container and left NPU7/port free.
v4 is immutable and supplies no correctness or performance datum.

Fresh v5 passes the frozen decode-plan, project-kernel file list, and PTO
lowering-closure identities into the runtime build. Its sole candidate
lifecycle later passed exact-output validation but failed the frozen physical
B16 cohort contract; the control did not run. All claim gates remain closed.

## PTO SwiGLU standalone software readiness

No new accelerator result is reported in this entry. The official-derived
fixed Qwen2.5-14B SwiGLU kernel now has a host component runner, deterministic
BF16 input generator, independent CPU oracle, raw ACL event timing, a frozen
NPU7 preregistration, and an exact-container lifecycle wrapper. The input
identity is `c8f620197d0f...500efb7`.

Software-only tests accept the frozen generator and a synthetic exact-oracle
fixture. A device-free, network-disabled CANN 9.0.0 container builds both the
AICore shared object and host executable; the shared object contains
`.aicore_binary`, and all host dynamic dependencies resolve. No NPU code has
yet executed for this lifecycle, so correctness, PTO-versus-ACLNN latency, and
the mechanism effect are unavailable. `formal_gate_open=false`,
`performance_claim=false`, and TTFT comparison remains forbidden.

## PTO SwiGLU standalone v1 ACL initialization rejection

The clean pushed v1 lifecycle created the NPU7-only, non-privileged,
network-disabled carrier, passed both idle-device stability probes, and built
the kernel and host runner. The ACLNN process then returned
`aclInit=500000`; its only additional diagnostic was
`DrvMngGetConsoleLogLevel failed. (ret=4)`. No ACLNN operator or PTO kernel
started, so correctness, timing, and comparison are unavailable.

Cleanup removed the exact non-restarting container with exit zero and left
NPU7 at its 3,445 MiB no-process baseline. Preserve the raw v1 directory and
its manifest SHA-256 `e107113c...4b64`; never retry it. Fresh v2 separates a
device-free build carrier from the repository's already established
ACL-capable CANN 9.0.0 runtime carrier and retains debug process logs. All
formal, performance, production, and TTFT gates remain closed.

## PTO SwiGLU standalone v2 device-visibility rejection

v2 successfully separated and audited a zero-device build carrier and an
NPU7-only runtime carrier. Before the ACLNN process, however, its runtime
shell sourced ATB environment setup. That setup imported Torch and made the
pre-arm boundary device-active. The retained CANN debug stream then showed
`drvGetDevNum` returning zero devices and driver error 87; physical NPU7 had
not been mapped through the Ascend visibility variables to logical ACL device
0. `aclInit` again returned 500000. Neither operator started.

An external `VLLMEngineCore` from container `32c5f946...3e4` also acquired
NPU7 after the stability window. During post-run diagnosis PID 537529 was
incorrectly attributed to the project container and terminated; later cgroup
inspection proved the error. This incident is explicitly retained in the v2
failure audit. Future cleanup may signal only a PID whose cgroup exactly
matches the project-owned container ID.

The raw v2 evidence manifest SHA-256 is `e4dff860...374da`. v2 is immutable
and supplies no correctness or performance value. Fresh v3 removes ATB/Torch
setup, sets both visibility variables to physical 7, calls ACL logical device
0, and requires NPU7 idle immediately before and after every arm. All claim
gates remain closed.

## PTO SwiGLU standalone v3 sourced-environment rejection

v3 froze both visibility variables and logical device 0, but inspection during
the live lifecycle proved that the vLLM runtime image's CANN setup script still
spawned Python/Torch probes. Its image entrypoint also spawned a Torch probe
under the otherwise inert keeper. NPU7 remained at the no-process baseline,
yet ACL again returned driver error 87 and zero devices before either
operator. v3 is therefore a sourced-environment rejection, not kernel
evidence.

The raw v3 manifest SHA-256 is `32462985...86d0`; exact container cleanup
passed. Fresh v4 overrides the image entrypoint with `/bin/bash`, sources no
environment script, freezes visibility and `SOC_VERSION` in the container
environment, and directly executes the component binary. Workload and gates
are unchanged.

## PTO SwiGLU standalone v4 device-node rejection

v4 successfully removed all profile, entrypoint, sourced-script, and Torch
side effects. The host component was directly executed with the frozen
environment, but `aclInit` still returned 500000 before either operator.
Because the only accelerator node was still named `/dev/davinci7` inside the
container while ACL initialization probes logical device 0, the active
boundary is now device-node numbering.

The raw v4 manifest SHA-256 is `66ad9f0e...8a49`; cleanup left NPU7
process-free. Fresh v5 maps only host `/dev/davinci7` to container
`/dev/davinci0`, sets container visibility to 0, and separately binds
`STATECENTRIC_PHYSICAL_NPU=7`. No other host accelerator is exposed. All
workload and claim gates remain unchanged.

## PTO SwiGLU standalone v5 permission rejection

v5 mapped host physical `/dev/davinci7` to container logical
`/dev/davinci0`, froze visibility 0, and separately verified physical NPU7.
`aclInit` still returned 500000 before either operator. Device-node naming is
therefore excluded. The remaining difference from the repository's successful
Ascend runtime carriers is permission mode: those carriers and the running
vLLM services use `Privileged=true` with `label=disable`, whereas v1--v5 were
non-privileged.

The raw v5 manifest SHA-256 is `5199de0b...5a9f`; cleanup left NPU7
process-free. Fresh v6 adopts that established carrier permission contract
while retaining direct exec and `ASCEND_*_VISIBLE_DEVICES=7`, which maps
logical device 0 to physical NPU7. No workload or claim gate changes.

## PTO SwiGLU standalone v10 completed correctness rejection

v10 crossed the previous device-noncompletion boundary: all four arms
completed. ACLNN matched the independent CPU oracle exactly. PTO copy returned
in 0.007340 ms median but had 220,995 bit mismatches; PTO cast-copy returned in
0.039840 ms median with 221,183 mismatches; complete PTO returned 200 samples
with 0.023040 ms median but had 221,183 mismatches and maximum absolute error
16.75. The independent auditor rejected the lifecycle, so the apparent
0.762153 ACLNN-over-PTO median ratio is not performance evidence.

The failure is consistent across the isolation arms with explicit
synchronization being absent: the build enabled automatic PTO passes while
calling the pinned official manual event helper, and that helper is empty
under `__PTO_AUTO__`. Exact-container cleanup passed and NPU7 returned idle.
Fresh v11 disables the automatic pass and preserves the manual event calls.
All formal, production, performance-claim, and TTFT gates remain closed.

## PTO SwiGLU standalone v11 control timeout

v11 built the manual-synchronization kernel successfully (SHA-256
`3a0c7a11...9d65`) but the unchanged ACLNN control process exceeded the
30-second process-level allowance without stdout or stderr. No PTO arm
started. The exact project container was removed and NPU7 returned to its
process-free 3,445 MiB baseline. Fresh v12 expands only the ACLNN allowance to
90 seconds and preserves the 30-second PTO deadlines. v11 contributes no
correctness or performance sample.

## PTO SwiGLU standalone v12 accepted mechanism result

The single clean-pushed v12 lifecycle completed all four arms and passed
independent audit without violations. PTO copy and BF16--FP32--BF16 cast-copy
were bitwise exact. ACLNN and complete PTO each matched the independent CPU
oracle exactly over 221,184 BF16 outputs, with zero nonfinite values and zero
maximum absolute error.

For 200 device-event samples, ACLNN had p50 0.027240 ms, mean 0.027737 ms, and
p95 0.048499 ms. PTO had p50 0.022380 ms, mean 0.024093 ms, and p95
0.051241 ms. The preregistered median ratio is 1.217158x, so
`mechanism_effect_observed=true`. Raw evidence-manifest file SHA-256 is
`433a63a...c6e24a`, and audit JSON SHA-256 is `0c53f869...5ac5f`.
This is an accepted standalone fixed-shape operator mechanism result;
`formal_gate_open=false`, `performance_claim=false`, and TTFT comparison is
still forbidden.

## PTO SwiGLU matched real-hardware profile

The repaired profile v2 completed matched ACLNN and PTO arms under CANN
`msprof` task-based `PipeUtilization` collection. Independent audit accepted
both arms with no violations. Each contains 220 matched compute rows and 624
executable task-timeline rows; ACLNN records 3,430 CANN API rows and PTO 1,879.
Both outputs have SHA-256 `f1d0d205...5c863`, exactly matching accepted v12
and the CPU oracle.

The ACLNN `SwiGlu_3_high_performance_27` row reports median task duration
10.1 us, MTE2 70.4%/5.423 us, vector 8.5%/0.651 us, scalar 24.8%/1.913 us,
and MTE3 2.8%/0.219 us. The project PTO row reports 6.1 us, MTE2
19.5%/0.795 us, vector 24.7%/1.011 us, scalar 35.6%/1.455 us, and MTE3
20.2%/0.826 us. This explains v12 as a shift from ACLNN's load-dominated row
to a more balanced manual load/compute/store pipeline. Because profiler
instrumentation perturbs execution, these durations are diagnostic only and
are not a second performance comparison.

## Qwen2.5-14B physical-B32 decode component accepted

The NPU7 B32 lifecycle completed six fresh full-model component processes and
passed independent audit without violations. Every process produced 32 exact
oracle tokens and certified frozen decisions, finite logits, correct
9,732,096-byte raw-logit output, and clean NPU/process/port release. The
deployment used state capacity 33, 80 physical KV blocks, and a 10-GiB
workspace arena; observed workspace peak was 5,444,805,120 bytes and minimum
post-execution free HBM was 12,651,876,352 bytes.

Fused ACLNN Gate/Up plus ACLNN SwiGLU has a 32.410655-ms median, below both the
preregistered 57.7-ms primary gate and 35.85-ms stretch gate. This accepts the
B32 component mechanism and authorizes a fresh Native-only online
B16-append/B32-decode control-candidate lifecycle. It does not enable the
online path by itself. The tracked result is
`results/20260728-qwen14b-b32-decode-component-npu7-v1/summary.json`;
`formal_gate_open=false`, `performance_claim=false`, and TTFT comparison is
forbidden.

The authorized online follow-up is now software-preregistered but has not run.
The tracked request/runner contract expresses two B16 prefill cohorts sharing
one atomic B32 decode-group identity, and scheduler-plan v11 closes that
policy into the state digest. No online throughput or latency number is added
by this software state.

The v29 control and v30 candidate artifacts have now been generated without
device access and independently accepted. Their execution config
(`df43e3f6...fd382`), execution artifact (`855bcce4...119b5`), and resident
plan (`374b36cb...fe534`) are identical. The control binds scheduler-plan v10
(`cdd4d7db...a9cd3`); the candidate binds v11
(`18d88566...cf9a`). This is readiness evidence only; no online arm has run.

The first v1 hardware submission stopped before the stage runner: carrier
creation and idle checks passed, but the Native CTest gate reported 30/32.
Both failures were stale source-text contracts that still described the
superseded NPU0-only Gate/Up runner and 1,536-element auto-pass SwiGLU kernel.
No model, request, correctness, or performance arm started; exact-container
cleanup restored idle NPU7. The immutable evidence is under
`results/qwen14b-native-b32-online-npu7-v1-controller/`.

The fresh v2 submission likewise stopped before the stage runner with Native
CTest at 30/32. Exact-container tracing showed that the remaining failures
were test-only: an obsolete literal-NPU0 auditor assertion, an incorrectly
unescaped generated-JSON source assertion, and a partition fixture still
expecting the superseded 54-KiB double buffer instead of the accepted
single-stage 13,824-byte UB footprint. No model, request, correctness, or
performance arm started. Exact-container cleanup restored idle NPU7; immutable
evidence is under
`results/qwen14b-native-b32-online-npu7-v2-controller/`.

Fresh v3 software custody is now frozen against clean pushed repair commit
`4ac811c`. Its preregistration preserves the v2 workload byte-for-byte at the
semantic level, and its new carrier/runner/auditor names prevent evidence
aliasing. The two affected CTest entries pass inside the carrier image; this
is readiness evidence only and adds no online result.

The v3 submission passed exact-carrier CTest 32/32, then stopped before
Cargo, model initialization, or requests because the ignored local
prompt-family working copy was absent. The identical frozen bytes are present
in a tracked accepted result and match SHA-256 `944c51b...731fe`. Cleanup
restored idle NPU7. This is migration/readiness evidence only, with no online
correctness or performance observation.

Fresh v4 custody now binds the atomic tracked-byte restoration helper and a
new carrier/runner/auditor namespace to clean pushed repair commit `a979dd7`.
The restored destination is ignored local working state; the authoritative
source remains the tracked result and its frozen SHA. No accelerator result is
added by this readiness repair.

The v4 submission passed CTest 32/32, prompt restoration, and Cargo, then
stopped before model initialization at oracle admission. The launcher
incorrectly compared the historical independent-oracle producer container to
the fresh serving carrier. No request or accelerator execution occurred;
cleanup restored idle NPU7. This is provenance-gate failure evidence, not an
online result.

Fresh v5 custody is now frozen against clean pushed provenance-repair commit
`a51df72`. It changes only the oracle/serving provenance admission rule and
fresh lifecycle identities; frozen oracle bytes, workload, artifacts, and
six-arm protocol are unchanged. This is readiness evidence only.

v5 completed control-1 and candidate-1 with 128 requests, zero request errors,
and exact outputs, then stopped before pair 2 because the generic client
post-validator applied legacy B16 formulas to the candidate. Control-1
measured 8.137208405 requests/s with 248 B16 decode batches; candidate-1
measured 11.105147278 requests/s with the preregistered 124 B32 decode batches.
These are incomplete 1/3-pair diagnostic observations only, not an accepted
mechanism result. Cleanup restored idle NPU7.

Fresh v6 custody is prepared against clean pushed telemetry-repair commit
`9fbbd20`. In addition to the phase-aware B16 append/B32 decode checks, its
lock explicitly binds the shared-prefix benchmark client SHA-256. It changes
no model, request, oracle, artifact, arm order, metric, or threshold. This is
readiness evidence only; v6 has no hardware result until its one permitted
submission completes.

v6 then completed its sole permitted NPU7 submission from clean pushed
`4371c26`. All six fresh lifecycles served 128/128 oracle-exact requests with
zero errors. Control request throughput was 8.053526, 7.970002, and 7.740457
requests/s; candidate throughput was 11.430122, 11.810337, and 10.407514
requests/s. The three paired gains were 41.9269%, 48.1849%, and 34.4561%;
their median was 41.9269%, so every pair and the preregistered 10% mechanism
gate passed. Every control recorded eight B16 append plus 248 B16 decode
batches; every candidate recorded eight B16 append plus 124 B32 decode
batches. The independent auditor accepted all arms with zero violations.

This closes the projected B32 mechanism question with real online evidence,
but not the cross-runtime performance gap. The candidate median was 11.430122
requests/s. For context only, that is 23.94% below the separately accepted
15.0274-requests/s pinned-vLLM diagnostic on another lifecycle/card. This is
not a formal paired comparison: `formal_gate_open=false`,
`performance_claim=false`, and TTFT comparison remains prohibited. Carrier
custody captured idle NPU7 and exact-container removal at lifecycle end; an
unrelated vLLM service began using NPU7 afterward and is not project residue.

An offline critical-path decomposition of the immutable v6 timing telemetry
locates the next bottleneck above the NPU executor. In candidate-1, the 132
measured executor intervals total 7.986 seconds, already below the 8.518-second
end-to-end budget corresponding to 15.0274 requests/s. Gaps from one executor
completion to the next executor start total 2.718 seconds: 1.662 seconds across
120 decode-to-decode transitions, 0.950 seconds across three
decode-to-prefill wave transitions, and 0.105 seconds across append/decode
transitions. The median B32 decode executor interval is 41.769 ms, while the
median decode-to-decode host gap is 12.311 ms. This shows that closing the
contextual vLLM gap requires removing serialized host dispatch work in
addition to any kernel tuning.

Fresh software therefore makes admission-stat caching an explicit,
default-off runtime option. When enabled, capacity-stable decode batches reuse
the last validated executor snapshot. Prefill, a decode that allocates a new
KV block, request completion, eviction, or cancellation forces a fresh worker
query before the next plan. New counters expose refreshes and cache hits.
This code has only CPU/mock-backend evidence: 121 Rust library tests,
all-target compilation, launcher syntax, and 28 client/launcher tests pass.
It is not a hardware result and does not change any v6 number.

Fresh offline custody code now binds this option through scheduler-plan v12.
The control and candidate artifact recipes both retain B16 append, B32 decode,
the v6 model/workload geometry, and eager ACLNN execution; their only intended
scheduler input difference is cache `0` versus `1`. The independent digest
test proves those values produce different v12 state identities, while
recomputation of the accepted v30 record proves the historical v11 digest is
unchanged. No v31/v32 artifact or accelerator result is claimed here.

The fresh v7 diagnostic protocol is now software-preregistered. It freezes
three alternating cache-off/cache-on pairs, requires identical B32 batch
histograms and exact outputs, and makes refresh/cache-hit deltas part of
acceptance. Its 5% paired-median threshold was fixed before artifact generation
or hardware execution. This is preregistration evidence only; no v7 lifecycle
or NPU observation exists yet.

The no-device artifact preparation completed for both arms. v31 control and
v32 candidate share execution-config SHA-256 `df43e3f...fd382`, execution-
artifact SHA-256 `855bcce...19b5`, and resident-plan record SHA-256
`6cff4fe...3f5c`. Both independent state audits accepted scheduler-plan v12.
Control binds cache 0 with scheduler digest `69679a5...1194`; candidate binds
cache 1 with `0e5364c...9d6d`. The generated v7 carrier and pair lock validate
these identities. This is derived-artifact/readiness evidence, not hardware
execution or a throughput result.

Recovery contract v2 was then exercised in full offline mode on clean pushed
`8bcc7c9`. The byte-level report accepted with zero violations and classified
`ready_for_software_work=true` and `migration_complete=true`. It separately
reported `hardware_idle=false` and
`ready_for_hardware_preflight=false` because NPU7 remained externally
occupied. This is recovery/readiness evidence only and adds no accelerator
measurement.

## Server-180 frozen-v7 recovery rejection

Server 180 fast-forwarded cleanly to authoritative commit `6980f16`. A full,
non-quick `scripts/bootstrap_new_server.sh --offline` audit then rejected with
exactly `docker_image` and `local_artifacts`; its ignored raw report has
SHA-256 `f2654655...2b43`. The 25-GiB layer pack, 3-GiB global pack, both
oracle families, and model identity passed full content verification. The only
missing local records are the six required files in each of the ignored v31
control and v32 candidate artifact directories.

The Docker rejection is an identity-representation mismatch. The frozen v7
content ID is arm64 config digest `sha256:0fc116f...10731`; Docker 29.1.3 with
the containerd store reports OCI index digest `sha256:105834a...ce13` as
`.Id`, and the selected arm64 manifest `sha256:36194fe...c73b` refers to the
frozen config. API compatibility modes and an immutable-digest pull did not
change that result. NPU7 and port 18088 were idle, but
`migration_complete=false` and `ready_for_hardware_preflight=false`, so the
tracked submitter was not invoked. No container, CTest, worker, model, request,
or accelerator phase started; this is recovery-failure evidence only and
provides no correctness, throughput, latency, memory, or comparison datum.

## Server-180 v7 recovery completion and pre-arm rejection

The missing v31/v32 records and exact Docker archive were subsequently
recovered from server 112. The artifact archive SHA-256 is
`3872069522541513933e3be351c8bd478ceb1e2e7738be3590da03b6a3112726`;
the 18,590,010,880-byte Docker-save archive SHA-256 is
`4603a3ab15072208ce51646f9f380177d744bbc50951b67c157f146f3f4fc01c`.
An isolated classic Docker store exposed the frozen config ID without
changing the shared Docker store. Full Recovery-v2 then accepted with zero
violations; its report SHA-256 is
`0c3a8a5a2a03f9d1af9cb272b03d1d5e3fa354050f47adb45e2035e8aca3cef`.

The tracked v7 submitter was called exactly once from authoritative commit
`dc810dd`. Carrier custody and live-image identity passed, and the native
suite passed 30/30. Before model or worker startup, the stage runner compared
the freshly built server SHA-256 `294ef03...a57b` with the frozen
`bf60456...d644` and exited 2 with the exact binary-drift rejection. No arm
directory, request, model load, port listener, or accelerator execution was
created. Consequently correctness, request/s, output token/s, latency, TPOT,
error rate, state-hit rate, reused tokens, and peak HBM are all `n/a`.

The frozen six-arm auditor also exited 1 with `KeyError: 'arm'` when presented
with the absent-arm lifecycle. Its stdout, stderr, and exit code are retained
as audit-coverage evidence. A separate fail-closed pre-arm auditor and two
contract tests now encode this negative-result class without modifying the
frozen performance auditor. Run from clean pushed `59c0ea1`, that auditor
accepted the lifecycle only as negative evidence with all 13 checks true,
zero violations, zero arms, no requests, and no hardware execution. Its
report SHA-256 is
`b0ba9fcecb19977a0fc1e51a90fddf2b86ded62c2bc9b1b691ee87b02d4d0581`;
the final 100-file evidence manifest SHA-256 is
`96cd29f9297b424a04b1daf10ea2ac48d9d620d5f6df76966e93a1f2fc5be531`.
Unrelated session-token values captured by the two full-machine process
snapshots were deterministically redacted before publication, and
command-generated trailing whitespace was removed.
The v7 unit, container, daemon, socket, manager environment, process names,
and port were absent at final cleanup. NPU7 was idle in the captured v7
postflight; a later unrelated `ascend-control-cruise` container acquired it,
and was identified but not disturbed.
Formal, performance, comparison, and TTFT gates remain closed.

## Post-v7 reproducible-executable diagnostic

Source-history inspection found no Rust, Cargo, native CMake, or Cargo.lock
change between the v7 artifact parent and the failed server-180 build. Two
independent current-host builds were byte-identical, while Rust 1.95, Rust
1.96, Ubuntu/Rust 1.97, openEuler/Rust 1.97, and different source paths
produced distinct ELF files. The v7 lock had `host_toolchain=null`; the
specific historical producer therefore cannot be reconstructed from its
identity record.

The successor bundle mechanism built three Rust executables twice in fresh
target directories. The latest diagnostic bundle audit accepted identity
`3c3609a...50abb`; its server is `500e1a...b8a4`, Build ID
`45b81d...02d`, and runtime-dependency identity `77f0485...5fb64`. A live
registry check independently verified OCI index `105834a...ce13`, selected
arm64 manifest `36194f...c73b`, and config `0fc116f...10731`.

These are software-only reproducibility and identity results. They predate the
required clean-pushed artifact freeze, started no worker, request, model, or
NPU work, and provide no throughput, latency, TTFT, memory, correctness, or
Native-versus-vLLM comparison result.

The first bundle attempt after the clean software push exposed one more
reproducibility bug before freeze. All three ELF records and the normalized
dependency-content identity were unchanged, but the overall manifest differed
because it included a hash of raw `ldd` output containing a temporary binary
path and ASLR addresses. That intermediate bundle is rejected. Bundle
identity now retains only normalized dependency names and content hashes.

The clean-pushed repair subsequently produced the same bundle in four builds
across two builder invocations. The eligible ignored bundle identity is
`63adcc2...3eae`; its server remains `500e1a4...b8a4`, its normalized
runtime-dependency identity remains `77f0485...5fb64`, and its manifest
SHA-256 is `c7eb9ae...aa60`.

The successor also closes the resident C++ build boundary. Scheduler-plan v14
adds a typed producer identity over the closure compiler, CMake/native inputs,
CMake cache/compiler/link records, actual Make/Ninja tool, compiler/linker
bytes, executor ELF, and normalized runtime libraries. Contract tests exercise
tamper rejection and require current-environment recomputation. No final C++
closure, v33/v34 artifact, carrier, pair lock, container, request, or NPU
execution has yet been admitted, so this remains software-only readiness
evidence and all online metrics are `n/a`.

From clean pushed `7b9491d`, a fresh device-free carrier reproduced the C++
closure twice from empty fixed build paths. Both complete closure records were
byte-identical at SHA-256 `0e35478...a681`, identity
`f8924a8...d37db`, and executor SHA-256 `b5a44b0...14268`; both state
audits and live `--audit-current` recomputations accepted. The carrier used
the exact config image `0fc116f...10731`, `network=none`,
`privileged=false`, no Devices or DeviceRequests, and read-only driver/install
metadata solely to satisfy link dependencies.

Two pre-measurement failures are retained as engineering evidence. Root with
all capabilities dropped could not traverse the user's mode-0700 home mount,
so the carrier was recreated under the matching UID/GID. The next build
reached linking but rejected because the device-free carrier had not mounted
the read-only host driver library closure (`libascend_hal.so`); adding those
read-only libraries fixed linking without granting accelerator devices.
Neither failure nor either accepted rebuild initialized a worker, model,
request, port, or NPU.

The first v33/v34 wrapper invocation from `fd2b8f1` generated an accepted
device-free v33 control artifact, then rejected before v34 because the new
pair audit loop was placed before the candidate builder call. The exact
failure named the absent v34 C++ closure. The orphan v33 is not eligible for
freezing and was removed after recording readiness SHA-256
`e862f59...f9360` and state-record SHA-256 `c597a9b...e15c`; the ordering
repair requires its own clean push
before both artifacts are regenerated. This is a software orchestration
failure with no container recreation, worker, request, port, or NPU work.

The accepted regeneration from clean pushed `0446d2c` produced both v33 and
v34. Execution config `df43e3f...fd382`, execution artifact
`855bcce...19b5`, resident plan `6cff4fe...3f5c`, Rust binding
`f5727fe...01e9`, and C++ closure `0e35478...a681` are common. Scheduler
v14 changes only the cache bit from 0 to 1, yielding control state
`c315229...87c8` and candidate state `0358688...9327`; both state audits
accept.

From clean pushed `7c6613f`, the first typed carrier and pair lock were frozen.
Carrier record SHA-256 was `8f79cdf...0332`, carrier identity
`0392afb...9423`, and lock SHA-256 `215c28f...ea13`. The lock bound the new
composed offline-readiness auditor at `91b5642...6ff3`. These records were
later invalidated and removed after the submitter implementation changed;
they remain device-free historical readiness evidence and add no online
result.

From clean pushed `39db504`, the composed offline-readiness auditor accepted
all 58 checks with no violations. The first saved audit SHA-256 is
`c0691e5...b952`; it records both arms, exact one-factor state divergence,
`hardware_execution=false`, and closed formal/performance/TTFT gates. This
audit identified and prompted correction of a documentation-only stale
preview carrier identity; the carrier and lock themselves both already bound
the final `0392afb...9423` identity.

Two NPU7/port admission samples were stable and idle, but no submission was
made: pre-submit supervisor inspection found that the v8 submitter did not
propagate the isolated Docker socket into its transient systemd unit. The
durable runner would therefore fall back to the shared daemon and its
different image-ID representation. This is a pre-submission software blocker;
the submitter, carrier, lock, and offline audit must be clean-pushed and
refrozen before resource admission is repeated.

The submitter repair was clean-pushed as `89cca3f`, and the current frozen
carrier/lock were regenerated from that boundary. Carrier record SHA-256 is
`e9f99b8...f1e51`, carrier identity `ae49eab...eab13`, and lock SHA-256
`cf0735e...00e91`; submitter SHA-256 is `1e27c99...973ed`. The v33/v34
artifact identities are unchanged. This is still software-only custody with
no request, worker, model load, or NPU execution.

From clean pushed `298031e`, the regenerated composed readiness audit accepted
all 58 checks with no violations; its SHA-256 is
`8865202...32ee`. Two fresh pre-submit samples found physical NPU7 idle at
3412 MiB baseline HBM, no device process, port 18088 free, no v8 unit or
container, and every controller/arm namespace absent.

The single authorized v8 submission then verified the isolated Docker socket,
created the exact NPU7-only carrier, accepted both current C++ producer
closures, and passed all 32 Native CTests. The first control arm failed before
runtime initialization: the launcher forwarded scheduler identity bit `0` to
Clap's boolean environment parser, which accepts only `false/true`. The server
exited 2, launcher and arm exited 1, health remained empty, port 18088 never
listened, no request or decode-timing record exists, and NPU7 remained idle.
No candidate or later arm was materialized.

The ordinary six-arm auditor correctly rejects the incomplete suite and
reports unknown custody for the partial control arm. A purpose-built
postmortem auditor uses the exact parser failure and resource/process evidence
to classify the lifecycle as `hardware_execution=false`,
`model_runtime_initialized=false`, zero requests, and accepted negative
evidence. All 14 checks pass with no violations; report SHA-256 is
`2b47823...d6b12`. Controller result SHA-256 is
`af071cb...5efa5`, and its final 93-file evidence-manifest SHA-256 is
`6cc0f58...1d19`.

The repair retains numeric `0/1` in scheduler/artifact identity and converts
only the Rust process environment to `false/true`. Its changed generic
launcher digest strictly invalidates v8. No rerun is permitted in this
namespace. Request/s, output token/s, P50/P95/P99, TPOT, error rate, state-hit
rate, effective reused tokens, and peak online HBM are all `n/a`; formal,
performance, and TTFT gates remain closed.

The v9 software skeleton adds no online result. Its direct frozen-binary
regression accepts `false` and `true` through Clap parsing and reaches the
deliberately missing execution-config boundary; the same binary rejects
numeric `0` at the exact boolean option. The probe reports
`hardware_execution=false`, and the full Python suite passes 358 tests with
seven conditional skips. v33/v34 and every model/Rust/C++/OCI identity remain
unchanged. Carrier/lock freeze and any NPU7 submission require a later clean
pushed commit.

The single v9 NPU7 lifecycle completed three control/candidate pairs. All
768 requests and 24,576 generated tokens matched the frozen independent
oracle; error rate was zero, state-hit rate was 1.0, each arm reused 262,144
tokens (2,048/request), append batches were `{"16":8}`, decode batches were
`{"32":124}`, and peak HBM was 44,658 MiB. Control request/s was 14.4462,
14.5348, and 14.5441; candidate request/s was 14.5206, 14.4782, and 14.6150.
Paired gains were +0.5155%, -0.3897%, and +0.4874%, with paired median
+0.4874%, far below the preregistered +5% threshold.

The cache mechanism itself activated: every control had 136 refreshes/0 hits,
while every candidate had 12 refreshes/124 hits. The frozen auditor rejected
because it asserted that admission polls must equal the 132 executing
batches; raw metrics show 136 polls = 132 executing batches plus four
non-executing scheduling polls. Its SHA-256 is `f4a838c...f7ef` and remains
rejected. The separate outcome audit accepts the exact failure explanation,
six-arm correctness, and cleanup with SHA-256 `df1fd72...d21fb`, while
retaining `frozen_suite_audit_accepted=false`,
`performance_result_accepted=false`, and `mechanism_gate_passed=false`.

Across-arm medians were 14.5348 versus 14.5206 request/s and 465.114 versus
464.660 output token/s. Median wall-latency P50/P95/P99 was
2178.022/2260.793/2261.729 ms for control and
2177.523/2254.696/2257.893 ms for candidate. Median TPOT P50/P95/P99 was
55.011/59.962/60.169 ms versus 54.786/59.923/60.063 ms. Raw Native TTFT is
retained in each arm but is not used for a cross-runtime or acceleration
claim. Final cleanup removed the container and released the worker, Docker
execs, port 18088, systemd units, and NPU7.

Before Git publication, six host-wide process snapshots were deterministically
sanitized because unrelated VS Code Remote processes exposed ephemeral
connection-token arguments. Only those token values were replaced with
`<redacted>`; a publication redaction manifest records every raw and published
SHA-256. Request/response, runtime, device, metric, identity, and audit files
were unchanged.

## v9 critical-path decomposition and v10 readiness

The checked-in derived artifact
`benchmarks/qwen14b_b32_admission_cache_v9_critical_path.json` recomputes all
six v9 arms at SHA-256 `a4082db...d8cb7`. Per arm, eight B16 append batches
sum to 2.373--2.422 s, 124 B32 decode batches sum to 4.813--4.863 s, and 132
executor-finish-to-state-release intervals sum to 1.394--1.403 s. The
across-arm median release sum is 1.395210 s and the median per-batch interval
is 10.654750 ms. State-release-to-next-executor gaps sum to only
0.138--0.171 s.

This derived result has `hardware_execution=false` and
`performance_result_accepted=false`; its sources are real-online v9 records.
It motivates an attribution experiment, not an optimization claim. Rust
timing schema v2 and scheduler-plan v15 now expose a strictly reconciled
completion breakdown and deliberately invalidate the frozen v9 launcher and
state identity. Unit tests pass for the timing partition and historical-v9
invalidation. Clean-pushed source `9ee539c` produced four byte-identical Rust
builds across two independent bundle invocations: bundle
`8b880604...77da3f`, server `0e566ecd...269f2`. A no-network, no-device,
capability-free temporary container generated v35; all artifact audits accept
scheduler-plan v15, telemetry v2, and state compatibility
`a909a4d...08ee4`. NPU7 remained at its idle 5% HBM baseline. These are
offline readiness records; no v10 online lifecycle has yet run.

The sole v10 submission then failed closed before runtime initialization.
Docker 29 reported the live container `Image` as OCI index
`105834a...ce13`, while the frozen carrier requires config
`0fc116f...10731`; the selected arm64 manifest still matched
`36194f...c73b`. The live carrier audit therefore rejected before CTest,
server launch, listener creation, model load, request submission, or NPU
execution. The postmortem audit accepts with zero violations, zero requests,
`hardware_execution=false`, and retry disabled. NPU7 was idle before and
after at 5% baseline HBM/0% AI Core, port 18088 is free, and the exact
container and collected unit are absent.

## v11 carrier-v3 software readiness

The v11 skeleton adds no online result. Carrier-v3 binds Docker 29's live
`Image` observation specifically as the OCI index role while retaining exact
independent index, arm64 manifest, and config verification. Mutation tests
reject a config-valued live field, a changed observation role, a missing
descriptor, and a substituted manifest digest. v11 deliberately reuses the
unchanged v35 artifact, scheduler-plan v15, timing-v2, Rust bundle, C++
producer closure, eager ACLNN path, B16 append and B32 decode.

Focused carrier/v11 tests pass 18/18 and complete Python discovery passes
375 tests with six skips. These are software-only records:
`hardware_execution=false`; request/s, output token/s, latency, TPOT, state
hits, reused tokens, peak HBM and TTFT remain unavailable. A real-online
sample exists only if a later clean-pushed carrier/lock and one-shot NPU7
lifecycle pass every gate.

## v11 real-online completion attribution

The sole clean-pushed v11 lifecycle completed successfully on physical NPU7
with no restart or retry. It served 128 synchronized c32/o32 requests; every
one of the 4,096 output tokens matched the independently frozen greedy oracle.
The client concurrency was 32, while Native physical execution remained
distinct: eight B16 append batches followed by 124 B32 decode batches. Error
rate was 0, state hit rate was 1.0, effective reuse was 262,144 tokens
(2,048/request), and peak HBM was 44,658 MiB.

This diagnostic measured 14.558904 requests/s and 465.884943 output tokens/s.
End-to-end wall latency P50/P95/P99 was
2,171.935/2,252.680/2,254.054 ms; TPOT P50/P95/P99 was
54.931/59.876/60.022 ms. Native TTFT remains recorded in raw evidence but is
not cross-runtime comparable and is not used here.

All 132 timing rows reconcile exactly. Request commit totals 1.393374729 s
(10.628797-ms median, 10.883409-ms P95). State-graph publication alone totals
1.321645676 s (10.286225-ms median, 10.517646-ms P95), or 94.85% of request
commit and 92.73% of the release partition. Scheduler requeue totals only
23.369062 ms (0.184086-ms median); completion staging totals 30.056123 ms
(0.219936-ms median). Worker metrics, cohort resolution, and release residual
are negligible at this scale.

The independent audit is accepted with no violations and SHA-256
`99be8e1d322efbbf6759c6d57ba774968fe2b9d7320afd30952ad14aec3ac511`.
It labels the evidence `real-online-attribution-diagnostic` and keeps all
formal, performance-claim, and TTFT-comparison gates closed. The run result
SHA-256 is
`3c6ccc5f9918410575d41756bdcce4187bafceb480d9303dc074c1a75d480e09`;
the controller result is
`b7e07b8532843cd78ab4cc0ba1c2da330a09ffcd44cf2fe37c949c5c19bc964f`.

Two host process snapshots contained unrelated VS Code Remote ephemeral
connection credentials. Publication replaced only those values with
`<redacted>`; `publication_redaction_manifest.json` binds raw and published
SHA-256 values and declares that scientific evidence is unchanged. Its
SHA-256 is
`2b4c8845b8092d2c7a241af635cd0f610ac5cedb55ada79fc20bff8afba7239d`;
the regenerated 60-file controller evidence manifest is
`8c54e1a1929209a73b28a6a177aab64b3d8970221405108389ff8b17b78e7d73`.

The attribution selects, but does not implement, an O(1) state-ID projection
index and atomic physical-cohort publication as the next candidate. Its
Ascend-specific hypothesis is that removing this host commit stall lets the
next fixed B32 cohort enter the ACL/CANN submission path earlier. Generic
double buffering, scheduler requeue, graph replay, and PTO kernel work are not
supported as the first response to this evidence.

After the lifecycle, the container is absent, the systemd unit is
inactive/dead with `Result=success`, port 18088 is free, no Native worker or
Docker exec remains, and NPU7 returned to its idle baseline with no device
process.

## v12 atomic state-publication software candidate

The working v12 implementation replaces the active-continuation scan with an
O(1) `state_id` projection and publishes each prepared physical cohort through
one atomic graph transaction. It also introduces protocol v3 and timing v3 so
C++ executor finish, Rust completion receipt, publication, and the next
batch's first actual Ascend runtime/ACL submission entry are observable in the
common Linux `CLOCK_MONOTONIC` domain. For decode with COW this entry precedes
the first asynchronous D2D copy; otherwise it precedes the blocking
`aclrtMemcpy` token-ID H2D call. It is therefore a common runtime API-entry
boundary, not a universal worker-stream-enqueue timestamp. A B16 mock test
also injects terminal eviction failure at positions 1, 8, and 16: every case
stops the actor/backend, rejects subsequent work, and returns no ambiguous
continuation. This confirms the documented fail-stop boundary without
claiming rollback of already-executed NPU work or per-state evictions.
Scheduler-plan v16 and the aggregate compatibility closure bind these changes;
v11 state is not reusable.

The exact v12 closure was frozen from clean pushed `283cfff`: Rust bundle
identity `caad9dc...e2b0d`, C++ producer closure
`1de155f...be246`, execution artifact `2763024...7c6f`, and aggregate state
compatibility `e64a33e...1dd3`. The latter differs from v11
`a909a4d...08ee4`, so old states fail closed. Composed offline readiness
accepted all checks from pushed lock commit `89d0d51`.

The sole durable NPU7 lifecycle then completed 128 synchronized c32/o32
requests without retry. Every response and all 4,096 output tokens matched the
independent greedy oracle. Physical execution was eight B16 append batches and
124 B32 decode batches; error rate was 0, state hit rate 1.0, effective reuse
262,144 tokens, and peak HBM 44,658 MiB. Throughput was 14.728668 requests/s
and 471.317381 output tokens/s. Wall P50/P95/P99 was
2,149.182/2,222.409/2,224.134 ms; TPOT P50/P95/P99 was
54.574/59.406/59.460 ms.

The mechanism is a negative result. State publication measured
9.934430 ms median, 10.016335 ms P95, and 1.272996749 s total. Relative to
v11's 10.286225 ms/1.321645676 s, this is only a 3.42% median and 3.68%
aggregate reduction, far below the frozen 30% requirement. Serialized release
was 10.470863 ms/1.372490305 s and missed both ceilings. Across 120 exact
adjacent B32 decode pairs, the next-Ascend-API gap was
11.523865 ms/1.384453570 s and also missed both ceilings. All 132 common-clock
rows and all 120 causal pairs reconcile.

The immutable frozen auditor rejected with four violations. Three are the
intended threshold failures. The fourth is an auditor schema-path defect: it
looks for worker batch deltas at validation top level, while the runner stores
them under the accepted `physical_append_admission` object. The raw result
itself has `validation.passed=true`, nested physical validation passed with no
violations, the exact B16/B32 histograms, and oracle-exact outputs. A separate
postmortem audit accepts all checks only under classification
`correct-online-negative-mechanism-result-with-frozen-auditor-schema-path-bug`;
its SHA-256 is `0b83710f...5a43029` and it binds postmortem-auditor
SHA-256 `c14ef1a4...d876600`. It keeps
`mechanism_gate_passed=false`, retry disabled, and all formal, performance,
vLLM, and TTFT claims closed.

Cleanup is complete: the exact container is absent, the collected unit is
inactive/dead with zero restarts, port 18088 is free, no scoped worker or
Docker exec remains, and the frozen post-run snapshot shows no NPU7 device
process. A later unrelated Cruise workload entered NPU7 after this cleanup and
was not touched. Host-process publication snapshots redact only unrelated VS
Code Remote tokens; the redaction manifest is `e7c57f55...d8f20` and the
regenerated controller evidence manifest is `0896a1d0...19a0`.

## v13 residual publication attribution software

The software gate adds hierarchical timing without changing state-publication
semantics. The existing publication interval now reconciles exactly into
reference preparation, graph-lock wait, graph work, identity assignment,
resident-map insertion, and residual. Graph work and the generic graph
transaction each have their own exact additive decomposition.

Rust unit tests cover successful transaction reconciliation, byte-identical
batched state identities, full runtime timing reconciliation, and deliberate
graph-mutex contention. The related artifact/launcher identity tests cover
timing-v4 and scheduler-plan v17. All 129 Rust tests and 27 focused Python
contract tests pass, and strict Clippy is clean. No v13 hardware result or
optimization conclusion exists yet.

## v13 real-online residual publication attribution

The sole supervised NPU7 lifecycle completed with no retry. All 128 requests
and 4,096 output tokens matched the frozen independent oracle. Client
concurrency was 32; physical execution was eight B16 append batches and 124
B32 decode batches. Throughput was 14.688789 requests/s and 470.041248 output
tokens/s. Wall P50/P95/P99 was
2,156.257/2,228.194/2,230.775 ms; TPOT P50/P95/P99 was
54.501/59.370/59.433 ms. Error rate was zero, state-hit rate was one,
effective reuse was 262,144 tokens, and peak HBM was 44,659 MiB.

All 132 rows reconcile at the outer publication, graph publication, and graph
transaction levels. Outer publication measured 9.918519 ms median and
1.271947166 s total. The graph call alone was 1.264652702 s, 99.43% of the
outer sum. Graph-mutex wait was 99,571 ns total (0.008%), while resident-map
commit was 5.382601 ms total (0.42%).

Inside graph publication, payload JSON serialization/SHA was 4.971867 ms
median and 637.603556 ms total (50.46%); initial object identity was
2.075653 ms/267.236546 ms (21.15%); and the graph transaction was
2.702548 ms/345.895711 ms (27.37%). Per-object validation was 82.03% of that
transaction and 22.40% of total graph time. The payload-hash, initial-identity,
and object-validation categories jointly account for 94.00% of graph
publication. The 120 adjacent decode completion-to-next-Ascend-API gaps
reconcile at 11.466940 ms median and 1.380189953 s total.

The independent audit accepts with no violations. The exact container is
absent, the supervised unit is inactive, port 18088 is free, and NPU7 has no
device process. This is an attribution result, not a performance comparison:
`formal_gate_open=false`, `performance_result_accepted=false`,
`performance_claim=false`, and `ttft_comparison_permitted=false`.

## v14 release/single-pass software repair

Post-v13 audit found that the frozen v12/v13 Rust bundles recorded
`profile=dev` and copied `target/debug` executables. This does not invalidate
their exact online observations, but it limits them to the measured dev
producer closure. They cannot serve as release-profile controls.

The working v14 software introduces a strict release bundle format and two
identity-bound publication policies in the same release binary. Unit evidence
proves a fixed framed-binary golden digest, distinct control and candidate
state identities, one object-identity computation for a prepared local object
versus two for the untrusted insertion path, stale-generation rejection after
sealing, and unchanged atomic/fail-closed graph behavior. Rust tests pass
133/133 and strict release Clippy passes. This is software evidence only; no
v14 online metric or speedup exists yet.

The pre-execution release proof is complete. Two outer bundle builds each
performed two isolated `cargo build --locked --offline --release`
invocations, and all four optimized servers were byte-identical. The v38 and
v39 artifacts share the release server, execution artifact, execution
configuration, runtime-dependency, C++ executor, and producer-closure
identities. Their scheduler-plan and state-compatibility digests intentionally
differ because the publication encoding and trusted-construction policy are
state-validity inputs. These are provenance facts, not online performance
results.

## v14 release-profile publication pair

The one authorized NPU7 pair completed from clean pushed `c4f2000` with
`NRestarts=0`, no retry, and an independent audit of `accepted=true` with zero
violations. Each fresh lifecycle completed 128 oracle-exact c32/o32 requests,
eight B16 append and 124 B32 decode batches, zero errors, full state hits,
262,144 reused tokens, and complete cleanup.

The candidate reduces aggregate graph publication from 48.430444 ms to
28.751421 ms (-40.63%). Median publication falls from 373.392 us to
221.601 us. Aggregate payload hashing falls from 21.836847 ms to 8.211090 ms
(-62.40%), while transaction object validation falls from 8.569864 ms to
1.275677 ms (-85.11%). Native tensor execution never needed JSON; the repair
removes JSON canonicalization and duplicate identity computation from
continuation publication.

The saving does not translate into this pair's end-to-end metrics. Control
versus candidate is 17.4315 versus 17.2754 request/s (-0.90%), 557.8090 versus
552.8143 output token/s, wall P50 1810.593 versus 1826.134 ms (+0.86%), and
TPOT P50 43.777 versus 44.312 ms (+1.22%). Peak HBM is 44,658/44,659 MiB.
The conclusion is a successful control-plane repair with a negative
end-to-end diagnostic, not an online speedup.

## v15 device/task attribution software boundary

The next milestone targets the dominant executor envelope rather than the
sub-millisecond publication path. Reanalysis of the 124 B32 rows in each v14
arm places median executor time near 38 ms, with roughly 6 ms spent submitting
the 48-layer operator chain and roughly 32 ms observed at final
synchronization. The final interval includes queued device execution; it is
not evidence of a redundant 32-ms host synchronization.

The v15 software adds a fail-closed profile-attribution gate and binds the
combined ACL-event/msprof policy into scheduler and state compatibility
identity. CANN export summarization now aggregates task duration by operator
family and computes per-stream inter-task gaps. Clean pushed `ac75b0f`
generated the v40 artifact with scheduler digest `7fde0816...018b` and state
compatibility `bf80a6b2...c4b1`; independent execution, runtime-binding, and
state-chain audits accept. This is pre-execution evidence only. No v15 online
result, selected optimization, or performance claim exists at this
checkpoint.

A final launcher-to-client audit caught and repaired a pre-execution contract
gap: the launcher passed the combined profile policy, while the client parser
accepted only bare timing-v5. No request or NPU work had started. The frozen
preregistration now binds the corrected client bytes.

## v15 unique lifecycle: post-run contract rejection

The only `Restart=no` NPU7 lifecycle served all 128 requests and captured
dynamic msprof for the exact worker PID. Outputs are 128/128 oracle-exact,
error rate is zero, hit rate is 1.0, effective reuse is 262,144 tokens, peak
HBM is 44,664 MiB, and execution contains eight B16 append plus 124 B32 decode
batches. ACL-event timing schema 3 is present for all decode batches. msprof
start/stop/quit succeeded with exit 0.

The frozen client nevertheless exited 1 after execution. `/metrics` correctly
emitted base schema `native-capacity-wave-timing-v5` and Linux monotonic clock,
whereas the client compared both against the combined state-identity policy
ending in `device-event-v1-msprof-attach-v1`. Its only two violations are
schema mismatch and clock-domain mismatch. The launcher and controller
therefore remain failed, `completed=false`, and no retry is permitted.
Profiled throughput (13.0995 request/s, 419.184 output token/s) and TPOT are
perturbed provenance and not a performance comparison.

The no-NPU postmortem export is complete. Its independent audit accepts with
zero violations and a repeated invocation is byte-identical
(`7dbd66a8...9fdce`). It does not promote the original lifecycle:
`original_lifecycle_accepted=false` and
`original_failure_preserved=true`.

The 124 B32 device timelines are 55.505/56.740/58.092 ms at P50/P95/P99.
Under profiler perturbation, host executor P50 is 56.810 ms, layer submission
P50 is 53.720 ms, and final-sync P50 is 1.982 ms. Thus the earlier
approximately 32-ms final-sync envelope was queued device work rather than
Native state serialization; the profiler changes where the host observes
that work, so these numbers cannot be compared causally with v14.

The exported 7.073 s of task duration selects `MatMulV2`: 35,845 records,
3.316 s, and 46.8867%. `MatMulV3` is 1.828 s (25.8440%) and
`IncreFlashAttention` is 0.998 s (14.1055%). Stream 4 contains 97,665 positive
inter-task gaps totaling 3.032 s, P50 8.5 us and P95 102 us. The gap statistic
mixes all phases in the profile window, so it is supporting attribution, not
a decode-only utilization claim. The successor question is now narrowly
defined: map the dominant MatMulV2 kernels to exact projection shapes,
formats, and cube utilization before choosing a PTO lowering, fusion, or
scheduling change.

Profiled provenance remains 13.0995 request/s, 419.184 output token/s,
TPOT P50/P95/P99 62.116/68.089/68.108 ms, zero errors, full state hits,
262,144 reused tokens, and 44,664 MiB peak HBM. It is not a performance
comparison, TTFT comparison, or speedup claim.

## v16 MatMulV2 attribution software boundary

The offline analyzer joins exact device task and operator-summary records,
classifies complete shapes against source-level model roles, checks expected
layer/batch counts, and binds source hashes. Mutation tests cover count drift,
unknown shapes, and missing lowering markers. This checkpoint is software
readiness only; an independent auditor additionally rejects file mutation,
result drift, and claim-gate mutation.

The clean-parent report accepts and a second generation is byte-identical.
All 35,845 MatMulV2 task rows join bijectively with zero unclassified rows.
B32 decode accounts for 35,836 rows, 3.3046 s, and 99.6474% of MatMulV2
duration. The exact decode-role decomposition is:

| Role | Count | Task duration | Median Cube utilization |
|---|---:|---:|---:|
| fused Gate/Up | 5,952 | 1.5517 s | 96.3995% |
| Down | 5,952 | 0.7610 s | 89.1230% |
| Q Addmm | 5,952 | 0.3335 s | 85.9155% |
| O | 5,952 | 0.3118 s | 86.1495% |
| K/V Addmm | 11,904 | 0.1830 s | 58.8720% |
| LM head B32 | 124 | 0.1637 s | 94.7615% |

Gate/Up is `[32,5120] x [27648,5120]^T`, uses ND BF16 inputs/output,
and maps exclusively to kernel
`MatMulV2_ND_ND_FP16_FP16_false_true_all_16876241`. It contributes 46.9549%
of decode MatMulV2 duration. Its preceding-task gaps total 0.5926 s; the
separate 5,952 SwiGLU tasks add 0.1049 s.

High Cube utilization plus the historical slower B16 PTO MatMul rejects a
plain backend substitution. The selected successor instead combines B32
Gate/Up and SwiGLU in one PTO data path, replaces the full cross-operator
`BF16[B,2I]` lifetime with bounded paired-tile staging, removes the dynamic
ACLNN/SwiGLU task boundary, and requires cross-N left-activation reuse to
address the prior PTO weakness. On A2/A3 the staging remains GM-backed; this
is an optimization hypothesis, not a measured speedup. Report SHA-256 is
`bee7e35c...c480`; audit SHA-256 is `c4115283...dc0e`.
## Physical-B32 PTO mixed component software readiness

v17 corrects the v16 successor hypothesis for the actual 910B2 data path.
A2/A3 PTO Cube-to-Vector communication uses a GM-backed TPUSH/TPOP FIFO, so
the candidate cannot eliminate intermediate GM traffic. The implemented
candidate instead combines Gate/Up and SwiGLU in one `dav-c220` mixed kernel,
uses `F322BF16` fixpipe conversion, streams paired 192-column tiles through a
576-KiB bounded FIFO, and removes the separate ACLNN SwiGLU launch boundary.

Two initial compile attempts were rejected before artifact creation. The first
called host-only `constexpr` address helpers from AICORE code; the second
placed the device-only `TPipe` alias in the host compilation pass. Both were
repaired without changing geometry or arithmetic. The next two fresh builds
were byte-identical with SHA-256 `cf78cd1e...a785`; the 158,248-byte ELF
contains both `_mix_aic` and `_mix_aiv` metadata. The full-model probe compiles
and links, and the partition and component contracts pass in Release mode.

Read-only code audit then found and blocked an unbalanced AIV output-store
event sequence: a post-wait re-seed could let a later chunk consume a stale
completion event. The repaired sequence follows the PTO A2/A3 pattern with
one initial seed, a wait before each UB reuse, a completion set after each
TSTORE, and one final drain; the mixed ELF recompiles successfully. The same
audit found that a component library could be substituted outside the
production execution-artifact identity. The probe now requires and verifies
the library's canonical SHA-256 before `dlopen`, while the new component
identity binds the clean parent, PTO tree, source, compiler, ELF, native
probe, execution artifacts, oracle, runtime closure, geometry, and event
protocol. The 576-KiB FIFO workspace is allocated once per complete decode
call and reused by all 48 same-stream layers.

These builds came from an implementation worktree and are software evidence,
not publishable artifacts or performance results. No NPU, model lifecycle,
online request, or timing comparison has run. A clean-parent rebuild,
identity, preregistration, independent correctness oracle, and NPU7 device
gate remain required.

The recovered v31 execution artifact cannot be reused for v17 because it
binds an older Native probe digest. Rather than bypass that check, v17 adds a
clean-only preparer for a fresh physical-B32 ACLNN execution artifact and a
separate two-stage runner. The runner first permits one PTO correctness
lifecycle; its paired 3+3 mode remains locked until that bundle passes the
independent auditor. The artifact-only auditor independently recomputes the
externally pinned identity, PTO git tree, file leaves, mixed ELF metadata and
symbol, local-memory geometry, GM FIFO contract, and output-store event
balance. No hardware result exists yet.

The pre-hardware runner audit also closed carrier substitution, container
path substitution, incomplete logit checking, PID-reuse cleanup, and missing
FFTS/FIFO telemetry. A no-device/no-network dirty-tree compile confirms the
telemetry change builds; it is not an experimental result. The mixed PTO ELF
remains `e32acc63...47986`; the telemetry-bearing probe is provisional until
rebuilt twice from the final clean pushed checkpoint. CANN appears here only
as the PTO compiler/runtime dependency and control substrate, not as the
candidate operator implementation.

The first v17 correctness invocation produced a pre-execution negative
result: the artifact auditor rejected live probe/oracle paths whose basenames
did not equal the saved identity leaves. The component bytes and digests
matched, no candidate worker started, and NPU7 remained idle. The runner now
audits the saved identity-bound copies and separately retains exact SHA-256
and container-path equality checks for the files actually executed. This is
a tooling-gate failure, not PTO correctness or performance evidence.

The repaired artifact audit accepted the second invocation, but the worker
then rejected v41 because its binary-bound decode execution-plan digest was
all zero. This occurred before model/HBM allocation and before any component
logit or timing output. The exact worker was cleaned and NPU7 returned idle.
The admission check is correct and is not bypassed. v42 instead introduces a
domain-separated, source-derived physical-B32 plan that freezes the complete
per-layer decode DAG, Qwen2.5-14B geometry, pinned PTO sources, the unique
mixed Gate/Up+SwiGLU backend exception, FFTS and 24-slice/576-KiB GM-FIFO
geometry, and closed claim gates. Its digest is compiled into the probe and
cross-checked against the execution artifact and component identity. No v17
correctness or performance result exists yet.

The v42 no-device preparation now closes successfully. Two fresh Native probe
builds are byte-identical (`9772f2e7...bd6e6d`); the execution artifact binds
the canonical plan as `da1cf2a4...ecefb`, and the regenerated component
identity is `b9906159...1cbcd`. Two independent artifact audits reproduce
byte-for-byte as accepted, violation-free record
`0060da65...c025`. These are build and identity results only. They authorize
at most the next single NPU7 correctness lifecycle after the preregistration
is clean-pushed; no component latency or speedup exists yet.

Correctness r03 passed the independent artifact gate and captured the exact
worker generation, then its outer session terminated with status 143 before
model allocation. The raw lifecycle has empty stdout/stderr, no inner exit
record, no logits or timing, HBM fixed at the idle 5%, and zero AICore and
AIVector utilization. Exact cleanup returned NPU7 and port 18088 to the
preregistered idle state. Because the former EXIT trap reported cleanup status
0 rather than preserving the incoming signal, this bundle is classified as a
zero-compute orchestration failure. Signal custody and a periodic progress
heartbeat are now part of the runner contract; r03 supplies neither PTO
correctness nor performance evidence.

r04 preserved a second orchestration/runtime failure. Because an unnecessary
`docker exec -i` ran in the background of a PTY shell, the host sudo/Docker
chain entered job-control stop state while the container worker continued.
After the exact stopped process chain was retained and resumed, buffered
stderr showed `aclrtSetDevice` error 107001. No HBM allocation or AIC/AIV
activity occurred, and exact cleanup succeeded. Logical device 7 failed with
the same error, while a single-device non-privileged carrier augmented with
`SYS_ADMIN` and unconfined seccomp failed earlier at `aclInit` error 500000.
The repository's established Ascend privileged permission model then passed
a 16-KiB exact-copy smoke with physical visibility fixed to NPU7. The
successor runner removes stdin attachment and binds new carrier
`b7a14106...200873`, contract `154a4516...e643e`; r04 contains no PTO output.

r05 proves that those carrier fixes reach real device execution but rejects
the mixed component as non-completing. The independent artifact gate
accepted, the full Qwen2.5-14B allocation raised HBM from 5% to a reported
68%, and 646 samples observed AICore=AIVector=100%. No output was emitted
before CANN reported a three-minute timeout on stream 4, task 2216, with 662
pending tasks. The preregistered 900-second limit ended the lifecycle with
status 137. Because there are no logits or component timings, neither
correctness nor latency is defined; the paired mode remained locked. The raw
plog/device logs, 1,062 HBM/use samples, PID/start generation, and complete
cleanup evidence remain in the ignored r05 bundle; its 92-file evidence
manifest SHA-256 is `576124fa...16630`. Exact carrier removal released the
uninterruptible worker and restored idle NPU7.

## v18 SageLLM architecture postmortem

v18 is a read-only cross-repository design audit, not an experiment or
performance result. It froze 15 private Qixin-Gaoke SageLLM repository heads
and inspected 12 runtime-facing source trees. The checked-in SageLLM umbrella
E2E baseline is explicitly simulated and lacks model/device provenance; no
SageLLM number is admitted here.

The audit finds a reusable declarative capability/ABI vocabulary and handle
lifecycle, but the realized executor remains HuggingFace/Torch-controlled,
uses dynamic kernel lookup/fallback, performs Python work per decode step, and
does not make its logical KV pool authoritative for physical accelerator
state. The resulting future design is an identity-bound sealed execution-
component descriptor with startup-only validation and pre-resolved direct
dispatch. It is unimplemented and has no performance claim. Full provenance
and the adopt/adapt/reject matrix are in `docs/SAGELLM_POSTMORTEM.md`.

## v19 sealed execution-component software contract

v19 implements the descriptor boundary proposed by v18. Rust and C++ encode,
decode, validate, and domain-hash the same canonical 640-byte record; their
shared identity golden is
`9d5a299808415350e4668cce010250062f0945a56e3179a7de542211d9c02873`.
Every persistent byte is mutation-tested: a flip must either produce a
different identity or fail decoding. C++ startup validation is the only public
constructor path for the opaque prepared capability, and stale identities or
dense slots reject before dispatch.

Execution-artifact schema v4 is a 456-byte successor that binds the descriptor
identity while preserving v1/v2/v3 at 360/392/424 bytes. The existing
execution-config, resident-plan, and Rust compiled-plan/state-compatibility
chain propagates the change, so a descriptor mutation cannot reuse old
continuations or physical state.

The five-process host component contract reports direct/prepared medians of
7.031/9.684 ns per call, or 2.653 ns added by prepared dispatch, with zero
prepared-call allocations. This is a negative host abstraction cost, not an
NPU or online inference result. v19 generated no production artifact, launched
no service, used no NPU, and measured no token or request. All online,
component-integration, performance, vLLM, and TTFT gates remain closed.

## v20 reproducible sealed-component artifact closure

v20 is a `derived-artifact`, no-device result. From clean-pushed commit
`963a22cac30cdae3b0b11be02c923421ee6f290a`, two serial fresh preparations
(`v43-a` and `v43-b`) reproduced the same 640-byte sealed descriptor
(`ea8a0d0c...ad316`, identity `2f959743...e5465`) and 456-byte schema-v4
execution artifact (`1a686bc3...c1e5`). The config binary
(`33171c70...5d98`), resident-plan identity (`73a87a0f...05c9`), and aggregate
state compatibility digest (`e402c361...adda3`) also match.

The two descriptor, artifact, runtime-binding, and state audits accepted with
zero violations/mismatches and are byte-identical across lifecycles. The
readiness record and closure record are also byte-identical. The only
different files are the two config compiler metadata/stdout copies, whose
single diff is the intentionally recorded `v43-a` versus `v43-b` artifact
path; their semantic and binary digests match.

The first reproduction attempt exposed and repaired a provenance bug: raw
`ldd` stdout contains ASLR addresses, so hashing that diagnostic text made
otherwise identical state-audit/readiness records differ. The canonical
runtime closure now retains the executable digest and sorted dependency
name/content digests, whose identity is `77f0485e...5fb64`, and excludes raw
loader output.

The final artifact deliberately retains an all-zero optional operator-library
digest and the production MLP policy remains fused ACLNN Gate/Up plus ACLNN
SwiGLU. The PTO mixed component is described and sealed, but is not selected
by a resident worker. No model was loaded, no NPU was used, and no request,
logit, latency, throughput, HBM, correctness, vLLM, or TTFT measurement exists.
All integration, correctness, performance, formal, and TTFT gates remain
closed; the v17 device non-completion is not repaired by this result.

## v21 isolated repair and structured component correctness

The old mixed AIC/AIV kernel failed the single-layer r02 reduction: one launch
did not complete within 45 seconds and was externally removed. r03/r04 were
later invalidated as successor evidence because their runner archived the new
files but executed hard-coded stale container paths. After that provenance
defect was fixed, the pure Cube r06, pure Vector r07, and same-stream combined
r08 arms all completed with bit-exact zero output and clean teardown.

The independently frozen structured r09 oracle then exercised nonzero
positive and negative Gate/Up values over every physical-B32 row and output.
All 442,368 BF16 outputs matched exactly: `mismatch_count=0`,
`max_abs_error=0`, and no nonfinite output. Its 1,359,599-ns one-shot elapsed
value is retained only as a correctness diagnostic, not a performance result.
This closes the standalone projection/layout/SwiGLU question, not full-model
correctness.

The resident source now rejects wrapper-only identity admission and requires
the three-ELF closure through the sealed descriptor and artifact-v4 identity
before loading the component. It compiles and its focused host/contract tests
pass in a no-device container. A fresh clean-source descriptor/artifact and
one NPU7 full-model oracle lifecycle remain required, so online, performance,
formal, vLLM, and TTFT gates remain closed.

The first sealed full-model r10 attempt passed artifact admission and loaded
real weights, but returned wrapper status 1 before either PTO stage. The
wrapper still required a nonnull legacy FFTS argument despite immediately
discarding it; r09 had supplied a nonnull historical address and therefore
did not expose the contradiction. r10 produced no result JSON, cleaned its
carrier with status 0, and returned NPU7 idle. The guard is removed and the
changed wrapper requires a fresh identity closure before retry.

r11 used that fresh closure and completed. Runtime metadata reproduced
descriptor `5ce73fb0...61dab` and three-ELF closure
`871491c0...f84b8`; the enclosing artifact/resident/state identities are
`826388b9...b1729`, `246520a2...b55ad`, and
`c954fd7a...b3092`. Generation `[525,264]` matched the independent oracle,
and all 32 physical-B32 rows selected token 264 with device-argmax,
independent-oracle, and frozen-decision parity. All logits are finite.
Bitwise frozen-logit parity is false, with maximum absolute error 0.3125 and
cosine similarity 0.999916, so the result is correctly described as bounded
numerical plus greedy correctness. The diagnostic one-shot decode was
30.557 ms and sampled peak HBM 68%; neither is a performance comparison.
Exit/cleanup were 0 and NPU7, port 18088, and workers were clean afterward.

The subsequent full CTest pass found one fail-closed ordering defect rather
than a device-compute error. Descriptor and descriptor-identity overrides
were rejected only after execution-config decoding, so the deliberately
invalid contract fixture produced a config-size error first. The guard now
rejects the complete forbidden override set before config or device work.
Because this changes the resident executable identity, r11 remains valid
evidence for clean commit `02e7d4b` but is not used to certify the successor
checkpoint; that checkpoint requires a fresh identity chain and NPU7 run.

The clean-pushed successor `be5f59d` produced v46 descriptor
`4339c195...686f3`, unchanged stage closure `871491c0...f84b8`, artifact
`c3c45637...0b44b`, resident-plan identity `6616ad44...c5dc0`, and aggregate
state compatibility `4a1e492e...784d`; all independent audits accept with no
violations. Fresh r12 exited and cleaned with status 0. Generation
`[525,264]` and all 32 B32 row decisions match the independent oracle, device
argmax, and frozen decision. Every logit is finite; bitwise parity remains
false with maximum absolute error 0.3125 and minimum cosine similarity
0.999916. Result JSON is `3678c7a6...53e9` and logits are
`b897be48...f828`. The 30.621-ms one-shot and 68% sampled peak HBM are
diagnostics only. NPU7 returned idle, the exact carrier is absent, port 18088
is free, and no worker remains.

## v22 matched component-attribution result

The v22 harness produced one accepted unprofiled hardware pilot and one
preserved failed profile lifecycle.
It compares the exact physical-B32 fused ACLNN Gate/Up plus ACLNN SwiGLU
control with the accepted v46 split PTO Cube/Vector component under one
structured input/weight/oracle family. The probe preserves production ACLNN
executor/launch order and reports preparation, submission, synchronization,
host-total, and device-event samples separately.

Admission binds the v46 wrapper `4540c3...9239`, Gate stage
`ee194a...fca4`, Vector stage `79766f...b0b82`, descriptor
`4339c195...686f3`, and frozen oracle `4246ca...c2bc`. An apparent local
three-ELF tree was rejected because its stages matched but its wrapper did
not, demonstrating that the complete closure rather than a directory name is
the evidence authority.

The accepted pilot contains 40 samples per backend. ACLNN device-event and
host-total medians are 335.450 and 389.413 us; PTO medians are 235.980 and
284.857 us. Thus PTO is 29.65% faster by device event and 26.85% faster by
host total at this exact component boundary. All four saved outputs have the
same SHA-256 `e686c1d6...95bcd`, match the frozen oracle, and contain no
nonfinite values. All 188 HBM samples report 5% usage.

The sole profile lifecycle completed ACLNN and msprof export, then failed
before PTO. The trace contains 19 task rows, 10 compute rows, and 434 CANN
API rows, but the shared summarizer incorrectly required at least 101 rows.
Offline analysis after the repair selects five MatMulV2 tasks (242.800-us
median) and five SwiGLU tasks (13.160-us median); this is postmortem evidence,
not matched PTO attribution. The original bundle audits as rejected with
`incomplete_or_invalid_bundle:FileNotFoundError:01-aclnn/profile_summary.json`.
All 93 profile-lifecycle HBM samples report 5%; carrier and NPU cleanup pass.

The shared 101-row summarizer remains byte-identical so historical
preregistration hashes remain valid. A v22-only summarizer requires at least
10 task, 10 compute, and 10 CSV rows before exact stage matching. The auditor
now emits a fail-closed rejection for incomplete bundles. No second profile
ran. There is no online, throughput, TPOT, TTFT, or vLLM result, and
`formal_gate_open=false`.
## v23 sealed-PTO online integration checkpoint

The software now contains an explicit enum-5 policy,
`fused_gate_up_pto_b32_split_sealed_aclnn_fallback_swiglu`. Unlike the
historical component-only variables, the policy is decoded identically by
Rust, C++ and Python and requires all three artifact leaves: decode plan,
operator library and sealed descriptor. The production protocol context now
owns the startup-prepared combined capability, supplies one reusable
cohort-lifetime workspace, and passes both into the existing physical-B32
layer branch. B1--B16 and append/prefill remain ACLNN.

Targeted validation passes for the Rust/Python codecs and artifact identities,
the C++ config/artifact tests, the resident worker build, and the online
readiness contract. No v23 artifact, NPU lifecycle, online request or vLLM
comparison exists at this checkpoint. The v22 component delta remains a
component result and is not promoted to online throughput.
## v26 sealed-PTO online pair pre-execution result

v26 produced no serving or performance result. Its inert Native carrier was
created and immediately rejected because Docker inspect reordered an
otherwise identical 28-entry environment. No model load, server process,
request, baseline lifecycle, or NPU kernel occurred. The controller records
exit 2 with Native acceptance and pair completion false; exact removal
returned NPU7 and scoped ports to their initial idle state. All performance
fields are n/a, and formal, performance-claim, and TTFT-comparison gates stay
closed.

## v27 sealed-PTO online pair pre-execution result

The canonical environment-map admission accepted the v27 live carrier.
Execution then stopped at the generic Native launcher because v47 carries
timing-v1 and no release Rust bundle, whereas the current online protocol
admits timing-v5 with frozen Rust/C++ producer identities. No server, model,
request, NPU kernel, or baseline arm ran. This is positive evidence for the
carrier fix and negative readiness evidence for v47 as a serving artifact,
not a correctness or performance sample.

## v28 sealed-PTO online pair pre-model result

v28 reached the fresh worker but rejected the runtime-built C++ binary because
its compiled decode-plan identity was zero instead of v48's nonzero plan
identity. Failure custody preserves the worker command, server stderr, exit
codes, parent/submodule status, NPU and port snapshots. The model, requests,
accelerator kernels and vLLM arm did not start. v29 fixes only the
artifact-to-build plan projection under a fresh implementation lock.

## v29 sealed-PTO online pair pre-request result

v29 proves the runtime plan-binding repair: CMake received the exact nonzero
`d7bca181...0e2b` plan, the worker passed plan parity, read the complete model
closure, and initialized NPU7 to roughly 31.7 GiB total HBM. It then failed
before HTTP readiness or requests with `sealed PTO split Gate/Up+SwiGLU
launch requires physical B32`. The failing cohort was the worker's B16
initialization path, which should have used the policy's ACLNN fallback. No
baseline arm ran and no throughput sample exists. Exact cleanup removed the
carrier and returned NPU7 and both ports idle. The successor fixes caller-side
B32 dispatch selection and must carry a fresh C++ producer and state identity.

The no-device v49 successor now accepts all closure audits. Its plan changed
from v48's `d7bca181...0e2b` to `7a7a338c...f39a1`, artifact to
`d8a193d8...d5b5`, resident plan to `2a5052dd...4f50`, and state
compatibility digest to `21faf5d3...6291`. All 43 Native CTests pass. This is
software/readiness evidence only; no v30 online or performance result exists
until fresh controls are frozen and a new lifecycle runs.

## v30 Native online execution, post-run validator rejection

v30 completed a real Native c=32/o=32 lifecycle on NPU7. All 128 requests and
4,096 output tokens matched the frozen oracle; error rate was zero. Throughput
was 17.5181 request/s and 560.5801 output token/s. Request latency
P50/P95/P99 was 1807.945/1870.321/1873.746 ms and TPOT
P50/P95/P99 was 43.487/48.348/48.405 ms. State hit rate was 1, effective
reuse was 262,144 tokens, and peak HBM was 44,659 MiB. The scheduler recorded
eight B16 append batches and 124 B32 decode batches; all 124 timing rows
reported 48 sealed PTO dispatches.

The lifecycle was nevertheless rejected after computation because the generic
timing validator did not enumerate enum-5 and compared its valid
`workspace_calls=486` against `-1`. The baseline did not run, so this Native
sample is not a paired performance conclusion. v31 changes only that evidence
schema branch.

v31 then failed before container creation because the extended materializer
fields were projected into a carrier schema with an exact historical
six-field map. This does not invalidate v30 execution or v31's materialized
validator. v32 retains all extended hashes in its lock while preserving the
carrier schema; no v31 hardware result exists.

## v32 accepted sealed-PTO online pair

V32 closes the component-to-serving evidence gap. Its independently audited
controller accepts with no violations after one fresh Native lifecycle and
one fresh pinned-vLLM lifecycle on physical NPU7. Each arm completed 128
real online requests and all 4,096 generated tokens matched the immutable
independent greedy oracle. The controller manifest contains and verifies 91
evidence files; exact cleanup left no experiment container, docker-exec
worker, listening port, or NPU7 process.

Native reached 17.6776 request/s and 565.6833 output token/s versus
14.9578 and 478.6482 for vLLM, a diagnostic +18.18% throughput delta.
Native request P50/P95/P99 was
1784.838/1873.236/1875.938 ms versus
2108.616/2190.653/2204.333 ms. Native TPOT P50/P95/P99 was
42.937/47.907/47.966 ms versus 46.294/50.342/57.533 ms. Both error rates
were zero. Native recorded a 1.0 state-hit rate, 262,144 effective reused
tokens, and 44,659 MiB peak HBM; the baseline recorded 53,461 MiB peak HBM
but exports no auditable hit/reuse counters.

The workload had client concurrency 32, while Native append was physically
B16 (eight batches) and decode was physically B32 (124 batches). All 124
decode records carry 48 sealed PTO dispatches. This proves the accepted v22
component is used by the online v49 closure rather than merely present in its
descriptor.

The pair is diagnostic-only: one lifecycle per arm,
`formal_gate_open=false`, `performance_claim=false`, and no cross-runtime
TTFT comparison. The B32 trace attributes 83.08% of mean Native executor
wall time to the final synchronization envelope. Because that envelope
contains queued device execution, it does not identify host serialization.
The only frozen next hypothesis is a physical-910B2 full-MLP
Cube-to-Vector-to-Cube pipeline that replaces the remaining PTO-SwiGLU to
ACLNN-Down boundary. Its first gate is matched component evidence, not an
online claim: at least 5% lower median device-event time, at most 2%
host-total regression, and unchanged frozen correctness. No successor was
implemented or executed in this milestone.

## v33 full-MLP component software readiness

The paper optimization inventory now groups effective mechanisms by state,
prefill, submission, workflow/resource scheduling, physical batching, state
publication, and Ascend lowering. It separately labels safety infrastructure
and falsified alternatives; measurements from different evidence classes are
not compounded.

Source inspection narrows the remaining B32 boundary to the accepted PTO
Vector SwiGLU result in GM followed by dynamic ACLNN Down. The first v33
candidate preserves the accepted stream order and GM materialization, and
adds only a project-owned PTO Down Cube stage. It uses twenty uniform
M32/K64/N256 output-stationary tiles. The earlier concurrent FFTS/FIFO cycle
is excluded.

BiSheng first rejected the independent Down ELF because the existing event
helpers were scoped only to the Gate/Up compile macro. Down-specific helpers
repair that source-visibility failure without changing the accepted Gate/Up
or SwiGLU stage bytes. A subsequent no-device build compiles the Down ELF,
full-MLP wrapper, and extended ACLNN/PTO probe. Focused tests pass. This is
readiness only: no clean-pushed v33 build identity, NPU sample, correctness
output, or component timing is admitted yet.

## v33 full-MLP component lifecycle outcome

The clean-pushed v33 build preserved the accepted Gate/Up and SwiGLU stage
digests and bound the new Down ELF, wrapper, probe, oracle, compiler, and
runtime closure. The sole NPU7 lifecycle nevertheless failed in the control
warmup before any candidate process. Five asynchronous control warmups each
created a fresh ACLNN Down executor, but the harness synchronized only after
all five submissions. The final stream synchronization returned 507035;
control exited 2 with empty stdout and no correctness or timing record.

The independent failure audit accepts with no violations and SHA-256
`fc295d121f18d345aa3bfd425c3263ddff5bed49ef79265549b712cac962fe96`.
It proves candidate absence and successful recovery cleanup. This is
reproducible failure evidence, not a PTO-Down performance result. The source
repair now synchronizes each unmeasured warmup before preparing the next ACLNN
executor; that changed probe requires a fresh component build identity and was
not rerun in v33.

## v34 corrected full-MLP component outcome

The independently accepted r02 build binds clean-pushed parent `a6fd2a3`, the
new probe/source/auditor identities, the unchanged wrapper and three stage
ELFs, the independent oracle, and a networkless device-free container. Its
readiness audit has no violations.

The sole NPU7 lifecycle proves the v33 warmup repair: both arms completed five
warmups and twenty event samples with exit zero. Control device-event/host-total
P50 is 375.430/443.318 us; full-PTO is 361.260/409.668 us. The candidate is
3.7743% faster on device and 7.5905% faster in host total. It therefore misses
the preregistered 5% device threshold while passing the host ceiling. Outputs
are byte-identical and numerically exact; all 9,344 oracle bit mismatches are
signed-zero representation only.

The lifecycle audit still rejects because both arm stderr files contain the
same two `npu-smi` setup warnings. We preserve that violation rather than
weaken the post-run contract. V34 is thus rejected component evidence and
cannot authorize online integration. Cleanup removed the exact carrier and
left NPU7 and scoped ports idle. The evidence points to Down's device compute
and GM dataflow, not executor preparation, as the next optimization boundary.

## v35 first four-card submission: carrier admission failure

The first v35 bundle reached no Down kernel. NPU4--7 each failed in C0 at
`aclrtSetDevice(0)` with status 107001; stdout was empty, each HBM sampler
remained at the idle 5% rate, and no H/C1/profile arm was created. The failure
was symmetric across cards and the image plus three CANN dependency digests
matched successful v34/v22 evidence. The decisive regression was the new
nonprivileged carrier. All four exact containers were removed and every card
had no process or device-file owner afterward. This is runtime-admission
failure evidence, not correctness, PTO, profile, or performance evidence.

The subsequent r02 carrier repair crossed AscendCL and completed an
oracle-exact, stderr-clean C0 on every card, proving the permission diagnosis.
It still produced no candidate comparison: after C0 the runner cleared the
host launcher variable before emitting PID identity, and `jq --argjson`
rejected the empty value. H/C1/profile arms are absent. R02 is therefore an
incomplete lifecycle with valid admission/correctness telemetry only.

R03 crossed the repaired carrier and exposed a kernel correctness defect.
NPU4/5 produced the identical wrong StepK4 control output: 4,608 differing
BF16 words, all within logical block 3's N256 tile at columns 768--1023. NPU6/7
were exact, but their later profiler capture failed because `msprof_raw` did
not yet exist. The lifecycle is rejected and supplies no accepted candidate
delta. PTO examples and source inspection motivated adding the missing
`PIPE_M -> PIPE_FIX` edge before `TSTORE`; the fresh identity also serialized
device lifecycles. R04 then produced a new identical NPU4/5 corruption in
logical block 7 rather than r03's block 3, while NPU6/7 remained exact. This
falsifies both changes as sufficient explanations and weakens a fixed-address
hypothesis. Its
profiler also failed because a shifted shell positional argument made the probe
ELF the `msprof` output parent. R04 is rejected and requires a fresh block-
runtime R0--R1--R0 rotation diagnostic in one ELF plus corrected profiler
argument binding.

The subsequent runtime-rotation r01 diagnostic used the next fresh control ELF
and captured physical card ownership during an eight-second ready hold. NPU4
and NPU6 each produced 15/15 exact outputs across R0--R1--R0; only the declared
card contained the worker. Thus the earlier error disappears after a launch-
ABI/kernel-layout change even at rotation zero, so block-versus-address remains
undecided. The first auditor misclassified all-empty mismatch sets as a fixed
tile; its custody checks are useful, but the interpretation is rejected and
must be rerun under the corrected auditor identity.

The corrected r02 audit accepts the same 30/30 exact runtime-rotation outputs
with `exact_all_rotations` on both NPU4 and NPU6. R05 subsequently exercised
the normal production entry point. NPU4/5 again produced the same 4,608-word
single-tile corruption, now in logical block 11; NPU6/7 completed exact
C0/H/C1. NPU6's same-card prefetch-StepK6 delta is only +0.3854%, but the
four-card screen is incomplete and cannot admit that number as an optimization
result. NPU7's ordinary event runs are exact; its separate msprof application
reported `Resource temporarily unavailable`, leaving no matching project Down
task and causing the independent summary to reject. The contrast between
exact rotated(0) and wrong standard entry points localizes the next repair to
duplicated host launch lowering. The production symbol now delegates to the
single rotated launch site with zero; this repair is pending fresh-artifact
hardware qualification.

R09's post-link audit proved a standard-to-rotated branch, yet r06 still
reproduced the NPU4/5 split: both outputs are byte-identical with 4,608 wrong
words in logical block 15. The sequence of affected blocks is now
3 -> 7 -> 11 -> 15 across r03--r06. NPU6 was exact at 53.100/53.370/53.420 us;
prefetch-StepK6 is 0.2065% slower than its same-card control mean. NPU7's
ordinary C0/H/C1 were exact at 53.160/52.610/52.730 us, but msprof again
contained no project task. The bundle is rejected and all comparative online
fields remain n/a. The next repair removes the standard-versus-rotated ABI
distinction entirely: one five-argument launch symbol serves both paths.

R07 proves that single ABI is also insufficient. NPU4/5 share 4,608 wrong words
in block 19, continuing the +4 tile sequence. NPU6's ordinary arms were exact
at 53.110/53.290/53.040 us but its profile exported no project task. NPU7 was
exact at 52.870/52.900/54.160 us and profiled successfully, but its 2.44%
control drift exceeds the frozen 2% ceiling. The bundle is rejected. Comparing
the exact runtime-rotation path identifies full stream synchronization, rather
than exported entry identity, as the remaining completion-semantic difference.

R08 validates that completion repair for the control: NPU4 and NPU5 C0 are
both byte-exact for the first time. Their candidate H arms then fail exactly:
prefetch-StepK4 on NPU4 and serial-StepK6 on NPU5 each omit logical block 3,
with the same 4,608 mismatches and output SHA `0a20a1bd...780e`. NPU6's
prefetch-StepK6 is exact but 0.1033% slower than its control mean and its
profile lacks a project task. NPU7's reference is exact with 0.26% drift and
an accepted profile. The screen therefore rejects all three optimization
hypotheses. It accepts only the stream-completion repair as an implementation
lesson; no candidate is integrated or used for an online claim.

V36 formal attempt 01 failed before hardware execution. The frozen hash
readiness audit passed, but `native_container_carrier_envmap.py` rejected the
carrier's invented `statecentric-native-container-carrier-v36` format; the
schema-3 payload requires canonical
`statecentric-native-container-carrier-v3`. The controller preserved a 0/6-arm,
zero-request failure record and cleaned NPU7, device FDs and ports. No
performance metric or claim exists. Attempt 02 fixes the contract and makes
readiness explicitly reject noncanonical carrier formats.

V36 formal attempt 02 passed that repaired carrier/readiness boundary and
created N1, but it also stopped before NPU execution. The generic launcher
rebuilt the C++ worker from current main (`a698873c...aa47d`), while the
accepted v49 execution artifact and producer closure bind the historical
frozen worker (`ce7576bd...8845`). The execution-artifact auditor therefore
reported `executor binary identity mismatch`, exactly as the state-identity
contract requires. A clean historical-source reconstruction in the pinned
carrier reproduced `ce7576bd...8845` byte-for-byte. The successor may use
those frozen bytes only through a host/container/producer-closure SHA-checked
launch path; silently accepting the rebuilt worker would invalidate the old
execution and state identity.

V37 recovers the exact v49 C++ executor through a dedicated materialized
launcher while preserving the historical generic-launcher hash. Six fresh
physical-NPU7 lifecycles complete in the frozen alternating order. All 768
requests, 24,576 output tokens, execution/state identities and cleanup checks
pass. Median Native/pinned-vLLM request throughput is 17.4420/15.0726
requests/s; output throughput is 558.1427/482.3236 token/s. The paired
throughput-ratio CI95 is [1.1406, 1.1727]. All frozen wall P95/P99 and TPOT
P50/P95/P99 upper-bound predicates also pass. Native median peak HBM is
44,659 MiB versus 53,461 MiB and reports 100% state hits with 262,144 reused
tokens per lifecycle. TTFT remains incomparable and excluded.

The original total auditor records six image violations because it used the
carrier config digest for Docker inspect `Image`. The carrier itself had
already frozen `Image` as the OCI index-digest field, and all six records equal
that index digest. The separately identity-bound correction auditor changes no
evidence or statistic, accepts with an empty violation list, and opens only the
exact-hot c32/o32 formal cell. Both audit outputs remain part of provenance.

## V39 current-path Native saturation profile

The carrier-only recovery completed on physical NPU7 with 128/128 exact
requests, 4,096/4,096 exact output tokens, zero errors, state hit rate 1.0 and
262,144 effective reused tokens. The physical scheduler emitted eight append
B16 cohorts and 124 decode B32 cohorts. Device-window P50/P95/P99 was
48.051/51.097/52.914 ms; these profiler-perturbed values are diagnostic and are
not compared to vLLM or the unprofiled formal result.

Across 97,289 PipeUtilization rows, aggregate task time was 1,498.243 ms for
PTO Gate/Up, 988.713 ms for attention, 760.555 ms for Down, 329.537 ms for Q,
315.434 ms for O, and 76.143 ms for PTO SwiGLU. Down showed 88.626% Cube
utilization and 97.537% AIC MTE2 activity. SwiGLU-to-Down direct-successor gaps
were 0 us P50 and 0.25 us P95. Direct GM bandwidth and UB occupancy were not
available. The evidence selects heterogeneous 24-Cube Down tiling for a v40
component screen; it establishes no online speedup.

## V40 heterogeneous 24-Cube Down component result

The clean-pushed double build reproduces probe, control and candidate ELFs
byte-for-byte and binds the independent fixture. On physical NPU7, strict
`C0 -> H -> C1` device-event P50 is 53.050/52.260/53.030 us. The control mean
is 53.040 us, control drift is 0.0377%, and the candidate is 1.4706% faster.
All three outputs are byte-identical to the independent CPU BF16 oracle;
stderr is empty and cleanup is complete. This is accepted component evidence
only. It does not mutate v49, project an online improvement, compare vLLM, or
open TTFT/formal gates.
The compact raw lifecycle and build-provenance record is retained under
`results/qwen14b-b32-down-heterogeneous24-v40-r01-npu7/`.

## V41 packed QKV AddMM component result

The clean-pushed, networkless double build reproduces the ACLNN probe and the
73.4-MB packed fixture byte-for-byte. Physical NPU7 then executes one strict
`C0 -> H -> C1` lifecycle with 5 warmups and 50 samples per arm. Device-event
P50 is 285.200/139.200/288.060 us; the candidate reduces the 286.630-us control
mean by 51.4357%, with 1.0028% control drift. Host-total P50 is
346.518/193.617/349.622 us, a 44.3742% candidate reduction.

Every arm produces the same exact `[32,7168]` Q--K--V bytes as the independent
Torch-free CPU oracle, with zero nonfinite values and empty stderr. The final
audit SHA-256 is `c87ac2dd...64b0`, accepts with an empty violation list, and
separately marks the frozen component hypothesis passed. Cleanup leaves NPU7,
device FDs and the owned container empty. This is not an online result or a
vLLM/TTFT comparison; v49 is unchanged. The 72-file tracked record is under
`results/qwen14b-b32-packed-qkv-v41-r01-npu7/`.

## V42 packed-QKV resident integration: software readiness

The default-off production path is implemented but has not yet produced a
hardware result. One physical QKV weight/bias domain now supports compact
serial subviews and one packed physical-B32 AddMM. A single activation
allocation, equal to the prior Q+K+V capacity, is reinterpreted without copies;
the B32 Q/K/V views carry row stride 7168 into RoPE, paged-KV scatter and
incremental attention.

The pack exporter accounts for every source tensor exactly once. C++ contracts
verify the `[7168,5120]`/`[7168]` physical geometry, offsets 0/5120/6144,
non-overlap, compact fallback strides, policy admission, and distinct pack and
resident identities. Python exporter contracts pass. The complete native
suite passes 43/43 after a full networkless build. These are software results,
not evidence that all ACL operators accept the strided device views, and not
an online or vLLM performance result.

The first nonzero-plan rebuild exited successfully but left its outputs only in
an ephemeral container, so it is excluded. The corrected independent builds are
byte-identical: worker `ca98c55c...d7bd`, inspector `0b5a9442...39d5`, embedded
plan `7a7a338c...f39a1`. The generated packed corpus has 48 layers, 384 physical
tensors and 26,426,081,280 packed bytes with unchanged model identity. These
are no-device readiness facts, not a performance result.

An initial packed/serial artifact pair passed its outer audits but is not
hardware-authorized: both referenced the historical descriptor whose nested
leaves bind old worker `ce7576bd...8845` and serial layout
`729a2924...24b5a`. This is a negative identity-readiness result, not a device
failure. The pair is retained as preseal evidence while matched split-seal
control/candidate closures are prepared.

The first matched-seal attempt also stopped before hardware: current sources
derive plan `9c34e92e...62540`, while the reproducible worker embedded the
inherited `7a7a338c...f39a1`. Thus v52 is negative readiness evidence, v53 was
not created, and the earlier double build is not eligible for the device gate.
All v42 performance fields remain n/a.

The corrected no-device builds are byte-identical: worker
`4414922a...c7e4b3`, inspector `fb2d821a...03518f`, both embedding
`9c34e92e...62540`. A tracked-plan verifier closes the generating ancestor,
current protected sources, PTO commit and three stage binaries without
regenerating a parent-sensitive digest. At that checkpoint this was
build/readiness evidence only; no NPU result existed.

V54 serial and v55 packed are now recursively sealed and independently
accepted. Their artifact identities are `90b9aad9...e1ab` and
`bd208500...b6b7e`; descriptors are `0385c52c...68e1` and
`4a3785ec...9543c`; state digests are `001907a2...08d7` and
`01e2cf4c...b4011`. This distinctness is required by the physical QKV layout.
The concrete lock authorizes one hardware lifecycle, but none has run yet, so
all v42 performance fields remain n/a.

Read-only inventory found NPU4--7 healthy and idle at the sampled instant, but
also found foreign long-lived containers with broad device mappings. The v42
carrier was therefore hardened to unprivileged, selected-device mapping before
hardware. No foreign container was changed and no v42 device work has yet run.

R01 then failed in preregistration preflight because the harness used jq's
reserved `label` identifier. No carrier, model load or NPU execution occurred;
NPU7 remained process/FD-free. Cleanup also assumed a not-yet-created output
directory, so its evidence was reconstructed in the r01 namespace. This is a
harness-readiness failure with no correctness or performance sample. R02 is the
sole corrected attempt.

R02 used the corrected unprivileged NPU7 carrier and passed identity, dependency,
process and FD admission. Its C0 application exited 2 with
`configured online PTO policy is protocol-worker only` before loading the
model or submitting device work. H and C1 never started. The independent audit
rejects the incomplete arms and reports empty timing/logit metrics; NPU7 and
the carrier are clean. Therefore the integrated noncompact QKV views remain
untested. The failure is an outer-policy/probe mismatch: v54/v55 selected PTO
as an online policy, whereas the probe accepts PTO only as a separately sealed
component override. No performance or correctness conclusion follows.

## V43 packed-QKV execution-surface repair: device-free readiness

V58 serial and v59 packed correct that authority pairing while retaining the
same worker, frozen plan, PTO stage closure, and respective physical layouts.
Both independently pass outer artifact, runtime-binding, sealed-component, and
aggregate-state audits. Their outer policy is fused ACLNN and their outer
operator-library digest is zero; the nonzero component descriptors remain
`0385c52c...68e1` and `4a3785ec...9543c`.

The corrected policy produces fresh artifact/resident/state identities:
`95ebcced...949ae7`/`65868d8c...92d8c2`/`7633401f...c08ad7` for serial and
`f07f1e36...aa72a3`/`df5c61e5...2c2288`/`a6a2e14e...61cb7b` for packed.
The first no-device builder attempt rejected an unresolved
`libascend_hal.so` before producing an artifact; the corrected builder used a
read-only driver mount and no Davinci devices, then was removed. These are
readiness facts only: no v43 NPU arm, online request, or performance sample has
run yet.

## V43 terminal hardware result: carrier rejection

The sole NPU7 lifecycle passed frozen artifact, dependency, process, FD, disk,
and container admission, then C0 exited 2 at `aclrtSetDevice` with ACL error
107001. HBM samples stayed at the 5% idle reporting floor, no device process
appeared, and no model allocation, operator submission, result JSON, raw
logits, H, or C1 occurred. The independent audit is rejected on six
missing-arm/order/logit checks and contains no timing metrics. Cleanup removed
the owned carrier and left NPU7, FDs, processes, and ports clean.

This is a carrier-permission failure, not packed-QKV or PTO correctness
evidence. Successful historical v21 r11/r12 used the same image and device
mappings with privileged carriers; the v43 carrier was nonprivileged despite
the repository's prior v35 finding that this stack requires the established
privilege closure. No retry is authorized, so integrated packed strides remain
unresolved.

## V44 repair in progress: carrier becomes a state dependency

The repair does not reinterpret ACL 107001 as a model failure and does not
retry v43. Schema-4 stays unchanged. The implementation now forms a canonical
execution-deployment identity from the execution-artifact and carrier
identities, domain-separates the carrier identity into the resident plan, and
binds carrier/deployment semantic and record digests into the independently
audited state chain. Focused Python/contract tests pass 42/42 and the rebuilt
resident-plan C++ test passes; no v44 NPU execution or performance result has
yet been produced. The complete checkpoint passes 657 project Python tests
plus 127 subtests and six expected skips, 138 Rust tests, and 43/43 Native
CTests. The 39-page paper rebuild is `589ada19...6b225a`, with clean fatal log
checks and visually accepted carrier-identity text on pages 6 and 15.

## V44 r01 and v45 successor: inherited entrypoint repair

V44 r01 stopped before C0. The privileged NPU7 carrier passed process, FD,
device, image, and runtime-library collection, but its live audit rejected the
only differing field: the contract said `entrypoint=null`, while Docker
inherited the image's four-element Ascend setup entrypoint. No model weights,
operator, logits, timing, or performance sample exists. Cleanup removed the
owned container and NPU7 remained process/FD-free.

V45 repairs the contract rather than bypassing the audit. It introduces a
successor carrier compiler that requires the complete inherited entrypoint,
does not truncate it through `--entrypoint`, and is accepted by execution-
deployment identity loading. Unit tests reject null and partial entrypoints.
Fresh v62/v63 identities and the sole v45 hardware lifecycle remain pending;
there is still no integrated correctness or online performance result.

## V45 r01: packed AddMM reaches an unsupported RoPE view

The entrypoint repair works: the privileged carrier live audit accepts and C0
loads the 14B model on NPU7. C0 exits zero with all frozen greedy decisions
correct, sealed PTO Gate/Up active, B32 raw logits saved, 30.513-ms diagnostic
elapsed time, and 68% peak reported HBM. H also loads the model and submits the
packed QKV AddMM, but ACLNN rejects its noncompact Q/K views at RoPE workspace
admission with status 561103. H emits no logits and C1 never starts. The
independent audit rejects the incomplete sequence; cleanup leaves no device
process, FD, or owned container. This is correctness localization, not a
performance comparison.

The v46 software repair keeps one packed AddMM and uses three same-stream
device 2-D DMA operations to place Q/K/V in compact slices of the existing Gate
arena before RoPE. Focused source contracts require exactly three D2D 2-D
copies, compact downstream strides, no new runtime allocation, and preservation
of the one packed projection. A no-device build succeeds; hardware evidence is
not yet available.

V46 r01 completes all three arms and proves that the compact-consumer repair
removes the RoPE admission failure. All arms exit zero, every B32 greedy
decision matches the frozen independent oracle, and cleanup is complete.
However, the preregistered bitwise cross-arm predicate rejects: the two serial
controls are byte-identical while the packed arm differs. Its oracle error is
slightly lower, which identifies a valid BF16 AddMM tiling/reduction difference
rather than an indexing or DMA corruption. The packed arm is also 7.3417%
slower than the serial-control mean. Preserve v46 as a negative component
result; no online or vLLM conclusion follows.

V47 r02 runs the packed projection and its compacting copies as separate device
stages. Every arm is exact, but the independent audit rejects the 11.26% serial
control drift. Packed AddMM is 147.57 us; three 2-D D2D copies alone are
310.72 us and the combined arm is 440.24 us. This is sufficient diagnosis to
choose a one-launch AIV/PTO compact consumer, but not an accepted performance
comparison or serving result.

V48 r01 establishes that the first one-launch implementation is not usable.
Its three-DMA control is byte-exact at 340.69 us device-event P50. The PTO arm
does not complete its first warmup in 300 seconds, emits empty stdout/stderr,
and holds 33% reported AIV utilization until forced termination; C1 never
starts. Cleanup removes the exact container and leaves no NPU7 process or FD.
There is no PTO timing, speed ratio, online result, or vLLM comparison. The
next repair replaces per-tile pipeline waits with three bulk segment transfers.

V49 validates that bulk transfer removes noncompletion but not correctness.
H finishes 5 warmups and 50 samples at a diagnostic 19.23-us device median,
then fails the independent oracle with 204,101 mismatches and 407 nonfinite
values; C1 is not run. Inspection identifies an existing documented PTO rule:
automatic passes define `__PTO_AUTO__`, under which manual wait helpers are
empty. The apparent latency is invalid. Cleanup is complete; v50 disables the
auto pass exactly as the accepted standalone manual-sync PTO path does.

V50 manual synchronization removes the v49 nonfinite corruption but is still
not correct. H completes at a diagnostic 14.74-us median; K and V are byte-
exact, while the five-tile Q helper transfer has 40,960 mismatched elements.
C1 is absent and cleanup passes. V51 will synchronize each 1024-element helper
tile, retaining seven dependency pairs per row and all other geometry.

V51 is also Q-incorrect: H reports 115,238 Q mismatches, exact K/V, zero
nonfinite values, and a diagnostic-only 5.98-us median. Cleanup passes. The
successor uses all 48 AIV cores and the proven global-tile schedule from the
accepted standalone PTO SwiGLU path.

V52 global tiling remains incorrect (86,088 mismatches) despite a diagnostic
7.57-us median. V53 tests a Vector-staged UB pipeline; no v52 ratio is valid.

V53 Vector staging completes at a diagnostic 6.81-us median but remains
incorrect with 78,366 finite mismatches across Q/K/V. Exact late-oracle tiles
appear in early destinations, identifying cross-iteration UB reuse. C0 is
exact at 189.43 us, C1 is absent, and cleanup passes. Neither timing forms a
component ratio or online comparison.

V54 adds direct manual reuse fences but completes no H warmup before bounded
termination while reporting 66% AIV utilization. C0 alone is exact at
343.92 us. Cleanup passes; there is no candidate latency, speed ratio, online
result, or vLLM comparison.

V55 has no device result. Its two auto-pass ELFs differ at executable AIV
instruction bytes (`31fb...0b34` versus `88fd...8e4e`), so reproducibility
admission rejects the candidate before preregistration or NPU use.

V56 also has no device result: the compiler ignores the proposed deterministic
compile-unit flag and reproduces v55's two executable hashes exactly. The
automatic scheduling branch is closed without selecting either artifact.

V57 is the first exact one-launch PTO compactor. C0/H/C1 are byte-identical
with device-event P50 194.130/34.320/186.300 us. The candidate is 81.96% below
the control mean, but the audit rejects 4.03% control drift against the frozen
2% limit. This remains diagnostic component evidence, not an accepted ratio.

V58 remains exact but increasing support exposes rather than removes phase
drift: C0/H/C1 are 188.920/24.700/333.260 us and control drift is 76.4%.
The audit rejects; the next probe must pair adjacent samples in one process.

V59 accepts that paired measurement: DMA/PTO medians are 223.900/29.250 us,
median paired reduction is 85.29%, and PTO is faster in every one of 200 pairs.
Both outputs are byte-exact. This is accepted component evidence, not serving
throughput or a vLLM comparison.

## V60 PTO-QKV full-model integration: software checkpoint

The accepted v57 QKV ELF is now reachable from the full-model packed consumer
through one stable launch ABI. Execution-artifact schema v5 adds an independent
QKV-library digest and both C++ and Python audits reject missing, substituted or
legacy-bound libraries. A fresh container build compiles the worker and passes
the C++ round-trip/substitution tests; the focused software suite passes 54
tests. The composite v60 plan compiler and candidate/control artifact preparer
are implemented, but no v60 plan, artifact, NPU run, online request or
Native/vLLM result has yet been frozen. Thus this checkpoint contains no new
performance result and does not unlock NPU4.

Pre-hardware audit subsequently supersedes v60: its output proves identity
validation and load but does not expose successful QKV dispatches. V61 adds
backend and dispatch-count telemetry and must regenerate the complete plan,
worker, artifact and state chain. No v60 artifact or hardware lifecycle is
authorized.

The clean-pushed v61 successor now has immutable composite plan identity
`993df80ae9df121d300a2f063fe6f17d9d27efa953845e711cd2295cf4f50967`,
derived from parent `ed0f6cee52193398d9410c89e61cbfd74f6f7315` and binding
QKV ELF `af50d373...e52ae`. This is still software provenance only: correctness,
full-model performance and formal gates remain closed.

Two fresh networkless, device-free builds bind that plan and produce identical
worker SHA-256 `60d9876f...dea1e`; both C++ artifact-identity tests pass. This
reproducibility checkpoint mints neither runtime artifacts nor NPU samples.

The v61 runner, independent auditor and privileged NPU7 carrier are now defined
before artifact creation. They freeze C0/H/C1 order, exact H dispatch count 96,
control count zero, frozen semantic-oracle gates, complete custody capture and
cleanup. This is protocol construction, not a hardware result.

The first v66 mint attempt exits before creating its namespace because the
minimal plan-bound build omitted the resident-plan inspector. Rebuilding that
tool twice gives identical SHA-256 `778104be...c6ec0e` without changing worker
bytes. This pre-execution failure contributes no artifact or NPU result.

A second no-device attempt first diagnoses a missing read-only driver mount;
after correcting that builder closure, v66 preseal completes but sealed
descriptor compilation rejects key `lowering`. Composite v61 intentionally
uses `mlp_lowering`, and also omits explicit FFTS/FIFO fields. V61 is therefore
superseded without hardware; v62 repairs the typed producer contract and will
use fresh artifact namespaces.

The repaired v62 composite plan is frozen at identity `cb0b60e3...39fc87`
from clean parent `d09d648`; it explicitly records no FFTS/FIFO scheduling and
binds the sealed producer/auditor sources. No worker, artifact or hardware
result exists for v62 at this checkpoint.

Two fresh no-device v62 builds are byte-identical at worker SHA-256
`5d2805d8...4152c9` and inspector `951313d9...ebbbdc`; both identity tests
pass. This closes artifact-producer readiness but remains non-hardware evidence.

The v62 runner, auditor and carrier are frozen before artifact creation.
Carrier identity is `d5e2d12b...ddd57`; the lifecycle remains NPU7-only and
contains no timing or correctness sample yet.

Fresh v68/v69 artifact creation now succeeds without a device. V68 control is
schema v4 at record `2f1dbcc4...794fc5` with a zero QKV leaf; v69 candidate is
schema v5 at `f2ca6777...eb9c84` and binds QKV ELF `af50d373...e52ae`.
Runtime, independent, state and sealed-component audits accept both. Their
resident and state identities are distinct as required; no model ran.

The single NPU7 v62 C0/H/C1 lifecycle accepts with no violations. All arms
exit zero and match every frozen greedy decision; dispatch counts are 0/96/0.
C0/H/C1 measured decode is 30.583327/30.987029/30.759237 ms, the serial mean is
30.671282 ms, control drift is 0.575%, and PTO QKV regresses the full model by
1.029%. Peak HBM is 68% for every arm. Raw logits differ only for the alternate
packed GEMM decomposition and are diagnostic, not the semantic gate. Cleanup
removes the owned container/process/FD and leaves NPU7 idle.
## V63 B16 online-pair readiness repair

The accepted v62 gate exposed a pre-execution incompatibility in the old NPU4
runner: its timing-v1 state and historical Rust/C++ binaries are correctly
rejected by the current timing-v5 protocol. Recreating the missing container
would not repair that identity mismatch. V63 instead adds an identity-bound
host-network/NPU4 carrier and a fresh revision-10 B16 artifact path using the
release Rust bundle and current C++ producer closure. Nineteen focused tests
pass. This is software readiness only; Native/vLLM throughput, latency, TPOT,
HBM and correctness are n/a until the fresh v71 artifact and paired lifecycle
run. `formal_gate_open=false`, `performance_claim=false`, and no TTFT
comparison is made.
## Rejected v63 preparation attempt

The first NPU4 carrier preparation is retained under
`.benchmarks/qwen14b-b16-online-pair-v63-preparation`. The live carrier audit
accepted identity `7c75bda2...5ca9`, but CTest exited 8 before artifact/model
execution: 15 test executables were not part of the minimal transferred build,
and one shell contract used a stale `dlopen` ordinal. This is preparation
failure evidence, not a Native or vLLM performance result. No v70 namespace
was created, NPU4 was empty before and after, and cleanup removed the owned
container.

The repaired software uses semantic-scope ordering, exact three-binary build
qualification, and a shared explicit pair-container route. It passes 774
Python tests plus 127 subtests (six expected skips) and 138 Rust tests. No
c32/o32 performance number is reported until the new preparation, lock, and
fresh paired lifecycle accept.

Preparation-v2 passed the corrected minimal-build gate, accepted carrier
`699b1669...15c3`, and matched all four runtime dependency digests. It then
exited 2 because the execution-deployment identity dispatcher lacked a v63
typed-loader branch. Only a partial v70 preseal exists; no state identity,
readiness, model execution, or online metric was produced. Cleanup again left
NPU4, its device FD, and paired ports empty. The repaired successor is v71 with
carrier identity `96161605...4c20`.

Preparation-v3c reached independent state-identity audit under
`96161605...4c20`; it rejected scheduler and aggregate compatibility digests
because v18 production omitted canonical zero-valued decode-group and
admission-cache fields. The partial v71 preseal has no readiness or online
sample. Two earlier controller validations never created a carrier. All three
paths left NPU4 untouched. V72 repairs cumulative-domain canonicalization and
binds the shared preparer core; its carrier identity is `99510cd9...e8749`.

Preparation-v4 then isolated ordering rather than membership: all v18 fields
were present, but incremental producer order placed inherited zeros after
newer closure/publication fields. The independent state audit again rejected
scheduler and aggregate digests before readiness/model/NPU work. V72 is
preserved; v73 performs one canonical schema-order pass under carrier
`b23923f2...bed66`.

Preparation-v5 accepts all pre-execution gates and mints v73. Its execution
artifact identity is `3ac3a2ab...5f1e`, resident identity is
`bf69a277...9b29`, state-compatibility digest is `a06972d7...b62`, and carrier
identity is `b23923f2...bed66`. No model, request, token or timing sample exists
in this preparation result; NPU4 and owned resources are clean. The frozen v63
pair lock self-identity is `18b0e6ae...64f1`.

The first locked v63 online attempt produces no comparison. An auxiliary
controller-v1 fails before carrier creation on a field-name adapter in its
extra audit. Controller-v2 then accepts the lock, live carrier and pinned OPP.
Native exits 2 before model work because the frozen independent oracle carries
historical producer provenance rather than the new serving-container identity.
The baseline subsequently enters NPU4 but EngineCore exits while loading shard
1/8, before health or any request. Independent pair audit rejects; request/s,
output token/s, latency, TPOT, error/reuse rates and peak measured model HBM are
n/a. The carrier is removed and NPU4/FD/ports are clean.

V64 repairs only the proven Native authority mismatch and preserves the
baseline load failure for a fresh retry. Its expanded carrier identity is
`f75a043a...85cb5`; no v74 artifact or performance result exists at this
checkpoint.
## V74/v64 B16 pair preparation

The fresh v64 preparation lifecycle completes without model or NPU execution.
Carrier, runtime dependency, execution artifact, deployment, native-state and
independent audits accept; preparer and exact-container removal exit 0, absence
inspection exits 1, stderr is empty, and NPU4 process/FD evidence is empty
before and after. V74 binds carrier `f75a043a...85cb5`, deployment
`ee6718cb...d842`, scheduler `49d7048b...8e4` and compatibility
`2cd38391...e8b1`. Lock `5df7989d...aac54` authorizes only one fresh v64-r01
diagnostic pair. There are no requests or performance metrics yet; all formal,
performance and TTFT-comparison gates remain closed.

## V64-r01 rejected NPU4 pair and V65 repair

V64-r01 completes no request. Native exits 2 before loading Qwen because the
build helper sends CMake to the isolated container path but validates binaries
under the default host path. Baseline reaches real NPU4 model loading and
consumes 28,345 MB after shard 1/8; the host watchdog then records PID 1130508
in carrier `c105c61b...d4dc1` as `terminated`. Its configuration watched
NPU0--4 but mapped approved runners only for NPU0--3, making every NPU4 process
unauthorized. Pair/remove/absence codes are 1/0/1 and cleanup is complete.
Rejected record identity is `9477ec24...a4662`; comparison SHA-256 is
`d5e067f5...4adf8`. All comparative metrics are unavailable; formal,
performance, and TTFT gates stay closed.

V65 separates host/container build namespaces and moves the user-authorized
NPU4 outside the GitHub-runner-only watch domain while leaving NPU0--3
protected. Carrier `bad139cd...401a9` binds both repairs plus watchdog program
and configuration hashes. This is readiness work, not an online result.

V75 preparation r01 stops before container creation because its custody script
references a nonexistent v65 materializer name; its separate failure namespace
contains no artifact or NPU work. R02 reuses the byte-identical, identity-bound
v64 materializer under the fresh v65 launcher namespace and accepts every host-
admission, live-carrier, dependency, artifact, deployment, state, runtime, and
independent audit. Preparer/remove/absence codes are 0/0/1; NPU4 and FDs are
empty before and after. Artifact identity remains `3ac3a2ab...5f1e`, while
resident `72595201...cd59`, scheduler `1936ec83...0265`, compatibility
`709ccd0a...f625`, deployment `0f954240...865b`, and C++ producer closure
`27d6d1ae...6d07f` change. Lock `5266f720...69920` authorizes only v65-r01.
This remains no-model readiness evidence with all performance fields `n/a`.

V65-r01 then exposes a different fail-closed boundary. Native reads every
layer/global pack but completes zero requests: an unconditional online rebuild
changes the frozen executor from `5d2805d8...4152c9` to
`5c4f5af1...91fc8`, and `/proc/self/exe` validation rejects before NPU
allocation. The baseline arm is independently successful and oracle-exact for
128/128 requests and 4,096 tokens: 14.7694 request/s, 472.6204 output token/s,
wall P50/P95/P99 2127.58/2237.47/2241.83 ms, TPOT P50/P95/P99
46.804/50.564/57.809 ms, zero errors and 53,461-MiB peak HBM. Because Native
has no online sample, no ratio or paired conclusion exists; TTFT remains
incomparable. Cleanup codes are 1/0/1 and NPU4/FD/ports/carrier are empty.

V66 implements the evidence-selected repair: a read-only, expected-digest
build gate and untouched reproducible build-b. Focused behavioral and contract
tests accept correct host/container bytes and reject a substituted digest
without mutation. This is repair readiness, not a performance result.

V66 preparation-r01 reaches no artifact or NPU work. The carrier starts, but
the live audit incorrectly expects Docker inspect to contain the typed
repository build policy and rejects. Exact removal and absence checks are 0/1;
NPU4, FDs and ports remain empty. This is preparation failure evidence with all
performance fields `n/a`; R02 uses a fresh namespace after the projection fix.
R02 accepts the corrected live audit, then exits before artifact creation
because the delegated preparer ignores the exported build-b selection and
checks hard-coded build-a. Exact cleanup again passes, with no model/NPU work
and every performance field `n/a`.
R03 then reaches the common artifact dispatcher, which rejects carrier-v66
before output because the whitelist ends at v65. No artifact/model/NPU work is
created and cleanup remains exact. This is another preparation failure with all
performance fields `n/a`.
R04 accepts the complete typed closure and creates v76 without loading the
model or executing on NPU4. Carrier, runtime-binding, deployment, state and
independent audits all accept; cleanup is 0/0/1 and NPU4/FD/ports/container are
empty afterward. Carrier/deployment/state identities are `8786c0be...cb04`,
`c14b2724...6baa`, and `020f1bd2...0f00`. This is readiness evidence only;
all online performance fields remain `n/a`.
V66-r01 then proves frozen build admission no longer mutates the executor, but
exposes an ordering defect before Native service launch: the admission record
is redirected into a result directory that has not yet been created. Native
completes zero requests and has no ordinary failure bundle; the controller
stderr is the preserved observability boundary. The baseline independently
completes 128/128 exact requests and 4,096 tokens at 14.8843 request/s and
476.2986 output token/s, with 53,461-MiB peak HBM. The pair is rejected and no
ratio exists. V67 binds the result-namespace-before-admission repair.
Fresh V67 preparation creates V77 and accepts carrier, deployment, state,
runtime-binding and independent audits without model or NPU execution. Cleanup
is 0/0/1 and NPU4 is empty. All online metrics remain `n/a`; this readiness
record only authorizes a fresh V67-r01 pair under the new lock identity.
V67-r01 then rejects before NPU allocation because authenticated build-b embeds
decode plan `cb0b60e3...fc87` while v77's eager artifact records zero. Baseline
completes 128/128 exact requests at 14.5272 request/s and 464.8713 output
token/s with 53,461-MiB peak HBM. The pair has no Native metric or ratio;
cleanup is exact and V68 will bind a fresh zero-plan eager executor.
V68's isolated build succeeds without NPU work. The fresh executor is
`5c4f5af1...91fc8`; host and container inspectors both report a zero plan, and
cleanup is 0/0/1. Carrier v68 identity `30e6f67e...1b63` binds that semantic
build closure. This is repair readiness, not an online result.
V78 preparation r01 stops before container creation on a stale controller path;
r02 passes live carrier audit but the legacy delegate compares the eager build
to the v62 PTO record. Both create no artifact and execute no model/NPU work.
The successor binds a typed v68 build record and fresh carrier identity before
r03; all online metrics remain `n/a`.
R03 accepts carrier, artifact, deployment, state, runtime-binding and
independent audits and creates v78 without model/NPU work. Cleanup is 0/0/1.
Artifact/deployment/state-record identities are `9fa5ab88...6423`,
`bc1c7cd8...2574`, and `286f58ae...1436`; this is readiness only.

V68-r01 executes both real online arms and both are independently oracle-exact
for 128/128 requests and 4,096 tokens. Native physical B16 at client c32 records
11.6434 request/s, 372.5904 output token/s, wall P50/P95/P99
2277.11/2801.50/2804.87 ms, TPOT P50/P95/P99
57.832/68.909/68.935 ms, zero errors, 100% state hits, 262,144 effective reused
tokens, and 40,544-MiB peak HBM. Pinned vLLM records 14.8110 request/s,
473.9511 output token/s, wall P50/P95/P99 2119.60/2208.37/2220.63 ms, TPOT
P50/P95/P99 46.242/50.250/57.037 ms, zero errors, and 53,461-MiB peak HBM.

The point estimate places Native 21.39% below vLLM in request and output-token
rate, but the pair is rejected: online Native omitted the carrier identity and
used noncanonical scheduler identity material, while runner/auditor policy
expectations were stale. This is retained negative exploration evidence, not a
publishable paired conclusion. Cleanup codes are 1/0/1 and NPU4, device FDs,
ports, processes, and the exact carrier are empty. Rejected identity is
`a35b930f...f28`; V69 repairs identity reconciliation before a fresh rerun.

V79 preparation then passed every offline audit and executed no model, but its
mandatory online-identity preflight found that the pair was still inadmissible:
the preparer froze workflow prefill cohort 16 while the V69 wrapper would leave
the launcher at cohort 0. Resident identity matched, but scheduler and aggregate
state identities did not. We preserve V69 as a pre-execution rejection with no
performance sample and advance to a fresh V70 closure that explicitly exports
the workflow identity.

V80 then passes every offline audit without model execution, and the independent
online projection reproduces all three locked identities: resident
`023a4693...91b6`, scheduler `7ae203f5...be52`, and aggregate state
`25045bbf...e87f`. The self-authenticating V70 lock is `385cab06...428a`.
This is readiness evidence only; it authorizes one fresh NPU4 pair and supplies
no performance metric by itself.

V70-r01 passes the no-model online identity preflight but fails before Native
model load because its frozen launcher uses an undefined `native_build_dir` at
frozen-build admission. Consequently there is no Native performance sample and
no pair ratio. The separately fresh baseline completes 128/128 frozen-oracle-
exact requests at 15.1495 request/s and 484.7844 output token/s with zero
errors and 53,461-MiB peak HBM; it remains standalone diagnostic evidence.
Cleanup leaves NPU4, device FDs, ports and the exact carrier empty. The outcome
is preserved by rejected identity `3608924c...eca1`; TTFT is not compared and
the formal gate remains closed.

V71 repairs the launcher generator rather than the frozen V70 bytes. It applies
the V63 build-directory binding before the V64 oracle and V67 admission
transforms, then verifies generated-shell syntax and definition-before-use.
The repaired launcher digest is `6396c222...8265` and fresh carrier identity is
`2f0ae620...3fe`; neither is yet a model-execution result.

The repair passes 838 project Python tests, 127 subtests and six expected
skips. Tectonic builds a visually checked 44-page PDF at SHA-256
`180a679f...178f`; only known underfull warnings remain.

Fresh V81 preparation accepts the complete carrier/artifact/state/runtime
closure without model or NPU execution and cleans 0/0/1. The self-authenticating
V71 lock is `cc72ebc8...91e3`; its independent online preflight exactly
reproduces resident `8057a95d...1219`, scheduler `6112d5eb...dde20`, and state
`785bc60b...0c28`. This is readiness evidence only and authorizes one fresh
V71-r01 pair after a clean push.

The lock checkpoint passes 840 project Python tests, 127 subtests and six
expected skips. The visually checked 44-page paper SHA-256 is
`600c3b56...e6a8`; only known underfull warnings remain.

V71-r01 completes both exact online arms but is rejected by two stale
workflow-marker checks. Native physical B16/client c32 is 11.6264 request/s
versus 15.0028 for pinned vLLM, an unaccepted -22.51% point; state hit is 100%,
reuse 262,144 tokens, and peaks are 40,544 versus 53,461 MiB. Explicit-prefill-
v3 produces four full markers, whereas the frozen auditor expected the old 2+2
implicit pattern. V72 binds the policy-aware auditor into fresh carrier/state
identity; V71 is not retroactively accepted and TTFT remains incomparable.

The V72 repair passes 844 project Python tests, 127 subtests and six expected
skips. Its 44-page Tectonic PDF is `62531513...4de5`; pages 36 and 43 are
visually clean and only known underfull warnings remain.

V82 preparation and V72 online identity projection accept without model/NPU
execution and clean 0/0/1. Lock `43df4caf...3da7` binds the policy-aware auditor
and exact resident/scheduler/state identities. It is readiness only and permits
one fresh V72-r01 pair after clean push.

The V72 lock checkpoint passes 846 project Python tests, 127 subtests and six
expected skips. The previously built paper remains visually checked at
`62531513...4de5`.

## V72-r01 accepted c32/o32 diagnostic

The fresh policy-aware pair accepts with zero audit violations. Both arms
complete 128/128 frozen-oracle-exact requests and 4,096 output tokens with zero
errors. Native explicitly separates client concurrency 32 from physical B16.
It records 11.5866 request/s and 370.7717 output token/s versus pinned vLLM's
14.6161 and 467.7151, a -20.73% Native diagnostic point. Native wall
P50/P95/P99 is 2289.25/2817.53/2821.23 ms and TPOT is
58.259/69.396/69.421 ms; baseline values are 2149.20/2273.38/2284.34 ms and
47.155/51.075/57.651 ms. Native hit rate is 1.0 with 262,144 effective reused
tokens. Peak HBM is 40,544 versus 53,461 MiB.

This result closes the requested diagnostic milestone but does not open the
formal gate. It establishes correctness, state reuse, accepted provenance and
a real negative performance point; it does not authorize TTFT claims, formal
3+3, B32, o128, COW, later matrices, or MiniMax work.

Final validation passes 847 project Python tests, 127 subtests and six expected
skips. The 45-page Tectonic paper SHA-256 is `f2b8fd89...d9257`; the updated
evaluation and discussion pages 36 and 43 are visually clean. Only known
underfull warnings remain.

### V73 profiling checkpoint (no performance result)

V73 freezes a physical-NPU7, client-c32/physical-B16, c32/o32 Native-only
task-bearing profile of the accepted V72 execution semantics. This checkpoint
contains no hardware measurement and no speed claim. Its purpose is to resolve
the 26.83-ms median device-completion interval into executable tasks before one
new Ascend-native mechanism is chosen. Profiler throughput and TTFT are
explicitly non-comparable.

V73-r01 stopped before worker/model/profiler execution. Its carrier mapped NPU7
but inherited NPU4 visibility environment, and its runner did not canonicalize
the absent zero-plan metadata field. The exact carrier was removed and NPU7,
FDs, ports and containers match their pre-run snapshots. This is rejected
pre-execution evidence with no performance metric. V74 is the fresh successor.

The V74 successor was rejected during closure review, before any container or
accelerator action. Its inherited launcher would reject the profile path, made
unscoped device inventory calls, and lacked a runtime digest gate. Consequently
V74 contributes no metric. V75 repairs the closure and also retains LM head in
critical-path ranking; this remains readiness work, not an optimization result.

V75-r01 also produced no performance sample. It passed the selected-NPU closure
gate and started its carrier, then failed independent-oracle admission before
worker/model/profiler execution because the runner omitted the frozen-producer
mode. NPU7, FD, port, and container snapshots match. V76 is a one-line semantic
successor; no conclusion is drawn from V75.

V76-r01 stopped even earlier, before container creation, because namespace
rewriting changed the shared launcher filename. It has no hardware or
performance sample. V77 restores and digest-tests the shared path.

V77-r01 likewise has no hardware or performance sample: shared auditor and
analyzer paths were still rewritten. V78 verifies the complete three-file
shared closure before execution.

## V79 B16 Down BF16-NZ screen: rejected negative

The single NPU7 C0/H/C1 lifecycle completes all three component arms with zero
exit status, empty stderr and byte-exact output against the independent frozen
oracle. ACLNN-ND controls measure 139.090 and 133.040 us device-event P50;
their 136.065-us mean is the preregistered reference. The BF16
GroupedMatmulWeightNz/FRACTAL_NZ candidate measures 326.930 us and allocates
16,777,728 workspace bytes, a 140.27% regression.

Control drift is 4.45%, exceeding the frozen 2% limit, so the independent audit
rejects even before the 5% positive gate. The result cannot authorize online
integration, a state-identity reissue or an NPU4 pair. Cleanup removed the
carrier and left NPU7 process and device-FD state empty. Rejected record
identity is `2536d762...9ebf`; `formal_gate_open=false` and TTFT is absent.

## V105 physical-B32 decode screen: accepted positive

V100--V104 are zero-request pre-execution rejections. V105 completes one NPU7
C0/H/C1 lifecycle at 11.5116/17.2734/11.6852 request/s. All 384 requests are
exact with zero errors and full reuse. Control drift is 1.50% and H improves
48.93%, so independent audit accepts. Cleanup is exact. This authorizes an
NPU4 idle check for a separate matched pair; formal and TTFT gates remain shut.

## V278 accepted cold-prefill stage attribution

One exact B16/P2177 NPU4 lifecycle attributes the 48-layer cold-prefill device
time as MLP+norm 67.5467%, QKV+RoPE+KV 12.4597%, attention 11.6954%, and
O-projection+norm 8.2982%. All 16 outputs equal the frozen token 51741 and the
four stages reproduce total device time within 1.70e-7%. This accepted
diagnostic success selects MLP+norm for V279; instrumented throughput and a
vLLM-HUST comparison are explicitly N/A.

## V279 combined cold-prefill screen: design-invalid

All 15 lifecycles are exact and raw medians improve 2.1105% in MLP+norm and
2.0691% in full prefill, but candidate changed both Gate-Up projection fusion
and Silu+Mul activation fusion. Preserve the observation without accepting it
or authorizing online testing; V280 isolates activation fusion.

## V280 accepted cold-prefill activation attribution

V280 holds one fused Gate-Up ACLNN Matmul and its contiguous output constant
in both arms, changing only separate Silu+Mul into one ACLNN SwiGLU call. The
complete admission plus two-warmup/five-measured alternating fresh-process
campaign has 15/15 exact lifecycles and 48 profiled layers per lifecycle.
Measured median MLP+norm time falls from 2.948820313 to 2.720644821 seconds
(+7.7378568%), while full-prefill time falls from 4.383365962 to 4.242042593
seconds (+3.2240833%). The candidate wins 5/5 measured pairs in both metrics;
control MLP CV is 0.1275584%. Independent audit exactly reproduces runner
result SHA `fd2ec43c...cacfef`, and NPU4 is clean. This is an accepted
activation-attribution success, not request/s or vLLM-HUST evidence; V281 must
close the matched c16/o128 online cell.

## V281 accepted matched c16/o128 online activation result

V281 completes the missing current-Native comparison on the exact frozen
independent-cold c16/o128 cell. Three fresh-service controls give median
1.759617 request/s; three fused-SwiGLU candidates give 1.778720 request/s, an
online A/B gain of 1.085635%. Against the immutable HUST median 1.711858, the
current Native candidate is 3.905824% faster. All six lifecycles use 10 warmups
and 128 measured 2,206-token prompts, produce 128 exact output tokens per
request, and observe zero hit/reuse. Independent recomputation exactly matches
result SHA `abbbcfa09c4e4820ce11ac8bb253ca2dd056e936251b5a6ceb941dc27395194d`.
This result covers only independent-cold c16/o128; HUST was not rerun.

## V282 accepted matched c32/o32 task attribution

V282 closes the previously missing cross-runtime profile on the exact
independent-cold c32/o32 cell. The accepted Native r10 trace contains 245,991
tasks over 20.780810 seconds; the accepted HUST r15 trace contains 388,206
tasks over 34.911986 seconds. Both summaries have empty violation lists and
the final controller, workload, profiler export, and NPU4 cleanup gates pass.
The profiled request rates (3.077557 Native and 3.353780 HUST) remain unscored.

The actionable difference is submission cadence. The r16 offline audit merges
overlapping task intervals across every stream: Native leaves 9.094216 seconds
device-wide uncovered at 69.5592% task-union utilization, versus HUST's
7.157238 seconds and 76.0287%. Thus Native has 1.936979 seconds (27.06%) more
idle and 6.47 percentage points lower utilization. Native also has 155,866
gaps of at least 10 us versus HUST's 48,333, selecting repeated eager host
submission/preparation for the next optimization. This is not a throughput
claim and does not alter the frozen 3.134766/3.375526 request/s comparison.

## Issue #3 variable-length ShareGPT feedback admission

The fresh default-off feedback bundle and state16/physical-B16 artifact pass a
matched 1+1 on the deterministic first 16 rows of the canonical V292 ShareGPT
workload. Both arms complete 16/16 cold requests with zero validation or
lifecycle failures, and all generated token IDs match across arms. The
candidate records 924 counter updates with zero drops; the control exports no
feedback snapshot. Peak HBM is 53,545 versus 53,544 MiB.

Request throughput is 0.573357921 req/s off and 0.572229729 req/s
counters-only, a single-run -0.1968% delta. TTFT P50/P95/P99 is
311.263/360.617/382.695 ms versus 307.660/349.951/367.561 ms; TPOT is
29.893/32.752/38.515 ms versus 30.027/33.110/38.845 ms. This is accepted
mechanism/coverage evidence only: no speedup, full-workload overhead, or
vLLM-HUST claim is made.

R1 and R2 are retained pre-execution rejections. R1 used a disallowed nested
probe evidence root. R2 found that the HTTP launcher treated an all-zero
optional weight-load-plan digest as present, contrary to the binary artifact
and independent auditors. The narrow canonical-absence fix passes host and
official-container regressions; R3 is the sole NPU result.

## Issue #3 agent state-tree feedback overhead (2026-08-14)

The r3 campaign closes the missing agent workload with a 14-request,
four-branch state tree. A same-checkpoint torch-NPU oracle was generated twice
in fresh official-image processes and agrees exactly on six tokens. All three
control and three candidate fresh-process runs are token/lifecycle exact. Each
candidate records 8 updates, 0 drops, 22 hits and 1 miss; controls expose no
feedback snapshot.

Median throughput is 13.620299 req/s off and 13.454486 req/s counters-only,
a -1.217394% candidate delta. Median request P99 is 88.514757 versus
86.933268 ms (-1.786695%), and peak HBM medians are 53,532 versus 53,533 MiB.
The tail gate passes, but throughput exceeds the preregistered 1% regression
limit. This is a default-off overhead rejection, not a speedup result. R1's
wrong-model oracle and R2's wrong continuation expectation are retained and
excluded from the aggregate.

## Issue #3 acceptance-boundary correction (2026-08-14)

No new NPU run was performed. Preserve the repeated-prefix counters-only 3+3
overhead pass and the agent 3+3 negative result. Preserve ShareGPT as exact
mechanism evidence only: its frozen preregistration calls the first-16-row 1+1
an `unscored-admission`, with `performance_claim=false` and
`full_sharegpt_overhead_claim=false`.

The three workload classes therefore have counters-only correctness coverage,
but the original issue remains incomplete. It requires a formal three-start
ShareGPT A/B, sampled/full overhead curve, blind diagnosis and two independent
schema-only consumers. Keep counters-only default-off and keep Issue #3 open;
see `docs/ISSUE3_STATE_FEEDBACK_ACCEPTANCE_AUDIT_20260814.md`.

## Issue #6 closure-boundary clarification (2026-08-14)

No new NPU run was performed. V274 remains a valid staged candidate rejection:
14 exact component lifecycles and 57,344 exact output tokens, but graph median
executor/device-event timing is 4.504760%/4.991168% slower than eager. Its
preregistration correctly forbids online promotion after that failed component
gate.

The repository does not implement the issue-proposed unified
`AclGraphDispatcher`, `NativeBatchDescriptor` or `GraphCapability`. Keep Issue
#6 closed as rejection of the V274 candidate direction, not as a claim that a
production dispatcher was delivered. See
`docs/ISSUE6_ACLGRAPH_CLOSURE_AUDIT_20260814.md`.

## Issue #22 portable toolchain closure (2026-08-14)

No NPU run was performed. The repository V301 manifest and export/import/
bootstrap/verify/env wrappers remain present, and all three toolchain tests
pass. Read-only host verification found the external archive at its frozen
404,686,777-byte size with exact SHA-256
`a23251d014952d3f62ae06ae135170a280068a764df1337fa0e1aecab203e42a`.

This closes the infrastructure issue only. It is not engine correctness,
serving, NPU or performance evidence. See
`docs/ISSUE22_PORTABLE_TOOLCHAIN_CLOSURE_20260814.md`.

## Issue #4 acceptance-boundary correction (2026-08-14)

No new NPU run was performed. The R8 3+3 remains valid bounded authority and
lifecycle evidence: 234 candidate authority applications, zero fail-closed
counters, exact runs and a preregistered no-significant-difference conclusion.
V295 remains a valid retrospective rejection of the same homogeneous ShareGPT
direction, with a 0.910982% idealized gain bound over its retained 512-row
late-decode timing window.

Neither result completes the original reservation/rollback fault matrix or
c1/8/16/32 × o32/128 acceptance matrix. V295 did not execute a candidate and
explicitly disclaims a universal scheduler result. Preserve both records, keep
the mechanism default-off, and keep the broader Issue #4 open. See
`docs/ISSUE4_ONE_STEP_SCHEDULING_ACCEPTANCE_AUDIT_20260814.md`.

# Issue #19 length-aware prefill authority closure (2026-08-14)

The previously frozen official-image NPU7 varied-length experiment is now
published with its production authority hook and complete raw evidence. Control
and candidate each completed three fresh-process runs with exact outputs,
identity-set/lifecycle parity, and zero fallback. Candidate authority applied
51 times per run. Mean throughput was 4.543 request/s for control and 4.511
request/s for candidate (about -0.70%); peak HBM was effectively unchanged.
This is a no-significant-difference result, so the feature remains default-off.
See `docs/ISSUE19_VARIED_LENGTH_R1_CLOSURE.md` and
`benchmarks/issue19_scheduler_cpu/native_serving_gate_20260812/`.

## Issue #10 incremental eviction closure and aggregation correction (2026-08-14)

The previously unpublished selector-timing campaign is now frozen as three
matched control and three matched candidate NPU7 runs. Every run exercised 128
eviction decisions, selected 128 victims, passed replacement/pressure token and
stale-generation checks, and recorded zero fallback, mismatch, rebuild or
stale-pop events. The candidate selector p50/p95 was 93,248/95,527 ns versus
27,648/30,516 ns for full-sort in the candidate arm, so the experimental
candidate was not promoted and main retains full-sort authority.

Request-level reaggregation also rejects the old 1.593/1.600 “requests/s”
values: they divided all HTTP operation count by the sum of overlapping request
latencies. Using the sum of each run's observed wall interval gives 10.1644
HTTP operations/s control and 10.1413 candidate; the HTTP-200 inference subset
is 5.2455 versus 5.2336 requests/s. Endpoint p50/p95 deltas are mixed; no
speedup or end-to-end superiority claim is made. Normalized raw requests,
per-run hashes, the rejected calculation and closure decision are preserved under
`results/issue10-incremental-eviction-closure-20260814/`.

## Issue #54 full-MLP launch-fusion component closure (2026-08-14)

r2 is retained as a first-warmup failure: ACL status 507035 and the bounded
runtime plog identify a Vector UB address-out-of-bounds exception in the PTO
SwiGLU stage. Static review found that a 1024-element compile-time tile was
laid out using 768-element offsets. r3 makes static capacity equal to the
unchanged 768-element chunk; double builds in the local official `.23` image
are byte-identical, and only the SwiGLU stage SHA changes.

The r3 NPU4 C0/H/C1 component sequence completes 50 measured samples per arm.
All outputs are byte-exact across arms and independently oracle-valid. Mean
device-event times are 421.815/370.623/442.236 µs. Although the candidate is
14.213% below the bracket-control mean, control drift is 4.727%, above the
frozen 2% stability gate. The result is therefore a matched negative; online
promotion and speedup/vLLM claims are forbidden. Observed lifecycle HBM is
3,418--3,889 MiB and cleanup is exact. Complete evidence is under
`results/issue54-full-mlp-heterogeneous24-r3-npu4/`.

## Issue #55 automatic content-addressed prefix cache closure (2026-08-14)

The production native HTTP/runtime path now has a default-off automatic prefix
cache for ordinary cold token requests. Identity binds namespace, cache salt,
token-block hashes and full token collision verification; cached handles remain
generation-qualified and live-graph checked, while decode uses the existing COW
fork path.

The official-image r3 campaign completed 12/12 exact fresh-process runs across
repeated-prefix and unique-salt no-reuse fixtures. Repeated candidate runs each
applied four hits and reused 8,708 tokens; no-reuse candidate runs had zero hits;
collision/stale counters were zero and default-off controls emitted zero APC
telemetry. Paired median repeated-prefix throughput improved 8.013%, cold-request
wall p50 fell 67.284%, and TTFT entered the exact-replay fast path. No-reuse worst
observed throughput slowdown was 0.296%, within the frozen 1% budget. HBM peak was
unchanged at sampler resolution. This is a bounded repeated-prefix TTFT result,
not a general speedup or vLLM-superiority claim; the feature remains opt-in. See
`docs/ISSUE55_AUTOMATIC_PREFIX_CACHE_CLOSURE_20260814.md` and
`results/issue55-auto-prefix-cache-20260814-r3-3plus3/`.

## Issue #56 dynamic batching / dual-microbatch rejection (2026-08-14)

The default-off candidate was connected to the production scheduler and native
executor with deterministic B16-to-8+8 splitting, two ACL streams, fail-closed
fallback and bounded authority/overlap telemetry. The r5 real-NPU B16 gate was
exact for both arms; candidate recorded 62 decisions, zero fallback and
3.573209017 s aggregate measured overlap. Its one-run throughput was 47.156%
below control, but the gate was not a repeated performance result.

Formal expansion rejected the candidate on correctness. r6 B1 cold and warm
each matched the official oracle through token 31 and then returned token 323
instead of 476 for all 128 requests. After narrowing to the candidate-eligible
B16 scope, r7 produced one exact matched control/candidate pair, but r8 with the
same frozen runtime and isolated per-run digest caches produced four candidate
cold mismatches (ordinals 5/6/7/10) while its warm phase was 128/128 exact.
This cross-fresh-process instability forbids completing or scoring the matrix.
The feature remains default-off and is closed as a correctness negative; no
speedup or vLLM superiority claim is made. Evidence is preserved under
`results/issue56-dynamic-batching-20260814-r5-1plus1/` and r6/r7/r8 matrix roots.

## Issue #9 host-tier prefetch matched negative (2026-08-15)

The generation-safe host-tier directory and default-off prefetch authority pass
233 Rust library tests. A frozen official-image real-NPU 1+1 then compared the
existing response-first control with candidate prefetch while an unrelated cold
request occupied the executor. Both arms were token/state/lifecycle exact;
candidate issued and applied one restore with zero fallback and returned pending
to zero.

The mechanism did not overlap on device. Candidate restore waited 570.013 ms
behind the worker's synchronous `ExecuteBatch` frame, while H2D itself took
3.684 ms. Host-tier-hit wall time increased from 596.474 to 631.609 ms
(+35.135 ms, +5.89%), pair makespan increased 24.675 ms, and peak HBM changed
44,175→44,177 MiB. The preregistration classified worker-queued/no-overlap or
non-improving 1+1 as negative and prohibited proceeding to 3+3, so no repeated
performance or speedup claim exists. Raw evidence and cleanup are preserved in
`results/issue9-host-tier-prefetch-20260815-r1-gate/`; the closure boundary is
`docs/ISSUE9_HOST_TIER_PREFETCH_CLOSURE_20260815.md`.

## Issue #76 asynchronous KV transfer lane bounded positive (2026-08-15)

The default-off r5 production candidate replaces the serialized native frame
loop with correlation-safe out-of-order completion, a dedicated ACL transfer
stream, bounded queues and transactional restore publication. All six matched
fresh-process NPU3 runs passed token/lifecycle exactness and state identity;
authority and prefetch fallback counts were zero. Candidate runs proved
1.578/1.730/1.730 ms of real device overlap using paired ACL events.

Host-tier-hit wall p50/p95 changed from 592.597/611.814 ms to
333.716/343.321 ms, a directional p50 reduction of 43.686%; pair makespan p50
changed from 607.648 to 355.473 ms. Peak HBM observations were effectively
unchanged at 44,175--44,177 MiB control and 44,174--44,177 MiB candidate. With
only three repetitions per arm this is not a statistical-significance, broad
speedup, capacity-scaling, or vLLM-superiority claim. Accepted raw evidence is
under `results/issue76-async-transfer-lane-20260815-r5/`; r3/r4 diagnostics are
preserved unscored, and the closure boundary is
`docs/ISSUE76_ASYNC_TRANSFER_LANE_CLOSURE_20260815.md`.

## Issue #77 logical descriptor / device-slot closure (2026-08-15)

The allocator already represented logical generation-qualified states separately
from physical KV blocks. New regressions freeze that invariant, including stale,
reuse, failed restore and worker-restart behavior. A matched NPU5 capacity gate
retained 34 control versus 68 candidate host logical states (2.0x) with the same
80 physical blocks and required resident HBM; exact/lifecycle and sampled
restores passed with zero fallback.

The accepted 2,177-token NPU3 campaign completed three fresh processes per arm.
All six cold and restored continuations were oracle exact, state/generation and
452,984,832-byte host payload identities matched, fallback was zero, and peak
HBM was 44,671 MiB in every run. Control/candidate cold wall p50 was
433.115/431.285 ms; restore wall p50 was 4,592.141/4,593.333 ms. Thus the gate
is capacity-positive, but restore is about 10.6x slower than cold recomputation
because full payload integrity verification dominates. The 4,096-token frozen
plan does not admit 8K/16K, and no performance or vLLM claim is made. Accepted
and failed evidence is preserved under `results/issue77-*`; see
`docs/ISSUE77_LOGICAL_DESCRIPTOR_CLOSURE_20260815.md`.

## Issue #11 hard-capacity session pressure closure (2026-08-15)

The default-off production candidate now applies session-aware ordering at the
existing state-slot pressure boundary while preserving the same safe idle
eligible set and excluding leased states. A reuse 1+1 and an independent
all-protected 1+1 were exact with zero fallback; the latter forced one protected
eviction and then reclaimed all 17 session-held states, proving soft protection
cannot deadlock admission.

The accepted official-image NPU5 3+3 completed all six fresh processes with
token/lifecycle exactness. Control/candidate recomputed tokens were 12/0;
candidate TPOT p99 was 5.53% lower and peak HBM was 53,534 MiB in both arms.
Final review rejected the original request/s numerator because it counted the
control-only expected stale attempt. The identity-bound corrected analysis uses
19 logical operations per arm: control/candidate p50 is 8.8560/8.9009 request/s
(+0.506% point estimate), while TTFT p99 is 1.76% higher. The release decision
is recomputation-positive but end-to-end mixed. The feature remains opt-in and
no statistical, general speedup or vLLM-superiority claim is made. Accepted evidence is under
`results/issue11-session-pressure-20260815-r3/`; failed runner/preflight evidence
is preserved separately. See
`docs/ISSUE11_SESSION_PRESSURE_CLOSURE_20260815.md`.

## Issue #12 high-fan-out program scheduling closure (2026-08-15)

The official-image NPU5 campaign completed the 1+1 gate and three fresh
processes per arm for the frozen 39-request, 16-program workload. All 234 formal
requests were token exact and lifecycle-clean. Candidate authority applied 129
times per run, changed 29 selections across the three runs, and had zero
fallback; HBM was 53,534 MiB in both arms.

Control/candidate program completion P50 is 2,467.839/2,172.363 ms (-11.973%),
P95 is 2,652.371/2,642.347 ms (-0.378%), and program throughput is
5.7477/5.7680 per second (+0.355%). The 15% target is not met. Ordinary TPOT
P99 is 812.371/878.030 ms (+8.082%), failing the 5% no-regression guard, while
selector P99 remains bounded at 43.631 us. The frozen 650 ms SLO has zero
completions in both arms and is rejected as an unmeasurable denominator rather
than converted into a gain. Final classification is matched negative;
attained-service authority stays default-off with no general speedup or vLLM
claim. Accepted and rejected evidence is preserved under
`results/issue12-program-performance-*`; see
`docs/ISSUE12_PROGRAM_PERFORMANCE_CLOSURE_20260815.md`.

## Issue #3 state feedback plane closure (2026-08-15)

The official-image NPU3 matrix completed 12 fresh service starts: off,
counters-only, sampled-events and full-trace each ran three times over the same
agent state-tree, repeated-prefix and synthetic ShareGPT-style workloads. All
420 requests were token exact and lifecycle-clean. Event drops were zero and
every retained request correlation covered scheduler, state-lifecycle, executor
and Ascend-backend producers.

The preregistered default-lightweight gate is negative. Counters-only/off
request/s and TTFT P99 ratio confidence intervals passed, but TPOT P99 ratio CI
was `[0.959233, 1.038599]`, exceeding the 1.02 upper guard. Counters-only used
9.543 telemetry bytes/request at the three-run median; sampled and full modes
used 1,437.971 and 9,166.857 bytes/request. Median peak HBM was 53,551 MiB in
all four modes. Device synchronization count is unavailable in the frozen
worker protocol and is not reported as zero.

Two independent schema-only consumers then passed the separately frozen gate.
Blind diagnosis identified 4/4 sealed producer-layer mutations with no labels
or code diff; bounded replay emitted advice with `authority_applied=false` for
all four. At 99% prefix loss all four diagnoses abstained. The sampled identity
count prediction of three versus actual five is retained as a non-gating
preregistration metadata error, without rewriting the preregistration or
rerunning the matrix. Classification is complete but default-off; no inference
speedup or vLLM-HUST claim is made. See
`docs/ISSUE3_STATE_FEEDBACK_CLOSURE_20260815.md` and `results/issue3-feedback-plane-20260815-r10-formal-matrix/`.

## Issue #4 one-step scheduling feasibility closure (2026-08-15)

Twelve previously frozen real-NPU Qwen2.5-14B runs cover c=16/32 and
o=32/128 with three exact lifecycles per cell. R10 rehashed every source and
removed the complete nonnegative executor-finish-to-next-enqueue interval to
compute an intentionally impossible performance ceiling. Median ceilings were
2.6324%, 1.4028%, 2.9199% and 1.8329%; the maximum individual run was 2.9798%,
below Issue #4's 5% target before reservation and rollback overhead.

Together with R8's matched 3+3 no-significant-difference result (1.0047x median,
234 exact authority applications, zero fallback/mismatch), this rejects the
current mechanism and keeps it default-off. It does not claim all future async
schedulers are impossible. The same patch repairs the 17/4/4 request/worker
digest drift by deriving one aggregate from all six canonical leaves and adds
fail-closed round-trip tests. See
`docs/ISSUE4_ONE_STEP_SCHEDULING_CLOSURE_20260815.md` and
`results/issue4-one-step-upper-bound-20260815-r10/`.

## Issue #8 R13c full-matrix closure (2026-08-15)

The later R13c campaign supersedes the earlier acceptance-boundary statement
without rewriting its raw evidence. It freezes exact repository-document
prompts at 2,177/8,192/16,384 tokens, concurrency 1/8/16/32, three matched
fresh-process repeats per arm, an official local `.23` image and one
identity-verified Qwen2.5-14B artifact. All 36 cells and all 72 arms completed
with exact outputs and recycled state. Three failed attempts (one digest-cache
preflight and two bounded scheduling/cleanup failures) remain append-only; the
same frozen keys were rerun successfully rather than discarded.

At concurrency greater than one, candidate authority activated in every run
with zero bypass; at concurrency one it correctly fail-closed because no decode
contention existed. The candidate reduced maximum continuous prefill execution
by about 82--92% for 8K/16K contention cells and improved hot TPOT P99 by up to
49.37%. It nevertheless reduced request throughput by 12.28--26.30% and raised
cold TTFT P95 by 39.05--118.31% across those cells. No cell passes the frozen
joint benefit/throughput/TTFT rule. Classification is therefore **negative**;
chunked prefill remains default-off and no speedup is claimed. Machine-readable
aggregation is in
`results/issue8-long-matrix-20260815-r13c-aggregate/`.

## Issue #95 bounded automatic prefix cache closure (2026-08-15)

Issue #95 closes the unbounded-residency gap after Issue #55 without changing
the default-off policy. The runtime now binds a positive APC capacity into
deployment identity, applies lease-safe LRU eviction between worker batches,
and reports current entries, evictions and lease-blocked insertions.

The first real candidate gate found that APC could index and later evict an
explicitly retained, caller-owned seed state. That failure remains preserved:
later exact requests received HTTP 409 `StaleState`. The narrow repair keeps
`retain_state=true` misses outside APC ownership and adds a seed/churn/exact
regression without weakening generation, lease, stale or digest validation.

The corrected official-image R3 1+1 and counterbalanced 3+3 completed on NPU3.
All outputs and lifecycles were exact. Each candidate run had eight lookups,
eight inserts, six evictions, two final residents, and zero hits, collisions,
stale entries or lease-blocked insertions; every control APC counter was zero.
Control/candidate median throughput was 1.021090/1.020829 request/s, an APC
overhead of 0.0256% against the 2% guard. Request/s CV was 0.326%/0.268%, and
both arms peaked at 53,550 MiB HBM. The bounded candidate is accepted for the
opt-in path, but this is not a speedup or vLLM-superiority result. See
`docs/ISSUE95_BOUNDED_APC_CLOSURE_20260815.md` and
`results/issue95-bounded-apc-20260815-r3-3plus3/`.

## Issue #57 generation-safe preemption/recompute closure (2026-08-15)

Issue #57 adds a narrow default-off authority that may checkpoint a
complete-token-lineage cold decode request at a batch boundary, invalidate its
old generation, serve queued state pressure, and recompute/resume only if the
frozen next token remains exact. Suspended-request liveness and cancellation
bugs were repaired offline; stale, double-resume, bounded-attempt and mismatch
fault regressions pass.

R1 retained an honest fixture failure: 256 blocks could not hold the intended
17 states because each frozen prompt consumes 18 blocks. R2 froze 320 blocks,
the 54,335,087,888-byte HBM admission requirement, official local `.23` image,
Qwen2.5-14B BF16 artifact and identity
`c66186228d6da10982eb5b4af604bf9da63fdc30b8d95d0effd153c2f3f9a7b3`.

The corrected 1+1 and counterbalanced 3+3 completed on NPU3. All arms were
token/lifecycle exact. Candidate applied/resumed/invalidated exactly once per
run, recomputed 2,178 tokens, and had zero fallback; all control counters were
zero. Pressure TTFT p50 improved 55.780% (1,566.811 to 692.851 ms), but long
sojourn regressed 113.375% (1,200.447 to 2,561.459 ms), failing the protected
5% guard. Matched wall interval improved 0.488%, request/s was
1.539056/1.546604 with CV 0.763%/0.999%, and both arms peaked at 55,085 MiB.
Classification is **matched negative**; the candidate remains default-off and
no speedup or vLLM comparison is claimed. See
`docs/ISSUE57_PREEMPTION_RECOMPUTE_CLOSURE_20260815.md` and
`results/issue57-preemption-20260815-r2-3plus3/`.

## Issue #58 sleep/wake and online weight-release closure (2026-08-16)

Issue #58 adds a default-off supervisor that admits sleep only for a uniquely
owned, state-empty runtime, exits the complete C++ worker to release all
worker-owned HBM, and wakes only after the frozen digest handshake and exact
capacity-geometry gate. Concurrent requests, persistent state, unsupported
feedback export and identity/geometry drift fail closed.

The official-image real-NPU admission 1+1 and formal fresh-process 3+3 were
token/lifecycle exact. Every control lifecycle call returned
`authority_disabled` and kept epoch one. Every candidate applied one sleep and
one wake, advanced epoch one to two, released 51,653 MiB, and produced the same
exact post-wake token. Candidate sleep p50/p95/max was
3.878/4.517/4.588 seconds and wake was 34.389/35.892/36.059 seconds, passing
the frozen 600-second SLO. The experiment container was removed and NPU3
returned to baseline.

This is a positive bounded resource-release result, not an inference speedup
or vLLM comparison; the feature remains explicit opt-in. See
`docs/ISSUE58_SLEEP_WAKE_CLOSURE_20260816.md` and
`results/issue58-sleep-wake-20260816-r1/`.

## Issue #59 on-device sampling closure (2026-08-16)

Issue #59 adds an identity-bound default-off Qwen categorical/beam sampling
path with temperature, top-k/top-p/min-p, presence/frequency/repetition
penalties, deterministic RNG and bounded logprobs. Canonical greedy frames and
telemetry remain unchanged. R1--R3 diagnostic failures are preserved: a
bounded real-worker trace located their ranking difference in a one-ULP
upstream BF16 tied-logit drift, not in the sampler. R4 correctness passed but
its performance interval was rejected because it included candidate-only beam
checks; R5 isolated the matched eight-request interval without changing the
binary, model, oracle or workload.

The official-image R5 counterbalanced 3+3 completed on NPU3 with exact
categorical tokens, RNG offsets, tied-rank contract, deterministic beam
lifecycles and zero state leaks. Control/candidate median throughput was
16.9508/14.4669 request/s; latency p50 was 57.797/58.328 ms, p95 was
63.120/113.699 ms, and peak HBM was 53,533/53,557 MiB. Candidate transferred
172 bytes/request. Its steady device sampling median was about 0.36 ms, but the
first fresh-process call took 76.801--79.728 ms. The narrow feature is
functionally accepted and remains default-off; fresh-process cold performance
is negative, no speedup or vLLM comparison is claimed. See
`docs/ISSUE59_ON_DEVICE_SAMPLING_CLOSURE_20260816.md` and
`results/issue59-on-device-sampling-20260816-r5-3plus3/`.

## Issue #67 production ACLGraph dispatcher closure (2026-08-16)

Issue #67 adds a versioned `NativeBatchDescriptor`/`GraphCapability` decision
at the production decode boundary. Eager remains the default. The explicit
candidate makes one fail-closed authority decision per batch and exposes
bounded decision, fallback, capture, replay and rebuild telemetry. The Qwen
B1--B32 contract, resident plan, full worker build and offline fault tests
passed.

R1 is retained as a pre-worker timing-contract rejection. R2 corrected only
the incompatible device-event override and completed an exact real-NPU 1+1,
while also performing the first full-byte verification under the canonical
container mount. R3 freezes those verified stat+SHA caches under aggregate
identity `590ac068643e9d7cb46e335ab2d634a1dde9a3dd9fe8a4793124dcb16bc06633`.

The official-image R3 counterbalanced fresh-process 3+3 completed on NPU3.
All six runs were token/lifecycle exact. Candidate applied 837 total decisions,
captured six graph buckets, replayed 837 times, and had zero fallback and zero
rebuild. Control/candidate median throughput was 2.995329/2.985617 request/s
(-0.324%); TTFT p50 was 8675.028/8678.994 ms, TPOT p50 was
37.730/38.501 ms, and peak HBM was 58,567/58,573 MiB. The dispatcher is
functionally accepted as a default-off production candidate, but this workload
shows no material end-to-end benefit. No speedup or vLLM comparison is claimed.
See `docs/ISSUE67_ACLGRAPH_DISPATCHER_CLOSURE_20260816.md` and
`results/issue67-aclgraph-dispatcher-20260816-r3-3plus3/`.

## Issue #16 identity-bound multi-LoRA foundation (2026-08-16)

Issue #16 adds a default-off identity-bound multi-LoRA foundation. Adapter
base root, ID/generation, module, A/B shape/layout/dtype/rank/scale/digests and
TP/EP placement are validated before execution. Request, protocol and retained
state carry the adapter generation. The scheduler groups the selected request
set into stable segments, while the resident Qwen worker runs the base
`lm_head` over the full physical batch and applies BF16 LoRA deltas by segment.
Host and HBM adapter bytes are bounded with demand load, stable LRU,
generation checks and in-flight leases.

R1 and R2 preserve runner-contract rejections. R3 reached the real worker and
exposed a manifest producer/consumer field-order bug that made rank four parse
as rank one; its early EOF remains rejected evidence. R4 freezes the corrected
`slot, generation, rank` schema and a producer round-trip that verifies every
A/B size and SHA.

The official-image R4 fresh-process 1+1 completed on dynamically selected NPU3.
All 64 emitted tokens per arm were exact and all temporary states recycled.
Control formed homogeneous four-row/one-segment batches; candidate formed the
required 32-row/eight-segment heterogeneous batch. Both arms applied 64 adapter
rows, loaded eight adapters, hit all eight on decode and reported zero fallback.
Peak HBM was 58,569/58,633 MiB. Request throughput was
31.276969/31.150412 request/s (-0.405% descriptively), and p95 latency was
202.862/251.639 ms. This is a correctness/authority gate only, not a repeated
performance result, so no speedup or vLLM comparison is claimed.

The narrow foundation is functionally accepted and remains default-off. The
unmet original matrix and policy acceptance is preserved in #103 (multi-module
segmented kernels), #104 (async bounded residency/eviction) and #105
(skew-aware merge/unmerge). See
`docs/ISSUE16_MULTILORA_FOUNDATION_20260816.md` and
`results/issue16-multilora-20260816-r4-gate/`.

## Issue #107 typed state-group coordinator foundation (2026-08-16)

Issue #107 splits the independently reviewable allocator foundation from #17's
real hybrid-model acceptance. Validated GQA IR now lowers to an ordered,
SHA-256-bound `StateGroupPlan`. Uniform full attention produces one group;
full-attention and block-aligned SWA layers produce independent physical pools
under one request-level transaction. Group descriptors bind kind, block
geometry and operator identity. SWA prefix reuse is disabled fail-closed.

The coordinator implements joint per-group admission, generation-safe state ID
reuse, fork/shared-tail COW, bounded SWA rollover, per-group accounting, and
atomic create/append/fork/cancel/evict. A failure in any group poisons the entire
transaction, and an epoch mismatch rejects stale commit. The deterministic
fault matrix covers exhaustion, rollback, stale generation, descriptor reorder
and substitution, pool-full rollover, repeated fork/cancel/evict and final leak
checks.

The offline gate passed all 297 library tests and every Rust binary target with
the repository's portable offline toolchain. This is software-only evidence:
the module is explicit opt-in, the existing Qwen execution config/protocol and
compatibility digest are unchanged, and no container, NPU, HBM or performance
claim is involved. MLA/indexer/recurrent wire and operator integration plus a
real hybrid checkpoint remain in #17 and depend on the end-to-end hybrid model
runtime tracked by #66. See
`docs/ISSUE107_TYPED_STATE_GROUP_FOUNDATION_20260816.md`.

## Issue #109 MiniMax full-checkpoint identity (2026-08-16)

Issue #109 freezes the complete official MiniMax-M2.5 W8A8 source identity as
the artifact prerequisite for #66. All 57 payload files passed local full-byte
SHA-256 at the pinned revision and total 230,772,955,024 physical bytes. The
index and safetensors headers agree exactly on 143,967 mappings and
230,754,320,384 tensor payload bytes. Every layer 0--61 has the exact 2,322
required semantics; embedding, final norm and LM head are the only non-layer
tensors.

Two independent full-byte root rebuilds took 73.72 and 67.74 seconds and
produced byte-identical manifests. Their all-layer root is
`b17196f31135c8dc9182fd158a3ccd4759032da251e679018dbeb8f4ee7b3591`.
The long real fetch exposed and repaired a resumability defect where curl's
in-process retry could roll a partial file back to its invocation-start offset;
bounded outer retries now resume from the latest durable length and have a
fault regression.

This is artifact identity and structural-completeness evidence only. No
container or NPU was used, and no HBM, execution, serving, performance or vLLM
claim is made. Issue #66 remains open. See
`docs/ISSUE109_MINIMAX_FULL_CHECKPOINT_CLOSURE_20260816.md` and
`results/issue109-minimax-full-checkpoint-20260816-r1/`.

## Issue #111 validated IR to persistent-plan contract bridge (2026-08-16)

Validated Rust `NativeModelIr` now lowers to a versioned, bounded canonical
`PersistentPlanContract` transport without family-name dispatch. The frozen
MiniMax vector covers 62 layers, TP8/EP8 ownership, W8A8 FP32 scale/offset
companions, startup/final tensors and eight rank memory minima. Its 210,445
bytes hash to
`db15b3d527520f6b366705cc5936b7d38689fdab310095c11b79deee1df3ffcd`
and bind complete IR file SHA-256
`a8bf2718ee79da2c4eff80415d31d0fdffb888d7e389892671874fb0b5df997d`.

The C++ decoder verifies the mandatory transport digest, enforces canonical
ordering and bounded fields, and feeds the existing v2 compiler. Rust lowering
tests and the direct C++ cross-language/fault test pass. Recomputed-digest
truncation, trailing bytes, noncanonical numbers, wrong trusted identity and
artifact tensor substitution all reject. No container or NPU was started.
This closes only the host structural bridge prerequisite; real prepack/import,
payload admission, all-rank HBM, collectives, 62-layer numerical execution,
online serving and performance remain in #66. See
`docs/ISSUE111_PERSISTENT_CONTRACT_BRIDGE_20260816.md` and
`results/issue111-persistent-contract-20260816-r1/`.

## Issue #113 MiniMax all-layer rank-artifact import plan (2026-08-16)

The offline planner revalidated all 57 source files byte-for-byte and all
safetensors headers against #109, then
covered every one of the 143,967 source tensors exactly once. It emitted 747
semantic recipes (three startup/final plus 62×12 layers) for TP8/EP8. Every
rank plans 31,021,818,368 raw artifact bytes.

All 47,864 FP32 offset payloads, totaling 392,863,744 bytes, were read from the
frozen checkpoint. They contain zero nonzero values and zero negative-zero
values. The audit root is
`f3da472d2fc192c8ab1b53190af49433b0a8edca10a3cb5339b613c283efa252`.
The physical profile SHA is
`3e61b672a5bc53edca1cd7b8520901937e823e003c001a45df525e84f31ba40a`.

Two independent 76,414,206-byte plan rebuilds and 24,791,904-byte offset
reports were byte-identical. The plan semantic root is
`e12fc83ab3a15c24e105a85ade77288c8656a623ccd9533f376c668b7c0f0d9f`.
Its complete-file SHA is
`1151f66ef57f1eca994d793287a407e064e9a6f05018390f34e2a12f3e0c8ef6`.
The profile overlay converts #111's dense expert semantics to the accepted
FRACTAL_NZ/BF16-scale/verified-zero-offset ABI and the full transformed
contract compiles in C++.

No output pack was materialized and no container or NPU was used. This is not
HBM, execution, correctness, serving, performance or vLLM-HUST evidence. See
`docs/ISSUE113_MINIMAX_IMPORT_PLAN_20260816.md` and
`results/issue113-minimax-import-plan-20260816-r1/`.

## Issue #115 MiniMax all-rank execution pack (2026-08-16)

The frozen #113 plan was materialized into all eight TP8/EP8 rank directories
after a fresh full-byte check of all 57 source files. The published pack has
10,936 artifact files, exactly 31,021,818,368 bytes per rank and
248,174,546,944 bytes total. The complete artifact catalog root is
`9fe82c343119f5038ec7d44ffc252041c8cdd067dc4d92b1255926750ed76f0a`.

The bounded-memory host kernel covers replicated copy, both TP slice axes,
W1+W3 concatenation, transpose plus INT8 FRACTAL_NZ packing, FP32 scale
concatenation and FP32-to-BF16 round-to-nearest-even. The generated
PersistentPlanSpec artifact catalog binds 1,367 primary/companion tensors and
has root
`bea542a0ea79f51de96dba4df5a4a22e0391a14749ed904840fb121d6760d803`.
Review rejected the first embedded catalog because it inherited row-parallel O
ownership for replicated O scale/offset; the accepted sidecar binds the same
verified pack with corrected per-companion ownership.
Its 10,936 artifact records compile successfully against the frozen #113
physical contract through `CompilePersistentExecutionPlan`.

All 32 layer-0 expert files are byte-identical to the accepted independent
prepack. A separate verifier reopened and rehashed every one of the 10,936
files and all 248,174,546,944 bytes, recomputed the rank totals, checked the
catalog and repeated the layer-0 comparison. Its record hashes to
`1af067b4d07ead7d057288367a6476ab6b342a818fd8e95e6af80cbb9b99c70a`.
An additional independent dense verifier reconstructed all 8,952 dense
artifacts and 23,201,517,568 output bytes directly from frozen source spans;
replicated, axis-0 and axis-1 outputs all matched byte-for-byte.

This closes only the host materialization prerequisite. No container or NPU
was used, and no HBM admission, collective, full-model numerical execution,
serving, performance or vLLM-HUST claim is made. See
`docs/ISSUE115_MINIMAX_RANK_PACK_CLOSURE_20260816.md` and
`results/issue115-minimax-rank-pack-20260816-r1/`.


## Qwen3.8 packed-transfer lease normal lifecycle qualification (2026-09-03)

Evidence: **real-online** r402; independently revalidated **derived-artifact**
r403. This is a fixed Hi/max8 correctness and normal-lifecycle result, not a
performance comparison or default promotion. Current classification and scope
are in [NATIVE_ENGINE_STATUS.md](NATIVE_ENGINE_STATUS.md) and
[native-pipeline-activation-lease.md](native-pipeline-activation-lease.md).

The r398 shutdown repair was frozen into new opt-in r399 from ordinary r364,
changing only executor/pipeline bindings. The qualified candidate manifest is
`538393c336941ebad5e8c59a627ba782022ff5d30a810f64742027d3f00f646a`;
the admitted host assembly is
`d979f3d37209bcf69fd914b1aad2360b523858a2634dd7ce8e7cc8953dbdceea`.
r400b passed actual Rust route admission and mixed-provider, wrong executor
hash, duplicate-rank and wrong-stage negatives. r401 installed exact preview
bytes during an independently supervised idle maintenance window and restored
r113 successfully. Earlier r400/r400a software preview failures are retained.

[r402 completion](/data/statecentric-builds/qwen38-pipeline-activation-20260903-r402-shape-gate/completion.json)
(SHA-256 `fdeec1d34177c6e581972429248b898e12954063c6754f9145d51162be2536c7`)
records 19 probes, 88 exact requests and 704 output tokens on physical NPU4–7.
All ranks cover B1–B4 graph execution; ranks 2/3 cover B2–B4 sharded greedy;
observer records are zero. The three overlap probes each report seven actual
transport permits. One engine instance/worker epoch is preserved across probes.

The owned stack exits normally via SIGTERM in 3.518532 s (shell status 143).
Four independently bound rank ready/drained pairs each show 268 acquired and
268 consumer-completed leases, zero shutdown retirement and no held leases.
Device process/container/device-FD idle checks pass before independent r113
restoration. Native, gateway and SageMate health pass after restoration;
protected HUST process identities remain unchanged. The configured default is
still r153; schema20 TP4 artifacts remain preserved.

[r403 analysis](/data/statecentric-builds/qwen38-pipeline-activation-20260903-r403-analysis/analysis.json)
(SHA-256 `5a11bc921d01e77e04a35774531ab69e847f178d07c046686822e562ba9dfaac`)
rechecks raw responses, physical activation, eight complete custody samples,
PID namespaces, lease counts, normal shutdown, release and restoration. It
executes the exact archived analysis tools rather than consulting later
working-tree versions.

r397 remains a failed r394 experiment and is not retroactively accepted.
Cancellation, faults/recovery, long context, soak, full A1–A4, graph-owned carry,
workspace pooling, greater in-flight concurrency and matched HUST performance
are outside this qualification. All new artifacts, caches and temporary
analysis files for this work are under `/data/statecentric-builds/`.


## 2026-09-03 — r399 all-subset cancellation and normal lease drain (r404/r405)

The unchanged r398→r399 candidate passes real-online bounded cancellation on
physical NPU4–7, followed by independently audited normal packed-buffer lease
retirement and detached r113 restoration. The configured default remains r153.
No launcher or runtime artifact changes are made in this qualification.

- Source run: [r404 completion](/data/statecentric-builds/qwen38-pipeline-activation-20260903-r404-cancel-gate/completion.json), SHA-256 `3f65c78f74cdc98a191a1d6d1bc5bbaa5115b66b38981375828077a846ae688b`.
- Derived audit: [r405 analysis](/data/statecentric-builds/qwen38-pipeline-activation-20260903-r405-analysis/analysis.json), SHA-256 `5c11fa3c6911b0b91df484cd71655440ae5a369ef61bd6f5681fa194dcf637e7`; runs exact archived analysis tools.
- Frozen tooling archive: `7319707d08a2d7620575a56403335c71bb8adb5b7155bf714c4a5d93321e0ea7` (39 files).
- Hi/max64, all14 partial-cancel subsets, 9 cycles/126 groups, 331.074738 continuous seconds.
- 506 submitted = 254 exact completed + 252 cancelled; 4914 lossless per-group batches; exact scalar recovery.
- Actual B4→B3/B2/B1 transitions, same worker epoch, fully reclaimed state/KV pool; whole-arm graph accounting has zero unaccounted pure-decode batches.
- All four ranks: acquired equals consumer-completed, shutdown-retired zero; independent rank/PID binding, custody and device-FD release pass.
- Normal owned-stack SIGTERM exit 143 in 3.868587s; independent r113 PID 3828786 restored healthy.
- Protected GLM container restarted externally before admission at04:58:03UTC. Waited until ready, then preserved its fresh worker/container identities throughout. No business service was stopped or modified.
- Software validation:70 tests; documentation governance:5 suites/96 Markdown files.

Scope is fixed-model bounded partial cancellation and normal transport retirement;
not worker-fault, long-context, graph-owned carry, pooling, extra concurrency,
HBM savings or performance qualification. Historical r397 remains failed.
The historical r038/HUST comparison's11 input hashes were reverified separately:
8.7118 versus49.9113 tokens/s at c4/max16. That is not a current r399 comparison;
see [comparison ledger](PERFORMANCE_COMPARISONS.md).


## 2026-09-03 — Fresh r399/HUST whole-engine performance comparison (r406/r407)

The user-requested fresh comparison completed on NPU4–7. Both backends serve
identical frozen Qwen3.8-27B requests in graph mode, BF16, max context2048,
max active4 and APC off. Native TP2×PP2 and HUST TP4 remain distinct engine
configurations; per-rank CPU policies are recorded.192 measured +64 warmup
requests per backend cover c1/c4 × max16/max64, four resident families and
three cell repetitions. Raw semantic content, prompt/output token counts and finish reason match for 156/192 measured request pairs. Output mismatches prevent an equal-quality speedup conclusion; the measurements remain conditional on their observed outputs.

| Max output | Concurrency | Native tokens/s | HUST tokens/s | Native/HUST throughput | Mean TPOT ms (N/H) | Mean semantic TTFT ms (N/H) |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 16 | 1 | 10.377 | 19.290 | 0.5380× | 48.072 / 31.766 | 820.484 / 352.682 |
| 16 | 4 | 20.895 | 51.313 | 0.4072× | 77.503 / 39.195 | 1736.458 / 491.475 |
| 64 | 1 | 17.560 | 27.839 | 0.6308× | 46.087 / 30.640 | 740.606 / 367.893 |
| 64 | 4 | 46.908 | 88.986 | 0.5271× | 56.828 / 35.025 | 1712.670 / 501.569 |

Raw [r406 completion](/data/statecentric-builds/qwen38-current-vllm-20260903-r406-compare/completion.json) and derived
[r407 audit](/data/statecentric-builds/qwen38-current-vllm-20260903-r407-analysis/analysis.json) bind all raw requests and archived tooling. Whole-run
request counts, Native normal lease drain, HUST exact-container release,
NPU4–7 process/container/FD release and protected business identities pass.
Independent r113 PID 4138414 is restored healthy; default r153
unchanged.12 software tests and documentation governance pass. No runtime or
Native launcher changes, eager fallback, business-service changes or promotion.
Full scope, timing definitions, output mismatches (if any), repeat-level values
and temporal/topology limitations are in the
[comparison ledger](PERFORMANCE_COMPARISONS.md). This does not establish net
lease-policy benefit, workspace reuse safety or complete A1–A4 qualification.


### r406 post-hoc repeat consistency

A separate [raw repeat audit](/data/statecentric-builds/qwen38-current-vllm-20260903-r407-analysis/repeat-consistency.json)
compares the three measured repetitions of each fixed input/output-limit/concurrency.
Native is identical for64/64 such groups; HUST is identical for48/64, with16
groups containing differing outputs. This is an exploratory consistency audit,
not a causal diagnosis or proof that either backend is numerically correct.
All192 request pairs have the same reported prompt/output token counts and
finish reason, but36 pairs differ in semantic content (1/1/18/16 in the table's
four rows). Equal output-token totals make the throughput denominator explicit;
text mismatch and HUST repeat variability remain unresolved. No failure was
removed and no eager rerun or runtime adjustment was substituted.

## 2026-09-03 r408：r406 性能瓶颈离线复核

`derived-artifact`，非新真机实验或优化收益。脚本
`benchmarks/analyze_qwen38_current_vllm_bottlenecks.py` 校验 r407 固定审计及其所有
原始输入 SHA，完成图计数守恒、SSE 间隔、尾部 batch 与 E2E 差距分段。
产物 `/data/statecentric-builds/qwen38-current-vllm-20260903-r408-bottlenecks/analysis.json`
SHA-256 `5f58a215397d3ed9151df56ecfce3a6921460697e8d02d5415e8024759c1a706`。
每 rank 6269 replay + 3 capture = 6272 decode；B4 host decode 均值 50.578 ms；
c4/max64 每格最先到达请求的首次非空 SSE 间隔 Native/HUST 为 1595.251/34.973 ms。
7 个尾部混合完成配对及源码显示 prefill/decode 共同返回边界。完整口径、非加性
限制和优化验证优先级见比较 ledger 及同目录 `report.md`。未改 runtime、默认或服务。

## 2026-09-03 r409–r412：prefill 诊断与复用组件开工

- r409：容器内 `/data` 父目录不存在，首次 profiler 启动前失败；16 个预热/对照
  请求仅为部分记录。已独立恢复 r113，失败保留。
- r410：完成 BFCL multiple/WildChat × rank1/rank3 四份真实 `msprof` task trace，
  加预热、采集前后对照，共 40 请求，同输入内容/usage/finish reason 一致，正常
  shutdown 和 packed-transfer lease audit 完成。整体仍失败：通用 graph helper
  要求未被本负载触发的 B2；恢复阶段保护业务容器更换代次，保护一致性检查失败。
  r113 自身恢复成功：PID315078、start ticks745025268。不得追认整体 gate 通过。
- r411：显式 `partial-diagnostic` 分析，`validated=false`、
  `profile_attribution_validated=true`。每份 profile 的 64 次 Model-RI 执行与
  decode计数相符。原始 SSE 重读、task CSV/DB hash 与计数、Model-RI/NOTIFY_WAIT
  映射均核验。产物 `/data/statecentric-builds/qwen38-prefill-20260903-r411-partial-analysis/analysis.json`，
  SHA-256 `b17b21325fee3d352edf61cfb217666c0e3f32f2a65f71a3ee809f6384b7793c`。
- rank1 BFCL 的公开 `aclrtMalloc` 为 43,259 次/340.418 ms，`aclrtFree` 为
  43,341 次/637.645 ms；其中 99.35%/99.75% 的 API 时间位于 prefill 相关 host
  窗口，图内为零。WildChat 分别 55,654 次/475.211 ms、55,741 次/828.322 ms；
  rank3 同样超过99%位于 prefill 相关窗口。混合窗口含一拍 decode，不能称纯 prefill
  device time；API 可嵌套、设备工作可重叠，不能重复求和当作可回收延迟。
- r412：`CompletedBufferPool` 模型无关所有权组件，CPU、ASan/UBSan 测试通过；
  包括活跃地址隔离、旧/错 owner lease、精确 size 脏缓冲区复用、内存/元数据预算、
  并发、分配失败、未知完成隔离、free失败不盲目重试。尚未接入 GDN、构建候选或
  部署，无性能收益声明。产物 `/data/statecentric-builds/qwen38-prefill-20260903-r412-buffer-pool-cpu/`。

相关源代码：`benchmarks/run_qwen38_current_prefill_profile.py`、
`benchmarks/analyze_qwen38_current_prefill_profile.py`、
`native/include/statecentric/completed_buffer_pool.h`、
`native/tests/completed_buffer_pool_test.cpp`。目标规划位于
`/data/statecentric-builds/prefill-latency-plan.WkZ5MO/task_plan.md`，后续验收仍需新
保护身份、不可变候选、正确性/取消/drain及同拓扑observer-free ABBA。


### 2026-09-03 — r413–r419：独立 prefill 张量复用候选与真机正确性

- r413 CPU/ASan/CANN 编译通过；加入真实 provider 分配/释放路径的 CPU ACL 故障注入后冻结 r414：`/data/statecentric-builds/qwen38-prefill-r414-frozen/build_manifest.json` SHA `623446be09b76d8554b931abd036c11ecb7d446820c8f49367acd84c2a324fac`。测试覆盖 capture/child/workspace 排除、脏值复用、并存 lease、同步失败隔离。无 NPU 构建阶段证据不作性能结论。
- r415 从不可变 r399 仅替换 GDN DSO，SHA `bbb8b4ab538b280e7e88573ec11e6b384e0d658ec78ad328545eb5aa5e795ded`；manifest SHA `745fbe42418aafc865855bbc4a0083611a761164d2082db4025b7477df4f06c9`，host assembly `7e9fe706f589ce50f930b33080c0b752351cc3d9c37c01a9049a0fdd28e10e16`，plan 保持 r399。独立 prefill token>=9、实际 capture NONE；每 rank/handle 64 MiB、单缓冲 8 MiB、1024 条元数据上限；精确 size 复用。workspace、状态、graph、aggregate/child 存储排除。预算 miss 私有分配，未知消费者完成隔离，未增加同步或调度并发。
- r416 路由预览的错误 hash 确被 Rust 拒绝，但测试误写 `GDN`/实际 `gdn` 大小写，故保留失败目录；新 r416b 修正断言通过。r417 完成 preview→精确停止 r113→NPU4–7/FD idle→按预览字节安装→receipt→独立恢复 r113。NPU0–3 新业务代次始终保持不变。
- r418 真机 19 组 Hi/max8 共88请求，加四族各两次长 prefill 共32请求，120个输出精确一致；B1–B4 capture+replay全部守恒，940 packed leases/rank正常归还。各rank fresh476/reuse189508/budget_miss96，峰值67,035,776 bytes<64MiB，关闭 owned_bytes/active_leases/quarantined_buffers 均0。证明有界真实复用与正常完成释放，不证明未知失败设备上下文可恢复或端到端加速。
- r419 独立审计通过：`/data/statecentric-builds/qwen38-prefill-r419-analysis.json` SHA `e413e9f5e8a262019fe39e5bc0adddedad2fad3c91bf9f15468cabc65c4cb02e`。后置 analyzer 明确标注非预注册；gate/原始解析器从 hash 校验归档执行。r113恢复 PID448381/start745217873。r420取消与后续ABBA尚未裁决，默认仍r153。

口径补充：上述 r415 pool 的 owned/peak_owned_bytes 是申请字节计数，不含 ACL 分配器粒度、碎片和管理开销，不能称为实际物理 HBM 峰值；设备占用以独立 custody 采样为准。


### 2026-09-03 — r420/r421：r415 取消恢复与复用池正常释放通过

`/data/statecentric-builds/qwen38-prefill-r420-cancel-gate` 的独立监督运行完成；全部14取消子集共9轮/126组，308.265274105秒。soak506提交=254 exact完成+252取消，4914条无损组内batch记录与executor宽度计数一致，观察4→3/2/1收缩。取消前后各32个长prefill请求与r399原始参考精确一致，总570请求=318正常精确完成+252取消。

各rank477次池分配、326067次复用、48次预算miss，峰值67,029,632申请bytes；正常Close owned_bytes/active_leases/quarantined_buffers均0。未启用workspace、graph或父子共享缓冲复用。NPU4–7完整custody/FD空闲证据及r113独立恢复通过（PID533973/start745302507）；NPU0–3保护业务代次未变。

预先冻结的analyzer及解析器从归档执行，独立审计 `/data/statecentric-builds/qwen38-prefill-r421-cancel-analysis.json` SHA `f0a33b2dddbad89b094018d61fc98b7d4eba050d1accd6d153ff9c1721c26546` validated=true。限定正常完成、逻辑取消与后续恢复，仍非worker故障恢复或性能收益证据。r422同配置r399/r415 ABBA开始，默认r153不提升。


### 2026-09-03 — r422/r423/r424：r415同拓扑ABBA完成，预设性能目标未达到

`/data/statecentric-builds/qwen38-prefill-r422-abba`：r399→r415→r415→r399，固定TP2×PP2/NPU4–7、BF16、graph mask30/capacity13、APC关闭、相同CPU亲和与四族输入。每臂完整64个warmup请求、192个计入结果的请求；总1024请求，768次相对第一臂的跨臂内容/usage/finish比较（含warmup）全部精确一致。所有实际decode capture+replay守恒、normal transport/tensor drain、NPU/FD释放、保护业务代次与独立r113恢复通过。r113 PID817667/start745563105；默认r153不变。

表内按两臂control和两臂candidate合并：吞吐=总生成token/总cell wall，延迟为逐请求均值；最后一列是逐请求最大连续非空SSE间隔的P95（线性插值，排除TTFT，单位ms）。每格每种实现96个计时请求。全部请求族、重复及相邻pair原始结果在分析JSON中保留。

| max tokens | 并发 | r399 tok/s | r415 tok/s | 吞吐变化 | TTFT ms（r399→r415） | TPOT ms（r399→r415） | E2E ms（r399→r415） | max-gap P95 ms（r399→r415） |
|---|---|---|---|---|---|---|---|---|
| 16 | 1 | 10.538 | 10.656 | +1.119% | 809.377 → 798.541 | 47.245 → 46.847 | 1518.052 → 1501.251 | 58.330 → 53.233 |
| 16 | 4 | 21.011 | 21.263 | +1.201% | 1726.830 → 1691.562 | 77.015 → 76.957 | 2882.059 → 2845.911 | 2201.795 → 2204.842 |
| 64 | 1 | 17.561 | 17.593 | +0.181% | 742.065 → 727.549 | 46.059 → 46.185 | 3643.813 → 3637.226 | 57.025 → 56.409 |
| 64 | 4 | 46.735 | 46.978 | +0.519% | 1729.213 → 1699.056 | 56.886 → 56.914 | 5313.050 → 5284.634 | 2249.116 → 2195.630 |

裁决：`primary_target_met=false`、`sse_gap_target_met=false`、`stable_regressions=[]`。c4两种输出长度均未达到至少5%的吞吐/E2E改善，最大停顿也未降低30%。max64/c1的两次相邻吞吐方向相反（-0.249%/+0.614%），不能据合并+0.181%宣称稳定收益。c4/max64两相邻吞吐+0.081%/+0.957%，合并+0.519%。每实现只有两次独立进程臂，非置信区间或推广资格。

两候选臂各rank均为445次池分配、877379次复用、0预算miss、峰值61107200申请bytes，Close后owned/active/quarantine全部0。减少分配次数没有带来预期端到端收益。r424从同一原始日志重算（whole-arm，含warmup）的混合prefill/decode调用平均1617.434→1596.056ms，仅下降1.322%，不能当作纯device kernel耗时。

r424同时重读明确失败的r410父运行：相对无profiler前后bracket均值，profile单格wall增加19.96–24.84%。这说明profile存在实际扰动，不能把公开malloc/free API时间直接全部当作可回收开销；不能据此精确归因每个API的扰动，也不追认r410整体通过。

独立冻结审计 `/data/statecentric-builds/qwen38-prefill-r423-abba-analysis.json` SHA `678625217a73f8c8e1e1606992c396401f4243993dbac4d9282bc68152a7c336`；后置有界诊断 `/data/statecentric-builds/qwen38-prefill-r424-followup.json` SHA `75dc2cae68a97492b06e460f8b874698e2283a6494c0ac4b8b9d4db71b1988b4`。r415保留实验资格与负结果，不提升默认。下一轮先准入同拓扑HUST TP2×PP2、再做低扰动联合prefill关键路径定位；仍需保留r406/r407的TP4拓扑混杂和跨引擎输出差异，不把本轮Native内部精确一致当作跨引擎等质量通过。


## 2026-09-03 r425：当前 decode 设备区间复核（部分诊断）

`/data/statecentric-builds/qwen38-r425-device-intervals.json`，SHA-256
`22d8bb0d876934072cc777ed1779969b2e00fdbdd721f2746d5b259e7a1b1b14`。
性质为 `derived-artifact`：重新校验 r411 所绑定的 r410 原始 CSV、SQLite 和
时钟/host batch 记录，没有重新运行 profiler，也不追认 r410 整体验收成功。
四份 rank1/rank3 × BFCL-multiple/WildChat profile，各 64 次图执行，其中
63 次不与 prefill host 窗口相交、1 次在混合窗口内。

按真实执行时间区间并集去重后，每个 rank 的 decode 图包络中，MatMul 占
74.67–74.94%，全部计算任务占 91.13–91.55%；不与计算重叠的通信包络约
6.0–6.4%，计算/通信/拷贝之外约 1.1%。每次图执行的 MatMul 约
17.66–17.72 ms，图包络约 23.57–23.71 ms。这复核了旧 r073/r081 的
small-M MatMul 主导方向；不能把同步 API 的等待时间再加到设备时间上。

Prefill host 窗口中的单 rank 计算覆盖率仅约 38–40%，但窗口包含其他 PP
阶段和混合 decode 的等待，剩余时间不能视为可回收空转。旧 profiler 对
单格 wall 的扰动约 20–25%；本文不估算可实现加速比例。图内 MatMul 的
shape/dtype 元数据多为 N/A，生成符号里的 FP16 字样不证明模型改用了 FP16；
没有据此宣称 HBM 带宽或计算单元已经饱和。

冻结 r399 manifest 明确使用 `mlp_variant=1`；当前每序列 prefill 上限64
 tokens，最多两序列组成128-token波次。GDN 保留按序列几何，因为 r133–r146
曾证实合批形状/位置影响 BF16 状态与输出；当前实现已有 sequence streams，
不能概括成所有 GDN 串行执行。`ExecutePrefillDecodeOverlap` 在收齐两组
wave/rank 完成后才返回，rank 内部的小波次并不自动成为 host 的可调度边界。

后续不能直接重复 r029/r032 Gate-Up 融合/辅助流、r093 Down-NZ、r095 Mm
替换或 r074–r080 固定 host chunk 试验；这些已有真实负结果。优先完成 HUST
TP2×PP2 对照，分离 TP4 拓扑混杂，再选择能保持数值和物理生命周期契约的改动。


## 2026-09-03 r429：MatMul 硬件计数器覆盖率核验

`/data/statecentric-builds/qwen38-r429-matmul-pmu.json`，SHA-256
`5f11bc6f1a09a38c301e947da2ed4a4045e5d85a49217ded0c884f138fdeee9c`，
为 r425/r411 原始数据库的 `derived-artifact`，仍是失败 r410 父实验的部分诊断。

CANN 的 `globalTaskId` 在每次图重放时复用；TASK 和 TASK_PMU_INFO 直接相连
会把重复次数乘起来。分析分别聚合两表，并要求每项 PMU 的条数与实际执行次数
一致。跨图内/图外的逻辑 task 单列 ambiguous，不捏造逐次计数器归属。

四份 profile 中，纯图内 MatMul 各15,808次执行的 PMU 都是全零占位记录：
这表示没有有效计数器，MAC/MTE 比例报告 null，不能称“计算利用率为零”。
有非零 PMU 的图外 MatMul，按报告的 AIC counter time 分子/分母分别求和，
MAC 比例11.57–11.66%，MTE2比例88.81–89.95%。它提示图外矩阵乘存在较大
数据搬运压力；这些管线可重叠，比例不能相加，也不能外推成 decode 图内
带宽饱和或 GB/s。graph MatMul 占约75%的**时间瓶颈**已经定位，但更具体的
带宽/算力归因仍需有效 PMU 或单一机制的端到端验证。


## 2026-09-03 r426/r427/r428：Native 与 HUST TP2×PP2 同拓扑实测

r426：`/data/statecentric-builds/qwen38-r426-tp2pp2-compare`，`real-online`，
HUST 后 Native r399，均仅 NPU4–7。独立冻结分析 r427：
`/data/statecentric-builds/qwen38-r427-tp2pp2-analysis.json`，SHA-256
`6420200a7b4b6faffd61c04d1e2657b662eabfce680f83b26c98df6b0ff00ce7`，
`validated=true`。r428 为后置端到端差额与 SSE 复算，非预注册 analyzer：
`/data/statecentric-builds/qwen38-r428-matched-bottlenecks.json`，SHA-256
`42ed312bf0172bb8468c915d101748178ea689afb31d3ad819351b05d00ce6cc`。

固定模型 revision、BF16、context2048、active4、APC off，沿用 r406 全部输入，
四请求族、c1/c4、max16/max64、gap100。每端256请求=64完整单元预热+192测量；
共512请求。HUST使用原固定镜像，只将独立比较 launcher 的TP4改成TP2×PP2，
保留FULL_DECODE_ONLY、[1,2,4]捕获尺寸、async scheduling、chunked prefill；
日志有真实捕获和重放，Native捕获/重放计数完整守恒。HUST首个预热单元约71秒，
后续同单元约4.2秒；所有预热均按冻结规则保留但不混入以下汇总。

表中所有成对数字均为 **Native / HUST**。吞吐按单元 token 总数除以 wall 总和，
延迟为请求均值；最大非空语义 SSE 间隔的 P95 不含 TTFT。

| max tokens | c | tokens/s | TTFT ms | TPOT ms | E2E ms | max-gap P95 ms |
|---|---|---|---|---|---|---|
| 16 | 1 | 10.636 / 15.305 | 800.7 / 378.9 | 46.890 / 44.418 | 1504.0 / 1045.1 | 55.8 / 55.6 |
| 16 | 4 | 21.094 / 42.888 | 1722.2 / 539.6 | 76.540 / 51.873 | 2870.3 / 1317.7 | 2039.0 / 394.5 |
| 64 | 1 | 17.583 / 21.323 | 740.6 / 375.9 | 46.010 / 41.665 | 3639.2 / 3000.8 | 56.4 / 51.2 |
| 64 | 4 | 46.752 / 69.544 | 1724.0 / 545.5 | 56.935 / 46.993 | 5310.9 / 3506.0 | 2067.5 / 393.5 |

c4/max64，HUST吞吐约为Native的1.4875倍；端到端差额1804.875ms，其中
TTFT差1178.518ms，占65.296%，首语义输出之后差626.357ms。c4/max16 的
TTFT差占E2E差76.168%。这是端点时间恒等式的拆分，不把TTFT等同于纯设备
prefill、不把剩余差额等同于纯decode算子时间。Native含预热的whole-arm日志仍有
32次混合调用、平均1610.089ms；1216次B4 host decode平均50.536ms。

192个测量请求中150个跨引擎内容/usage/finish完全一致，42个不同。两端各自
64/64组在三次测量中重复稳定；这不消除跨引擎差异，不能作等质量速度结论。
两种HUST拓扑的历史/本次运行时间不同，不能把88.986→69.544 tokens/s
全部当成拓扑的因果效应。两端CPU策略仍不同：HUST实际各rank为0–191，
Native容器为0–23,48–71；HUST自动绑核失败警告在r406也存在。这里匹配的是
TP/PP拓扑与公开工作负载配置，不是所有内部调度、CPU或kernel路径。

正常退出、packed activation lease drain、NPU/FD释放、保护业务身份和独立
r113恢复均通过；恢复PID1311597/start746415538，默认仍r153，不提升候选。
所有50个冻结工具文件在运行中保持原字节，分析器从已验证archive执行。

结合r425，下一优先级为 **prefill执行/完成边界**，decode small-M MatMul为
第二线。具体候选需在不改变64-token数值几何的前提下，提供worker内部合法
wave yield/resume，让已完成decode可继续推进，避免每个小wave新增全局往返。
必须先完成cursor/generation/carry与graph引用生命周期，取消不提前释放；
yield能力与SLO/合批策略分开。频繁小B1可能伤吞吐，因此仍要求exact、取消/drain、
图模式及同配置ABBA，并同时满足E2E/吞吐和SSE尾延迟目标。这个新执行机制
尚未实现/部署；本轮交付是实测基线与瓶颈定位，没有新增性能候选的加速结论。

## 2026-09-03 r430/r431：prefill continuation 的软件实现与冻结构建

证据类型 `derived-artifact`，不是 NPU 实测。r430 提取并接入拥有输入和身份的
prefill cursor；r431 进一步将真实 rank 适配器拆为 `Advance`/`Finish`，保留结果行、
验证分配作用域，并恢复请求/microbatch 上下文。现有命令仍连续执行到结束，
没有开放额外在途批次，也没有独立 decode 完成通知。

每个冻结版本均通过 device-free CPU 9/9、ASan/UBSan 9/9、CANN selected 2/2，
完整 executor DSO 和 protocol worker 编译通过。测试覆盖旧 cold/retained 分区、
ragged/append 位置、输入所有权、错误策略、状态代次、提前/重复完成及取消后在途引用。
多依赖 ACK 测试属于注入契约；不能移植为真实跨 rank、graph scratch 或取消验收。

| 构建 | build_manifest.json SHA-256 | source.tar.gz SHA-256 |
|---|---|---|
| `/data/statecentric-builds/qwen38-prefill-continuation-r430-frozen` | `1609b4d0d3fe3bc117acb02ae4c5b59910d440f2dc84d627fdd846fa68353671` | `19289c4fd9725a18bf9e7b8afe16958dd74f07489f41098266ac45eac9201160` |
| `/data/statecentric-builds/qwen38-prefill-continuation-r431-frozen` | `617e8f77dd3afd9322fd11eb58451469cf36582a43f0114ea230f29f163323c3` | `126b0651d53f154ba6768a22934be1322b17412b9155f0c8a0c9ffcebb03862a` |

r431 executor SHA-256：`175fc7fe8a9f34e5b3dc3e1e2db7daed2443c9f8bc77bd6299e48fc9b2e6fca0`。
源码、命令日志和全部产物哈希已独立重验，工作树相关代码与 r431 冻结输入一致。
两个 Restart=no user build units 均正常结束，未挂载 NPU 设备、未切换在线服务。
18093/18083/18001 健康探测均 HTTP 200；默认和 launcher 未修改。

尚未封装/准入新在线候选。下一步必须贯通 cohort 执行次序、provider/protocol
独立完成及 actor 的多轮 decode credit，再进行 exact/B1–B4/all14 cancel/drain
真机验收和同配置 ABBA。完整边界见 `native-pipeline-activation-lease.md`。
工作记录与独立哈希复核：`/data/statecentric-builds/native-resumable-prefill.32kmgn4i/`。

## 2026-09-20：hybrid recurrent state-group host contract

证据类型 `host-structural`，属于 #73 StateAxis unscored intake，不继承旧性能资格。
`NativeModelIr` 新增结构化 Gated DeltaNet 语义，`StateGroupPlan` schema v2 将
conv history 与 recurrent matrix 降为一个固定状态组，并与 token-growing paged KV
置于同一 request transaction。固定组在首次 materialize 时占一个 snapshot slot，
fork 后首次更新 COW 一次，后续 token 增长不增加 recurrent 容量；任一 pool admission
失败会 poison 整个 shadow transaction，不能发布部分 state generation 或 token position。

Qwen3.8 TP4 fixture 覆盖 48 个 GDN 层和 16 个 full-attention 层。Rust lowering 得到
每 rank 每 sequence 固定状态 38,486,016 bytes、4,096-token KV 67,108,864 bytes、
合计 105,594,880 bytes，与现有 `native/src/qwen38_state_plan.cpp` 的 host 公式一致。
测试还覆盖 TP divisibility、recurrent matrix 非 token-growing 约束、fork/COW、联合
admission、失败回滚以及 cancel/evict 零泄漏。

该结果未接在线 worker/protocol，未运行 NPU，也没有 token exactness、HBM、容量、
TTFT、TPOT 或吞吐结论。下一门禁是把 ordered group descriptor 与 plan identity 接入
Qwen3.8 worker，再依次执行独立 oracle、失败恢复、matched uniform-vs-typed capacity
和重复 online E2E。完整契约见
[`HYBRID_RECURRENT_STATE_GROUP_CONTRACT.md`](HYBRID_RECURRENT_STATE_GROUP_CONTRACT.md)。

## 2026-09-20：typed state-group protocol-v3 binding

证据类型 `host-structural`，属于 #73 StateAxis unscored intake。protocol-v3 新增
default-off flag `0x4`，在既有 tokens、sampling、adapter 后携带 ordered typed
state-group plan。schema-v1 prefix 固定 40 bytes，每个 descriptor 固定 72 bytes，
绑定 plan identity、group order、state kind、growth/prefix policy、layer/窗口/块几何、
rank-local token/fixed-state bytes 和 operator-binding SHA-256。

Rust 与 C++ 对同一 Qwen3.8-shaped recurrent + full-KV 请求产生完全相同的 332-byte
frame；golden 文件为 `native/tests/native_protocol_state_groups_v3.hex`。codec 拒绝未知
枚举、零 identity、重排/不连续 ID、类型与增长规则冲突、非 canonical 几何、reserved
非零、截断和 trailing bytes。无 state-group 的 legacy protocol-v3 frame 保持逐字节不变，
三个可选 extension 可组合且顺序固定。

本结果未把 client 提供的 digest 当作信任根。在线 worker 尚未把 decoded plan 与独立
resident compiled plan 对照，也未让 Qwen3.8 arena 按 typed group 执行 physical ownership。
因此没有 worker lifecycle、NPU exactness、HBM、容量、延迟或吞吐资格；这里只完成
跨语言 transport 和 fail-closed syntax 门禁。

## 2026-09-28：七个 ECPA mod 的真机功能闭环与 matched screen

证据类型为 `matched-real-online-single-service-candidate`，仍属于 #73 StateAxis
unscored intake。commit `167e3945350dbf080542fd1c2adca621364da2e7` 与镜像
`stateaxis/runtime:dev42-cann91` 在物理 NPU4--7、Qwen3.8-27B、TP4、eager 下，
先后完成 ECPA-off control 和七个 active carrier。每轮均核对端口 PID 与容器 PID，
显式停止 Docker，并确认端口和 NPU4--7 归零；NPU0--3 未使用。

七个机制都产生了进程内效果证据并通过健康/回收检查。feedback emitted=108；
Ascend action 只有 fallback=96；hybrid 6/6 fork 接受、18,432 inherited tokens、
30 shared references、结束 ownership=0；no-harm prepared/promoted=6/6；dependency
generation advance/state invalidation=3/3；workflow 对有效/过期 hint 分别记录 admitted
与 validity_rejected 且均返回 HTTP 200；hibernation hibernated/resumed=5/5。

性能 screen 只发现 feedback 单次中位数低 1.06%，尚无跨服务重复，不能晋级。
其余 matched 路径慢 1.00%--8.20% 或仅命中 fallback。hybrid 每请求实际复制
76,972,032 recurrent-state bytes，是当前主要机制成本。所有结果保持
`performance_qualified=false`。此外，ECPA-off 进程仍可由请求 xarg 触发 generic
state-fork；它是待关闭的管理边界，不能把 carrier admission 表述成独占 activation。

首次四个候选计时因 ECPA parent 停止后 privileged Docker child 仍占 18094 而判为
`invalid-port-custody`，原始数据保留但不支持任何性能结论。修正后的完整证据位于
`/data/statecentric-builds/stateaxis-ecpa-seven-performance-20260928-r001`，其
`PERFORMANCE_SUMMARY.json` SHA-256 为
`08f7032ceb48eb3e90346b63e1f597f9b2491b98273fa39bf86763075c6ed857`，全树清单
`ALL_SHA256SUMS` SHA-256 为
`24f3afb939b891b14aaa7a2be5bccfa268faa266dfa9e26642d48c14559d87fa`。
