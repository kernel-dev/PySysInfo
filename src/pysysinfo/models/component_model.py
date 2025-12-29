from pydantic import BaseModel

from pysysinfo.models.status_models import SuccessStatus, StatusModel


class ComponentInfo(BaseModel):
    status: StatusModel = SuccessStatus()
