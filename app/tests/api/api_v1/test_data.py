from sqlalchemy import insert, select
from models.models import domain_data
from tests.conftest import async_session_maker, client
from settings import settings


async def test_add_domain_data(superuser_token):
    response = client.post("api/v1/domain/add_domain_data", headers=superuser_token, json={
        "main_info": {
            "domain_name": "string",
            "ls_number": 0,
            "ls": 0,
            "location": "string",
            "users_operators_count": "string",
            "domain_owner": "string",
            "company_name": "string",
            "max_count_users": 0,
            "max_count_operators": 0,
            "call_redirect": "string",
            "fax_redirect": "string",
            "connect_conference": "string",
            "disconnect_conference": "string",
            "call_hold": "string",
            "call_interception": "string",
            "email": settings.ROOT_LOGIN,
            "limit_balance": 0,
            "input_error_count": 0,
            "timeout": 0,
            "direction_restriction_calls": "string",
            "b_number_conversion_template": "string",
            "incoming_line": "string",
            "timezone": "string",
            "notify_balance_reduction": True,
            "new_routing": True,
            "allow_transcoding_audio_streams": True,
            "balance": "string",
            "vol_block": True,
            "adm_block": True,
            "fin_block": True,
            "rate": "string"
            },

        "active_users": [
            {
            "username": "string",
            "login": "string",
            "sip_uri": "string",
            "ip_address": "string",
            "expired": "string"
            }
        ],

        "incoming_line": [
            {
            "params": {
                "incoming_line": "string",
                "sip_uri": "string",
                "sip_number": True,
                "only_incoming_calls": True
            },

            "routing_rules": [
                {
                "state": True,
                "prefix": "string",
                "schedule": "string",
                "redirect_to": "string",
                "action": "string"
                }
            ],

            "filter_list": [
                "string"
                ]
            }
        ],

        "user_info": [
            {
            "username": "string",
            "inner_number": 0,
            "email": "string",
            "login": "string",
            "is_supervisor": True,
            "visibility_other_group": True,
            "prohibition_internal_number": True,
            "voicemail_on": True,
            "notice_missing_calls": False,
            "call_direction_restrictions": "string",
            "redirect_to_user": "string",
            "group_for_outgoing_calls": "string",
            "number_for_outgoing_calls": "string",
            "variables_send_to_email": "string",
            "greeting": "string",
            "music_instead_beeps": "string",
            "greeting_voicemail": "string",
            "dial_up_cycles": 0,
            "block": True,
            "is_operator": True,
            "conversation_is_recording": True
            }
        ],

        "contacts_user": [
            {
            "username": "string",
            "login": "string",
            "is_on": True,
            "do_not_display_other": True,
            "number": "string",
            "fmc": True,
            "priority": 0,
            "dial_up_time": 0,
            "contact_type": "Мобильный",
            "filter_list": "string",
            "working_time": "string"
            }
        ],

        "groups_user": [
            {
            "username": "string",
            "login": "string",
            "groups_list": [
                "string"
                ]
            }
        ],

        "group_info": [
            {
            "group_name": "string",
            "number": 0,
            "email": "string",
            "interception_call": True,
            "skip_greeting": True,
            "prohibition_dialing_number": True,
            "voicemail_is_on": True,
            "distribution_alg": "string",
            "voice_greeting": "string",
            "voicemail_greeting": "string"
            }
        ],

        "users_in_group": [
            {
            "group_name": "string",
            "users_list": [
                {
                "username": "string",
                "priority": 0
                    }
                ]
            }
        ],

        "names_id_ivr": [
            {
            "ivr_name": "string",
            "ivr_id": 0
            }
        ],

        "ivr_params_events": [
            {
            "name_menu": "string",
            "voice_file": "string",
            "ivr_id": 0,
            "events_and_actions": [
                {
                "event": 0,
                "action": "default",
                "params": "string"
                    }
                ]
            }
        ],

        "route_info": [
            {
            "route_id": 0,
            "status": True,
            "name": "string",
            "private": True,
            "regular_exp_to": "string",
            "tgrp": "string",
            "outgoing_calls": "string"
            }
        ],

        "route_settings": [
            {
            "name": "string",
            "authorization_name": "string",
            "digest_username": "string",
            "update_period": 0,
            "nat_ping_period": 0,
            "assigned_ip": "string",
            "tgrp": "string",
            "exp_for_callee_number": "string",
            "exp_for_caller_number": "string",
            "added_to_begin_str": "string",
            "default_uri_for_caller_domain": "string",
            "private": True,
            "is_on": True,
            "convert_to_e164": True,
            "allow_sub_number_from": True,
            "allow_accept_calls_to_unique_username": True,
            "activation": "string",
            "authorization_type_calls": "string",
            "transport": "TCP",
            "type_route_choice": "По линиям",
            "only_for_groups": "string",
            "number_sub_for_domain_caller": "string",
            "type_header_allow_auth": "string",
            "type_header_history_redirect": "Не использовать",
            "limit_directions_transit_calls_SSOP": "string",
            "count_digits_cutter_in_begin_number": 0,
            "max_count_renewals_registration": 0,
            "ip_address": "string",
            "destination_domain_or_sip_proxy": "string"
                }
            ]
        }
    )
    assert response.status_code == 201

    async with async_session_maker() as session:
        query = select(domain_data)
        response = await session.execute(query)
        result = response.mappings().all()

        assert result[0]["main_info"]["email"] == settings.ROOT_LOGIN


async def test_get_main_info(superuser_token):
    response = client.get("api/v1/domain/get_main_info", headers=superuser_token, params={"domain": "string"})
    assert response.status_code == 200

