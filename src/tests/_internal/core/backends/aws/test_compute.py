from dstack._internal.core.backends.aws.compute import _supported_instances
from dstack._internal.core.models.backends.base import BackendType
from dstack._internal.core.models.instances import (
    Disk,
    InstanceOffer,
    InstanceType,
    Resources,
)


def _instance_offer(instance_name: str) -> InstanceOffer:
    return InstanceOffer(
        backend=BackendType.AWS,
        instance=InstanceType(
            name=instance_name,
            resources=Resources(
                cpus=1,
                memory_mib=1024,
                gpus=[],
                spot=False,
                disk=Disk(size_mib=102400),
            ),
        ),
        region="us-east-1",
        price=1.0,
    )


def test_supported_instances_include_p6_b200() -> None:
    assert _supported_instances(_instance_offer("p6-b200.48xlarge"))


def test_supported_instances_exclude_unknown_families() -> None:
    assert not _supported_instances(_instance_offer("p6.2xlarge"))
