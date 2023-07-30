from httpx import AsyncClient
from sqlalchemy import insert, select
from models.models import domain_data
from tests.conftest import async_session_maker, client
from settings import settings


