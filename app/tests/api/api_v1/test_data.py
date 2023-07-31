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
        query = select(domain_data)
        response = await session.execute(query)
        result = response.mappings().all()

        assert result[0]["main_info"]["email"] == settings.ROOT_LOGIN


async def test_get_main_info(superuser_token):
    response = client.get(
        "api/v1/domain/get_main_info", 
        headers=superuser_token, 
        params={"domain": settings.DOMAIN_NAME})

    assert response.status_code == 200


async def test_get_active_users(superuser_token):
    response = client.get(
        "api/v1/domain/get_active_users", 
        headers=superuser_token, 
        params={"domain": settings.DOMAIN_NAME})

    assert response.status_code == 200


async def test_get_incoming_line_info(superuser_token):
    response = client.get(
        "api/v1/domain/get_incoming_line_info", 
        headers=superuser_token, 
        params={"domain": settings.DOMAIN_NAME})

    assert response.status_code == 200


async def test_get_user_info(superuser_token):
    response = client.get(
        "api/v1/domain/get_user_info", 
        headers=superuser_token, 
        params={"domain": settings.DOMAIN_NAME})

    assert response.status_code == 200


async def test_get_contacts_user(superuser_token):
    response = client.get(
        "api/v1/domain/get_contacts_user", 
        headers=superuser_token, 
        params={"domain": settings.DOMAIN_NAME})

    assert response.status_code == 200


async def test_get_groups_user(superuser_token):
    response = client.get(
        "api/v1/domain/get_groups_user", 
        headers=superuser_token, 
        params={"domain": settings.DOMAIN_NAME})

    assert response.status_code == 200


async def test_get_group_info(superuser_token):
    response = client.get(
        "api/v1/domain/get_group_info", 
        headers=superuser_token, 
        params={"domain": settings.DOMAIN_NAME})

    assert response.status_code == 200


async def test_get_users_in_group(superuser_token):
    response = client.get(
        "api/v1/domain/get_users_in_group", 
        headers=superuser_token, 
        params={"domain": settings.DOMAIN_NAME})

    assert response.status_code == 200


async def test_get_name_id_ivr(superuser_token):
    response = client.get(
        "api/v1/domain/get_name_id_ivr", 
        headers=superuser_token, 
        params={"domain": settings.DOMAIN_NAME})

    assert response.status_code == 200


async def test_get_events_and_params_ivr(superuser_token):
    response = client.get(
        "api/v1/domain/get_events_and_params_ivr", 
        headers=superuser_token, 
        params={"domain": settings.DOMAIN_NAME})

    assert response.status_code == 200


async def test_get_route_info(superuser_token):
    response = client.get(
        "api/v1/domain/get_route_info", 
        headers=superuser_token, 
        params={"domain": settings.DOMAIN_NAME})

    assert response.status_code == 200


async def test_get_route_settings(superuser_token):
    response = client.get(
        "api/v1/domain/get_route_settings", 
        headers=superuser_token, 
        params={"domain": settings.DOMAIN_NAME})

    assert response.status_code == 200
