from src.pysysinfo.dumps.linux.linux_dump import LinuxHardwareManager


lhm = LinuxHardwareManager()

lhm.cpu_info()

print(lhm.info)