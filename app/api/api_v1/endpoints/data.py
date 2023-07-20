from fastapi import APIRouter
from database import db
from typing import List
from schemas.schemas import *


router = APIRouter()


@router.get("/get_main_info", response_model=List[DomainMainInfo])
async def get_main_info(domain: str) -> List[DomainMainInfo]:
    return [main_info for main_info in db.domain_main_info if main_info.get("domain_name") == domain]


@router.get("/get_active_users", response_model=List[DomainActiveUser])
async def get_active_users(domain: str) -> List[DomainActiveUser]:
    return [active for active in db.active_users if str(active.get("sip_uri")).split("@")[1] == domain]


@router.get("/get_incoming_line_info", response_model=List[DomainIncomingLine])
async def get_incoming_line_info(incoming_line: str) -> List[DomainIncomingLine]:
    return [line for line in db.info_numbers if line.get("params").get("incoming_line") == incoming_line]


@router.get("/get_user_info", response_model=List[DomainUserInfo])
async def get_user_info(username: str = None, login: str = None) -> List[DomainUserInfo]:
    return [user for user in db.info_user if user.get("username") == username or user.get("login") == login]


@router.get("/get_contacts_user", response_model=List[DomainContactsUser])
async def get_contacts_user(username: str = None, login: str = None) -> List[DomainContactsUser]:
    contacts = []
    for contact in db.contacts_user:
        for key, value in contact.items():
            if key == "contact_numbers_user":
                contacts.extend(value)
    return [cnt for cnt in contacts if cnt.get("username") == username or cnt.get("login") == login]


@router.get("/get_groups_user", response_model=List[DomainGroupsUser])
async def get_groups_user(username: str = None, login: str = None) -> List[DomainGroupsUser]:
    return [group for group in db.groups_user if group.get("username") == username or group.get("login") == login]


@router.get("/get_group_info", response_model=List[DomainGroupInfo])
async def get_groups_user(group_name: str = None, number: int = None) -> List[DomainGroupInfo]:
    return [grp for grp in db.group_info if grp.get("group_name") == group_name or grp.get("number") == number]


@router.get("/get_users_in_group", response_model=List[DomainUsersInGroup])
async def get_groups_user(group_name: str = None) -> List[DomainUsersInGroup]:
    return [usrg for usrg in db.users_in_group if usrg.get("group_name") == group_name]


@router.get("/get_name_id_ivr", response_model=List[DomainNamesIdIvr])
async def get_groups_user(ivr_name: str = None) -> List[DomainNamesIdIvr]:
    return [ivr for ivr in db.names_ivr if ivr.get("ivr_name") == ivr_name]


@router.get("/get_events_and_params_ivr", response_model=List[DomainIvrParamsEvents])
async def get_groups_user(name_menu: str = None, ivr_id: int = None) -> List[DomainIvrParamsEvents]:
    return [par for par in db.params_events_ivr if par.get("name_menu") == name_menu or par.get("ivr_id") == ivr_id]


@router.get("/get_route_info", response_model=List[DomainRouteInfo])
async def get_groups_user(route_id: int = None) -> List[DomainRouteInfo]:
    return [route for route in db.route_info if route.get("route_id") == route_id]


@router.get("/get_route_settings", response_model=List[DomainRouteSettings])
async def get_groups_user(name: str = None) -> List[DomainRouteSettings]:
    return [setting for setting in db.route_settings if setting.get("name") == name]

