# ECPA activation-contract evidence

Label: `real-npu-component-bytes-positive-online-unqualified`.

For a stable state ID and generation, the worker keeps a host shadow of the
fixed device row and directly patches only changed slot and contiguous block
ranges. An uninitialized row, state/generation change or dual-microbatch path
uses the exact full-upload fallback. Stale generations remain rejected by the
allocator.

The real-NPU component pair produced identical D2H snapshots. For the tested
append update, control transferred a 32-byte block row plus a 4-byte slot;
candidate transferred two changed block entries plus the slot, or 12 bytes.
This small component cell does not establish online latency or throughput.
