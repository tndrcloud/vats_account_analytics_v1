from enum import Enum
from pydantic import BaseModel, Field


class RoleType(Enum):
    root = "root"
    admin = "admin"
    user = "user"


class Role(BaseModel):
    id: int = Field(ge=0)
    name: RoleType
    permissions: str


    class Config:
        from_attributes = True
        