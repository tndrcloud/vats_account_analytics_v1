users = [
    {"id": 1,
     "role": "root",
     "login": "Aleksandr Bardusov",
     "password_hash": "5RTXnCsX8Xr9I1kfTfbc"},

    {"id": 2,
     "role": "admin",
     "login": "Yuriy Evsyukov",
     "password_hash": "5RTXnCsX8Xr9I1kfTfbc"},

    {"id": 3,
     "role": "user",
     "login": "Aleksandr Krysanov",
     "password_hash": "5RTXnCsX8Xr9I1kfTfbc"}
]

domain_main_info = [
    {"domain_name": "S001.14.rt.ru",
     "ls_number": 841,
     "ls": None,
     "location": "Москва",
     "users_operators_count": "231/2",
     "domain_owner": "ЛЦК Тулы ДЭФИР",
     "company_name": "Ростелеком",
     "max_count_users": 260,
     "max_count_operators": 54,
     "call_redirect": "#1#",
     "fax_redirect": "#2#",
     "connect_conference": "#3#",
     "disconnect_conference": "#4#",
     "call_hold": "#0#",
     "call_interception": "77",
     "email": "Konstantin_Udachin@center.rt.ru",
     "limit_balance": 10000,
     "input_error_count": 3,
     "timeout": 15,
     "direction_restriction_calls": None,
     "b_number_conversion_template": "Москва и Область (Центр)",
     "incoming_line": "74952491146",
     "timezone": "(UTC + 3:00) Moscow, Saint Petersburg, Minsk, Baghdad, Riyadh",
     "notify_balance_reduction": True,
     "new_routing": True,
     "allow_transcoding_audio_streams": False,
     "balance": -7365.48,
     "vol_block": False,
     "adm_block": False,
     "fin_block": False,
     "rate": "msk_Пакет_1000_МОНО_19_Москва-Ю (5823)"}
]

active_users = [
     {"username": "Осенний Антон",
      "login": "a.osenniy",
      "sip_uri": "sip:a.osenniy@S001.14.rt.ru",
      "ip_address": "10.243.208.20:5060",
      "expired": "2022-04-01 11:47:50"},

      {"username": "Александр Лаппо 2",
       "login": "alexl2",
       "sip_uri": "sip:alexl2@S001.14.rt.ru",
       "ip_address": "10.243.208.20:5060",
       "expired": "2022-04-01 11:53:10"},

      {"username": "Андросов Евгений",
       "login": "androsov",
       "sip_uri": "sip:androsov@S001.15.rt.ru",
       "ip_address": "10.243.208.20:5060",
       "expired": "2022-04-01 11:43:33"},

      {"username": "Осенний Антон гарнитура",
       "login": "anton",
       "sip_uri": "sip:anton@S001.14.rt.ru",
       "ip_address": "10.243.208.20:5060",
       "expired": "2022-04-01 11:49:57"},

      {"username": "Артем Бреховских",
       "login": "artem",
       "sip_uri": "sip:artem@S001.16.rt.ru",
       "ip_address": "10.243.208.20:5060",
       "expired": "2022-04-01 11:44:37"}
]

