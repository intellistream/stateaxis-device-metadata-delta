# stateaxis-device-metadata-delta

Extension ID: `org.vllm-hust.stateaxis-device-metadata-delta`

This active experimental MOD implements the bounded first production mechanism
for StateAxis issue [#5](https://github.com/Qixin-Gaoke/stateaxis/issues/5).
Shuhao Zhang (Tony) is directly responsible; no advisor is declared.

For decode rows whose state ID and generation remain stable, the worker retains
the fixed device block-table and slot buffers and directly uploads only changed
slot values and contiguous changed block ranges. A new row, generation change
or uninitialized cache uploads the complete row. Dual microbatch invalidates
the sparse cache and uses its existing full-upload path. The allocator remains
the ownership authority and rejects stale generations.

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

Rust matched runtime tests preserve exact output and record candidate decode
batches/requests. The complete native worker builds against CANN/ATB 9.1. A
real-NPU component pair produced identical device snapshots while the tested
append update transferred 36 bytes in control and 12 bytes in candidate.

That 66.67% byte reduction is a single small component cell. It is not an
online latency or throughput result. A fresh identity-bound full-model artifact
and alternating 3+3 service matrix remain required. See [EVIDENCE.md](EVIDENCE.md).

## Validate

```bash
python -m pip install -e '.[test]'
ruff check .
ruff format --check .
pytest -q
python -m build
```
