from pydantic import BaseModel


class Data(BaseModel):
    name: str


class CustomerResponse(BaseModel):
    data: Data
    success: bool
