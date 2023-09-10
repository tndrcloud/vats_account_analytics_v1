from datetime import datetime

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTable
from fastapi_users.db import SQLAlchemyUserDatabase

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import JSON
from sqlalchemy import Boolean
from sqlalchemy import Integer
from sqlalchemy import TIMESTAMP
from sqlalchemy import ForeignKey

from sqlalchemy.ext.asyncio import AsyncSession

from database.session import get_async_session
from database.base_class import Base


class Role(Base):
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String, nullable=False)
    permissions: str = Column(JSON, nullable=True)
    

    class Config:
        from_attributes = True


class User(SQLAlchemyBaseUserTable[int], Base):
    id: int = Column(Integer, primary_key=True)
    email: str = Column(String, nullable=False)
    username: str = Column(String, nullable=False)
    hashed_password: str = Column(String(length=1024), nullable=False)
    registered_at: datetime = Column(TIMESTAMP, default=datetime.utcnow)
    role_id: int = Column(Integer, ForeignKey(Role.id))
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)


    class Config:
        from_attributes = True
        

class Data(Base):
    name: str = Column(String, primary_key=True)
    main_info: str = Column(JSON, nullable=False)
    active_users: str = Column(JSON, nullable=False)
    incoming_line: str = Column(JSON, nullable=False)
    user_info: str = Column(JSON, nullable=False)
    contacts_user: str = Column(JSON, nullable=False)
    groups_user: str = Column(JSON, nullable=False)
    group_info: str = Column(JSON, nullable=False)
    users_in_group: str = Column(JSON, nullable=False)
    names_id_ivr: str = Column(JSON, nullable=False)
    ivr_params_events: str = Column(JSON, nullable=False)
    route_info: str = Column(JSON, nullable=False)
    route_settings: str = Column(JSON, nullable=False)


    class Config:
        from_attributes = True


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)