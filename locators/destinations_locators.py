# -*- coding: utf-8 -*-

"""НАПРАВЛЕНИЯ"""
# ------------ПОЛЯ ВВОДА------------
# Настройки
destination_name = '//*[.="Название"]//input[1]'
# TELEPHONE
TEL_COD_main = '(//div[@class="channel-settings"])[1]//input[@placeholder="Код"]'
TEL_NUM_main = '((//div[@class="channel-settings"])[1]//input[2])'
TEL_COD_rezerv_1 = '(//div[@class="channel-settings"])[2]//input[@placeholder="Код"]'
TEL_NUM_rezerv_1 = '((//div[@class="channel-settings"])[2]//input[2])'
TEL_COD_rezerv_2 = '(//div[@class="channel-settings"])[3]//input[@placeholder="Код"]'
TEL_NUM_rezerv_2 = '((//div[@class="channel-settings"])[3]//input[2])'
# Количество повторов
count_reset_main = '(//*[.="Количество повторов"]//input)[1]'
count_reset_rezerv_1 = '(//*[.="Количество повторов"]//input)[2]'
count_reset_rezerv_2 = '(//*[.="Количество повторов"]//input)[3]'
# Таймаут при ошибке
Timeout_on_error_main = '(//*[.="Таймаут при ошибке"]//input)[1]'
Timeout_on_error_rezerv_1 = '(//*[.="Таймаут при ошибке"]//input)[2]'
Timeout_on_error_rezerv_2 = '(//*[.="Таймаут при ошибке"]//input)[3]'

# Интервал тестирования
Test_interval_main = '(//*[.="Интервал тестирования"]//input)[1]'
Test_interval_rezerv_1 = '(//*[.="Интервал тестирования"]//input)[2]'
Test_interval_rezerv_2 = '(//*[.="Интервал тестирования"]//input)[3]'

# Адрес
address_DC09_main = '(//*[.="Адрес"]//input)[1]'
address_DC09_reserv_1 = '(//*[.="Адрес"]//input)[2]'
address_DC09_reserv_2 = '(//*[.="Адрес"]//input)[3]'

# Порт
port_DC09_main = '(//*[.="Порт"]//input)[1]'
port_DC09_reserv_1 = '(//*[.="Порт"]//input)[2]'
port_DC09_reserv_2 = '(//*[.="Порт"]//input)[3]'

# Таймаут подтверждения, сек
confirmation_timeout_DC09_main = '(//*[.="Таймаут подтверждения, сек"]//input)[1]'
confirmation_timeout_DC09_reserv_1 = '(//*[.="Таймаут подтверждения, сек"]//input)[2]'
confirmation_timeout_DC09_reserv_2 = '(//*[.="Таймаут подтверждения, сек"]//input)[3]'

# Количество повторов
number_of_repetitions_DC09_main = '(//*[.="Количество повторов"]//input)[1]'
number_of_repetitions_DC09_reserv_1 = '(//*[.="Количество повторов"]//input)[2]'
number_of_repetitions_DC09_reserv_2 = '(//*[.="Количество повторов"]//input)[3]'

# Ключ шифрования
encryption_key_DC09_main = '(//*[.="Ключ шифрования"]//input)[1]'
encryption_key_DC09_reserv_1 = '(//*[.="Ключ шифрования"]//input)[2]'
encryption_key_DC09_reserv_2 = '(//*[.="Ключ шифрования"]//input)[3]'

# ------------ КНОПКИ ------------
# Настройки
maim_settings_button = '(//*[@id="destinationsScrollable"]//button[.="Настройки"])'
# Кнопка выпадающего списка Разрешения
permissions_dropdown = '//*[.="Разрешения"]/following::span[1]'
# Выбор опции
option_key = '(/html/body//div[@class="option"])'
# Сохранить
save_button = '//*[@id="modalSettings"]//button[.="Сохранить"]'

