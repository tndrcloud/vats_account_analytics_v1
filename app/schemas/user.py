from datetime import datetime

from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from fastapi_users import schemas


class User(BaseModel):
    id: int = Field(ge=0)
    email: str
    username: str
    hashed_password: str
    registered_at: datetime
    role_id: int
    is_active: bool
    is_superuser: bool
    is_verified: bool


class UserRead(schemas.BaseUser[int]):
    id: int
    username: str
    email: str
    role_id: int
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False


class UserCreate(schemas.BaseUserCreate):
    username: str
    email: str
    password: str
    role_id: int = 1
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class UserUpdate(schemas.BaseUserUpdate):
    username: str
    email: str
    password: str
    role_id: int = 1
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
    