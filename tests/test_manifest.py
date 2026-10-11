import hashlib
import json
from pathlib import Path

import pytest
from vllm_hust_ext.manifest import activation_blocker, load_manifest

import stateaxis_device_metadata_delta
from stateaxis_device_metadata_delta import (
    DeviceMetadataDeltaConfig,
    device_metadata_delta,
)


def test_manifest_is_active_and_hash_bound() -> None:
    package = Path(stateaxis_device_metadata_delta.__file__).parent
    repo = package.parents[1]
    path = package / "vllm-hust-extension-v0.3.json"
    manifest = load_manifest(path)
    assert activation_blocker(manifest) is None
    raw = json.loads(path.read_text())
    expected = raw["activation"]["additional_config"]["stateaxis_mod"][
        "manifest_sha256"
    ]
    actual = hashlib.sha256((repo / "RESEARCH_MANIFEST.json").read_bytes()).hexdigest()
    assert actual == expected


def test_contract_is_sparse_generation_bound_and_not_a_kernel_claim() -> None:
    assert device_metadata_delta() == DeviceMetadataDeltaConfig()
    with pytest.raises(ValueError, match="reviewed contract"):
        DeviceMetadataDeltaConfig(device_kernel=True)
