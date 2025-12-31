Classes
=======

Hardware Managers
-----------------
- `WindowsHardwareManager`: Implements `HardwareManagerInterface` and pulls CPU, memory, storage, and graphics data via Windows Registry and WMI helpers. See [src/pysysinfo/dumps/windows/windows_dump.py](src/pysysinfo/dumps/windows/windows_dump.py#L14-L49).
- `MacHardwareManager`: Uses `sysctl` and IORegistry helpers to populate platform models. See [src/pysysinfo/dumps/mac/mac_dump.py](src/pysysinfo/dumps/mac/mac_dump.py#L14-L49).
- `LinuxHardwareManager`: Reads sysfs-driven helpers to build the Linux hardware snapshot. See [src/pysysinfo/dumps/linux/linux_dump.py](src/pysysinfo/dumps/linux/linux_dump.py#L12-L49).

The top-level `HardwareManager` alias in [src/pysysinfo/__init__.py](src/pysysinfo/__init__.py#L1-L14) selects one of the managers above based on the current platform, so user code can depend on a single interface.
