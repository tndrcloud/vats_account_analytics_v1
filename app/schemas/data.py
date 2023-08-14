from enum import Enum
from pydantic import BaseModel, Field
from typing import List, Optional, Union


class DomainMainInfo(BaseModel):
    domain_name: str
    ls_number: int = Field(ge=0)
    ls: int | None
    location: str
    users_operators_count: str
    domain_owner: str
    company_name: str
    max_count_users: int = Field(ge=0)
    max_count_operators: int = Field(ge=0)
    call_redirect: str | None
    fax_redirect: str | None
    connect_conference: str | None
    disconnect_conference: str | None
    call_hold: str | None
    call_interception: str
    email: str
    limit_balance: int
    input_error_count: int
    timeout: int
    direction_restriction_calls: str | None
    b_number_conversion_template: str
    incoming_line: str
    timezone: str
    notify_balance_reduction: bool
    new_routing: bool
    allow_transcoding_audio_streams: bool
    balance: str
    vol_block: bool
    adm_block: bool
    fin_block: bool
    rate: str


    class Config:
        from_attributes = True


class DomainActiveUser(BaseModel):
    username: str
    login: str
    sip_uri: str
    ip_address: str
    expired: str


    class Config:
        from_attributes = True


class ParamsIncomingLine(BaseModel):
    incoming_line: str
    sip_uri: str
    sip_number: bool
    only_incoming_calls: bool


    class Config:
        from_attributes = True


class RoutingRuleIncomingLine(BaseModel):
    state: bool
    prefix: str
    schedule: str | None
    redirect_to: str
    action: str


    class Config:
        from_attributes = True


class DomainIncomingLine(BaseModel):
    params: ParamsIncomingLine
    routing_rules: List[RoutingRuleIncomingLine]
    filter_list: List[str]


    class Config:
        from_attributes = True


class DomainUserInfo(BaseModel):
    username: str
    inner_number: int = Field(ge=0)
    email: str | None
    login: str
    is_supervisor: bool
    visibility_other_group: bool
    prohibition_internal_number: bool
    voicemail_on: bool
    notice_missing_calls: Optional[bool] = False
    call_direction_restrictions: str
    redirect_to_user: str
    group_for_outgoing_calls: Optional[str] = None
    number_for_outgoing_calls: str | None
    variables_send_to_email: Optional[str] = None
    greeting: str | None
    music_instead_beeps: str | None
    greeting_voicemail: str | None
    dial_up_cycles: int = Field(ge=0)
    block: bool
    is_operator: bool
    conversation_is_recording: bool


    class Config:
        from_attributes = True


class ContactType(Enum):
    mobile = "Мобильный"
    ip_phone = "IP-телефон"
    home = "Домашний"
    work = "Рабочий"
    other = "Другой"


class DomainContactsUser(BaseModel):
    username: str
    login: str
    is_on: bool
    do_not_display_other: bool
    number: str
    fmc: bool | None
    priority: int = Field(ge=0)
    dial_up_time: int = Field(ge=0)
    contact_type: ContactType
    filter_list: str | None
    working_time: str | None


    class Config:
        from_attributes = True


class DomainGroupsUser(BaseModel):
    username: str
    login: str
    groups_list: List[str] | None


    class Config:
        from_attributes = True


class DomainGroupInfo(BaseModel):
    group_name: str
    number: int = Field(ge=0)
    email: str | None
    interception_call: bool
    skip_greeting: bool
    prohibition_dialing_number: bool
    voicemail_is_on: bool
    distribution_alg: str | None
    voice_greeting: str | None
    voicemail_greeting: str | None


    class Config:
        from_attributes = True


class UsersInGroup(BaseModel):
    username: str
    priority: int = Field(ge=0)


    class Config:
        from_attributes = True


class DomainUsersInGroup(BaseModel):
    group_name: str
    users_list: List[UsersInGroup]


    class Config:
        from_attributes = True


class DomainNamesIdIvr(BaseModel):
    ivr_name: str
    ivr_id: int = Field(ge=0)

    class Config:
        from_attributes = True


class ActionsIvr(Enum):
    default = "default"
    redirect_to_group = "redirect_to_group"
    redirect_to_user = "redirect_to_user"
    redirect_to_menu = "redirect_to_menu"
    redirect_to_arb_number = "redirect_to_arb_number"
    return_to_prev_menu = "return_to_prev_menu"
    redirect_to_voicemail_group = "redirect_to_voicemail_group"
    pronounce_phrase = "pronounce_phrase"
    disconnect = "disconnect"
    repeat_menu = "repeat_menu"
    additional_inner_number_user = "additional_inner_number_user"
    redirect_to_voicemail_user = "redirect_to_voicemail_user"
    redirect_to_fax_group = "redirect_to_fax_group"
    redirect_to_fax_user = "redirect_to_fax_user"
    call_in_route_with_additional = "call_in_route_with_additional"
    return_to_queue = "return_to_queue"


class EventAndActionZero(BaseModel):
    event: int = 0
    action: ActionsIvr
    params: str | None


    class Config:
        from_attributes = True


