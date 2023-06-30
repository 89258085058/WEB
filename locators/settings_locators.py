# -*- coding: utf-8 -*-

"""ОБЪЕКТ"""
# ------------ПОЛЯ ВВОДА------------
# Название объекта
object_name = '//*[.="Название объекта"]/following::input[1]'
object_name_error = '//*[.="Название объекта"]//input[contains(@class, "error")]'
# Номер объекта
object_number = '//*[.="Номер объекта"]/following::input[1]'
# Задержка взятия
object_delay_take_on = '//*[.="Задержка взятия"]/following::input[1]'
# Задержка тревоги входа
object_delay_alarm_enter = '//*[.="Задержка тревоги входа"]/following::input[1]'
# Время автовзятия
object_time_auto_take_on = '//*[.="Время автовзятия"]/following::input[1]'
# ------------ЧЕКБОКСЫ-------------
# Тревога при потере датчика
object_sensor_loss_alarm_click = '(//*[@id="app"]//label/span)[1]'
object_sensor_loss_alarm_status = '(//*[@id="app"]//label/input)[1]'
# Взятие при потерянных датчиках
object_taking_with_lost_sensors_click = '(//*[@id="app"]//label/span)[2]'
object_taking_with_lost_sensors_status = '(//*[@id="app"]//label/input)[2]'
# Взятие при датчиках в тревоге
object_taking_sensors_in_alarm_click = '(//*[@id="app"]//label/span)[3]'
object_taking_sensors_in_alarm_status = '(//*[@id="app"]//label/input)[3]'
# Взятие при датчиках в неисправности
object_capturing_with_sensors_in_error_click = '(//*[@id="app"]//label/span)[3]'
object_capturing_with_sensors_in_error_status = '(//*[@id="app"]//label/input)[3]'
# Принудительное взятие из тревоги
object_forced_take_from_alarm_click = '(//*[@id="app"]//label/span)[4]'
object_forced_take_from_alarm_status = '(//*[@id="app"]//label/input)[4]'
# ------------ТЕКСТ-------------------
object_text = '//div[@class="settings-object"]'
# ------------КНОПКИ------------------
# Кнопка сохранить
save_button = '//*[@id="app"]//button[.=" Сохранить "]'
# Кнопка редактировать
edit_button = '//*[@id="app"]//button[.=" Редактировать "]'
# Кнопка редактировать
reset_button = '//*[@id="app"]//button[.=" Сбросить "]'

"""ДАТА И ВРЕМЯ"""
# ------------ТЕКСТ__________________
data_time_text = '//div[@class="settings-datetime"]'
# ------------ВЫПАДАЮЩИЙ СПИСОК-----
# Дата и время на устройстве
date_time_dropdown_1 = '(//*[@id="app"]/main//span[@class="label"])[1]'
# Использовать время GSM сети
Use_GSM_network_time = '(/html/body//div[@class="option"])[1]'
# Синхронизация по NTP/HTP
Synchronization_via_NTP_HTP = '(/html/body//div[@class="option"])[2]'
# Вручную
Manually = '(/html/body//div[@class="option"])[3]'
# Часовой пояс
date_time_dropdown_2 = '(//*[@id="app"]/main//span[@class="label"])[2]'
utc = '(/html/body//div[@class="option"])'
# ------------ЧЕКБОКСЫ-------------
# Использовать временную зону GSM сети
Use_time_zone_of_GSM_network_click = '//*[.="Использовать временную зону GSM сети"]//label/span'
Use_time_zone_of_GSM_network_status = '//*[.="Использовать временную зону GSM сети"]//label/input'
# Переход на летнее время
Daylight_Saving_Time_click = '//*[.="Переход на летнее время"]//label/span'
Daylight_Saving_Time_status = '//*[.="Переход на летнее время"]//label/input'
# ------------ПОЛЯ ВВОДА------------
# Адрес сервера
address_server_data_time = '(//*[.="Адрес сервера"]/following::input[1])[1]'
# ------------КАЛЕНДАРЬ-------------
data = '//div[@class="dp__calendar_wrap"]'