# ------------ ВЫПАДАЮЩИЕ СПИСКИ ------------
# Кнопка Тип управления - ОСНОВНОЙ КАНАЛ
type_main = '((//div[@class="channel-settings"])[1]//span[@class="label"])[1]'
type_rezerv_1 = '((//div[@class="channel-settings"])[2]//span[@class="label"])[1]'
type_rezerv_2 = '((//div[@class="channel-settings"])[3]//span[@class="label"])[1]'
# Тестировать
Test_at_intervals_main = '((//div[@class="channel-settings"])[1]//span[@class="label"])[6]'
Test_at_intervals_rezerv_1 = '((//div[@class="channel-settings"])[2]//span[@class="label"])[6]'
Test_at_intervals_rezerv_2 = '((//div[@class="channel-settings"])[3]//span[@class="label"])[6]'
# Тестировать
Test_at_intervals_sms_egida_main = '((//div[@class="channel-settings"])[1]//span[@class="label"])[5]'
Test_at_intervals_sms_egida_rezerv_1 = '((//div[@class="channel-settings"])[2]//span[@class="label"])[5]'
Test_at_intervals_sms_egida_rezerv_2 = '((//div[@class="channel-settings"])[3]//span[@class="label"])[5]'
# Язык
lang_main = '((//div[@class="channel-settings"])[1]//span[@class="label"])[3]'
lang_rezerv_1 = '((//div[@class="channel-settings"])[2]//span[@class="label"])[3]'
lang_rezerv_2 = '((//div[@class="channel-settings"])[3]//span[@class="label"])[3]'
# Тестировать если
test_IF_main = '((//div[@class="channel-settings"])[1]//span[@class="label"])[4]'
test_IF_rezerv_1 = '((//div[@class="channel-settings"])[2]//span[@class="label"])[4]'
test_IF_rezerv_2 = '((//div[@class="channel-settings"])[3]//span[@class="label"])[4]'

# Тестировать если СМС ЭГИДА
test_IF_sms_egida_main = '((//div[@class="channel-settings"])[1]//span[@class="label"])[3]'
test_IF_sms_egidrezerv_1 = '((//div[@class="channel-settings"])[2]//span[@class="label"])[3]'
test_IF_sms_egidrezerv_2 = '((//div[@class="channel-settings"])[3]//span[@class="label"])[3]'

# Канал соединения
connection_main = '((//div[@class="channel-settings"])[1]//span[@class="label"])[2]'
connection_rezerv_1 = '((//div[@class="channel-settings"])[2]//span[@class="label"])[2]'
connection_rezerv_2 = '((//div[@class="channel-settings"])[3]//span[@class="label"])[2]'

# Метод тестирования
test_method_main = '((//div[@class="channel-settings"])[1]//span[@class="label"])[5]'
test_method_rezerv_1 = '((//div[@class="channel-settings"])[2]//span[@class="label"])[5]'
test_method_rezerv_2 = '((//div[@class="channel-settings"])[3]//span[@class="label"])[5]'

# Метод тестирования - sms ЭГИДА
test_method_sms_egida_main = '((//div[@class="channel-settings"])[1]//span[@class="label"])[4]'
test_method_sms_egida_rezerv_1 = '((//div[@class="channel-settings"])[2]//span[@class="label"])[4]'
test_method_sms_egida_rezerv_2 = '((//div[@class="channel-settings"])[3]//span[@class="label"])[4]'

# Тестировать
testing_main = '((//div[@class="channel-settings"])[1]//span[@class="label"])[6]'
testing_rezerv_1 = '((//div[@class="channel-settings"])[2]//span[@class="label"])[6]'
testing_rezerv_2 = '((//div[@class="channel-settings"])[3]//span[@class="label"])[6]'

# Тестировать - sms ЭГИДА
testing_sms_egida_main = '((//div[@class="channel-settings"])[1]//span[@class="label"])[5]'
testing_sms_egida_rezerv_1 = '((//div[@class="channel-settings"])[2]//span[@class="label"])[5]'
testing_sms_egida_rezerv_2 = '((//div[@class="channel-settings"])[3]//span[@class="label"])[5]'

# Дни недели
days_of_the_week_main = '(//div[@class="b-multiselect-label"])[2]'
days_of_the_week_rezerv_1 = '(//div[@class="b-multiselect-label"])[3]'
days_of_the_week_rezerv_2 = '(//div[@class="b-multiselect-label"])[4]'
main_check_box_drop_down_days = '(/html/body/div[3]/div[1]/label/span)[1]'

