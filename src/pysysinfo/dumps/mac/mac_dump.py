from pysysinfo.dumps.mac.cpu import fetch_cpu_info
from pysysinfo.dumps.mac.graphics import fetch_graphics_info
from pysysinfo.dumps.mac.memory import fetch_memory_info
from pysysinfo.dumps.mac.storage import fetch_storage_info
from pysysinfo.models.cpu_models import CPUInfo
from pysysinfo.models.gpu_models import GraphicsInfo
from pysysinfo.models.info_models import MacHardwareInfo
from pysysinfo.models.memory_models import MemoryInfo
from pysysinfo.models.storage_models import StorageInfo


class MacHardwareManager:
    """
    Instance, implementing `DeviceManager`, for extracting system information
    from macOS using `sysctl` and IOreg
    """

    def __init__(self):
        self.info = MacHardwareInfo(
            cpu=CPUInfo(),
            memory=MemoryInfo(),
            storage=StorageInfo(),
            graphics=GraphicsInfo(),
        )

    def fetch_cpu_info(self):
        self.info.cpu = fetch_cpu_info()

    def fetch_memory_info(self):
        self.info.memory = fetch_memory_info()

    def fetch_storage_info(self):
        self.info.storage = fetch_storage_info()

    def fetch_graphics_info(self):
        self.info.graphics = fetch_graphics_info()
