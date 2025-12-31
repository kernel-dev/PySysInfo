from pydantic import BaseModel, Field

from pysysinfo.models.status_models import SuccessStatus, StatusModel


class ComponentInfo(BaseModel):
    # Each component gets its own fresh status object
    status: StatusModel = Field(default_factory=SuccessStatus)
