from sqlalchemy import insert, select
from models.models import domain_data
from tests.conftest import async_session_maker, client
from tests.api.api_v1.json_data import json_data
from settings import settings


async def test_add_domain_data(superuser_token):
    response = client.post(
        "api/v1/domain/add_domain_data", 
        headers=superuser_token,
        json=json_data 
    )
    assert response.status_code == 201

    async with async_session_maker() as session:
        query = select(domain_data.c.main_info)
        response = await session.execute(query)
        result = response.first()
    
        assert result[0]["domain_name"] == settings.SAMPLE_DOMAIN_NAME
        assert result[0]["email"] == settings.ROOT_LOGIN


async def test_get_main_info(superuser_token):
    response = client.get(
        "api/v1/domain/get_main_info", 
        headers=superuser_token, 
        params={"domain": settings.SAMPLE_DOMAIN_NAME})

    assert response.status_code == 200
    content = response.json()

    async with async_session_maker() as session:
        query = select(domain_data.c.main_info)
        response = await session.execute(query)
        result = response.first()

        assert content["domain_name"] == settings.SAMPLE_DOMAIN_NAME
        assert result[0]["domain_name"] == settings.SAMPLE_DOMAIN_NAME


async def test_get_active_users(superuser_token):
    response = client.get(
        "api/v1/domain/get_active_users", 
        headers=superuser_token, 
        params={"domain": settings.SAMPLE_DOMAIN_NAME})

    assert response.status_code == 200
    content = response.json()

    async with async_session_maker() as session:
        query = select(domain_data.c.active_users)
        response = await session.execute(query)
        result = response.first()

        assert content[0]["login"] == settings.ROOT_LOGIN
        assert result[0][0]["login"] == settings.ROOT_LOGIN


async def test_get_incoming_line_info(superuser_token):
    response = client.get(
        "api/v1/domain/get_incoming_line_info", 
        headers=superuser_token, 
        params={"domain": settings.SAMPLE_DOMAIN_NAME})

    assert response.status_code == 200
    content = response.json()

    async with async_session_maker() as session:
        query = select(domain_data.c.incoming_line)
        response = await session.execute(query)
        result = response.first()
        
        assert content[0]["params"]["incoming_line"] == settings.SAMPLE_INCOMING_LINE
        assert result[0][0]["params"]["incoming_line"] == settings.SAMPLE_INCOMING_LINE


async def test_get_user_info(superuser_token):
    response = client.get(
        "api/v1/domain/get_user_info", 
        headers=superuser_token, 
        params={"domain": settings.SAMPLE_DOMAIN_NAME,
                "username": settings.ROOT_LOGIN,
                "number": settings.SAMPLE_INNER_NUMBER})

    assert response.status_code == 200
    content = response.json()

    async with async_session_maker() as session:
        query = select(domain_data.c.user_info)
        response = await session.execute(query)
        result = response.first()
        
        assert content[0]["username"] == settings.ROOT_LOGIN
        assert content[0]["inner_number"] == settings.SAMPLE_INNER_NUMBER
        assert result[0][0]["username"] == settings.ROOT_LOGIN
        assert result[0][0]["inner_number"] == settings.SAMPLE_INNER_NUMBER


async def test_get_contacts_user(superuser_token):
    response = client.get(
        "api/v1/domain/get_contacts_user", 
        headers=superuser_token, 
        params={"domain": settings.SAMPLE_DOMAIN_NAME,
                "username": settings.ROOT_LOGIN,
                "login": settings.ROOT_LOGIN})

    assert response.status_code == 200
    content = response.json()

    async with async_session_maker() as session:
        query = select(domain_data.c.contacts_user)
        response = await session.execute(query)
        result = response.first()
        
        assert content[0]["username"] == settings.ROOT_LOGIN
        assert content[0]["login"] == settings.ROOT_LOGIN
        assert result[0][0]["username"] == settings.ROOT_LOGIN
        assert result[0][0]["login"] == settings.ROOT_LOGIN


async def test_get_groups_user(superuser_token):
    response = client.get(
        "api/v1/domain/get_groups_user", 
        headers=superuser_token, 
        params={"domain": settings.SAMPLE_DOMAIN_NAME,
                "username": settings.ROOT_LOGIN,
                "login": settings.ROOT_LOGIN})

    assert response.status_code == 200
    content = response.json()

    async with async_session_maker() as session:
        query = select(domain_data.c.groups_user)
        response = await session.execute(query)
        result = response.first()

        assert content[0]["username"] == settings.ROOT_LOGIN
        assert result[0][0]["username"] == settings.ROOT_LOGIN
        assert result[0][0]["groups_list"][0] == settings.SAMPLE_GROUP


