=================
Hardware Managers
=================

Depending on the OS present, PySysInfo can automatically load one of the following Hardware Manager classes.
All these classes implement the structure in :class:`pysysinfo.models.info_models.HardwareManagerInterface`.

------------

When the following code is run on a macOS machine, the output is as follows.

.. code-block:: python

    import pysysinfo
    from pysysinfo.models.info_models import HardwareManagerInterface

    hm = pysysinfo.HardwareManager()

    print(type(hm))
    print(isinstance(hm, HardwareManagerInterface))


Output:

.. code-block:: shell

    <class 'pysysinfo.dumps.mac.mac_dump.MacHardwareManager'>
    True

------------

The ``HardwareManager`` has the following methods:

.. autoclass:: pysysinfo.models.info_models.HardwareManagerInterface
    :members:

Depending on your OS, one of the following classes will be instantiated:

.. autoclass:: pysysinfo.dumps.windows.windows_dump.WindowsHardwareManager
    :exclude-members: __init__,__new__
    :noindex:

.. autoclass:: pysysinfo.dumps.mac.mac_dump.MacHardwareManager
    :exclude-members: __init__,__new__
    :noindex:

.. autoclass:: pysysinfo.dumps.linux.linux_dump.LinuxHardwareManager
    :exclude-members: __init__,__new__
    :noindex:

------------

We can now use this knowledge to query information about the hardware.

.. code-block:: python

    import pysysinfo

    hm = pysysinfo.HardwareManager()

    info = hm.fetch_hardware_info()
    print(type(info))

Output on a macOS machine:

.. code-block:: shell

    <class 'pysysinfo.models.info_models.MacHardwareInfo'>

------------

Information can be queried all at once, or on a per-component basis.

:meth:`fetch_hardware_info() <pysysinfo.models.info_models.HardwareManagerInterface.fetch_hardware_info>` can be used to query all info.

The other methods in the
:class:`HardwareManagerInterface <pysysinfo.models.info_models.HardwareManagerInterface>`
class can be used to query each component.


We explore ``HardwareInfo`` in the :ref:`querying-info` section.