# Разделы
reset_path_main = '/html//div[@class="b-multiselect-header"]/button'
path_main = '(//div[@class="b-multiselect-label"])[1]'
main_check_box_drop_down = '(/html/body//span[@class="checkmark-container"])[1]'
main_check_box_drop_down_path = '(//span[@class="checkmark"])[4]'
status_path_check_box = '(//*[@class="b-multiselect-items-wrapper scrollable"]//label/input)'

# ------------ЧЕКБОКСЫ-------------
# Включить модуль GSM
main_Enable_channel_testing_click = '(//*[.="Включить тестирование канала"]//label/span)[1]'
main_Enable_channel_testing_status = '(//*[.="Включить тестирование канала"]//label/input)[1]'
rezerv_1_Enable_channel_testing_click = '(//*[.="Включить тестирование канала"]//label/span)[2]'
rezerv_1_Enable_channel_testing_status = '(//*[.="Включить тестирование канала"]//label/input)[2]'
rezerv_2_Enable_channel_testing_click = '(//*[.="Включить тестирование канала"]//label/span)[3]'
rezerv_2_Enable_channel_testing_status = '(//*[.="Включить тестирование канала"]//label/input)[3]'

# Отправлять время события
main_Send_event_time_click = '(//*[.="Отправлять время события"]//label/span)[1]'
main_Send_event_time_status = '(//*[.="Отправлять время события"]//label/input)[1]'
rezerv_1_Send_event_time_click = '(//*[.="Отправлять время события"]//label/span)[2]'
rezerv_1_Send_event_time_status = '(//*[.="Отправлять время события"]//label/input)[2]'
rezerv_2_Send_event_time_click = '(//*[.="Отправлять время события"]//label/span)[3]'
rezerv_2_Send_event_time_status = '(//*[.="Отправлять время события"]//label/input)[3]'

# Шифрование
main_Encryption_click = '(//*[.="Шифрование"]//label/span)[1]'
main_Encryption_status = '(//*[.="Шифрование"]//label/input)[1]'
rezerv_1_Encryption_click = '(//*[.="Шифрование"]//label/span)[2]'
rezerv_1_Encryption_status = '(//*[.="Шифрование"]//label/input)[2]'
rezerv_2_Encryption_click = '(//*[.="Шифрование"]//label/span)[3]'
rezerv_2_Encryption_status = '(//*[.="Шифрование"]//label/input)[3]'

# Отправлять дату события
main_Send_event_data_click = '(//*[.="Отправлять дату события"]//label/span)[1]'
main_Send_event_data_status = '(//*[.="Отправлять дату события"]//label/input)[1]'
rezerv_1_Send_event_data_click = '(//*[.="Отправлять дату события"]//label/span)[2]'
rezerv_1_Send_event_data_status = '(//*[.="Отправлять дату события"]//label/input)[2]'
rezerv_2_Send_event_data_click = '(//*[.="Отправлять дату события"]//label/span)[3]'
rezerv_2_Send_event_data_status = '(//*[.="Отправлять дату события"]//label/input)[3]'

