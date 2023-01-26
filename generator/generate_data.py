# -*- coding: utf-8 -*-
import os.path
import random
import string
from dataclasses import dataclass

import jsonpickle
import mimesis


@dataclass
class Ganerate:
    app: any

    @staticmethod
    def createData():
        f = "data/db_data.json"

        name = 'a' * 31
        name_path = random.randint(1111111111, 9999999999)

        # Настройки/Дата время
        random_1 = random.choice([".", '-'])
        random_2 = random.choice(string.ascii_lowercase)
        server_address = str(random_2 * 3) + str(random_1) + str(random.randint(111, 999)) + str(random_2 * 5) + str(
            '.ru')
        server_address_work = 'dc7-serv.bolid.ru'

        # Настройки/Объект
        name_object = 'a' * 31
        number_object = random.randint(1, 9999)
        Take_Delay = random.randint(5, 65535)
        Input_Alarm_Delay = random.randint(5, 65535)
        Auto_arm_time = random.randint(5, 65535)

        # Настройки/Звуковая индикация
        Signal_duration = random.randint(10, 65535)
        Event_volume = random.randint(1, 100)
        Alarm_volume = random.randint(1, 100)

        # Настройки/Радио
        Resolution_time_for_adding_new_sensors = random.randint(60, 900)
        Sensor_polling_period = random.randint(60, 120)

        # Настройки/GSM
        Number_of_digits_of_the_number_to_check = random.randint(3, 11)
        Balance_Notification_Threshold = random.randint(1, 32767)
        SIM_1_USSD = ("*" + str(random.randint(1111, 9999)) + "#")
        SIM_2_USSD = ("*" + str(random.randint(1111, 9999)) + "#")
        SIM_1_PIN = random.randint(111111111, 999999999)
        SIM_2_PIN = random.randint(111111111, 999999999)
        APN_1 = random.choice(string.ascii_lowercase) * (random.randint(1, 63))
        APN_2 = random.choice(string.ascii_lowercase) * (random.randint(1, 63))
        login_sim_1 = random.choice(string.ascii_lowercase) * (random.randint(1, 63))
        login_sim_2 = random.choice(string.ascii_lowercase) * (random.randint(1, 63))
        password_sim_1 = random.choice(string.ascii_lowercase) * (random.randint(1, 63))
        password_sim_2 = random.choice(string.ascii_lowercase) * (random.randint(1, 63))

        # Настройки/Ethernet
        MAC_address = (random.choice(string.hexdigits) * 2) + '-' + (random.choice(string.hexdigits) * 2) + '-' + (
                random.choice(string.hexdigits) * 2) + '-' + (random.choice(string.hexdigits) * 2) + '-' + (
                              random.choice(string.hexdigits) * 2) + '-' + (random.choice(string.hexdigits) * 2)
        Server_name = (random.choice(string.ascii_letters) * 8) + (random.choice(string.digits) * 8)
        Address_IPv4 = mimesis.Internet().ip_v4()
        Subnet_mask = mimesis.Internet().ip_v4()
        Main_gate = mimesis.Internet().ip_v4()
        Preferred_DNS_Server = mimesis.Internet().ip_v4()
        Alternative_DNS_Server = mimesis.Internet().ip_v4()
        Local_IPv6_address = mimesis.Internet().ip_v6()
        Global_IPv6_address = mimesis.Internet().ip_v6()
        Preferred_IPv6_DNS_Server = mimesis.Internet().ip_v6()
        Alternative_IPv6_DNS_Server = mimesis.Internet().ip_v6()

        # Выходы
        rus = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у",
               "ф", "х", "ц", "ч", "ш",
               "щ", "ъ", "ы", "ь", "э", "ю", "я"]
        tumbler = ['ON', 'OFF']
        tumbler_1 = ['OFF', 'ON']
        tumbler_2 = ['ON', 'OFF']
        tumbler_3 = ['ON', 'OFF']
        tumbler_4 = ['ON', 'OFF']
        tumbler_5 = ['ON', 'OFF']
        tumbler_6 = ['ON', 'OFF']
        mask_out_1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17']
        mask_out_2 = ['17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32',
                      '33']
        Time_widget = random.randint(1, 1024)
        Tumbler_turn_on_when_finished = random.choice(tumbler)
        Tumbler_random_1 = random.choice(tumbler_1)
        Tumbler_random_2 = random.choice(tumbler_2)
        Tumbler_random_3 = random.choice(tumbler_3)
        Tumbler_random_4 = random.choice(tumbler_4)
        Tumbler_random_5 = random.choice(tumbler_5)
        Mask_random_out_1 = random.choice(mask_out_1)
        Mask_random_out_2 = random.choice(mask_out_2)
        Gisteresis_outs = random.randint(1, 10)
        Internal_reference_signal = random.randint(1, 100)
        Out_name = (random.choice(rus) * 31)

        # Разделы
        Number_path = random.randint(1, 999)
        Name_path = 'a' * 31

        # Направления
        Name_direction = random.choice(string.ascii_letters) * 31
        path = ['Раздел № 01', 'Раздел № 02', 'Раздел № 03', 'Раздел № 04', 'Раздел № 05', 'Раздел № 06',
                'Раздел № 07', 'Раздел № 08', 'Раздел № 09', 'Раздел № 10', 'Раздел № 11', 'Раздел № 12',
                'Раздел № 13', 'Раздел № 14', 'Раздел № 15', 'Раздел № 16']
        cod_n = ['+7', '+375', '+994', '+374', '+995', '+996', '+373', '+992', '+993', '+998']
        langList = ['Русский', 'Английский']
        day = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
        time = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00',
                '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00',
                '22:00', '23:00']
        pathList = random.choice(path)
        pathList_2 = random.choice(path)
        Phone_cod = random.choice(cod_n)
        Phone_cod_2 = random.choice(cod_n)
        assert_Phone_number = f'(' + str(random.randint(111, 999)) + ') ' \
                              + str(random.randint(111, 999)) + '-' + str(random.randint(11, 99)) \
                              + '-' + str(random.randint(11, 99))
        Phone_number = f'(' + str(random.randint(111, 999)) + ')' \
                       + str(random.randint(111, 999)) + '-' + str(random.randint(11, 99)) \
                       + '-' + str(random.randint(11, 99))
        Phone_number_2 = f'(' + str(random.randint(111, 999)) + ')' \
                         + str(random.randint(111, 999)) + '-' + str(random.randint(11, 99)) \
                         + '-' + str(random.randint(11, 99))
        Lang = random.choice(langList)
        Test_if = random.choice(['Канал активен', 'Всегда'])
        Test_method = random.choice(['SMS', 'Звонок', 'SMS Эгида'])
        Timeout_on_error = str(random.randint(11, 23)) + ':' + str(random.randint(11, 59))
        Test_interval = str(random.randint(11, 23)) + ':' + str(random.randint(11, 59))
        Days_of_the_week = random.choice(day)
        Time = random.choice(time)
        count_rep = random.randint(1, 65535)
        dc09_adr = 'http://www' + str(random.randint(111111, 999999)) + '.ru'
        dc09_port = random.randint(1111, 9999)
        Connection_channel = random.choice(['Авто', 'Ethernet', 'GPRS'])
        Confirmation_timeout_sec = random.randint(20, 90)
        num_random = random.randint(11, 99)
        Encryption_key = f'{num_random}:{num_random}:{num_random}:{num_random}:{num_random}:{num_random}:{num_random}:{num_random}:{num_random}:{num_random}:{num_random}:{num_random}:{num_random}:{num_random}:{num_random}:{num_random}'

        # Пользователи и ключи
        user_name = mimesis.Person("en").name()
        user_login = mimesis.Person("en").name()
        Listnumber_1 = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9',
                                      '10', '11', '12', '13', '14', '15', '16'])
        Listnumber_2 = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9',
                                      '10', '11', '12', '13', '14', '15', '16'])

        Listnumber_11 = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9',
                                       '10', '11', '12', '13', '14', '15', '16'])
        Listnumber_22 = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9',
                                       '10', '11', '12', '13', '14', '15', '16'])

        Permissions = random.choice(['Не настроен', 'Взятие/снятие разделов',
                                     'Взятие разделов', 'Снятие разделов'])

        # Брелок
        brelok_name = name
        brelok_silent_larm_method_list = random.choice(['Зажать на 3-10 сек', 'Зажать на 3 сек, нажать 1 раз'])

        # c 2000p ik
        c_2000p_ik_display_mode = random.choice(['Автоматический режим индикации', 'Индикация включена',
                                                 'Индикация выключена', 'Мигание по маске, согласно протоколу ДПЛС'])
        # c 2000p smk
        c_2000p_smk_mode_off = random.choice(['Герконы', 'Шлейф', 'Геркон и шлейф'])

        # КЦ
        kc_type_zone = random.choice(['Охранный', 'Тревожный', 'Вход', 'Пожарный'])

        # СДВИГ
        list_001 = ['3', '5', '10', '15', '20', '25', '30', '45']
        list_002 = ['50', '100', '150', '200', '250', '300', '450', '500']
        porog_alarm_till_list = random.choice(list_001)
        porog_alarm_threshold_list = random.choice(list_002)

        # c 2000p IP
        Notification_made = random.choice(['Без уведомлений', 'Только по снижению', 'Только по повышению',
                                           'По снижению и повышению'])

        testdata = {

            'object': {
                'name_object': str(name_object),
                'number_object': str(number_object),
                'Take_Delay': str(Take_Delay),
                'Input_Alarm_Delay': str(Input_Alarm_Delay),
                'Auto_arm_time': str(Auto_arm_time)
            },

            'Radio': {
                'Resolution_time_for_adding_new_sensors': str(Resolution_time_for_adding_new_sensors),
                'Sensor_polling_period': str(Sensor_polling_period),
            },

            'DateTime': {
                'server_address': str(server_address_work),
            },

            'GSM': {
                'Resolution_time_for_adding_new_sensors': str(Number_of_digits_of_the_number_to_check),
                'Sensor_polling_period': str(Balance_Notification_Threshold),
                'SIM_1_USSD': str(SIM_1_USSD),
                'SIM_2_USSD': str(SIM_2_USSD),
                'SIM_1_PIN': str(SIM_1_PIN),
                'SIM_2_PIN': str(SIM_2_PIN),
                'APN_1': str(APN_1),
                'APN_2': str(APN_2),
                'login_sim_1': str(login_sim_1),
                'login_sim_2': str(login_sim_2),
                'password_sim_1': str(password_sim_1),
                'password_sim_2': str(password_sim_2),
            },

            'Ethernet': {
                'MAC_address': str(MAC_address),
                'Server_name': str(Server_name),
                'Address_IPv4': str(Address_IPv4),
                'Subnet_mask': str(Subnet_mask),
                'Main_gate': str(Main_gate),
                'Preferred_DNS_Server': str(Preferred_DNS_Server),
                'Alternative_DNS_Server': str(Alternative_DNS_Server),
                'Local_IPv6_address': str(Local_IPv6_address),
                'Global_IPv6_address': str(Global_IPv6_address),
                'Preferred_IPv6_DNS_Server': str(Preferred_IPv6_DNS_Server),
                'Alternative_IPv6_DNS_Server': str(Alternative_IPv6_DNS_Server)

            },

            'VolumIndication': {
                'Signal_duration': str(Signal_duration),
                'Event_volume': str(Event_volume),
                'Alarm_volume': str(Alarm_volume)
            },

            'Out': {
                'Time_widget': str(Time_widget),
                'Tumbler_turn_on_when_finished': str(Tumbler_turn_on_when_finished),
                'Mask_random_out_1': str(Mask_random_out_1),
                'Mask_random_out_2': str(Mask_random_out_2),
                'Gisteresis_outs': str(Gisteresis_outs),
                'Internal_reference_signal': str(Internal_reference_signal),
                'Tumbler_inversion_of_control': str(Tumbler_turn_on_when_finished),
                'Out_name': str(Out_name),
                'tumbler_1': str(Tumbler_random_1),
                'tumbler_2': str(Tumbler_random_2),
            },

            'Path': {
                'Name_path': str(name_path),
                'Number_path': str(Number_path),
                'tumbler_1': str(Tumbler_random_1),
                'tumbler_2': str(Tumbler_random_2),
                'tumbler_3': str(Tumbler_random_3)
            },

            'Directions': {
                'Name_direction': str(name),
                'pathList': str(pathList),
                'Phone_cod': str(Phone_cod),
                'Phone_number': str(Phone_number),
                'assert_Phone_number': str(assert_Phone_number),
                'Lang': str(Lang),
                'Send_event_time': str(Tumbler_random_1),
                'Send_event_date': str(Tumbler_random_2),
                'Test_if': str(Test_if),
                'Test_method': str(Test_method),
                'Timeout_on_error': str(Timeout_on_error),
                'Test_interval': str(Test_interval),
                'Days_of_the_week': str(Days_of_the_week),
                'Time': str(Time),
                'Count_rep': str(count_rep),
                'DC09_address': str(dc09_adr),
                'DC09_port': str(dc09_port),
                'Connection_channel': str(Connection_channel),
                'Confirmation_timeout_sec': str(Confirmation_timeout_sec),
                'Encryption_key': str(Encryption_key)

            },

            'User': {
                'CB_egida': str(Tumbler_random_5),
                'user_name': str(user_name),
                'user_login': str(user_login),
                'user_password': str(user_name),
                'CB_Operator_message_forwarding': str(Tumbler_random_1),
                'CB_Sending_out_of_broadcast': str(Tumbler_random_2),
                'DL_Group_of_outputs_controlled_by_SMS': str(Listnumber_1),
                'DL_Group_of_outputs_with_call_control': str(Listnumber_2),
                'CB_Allow_withdrawal_by_SMS': str(Tumbler_random_3),
                'CB_Allow_Pickup_by_SMS': str(Tumbler_random_4),
                'user_phone_cod': str(Phone_cod),
                'user_phone_number': str(Phone_number),
                'user_sms_password': str(random.randint(11111, 99999)),
                'pathList': str(pathList),

                'CB_egida_2': str(Tumbler_random_1),
                'user_name_2': str(user_name),
                'user_login_2': str(user_login),
                'user_password_2': str(user_name),
                'CB_Operator_message_forwarding_2': str(Tumbler_random_2),
                'CB_Sending_out_of_broadcast_2': str(Tumbler_random_3),
                'DL_Group_of_outputs_controlled_by_SMS_2': str(Listnumber_11),
                'DL_Group_of_outputs_with_call_control_2': str(Listnumber_22),
                'CB_Allow_withdrawal_by_SMS_2': str(Tumbler_random_4),
                'CB_Allow_Pickup_by_SMS_2': str(Tumbler_random_5),
                'user_phone_cod_2': str(Phone_cod_2),
                'user_phone_number_2': str(Phone_number_2),
                'user_sms_password_2': str(random.randint(11111, 99999)),
                'pathList_2': str(pathList_2)

            },
            'Key': {
                'key_id': str(random.randint(111, 999999999999)),
                'Permissions': str(Permissions),
                'pathList': str(pathList)
            },

            'Brelok': {
                'brelok_CB_sensor_on': "ON",
                'brelok_name': str(name),
                'brelok_path': str(pathList),
                'brelok_pathList_1': str(pathList),
                'brelok_pathList_2': str(pathList_2),
                'brelok_silent_larm_method': str(brelok_silent_larm_method_list),
                'brelok_button_output_group_1': str(Listnumber_1),
                'brelok_button_output_group_2': str(Listnumber_2),
                'brelok_CB_take_off': str(random.choice(tumbler)),
                'brelok_CB_take_on': "ON",
                'brelok_CB_sirena_off': str(random.choice(tumbler_2))
            },

            'C_2000P_IK': {
                'c_2000p_ik_CB_sensor_on': "ON",
                'c_2000p_ik_name': str(name),
                'c_2000p_ik_path': str(pathList),
                'c_2000p_ik_display_mode': str(c_2000p_ik_display_mode),
                'c_2000p_ik_CB_bell_mode': str(random.choice(tumbler)),
                'c_2000p_ik_CB_energy_saving_mode': str(random.choice(tumbler_1)),
                'c_2000p_ik_CB_test_mode': str(random.choice(tumbler_2)),
                'c_2000p_ik_W_Sensitivity': str(random.randint(1, 255))
            },

            'C_2000P_SMK': {
                'c_2000p_smk_CB_sensor_on': "ON",
                'c_2000p_smk_name': str(name),
                'c_2000p_smk_path': str(pathList),
                'c_2000p_smk_display_mode': str(c_2000p_ik_display_mode),
                'c_2000p_smk__CB_bell_mode': str(random.choice(tumbler)),
                'c_2000p_smk_CB_enabling_the_Anti_sabotage_mode': str(random.choice(tumbler_2)),
                'c_2000p_smk_W_Sensitivity': str(c_2000p_smk_mode_off)
            },

            'SENSOR_KC': {
                'sensor_kc_DL_type_zone': str(kc_type_zone),
                'sensor_kc_CB_sensor_on': str(random.choice(tumbler_3)),
                'sensor_kc_name': str(name),
                'sensor_kc_path': str(pathList),
                'sensor_kc_CB_bell_mode': str(random.choice(tumbler))
            },

            'C_2000P_SDVIG': {
                'c_2000p_sdvig_CB_sensor_on': "ON",
                'c_2000p_sdvig_name': str(name),
                'c_2000p_sdvig_path': str(pathList),
                'c_2000p_sdvig_display_mode': str(c_2000p_ik_display_mode),
                'c_2000p_sdvig_CB_bell_mode': str(random.choice(tumbler)),
                'c_2000p_sdvig_CB_tilt_sdvig': str(random.choice(tumbler_1)),
                'c_2000p_sdvig_CB_tilt_control': str(random.choice(tumbler_2)),
                'c_2000p_sdvig_CB_fix_tilt_control': str(random.choice(tumbler_3)),
                'c_2000p_sdvig_CB_energo_mode': str(random.choice(tumbler_4)),
                'c_2000p_sdvig_CB_fix_position': str(random.choice(tumbler_5)),
                'c_2000p_sdvig_CB_control_gerkon': str(random.choice(tumbler_6)),
                'c_2000p_DL_sdvig_tilt_alarm_threshold': str(porog_alarm_till_list),
                'c_2000p_DL_sdvig_movement_alarm_threshold': str(porog_alarm_threshold_list)
            },

            'C_2000P_IP': {
                'C_2000P_IP_CB_sensor_on': "ON",
                'C_2000P_IP_name': str(name),
                'C_2000P_IP_path': str(pathList),
                'C_2000P_IP_display_mode': str(c_2000p_ik_display_mode),
                'C_2000P_IP_CB_bell_mode': str(random.choice(tumbler_1)),
                'C_2000P_IP_gisteresis': str(random.randint(1, 99)),
                'C_2000P_IP_temp_min': str(random.randint(1, 99)),
                'C_2000P_IP_temp_max': str(random.randint(1, 99)),
                'C_2000P_IP_notification_mode': str(Notification_made),
                'C_2000P_IP_CB_open': str(random.choice(tumbler_2)),

            }

        }

        file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

        with open(file, "w", encoding='utf-8') as out:
            jsonpickle.set_encoder_options("json", indent=4, sort_keys=False, ensure_ascii=False)
            out.write(jsonpickle.encode(testdata))
