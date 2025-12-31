Models
======

PySysInfo exposes Pydantic models for each hardware subsystem plus shared helpers for capacity units and discovery status.

----------------
Component Models
----------------

=============
CPU
=============
.. autopydantic_model:: pysysinfo.models.cpu_models.CPUInfo
    :show-inheritance:
    :inherited-members: ComponentInfo
    :exclude-members: __init__

=============
GPU
=============

.. autopydantic_model:: pysysinfo.models.gpu_models.GraphicsInfo
    :show-inheritance:
    :inherited-members: ComponentInfo
    :exclude-members: __init__

.. autopydantic_model:: pysysinfo.models.gpu_models.GPUInfo
    :exclude-members: __init__

- ``MemoryInfo``
- ``MemoryModuleInfo``
- ``MemoryModuleSlot``
- ``StorageInfo``
- ``DiskInfo``

-------------
Status Models
-------------

.. autopydantic_model:: pysysinfo.models.status_models.SuccessStatus
    :exclude-members: __init__
    :show-inheritance:

.. autopydantic_model:: pysysinfo.models.status_models.PartialStatus
    :exclude-members: __init__
    :show-inheritance:

.. autopydantic_model:: pysysinfo.models.status_models.FailedStatus
    :exclude-members: __init__
    :show-inheritance:

.. autopydantic_model:: pysysinfo.models.status_models.StatusModel
    :exclude-members: __init__

---------------
Capacity Models
---------------