class EventAndActionOne(BaseModel):
    event: int = 1
    action: ActionsIvr
    params: str | None
 

    class Config:
        from_attributes = True


class EventAndActionTwo(BaseModel):
    event: int = 2
    action: ActionsIvr
    params: str | None


    class Config:
        from_attributes = True


class EventAndActionThree(BaseModel):
    event: int = 3
    action: ActionsIvr
    params: str | None


    class Config:
        from_attributes = True


class EventAndActionFour(BaseModel):
    event: int = 4
    action: ActionsIvr
    params: str | None


    class Config:
        from_attributes = True


class EventAndActionFive(BaseModel):
    event: int = 5
    action: ActionsIvr
    params: str | None


    class Config:
        from_attributes = True


class EventAndActionSix(BaseModel):
    event: int = 6
    action: ActionsIvr
    params: str | None


    class Config:
        from_attributes = True


class EventAndActionSeven(BaseModel):
    event: int = 7
    action: ActionsIvr
    params: str | None


    class Config:
        from_attributes = True


class EventAndActionEight(BaseModel):
    event: int = 8
    action: ActionsIvr
    params: str | None


    class Config:
        from_attributes = True


class EventAndActionNine(BaseModel):
    event: int = 9
    action: ActionsIvr
    params: str | None


    class Config:
        from_attributes = True


class EventAndActionStar(BaseModel):
    event: str = "*"
    action: ActionsIvr
    params: str | None


    class Config:
        from_attributes = True


class EventAndActionHash(BaseModel):
    event: str = "#"
    action: ActionsIvr
    params: str | None


    class Config:
        from_attributes = True


class EventAndActionTimeout(BaseModel):
    event: str = "timeout"
    action: ActionsIvr
    params: str | None


    class Config:
        from_attributes = True


class EventAndActionDefault(BaseModel):
    event: str = "default"
    action: ActionsIvr
    params: str | None


    class Config:
        from_attributes = True


class DomainIvrParamsEvents(BaseModel):
    name_menu: str
    voice_file: str | None
    ivr_id: int = Field(ge=0)
    events_and_actions: List[Union[
        EventAndActionZero,
        EventAndActionOne,
        EventAndActionTwo,
        EventAndActionThree,
        EventAndActionFour,
        EventAndActionFive,
        EventAndActionSix,
        EventAndActionSeven,
        EventAndActionEight,
        EventAndActionNine,
        EventAndActionStar,
        EventAndActionHash,
        EventAndActionTimeout,
        EventAndActionDefault]]
    

    class Config:
        from_attributes = True


class DomainRouteInfo(BaseModel):
    route_id: int = Field(ge=0)
    status: bool
    name: str
    private: bool
    regular_exp_to: str
    tgrp: str
    outgoing_calls: str


    class Config:
        from_attributes = True


class Transport(Enum):
    tcp = "TCP"
    udp = "UDP"


class TypeRoute(Enum):
    line = "По линиям"
    number = "По номерам"


class TypeHeaderRedirect(Enum):
    not_used = "Не использовать"
    diversion = "Diversion или History-Info"
    remote_id = "Remote-Party-ID"
    identify = "P-Asserted-Identify"


class DomainRouteSettings(BaseModel):
    name: str
    authorization_name: str | None
    digest_username: str | None
    update_period: int = Field(ge=0)
    nat_ping_period: int = Field(ge=0)
    assigned_ip: str | None
    tgrp: str
    exp_for_callee_number: str
    exp_for_caller_number: str
    added_to_begin_str: str | None
    default_uri_for_caller_domain: str | None
    private: bool
    is_on: bool
    convert_to_e164: bool
    allow_sub_number_from: bool
    allow_accept_calls_to_unique_username: bool
    activation: str | None
    authorization_type_calls: str
    transport: Transport
    type_route_choice: TypeRoute
    only_for_groups: str | None
    number_sub_for_domain_caller: str
    type_header_allow_auth: str | None
    type_header_history_redirect: TypeHeaderRedirect
    limit_directions_transit_calls_SSOP: str | None
    count_digits_cutter_in_begin_number: int = Field(ge=0)
    max_count_renewals_registration: int = Field(ge=0)
    ip_address: str
    destination_domain_or_sip_proxy: str


    class Config:
        from_attributes = True


class DomainDataSchema(BaseModel):
    main_info: DomainMainInfo
    active_users: List[DomainActiveUser]
    incoming_line: List[DomainIncomingLine]
    user_info: List[DomainUserInfo]
    contacts_user: List[DomainContactsUser]
    groups_user: List[DomainGroupsUser]
    group_info: List[DomainGroupInfo]
    users_in_group: List[DomainUsersInGroup]
    names_id_ivr: List[DomainNamesIdIvr]
    ivr_params_events: List[DomainIvrParamsEvents]
    route_info: List[DomainRouteInfo]
    route_settings: List[DomainRouteSettings]

    
    class Config:
        from_attributes = True
        