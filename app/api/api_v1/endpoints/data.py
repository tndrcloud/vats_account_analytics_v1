from fastapi import APIRouter
from typing import List
from schemas.schemas import *
from models.models import domain_data
from fastapi import Depends, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy import select, insert, or_
from database.session import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter()


@router.post("/add_domain_data", response_model=DomainData)
async def add_domain_data(
    data: DomainData,
    session: AsyncSession = Depends(get_async_session)
    ) -> DomainData:
    try:
        json_data = jsonable_encoder(data)
        statement = insert(domain_data).values(
            name = data.main_info.domain_name,
            **json_data
            )
        await session.execute(statement)
        await session.commit()

        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content=jsonable_encoder({"detail": "successfully"})
        )
    
    except Exception:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=jsonable_encoder({"detail": "validation error"})
        )


@router.get("/get_main_info", response_model=DomainMainInfo)
async def get_main_info(
    domain: str,
    session: AsyncSession = Depends(get_async_session)
    ) -> DomainMainInfo:
    query = select(domain_data.c.main_info).where(domain_data.c.name == domain)
    request = await session.execute(query)
    response = request.mappings().all()

    if response:
        return response[0]["main_info"]
    return response


@router.get("/get_active_users", response_model=List[DomainActiveUser])
async def get_active_users(
    domain: str,
    session: AsyncSession = Depends(get_async_session)
    ) -> List[DomainActiveUser]:
    query = select(domain_data.c.active_users).where(domain_data.c.name == domain)
    request = await session.execute(query)
    response = request.mappings().all()

    if response:
        return response[0]["active_users"]
    return response
    

@router.get("/get_incoming_line_info", response_model=List[DomainIncomingLine])
async def get_incoming_line_info(
    domain: str,
    session: AsyncSession = Depends(get_async_session)
    ) -> List[DomainIncomingLine]:
    query = select(domain_data.c.incoming_line).where(domain_data.c.name == domain)
    request = await session.execute(query)
    response = request.mappings().all()

    if response:
        return response[0]["incoming_line"]
    return response


@router.get("/get_user_info", response_model=List[DomainUserInfo])
async def get_user_info(
    domain: str,
    username: str = None, 
    number: int = None,
    session: AsyncSession = Depends(get_async_session)
    ) -> List[DomainUserInfo]:
    query = select(domain_data.c.user_info).where(domain_data.c.name == domain)
    request = await session.execute(query)
    response = request.mappings().all()
    
    user_info = []
    if response:
        for info in response[0]["user_info"]:
            if info["username"] == username or info["inner_number"] == number:
                user_info.append(info)

    if user_info:
        return user_info
    elif not response:
        return response
    elif not username and not number: 
        return response[0]["user_info"]
    

@router.get("/get_contacts_user", response_model=List[DomainContactsUser])
async def get_contacts_user(
    domain: str,
    username: str = None, 
    login: str = None,
    session: AsyncSession = Depends(get_async_session)
    ) -> List[DomainContactsUser]:
    query = select(domain_data.c.contacts_user).where(domain_data.c.name == domain)
    request = await session.execute(query)
    response = request.mappings().all()

    user_contacts = []
    for contact in response[0]["contacts_user"]:
        if contact["username"] == username or contact["login"] == login:
            user_contacts.append(contact)

    if user_contacts:
        return user_contacts
    elif not username and not login: 
        return response[0]["contacts_user"]


@router.get("/get_groups_user")
async def get_groups_user(
    domain: str,
    username: str = None, 
    login: str = None,
    session: AsyncSession = Depends(get_async_session)
    ):
    query = select(domain_data.c.groups_user).where(domain_data.c.name == domain)
    result = await session.execute(query)
    return result.mappings().all()


@router.get("/get_group_info")
async def get_group_info(
    domain: str,
    group_name: str = None, 
    number: int = None,
    session: AsyncSession = Depends(get_async_session)
    ):
    query = select(domain_data.c.group_info).where(domain_data.c.name == domain)
    result = await session.execute(query)
    return result.mappings().all()


@router.get("/get_users_in_group")
async def get_users_in_group(
    domain: str,
    group_name: str = None,
    session: AsyncSession = Depends(get_async_session)
    ):
    query = select(domain_data.c.users_in_group).where(domain_data.c.name == domain)
    result = await session.execute(query)
    return result.mappings().all()


@router.get("/get_name_id_ivr")
async def get_name_id_ivr(
    domain: str,
    ivr_name: str = None,
    session: AsyncSession = Depends(get_async_session)
    ):
    query = select(domain_data.c.names_id_ivr).where(domain_data.c.name == domain)
    result = await session.execute(query)
    return result.mappings().all()


@router.get("/get_events_and_params_ivr")
async def get_events_and_params_ivr(
    domain: str,
    name_menu: str = None, 
    ivr_id: int = None,
    session: AsyncSession = Depends(get_async_session)
    ):
    query = select(domain_data.c.ivr_params_events).where(domain_data.c.name == domain)
    result = await session.execute(query)
    return result.mappings().all()


@router.get("/get_route_info")
async def get_route_info(
    domain: str,
    route_id: int = None,
    session: AsyncSession = Depends(get_async_session)
    ):
    query = select(domain_data.c.route_info).where(domain_data.c.name == domain)
    result = await session.execute(query)
    return result.mappings().all()


@router.get("/get_route_settings")
async def get_route_settings(
    domain: str,
    name: str = None,
    session: AsyncSession = Depends(get_async_session)
    ):
    query = select(domain_data.c.route_settings).where(domain_data.c.name == domain)
    result = await session.execute(query)
    return result.mappings().all()
