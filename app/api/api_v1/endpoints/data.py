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
    if response:
        for contact in response[0]["contacts_user"]:
            if contact["username"] == username or contact["login"] == login:
                user_contacts.append(contact)

    if user_contacts:
        return user_contacts
    elif not response:
        return response
    elif not username and not login: 
        return response[0]["contacts_user"]


@router.get("/get_groups_user", response_model=List[DomainGroupsUser])
async def get_groups_user(
    domain: str,
    username: str = None, 
    login: str = None,
    session: AsyncSession = Depends(get_async_session)
    ) -> List[DomainGroupsUser]:
    query = select(domain_data.c.groups_user).where(domain_data.c.name == domain)
    request = await session.execute(query)
    response = request.mappings().all()

    user_groups = []
    if response:
        for group_user in response[0]["groups_user"]:
            if group_user["username"] == username or group_user["login"] == login:
                user_groups.append(group_user)

    if user_groups:
        return user_groups
    elif not response:
        return response
    elif not username and not login:
        return response[0]["groups_user"]


@router.get("/get_group_info", response_model=List[DomainGroupInfo])
async def get_group_info(
    domain: str,
    group_name: str = None, 
    number: int = None,
    session: AsyncSession = Depends(get_async_session)
    ) -> List[DomainGroupInfo]:
    query = select(domain_data.c.group_info).where(domain_data.c.name == domain)
    request = await session.execute(query)
    response = request.mappings().all()

    group_info = []
    if response:
        for group in response[0]["group_info"]:
            if group["group_name"] == group_name or group["number"] == number:
                group_info.append(group)

    if group_info:
        return group_info
    elif not response:
        return response
    elif not group_name and not number:
        return response[0]["group_info"]


@router.get("/get_users_in_group", response_model=List[DomainUsersInGroup])
async def get_users_in_group(
    domain: str,
    group_name: str = None,
    session: AsyncSession = Depends(get_async_session)
    ) -> List[DomainUsersInGroup]:
    query = select(domain_data.c.users_in_group).where(domain_data.c.name == domain)
    request = await session.execute(query)
    response = request.mappings().all()

    users_in_group = []
    if response:
        for users in response[0]["users_in_group"]:
            if users["group_name"] == group_name:
                users_in_group.append(users)

    if users_in_group:
        return users_in_group 
    elif not response and not users_in_group:
        return response           
    elif not group_name or not response:
        return response[0]["users_in_group"]


@router.get("/get_name_id_ivr", response_model=List[DomainNamesIdIvr])
async def get_name_id_ivr(
    domain: str,
    ivr_name: str = None,
    session: AsyncSession = Depends(get_async_session)
    ) -> List[DomainNamesIdIvr]:
    query = select(domain_data.c.names_id_ivr).where(domain_data.c.name == domain)
    request = await session.execute(query)
    response = request.mappings().all()

    ivr_id = []
    if response:
        for ivr in response[0]["names_id_ivr"]:
            if ivr["ivr_name"] == ivr_name:
                ivr_id.append(ivr)
    
    if ivr_id:
        return ivr_id
    elif not response and not ivr_id:
        return response
    elif not ivr_name:
        return response[0]["names_id_ivr"]


@router.get("/get_events_and_params_ivr", response_model=List[DomainIvrParamsEvents])
async def get_events_and_params_ivr(
    domain: str,
    name_menu: str = None, 
    ivr_id: int = None,
    session: AsyncSession = Depends(get_async_session)
    ) -> List[DomainIvrParamsEvents]:
    query = select(domain_data.c.ivr_params_events).where(domain_data.c.name == domain)
    request = await session.execute(query)
    response =  request.mappings().all()

    events_params = []
    if response:
        for event in response[0]["ivr_params_events"]:
            if event["name_menu"] == name_menu or event["ivr_id"] == ivr_id:
                events_params.append(event)

    if events_params:
        return events_params
    elif not response:
        return response
    elif not name_menu and not ivr_id:
        return response[0]["ivr_params_events"]


@router.get("/get_route_info", response_model=List[DomainRouteInfo])
async def get_route_info(
    domain: str,
    route_id: int = None,
    session: AsyncSession = Depends(get_async_session)
    ) -> List[DomainRouteInfo]:
    query = select(domain_data.c.route_info).where(domain_data.c.name == domain)
    request = await session.execute(query)
    response = request.mappings().all()

    route_info = []
    if response:
        for route in response[0]["route_info"]:
            if route["route_id"] == route_id:
                route_info.append(route)
    
    if route_info:
        return route_info
    elif not response and not route_info:
        return response
    elif not route_id:
        return response[0]["route_info"]


@router.get("/get_route_settings")
async def get_route_settings(
    domain: str,
    name: str = None,
    session: AsyncSession = Depends(get_async_session)
    ):
    query = select(domain_data.c.route_settings).where(domain_data.c.name == domain)
    request = await session.execute(query)
    response = request.mappings().all()

    route_settings = []
    if response:
        for setting in response[0]["route_settings"]:
            if setting["name"] == name:
                route_settings.append(setting)

    if route_settings:
        return route_settings
    elif not response and not route_settings:
        return response
    elif not name:
        return response[0]["route_settings"]
    