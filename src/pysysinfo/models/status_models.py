from typing import List, Optional

from pydantic import BaseModel, Field


class StatusModel(BaseModel):
    string: str
    messages: List[str] = Field(default_factory=list)


class SuccessStatus(StatusModel):
    string: str = "success"
    messages: List[str] = Field(default_factory=list)


class PartialStatus(StatusModel):
    """
    Class to denote a Partially failed discovery of a particular component.
    """
    string: str = "partial"
    messages: List[str] = Field(default_factory=list)


class FailedStatus(StatusModel):
    """
    Class to denote a the complete failure of discovery for a particular component.
    A Failed state can be logged like so:
    ```
    cpu_info.status = FailedStatus("Failed to open /proc/cpuinfo")
    ```
    """
    string: str = "failed"
    messages: List[str] = Field(default_factory=list)

    def __init__(self, message: Optional[str] = None, messages: Optional[List[str]] = None):
        # Ensure each instance gets its own list
        base_messages = list(messages) if messages else []
        if message:
            base_messages.append(message)
        super().__init__(string="failed", messages=base_messages)


"""
The intention of `messages` being List[str] is that PartialStatus can benefit from containing many messages.

When changing the status of a component to PartialStatus(), we do the following.
```
cpu_info.status = PartialStatus(messages=cpu_info.status.messages))
cpu_info.status.messages.append("My New Debug Message")
```

This is done because cpu_info.status may be an instance of SuccessStatus or PartialStatus.
if it is FailureStatus, the discovery of that component would have probably stopped after reaching the failure state.

The above code snippet can be replaced with the below snippet, and would yield the same result. 
```
if isinstance(cpu_info.status, PartialStatus):
    cpu_info.status.messages.append("My New Debug Message")
else:
    cpu_info.status = PartialStatus(messages=["My New Debug Message"])]
```
"""