info_numbers = [
    {
     "params": {
         "incoming_line": "74955874149",
         "sip_uri": "sip:74955874149@10.243.214.36",
         "sip_number": False,
         "only_incoming_calls": False},

     "routing_rules": [
         {"state": True,
          "prefix": ".*",
          "schedule": None,
          "redirect_to": "Факс пользователя",
          "action": "Вадим Яценко"},

         {"state": False,
          "prefix": ".*",
          "schedule": "schedule_43",
          "redirect_to": "IVR-сценарий",
          "action": "ягуар 1"},

         {"state": False,
          "prefix": ".*",
          "schedule": "schedule_44",
          "redirect_to": "IVR-сценарий",
          "action": "ягуар 2"},

         {"state": False,
          "prefix": "^(74872408167|4872408167|84872408167|84955874143|74955874143|"
                      "79622725823|79207990870|79175159857|79175159859|79175156289|"
                      "+79175156289|79066287875)",
          "schedule": "schedule_15",
          "redirect_to": "Пользователя",
          "action": "Гуня Зойпер"},

         {"state": False,
          "prefix": ".*",
          "schedule": None,
          "redirect_to": "Пользователя",
          "action": "Вадим Яценко"},

         {"state": False,
          "prefix": "^(495)",
          "schedule": None,
          "redirect_to": "Завершение",
          "action": "0"},

         {"state": False,
          "prefix": ".*",
          "schedule": None,
          "redirect_to": "Завершение",
          "action": "0"},

         {"state": False,
          "prefix": ".*",
          "schedule": None,
          "redirect_to": "Пользователя",
          "action": "Гуня Ярослав gunya.mob"},

         {"state": False,
          "prefix": ".*",
          "schedule": None,
          "redirect_to": "Пользователя",
          "action": "av"}
     ],

     "filter_list": [
         "Cписок фильтрации для входящей линии 74955874149",
         "Включён ЧС",
         "84995039327"
        ]
    },

    {
     "params": {
         "incoming_line": "74996734415",
         "sip_uri": "sip:74996734415@10.243.214.36",
         "sip_number": False,
         "only_incoming_calls": False},

     "routing_rules": [
          {"state": True,
           "prefix": "^(79622725823)",
           "schedule": None,
           "redirect_to": "Пользователя",
           "action": "Гуня ФПБХ2"},

          {"state": True,
           "prefix": ".*",
           "schedule": None,
           "redirect_to": "Пользователя",
           "action": "Горелов Кирилл"}
     ],

     "filter_list": [
         "Cписок фильтрации для входящей линии 74996734415",
         "Включён ЧС",
         "4995039327"
        ]
    }
]

info_user = [
    {"username": "Chursina_SV",
     "inner_number": 74181,
     "email": None,
     "login": "test1",
     "is_supervisor": True,
     "visibility_other_group": True,
     "prohibition_internal_number": False,
     "voicemail_on": True,
     "call_direction_restrictions": "<По умолчанию>",
     "redirect_to_user": "<По умолчанию>",
     "group_for_outgoing_calls": None,
     "number_for_outgoing_calls": "74951222037",
     "greeting": None,
     "music_instead_beeps": "ringout.wav",
     "greeting_voicemail": "voicemail.wav",
     "dial_up_cycles": 1,
     "block": False,
     "is_operator": False,
     "conversation_is_recording": True},

    {"username": "katana",
     "inner_number": 601,
     "email": "elenakatana@mail.ru",
     "login": "katana4",
     "is_supervisor": True,
     "visibility_other_group": True,
     "prohibition_internal_number": False,
     "voicemail_on": False,
     "notice_missing_calls": False,
     "call_direction_restrictions": "<По умолчанию>",
     "redirect_to_user": "<По умолчанию>",
     "group_for_outgoing_calls": None,
     "number_for_outgoing_calls": "74951222037",
     "variables_send_to_email": "Ссылкой",
     "greeting": None,
     "music_instead_beeps": "ringout.wav",
     "greeting_voicemail": "voicemail.wav",
     "dial_up_cycles": 1,
     "block": False,
     "is_operator": False,
     "conversation_is_recording": True},

    {"username": "Александр Бардусов",
     "inner_number": 98879,
     "email": None,
     "login": "bardusov.a",
     "is_supervisor": False,
     "visibility_other_group": False,
     "prohibition_internal_number": False,
     "voicemail_on": True,
     "call_direction_restrictions": "<По умолчанию>",
     "redirect_to_user": "<По умолчанию>",
     "number_for_outgoing_calls": "<По умолчанию>",
     "greeting": None,
     "music_instead_beeps": "ringout.wav",
     "greeting_voicemail": "voicemail.wav",
     "dial_up_cycles": 1,
     "block": False,
     "is_operator": False,
     "conversation_is_recording": True}
]

