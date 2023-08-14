from sqlalchemy import select
from models.models import Data
from tests.conftest import async_session_maker, client
from tests.api.api_v1.json_data import json_data
from settings import settings


async def test_add_domain_data(superuser_token) -> None:
    response = client.post(
        "api/v1/domain/add_domain_data", 
        headers=superuser_token,
        json=json_data 
    )
    assert response.status_code == 201

    async with async_session_maker() as session:
        query = select(Data.main_info)
        response = await session.execute(query)
        result = response.scalars().first()

        assert result["domain_name"] and result["email"]


async def test_get_main_info(superuser_token) -> None:
    response = client.get(
        "api/v1/domain/get_main_info", 
        headers=superuser_token, 
        params={"domain": settings.SAMPLE_DOMAIN_NAME})

    assert response.status_code == 200
    content = response.json()

    async with async_session_maker() as session:
        query = select(Data.main_info)
        response = await session.execute(query)
        result = response.scalars().first()

        assert content == result


async def test_get_active_users(superuser_token) -> None:
    response = client.get(
        "api/v1/domain/get_active_users", 
        headers=superuser_token, 
        params={"domain": settings.SAMPLE_DOMAIN_NAME})

    assert response.status_code == 200
    content = response.json()

    async with async_session_maker() as session:
        query = select(Data.active_users)
        response = await session.execute(query)
        result = response.scalars().first()

        assert content == result


async def test_get_incoming_line_info(superuser_token) -> None:
    response = client.get(
        "api/v1/domain/get_incoming_line_info", 
        headers=superuser_token, 
        params={"domain": settings.SAMPLE_DOMAIN_NAME})

    assert response.status_code == 200
    content = response.json()

    async with async_session_maker() as session:
        query = select(Data.incoming_line)
        response = await session.execute(query)
        result = response.scalars().first()
        
        assert content == result


async def test_get_user_info(superuser_token) -> None:
    response = client.get(
        "api/v1/domain/get_user_info", 
        headers=superuser_token, 
        params={"domain": settings.SAMPLE_DOMAIN_NAME,
                "username": settings.ROOT_LOGIN,
                "number": settings.SAMPLE_INNER_NUMBER})

    assert response.status_code == 200
    content = response.json()

    async with async_session_maker() as session:
        query = select(Data.user_info)
        response = await session.execute(query)
        result = response.scalars().first()
        
        assert content == result


async def test_get_contacts_user(superuser_token) -> None:
    response = client.get(
        "api/v1/domain/get_contacts_user", 
        headers=superuser_token, 
        params={"domain": settings.SAMPLE_DOMAIN_NAME,
                "username": settings.ROOT_LOGIN,
                "login": settings.ROOT_LOGIN})

    assert response.status_code == 200
    content = response.json()

    async with async_session_maker() as session:
        query = select(Data.contacts_user)
        response = await session.execute(query)
        result = response.scalars().first()
        
        assert content == result


async def test_get_groups_user(superuser_token) -> None:
    response = client.get(
        "api/v1/domain/get_groups_user", 
        headers=superuser_token, 
        params={"domain": settings.SAMPLE_DOMAIN_NAME,
                "username": settings.ROOT_LOGIN,
                "login": settings.ROOT_LOGIN})

    assert response.status_code == 200
    content = response.json()

    async with async_session_maker() as session:
        query = select(Data.groups_user)
        response = await session.execute(query)
        result = response.scalars().first()

        assert content == result
        assert result[0]["groups_list"][0] == settings.SAMPLE_GROUP


async def test_get_group_info(superuser_token) -> None:
    response = client.get(
        "api/v1/domain/get_group_info", 
        headers=superuser_token, 
        params={"domain": settings.SAMPLE_DOMAIN_NAME,
                "group_name": settings.SAMPLE_GROUP,
                "number": settings.SAMPLE_INNER_NUMBER})

    assert response.status_code == 200
    content = response.json()

    async with async_session_maker() as session:
        query = select(Data.group_info)
        response = await session.execute(query)
        result = response.scalars().first()

        assert content == result


async def test_get_users_in_group(superuser_token) -> None:
    response = client.get(
        "api/v1/domain/get_users_in_group", 
        headers=superuser_token, 
        params={"domain": settings.SAMPLE_DOMAIN_NAME,
                "group_name": settings.SAMPLE_GROUP})

    assert response.status_code == 200
    content = response.json()

    async with async_session_maker() as session:
        query = select(Data.users_in_group)
        response = await session.execute(query)
        result = response.scalars().first()

        assert content == result


async def test_get_name_id_ivr(superuser_token) -> None:
    response = client.get(
        "api/v1/domain/get_name_id_ivr", 
        headers=superuser_token, 
        params={"domain": settings.SAMPLE_DOMAIN_NAME,
                "ivr_name": settings.SAMPLE_IVR_NAME})

    assert response.status_code == 200
    content = response.json()

    async with async_session_maker() as session:
        query = select(Data.names_id_ivr)
        response = await session.execute(query)
        result = response.scalars().first()

        assert content == result


async def test_get_events_and_params_ivr(superuser_token) -> None:
    response = client.get(
        "api/v1/domain/get_events_and_params_ivr", 
        headers=superuser_token, 
        params={"domain": settings.SAMPLE_DOMAIN_NAME,
                "name_menu": settings.SAMPLE_GROUP,
                "ivr_id": settings.SAMPLE_IVR_ID})

    assert response.status_code == 200
    content = response.json()

    async with async_session_maker() as session:
        query = select(Data.ivr_params_events)
        response = await session.execute(query)
        result = response.scalars().first()

        assert content == result
    

async def test_get_route_info(superuser_token) -> None:
    response = client.get(
        "api/v1/domain/get_route_info", 
        headers=superuser_token, 
        params={"domain": settings.SAMPLE_DOMAIN_NAME,
                "route_id": settings.SAMPLE_INNER_NUMBER})

    assert response.status_code == 200
    content = response.json()

    async with async_session_maker() as session:
        query = select(Data.route_info)
        response = await session.execute(query)
        result = response.scalars().first()

        assert content == result


async def test_get_route_settings(superuser_token) -> None:
    response = client.get(
        "api/v1/domain/get_route_settings", 
        headers=superuser_token, 
        params={"domain": settings.SAMPLE_DOMAIN_NAME,
                "name": settings.SAMPLE_GROUP})

    assert response.status_code == 200
    content = response.json()

    async with async_session_maker() as session:
        query = select(Data.route_settings)
        response = await session.execute(query)
        result = response.scalars().first()

        assert content == result
