# -*- coding: utf-8 -*-

# ---------------------Автороизация----------------------
# Логин
login_input = '//*[@id="username"]'
# Пароль
password_input = '//*[@id="password"]'

# НАСТРОЙКИ
# ------------------------Объект--------------------------
# Название объекта
object_name_input = '//*[.="Название объекта"]//input'
object_name = '//*[@id="app"]/main//span[.="Название объекта"]'
# Номер объекта
object_number_input = '//*[.="Номер объекта"]/following::input[1]'
object_number = '//*[@id="app"]/main//span[.="Номер объекта"]'
# Задержка взятия
object_delay_take_on_input = '//*[.="Задержка взятия"]/following::input[1]'
object_delay_take_on = '//*[@id="app"]/main//span[.="Задержка взятия"]'
# Задержка тревоги входа
object_delay_alarm_enter_input = '//*[.="Задержка тревоги входа"]/following::input[1]'
object_delay_alarm_enter = '//*[@id="app"]/main//span[.="Задержка тревоги входа"]'
# Время автовзятия
object_time_auto_take_on_input = '//*[.="Время автовзятия"]/following::input[1]'
object_time_auto_take_on = '//*[@id="app"]/main//span[.="Время автовзятия"]'
# Тревога при потере датчика
object_sensor_loss_alarm = '//*[@id="app"]/main//span[.="Тревога при потере датчика"]'
# Взятие при потерянных датчиках
object_taking_with_lost_sensors = '//*[@id="app"]/main//span[.="Взятие при потерянных датчиках"]'
# Взятие при датчиках в тревоге
object_taking_with_sensors_in_alarm = '//*[@id="app"]/main//span[.="Взятие при датчиках в тревоге"]'
# Взятие при датчиках в неисправности
object_capturing_with_sensors_in_error = '//*[@id="app"]/main//span[.="Взятие при датчиках в неисправности"]'
# Принудительное взятие из тревоги
object_forced_take_from_alarm = '//*[@id="app"]/main//span[.="Принудительное взятие из тревоги"]'

# ------------------------Дата и время--------------------------
# Дата и время на устройстве
Date_and_time_on_the_device = '//span[@class="label"]'
# Использовать временную зону GSM сети
date_time_use_time_zone_of_GSM_network = '//*[@id="app"]/main//span[.="Использовать временную зону GSM сети"]'
# Переход на летнее время
date_time_daylight_Saving_Time = '//*[@id="app"]/main//span[.="Переход на летнее время"]'
# Адрес сервера
date_time_ntp_server_address = '//*[@id="app"]/main//span[.="Адрес сервера"]'
date_time_ntp_server_address_input = '//*[.="Адрес сервера"]/following::input[1]'
# Часовой пояс
date_time_time_zone = '//*[@id="app"]/main//span[.="Часовой пояс"]'
# Дата и время
date_time_locator = '//*[@id="app"]/main//span[.="Дата и время"]'

# ------------------------Прибор--------------------------
# Включить энергосберегающий режим
Enable_power_saving_mode = '//*[@id="app"]/main//span[.="Включить энергосберегающий режим"]'
# Разрешить настройку при закрытом корпусе
Allow_configuration_when_the_case_is_closed = '//*[@id="app"]/main//span[.="Разрешить настройку при закрытом корпусе"]'
# Фиксировать повторные тревоги раздела
Fix_partition_repeated_alarms = '//*[@id="app"]/main//span[.="Фиксировать повторные тревоги раздела"]'
# Фиксировать повторные тревоги датчика
Fix_repeated_sensor_alarms = '//*[@id="app"]/main//span[.="Фиксировать повторные тревоги датчика"]'
# Фиксировать повторные пожарные тревоги раздела
Fix_repeated_fire_alarms_in_a_section = '//*[@id="app"]/main//span[.="Фиксировать повторные пожарные тревоги раздела"]'
# Фиксировать повторные пожарные тревоги датчика
Fix_repeated_fire_alarms_of_the_sensor = '//*[@id="app"]/main//span[.="Фиксировать повторные пожарные тревоги датчика"]'
# Фиксировать повторные события взятия/снятия
Fix_repeated_arming_disarming_events = '//*[@id="app"]/main//span[.="Фиксировать повторные события взятия/снятия"]'
# Управлять выходами при повторном взятии/снятии
Control_exits_when_re_arming_disarming = '//*[@id="app"]/main//span[.="Управлять выходами при повторном взятии/снятии"]'