# ------------ТУМБЛЕРЫ-------------
# События разделов
Take_all_event_path_click = '(//*[.="Выбрать все"]//label/span)[1]'
Take_all_event_path_status = '(//*[.="Выбрать все"]//label/input)[1]'
No_take_click = '(//*[.="Невзятие"]//label/span)[1]'
No_takel_status = '(//*[.="Невзятие"]//label/input)[1]'
Outfit_mark_click = '(//*[.="Отметка наряда"]//label/span)[1]'
Outfit_mark_status = '(//*[.="Отметка наряда"]//label/input)[1]'
Fire_click = '(//*[.="Пожар"]//label/span)[1]'
Fire_status = '(//*[.="Пожар"]//label/input)[1]'
Fire_by_manual_call_point_click = '(//*[.="Пожар по ручному извещателю"]//label/span)[1]'
Fire_by_manual_call_point_status = '(//*[.="Пожар по ручному извещателю"]//label/input)[1]'
No_Fire_click = '(//*[.="Пожара нет"]//label/span)[1]'
No_Fire_status = '(//*[.="Пожара нет"]//label/input)[1]'
Forcing_Partition_click = '(//*[.="Принудительное взятие раздела"]//label/span)[1]'
Forcing_Partition_status = '(//*[.="Принудительное взятие раздела"]//label/input)[1]'
Water_leak_click = '(//*[.="Протечка воды"]//label/span)[1]'
Water_leak_status = '(//*[.="Протечка воды"]//label/input)[1]'
Section_taken_click = '(//*[.="Раздел взят"]//label/span)[1]'
Section_taken_status = '(//*[.="Раздел взят"]//label/input)[1]'
Section_taken_off_click = '(//*[.="Раздел снят"]//label/span)[1]'
Section_taken_off_status = '(//*[.="Раздел снят"]//label/input)[1]'
Silent_alarm_click = '(//*[.="Тихая тревога"]//label/span)[1]'
Silent_alarm_status = '(//*[.="Тихая тревога"]//label/input)[1]'
Alarm_click = '(//*[.="Тревога"]//label/span)[1]'
Alarm_status = '(//*[.="Тревога"]//label/input)[1]'
Alarm_enter_click = '(//*[.="Тревога входа"]//label/span)[1]'
Alarm_enter_status = '(//*[.="Тревога входа"]//label/input)[1]'

# Питание прибора
Take_all_power_device_click = '(//*[.="Выбрать все"]//label/span)[3]'
Take_all_power_device_status = '(//*[.="Выбрать все"]//label/input)[3]'
Battery_is_OK_click = '(//*[.="Аккумулятор в норме"]//label/span)[1]'
Battery_is_OK_status = '(//*[.="Аккумулятор в норме"]//label/input)[1]'
The_battery_is_charging_click = '(//*[.="Аккумулятор заряжается"]//label/span)[1]'
The_battery_is_charging_status = '(//*[.="Аккумулятор заряжается"]//label/input)[1]'
Battery_is_charged_click = '(//*[.="Аккумулятор заряжен"]//label/span)[1]'
Battery_is_charged_status = '(//*[.="Аккумулятор заряжен"]//label/input)[1]'
Battery_not_connected_or_connected_incorrectly_click = '(//*[.="Аккумулятор не подключен или подключен неверно"]//label/span)[1]'
Battery_not_connected_or_connected_incorrectly_status = '(//*[.="Аккумулятор не подключен или подключен неверно"]//label/input)[1]'
Battery_low_click = '(//*[.="Аккумулятор разряжен"]//label/span)[1]'
Battery_low_status = '(//*[.="Аккумулятор разряжен"]//label/input)[1]'
High_internal_battery_resistance_click = '(//*[.="Высокое внутреннее сопротивление аккумулятора"]//label/span)[1]'
High_internal_battery_resistance_status = '(//*[.="Высокое внутреннее сопротивление аккумулятора"]//label/input)[1]'
Mains_power_is_OK_click = '(//*[.="Сетевое питание в норме"]//label/span)[1]'
Mains_power_is_OK_status = '(//*[.="Сетевое питание в норме"]//label/input)[1]'
Mains_power_off_click = '(//*[.="Сетевое питание отключено"]//label/span)[1]'
Mains_power_off_status = '(//*[.="Сетевое питание отключено"]//label/input)[1]'