"""ПРИБОР"""
# ------------ТЕКСТ__________________
device_text = '//div[@class="settings-device"]'
# ------------ЧЕКБОКСЫ-------------
# Включить энергосберегающий режим
enable_power_saving_mode_click = '//*[.="Включить энергосберегающий режим"]//label/span'
enable_power_saving_mode_status = '//*[.="Включить энергосберегающий режим"]//label/input'
# Разрешить настройку при закрытом корпусе
allow_configuration_when_the_case_is_closed_click = '//*[.="Разрешить настройку при закрытом корпусе"]//label/span'
allow_configuration_when_the_case_is_closed_status = '//*[.="Разрешить настройку при закрытом корпусе"]//label/input'
# Фиксировать повторные тревоги раздела
fix_partition_repeated_alarms_click = '//*[.="Фиксировать повторные тревоги раздела"]//label/span'
fix_partition_repeated_alarms_status = '//*[.="Фиксировать повторные тревоги раздела"]//label/input'
# Фиксировать повторные тревоги датчика
fix_repeated_sensor_alarms_click = '//*[.="Фиксировать повторные тревоги датчика"]//label/span'
fix_repeated_sensor_alarms_status = '//*[.="Фиксировать повторные тревоги датчика"]//label/input'
# Фиксировать повторные пожарные тревоги раздела
fix_repeated_fire_alarms_in_a_section_click = '//*[.="Фиксировать повторные пожарные тревоги раздела"]//label/span'
fix_repeated_fire_alarms_in_a_section_status = '//*[.="Фиксировать повторные пожарные тревоги раздела"]//label/input'
# Фиксировать повторные пожарные тревоги датчика
fix_repeated_fire_alarms_of_the_sensor_click = '//*[.="Фиксировать повторные пожарные тревоги датчика"]//label/span'
fix_repeated_fire_alarms_of_the_sensor_status = '//*[.="Фиксировать повторные пожарные тревоги датчика"]//label/input'
# Фиксировать повторные события взятия/снятия
fix_repeated_arming_disarming_events_click = '//*[.="Фиксировать повторные события взятия/снятия"]//label/span'
fix_repeated_arming_disarming_events_status = '//*[.="Фиксировать повторные события взятия/снятия"]//label/input'
# Управлять выходами при повторном взятии/снятии
control_exits_when_re_arming_disarming_click = '//*[.="Управлять выходами при повторном взятии/снятии"]//label/span'
control_exits_when_re_arming_disarming_status = '//*[.="Управлять выходами при повторном взятии/снятии"]//label/input'

"""Световая индикация"""
# ------------ТЕКСТ__________________
light_indication_text = '//div[@class="settings-led"]'
# ------------ЧЕКБОКСЫ-------------
# Инверсия индикации считывателя
reader_indication_inversion_click = '//*[.="Инверсия индикации считывателя"]//label/span'
reader_indication_inversion_status = '//*[.="Инверсия индикации считывателя"]//label/input'
# ------------ВЫПАДАЮЩИЙ СПИСОК-----
options = '(/html/body//div[@class="option"])'
# Режим светодиодов для охранных датчиков
LED_mode_for_security_sensors = '(//*[@id="app"]//span[@class="label"])[1]'
# Режим светодиодов для пожарных датчиков
LED_mode_for_fire_detectors = '(//*[@id="app"]//span[@class="label"])[2]'
# Режим светодиодов для технологических датчиков
LED_mode_for_process_sensors = '(//*[@id="app"]//span[@class="label"])[3]'
# Режим работы считывателя
Reader_operation_mode = '(//*[@id="app"]//span[@class="label"])[4]'

"""РАДИО"""
# ------------ТЕКСТ__________________
radio_text = '//div[@class="device-settings-wrapper card"]'
# ------------ПОЛЯ ВВОДА------------
# Время разрешения добавления новых датчиков
resolution_time_for_adding_new_sensors = '(//*[.="Время разрешения добавления новых датчиков"]/following::input[1])[1]'
# Период опроса датчиков
# sensor_polling_period = '//*[.="Период опроса датчиков"]/following::input[1]'
# ------------ЧЕКБОКСЫ-------------
# Включить радиомодуль
radio_modul_on_click = '(//*[@id="app"]//label/span)[1]'
radio_modul_on_status = '(//*[@id="app"]//label/input)[1]'
# ------------ВЫПАДАЮЩИЙ СПИСОК-----
# Кнопка выпадающего списка Канал
radio_chanel_button = '(//*[@id="app"]//span[@class="label"])[1]'
radio_device_button = '(//*[@id="app"]//span[@class="label"])[2]'
# Канал
radio_chanel = '(/html/body//div[@class="option"])'

