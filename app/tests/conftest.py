import asyncio
import pytest

from httpx import AsyncClient

from fastapi.testclient import TestClient
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from typing import AsyncGenerator

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.pool import NullPool
from sqlalchemy import insert
from sqlalchemy import update

from redis import asyncio as async_redis

from database.base_class import Base
from models.models import Role
from models.models import User
from database.session import get_async_session
from tests.utils.utils import get_superuser_token
from tests.utils.utils import create_superuser
from settings import settings
from main import app


engine_test = create_async_engine(settings.DATABASE_URL_TEST, poolclass=NullPool)
async_session_maker = sessionmaker(engine_test, class_=AsyncSession, expire_on_commit=False)


metadata = Base.metadata
metadata.bind = engine_test


async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


app.dependency_overrides[get_async_session] = override_get_async_session


client = TestClient(app)


@pytest.fixture(autouse=True, scope="session")
def init_redis():
    redis = async_redis.from_url(
            f"redis://localhost:{settings.REDIS_PORT}", 
            encoding="utf8", 
            decode_responses=True)
    
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")


@pytest.fixture(autouse=True, scope="session")
async def prepare_test_database():
    async with engine_test.begin() as connection:
        await connection.run_sync(metadata.create_all)
    yield
    async with engine_test.begin() as connection:
        await connection.run_sync(metadata.drop_all)


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def async_client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test", follow_redirects=True) as client:
        yield client


@pytest.fixture(scope="session")
async def superuser_token():
    async with async_session_maker() as session:
        statement = insert(Role).values(
            [{"id": 1, "name": "user", "permissions": None},
             {"id": 2, "name": "admin", "permissions": None},
             {"id": 3, "name": "root", "permissions": None}])
        
        await session.execute(statement)
        await session.commit()
        create_superuser(client)
    
        statement = update(User).where(User.email == settings.ROOT_LOGIN).values(role_id=3, is_superuser=True)
        await session.execute(statement)
        await session.commit()
        
    return get_superuser_token(client)
