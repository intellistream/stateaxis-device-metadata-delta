"""Generation-bound sparse decode metadata activation contract."""

from __future__ import annotations

from dataclasses import asdict, dataclass

MOD_ID = "org.vllm-hust.stateaxis-device-metadata-delta"


@dataclass(frozen=True, slots=True)
class DeviceMetadataDeltaConfig:
    enabled: bool = True
    scope: str = "decode-block-table-and-slot-direct-patch"
    device_resident_buffers: bool = True
    generation_bound_row_cache: bool = True
    sparse_contiguous_h2d: bool = True
    device_kernel: bool = False
    exact_host_shadow: bool = True
    full_row_on_identity_change: bool = True
    full_row_on_uninitialized_cache: bool = True
    dual_microbatch_fallback_to_full_upload: bool = True
    stale_generation_rejected_by_allocator: bool = True
    fixed_device_addresses: bool = True
    fail_closed: bool = True

    def __post_init__(self) -> None:
        expected = {
            "enabled": True,
            "scope": "decode-block-table-and-slot-direct-patch",
            "device_resident_buffers": True,
            "generation_bound_row_cache": True,
            "sparse_contiguous_h2d": True,
            "device_kernel": False,
            "exact_host_shadow": True,
            "full_row_on_identity_change": True,
            "full_row_on_uninitialized_cache": True,
            "dual_microbatch_fallback_to_full_upload": True,
            "stale_generation_rejected_by_allocator": True,
            "fixed_device_addresses": True,
            "fail_closed": True,
        }
        if asdict(self) != expected:
            raise ValueError("device metadata delta requires the reviewed contract")


def device_metadata_delta() -> DeviceMetadataDeltaConfig:
    return DeviceMetadataDeltaConfig()


__all__ = ["MOD_ID", "DeviceMetadataDeltaConfig", "device_metadata_delta"]
