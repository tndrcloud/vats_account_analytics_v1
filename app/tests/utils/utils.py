from typing import Dict
from fastapi.testclient import TestClient
from settings import settings


def create_superuser(client: TestClient):
    response = client.post("api/auth/register", json={
        "email": settings.ROOT_LOGIN,
        "password": settings.ROOT_PASSWORD,
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "username": "string",
        "role_id": 1
        }
    )

    return response


def get_superuser_token(client: TestClient) -> Dict[str, str]:
    response = client.post("api/auth/login", data={
        "username": settings.ROOT_LOGIN,
        "password": settings.ROOT_PASSWORD,
        }
    )
    
    result = response.json()["access_token"]
    token = {"Authorization": f"Bearer {result}"}
    return token
