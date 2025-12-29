import os
import platform

__version__ = "0.0.1"
__author__ = "Mahasvan"
__license__ = "BSD-3-Clause"

if os.name == "nt":
    from pysysinfo.dumps.windows.windows_dump import WindowsHardwareManager as HardwareManager
elif platform.system() == "Darwin":
    from pysysinfo.dumps.mac.mac_dump import MacHardwareManager as HardwareManager
else:
    from pysysinfo.dumps.linux.linux_dump import LinuxHardwareManager as HardwareManager

__all__ = ["HardwareManager"]
