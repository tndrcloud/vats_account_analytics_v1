from datetime import datetime
from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy import Column, String, Boolean, Integer, TIMESTAMP, ForeignKey
from sqlalchemy.ext.asyncio import AsyncSession
from models.models import role
from database.session import Base, get_async_session


class User(SQLAlchemyBaseUserTable[int], Base):
    id: int = Column(Integer, primary_key=True)
    email: str = Column(String, nullable=False)
    username: str = Column(String, nullable=False)
    hashed_password: str = Column(String(length=1024), nullable=False)
    registered_at: datetime = Column(TIMESTAMP, default=datetime.utcnow)
    role_id: int = Column(Integer, ForeignKey(role.c.id))
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
