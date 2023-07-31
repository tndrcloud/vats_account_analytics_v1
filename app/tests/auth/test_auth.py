from sqlalchemy import insert, select, update
from models.models import role, user
from tests.conftest import async_session_maker, client
from settings import settings


async def test_add_role():
    async with async_session_maker() as session:
        statement = insert(role).values(id=4, name="guest", permissions=None)
        await session.execute(statement)
        await session.commit()

        query = select(role)
        response = await session.execute(query)
        result = response.mappings().all() 

        assert result[3]["name"] == "guest"


def test_register():
    response = client.post("api/auth/register", json={
        "email": settings.USER_LOGIN,
        "password": settings.USER_PASSWORD,
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "username": "string",
        "role_id": 1
        }
    )

    assert response.status_code == 201


async def test_create_superuser():
    async with async_session_maker() as session:
        statement = update(user).where(user.c.email == settings.USER_LOGIN).values(is_superuser=True)
        await session.execute(statement)
        await session.commit()

        query = select(user).where(user.c.email == settings.USER_LOGIN)
        response = await session.execute(query)
        result = response.mappings().all()
        
        assert result[0]["is_superuser"] == True


def test_login():
    response = client.post("api/auth/login", data={
        "username": settings.USER_LOGIN,
        "password": settings.USER_PASSWORD,
        }
    )

    assert response.status_code == 200
    result = response.json()
    assert "access_token" in result
    assert result["access_token"]