# ------------------------Световая индикация--------------------------
# Режим светодиодов для охранных датчиков
LED_mode_for_security_sensors = '//*[@id="app"]/main//span[.="Режим светодиодов для охранных датчиков"]'
# Режим светодиодов для пожарных датчиков
LED_mode_for_fire_detectors = '//*[@id="app"]/main//span[.="Режим светодиодов для пожарных датчиков"]'
# Режим светодиодов для технологических датчиков
LED_mode_for_process_sensors = '//*[@id="app"]/main//span[.="Режим светодиодов для технологических датчиков"]'
# Режим работы считывателя
Reader_operation_mode = '//*[@id="app"]/main//span[.="Режим работы считывателя"]'
# Режим работы считывателя
Reader_indication_inversion = '//*[@id="app"]/main//span[.="Инверсия индикации считывателя"]'

# ------------------------Звуковая индикация--------------------------
# Включить
Volume_indication_ON = '//*[@id="app"]/main//span[.="Включить"]'
# Длительность сигнала
Signal_duration = '//*[@id="app"]/main//span[.="Длительность сигнала"]'
Signal_duration_input = '//*[.="Длительность сигнала"]/following::input[1]'
# Громкость событий
Event_volume = '//*[@id="app"]/main//span[.="Громкость событий"]'
# Громкость тревог
Alarm_volume = '//*[@id="app"]/main//span[.="Громкость тревог"]'
# Тревога
Anxiety = '//*[@id="app"]/main//span[.="Тревога"]'
# Пожар
Fire = '//*[@id="app"]/main//span[.="Пожар"]'
# Взятие раздела
Taking_section = '//*[@id="app"]/main//span[.="Взятие раздела"]'
# Снятие раздела
Removing_partition = '//*[@id="app"]/main//span[.="Снятие раздела"]'
# Задержка взятия
Take_Delay = '//*[@id="app"]/main//span[.="Задержка взятия"]'
# Невзятие
Not_taking = '//*[@id="app"]/main//span[.="Невзятие"]'
# Разделы частично взяты
Sections_partially_taken = '//*[@id="app"]/main//span[.="Разделы частично взяты"]'
# Добавление датчика
Adding_sensor = '//*[@id="app"]/main//span[.="Добавление датчика"]'
# Колокольчик
Bell = '//*[@id="app"]/main//span[.="Колокольчик"]'

# ------------------------Радио--------------------------
# Включить радиомодуль
Radio_Enable_radio = '//*[@id="app"]/main//span[.="Включить радиомодуль"]'
# Время разрешения добавления новых датчиков
Radio_Resolution_time_adding_new_sensors = '//*[@id="app"]/main//span[.="Время разрешения добавления новых датчиков"]'
Radio_Resolution_time_adding_new_sensors_input = '//*[.="Время разрешения добавления новых датчиков"]/following::input[1]'
# Канал
Radio_Channel = '//*[@id="app"]/main//span[.="Канал"]'
# Период опроса датчиков
Radio_Sensor_polling_period = '//*[@id="app"]/main//span[.="Период опроса датчиков"]'
Radio_Sensor_polling_period_input = '(//*[@id="app"]//span[@class="label"])[2]'

