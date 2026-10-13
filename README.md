# stateaxis-device-metadata-delta

Extension ID: `org.vllm-hust.stateaxis-device-metadata-delta`

This active experimental MOD implements the bounded first production mechanism
for StateAxis issue [#5](https://github.com/Qixin-Gaoke/stateaxis/issues/5).
Shuhao Zhang (Tony) is directly responsible; no advisor is declared.

For decode rows whose state ID and generation remain stable, the worker retains
the fixed device block-table and slot buffers and skips unchanged data. It first
plans the whole batch, then keeps a single-row/single-range update sparse while
coalescing multiple slot rows or block ranges into contiguous batch uploads.
This bounds ACL submission overhead without giving up the zero-copy unchanged
case. A new row, generation change or uninitialized cache uploads the complete
row. Dual microbatch invalidates the cache and uses its existing full-upload
path. The allocator remains the ownership authority and rejects stale
generations.

This revision uses sparse H2D writes into device-resident buffers. It does not
contain or claim a device-side delta kernel. Historical V296/V297 changed full
metadata uploads from synchronous to asynchronous; they are retained as
historical evidence but are not treated as delta evidence.

## Activation

Activation is default-off and must go through vLLM-HUST Extension Manager/ECPA:

```bash
python -m pip install .
VLLM_HUST_EXT_CONFIG=evidence/ecpa-contract-20261011/manager-config.json \
  vllm-hust-ext extension check \
  org.vllm-hust.stateaxis-device-metadata-delta
VLLM_HUST_EXT_CONFIG=evidence/ecpa-contract-20261011/manager-config.json \
  vllm-hust-ext extension plan \
  org.vllm-hust.stateaxis-device-metadata-delta
```

StateAxis accepts only version `0.2.0` and the exact research-manifest SHA-256.
Rollback disables the extension and restores full block-table and slot uploads.

## Evidence boundary

The current matched component campaign used both available Ascend 910B2 devices,
32 block entries per sequence, 200 warmups and 2,000 measured repetitions per
cell. Every device snapshot matched. For a decode-shaped cycle with a slot
update every step and one new block every 128 steps, adaptive coalescing reduced
median metadata preparation plus H2D synchronization time by 1.92x/1.88x/1.85x
at B1/B8/B32 on device 0 and 1.91x/1.87x/1.86x on device 1. The former row-wise
sparse policy was negative at B8/B32 (0.25x/0.068x), which identifies ACL call
fan-out as the bottleneck and motivates the retained policy.

These are matched real-NPU **component** timings, not online request latency or
throughput. Fragmented/full-change cells remain slightly negative after
coalescing because host planning remains on the measured path. A fresh
identity-bound full-model artifact and alternating 3+3 service matrix remain
required. See [EVIDENCE.md](EVIDENCE.md).

## Validate

```bash
python -m pip install -e '.[test]'
ruff check .
ruff format --check .
pytest -q
python -m build
```