"""ETHERNET"""
# ------------ТЕКСТ__________________
ethernet_text = '//div[@class="settings-ethernet"]'
# ------------ПОЛЯ ВВОДА------------
# MAC адрес
ethernet_mac_address = '(//*[.="MAC адрес"]/following::input[1])[1]'
# Название сервера
ethernet_name_server = '(//*[.="Название сервера"]/following::input[1])[1]'
# Адрес IPv4
ethernet_address_IPv4 = '(//*[.="Адрес IPv4"]/following::input[1])[1]'
# Маска подсети
ethernet_subnet_mask = '(//*[.="Маска подсети"]/following::input[1])[1]'
# Основной шлюз
ethernet_main_gate = '(//*[.="Основной шлюз"]/following::input[1])[1]'
# Предпочтительный DNS сервер
ethernet_preferred_DNS_server = '(//*[.="Предпочтительный DNS сервер"]/following::input[1])[1]'
# Альтернативный DNS сервер
ethernet_alternative_DNS_server = '(//*[.="Альтернативный DNS сервер"]/following::input[1])[1]'
# Локальный IPv6 адрес
ethernet_local_ipv6 = '(//*[.="Локальный IPv6 адрес"]/following::input[1])[1]'
# Глобальный IPv6 адрес
ethernet_global_ipv6 = '(//*[.="Глобальный IPv6 адрес"]/following::input[1])[1]'
# Предпочтительный IPv6 DNS сервер
ethernet_preferred_IPv6_DNS_server = '(//*[.="Предпочтительный IPv6 DNS сервер"]/following::input[1])[1]'
# Альтернативный IPv6 DNS сервер
ethernet_alternative_IPv6_DNS_server = '(//*[.="Альтернативный IPv6 DNS сервер"]/following::input[1])[1]'
# Адреса маска под сети википедия
list_mask = ['0.0.0.0', '0.0.0.1', '0.0.0.3', '0.0.0.7', '0.0.0.15', '0.0.0.31', '0.0.0.63', '0.0.0.127',
             '0.0.0.255', '0.0.1.255', '0.0.3.255', '0.0.7.255', '0.0.15.255', '0.0.31.255', '0.0.63.255',
             '0.0.127.255', '0.0.255.255', '0.1.255.255', '0.3.255.255', '0.7.255.255', '0.15.255.255',
             '0.31.255.255', '0.63.255.255', '0.127.255.255', '0.255.255.255', '1.255.255.255',
             '3.255.255.255', '7.255.255.255', '15.255.255.255', '31.255.255.255', '63.255.255.255',
             '127.255.255.255', '255.255.255.255', '255.255.255.254', '255.255.255.252', '255.255.255.248',
             '255.255.255.240', '255.255.255.224', '255.255.255.192', '255.255.255.128', '255.255.255.0',
             '255.255.254.0', '255.255.252.0', '255.255.248.0', '255.255.240.0', '255.255.224.0',
             '255.255.192.0', '255.255.128.0', '255.255.0.0', '255.254.0.0', '255.252.0.0',
             '255.248.0.0', '255.240.0.0', '255.224.0.0', '255.192.0.0', '255.128.0.0',
             '255.0.0.0', '254.0.0.0', '252.0.0.0', '248.0.0.0', '240.0.0.0',
             '224.0.0.0', '192.0.0.0', '128.0.0.0', '0.0.0.0']
# Адреса ipv4 википедия
ip_list = ['0.0.0.0', '10.0.0.0', '100.64.0.0', '127.0.0.0', '169.254.0.0', '172.16.0.0', '172.16.0.0',
           '192.0.0.0', '192.0.0.170', '192.0.0.171', '192.0.2.0', '192.88.99.0', '192.88.99.1',
           '192.168.0.0', '198.51.100.0', '203.0.113.0', '224.0.0.0', '240.0.0.0', '255.255.255.255']
# Адреса ipv6 википедия
ip_v6_list = ['::', '::1', '::ffff:0:0:0:0', '::ffff:0:0:0:0:0', '64:ff9b::0:0:0:0', '100::', '2001::', '2001:20::',
              '2001:db8::', '2002::', 'feff::', 'fc00::', 'fe80::', 'ff00::',
              'ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff', '::ffff:255:255:255:255', '::ffff:0:255:255:255:255',
              '64:ff9b::255:255:255:255', '100::ffff:ffff:ffff:ffff', '2001::ffff:ffff:ffff:ffff:ffff:ffff',
              '2001:2f:ffff:ffff:ffff:ffff:ffff:ffff', '2001:db8:ffff:ffff:ffff:ffff:ffff:ffff',
              '2002:ffff:ffff:ffff:ffff:ffff:ffff:ffff', 'fec0:ffff:ffff:ffff:ffff:ffff:ffff:ffff',
              'fdff:ffff:ffff:ffff:ffff:ffff:ffff:ffff', 'febf:ffff:ffff:ffff:ffff:ffff:ffff:ffff',
              'ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff', '2403:6200:8862:2cb4::2',
              '2403:6200:8862:2cb4:bc07:bcb4:b7d0:24eb', 'fd14:9d09:d004:7e00:7462:9648:7bcd:20a8']
