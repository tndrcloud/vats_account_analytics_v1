from settings import settings


json_data={
    "main_info": {
        "domain_name": settings.DOMAIN_NAME,
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
        "login": settings.ROOT_LOGIN,
        "sip_uri": "string",
        "ip_address": "string",
        "expired": "string"
        }
    ],

    "incoming_line": [
        {
        "params": {
            "incoming_line": settings.SAMPLE_INCOMING_LINE,
            "sip_uri": "string",
            "sip_number": True,
            "only_incoming_calls": True
        },

        "routing_rules": [
            {
            "state": True,
            "prefix": settings.SAMPLE_PREFIX,
            "schedule": "string",
            "redirect_to": "string",
            "action": "string"
            }
        ],

        "filter_list": [
            settings.SAMPLE_FILTER_LIST
            ]
        }
    ],

    "user_info": [
        {
        "username": settings.ROOT_LOGIN,
        "inner_number": settings.SAMPLE_INNER_NUMBER,
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
        "username": settings.ROOT_LOGIN,
        "login": settings.ROOT_LOGIN,
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
        "username": settings.ROOT_LOGIN,
        "login": "string",
        "groups_list": [
            settings.SAMPLE_GROUPS_LIST
            ]
        }
    ],

    "group_info": [
        {
        "group_name": settings.SAMPLE_GROUPS_LIST[0],
        "number": settings.SAMPLE_INNER_NUMBER,
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
        "group_name": settings.SAMPLE_GROUPS_LIST[0],
        "users_list": [
            {
            "username": settings.ROOT_LOGIN,
            "priority": 0
                }
            ]
        }
    ],

    "names_id_ivr": [
        {
        "ivr_name": settings.SAMPLE_IVR_NAME,
        "ivr_id": settings.SAMPLE_IVR_ID
        }
    ],

    "ivr_params_events": [
        {
        "name_menu": settings.SAMPLE_GROUPS_LIST[0],
        "voice_file": "string",
        "ivr_id": settings.SAMPLE_IVR_ID,
        "events_and_actions": [
            {"event": 0, "action": "redirect_to_arb_number", "params": None},
            {"event": 1, "action": "redirect_to_menu", "params": "Тест НСК"},
            {"event": 2, "action": "disconnect", "params": None},
            {"event": 3, "action": "disconnect", "params": None},
            {"event": 4, "action": "redirect_to_arb_number", "params": "1001"},
            {"event": 5, "action": "default", "params": None},
            {"event": 6, "action": "default", "params": None},
            {"event": 7, "action": "disconnect", "params": None},
            {"event": 8, "action": "redirect_to_user", "params": "Яковлев П.Е."},
            {"event": 9, "action": "additional_inner_number_user", "params": None},
            {"event": "*", "action": "default", "params": None},
            {"event": "#", "action": "default", "params": None},
            {"event": "timeout", "action": "redirect_to_menu", "params": "Тест НСК"},
            {"event": "default", "action": "additional_inner_number_user", "params": None}
                ]
        }
    ],

    "route_info": [
        {
        "route_id": settings.SAMPLE_INNER_NUMBER,
        "status": True,
        "name": settings.SAMPLE_GROUPS_LIST[0],
        "private": True,
        "regular_exp_to": "string",
        "tgrp": "string",
        "outgoing_calls": "string"
        }
    ],

    "route_settings": [
        {
        "name": settings.SAMPLE_GROUPS_LIST[0],
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