# ------------------------GSM--------------------------
# Включить модуль GSM
GSM_Enable_GSM_module = '//*[@id="app"]/main//span[.="Включить модуль GSM"]'
# Использовать GPRS
GSM_Use_GPRS = '//*[@id="app"]/main//span[.="Использовать GPRS"]'
# Использовать резервную SIM
GSM_Use_backup_SIM = '//*[@id="app"]/main//span[.="Использовать резервную SIM"]'
# Разрешить USSD
GSM_Allow_USSD = '//*[@id="app"]/main//span[.="Разрешить USSD"]'
# Число знаков номера для проверки
GSM_Number_digits_number_to_check = '//*[@id="app"]/main//span[.="Число знаков номера для проверки"]'
GSM_Number_digits_number_to_check_input = '//*[.="Число знаков номера для проверки"]/following::input[1]'
# Порог уведомления о балансе
GSM_Balance_Notification_Threshold = '//*[@id="app"]/main//span[.="Порог уведомления о балансе"]'
GSM_Balance_Notification_Threshold_input = '//*[.="Порог уведомления о балансе"]/following::input[1]'
# Разрешить трансляцию событий
GSM_Allow_Event_Broadcast = '//*[@id="app"]/main//span[.="Разрешить трансляцию событий"]'
GSM_sim_1_pin_input = '(//*[.="PIN"]//input[1])[1]'
GSM_sim_2_pin_input = '(//*[.="PIN"]//input[1])[2]'
GSM_sim_1_USSD_cod_input = '(//*[.="USSD-код запроса баланса"]//input[1])[1]'
GSM_sim_2_USSD_cod_input = '(//*[.="USSD-код запроса баланса"]//input[1])[2]'
GSM_sim_1_APN_input = '(//*[.="APN"]//input[1])[1]'
GSM_sim_2_APN_input = '(//*[.="APN"]//input[1])[2]'
GSM_sim_1_user_input = '(//*[.="Пользователь"]//input[1])[1]'
GSM_sim_2_user_input = '(//*[.="Пользователь"]//input[1])[2]'
GSM_sim_1_password_input = '(//*[.="Пароль"]//input[1])[1]'
GSM_sim_2_password_input = '(//*[.="Пароль"]//input[1])[2]'

# ------------------------Ethernet--------------------------
# MAC адрес
Ethernet_MAC_address = '//*[@id="app"]/main//span[.="MAC адрес"]'
Ethernet_MAC_address_input = '//*[.="MAC адрес"]/following::input[1]'
# Название сервера
Ethernet_Server_name = '//*[@id="app"]/main//span[.="Название сервера"]'
Ethernet_Server_name_input = '//*[.="Название сервера"]/following::input[1]'
# Адрес IPv4
Ethernet_IPv4_address = '//*[@id="app"]/main//span[.="Адрес IPv4"]'
Ethernet_IPv4_address_input = '//*[.="Адрес IPv4"]/following::input[1]'
# Маска подсети
Ethernet_Subnet_mask = '//*[@id="app"]/main//span[.="Маска подсети"]'
Ethernet_Subnet_mask_input = '//*[.="Маска подсети"]/following::input[1]'
# Основной шлюз
Ethernet_Main_gate = '//*[@id="app"]/main//span[.="Основной шлюз"]'
Ethernet_Main_gate_input = '//*[.="Основной шлюз"]/following::input[1]'
# Предпочтительный DNS сервер
Ethernet_Preferred_DNS_Server = '//*[@id="app"]/main//span[.="Предпочтительный DNS сервер"]'
Ethernet_Preferred_DNS_Server_input = '//*[.="Предпочтительный DNS сервер"]/following::input[1]'
# Альтернативный DNS сервер
Ethernet_Alternative_DNS_Server = '//*[@id="app"]/main//span[.="Альтернативный DNS сервер"]'
Ethernet_Alternative_DNS_Server_input = '//*[.="Альтернативный DNS сервер"]/following::input[1]'
# Получать IPv4 адрес и настройки автоматически
Ethernet_Obtain_IPv4_address_settings_automatically = '//*[@id="app"]/main//span[.="Получать IPv4 адрес и настройки автоматически"]'
# Использовать как сервер
Ethernet_Use_as_server = '//*[@id="app"]/main//span[.="Использовать как сервер"]'
# Получать адрес IPv6 от DHCP автоматически
Ethernet_Obtain_IPv6_address_DHCP_automatically = '//*[@id="app"]/main//span[.="Получать адрес IPv6 от DHCP автоматически"]'
# Разрешить удаленное управление
Ethernet_Allow_remote_control = '//*[@id="app"]/main//span[.="Разрешить удаленное управление"]'
# Получать адрес IPv6 от SLAAC автоматически
Ethernet_Obtain_IPv6_address_SLAAC_automatically = '//*[@id="app"]/main//span[.="Получать адрес IPv6 от SLAAC автоматически"]'
# Разрешить незащищенное HTTP-соединение
Ethernet_Allow_insecure_HTTP_connection = '//*[@id="app"]/main//span[.="Разрешить незащищенное HTTP-соединение"]'
# Устанавливать сетевые подключения через
Ethernet_Establish_network_connections = '//*[@id="app"]/main//span[.="Устанавливать сетевые подключения через"]'
# Локальный IPv6 адрес
Ethernet_Local_IPv6_address = '//*[@id="app"]/main//span[.="Локальный IPv6 адрес"]'
Ethernet_Local_IPv6_address_input = '//*[.="Локальный IPv6 адрес"]/following::input[1]'
# Глобальный IPv6 адрес
Ethernet_Global_IPv6_Address = '//*[@id="app"]/main//span[.="Глобальный IPv6 адрес"]'
Ethernet_Global_IPv6_Address_input = '//*[.="Глобальный IPv6 адрес"]/following::input[1]'
# Предпочтительный IPv6 DNS сервер
Ethernet_Preferred_IPv6_DNS_Server = '//*[@id="app"]/main//span[.="Предпочтительный IPv6 DNS сервер"]'
Ethernet_Preferred_IPv6_DNS_Server_input = '//*[.="Предпочтительный IPv6 DNS сервер"]/following::input[1]'
# Альтернативный IPv6 DNS сервер
Ethernet_Alternative_IPv6_DNS_Server = '//*[@id="app"]/main//span[.="Альтернативный IPv6 DNS сервер"]'
Ethernet_Alternative_IPv6_DNS_Server_input = '//*[.="Альтернативный IPv6 DNS сервер"]/following::input[1]'