async def test_get_group_info(superuser_token):
    response = client.get(
        "api/v1/domain/get_group_info", 
        headers=superuser_token, 
        params={"domain": settings.SAMPLE_DOMAIN_NAME,
                "group_name": settings.SAMPLE_GROUP,
                "number": settings.SAMPLE_INNER_NUMBER})

    assert response.status_code == 200
    content = response.json()

    async with async_session_maker() as session:
        query = select(domain_data.c.group_info)
        response = await session.execute(query)
        result = response.first()

        assert content[0]["group_name"] == settings.SAMPLE_GROUP
        assert content[0]["number"] == settings.SAMPLE_INNER_NUMBER
        assert result[0][0]["group_name"] == settings.SAMPLE_GROUP
        assert result[0][0]["number"] == settings.SAMPLE_INNER_NUMBER


async def test_get_users_in_group(superuser_token):
    response = client.get(
        "api/v1/domain/get_users_in_group", 
        headers=superuser_token, 
        params={"domain": settings.SAMPLE_DOMAIN_NAME,
                "group_name": settings.SAMPLE_GROUP})

    assert response.status_code == 200
    content = response.json()

    async with async_session_maker() as session:
        query = select(domain_data.c.users_in_group)
        response = await session.execute(query)
        result = response.first()

        assert content[0]["group_name"] == settings.SAMPLE_GROUP
        assert content[0]["users_list"][0]["username"] == settings.ROOT_LOGIN
        assert result[0][0]["group_name"] == settings.SAMPLE_GROUP
        assert result[0][0]["users_list"][0]["username"] == settings.ROOT_LOGIN


async def test_get_name_id_ivr(superuser_token):
    response = client.get(
        "api/v1/domain/get_name_id_ivr", 
        headers=superuser_token, 
        params={"domain": settings.SAMPLE_DOMAIN_NAME,
                "ivr_name": settings.SAMPLE_IVR_NAME})

    assert response.status_code == 200
    content = response.json()

    async with async_session_maker() as session:
        query = select(domain_data.c.names_id_ivr)
        response = await session.execute(query)
        result = response.first()

        assert content[0]["ivr_name"] == settings.SAMPLE_IVR_NAME
        assert content[0]["ivr_id"] == settings.SAMPLE_IVR_ID
        assert result[0][0]["ivr_name"] == settings.SAMPLE_IVR_NAME
        assert result[0][0]["ivr_id"] == settings.SAMPLE_IVR_ID


async def test_get_events_and_params_ivr(superuser_token):
    response = client.get(
        "api/v1/domain/get_events_and_params_ivr", 
        headers=superuser_token, 
        params={"domain": settings.SAMPLE_DOMAIN_NAME,
                "name_menu": settings.SAMPLE_GROUP,
                "ivr_id": settings.SAMPLE_IVR_ID})

    assert response.status_code == 200
    content = response.json()

    async with async_session_maker() as session:
        query = select(domain_data.c.ivr_params_events)
        response = await session.execute(query)
        result = response.first()

        assert content[0]["name_menu"] == settings.SAMPLE_GROUP
        assert content[0]["ivr_id"] == settings.SAMPLE_IVR_ID
        assert result[0][0]["name_menu"] == settings.SAMPLE_GROUP
        assert result[0][0]["ivr_id"] == settings.SAMPLE_IVR_ID
    


async def test_get_route_info(superuser_token):
    response = client.get(
        "api/v1/domain/get_route_info", 
        headers=superuser_token, 
        params={"domain": settings.SAMPLE_DOMAIN_NAME,
                "route_id": settings.SAMPLE_INNER_NUMBER})

    assert response.status_code == 200
    content = response.json()

    async with async_session_maker() as session:
        query = select(domain_data.c.route_info)
        response = await session.execute(query)
        result = response.first()

        assert content[0]["route_id"] == settings.SAMPLE_INNER_NUMBER
        assert content[0]["name"] == settings.SAMPLE_GROUP
        assert result[0][0]["route_id"] == settings.SAMPLE_INNER_NUMBER
        assert result[0][0]["name"] == settings.SAMPLE_GROUP


async def test_get_route_settings(superuser_token):
    response = client.get(
        "api/v1/domain/get_route_settings", 
        headers=superuser_token, 
        params={"domain": settings.SAMPLE_DOMAIN_NAME,
                "name": settings.SAMPLE_GROUP})

    assert response.status_code == 200
    content = response.json()

    async with async_session_maker() as session:
        query = select(domain_data.c.route_settings)
        response = await session.execute(query)
        result = response.first()

        assert content[0]["name"] == settings.SAMPLE_GROUP
        assert result[0][0]["name"] == settings.SAMPLE_GROUP