# События зон
zone_events_device_click = '(//*[.="Выбрать все"]//label/span)[2]'
zone_events_device_status = '(//*[.="Выбрать все"]//label/input)[2]'
Battery_OK_zone_events_device_click = '(//*[.="Батарея в норме"]//label/span)[1]'
Battery_OK_zone_events_device_status = '(//*[.="Батарея в норме"]//label/input)[1]'
ready_click = '(//*[.="Готов"]//label/span)[1]'
ready_status = '(//*[.="Готов"]//label/input)[1]'
Case_closed_click = '(//*[.="Корпус закрыт"]//label/span)[1]'
Case_closed_status = '(//*[.="Корпус закрыт"]//label/input)[1]'
Case_open_click = '(//*[.="Корпус открыт"]//label/span)[1]'
Case_open_status = '(//*[.="Корпус открыт"]//label/input)[1]'
Low_battery_zone_events_click = '(//*[.="Низкий заряд батареи"]//label/span)[1]'
Low_battery_zone_events_status = '(//*[.="Низкий заряд батареи"]//label/input)[1]'
Backup_battery_error_zone_events_click = '(//*[.="Ошибка резервной батареи"]//label/span)[1]'
Backup_battery_error_zone_events_status = '(//*[.="Ошибка резервной батареи"]//label/input)[1]'
Device_error_zone_events_click = '(//*[.="Ошибка устройства"]//label/span)[1]'
Device_error_zone_events_status = '(//*[.="Ошибка устройства"]//label/input)[1]'
Sensor_reset_zone_events_click = '(//*[.="Перезагрузка датчика"]//label/span)[1]'
Sensor_reset_zone_events_status = '(//*[.="Перезагрузка датчика"]//label/input)[1]'
Lost_zone_events_click = '(//*[.="Потерян"]//label/span)[1]'
Lost_zone_events_status = '(//*[.="Потерян"]//label/input)[1]'
Check_connection_zone_events_click = '(//*[.="Проверка связи"]//label/span)[1]'
Check_connection_zone_events_status = '(//*[.="Проверка связи"]//label/input)[1]'
Backup_battery_is_OK_zone_events_click = '(//*[.="Резервная батарея в норме"]//label/span)[1]'
Backup_battery_is_OK_zone_events_status = '(//*[.="Резервная батарея в норме"]//label/input)[1]'
Sabotage_zone_events_click = '(//*[.="Саботаж"]//label/span)[1]'
Sabotage_zone_events_status = '(//*[.="Саботаж"]//label/input)[1]'
Communication_restored_zone_events_click = '(//*[.="Связь восстановлена"]//label/span)[1]'
Communication_restored_zone_events_status = '(//*[.="Связь восстановлена"]//label/input)[1]'
Humidity_event_zone_events_click = '(//*[.="Событие по влажности"]//label/span)[1]'
Humidity_event_zone_events_status = '(//*[.="Событие по влажности"]//label/input)[1]'
CO_sensor_event_zone_events_click = '(//*[.="Событие по датчику CO"]//label/span)[1]'
CO_sensor_event_zone_events_status = '(//*[.="Событие по датчику CO"]//label/input)[1]'
Temperature_event_zone_events_click = '(//*[.="Событие по температуре"]//label/span)[1]'
Temperature_event_zone_events_status = '(//*[.="Событие по температуре"]//label/input)[1]'
Sensor_activation_Bell_mode_zone_events_click = '(//*[.=\'Сработка датчика, режим "Колокольчик"\']//label/span)[1]'
Sensor_activation_Bell_mode_zone_events_status = '(//*[.=\'Сработка датчика, режим "Колокольчик"\']//label/input)[1]'
SS_is_normal_zone_events_click = '(//*[.="ШС в норме"]//label/span)[1]'
SS_is_normal_zone_events_status = '(//*[.="ШС в норме"]//label/input)[1]'
AL_is_closed_zone_events_click = '(//*[.="ШС замкнут"]//label/span)[1]'
AL_is_closed_zone_events_status = '(//*[.="ШС замкнут"]//label/input)[1]'
AL_interrupted_zone_events_click = '(//*[.="ШС оборван"]//label/span)[1]'
AL_interrupted_zone_events_status = '(//*[.="ШС оборван"]//label/input)[1]'

# Системные события прибора
instrument_system_events_click = '(//*[.="Выбрать все"]//label/span)[4]'
instrument_system_events_status = '(//*[.="Выбрать все"]//label/input)[4]'
Opening_the_case_of_the_device_click = '(//*[.="Вскрытие корпуса прибора"]//label/span)[1]'
Opening_the_case_of_the_device_status = '(//*[.="Вскрытие корпуса прибора"]//label/input)[1]'
Closing_the_instrument_housing_click = '(//*[.="Закрытие корпуса прибора"]//label/span)[1]'
Closing_the_instrument_housing_status = '(//*[.="Закрытие корпуса прибора"]//label/input)[1]'
The_device_has_been_rebooted_click = '(//*[.="Устройство было перезагружено"]//label/span)[1]'
The_device_has_been_rebooted_status = '(//*[.="Устройство было перезагружено"]//label/input)[1]'
