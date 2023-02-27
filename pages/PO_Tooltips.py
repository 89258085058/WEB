# -*- coding: utf-8 -*-

from dataclasses import dataclass

from selenium.common import TimeoutException

from data.tooltips_text import *
from locators.auth_locators import *
from locators.tooltips_locators import *


@dataclass
class TooltipsHelper:
    app: any

    # Метод проверка вспывающей подсказки
    def assert_tooltip_messege(self, locator, text):
        try:
            self.app.method.elementFocus(locator)
            self.app.method.assertTooltipText(text)
        except TimeoutException as exc:
            assert exc == TimeoutException, f"Ошибка!!! Текст по локатору '{locator}' -  не найден"

    # АВТОРИЗАЦИЯ - Проверка подсказки логин
    def tooltip_login(self):
        self.assert_tooltip_messege(locator=login_input, text=login_tooltip_messege)

    # АВТОРИЗАЦИЯ - Проверка подсказки пароль
    def tooltip_password(self):
        self.assert_tooltip_messege(locator=password_input, text=password_tooltip_messege)

    # НАСТРОЙКИ/ОБЪЕКТ - Проверка подсказки Название объекта
    def tooltip_settings_object_name_input(self):
        self.assert_tooltip_messege(locator=object_name_input, text=input_max_len_32)

    def tooltip_settings_object_name(self):
        self.assert_tooltip_messege(locator=object_name, text=Settings_object_tooltip_messege_name_object)

    # НАСТРОЙКИ/ОБЪЕКТ Проверка подсказки Номер объекта
    def tooltip_settings_object_number_input(self):
        self.assert_tooltip_messege(locator=object_number_input,
                                    text=input_numbers_1_9999_num)

    def tooltip_settings_object_number(self):
        self.assert_tooltip_messege(locator=object_number, text=Settings_object_tooltip_messege_number_object)

    # НАСТРОЙКИ/ОБЪЕКТ Проверка подсказки Задержка взятия
    def tooltip_settings_take_delay_input(self):
        self.assert_tooltip_messege(locator=object_delay_take_on_input, text=input_65535_necessary)

    def tooltip_settings_take_delay(self):
        self.assert_tooltip_messege(locator=object_delay_take_on, text=Settings_object_tooltip_messege_take_delay)

    # НАСТРОЙКИ/ОБЪЕКТ Проверка подсказки Задержка тревоги входа
    def tooltip_settings_object_delay_alarm_enter_input(self):
        self.assert_tooltip_messege(locator=object_delay_alarm_enter_input, text=input_65535_necessary)

    def tooltip_settings_object_delay_alarm_enter(self):
        self.assert_tooltip_messege(locator=object_delay_alarm_enter,
                                    text=Settings_object_tooltip_messege_input_alarm_delay)

    # НАСТРОЙКИ/ОБЪЕКТ Проверка подсказки Время автовзятия
    def tooltip_settings_object_time_auto_take_on_input(self):
        self.assert_tooltip_messege(locator=object_time_auto_take_on_input, text=input_65535_necessary)

    def tooltip_settings_object_time_auto_take_on(self):
        self.assert_tooltip_messege(locator=object_time_auto_take_on,
                                    text=Settings_object_tooltip_messege_input_auto_arm_time)

    # НАСТРОЙКИ ОБЪЕКТ Проверка подсказки Тревога при потере датчика
    def tooltip_settings_object_sensor_loss_alarm(self):
        self.assert_tooltip_messege(locator=object_sensor_loss_alarm,
                                    text=Settings_object_tooltip_messege_sensor_loss_alarm)

    # НАСТРОЙКИ/ОБЪЕКТ Проверка подсказки Взятие при потерянных датчиках
    def tooltip_settings_object_taking_with_lost_sensors(self):
        self.assert_tooltip_messege(locator=object_taking_with_lost_sensors,
                                    text=Settings_object_tooltip_messege_taking_with_lost_sensors)

    # НАСТРОЙКИ/ОБЪЕКТ Проверка подсказки Взятие при датчиках в тревоге
    def tooltip_settings_object_taking_with_sensors_in_alarm(self):
        self.assert_tooltip_messege(locator=object_taking_with_sensors_in_alarm,
                                    text=Settings_object_tooltip_messege_taking_with_sensors_in_alarm)

    # НАСТРОЙКИ/ОБЪЕКТ Проверка подсказки Взятие при датчиках в неисправности
    def tooltip_settings_object_capturing_with_sensors_in_error(self):
        self.assert_tooltip_messege(locator=object_capturing_with_sensors_in_error,
                                    text=Settings_object_tooltip_messege_capturing_with_sensors_in_error)

    # НАСТРОЙКИ/ОБЪЕКТ Проверка подсказки Принудительное взятие из тревоги
    def tooltip_settings_object_forced_take_from_alarm(self):
        self.assert_tooltip_messege(locator=object_forced_take_from_alarm,
                                    text=Settings_object_tooltip_messege_forced_take_from_alarm)

    # НАСТРОЙКИ/ДАТА И ВРЕМЯ - Использовать время GSM сети
    def tooltip_settings_date_time_drop_list_gsm(self):
        self.assert_tooltip_messege(locator=Date_and_time_on_the_device, text=Settings_date_time_tooltip_messege_gsm)

    # НАСТРОЙКИ/ДАТА И ВРЕМЯ - Использовать время GSM сети - Использовать временную зону GSM сети
    def tooltip_settings_date_time_drop_list_use_gsm(self):
        self.assert_tooltip_messege(locator=date_time_use_time_zone_of_GSM_network,
                                    text=Settings_date_time_tooltip_messege_use_time_zone_of_GSM_network)

    # НАСТРОЙКИ/ДАТА И ВРЕМЯ - Использовать время GSM сети - Переход на летнее время
    def tooltip_settings_date_time_daylight_Saving_Time(self):
        self.assert_tooltip_messege(locator=date_time_daylight_Saving_Time,
                                    text=Settings_date_time_tooltip_messege_daylight_Saving_Time)

    # НАСТРОЙКИ/ДАТА И ВРЕМЯ - Синхронизация по NTP/HTP
    def tooltip_settings_date_time_drop_list_ntp(self):
        self.assert_tooltip_messege(locator=Date_and_time_on_the_device, text=Settings_date_time_tooltip_messege_ntp)

    def tooltip_settings_date_time_drop_list_ntp_input(self):
        self.assert_tooltip_messege(locator=date_time_ntp_server_address_input, text=input_server_address_23)

    # НАСТРОЙКИ/ДАТА И ВРЕМЯ - Синхронизация по NTP/HTP - Адрес сервера
    def tooltip_settings_date_time_drop_list_ntp_adress_server(self):
        self.assert_tooltip_messege(locator=date_time_ntp_server_address,
                                    text=Settings_date_time_tooltip_messege_ntp_server_address)

    # НАСТРОЙКИ/ДАТА И ВРЕМЯ - Синхронизация по NTP/HTP - Часовой пояс
    def tooltip_settings_date_time_drop_list_ntp_server_time_zone(self):
        self.assert_tooltip_messege(locator=date_time_time_zone, text=Settings_date_time_tooltip_messege_ntp_time_zon)

    # НАСТРОЙКИ/ДАТА И ВРЕМЯ - Вручную
    def tooltip_settings_date_time_drop_list_hend(self):
        self.assert_tooltip_messege(locator=Date_and_time_on_the_device, text=Settings_date_time_tooltip_messege_hend)

    # НАСТРОЙКИ/ДАТА И ВРЕМЯ - Вручную - Дата и время
    def tooltip_settings_date_time_drop_list_hend_date_time(self):
        self.assert_tooltip_messege(locator=date_time_locator, text=Settings_date_time_tooltip_messege_hend_date_time)

    # НАСТРОЙКИ/ДАТА И ВРЕМЯ - Вручную - Часовой пояс
    def tooltip_settings_date_time_drop_list_hend_time_zone(self):
        self.assert_tooltip_messege(locator=date_time_time_zone, text=Settings_date_time_tooltip_messege_ntp_time_zon)

    # НАСТРОЙКИ/Прибор - Включить энергосберегающий режим
    def tooltip_settings_device_enable_power_saving_mode(self):
        self.assert_tooltip_messege(locator=Enable_power_saving_mode,
                                    text=text_Enable_power_saving_mode)

    # НАСТРОЙКИ/Прибор - Разрешить настройку при закрытом корпусе
    def tooltip_settings_device_Allow_configuration_when_the_case_is_closed(self):
        self.assert_tooltip_messege(locator=Allow_configuration_when_the_case_is_closed,
                                    text=text_Allow_configuration_when_the_case_is_closed)

    # НАСТРОЙКИ/Прибор - Фиксировать повторные тревоги раздела
    def tooltip_settings_device_Fix_partition_repeated_alarms(self):
        self.assert_tooltip_messege(locator=Fix_partition_repeated_alarms,
                                    text=text_Fix_partition_repeated_alarms)

    # НАСТРОЙКИ/Прибор - Фиксировать повторные тревоги датчика
    def tooltip_settings_device_Fix_repeated_sensor_alarms(self):
        self.assert_tooltip_messege(locator=Fix_repeated_sensor_alarms,
                                    text=text_Fix_repeated_sensor_alarms)

    # НАСТРОЙКИ/Прибор - Фиксировать повторные пожарные тревоги раздела
    def tooltip_settings_device_Fix_repeated_fire_alarms_in_a_section(self):
        self.assert_tooltip_messege(locator=Fix_repeated_fire_alarms_in_a_section,
                                    text=text_Fix_repeated_fire_alarms_in_a_section)

    # НАСТРОЙКИ/Прибор - Фиксировать повторные пожарные тревоги датчика
    def tooltip_settings_device_Fix_repeated_fire_alarms_of_the_sensor(self):
        self.assert_tooltip_messege(locator=Fix_repeated_fire_alarms_of_the_sensor,
                                    text=text_Fix_repeated_fire_alarms_of_the_sensor)

    # НАСТРОЙКИ/Прибор - Фиксировать повторные события взятия/снятия
    def tooltip_settings_device_Fix_repeated_arming_disarming_events(self):
        self.assert_tooltip_messege(locator=Fix_repeated_arming_disarming_events,
                                    text=text_Fix_repeated_arming_disarming_events)

    # НАСТРОЙКИ/Прибор - Управлять выходами при повторном взятии/снятии
    def tooltip_settings_device_Control_exits_when_re_arming_disarming(self):
        self.assert_tooltip_messege(locator=Control_exits_when_re_arming_disarming,
                                    text=text_Control_exits_when_re_arming_disarming)

    # НАСТРОЙКИ/Световая индикация  - Режим светодиодов для охранных датчиков
    def tooltip_settings_light_indications_LED_mode_for_security_sensors(self):
        self.assert_tooltip_messege(locator=LED_mode_for_security_sensors,
                                    text=text_LED_mode_for_security_sensors)

    # НАСТРОЙКИ/Световая индикация  - Режим светодиодов для пожарных датчиков
    def tooltip_settings_light_indications_LED_mode_for_fire_detectors(self):
        self.assert_tooltip_messege(locator=LED_mode_for_fire_detectors,
                                    text=text_LED_mode_for_fire_detectors)

    # НАСТРОЙКИ/Световая индикация  - Режим светодиодов для технологических датчиков
    def tooltip_settings_light_indications_LED_mode_for_process_sensors(self):
        self.assert_tooltip_messege(locator=LED_mode_for_process_sensors,
                                    text=text_LED_mode_for_process_sensors)

    # НАСТРОЙКИ/Световая индикация  - Режим работы считывателя
    def tooltip_settings_light_indications_Reader_operation_mode(self):
        self.assert_tooltip_messege(locator=Reader_operation_mode,
                                    text=text_Reader_operation_mode)

    # НАСТРОЙКИ/Световая индикация - Инверсия индикации считывателя
    def tooltip_settings_light_indications_Reader_indication_inversion(self):
        self.assert_tooltip_messege(locator=Reader_indication_inversion,
                                    text=text_Reader_indication_inversion)

    # НАСТРОЙКИ/Звуковая индикация - Включить
    def tooltip_settings_volum_indications_ON(self):
        self.assert_tooltip_messege(locator=Volume_indication_ON,
                                    text=text_vol_indication_Volume_indication_ON)

    # НАСТРОЙКИ/Звуковая индикация - Длительность сигнала
    def tooltip_settings_volum_indications_Signal_duration(self):
        self.assert_tooltip_messege(locator=Signal_duration,
                                    text=text_vol_indication_Signal_duration)

    def tooltip_settings_volum_indications_Signal_duration_input(self):
        self.assert_tooltip_messege(locator=Signal_duration_input,
                                    text=input_65535_not_necessary)

    # НАСТРОЙКИ/Звуковая индикация - Громкость событий
    def tooltip_settings_volum_indications_Event_volume(self):
        self.assert_tooltip_messege(locator=Event_volume,
                                    text=text_vol_indication_Event_volume)

    # НАСТРОЙКИ/Звуковая индикация - Громкость тревог
    def tooltip_settings_volum_indications_Alarm_volume(self):
        self.assert_tooltip_messege(locator=Alarm_volume,
                                    text=text_vol_indication_Alarm_volume)

    # НАСТРОЙКИ/Звуковая индикация - Тревога
    def tooltip_settings_volum_indications_Anxiety(self):
        self.assert_tooltip_messege(locator=Anxiety,
                                    text=text_vol_indication_Anxiety)

    # НАСТРОЙКИ/Звуковая индикация - Пожар
    def tooltip_settings_volum_indications_Fire(self):
        self.assert_tooltip_messege(locator=Fire,
                                    text=text_vol_indication_Fire)

    # НАСТРОЙКИ/Звуковая индикация - Взятие раздела
    def tooltip_settings_volum_indications_Taking_section(self):
        self.assert_tooltip_messege(locator=Taking_section,
                                    text=text_vol_indication_Taking_section)

    # НАСТРОЙКИ/Звуковая индикация - Снятие раздела
    def tooltip_settings_volum_indications_Removing_partition(self):
        self.assert_tooltip_messege(locator=Removing_partition,
                                    text=text_vol_indication_Removing_partition)

    # НАСТРОЙКИ/Звуковая индикация - Задержка взятия
    def tooltip_settings_volum_indications_Take_Delay(self):
        self.assert_tooltip_messege(locator=Take_Delay,
                                    text=text_vol_indication_Take_Delay)

    # НАСТРОЙКИ/Звуковая индикация - Невзятие
    def tooltip_settings_volum_indications_Not_taking(self):
        self.assert_tooltip_messege(locator=Not_taking,
                                    text=text_vol_indication_Not_taking)

    # НАСТРОЙКИ/Звуковая индикация - Разделы частично взяты
    def tooltip_settings_volum_indications_Sections_partially_taken(self):
        self.assert_tooltip_messege(locator=Sections_partially_taken,
                                    text=text_vol_indication_Sections_partially_taken)

    # НАСТРОЙКИ/Звуковая индикация - Добавление датчика
    def tooltip_settings_volum_indications_Adding_sensor(self):
        self.assert_tooltip_messege(locator=Adding_sensor,
                                    text=text_vol_indication_Adding_sensor)

    # НАСТРОЙКИ/Звуковая индикация - Колокольчик
    def tooltip_settings_volum_indications_Bell(self):
        self.assert_tooltip_messege(locator=Bell,
                                    text=text_vol_indication_Bell)

    # НАСТРОЙКИ/Радио - Включить радиомодуль
    def tooltip_settings_radio_Enable_radio(self):
        self.assert_tooltip_messege(locator=Radio_Enable_radio,
                                    text=text_Radio_Enable_radio)

    # НАСТРОЙКИ/Радио - Время разрешения добавления новых датчиков
    def tooltip_settings_radio_Resolution_time_adding_new_sensor(self):
        self.assert_tooltip_messege(locator=Radio_Resolution_time_adding_new_sensors,
                                    text=text_Radio_Resolution_time_adding_new_sensors)

    def tooltip_settings_radio_Resolution_time_adding_new_sensor_input(self):
        self.assert_tooltip_messege(locator=Radio_Resolution_time_adding_new_sensors_input,
                                    text=input_60_900)

    # НАСТРОЙКИ/Радио - Канал
    def tooltip_settings_radio_Channel(self):
        self.assert_tooltip_messege(locator=Radio_Channel,
                                    text=text_Radio_Channel)

    # НАСТРОЙКИ/Радио - Период опроса датчиков
    def tooltip_settings_radio_Sensor_polling_period(self):
        self.assert_tooltip_messege(locator=Radio_Sensor_polling_period,
                                    text=text_Radio_Sensor_polling_period)

    def tooltip_settings_radio_Sensor_polling_period_input(self):
        self.assert_tooltip_messege(locator=Radio_Sensor_polling_period_input,
                                    text=input_5_120)

    # НАСТРОЙКИ/GSM - Включить модуль GSM
    def tooltip_settings_gsm_Enable_GSM_module(self):
        self.assert_tooltip_messege(locator=GSM_Enable_GSM_module,
                                    text=text_GSM_Enable_GSM_module)

    # НАСТРОЙКИ/GSM - Использовать GPRS
    def tooltip_settings_gsm_Use_GPRS(self):
        self.assert_tooltip_messege(locator=GSM_Use_GPRS,
                                    text=text_GSM_Use_GPRS)

    # НАСТРОЙКИ/GSM - Использовать резервную SIM
    def tooltip_settings_gsm_Use_backup_SIM(self):
        self.assert_tooltip_messege(locator=GSM_Use_backup_SIM,
                                    text=text_GSM_Use_backup_SIM)

    # НАСТРОЙКИ/GSM - Разрешить USSD
    def tooltip_settings_gsm_Allow_USSD(self):
        self.assert_tooltip_messege(locator=GSM_Allow_USSD,
                                    text=text_GSM_Allow_USSD)

    # НАСТРОЙКИ/GSM - Число знаков номера для проверки
    def tooltip_settings_gsm_Number_digits_number_to_check(self):
        self.assert_tooltip_messege(locator=GSM_Number_digits_number_to_check,
                                    text=text_GSM_Number_digits_number_to_check)

    def tooltip_settings_gsm_Number_digits_number_to_check_input(self):
        self.assert_tooltip_messege(locator=GSM_Number_digits_number_to_check_input,
                                    text=input_digits_11)

    # НАСТРОЙКИ/GSM - Порог уведомления о балансе
    def tooltip_settings_gsm_Balance_Notification_Threshold(self):
        self.assert_tooltip_messege(locator=GSM_Balance_Notification_Threshold,
                                    text=text_GSM_Balance_Notification_Threshold)

    def tooltip_settings_gsm_Balance_Notification_Threshold_input(self):
        self.assert_tooltip_messege(locator=GSM_Balance_Notification_Threshold_input,
                                    text=input_32768_)

    # НАСТРОЙКИ/GSM - Разрешить трансляцию событий
    def tooltip_settings_gsm_Allow_Event_Broadcast(self):
        self.assert_tooltip_messege(locator=GSM_Allow_Event_Broadcast,
                                    text=text_GSM_Allow_Event_Broadcast)

    # НАСТРОЙКИ/Ethernet - MAC адрес
    def tooltip_settings_ethernet_MAC_address(self):
        self.assert_tooltip_messege(locator=Ethernet_MAC_address,
                                    text=text_Ethernet_MAC_address)

    # НАСТРОЙКИ/Ethernet - Название сервера
    def tooltip_settings_ethernet_Server_name(self):
        self.assert_tooltip_messege(locator=Ethernet_Server_name,
                                    text=text_Ethernet_Server_name)

    # НАСТРОЙКИ/Ethernet - Адрес IPv4
    def tooltip_settings_ethernet_IPv4_address(self):
        self.assert_tooltip_messege(locator=Ethernet_IPv4_address,
                                    text=text_Ethernet_IPv4_address)

    # НАСТРОЙКИ/Ethernet - Маска подсети
    def tooltip_settings_ethernet_Subnet_mask(self):
        self.assert_tooltip_messege(locator=Ethernet_Subnet_mask,
                                    text=text_Ethernet_Subnet_mask)

    # НАСТРОЙКИ/Ethernet - Основной шлюз
    def tooltip_settings_ethernet_Main_gate(self):
        self.assert_tooltip_messege(locator=Ethernet_Main_gate,
                                    text=text_Ethernet_Main_gate)

    # НАСТРОЙКИ/Ethernet - Предпочтительный DNS сервер
    def tooltip_settings_ethernet_Preferred_DNS_Server(self):
        self.assert_tooltip_messege(locator=Ethernet_Preferred_DNS_Server,
                                    text=text_Ethernet_Preferred_DNS_Server)

    # НАСТРОЙКИ/Ethernet - Альтернативный DNS сервер
    def tooltip_settings_ethernet_Alternative_DNS_Server(self):
        self.assert_tooltip_messege(locator=Ethernet_Alternative_DNS_Server,
                                    text=text_Ethernet_Alternative_DNS_Server)

    # НАСТРОЙКИ/Ethernet - Получать IPv4 адрес и настройки автоматически
    def tooltip_settings_ethernet_Obtain_IPv4_address_settings_automatically(self):
        self.assert_tooltip_messege(locator=Ethernet_Obtain_IPv4_address_settings_automatically,
                                    text=text_Ethernet_Obtain_IPv4_address_settings_automatically)

    # НАСТРОЙКИ/Ethernet - Использовать как сервер
    def tooltip_settings_ethernet_Use_as_server(self):
        self.assert_tooltip_messege(locator=Ethernet_Use_as_server,
                                    text=text_Ethernet_Use_as_server)

    # НАСТРОЙКИ/Ethernet - Получать адрес IPv6 от DHCP автоматически
    def tooltip_settings_ethernet_Obtain_IPv6_address_DHCP_automatically(self):
        self.assert_tooltip_messege(locator=Ethernet_Obtain_IPv6_address_DHCP_automatically,
                                    text=text_Ethernet_Obtain_IPv6_address_DHCP_automatically)

    # НАСТРОЙКИ/Ethernet - Разрешить удаленное управление
    def tooltip_settings_ethernet_Allow_remote_control(self):
        self.assert_tooltip_messege(locator=Ethernet_Allow_remote_control,
                                    text=text_Ethernet_Allow_remote_control)

    # НАСТРОЙКИ/Ethernet - Получать адрес IPv6 от SLAAC автоматически
    def tooltip_settings_ethernet_Obtain_IPv6_address_SLAAC_automatically(self):
        self.assert_tooltip_messege(locator=Ethernet_Obtain_IPv6_address_SLAAC_automatically,
                                    text=text_Ethernet_Obtain_IPv6_address_SLAAC_automatically)

    # НАСТРОЙКИ/Ethernet - Разрешить незащищенное HTTP-соединение
    def tooltip_settings_ethernet_Allow_insecure_HTTP_connection(self):
        self.assert_tooltip_messege(locator=Ethernet_Allow_insecure_HTTP_connection,
                                    text=text_Ethernet_Allow_insecure_HTTP_connection)

    # НАСТРОЙКИ/Ethernet - Устанавливать сетевые подключения через
    def tooltip_settings_ethernet_Establish_network_connections(self):
        self.assert_tooltip_messege(locator=Ethernet_Establish_network_connections,
                                    text=text_Ethernet_Establish_network_connections)

    # НАСТРОЙКИ/Ethernet - Локальный IPv6 адрес
    def tooltip_settings_ethernet_Local_IPv6_address(self):
        self.assert_tooltip_messege(locator=Ethernet_Local_IPv6_address,
                                    text=text_Ethernet_Local_IPv6_address)

    # НАСТРОЙКИ/Ethernet - Глобальный IPv6 адрес
    def tooltip_settings_ethernet_Global_IPv6_Address(self):
        self.assert_tooltip_messege(locator=Ethernet_Global_IPv6_Address,
                                    text=text_Ethernet_Global_IPv6_Address)

    # НАСТРОЙКИ/Ethernet - Предпочтительный IPv6 DNS сервер
    def tooltip_settings_ethernet_Preferred_IPv6_DNS_Server(self):
        self.assert_tooltip_messege(locator=Ethernet_Preferred_IPv6_DNS_Server,
                                    text=text_Ethernet_Preferred_IPv6_DNS_Server)

    # НАСТРОЙКИ/Ethernet - Альтернативный IPv6 DNS сервер
    def tooltip_settings_ethernet_Alternative_IPv6_DNS_Server(self):
        self.assert_tooltip_messege(locator=Ethernet_Alternative_IPv6_DNS_Server,
                                    text=text_Ethernet_Alternative_IPv6_DNS_Server)

    # НАСТРОЙКИ/GSM - SIM PIN
    def tooltip_settings_gsm_sim_1_pin_input(self):
        self.assert_tooltip_messege(locator=GSM_sim_1_pin_input,
                                    text=input_PIN)

    def tooltip_settings_gsm_sim_2_pin_input(self):
        self.assert_tooltip_messege(locator=GSM_sim_2_pin_input,
                                    text=input_PIN)

    # НАСТРОЙКИ/GSM - SIM USSD
    def tooltip_settings_gsm_sim_1_ussd_input(self):
        self.assert_tooltip_messege(locator=GSM_sim_1_USSD_cod_input,
                                    text=input_USSD)

    def tooltip_settings_gsm_sim_2_ussd_input(self):
        self.assert_tooltip_messege(locator=GSM_sim_2_USSD_cod_input,
                                    text=input_USSD)

    # НАСТРОЙКИ/GSM - SIM APN
    def tooltip_settings_gsm_sim_1_apn_input(self):
        self.assert_tooltip_messege(locator=GSM_sim_1_APN_input,
                                    text=input_APN)

    def tooltip_settings_gsm_sim_2_apn_input(self):
        self.assert_tooltip_messege(locator=GSM_sim_2_APN_input,
                                    text=input_APN)

    # НАСТРОЙКИ/GSM - SIM user
    def tooltip_settings_gsm_sim_1_user_input(self):
        self.assert_tooltip_messege(locator=GSM_sim_1_user_input,
                                    text=input_sim_user)

    def tooltip_settings_gsm_sim_2_user_input(self):
        self.assert_tooltip_messege(locator=GSM_sim_2_user_input,
                                    text=input_sim_user)

    # НАСТРОЙКИ/GSM - SIM password
    def tooltip_settings_gsm_sim_1_password_input(self):
        self.assert_tooltip_messege(locator=GSM_sim_1_password_input,
                                    text=input_sim_password)

    def tooltip_settings_gsm_sim_2_password_input(self):
        self.assert_tooltip_messege(locator=GSM_sim_2_password_input,
                                    text=input_sim_password)

    # НАСТРОЙКИ/Ethernet - MAC адрес - поле ввода
    def tooltip_settings_ethernet_MAC_address_input(self):
        self.assert_tooltip_messege(locator=Ethernet_MAC_address_input,
                                    text=input_mac_address)

    # НАСТРОЙКИ/Ethernet - Название сервера - поле ввода
    def tooltip_settings_ethernet_Server_name_input(self):
        self.assert_tooltip_messege(locator=Ethernet_Server_name_input,
                                    text=input_server_name)

    # НАСТРОЙКИ/Ethernet - Адрес IPv4 - поле ввода
    def tooltip_settings_ethernet_IPv4_address_input(self):
        self.assert_tooltip_messege(locator=Ethernet_IPv4_address_input,
                                    text=input_ipV4_necessary)

    # НАСТРОЙКИ/Ethernet - Маска подсети - поле ввода
    def tooltip_settings_ethernet_Subnet_mask_input(self):
        self.assert_tooltip_messege(locator=Ethernet_Subnet_mask_input,
                                    text=input_ipV4_necessary)

    # НАСТРОЙКИ/Ethernet - Основной шлюз - поле ввода
    def tooltip_settings_ethernet_Main_gate_input(self):
        self.assert_tooltip_messege(locator=Ethernet_Main_gate_input,
                                    text=input_ipV4_necessary)

    # НАСТРОЙКИ/Ethernet - Предпочтительный DNS сервер - поле ввода
    def tooltip_settings_ethernet_Preferred_DNS_Server_input(self):
        self.assert_tooltip_messege(locator=Ethernet_Preferred_DNS_Server_input,
                                    text=input_ipV4_necessary)

    # НАСТРОЙКИ/Ethernet - Альтернативный DNS сервер - поле ввода
    def tooltip_settings_ethernet_Alternative_DNS_Server_input(self):
        self.assert_tooltip_messege(locator=Ethernet_Alternative_DNS_Server_input,
                                    text=input_ipV4_no_necessary)

    # НАСТРОЙКИ/Ethernet - Локальный IPv6 адрес - поле ввода
    def tooltip_settings_ethernet_Local_IPv6_address_input(self):
        self.assert_tooltip_messege(locator=Ethernet_Local_IPv6_address_input,
                                    text=input_ipV6)

    # НАСТРОЙКИ/Ethernet - Глобальный IPv6 адрес - поле ввода
    def tooltip_settings_ethernet_Global_IPv6_Address_input(self):
        self.assert_tooltip_messege(locator=Ethernet_Global_IPv6_Address_input,
                                    text=input_ipV6)

    # НАСТРОЙКИ/Ethernet - Предпочтительный IPv6 DNS сервер - поле ввода
    def tooltip_settings_ethernet_Preferred_IPv6_DNS_Server_input(self):
        self.assert_tooltip_messege(locator=Ethernet_Preferred_IPv6_DNS_Server_input,
                                    text=input_ipV6)

    # НАСТРОЙКИ/Ethernet  - Альтернативный IPv6 DNS сервер - поле ввода
    def tooltip_settings_ethernet_Alternative_IPv6_DNS_Server_input(self):
        self.assert_tooltip_messege(locator=Ethernet_Alternative_IPv6_DNS_Server_input,
                                    text=input_ipV6)

    # ПОЛЬЗОВАТЕЛИ И КЛЮЧИ/ПОЛЬЗОВАТЕЛИ - Администратор
    def tooltip_user_keys_administrator(self):
        self.assert_tooltip_messege(locator=user_administrator, text=text_U_K_user_administrator)

    # ПОЛЬЗОВАТЕЛИ И КЛЮЧИ/ПОЛЬЗОВАТЕЛИ - Режим Эгида3
    def tooltip_user_keys_user_egida3(self):
        self.assert_tooltip_messege(locator=user_egida3, text=text_U_K_user_egida3)

    # ПОЛЬЗОВАТЕЛИ И КЛЮЧИ/ПОЛЬЗОВАТЕЛИ - Имя пользователя
    def tooltip_user_keys_user_name(self):
        self.assert_tooltip_messege(locator=user_name, text=text_U_K_user_name)

    def tooltip_user_keys_user_name_input(self):
        self.assert_tooltip_messege(locator=user_name_input, text=input_63)

    # ПОЛЬЗОВАТЕЛИ И КЛЮЧИ/ПОЛЬЗОВАТЕЛИ - Логин
    def tooltip_user_keys_user_login(self):
        self.assert_tooltip_messege(locator=user_login, text=text_U_K_user_login)

    def tooltip_user_keys_user_login_input(self):
        self.assert_tooltip_messege(locator=user_login_input, text=input_login)

    # ПОЛЬЗОВАТЕЛИ И КЛЮЧИ/ПОЛЬЗОВАТЕЛИ - Пароль
    def tooltip_user_keys_user_password(self):
        self.assert_tooltip_messege(locator=user_password, text=text_U_K_user_password)

    def tooltip_user_keys_user_password_input(self):
        self.assert_tooltip_messege(locator=user_password_input, text=input_password_necessary)

    # ПОЛЬЗОВАТЕЛИ И КЛЮЧИ/ПОЛЬЗОВАТЕЛИ - Повторите пароль
    def tooltip_user_keys_user_rep_password(self):
        self.assert_tooltip_messege(locator=user_rep_password, text=text_U_K_user_rep_password)

    def tooltip_user_keys_user_rep_password_input(self):
        self.assert_tooltip_messege(locator=user_rep_password_input, text=input_password_necessary)

    # ПОЛЬЗОВАТЕЛИ И КЛЮЧИ/ПОЛЬЗОВАТЕЛИ - Перенаправление сообщений оператора
    def tooltip_user_keys_user_operator_message_forwarding(self):
        self.assert_tooltip_messege(locator=user_operator_message_forwarding,
                                    text=text_U_K_user_operator_message_forwarding)

    # ПОЛЬЗОВАТЕЛИ И КЛЮЧИ/ПОЛЬЗОВАТЕЛИ - Отправка вне трансляции
    def tooltip_user_keys_user_sending_out_of_broadcast(self):
        self.assert_tooltip_messege(locator=user_sending_out_of_broadcast, text=text_U_K_user_sending_out_of_broadcast)

    # ПОЛЬЗОВАТЕЛИ И КЛЮЧИ/ПОЛЬЗОВАТЕЛИ - Группа выходов с управлением по SMS
    def tooltip_user_keys_user_group_of_outputs_controlled_by_SMS(self):
        self.assert_tooltip_messege(locator=user_group_of_outputs_controlled_by_SMS,
                                    text=text_U_K_user_group_of_outputs_controlled_by_SMS)

    # ПОЛЬЗОВАТЕЛИ И КЛЮЧИ/ПОЛЬЗОВАТЕЛИ - Группа выходов с управлением звонком
    def tooltip_user_keys_user_group_of_outputs_with_call_control(self):
        self.assert_tooltip_messege(locator=user_group_of_outputs_with_call_control,
                                    text=text_U_K_user_group_of_outputs_with_call_control)

    # ПОЛЬЗОВАТЕЛИ И КЛЮЧИ/ПОЛЬЗОВАТЕЛИ - Разрешить снятие по SMS
    def tooltip_user_keys_user_allow_withdrawal_by_SMS(self):
        self.assert_tooltip_messege(locator=user_allow_withdrawal_by_SMS, text=text_U_K_user_allow_withdrawal_by_SMS)

    # ПОЛЬЗОВАТЕЛИ И КЛЮЧИ/ПОЛЬЗОВАТЕЛИ - Разрешить взятие по SMS
    def tooltip_user_keys_user_allow_pickup_by_SMS(self):
        self.assert_tooltip_messege(locator=user_allow_pickup_by_SMS, text=text_U_K_user_allow_pickup_by_SMS)

    # ПОЛЬЗОВАТЕЛИ И КЛЮЧИ/ПОЛЬЗОВАТЕЛИ - Телефон
    def tooltip_user_keys_user_phone(self):
        self.assert_tooltip_messege(locator=user_phone, text=text_U_K_user_hone)

    def tooltip_user_keys_user_phone_input_cod(self):
        self.assert_tooltip_messege(locator=user_phone_cod, text=input_phone_text_necessary)

    def tooltip_user_keys_user_phone_input_number(self):
        self.assert_tooltip_messege(locator=user_phone_number, text=input_phone_text_necessary)

    # ПОЛЬЗОВАТЕЛИ И КЛЮЧИ/ПОЛЬЗОВАТЕЛИ - Пароль SMS
    def tooltip_user_keys_user_password_sms(self):
        self.assert_tooltip_messege(locator=user_password_sms, text=text_U_K_user_password_sms)

    def tooltip_user_keys_user_password_sms_input(self):
        self.assert_tooltip_messege(locator=user_password_sms_input, text=input_password_5)

    # ПОЛЬЗОВАТЕЛИ И КЛЮЧИ/ПОЛЬЗОВАТЕЛИ - Повторите пароль SMS
    def tooltip_user_keys_user_rep_password_sms(self):
        self.assert_tooltip_messege(locator=user_rep_password_sms, text=text_U_K_user_rep_password_sms)

    def tooltip_user_keys_user_rep_password_sms_input(self):
        self.assert_tooltip_messege(locator=user_rep_password_sms_input, text=input_password_5)

    # ПОЛЬЗОВАТЕЛИ И КЛЮЧИ/ПОЛЬЗОВАТЕЛИ - Управляемые по SMS разделы
    def tooltip_user_keys_user_SMS_controlled_sections(self):
        self.assert_tooltip_messege(locator=user_SMS_controlled_sections, text=text_U_K_user_SMS_controlled_sections)

    # ПОЛЬЗОВАТЕЛИ И КЛЮЧИ/КЛЮЧИ - ID
    def tooltip_user_keys_keys_id(self):
        self.assert_tooltip_messege(locator=keys_id, text=text_U_K_keys_id)

    def tooltip_user_keys_keys_id_input(self):
        self.assert_tooltip_messege(locator=keys_id_input, text=input_key_12)

    # ПОЛЬЗОВАТЕЛИ И КЛЮЧИ/КЛЮЧИ - Пользователь
    def tooltip_user_keys_keys_user(self):
        self.assert_tooltip_messege(locator=keys_user, text=text_U_K_keys_user)

    # ПОЛЬЗОВАТЕЛИ И КЛЮЧИ/КЛЮЧИ - Разрешения
    def tooltip_user_keys_keys_permissions(self):
        self.assert_tooltip_messege(locator=keys_permissions, text=text_U_K_keys_permissions)

    # ПОЛЬЗОВАТЕЛИ И КЛЮЧИ/КЛЮЧИ - Разделы
    def tooltip_user_keys_keys_path(self):
        self.assert_tooltip_messege(locator=keys_path, text=text_U_K_keys_path)

    # Зоны/Разделы/Разделы - Номер
    def tooltip_path_number(self):
        self.assert_tooltip_messege(locator=path_number, text=text_path_number)

    def tooltip_path_number_input(self):
        self.assert_tooltip_messege(locator=path_number_input, text=input_numbers_0_9999)

    # Зоны/Разделы/Разделы - Название
    def tooltip_path_name(self):
        self.assert_tooltip_messege(locator=path_name, text=text_path_name)

    def tooltip_path_name_input(self):
        self.assert_tooltip_messege(locator=path_name_input, text=input_name_31)

    # Зоны/Разделы/Разделы - Управляющие разделы
    def tooltip_path_control_sections(self):
        self.assert_tooltip_messege(locator=path_control_sections, text=text_path_control_sections)

    # Зоны/Разделы/Разделы - Задержка взятия
    def tooltip_path_take_delay(self):
        self.assert_tooltip_messege(locator=path_take_delay, text=text_path_take_delay)

    # Зоны/Разделы/Разделы - Автовзятие из невзятия
    def tooltip_path_auto_pickup_from_non_pickup(self):
        self.assert_tooltip_messege(locator=path_auto_pickup_from_non_pickup,
                                    text=text_path_auto_pickup_from_non_pickup)

    # Зоны/Разделы/Разделы - Автовзятие из тревоги
    def tooltip_path_auto_arm_from_alarm(self):
        self.assert_tooltip_messege(locator=path_auto_arm_from_alarm, text=text_path_auto_arm_from_alarm)

    # Направления - Название
    def tooltip_directions_name(self):
        self.assert_tooltip_messege(locator=directions_name, text=text_directions_name)

    def tooltip_directions_name_input(self):
        self.assert_tooltip_messege(locator=directions_name_input, text=input_name_63)

    # Направления - Номер телефона - код
    def tooltip_directions_phone_cod_input(self):
        self.assert_tooltip_messege(locator=directions_phone_cod, text=input_phone_text_no_necessary)

    def tooltip_directions_phone_cod_input_rezerv_1(self):
        self.assert_tooltip_messege(locator=directions_phone_cod_rezerv_1, text=input_phone_text_no_necessary)

    def tooltip_directions_phone_cod_input_rezerv_2(self):
        self.assert_tooltip_messege(locator=directions_phone_cod_rezerv_2, text=input_phone_text_no_necessary)

    # Направления - Номер телефона - номер
    def tooltip_directions_phone_number_input(self):
        self.assert_tooltip_messege(locator=directions_phone_number, text=input_phone_text_no_necessary)

    def tooltip_directions_phone_number_input_rezerv_1(self):
        self.assert_tooltip_messege(locator=directions_phone_number_rezerv_1, text=input_phone_text_no_necessary)

    def tooltip_directions_phone_number_input_rezerv_2(self):
        self.assert_tooltip_messege(locator=directions_phone_number_rezerv_2, text=input_phone_text_no_necessary)

    # Направления - Разделы
    def tooltip_directions_path(self):
        self.assert_tooltip_messege(locator=directions_path, text=text_directions_path)

    # Направления - Тип управления
    def tooltip_directions_control_type(self):
        self.assert_tooltip_messege(locator=directions_control_type, text=text_directions_control_type)

    # Направления - Текущий пользователь
    def tooltip_directions_current_user(self):
        self.assert_tooltip_messege(locator=directions_current_user, text=text_directions_current_user)

    def tooltip_directions_current_user_rezerv_1(self):
        self.assert_tooltip_messege(locator=directions_current_user_rezerv_1, text=text_directions_current_user)

    def tooltip_directions_current_user_rezerv_2(self):
        self.assert_tooltip_messege(locator=directions_current_user_rezerv_2, text=text_directions_current_user)

    # Направления - Отправлять время события
    def tooltip_directions_send_event_time(self):
        self.assert_tooltip_messege(locator=directions_send_event_time, text=text_directions_send_event_time)

    def tooltip_directions_send_event_time_rezerv_1(self):
        self.assert_tooltip_messege(locator=directions_send_event_time_rezerv_1, text=text_directions_send_event_time)

    def tooltip_directions_send_event_time_rezerv_2(self):
        self.assert_tooltip_messege(locator=directions_send_event_time_rezerv_2, text=text_directions_send_event_time)

    # Направления - Отправлять дату события
    def tooltip_directions_send_event_date(self):
        self.assert_tooltip_messege(locator=directions_send_event_date, text=text_directions_send_event_date)

    def tooltip_directions_send_event_date_rezerv_1(self):
        self.assert_tooltip_messege(locator=directions_send_event_date_rezerv_1, text=text_directions_send_event_date)

    def tooltip_directions_send_event_date_rezerv_2(self):
        self.assert_tooltip_messege(locator=directions_send_event_date_rezerv_2, text=text_directions_send_event_date)

    # Направления - Включить тестирование канала
    def tooltip_directions_enable_channel_testing(self):
        self.assert_tooltip_messege(locator=directions_enable_channel_testing,
                                    text=text_directions_enable_channel_testing)

    def tooltip_directions_enable_channel_testing_rezerv_1(self):
        self.assert_tooltip_messege(locator=directions_enable_channel_testing_rezerv_1,
                                    text=text_directions_enable_channel_testing)

    def tooltip_directions_enable_channel_testing_rezerv_2(self):
        self.assert_tooltip_messege(locator=directions_enable_channel_testing_rezerv_2,
                                    text=text_directions_enable_channel_testing)

    # Направления - Таймаут при ошибке
    def tooltip_directions_timeout_on_error(self):
        self.assert_tooltip_messege(locator=directions_timeout_on_error, text=text_directions_timeout_on_error)

    def tooltip_directions_timeout_on_error_rezerv_1(self):
        self.assert_tooltip_messege(locator=directions_timeout_on_error_rezerv_1, text=text_directions_timeout_on_error)

    def tooltip_directions_timeout_on_error_rezerv_2(self):
        self.assert_tooltip_messege(locator=directions_timeout_on_error_rezerv_2, text=text_directions_timeout_on_error)

    def tooltip_directions_timeout_on_error_input(self):
        self.assert_tooltip_messege(locator=directions_timeout_on_error_input, text=input_00_05__23_59)

    def tooltip_directions_timeout_on_error_input_rezerv_1(self):
        self.assert_tooltip_messege(locator=directions_timeout_on_error_input_rezerv_1, text=input_00_05__23_59)

    def tooltip_directions_timeout_on_error_input_rezerv_2(self):
        self.assert_tooltip_messege(locator=directions_timeout_on_error_input_rezerv_2, text=input_00_05__23_59)

    # Направления - Тестировать если
    def tooltip_directions_test_if(self):
        self.assert_tooltip_messege(locator=directions_test_if, text=text_directions_test_if)

    def tooltip_directions_test_if_rezerv_1(self):
        self.assert_tooltip_messege(locator=directions_test_if_rezerv_1, text=text_directions_test_if)

    def tooltip_directions_test_if_rezerv_2(self):
        self.assert_tooltip_messege(locator=directions_test_if_rezerv_2, text=text_directions_test_if)

    # Направления - Метод тестирования
    def tooltip_directions_test_method(self):
        self.assert_tooltip_messege(locator=directions_test_method, text=text_directions_test_method)

    def tooltip_directions_test_method_rezerv_1(self):
        self.assert_tooltip_messege(locator=directions_test_method_rezerv_1, text=text_directions_test_method)

    def tooltip_directions_test_method_rezerv_2(self):
        self.assert_tooltip_messege(locator=directions_test_method_rezerv_2, text=text_directions_test_method)

    # Направления - Тестировать
    def tooltip_directions_test(self):
        self.assert_tooltip_messege(locator=directions_test, text=text_directions_test)

    def tooltip_directions_test_rezerv_1(self):
        self.assert_tooltip_messege(locator=directions_test_rezerv_1, text=text_directions_test)

    def tooltip_directions_test_rezerv_2(self):
        self.assert_tooltip_messege(locator=directions_test_rezerv_2, text=text_directions_test)

    # Направления - Дни недели
    def tooltip_directions_days_of_th_week(self):
        self.assert_tooltip_messege(locator=directions_days_of_th_week, text=text_directions_days_of_th_week)

    def tooltip_directions_days_of_th_week_rezerv_1(self):
        self.assert_tooltip_messege(locator=directions_days_of_th_week_rezerv_1, text=text_directions_days_of_th_week)

    def tooltip_directions_days_of_th_week_rezerv_2(self):
        self.assert_tooltip_messege(locator=directions_days_of_th_week_rezerv_2, text=text_directions_days_of_th_week)

    # Направления - Количество повторов
    def tooltip_directions_number_of_repetitions(self):
        self.assert_tooltip_messege(locator=directions_number_of_repetitions,
                                    text=text_directions_number_of_repetitions)

    def tooltip_directions_number_of_repetitions_rezerv_1(self):
        self.assert_tooltip_messege(locator=directions_number_of_repetitions_rezerv_1,
                                    text=text_directions_number_of_repetitions)

    def tooltip_directions_number_of_repetitions_rezerv_2(self):
        self.assert_tooltip_messege(locator=directions_number_of_repetitions_rezerv_2,
                                    text=text_directions_number_of_repetitions)

    def tooltip_directions_number_of_repetitions_input(self):
        self.assert_tooltip_messege(locator=directions_number_of_repetitions_input,
                                    text=input_0_65535_not_necessary)

    def tooltip_directions_number_of_repetitions_input_rezerv_1(self):
        self.assert_tooltip_messege(locator=directions_number_of_repetitions_input_rezerv_1,
                                    text=input_0_65535_not_necessary)

    def tooltip_directions_number_of_repetitions_input_rezerv_2(self):
        self.assert_tooltip_messege(locator=directions_number_of_repetitions_input_rezerv_2,
                                    text=input_0_65535_not_necessary)

    # Направления - Адрес
    def tooltip_directions_address(self):
        self.assert_tooltip_messege(locator=directions_address, text=text_directions_address)

    def tooltip_directions_address_rezerv_1(self):
        self.assert_tooltip_messege(locator=directions_address_rezerv_1, text=text_directions_address)

    def tooltip_directions_address_rezerv_2(self):
        self.assert_tooltip_messege(locator=directions_address_rezerv_2, text=text_directions_address)

    def tooltip_directions_address_input(self):
        self.assert_tooltip_messege(locator=directions_address_input, text=input_hostname)

    def tooltip_directions_address_input_rezerv_1(self):
        self.assert_tooltip_messege(locator=directions_address_input_rezerv_1, text=input_hostname)

    def tooltip_directions_address_input_rezerv_2(self):
        self.assert_tooltip_messege(locator=directions_address_input_rezerv_2, text=input_hostname)

    # Направления - Порт
    def tooltip_directions_port(self):
        self.assert_tooltip_messege(locator=directions_port, text=text_directions_port)

    def tooltip_directions_port_rezerv_1(self):
        self.assert_tooltip_messege(locator=directions_port_rezerv_1, text=text_directions_port)

    def tooltip_directions_port_rezerv_2(self):
        self.assert_tooltip_messege(locator=directions_port_rezerv_2, text=text_directions_port)

    def tooltip_directions_port_input(self):
        self.assert_tooltip_messege(locator=directions_port_input, text=input_0_65535_not_necessary)

    def tooltip_directions_port_input_rezerv_1(self):
        self.assert_tooltip_messege(locator=directions_port_input_rezerv_1, text=input_0_65535_not_necessary)

    def tooltip_directions_port_input_rezerv_2(self):
        self.assert_tooltip_messege(locator=directions_port_input_rezerv_2, text=input_0_65535_not_necessary)

    # Направления - Канал соединения
    def tooltip_directions_connection_channel(self):
        self.assert_tooltip_messege(locator=directions_connection_channel, text=text_directions_connection_channel)

    def tooltip_directions_connection_channel_rezerv_1(self):
        self.assert_tooltip_messege(locator=directions_connection_channel_rezerv_1,
                                    text=text_directions_connection_channel)

    def tooltip_directions_connection_channel_rezerv_2(self):
        self.assert_tooltip_messege(locator=directions_connection_channel_rezerv_2,
                                    text=text_directions_connection_channel)

    # Направления - Таймаут подтверждения, сек
    def tooltip_directions_confirmation_timeout_sec(self):
        self.assert_tooltip_messege(locator=directions_confirmation_timeout_sec,
                                    text=text_directions_confirmation_timeout_sec)

    def tooltip_directions_confirmation_timeout_sec_rezerv_1(self):
        self.assert_tooltip_messege(locator=directions_confirmation_timeout_sec_rezerv_1,
                                    text=text_directions_confirmation_timeout_sec)

    def tooltip_directions_confirmation_timeout_sec_rezerv_2(self):
        self.assert_tooltip_messege(locator=directions_confirmation_timeout_sec_rezerv_2,
                                    text=text_directions_confirmation_timeout_sec)

    def tooltip_directions_confirmation_timeout_sec_input(self):
        self.assert_tooltip_messege(locator=directions_confirmation_timeout_sec_input,
                                    text=input_0_99)

    def tooltip_directions_confirmation_timeout_sec_input_rezerv_1(self):
        self.assert_tooltip_messege(locator=directions_confirmation_timeout_sec_input_rezerv_1,
                                    text=input_0_99)

    def tooltip_directions_confirmation_timeout_sec_input_rezerv_2(self):
        self.assert_tooltip_messege(locator=directions_confirmation_timeout_sec_input_rezerv_2,
                                    text=input_0_99)

    # Направления - Количество повторов
    def tooltip_directions_number_of_repetitions_DC09(self):
        self.assert_tooltip_messege(locator=directions_number_of_repetitions_DC09,
                                    text=text_directions_number_of_repetitions_DC09)

    def tooltip_directions_number_of_repetitions_DC09_rezerv_1(self):
        self.assert_tooltip_messege(locator=directions_number_of_repetitions_DC09_rezerv_1,
                                    text=text_directions_number_of_repetitions_DC09)

    def tooltip_directions_number_of_repetitions_DC09_rezerv_2(self):
        self.assert_tooltip_messege(locator=directions_number_of_repetitions_DC09_rezerv_2,
                                    text=text_directions_number_of_repetitions_DC09)

    def tooltip_directions_number_of_repetitions_DC09_input(self):
        self.assert_tooltip_messege(locator=directions_number_of_repetitions_DC09_input,
                                    text=input_0_65535_not_necessary)

    # Направления - Шифрование
    def tooltip_directions_encryption(self):
        self.assert_tooltip_messege(locator=directions_encryption, text=text_directions_encryption)

    def tooltip_directions_encryption_rezerv_1(self):
        self.assert_tooltip_messege(locator=directions_encryption_rezerv_1, text=text_directions_encryption)

    def tooltip_directions_encryption_rezerv_2(self):
        self.assert_tooltip_messege(locator=directions_encryption_rezerv_2, text=text_directions_encryption)

    # Направления - Ключ шифрования
    def tooltip_directions_encryption_keyn(self):
        self.assert_tooltip_messege(locator=directions_encryption_key, text=text_directions_encryption_key)

    def tooltip_directions_encryption_keyn_rezerv_1(self):
        self.assert_tooltip_messege(locator=directions_encryption_key_rezerv_1, text=text_directions_encryption_key)

    def tooltip_directions_encryption_keyn_rezerv_2(self):
        self.assert_tooltip_messege(locator=directions_encryption_key_rezerv_2, text=text_directions_encryption_key)
