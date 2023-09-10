from sqlalchemy import insert, select, update

from models.models import Role
from models.models import User
from tests.conftest import async_session_maker
from settings import settings


async def test_add_role():
    async with async_session_maker() as session:
        statement = insert(Role).values(id=4, name="guest", permissions=None)
        await session.execute(statement)
        await session.commit()

        query = select(Role).where(Role.id == 4)
        response = await session.execute(query)
        result = response.scalars().first() 

        assert result.name == "guest"


async def test_create_superuser():
    async with async_session_maker() as session:
        statement = update(User).where(User.email == settings.USER_LOGIN).values(is_superuser=True)
        await session.execute(statement)
        await session.commit()

        query = select(User).where(User.email == settings.USER_LOGIN)
        response = await session.execute(query)
        result = response.scalars().first()

        assert result.is_superuser is True