contacts_user = [
    {"contact_numbers_user": [
         {"username": "katana",
          "login": "katana4",
          "is_on": True,
          "do_not_display_other": False,
          "number": "+79107018535",
          "fmc": True,
          "priority": 1,
          "dial_up_time": 40,
          "contact_type": "Мобильный",
          "filter_list": None,
          "working_time": None}
        ]
    },

    {"contact_numbers_user": [
        {"username": "katana",
         "login": "katana4",
         "is_on": True,
         "do_not_display_other": False,
         "number": "katana4",
         "fmc": None,
         "priority": 1,
         "dial_up_time": 40,
         "contact_type": "IP-телефон",
         "filter_list": None,
         "working_time": None},

        {"username": "katana",
         "login": "katana4",
         "is_on": True,
         "do_not_display_other": False,
         "number": "katana",
         "fmc": None,
         "priority": 1,
         "dial_up_time": 40,
         "contact_type": "IP-телефон",
         "filter_list": None,
         "working_time": None},

        {"username": "katana",
         "login": "katana4",
         "is_on": True,
         "do_not_display_other": False,
         "number": "89107018535",
         "fmc": False,
         "priority": 10,
         "dial_up_time": 40,
         "contact_type": "Мобильный",
         "filter_list": None,
         "working_time": None}
        ]
    },

    {"contact_numbers_user": [
         {"username": "Александр Бардусов",
          "login": "bardusov.a",
          "is_on": True,
          "do_not_display_other": False,
          "number": "bardusov.a",
          "fmc": None,
          "priority": 10,
          "dial_up_time": 40,
          "contact_type": "IP-телефон",
          "filter_list": None,
          "working_time": None},

         {"username": "Александр Бардусов",
          "login": "bardusov.a",
          "is_on": True,
          "do_not_display_other": False,
          "number": "89104149571",
          "fmc": False,
          "priority": 20,
          "dial_up_time": 40,
          "contact_type": "Мобильный",
          "filter_list": None,
          "working_time": None}
        ]
    }
]

groups_user = [
    {"username": "Chursina_SV",
     "login": "test1",
     "groups_list": ["oums", "1.5 ЛТП ВАТС (GMT+3)"]},

    {"username": "katana",
     "login": "katana4",
     "groups_list": ["Катана Елена Ивановна", "1.5 ЛТП ВАТС (GMT+3)"]},

    {"username": "Александр Бардусов",
     "login": "bardusov.a",
     "groups_list": ["1.5 ЛТП ВАТС (GMT+3)"]},

    {"username": "Александр Лаппо 2",
     "login": "alexl2",
     "groups_list": ["oums", "1.5 ЛТП ВАТС (GMT+3)"]},
]

group_info = [
    {"group_name": "1.5 ЛТП ВАТС (GMT+3)",
     "number": 98863,
     "email": None,
     "interception_call": False,
     "skip_greeting": False,
     "prohibition_dialing_number": False,
     "voicemail_is_on": False,
     "distribution_alg": None,
     "voice_greeting": "greeting.wav",
     "voicemail_greeting": "domainvoicemail.wav"},

    {"group_name": "1.5 ЛТП ВАТС (GMT+7)",
     "number": 98865,
     "email": None,
     "interception_call": False,
     "skip_greeting": False,
     "prohibition_dialing_number": False,
     "voicemail_is_on": False,
     "distribution_alg": None,
     "voice_greeting": "greeting.wav",
     "voicemail_greeting": "domainvoicemail.wav"},

    {"group_name": "113231",
     "number": 98786,
     "email": None,
     "interception_call": False,
     "skip_greeting": False,
     "prohibition_dialing_number": False,
     "voicemail_is_on": False,
     "distribution_alg": None,
     "voice_greeting": "greeting.wav",
     "voicemail_greeting": "domainvoicemail.wav"},

    {"group_name": "FMC DC OTT",
     "number": 89067,
     "email": None,
     "interception_call": False,
     "skip_greeting": False,
     "prohibition_dialing_number": False,
     "voicemail_is_on": False,
     "distribution_alg": None,
     "voice_greeting": "greeting.wav",
     "voicemail_greeting": "domainvoicemail.wav"}
]