# ------------ЧЕКБОКСЫ-------------
# Получать IPv4 адрес и настройки автоматически
ethernet_obtain_IPv4_address_and_settings_automatically_click = '//*[.="Получать IPv4 адрес и настройки автоматически"]//label/span'
ethernet_obtain_IPv4_address_and_settings_automatically_status = '//*[.="Получать IPv4 адрес и настройки автоматически"]//label/input'
# Использовать как сервер
ethernet_use_as_server_click = '//*[.="Использовать как сервер"]//label/span'
ethernet_use_as_server_status = '//*[.="Использовать как сервер"]//label/input'
# Получать адрес IPv6 от DHCP автоматически
ethernet_obtain_an_IPv6_address_from_DHCP_automatically_click = '//*[.="Получать адрес IPv6 от DHCP автоматически"]//label/span'
ethernet_obtain_an_IPv6_address_from_DHCP_automatically_status = '//*[.="Получать адрес IPv6 от DHCP автоматически"]//label/input'
# Разрешить удаленное управление
ethernet_allow_remote_control_click = '//*[.="Разрешить удаленное управление"]//label/span'
ethernet_allow_remote_control_status = '//*[.="Разрешить удаленное управление"]//label/input'
# Получать адрес IPv6 от SLAAC автоматически
ethernet_obtain_an_IPv6_address_from_SLAAC_automatically_click = '//*[.="Получать адрес IPv6 от SLAAC автоматически"]//label/span'
ethernet_obtain_an_IPv6_address_from_SLAAC_automatically_status = '//*[.="Получать адрес IPv6 от SLAAC автоматически"]//label/input'
# Разрешить незащищенное HTTP-соединение
ethernet_allow_insecure_HTTP_connection_click = '//*[.="Разрешить незащищенное HTTP-соединение"]//label/span'
ethernet_allow_insecure_HTTP_connection_status = '//*[.="Разрешить незащищенное HTTP-соединение"]//label/input'
# ------------ВЫПАДАЮЩИЙ СПИСОК-----
# Кнопка выпадающего списка Устанавливать сетевые подключения через
ethernet_network_connections_button = '//*[@id="app"]//span[@class="label"]'
# Устанавливать сетевые подключения через выбор позиции
ethernet_network_connection_positions = '(/html/body//div[@class="option"])'

"""GSM"""
# ------------ТЕКСТ__________________
GSM_text = '//div[@class="settings-gsm"]'
GSM_SMS_modal_text = '//div[@class="modal card"]'
### Поля ввода ###
# Число знаков номера для проверки
number_of_digits_of_the_number_to_check = '(//*[.="Число знаков номера для проверки"]/following::input[1])[1]'
# Порог уведомления о балансе
balance_notification_threshold = '(//*[.="Порог уведомления о балансе"]/following::input[1])[1]'
# PIN -SIM_1
PIN_SIM_1 = '(//*[.="PIN"]/following::input[1])[1]'
# USSD -SIM_1
USSD_SIM_1 = '(//*[.="USSD-код запроса баланса"]/following::input[1])[1]'
# PIN -SIM_2
PIN_SIM_2 = '(//*[.="PIN"]/following::input[1])[3]'
# USSD -SIM_2
USSD_SIM_2 = '(//*[.="USSD-код запроса баланса"]/following::input[1])[3]'
# APN - SIM_1
APN_SIM_1 = '(//*[.="APN"]/following::input[1])[1]'
# APN - SIM_2
APN_SIM_2 = '(//*[.="APN"]/following::input[1])[3]'
# USER - SIM_1
USER_SIM_1 = '(//*[.="Пользователь"]/following::input[1])[1]'
# USER - SIM_2
USER_SIM_2 = '(//*[.="Пользователь"]/following::input[1])[3]'
# PASSWORD - SIM_1
PASSWORD_SIM_1 = '(//*[.="Пароль"]/following::input[1])[1]'
# PASSWORD - SIM_2
PASSWORD_SIM_2 = '(//*[.="Пароль"]/following::input[1])[3]'
# TELEPHONE
TEL_COD = '(/html/body//input[@placeholder="Код"])[2]'
TEL_NUM = '(/html/body//div/input[2])[2]'
# Сообщение
MESSEGE = '(//*[.="Сообщение"]/following::input[@type="text"])[4]'
# ------------КНОПКИ------------------
# SIM 1 - Проверить
button_verify_1 = '(//*[@id="app"]//button[.=" Проверить "])[1]'
# SIM 2 - Проверить
button_verify_2 = '(//*[@id="app"]//button[.=" Проверить "])[2]'
# SIM 2 - Проверить
button_cancel = '(//div[.=" Отменить "])[last()]'

