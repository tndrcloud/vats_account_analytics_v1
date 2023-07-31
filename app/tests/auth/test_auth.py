from tests.conftest import client
from settings import settings


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


def test_login():
    response = client.post("api/auth/login", data={
        "username": settings.USER_LOGIN,
        "password": settings.USER_PASSWORD,
        }
    )

    result = response.json()

    assert response.status_code == 200
    assert "access_token" in result
    assert result["access_token"]