users_in_group = [
    {"group_name": "1.5 ЛТП ВАТС (GMT+3)",
     "users_list": [
             {"username": "Афанасьев Дмитрий", "priority": 1},
             {"username": "Крючков Николай", "priority": 2},
             {"username": "Поисьева Екатерина", "priority": 3},
             {"username": "Александр Бардусов", "priority": 4},
             {"username": "Вадим Яценко", "priority": 5}
         ]
    },

    {"group_name": "1.5 ЛТП ВАТС (GMT+7)",
     "users_list": [
              {"username": "Кабанцов Алексей", "priority": 10},
              {"username": "Киселев Ярослав", "priority": 10},
              {"username": "Кузнецова Юлия", "priority": 20},
              {"username": "Олег Барабанщиков", "priority": 1},
              {"username": "Оксана Касицина", "priority": 4}
         ]
    }
]

names_ivr = [
    {"ivr_name": "wewe", "ivr_id": 1941},
    {"ivr_name": "ЛЦК", "ivr_id": 21432},
    {"ivr_name": "привет", "ivr_id": 62412},
    {"ivr_name": "ghhf", "ivr_id": 63082},
    {"ivr_name": "sdas", "ivr_id": 63502}
]

params_events_ivr = [
    {"name_menu": "Главное меню",
     "voice_file": "Alarm05.wav",
     "ivr_id": 1941,
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
    },

    {"name_menu": "Тест НСК",
     "voice_file": None,
     "ivr_id": 1941,
     "events_and_actions": [
            {"event": 0, "action": "pronounce_phrase", "params": "userrecord13.wav"},
            {"event": 1, "action": "disconnect", "params": None},
            {"event": 2, "action": "pronounce_phrase", "params": None},
            {"event": 3, "action": "disconnect", "params": None},
            {"event": 4, "action": "default", "params": None},
            {"event": 5, "action": "default", "params": None},
            {"event": 6, "action": "default", "params": None},
            {"event": 7, "action": "default", "params": None},
            {"event": 8, "action": "default", "params": None},
            {"event": 9, "action": "default", "params": None},
            {"event": "*", "action": "default", "params": None},
            {"event": "#", "action": "default", "params": None},
            {"event": "timeout", "action": "pronounce_phrase", "params": None},
            {"event": "default", "action": "additional_inner_number_user", "params": None}
        ]
     }
]

route_info = [
    {"route_id": 25480,
     "status": True,
     "name": "ip_192.168.32.200_vpn9139",
     "private": True,
     "regular_exp_to": "sip:007[0-9]{10}@.*",
     "tgrp": "V1244-192168032200",
     "outgoing_calls": "Без ограничений"}
]

route_settings = [
    {"name": "ip_192.168.32.200_vpn9139",
     "authorization_name": None,
     "digest_username": None,
     "update_period": 3600,
     "nat_ping_period": 300,
     "assigned_ip": None,
     "tgrp": "V1244-192168032200",
     "exp_for_callee_number": "sip:007[0-9]{10}@.*",
     "exp_for_caller_number": ".*",
     "added_to_begin_str": None,
     "default_uri_for_caller_domain": None,
     "private": True,
     "is_on": True,
     "convert_to_e164": False,
     "allow_sub_number_from": True,
     "allow_accept_calls_to_unique_username": False,
     "activation": None,
     "authorization_type_calls": "ipsource-tgrp",
     "transport": "UDP",
     "type_route_choice": "for_lines",
     "only_for_groups": None,
     "number_sub_for_domain_caller": "Внутренний номер",
     "type_header_allow_auth": None,
     "type_header_history_redirect": "Diversion или History-Info",
     "limit_directions_transit_calls_SSOP": None,
     "count_digits_cutter_in_begin_number": 2,
     "max_count_renewals_registration": 0,
     "ip_address": "10.243.208.20:5060",
     "destination_domain_or_sip_proxy": "private.trunk"}
]