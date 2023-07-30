from typing import Dict
from fastapi.testclient import TestClient
from settings import settings


def get_user_token(client: TestClient) -> Dict[str, str]:
    response = client.post("api/auth/login", data={
        "username": settings.USER_LOGIN,
        "password": settings.USER_PASSWORD,
        }
    )
    
    result = response.json()["access_token"]
    token = {"Authorization": f"Bearer {result}"}
    return token
