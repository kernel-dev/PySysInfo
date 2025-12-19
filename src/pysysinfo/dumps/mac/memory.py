import subprocess

from src.pysysinfo.dumps.mac.ioreg import corefoundation_to_native, IORegistryEntryCreateCFProperties, \
    IORegistryEntryFromPath, kIOMasterPortDefault, kNilOptions
from CoreFoundation import kCFAllocatorDefault
from src.pysysinfo.models.memory_models import MemoryInfo
from src.pysysinfo.models.status_models import FailedStatus


def fetch_memory_info() -> MemoryInfo:

    memory_info = MemoryInfo()
    """
    Memory Module Information, can only work on Intel and AMD machines.
    Does not work on Apple Silicon, because the modules are part of the SoC, and the info we need is not exposed.
    """
    arch = subprocess.check_output(["uname", "-m"]).decode()
    """
    Output:
    x86_64 for late-model Intel Macs
    i386 for earlier Intel Macs
    arm64 for Apple Silicon
    """
    if "arm" in arch.lower():
        memory_info.status = FailedStatus()
        return memory_info

    interface = corefoundation_to_native(
        IORegistryEntryCreateCFProperties(
            IORegistryEntryFromPath(kIOMasterPortDefault, b"IODeviceTree:/memory"),
            None,
            kCFAllocatorDefault,
            kNilOptions,
        )
    )[1]
    if not interface:
        memory_info.status = FailedStatus()
        return memory_info

    modules = []
    part_no = []
    sizes = []
    length = None

    print(interface)
    print(interface.keys())
    print(interface.values())

    print("----")
    for k, v in interface.items():
        print(k)
        print(v)

    return memory_info