# ------------ЧЕКБОКСЫ-------------
# Включить модуль GSM
gsm_Enable_GSM_module_click = '//*[.="Включить модуль GSM"]//label/span'
gsm_Enable_GSM_module_status = '//*[.="Включить модуль GSM"]//label/input'
# Использовать GPRS
gsm_Use_GPRS_click = '//*[.="Использовать GPRS"]//label/span'
gsm_Use_GPRS_status = '//*[.="Использовать GPRS"]//label/input'
# Использовать резервную SIM
gsm_Use_backup_SIM_click = '//*[.="Использовать резервную SIM"]//label/span'
gsm_Use_backup_SIM_status = '//*[.="Использовать резервную SIM"]//label/input'
# Разрешить USSD
gsm_Allow_USSD_click = '//*[.="Разрешить USSD"]//label/span'
gsm_Allow_USSD_status = '//*[.="Разрешить USSD"]//label/input'
# Разрешить трансляцию событий
gsm_Allow_Event_Broadcast_click = '//*[.="Разрешить трансляцию событий"]//label/span'
gsm_Allow_Event_Broadcast_status = '//*[.="Разрешить трансляцию событий"]//label/input'

"""ЗВУКОВАЯ ИНДИКАЦИЯ"""
# ------------ТЕКСТ__________________
volum_indication_text = '//div[@class="settings-beeper"]'
# Длительность сигнала
volum_indication_signal_duration = '(//*[.="Длительность сигнала"]/following::input[1])[1]'
# ------------ПОЛЗУНКИ_______________
# Громкость событий
event_volume_slider_widget = '//*[.="Громкость событий"]//input[1]'
# Громкость тревог
alarm_volume_slider_widget = '//*[.="Громкость тревог"]//input[1]'
# ------------КНОПКИ------------------
# Связанные события
button_related_events = '//*[.="Связанные события"]//i'
# ------------ЧЕКБОКСЫ-------------
# Включить
volum_on_click = '//*[.="Включить"]//label/span'
volum_on_status = '//*[.="Включить"]//label/input'
# Тревога
volum_alarm_click = '//*[.="Тревога"]//label/span'
volum_alarm_status = '//*[.="Тревога"]//label/input'
# Пожар
volum_fire_click = '//*[.="Пожар"]//label/span'
volum_fire_status = '//*[.="Пожар"]//label/input'
# Взятие раздела
volum_take_path_click = '//*[.="Взятие раздела"]//label/span'
volum_take_path_status = '//*[.="Взятие раздела"]//label/input'
# Снятие раздела
volum_take_off_path_click = '//*[.="Снятие раздела"]//label/span'
volum_take_off_path_status = '//*[.="Снятие раздела"]//label/input'
# Задержка взятия
volum_delay_take_click = '//*[.="Задержка взятия"]//label/span'
volum_delay_take_status = '//*[.="Задержка взятия"]//label/input'
# Невзятие
volum_no_take_click = '//*[.="Невзятие"]//label/span'
volum_no_take_status = '//*[.="Невзятие"]//label/input'
# Разделы частично взяты
volum_some_take_on_click = '//*[.="Разделы частично взяты"]//label/span'
volum_some_take_on_status = '//*[.="Разделы частично взяты"]//label/input'
# Добавление датчика
volum_add_sensor_click = '//*[.="Добавление датчика"]//label/span'
volum_add_sensor_status = '//*[.="Добавление датчика"]//label/input'
# Колокольчик
volum_bang_click = '//*[.="Колокольчик"]//label/span'
volum_bang_status = '//*[.="Колокольчик"]//label/input'
