# PySysInfo

A Python Library to simplify retrieval of hardware components of your computer.

## Installation

```bash
pip install PySysInfo
```

## Usage

```python
from pysysinfo import HardwareManager

# Initialize the manager (automatically detects OS)
hm = HardwareManager()

# Fetch CPU info
hm.fetch_cpu_info()
print(hm.info.cpu)

# Fetch Memory info
hm.fetch_memory_info()
print(hm.info.memory)

# Fetch Storage info
hm.fetch_storage_info()
print(hm.info.storage)

# Fetch Graphics info
hm.fetch_graphics_info()
print(hm.info.graphics)
```

## Tracker

### Hardware Discovery

- Linux
  - [x] CPU
  - [x] GPU
  - [x] Memory
  - [ ] Network
  - [ ] Audio
  - [ ] Motherboard
  - [ ] Input
  - [x] Storage
- macOS
  - [x] CPU
  - [x] GPU* [could get more info than what is currently discovered]
  - [x] Memory
  - [ ] Network
  - [ ] Audio
  - [ ] Vendor
  - [ ] Input
  - [x] Storage
  - [ ] Display
- Windows
  - [x] CPU
  - [x] GPU* [PCIe gen info only for Nvidia GPUs]
  - [x] Memory
  - [ ] Network
  - [ ] Audio
  - [ ] Motherboard
  - [ ] Input
  - [x] Storage

### Supporting Features

- [ ] PCI Lookup - DeviceHunt
- [ ] PCI Lookup - [PCI IDs Repository](https://pci-ids.ucw.cz) - [GitHub](https://github.com/pciutils/pciids/blob/master/pci.ids)
- [ ] Intel ARK and AMD Equivalent
- [ ] Logging
- [ ] Working Library
