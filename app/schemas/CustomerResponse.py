from pydantic import BaseModel
from typing import List, Optional


class CustomField(BaseModel):
    name: str
    value: Optional[str] = None


class Data(BaseModel):
    name: str
    internal_id: str
    custom_fields: List[CustomField]


class CustomerResponse(BaseModel):
    data: List[Data]
    success: bool