# ПОЛЬЗОВАТЕЛИ И КЛЮЧИ
# ------------------------Пользователи--------------------------
# Администратор
user_administrator = '//*[@id="modalSettings"]//span[.="Администратор"]'
# Режим Эгида3
user_egida3 = '//*[@id="modalSettings"]//span[.="Режим Эгида3"]'
# Имя пользователя
user_name = '//*[@id="modalSettings"]//span[.="Имя пользователя"]'
user_name_input = '//*[@id="modalSettings"]//*[.="Имя пользователя"]/following::input[1]'
# Логин
user_login = '//*[@id="modalSettings"]//span[.="Логин"]'
user_login_input = '//*[@id="modalSettings"]//*[.="Логин"]/following::input[1]'
# Пароль
user_password = '//*[@id="modalSettings"]//span[.="Пароль"]'
user_password_input = '//*[@id="modalSettings"]//*[.="Пароль"]/following::input[1]'
# Повторите пароль
user_rep_password = '//*[@id="modalSettings"]//span[.="Повторите пароль"]'
user_rep_password_input = '//*[@id="modalSettings"]//*[.="Повторите пароль"]/following::input[1]'
# Перенаправление сообщений оператора
user_operator_message_forwarding = '//*[@id="modalSettings"]//span[.="Перенаправление сообщений оператора"]'
# Отправка вне трансляции
user_sending_out_of_broadcast = '//*[@id="modalSettings"]//span[.="Отправка вне трансляции"]'
# Группа выходов с управлением по SMS
user_group_of_outputs_controlled_by_SMS = '//*[@id="modalSettings"]//span[.="Группа выходов с управлением по SMS"]'
# Группа выходов с управлением звонком
user_group_of_outputs_with_call_control = '//*[@id="modalSettings"]//span[.="Группа выходов с управлением звонком"]'
# Разрешить снятие по SMS
user_allow_withdrawal_by_SMS = '//*[@id="modalSettings"]//span[.="Разрешить снятие"]'
# Разрешить взятие по SMS
user_allow_pickup_by_SMS = '//*[@id="modalSettings"]//span[.="Разрешить взятие"]'
# Телефон
user_phone = '//*[@id="modalSettings"]//span[.="Телефон"]'
user_phone_cod = '//*[@id="modalSettings"]//*[.="Телефон"]/following::input[1]'
user_phone_number = '//*[@id="modalSettings"]//*[.="Телефон"]/following::input[2]'
# Пароль SMS
user_password_sms = '//*[@id="modalSettings"]//span[.="Пароль SMS"]'
user_password_sms_input = '//*[@id="modalSettings"]//*[.="Пароль SMS"]/following::input[1]'
# Повторите пароль SMS
user_rep_password_sms = '//*[@id="modalSettings"]//span[.="Повторите пароль SMS"]'
user_rep_password_sms_input = '//*[@id="modalSettings"]//*[.="Повторите пароль SMS"]/following::input[1]'
# Управляемые по SMS разделы
user_SMS_controlled_sections = '//*[@id="modalSettings"]//span[.="Управляемые разделы"]'
# ------------------------Ключи--------------------------
# Идентификатор
keys_id = '//*[@id="modalSettings"]//span[.="Идентификатор"]'
keys_id_input = '//*[@id="modalSettings"]//*[.="Идентификатор"]/following::input[1]'
# Пользователь
keys_user = '//*[@id="modalSettings"]//span[.="Пользователь"]'
# Разрешения
keys_permissions = '//*[@id="modalSettings"]//span[.="Разрешения"]'
# Разделы
keys_path = '//*[@id="modalSettings"]//span[.="Разделы"]'

