from pysysinfo.dumps.windows.cpu import fetch_cpu_info
from pysysinfo.dumps.windows.graphics import fetch_graphics_info
from pysysinfo.dumps.windows.memory import fetch_memory_info
from pysysinfo.dumps.windows.storage import fetch_storage_info
from pysysinfo.models.cpu_models import CPUInfo
from pysysinfo.models.gpu_models import GraphicsInfo
from pysysinfo.models.info_models import WindowsHardwareInfo
from pysysinfo.models.memory_models import MemoryInfo
from pysysinfo.models.storage_models import StorageInfo


class WindowsHardwareManager:
    """
    Instance, implementing `DeviceManager`, for extracting system information
    from Windows using the Registry and WMI
    """

    def __init__(self):
        self.info = WindowsHardwareInfo(
            cpu=CPUInfo(),
            memory=MemoryInfo(),
            storage=StorageInfo(),
            graphics=GraphicsInfo(),
        )

    def fetch_cpu_info(self):
        pass
        self.info.cpu = fetch_cpu_info()

    def fetch_memory_info(self):
        pass
        self.info.memory = fetch_memory_info()

    def fetch_storage_info(self):
        self.info.storage = fetch_storage_info()

    def fetch_graphics_info(self):
        self.info.graphics = fetch_graphics_info()