# Зоны/Разделы
# ------------------------Разделы--------------------------
# Номер
path_number = '//*[@id="modalSettings"]//span[.="Номер раздела"]'
path_number_input = '//*[@id="modalSettings"]//*[.="Номер раздела"]/following::input[1]'
# Название
path_name = '//*[@id="modalSettings"]//span[.="Название"]'
path_name_input = '//*[@id="modalSettings"]//*[.="Название"]/following::input[1]'
# Управляющие разделы
path_control_sections = '//*[@id="modalSettings"]//span[.="Управляющие разделы"]'
# Задержка взятия
path_take_delay = '//*[@id="modalSettings"]//span[.="Задержка взятия"]'
# Автовзятие из невзятия
path_auto_pickup_from_non_pickup = '//*[@id="modalSettings"]//span[.="Автовзятие из невзятия"]'
# Автовзятие из тревоги
path_auto_arm_from_alarm = '//*[@id="modalSettings"]//span[.="Автовзятие из тревоги"]'

# Направления
# ------------------------Направления--------------------------
# Название
directions_name = '//*[@id="modalSettings"]//span[.="Название"]'
directions_name_input = '//*[@id="modalSettings"]//*[.="Название"]/following::input[1]'
# Разделы
directions_path = '//*[@id="modalSettings"]//span[.="Разделы"]'
# Тип управления
directions_control_type = '(//*[@id="modalSettings"]//span[.="Тип управления"])[1]'
directions_control_type_rezerv_1 = '(//*[@id="modalSettings"]//span[.="Тип управления"])[2]'
directions_control_type_rezerv_2 = '(//*[@id="modalSettings"]//span[.="Тип управления"])[3]'
# Текущий пользователь
directions_current_user = '(//*[@id="modalSettings"]//span[.="Текущий пользователь"])[1]'
directions_current_user_rezerv_1 = '(//*[@id="modalSettings"]//span[.="Текущий пользователь"])[2]'
directions_current_user_rezerv_2 = '(//*[@id="modalSettings"]//span[.="Текущий пользователь"])[3]'
# Отправлять время события
directions_send_event_time = '(//*[@id="modalSettings"]//span[.="Отправлять время события"])[1]'
directions_send_event_time_rezerv_1 = '(//*[@id="modalSettings"]//span[.="Отправлять время события"])[2]'
directions_send_event_time_rezerv_2 = '(//*[@id="modalSettings"]//span[.="Отправлять время события"])[3]'
# Отправлять дату события
directions_send_event_date = '(//*[@id="modalSettings"]//span[.="Отправлять дату события"])[1]'
directions_send_event_date_rezerv_1 = '(//*[@id="modalSettings"]//span[.="Отправлять дату события"])[2]'
directions_send_event_date_rezerv_2 = '(//*[@id="modalSettings"]//span[.="Отправлять дату события"])[3]'
# Включить тестирование канала
directions_enable_channel_testing = '(//*[@id="modalSettings"]//span[.="Включить тестирование канала"])[1]'
directions_enable_channel_testing_rezerv_1 = '(//*[@id="modalSettings"]//span[.="Включить тестирование канала"])[2]'
directions_enable_channel_testing_rezerv_2 = '(//*[@id="modalSettings"]//span[.="Включить тестирование канала"])[3]'
# Таймаут при ошибке
directions_timeout_on_error = '(//*[@id="modalSettings"]//span[.="Таймаут при ошибке"])[1]'
directions_timeout_on_error_rezerv_1 = '(//*[@id="modalSettings"]//span[.="Таймаут при ошибке"])[2]'
directions_timeout_on_error_rezerv_2 = '(//*[@id="modalSettings"]//span[.="Таймаут при ошибке"])[3]'
directions_timeout_on_error_input = '(//*[.="Таймаут при ошибке"])[1]/../..//input'
directions_timeout_on_error_input_rezerv_1 = '(//*[.="Таймаут при ошибке"])[2]/../..//input'
directions_timeout_on_error_input_rezerv_2 = '(//*[.="Таймаут при ошибке"])[3]/../..//input'
# Тестировать если
directions_test_if = '(//*[@id="modalSettings"]//span[.="Тестировать если"])[1]'
directions_test_if_rezerv_1 = '(//*[@id="modalSettings"]//span[.="Тестировать если"])[2]'
directions_test_if_rezerv_2 = '(//*[@id="modalSettings"]//span[.="Тестировать если"])[3]'
# Метод тестирования
directions_test_method = '(//*[@id="modalSettings"]//span[.="Метод тестирования"])[1]'
directions_test_method_rezerv_1 = '(//*[@id="modalSettings"]//span[.="Метод тестирования"])[2]'
directions_test_method_rezerv_2 = '(//*[@id="modalSettings"]//span[.="Метод тестирования"])[3]'
# Тестировать
directions_test = '(//*[@id="modalSettings"]//span[.="Тестировать"])[1]'
directions_test_rezerv_1 = '(//*[@id="modalSettings"]//span[.="Тестировать"])[2]'
directions_test_rezerv_2 = '(//*[@id="modalSettings"]//span[.="Тестировать"])[3]'
# Дни недели
directions_days_of_th_week = '(//*[@id="modalSettings"]//span[.="Дни недели"])[1]'
directions_days_of_th_week_rezerv_1 = '(//*[@id="modalSettings"]//span[.="Дни недели"])[2]'
directions_days_of_th_week_rezerv_2 = '(//*[@id="modalSettings"]//span[.="Дни недели"])[3]'
# Количество повторов
directions_number_of_repetitions = '(//*[@id="modalSettings"]//span[.="Количество повторов"])[1]'
directions_number_of_repetitions_rezerv_1 = '(//*[@id="modalSettings"]//span[.="Количество повторов"])[2]'
directions_number_of_repetitions_rezerv_2 = '(//*[@id="modalSettings"]//span[.="Количество повторов"])[3]'
directions_number_of_repetitions_input = '(//div[@class = "channel-settings"])[1]//input[@maxlength="2"]'
directions_number_of_repetitions_input_rezerv_1 = '(//div[@class = "channel-settings"])[2]//input[@maxlength="2"]'
directions_number_of_repetitions_input_rezerv_2 = '(//div[@class = "channel-settings"])[3]//input[@maxlength="2"]'
# Адрес
directions_address = '(//*[@id="modalSettings"]//span[.="Адрес"])[1]'
directions_address_rezerv_1 = '(//*[@id="modalSettings"]//span[.="Адрес"])[2]'
directions_address_rezerv_2 = '(//*[@id="modalSettings"]//span[.="Адрес"])[3]'
directions_address_input = '(//div[@class = "channel-settings"])[1]//input[@maxlength="31"]'
directions_address_input_rezerv_1 = '(//div[@class = "channel-settings"])[2]//input[@maxlength="31"]'
directions_address_input_rezerv_2 = '(//div[@class = "channel-settings"])[3]//input[@maxlength="31"]'
# Порт
directions_port = '(//*[@id="modalSettings"]//span[.="Порт"])[1]'
directions_port_rezerv_1 = '(//*[@id="modalSettings"]//span[.="Порт"])[2]'
directions_port_rezerv_2 = '(//*[@id="modalSettings"]//span[.="Порт"])[3]'
directions_port_input = '(//div[@class = "channel-settings"])[1]//input[@maxlength="5"]'
directions_port_input_rezerv_1 = '(//div[@class = "channel-settings"])[2]//input[@maxlength="5"]'
directions_port_input_rezerv_2 = '(//div[@class = "channel-settings"])[3]//input[@maxlength="5"]'
# Канал соединения
directions_connection_channel = '(//*[@id="modalSettings"]//span[.="Канал соединения"])[1]'
directions_connection_channel_rezerv_1 = '(//*[@id="modalSettings"]//span[.="Канал соединения"])[2]'
directions_connection_channel_rezerv_2 = '(//*[@id="modalSettings"]//span[.="Канал соединения"])[3]'
# Таймаут подтверждения, сек
directions_confirmation_timeout_sec = '(//*[@id="modalSettings"]//span[.="Таймаут подтверждения, сек"])[1]'
directions_confirmation_timeout_sec_rezerv_1 = '(//*[@id="modalSettings"]//span[.="Таймаут подтверждения, сек"])[2]'
directions_confirmation_timeout_sec_rezerv_2 = '(//*[@id="modalSettings"]//span[.="Таймаут подтверждения, сек"])[3]'
directions_confirmation_timeout_sec_input = '((//div[@class = "channel-settings"])[1]//input[@maxlength="2"])[1]'
directions_confirmation_timeout_sec_input_rezerv_1 = '((//div[@class = "channel-settings"])[2]//input[@maxlength="2"])[1]'
directions_confirmation_timeout_sec_input_rezerv_2 = '((//div[@class = "channel-settings"])[3]//input[@maxlength="2"])[1]'
# Количество повторов
directions_number_of_repetitions_DC09 = '(//*[@id="modalSettings"]//span[.="Количество повторов"])[1]'
directions_number_of_repetitions_DC09_rezerv_1 = '(//*[@id="modalSettings"]//span[.="Количество повторов"])[2]'
directions_number_of_repetitions_DC09_rezerv_2 = '(//*[@id="modalSettings"]//span[.="Количество повторов"])[3]'
directions_number_of_repetitions_DC09_input = '(//*[@id="modalSettings"]//*[.="Количество повторов"]//input)[1]'
directions_number_of_repetitions_DC09_input_rezerv_1 = '(//*[@id="modalSettings"]//*[.="Количество повторов"]//input)[2]'
directions_number_of_repetitions_DC09_input_rezerv_2 = '(//*[@id="modalSettings"]//*[.="Количество повторов"]//input)[3]'
# Шифрование
directions_encryption = '(//*[@id="modalSettings"]//span[.="Шифрование"])[1]'
directions_encryption_rezerv_1 = '(//*[@id="modalSettings"]//span[.="Шифрование"])[2]'
directions_encryption_rezerv_2 = '(//*[@id="modalSettings"]//span[.="Шифрование"])[3]'
# Ключ шифрования
directions_encryption_key = '(//*[@id="modalSettings"]//span[.="Ключ шифрования"])[1]'
directions_encryption_key_rezerv_1 = '(//*[@id="modalSettings"]//span[.="Ключ шифрования"])[2]'
directions_encryption_key_rezerv_2 = '(//*[@id="modalSettings"]//span[.="Ключ шифрования"])[3]'
# Телефон
directions_phone_cod = '(//div[@class = "channel-settings"])[1]//input[contains(@class, "b-phone-code")]'
directions_phone_cod_rezerv_1 = '(//div[@class = "channel-settings"])[2]//input[contains(@class, "b-phone-code")]'
directions_phone_cod_rezerv_2 = '(//div[@class = "channel-settings"])[3]//input[contains(@class, "b-phone-code")]'
directions_phone_number = '(//div[@class = "channel-settings"])[1]//input[contains(@class, "b-phone-number")]'
directions_phone_number_rezerv_1 = '(//div[@class = "channel-settings"])[2]//input[contains(@class, "b-phone-number")]'
directions_phone_number_rezerv_2 = '(//div[@class = "channel-settings"])[3]//input[contains(@class, "b-phone-number")]'
