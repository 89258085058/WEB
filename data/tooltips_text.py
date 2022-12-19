"""Всплвающие подсказки"""

# Авторизация/подсказки:
login_tooltip_messege = 'Разрешен ввод: латинские буквы и цифры. Поле обязательно для заполнения. Максимальная длина: 63.'
password_tooltip_messege = 'Разрешен ввод: латинские буквы, цифры, символы. Поле обязательно для заполнения. Максимальная длина: 63.'

# Настройки/Объект/ПОЛЕ ВВОДА:
Settings_object_tooltip_messege_name_object = 'Тестовое обозначение объекта охраны, которое используется при трансляции событий в формате SMS.'
Settings_object_tooltip_messege_number_object = 'Номер объекта используется при трансляции событий посредством SMS в формате Эгида-3.'
Settings_object_tooltip_messege_take_delay = 'Задержка взятия на охрану разделов, для которых включена функция "Задержка взятия". Задержка предназначена для покидания пользователем охраняемого объекта после команды взятия разделов на охрану.'
Settings_object_tooltip_messege_input_alarm_delay = 'Задержка перехода раздела, взятого на охрану, в состояние "Тревога" при сработке извещателя с типом зоны "Вход". Задержка предназначена для снятия раздела с охраны пользователем при входе на охраняемый объект.'
Settings_object_tooltip_messege_input_auto_arm_time = 'Период проверки состояния разделов, имеющих статус "Тревога", для которых включена функция "Автовзятие из тревоги" и/или "Автовзятие из невзятия". Если на момент проверки все извещатели, включённые в раздел, перешли в состояние "Норма", происходит автоматическое взятие раздела на охрану.'
Settings_object_tooltip_messege_sensor_loss_alarm = 'При установке данного флага, если в разделе, взятом на охрану, происходит потеря радиосвязи с охранным датчиком, формируется событие "Тревога" по этому датчику.'
Settings_object_tooltip_messege_taking_with_lost_sensors = 'Разрешение взятия на охрану разделов, включающих устройства, с которыми потеряна радиосвязь.'
Settings_object_tooltip_messege_taking_with_sensors_in_alarm = 'Разрешение взятия на охрану разделов, включающих охранные датчики, находящихся в состоянии "Тревога".'
Settings_object_tooltip_messege_capturing_with_sensors_in_error = 'Разрешение взятия на охрану разделов, включающих охранные датчики, находящихся в состоянии "Неисправность".'
Settings_object_tooltip_messege_forced_take_from_alarm = 'Разрешение принудительного взятия на охрану разделов, включающих охранные датчики, находящиеся в состоянии "Тревога". Отличается от обычного взятия с датчиками в тревоге тем, что дальнейшее состояние этих датчиков будет игнорироваться, даже если они перейдут в норму. Рекомендуется использовать этот режим исключительно в случае неисправности датчиков.'

# Настройки/Дата и время:
Settings_date_time_tooltip_messege_gsm = 'Использовать время GSM сети'
Settings_date_time_tooltip_messege_ntp = 'Синхронизация по NTP/HTP'
Settings_date_time_tooltip_messege_hend = 'Вручную'
Settings_date_time_tooltip_messege_use_time_zone_of_GSM_network = 'Синхронизация часового пояса с оператором связи по сети GSM.'
Settings_date_time_tooltip_messege_daylight_Saving_Time = 'Синхронизация данных о летнем времени с оператором связи по сети GSM.'
Settings_date_time_tooltip_messege_ntp_server_address = '?????'
Settings_date_time_tooltip_messege_ntp_time_zon = 'Выбор часового пояса вручную.'
Settings_date_time_tooltip_messege_hend_date_time = 'Синхронизация данных о летнем времени с оператором связи по сети GSM.'

# Настройки/Прибор:
text_Enable_power_saving_mode = 'Прибор переходит в энергосберегающий режим при отсутствии внешнего сетевого источника питания. В этом режиме отсутствует звуковая и световая индикация и обрабатываются только регулярные обмены данными с радиоустройствами. Для корректной работы энергосберегающего режима к сигнальной панели не должно быть подключено радиобрелоков и исполнительных устройств. В этом режиме отсутствует звуковая и световая индикация и обрабатываются только регулярные обмены данными с радиоустройствами. Для корректной работы энергосберегающего режима к сигнальной панели не должно быть подключено радиобрелоков и исполнительных устройств.'
text_Allow_configuration_when_the_case_is_closed = 'Установка флага позволяет осуществлять удалённую настройку прибора, когда корпус сигнальной панели закрыт.'
text_Fix_partition_repeated_alarms = 'Если включено, то при сработке любого охранного датчика в разделе, где уже была тревога, вновь будет отправлено событие тревоги. Если выключено, то при сработке любого охранного датчика в разделе, где уже была тревога, нового события тревоги не будет до тех пор, пока раздел не будет повторно взят (вручную или автовзятием).'
text_Fix_repeated_sensor_alarms = 'Если включено, то при повторной сработке охранного датчика, вновь будет отправлено событие тревоги. Если выключено, то при повторной сработке охранного датчика, события тревоги не будет, если раздел до этого не был повторно взят (вручную или автовзятием).'
text_Fix_repeated_fire_alarms_in_a_section = '???'
text_Fix_repeated_fire_alarms_of_the_sensor = '???'
text_Fix_repeated_arming_disarming_events = 'Если включено, то при повторном взятии/снятии раздела, в журнал будет записано событие взятия/снятия раздела, независимо от предыдущего состояния раздела.'
text_Control_exits_when_re_arming_disarming = 'Если включено, то при повторном взятии/снятии раздела, сигнал о взятии/снятии будет передан на отработку в исполнительные устройства (сирены, релейные модули, выходы и т.д.), независимо от предыдущего состояния раздела.'

# Настройки/Световая индикация:
text_LED_mode_for_security_sensors = 'Позволяет глобально включить или выключить светодиодную индикацию на всех охранных датчиках сразу. Обратите внимание, постоянное включение индикации приведёт к быстрой разрядке элементов питания!'
text_LED_mode_for_fire_detectors = 'Позволяет глобально включить или выключить светодиодную индикацию на всех пожарных датчиках сразу. Обратите внимание, постоянное включение индикации приведёт к быстрой разрядке элементов питания!'
text_LED_mode_for_process_sensors = 'Позволяет глобально включить или выключить светодиодную индикацию на всех технологических датчиках сразу. Обратите внимание, постоянное включение индикации приведёт к быстрой разрядке элементов питания!'
text_Reader_operation_mode = 'Первое касание - статус, последующие управляющие. Один светодиод: первое касание ключа отображает статус управляемых разделов, последующие касания до истечения таймаута взятие/снятие.\n Первое касание - статус, второе - управляющее. Один светодиод: первое касание ключа отображает статус управляемых разделов, второе касание до истечения таймаута взятие/снятие. Третье касание будет аналогично первому.\n Первое касание - статус, последующие управляющие. Два светодиода: первый светодиод отображает реакцию на поднесение ключа, второй светодиод отображает статус управляемых разделов. В остальном поведение аналогично режиму с одним светодиодом.\n Первое касание - статус, второе - управляющее. Два светодиода: первый светодиод отображает реакцию на поднесение ключа, второй светодиод отображает статус управляемых разделов. В остальном поведение аналогично режиму с одним светодиодом.\n Любое касание - управляющее. Два светодиода: первое и последующие касания ключа производят взятие/снятие разделов. Статус разделов всегда отображается вторым светодиодом. ВНИМАНИЕ! Режим рекомендуется только если у всех пользователей одинаковые права доступа к охранным и пожарным разделам.'
text_Reader_indication_inversion = 'Инверсия управления светодиодом считывателя iButton.'

# Настройки/Звуковая индикация:
text_vol_indication_Volume_indication_ON = 'Включение/выключение всей звуковой индикации.'
text_vol_indication_Signal_duration = 'Настройка длительности непрерывной звуковой индикации событий "Тревога" и "Пожар".'
text_vol_indication_Event_volume = 'Настройка громкости звуковой индикации всех событий кроме "Тревога" и "Пожар".'
text_vol_indication_Alarm_volume = 'Настройка громкости звуковой индикации событий "Тревога" и "Пожар".'
text_vol_indication_Anxiety = 'Включение/выключение звуковой индикации тревоги в раздела, взятых на охрану.'
text_vol_indication_Fire = 'Включение/выключение звуковой индикации сработки пожарных датчиков.'
text_vol_indication_Taking_section = 'Включение/выключение звуковой индикации взятия разделов на охрану.'
text_vol_indication_Removing_partition = 'Включение/выключение звуковой индикации снятия разделов с охраны.'
text_vol_indication_Take_Delay = 'Включение/выключение звуковой индикации задержки взятия разделов на охрану.'
text_vol_indication_Not_taking = 'Включение/выключение звуковой индикации событий невзятия разделов на охрану.'
text_vol_indication_Sections_partially_taken = 'Включение/выключение звуковой индикации частичного взятия разделов на охрану.'
text_vol_indication_Adding_sensor = 'Включение/выключение звуковой индикации подключения к прибору радиоустройств.'
text_vol_indication_Bell = 'Включение/выключение звуковой индикации сработки извещателей в разделах, снятых с охраны.'

# Настройки/Радио:
text_Radio_Enable_radio = 'Включение/выключение модуля, обеспечивающего связь с радиоустройствами.'
text_Radio_Resolution_time_adding_new_sensors = 'Назначение времени автоматического выхода сигнальной панели из режима подключения радиоустройств.'
text_Radio_Channel = 'Назначение автоматического выбора радиоканала или выбор радиоканала вручную. При использовании нескольких сигнальных панелей следует назначать им разные радиоканалы.'
text_Radio_Sensor_polling_period = 'Период регулярных сеансов радиосвязи сигнальной панели с подключенными устройствами. Минимальный период опроса должен быть не менее: (количство подключенных РУ) х 0.31 секунд, с округлением в большую сторону. В энергосберегающем режиме извещения о сработке передаются только при регулярных сеансах радиосвязи.'

# Настройки/ GSM:
text_GSM_Enable_GSM_module = 'Включение/выключение модуля GSM.'
text_GSM_Use_GPRS = 'Включить мобильную передачу данных по GPRS, 3G, 4G и иным доступным сетям.'
text_GSM_Use_backup_SIM = 'Подключение резервной SIM-карты.'
text_GSM_Allow_USSD = 'Включает возможность отправлять USSD запросы через SMS командой P12345m, результат запроса будет перенаправлен на телефонный номер этого пользователя.'
text_GSM_Number_digits_number_to_check = 'При получении команды управления посредством SMS осуществляется проверка номера абонента на соответствие номерам в списке авторизованных пользователей системы. Количество проверяемых цифр считается с конца телефонного номера.'
text_GSM_Balance_Notification_Threshold = 'Значение баланса счета SIM-карты при котором прибор отправит уведомительное сообщение.'
text_GSM_Allow_Event_Broadcast = 'Снятие данного флага запрещает трансляцию событий по сети GSM для проведения настройки и тестирования работы системы без затрат на услуги оператора.'

# Настройки/ Ethernet:
text_Ethernet_MAC_address = 'Уникальный идентификатор, присваиваемый каждой единице активного оборудования.'
text_Ethernet_Server_name = 'Текстовое названия сервера. Для корректной работы имя должно содержать только латинские буквы и цифры.'
text_Ethernet_IPv4_address = 'Текущий адрес.'
text_Ethernet_Subnet_mask = 'Битовая маска для определения по IP-адресу адреса подсети и адреса узла этой подсети.'
text_Ethernet_Main_gate = 'Сетевой шлюз, на который пакет отправляется в том случае, если маршрут к сети назначения пакета не известен.'
text_Ethernet_Preferred_DNS_Server = 'DNS сервер который будет использоваться в первую очередь.'
text_Ethernet_Alternative_DNS_Server = 'DNS сервер используемый в случае проблем с сервером предпочтительным.'
text_Ethernet_Obtain_IPv4_address_settings_automatically = 'IP-адреса присваиваются устройствам сети автоматически без вмешательства администратора.'
text_Ethernet_Use_as_server = 'Использовать устройство в качестве сервера.'
text_Ethernet_Obtain_IPv6_address_DHCP_automatically = 'IP-адреса присваиваются устройствам сети автоматически без вмешательства администратора.'
text_Ethernet_Allow_remote_control = 'Удаленное управление системой через сеть интернет.'
text_Ethernet_Obtain_IPv6_address_SLAAC_automatically = 'Автоматическая настройка адреса без отслеживания состояния.'
text_Ethernet_Allow_insecure_HTTP_connection = 'Использовать незащищенное соединение.'
text_Ethernet_Establish_network_connections = 'Выбор приоритетного канала связи с Интернетом.'
text_Ethernet_Local_IPv6_address = 'Текущий адрес версии IPv6.'
text_Ethernet_Global_IPv6_Address = 'Адрес доступный из сети интернет.'
text_Ethernet_Preferred_IPv6_DNS_Server = 'DNS протокола IPv6 сервер который будет использоваться в первую очередь.'
text_Ethernet_Alternative_IPv6_DNS_Server = 'DNS версии протокола IPv6 сервер используемый в случае проблем с сервером предпочтительным.'

# Пользователи и ключи/Пользователи/ПОЛЕ ВВОДА:
text_U_K_user_administrator = 'Флаг предоставления пользователю прав администратора для доступа к настройкам системы.'
text_U_K_user_egida3 = 'Флаг установки режима работы с АРМ. Данный флаг необходимо установить, если пользователь создаётся для обеспечения управления системой со стороны АРМ посредством управляющих SMS-сообщений.'
text_U_K_user_name = 'Поле ввода имени пользователя системы. При получении команд управления от пользователя его имя записывается в Журнал и используется при формировании текстов транслируемых оповещений.'
text_U_K_user_login = 'Поле ввода имени пользователя для запуска Конфигуратора.'
text_U_K_user_password = 'Поле ввода пароля пользователя для запуска Конфигуратора.'
text_U_K_user_rep_password = 'Поле ввода контрольного повтора пароля.'
text_U_K_user_operator_message_forwarding = 'Флаг, при установке которого данному пользователю будут перенаправляться сообщения, поступившие на номер Блока от оператора связи и с других «коротких номеров».'
text_U_K_user_sending_out_of_broadcast = 'Флаг, при установке которого данному пользователю будет отправляться SMS-оповещение об управлении системой при помощи брелоков и ключей, привязанных к данному пользователю, даже если на его номер не настроена трансляция событий.'
text_U_K_user_group_of_outputs_controlled_by_SMS = 'Выбор групп выходов, управление которыми по SMS разрешено данному пользователю.'
text_U_K_user_group_of_outputs_with_call_control = 'Выбора группы выходов, управление которой по телефонному вызову разрешено данному пользователю.'
text_U_K_user_allow_withdrawal_by_SMS = 'Флаг разрешения на снятие с охраны управляемых разделов.'
text_U_K_user_allow_pickup_by_SMS = 'Флаг разрешения на взятие на охрану управляемых разделов.'
text_U_K_user_hone = 'Номер телефона используется как идентификатор пользователя при управлении системой посредством SMS и телефонного вызова, а также для трансляции событий.'
text_U_K_user_password_sms = 'Поле ввода пароля пользователя для управления системой посредством SMS-сообщений.'
text_U_K_user_rep_password_sms = 'Поле ввода контрольного повтора пароля.'
text_U_K_user_SMS_controlled_sections = 'Выпадающий список для выбора разделов системы, управление которыми посредством SMS разрешено данному пользователю.'

# Пользователи и ключи/Ключи/ПОЛЕ ВВОДА:
text_U_K_keys_id = ''
text_U_K_keys_user = 'Назначение пользователя, за которым закреплён данный ключ. Имя пользователя записывается в Журнал при использовании ключа.'
text_U_K_keys_permissions = 'Назначение набора прав управления.'
text_U_K_keys_path = 'Назначение разделов, на которые распространяются права управления данного ключа.'

# Зоны/Разделы/Разделы/ПОЛЕ ВВОДА:
text_path_number = 'Номер раздела для передачи в АРМ Орион, по-умолчанию он равен индексу раздела.'
text_path_name = 'Название раздела.'
text_path_control_sections = 'Список разделов, состояние которых является определяющим для данного раздела. Если все управляющие разделы взяты на охрану, управляемый раздел автоматически бертся на охрану. Если один из управляющих разделов снят с охраны, управляемый раздел автоматически снимается с охраны. Прямое (командой от пользователя) взятие или снятие с охраны управляемого раздела не предусмотрено.'
text_path_take_delay = 'Включение/выключение задержки взятия раздела на охрану.'
text_path_auto_pickup_from_non_pickup = 'Включение/выключение автоматического взятия раздела на охрану в том случае, если после события невзятия все извещатели перешли в состояние "Норма".'
text_path_auto_arm_from_alarm = 'Включение/выключение автоматического взятия раздела на охрану в том случае, если после события тревоги все извещатели перешли в состояние "Норма".'

# Направления/ПОЛЕ ВВОДА:
text_directions_name = 'Название направления.'
text_directions_path = 'Разделы по которым приходят события.'
text_directions_control_type = ''
text_directions_current_user = ''
text_directions_send_event_time = 'Добавить в оповещение время события.'
text_directions_send_event_date = 'Добавить в оповещение дату события.'
text_directions_enable_channel_testing = ''
text_directions_timeout_on_error = 'Пауза перед повторной попыткой отправки по каналу в секундах.'
text_directions_test_if = 'Независимое тестирование канала. В противном случае будет тестироваться только активный канал.'
text_directions_test_method = ''
text_directions_test = ''
text_directions_days_of_th_week = ''
text_directions_number_of_repetitions = 'Количество повторов'
text_directions_address = ''
text_directions_port = ''
text_directions_connection_channel = 'Выбор приоритетного канала связи с Интернет.'
text_directions_confirmation_timeout_sec = 'Период повтора DC-09, с которым будет повторяться сообщение в протоколе DC-09, при отсутствии подтверждения от сервера.'
text_directions_number_of_repetitions_DC09 = 'Число повторов DC-09.'
text_directions_encryption = ''
text_directions_encryption_key = ''

# --------------------ПОЛЯ ВВОДА--------------------------------------------
input_max_len_32 = 'Максимальная длина: 32 символа.'
input_numbers_1_9999 = 'Разрешен ввод только цифр. Минимальное значение: 1. Максимальное значение: 9999.'
input_numbers_0_9999 = 'Разрешен ввод только цифр. Минимальное значение: 0. Максимальное значение: 9999.'
input_numbers_1_9999_num = 'Разрешен ввод только цифр. Поле обязательно для заполнения. Минимальное значение: 1. Максимальное значение: 9999.'
input_65535_necessary = 'Разрешен ввод только цифр. Поле обязательно для заполнения. Минимальное значение: 1. Максимальное значение: 65535.'
input_server_address_23 = 'Разрешен ввод: латинские буквы, числа, ".", "-". Максимальная длина: 23.'
input_65535_not_necessary = 'Разрешен ввод только цифр. Минимальное значение: 1. Максимальное значение: 65535.'
input_0_65535_not_necessary = 'Разрешен ввод только цифр. Минимальное значение: 0. Максимальное значение: 65535.'
input_60_900 = 'Разрешен ввод только цифр. Поле обязательно для заполнения. Минимальное значение: 60. Максимальное значение: 900.'
input_5_120 = 'Разрешен ввод только цифр. Поле обязательно для заполнения. Минимальное значение: 5. Максимальное значение: 120.'
input_digits_11 = 'Разрешен ввод только цифр. Поле обязательно для заполнения. Минимальное значение: 0. Максимальное значение: 11.'
input_0_to_65535_necessary = 'Разрешен ввод только цифр. Поле обязательно для заполнения. Минимальное значение: 0. Максимальное значение: 65535.'
input_PIN = 'Разрешен ввод только цифр. Минимальное количество чисел: 4. Максимальное количество чисел: 9.'
input_USSD = 'Разрешен ввод: цифры, "*", "#". Максимальная длина: 31.'
input_APN = 'Разрешен ввод: латинские буквы, числа. Максимальная длина: 63.'
input_sim_user = 'Разрешен ввод: латинские буквы, числа. Максимальная длина: 63.'
input_sim_password = 'Разрешен ввод: латинские буквы, цифры, символы. Максимальная длина: 63.'
input_ipV4_necessary = 'Разрешен ввод: цифры, ".". Поле обязательно для заполнения.'
input_ipV4_no_necessary = 'Разрешен ввод: цифры, ".".'
input_ipV6 = 'Разрешен ввод: шестнадцатеричные цифры, ":".'
input_mac_address = 'Разрешен ввод: шестнадцатеричные цифры, ":", "-". Максимальная длина: 64.'
input_server_name = 'Разрешен ввод: латинские буквы, числа. Максимальная длина: 32.'
input_128 = 'Поле обязательно для заполнения. Максимальная длина: 128.'
input_login = 'Разрешен ввод: латинские буквы, числа, символы. Максимальная длина: 63.'
input_password_necessary = 'Разрешен ввод: латинские буквы, цифры, символы. Поле обязательно для заполнения. Максимальная длина: 63.'
input_phone_text_necessary = 'Введите допустимые символы. Поле обязательно для заполнения.'
input_phone_text_no_necessary = 'Введите допустимые символы.'
input_password_5 = 'Разрешен ввод: цифры. Поле обязательно для заполнения. Максимальная длина: 5.'
input_password_5_no_necessary = 'Разрешен ввод: цифры. Максимальная длина: 5.'
input_password_5_necessary = 'Разрешен ввод: цифры. Максимальная длина: 5.'
input_key_12 = 'Разрешен ввод: шестнадцатеричные цифры. Поле обязательно для заполнения. Максимальная длина: 12.'
input_name_95 = 'Разрешен ввод: Русские буквы, латинские буквы, спецсимволы, цифры. Максимальная длина: 95'
input_name_63 = 'Разрешен ввод: Русские буквы, латинские буквы, спецсимволы, цифры. Максимальная длина: 63'
input_hostname = ''
input_0_255 = 'Разрешен ввод только цифр. Минимальное значение: 0. Максимальное значение: 255.'
input_32768_ = 'Разрешен ввод: цифры, знак минус. Поле обязательно для заполнения. Минимальное значение: -32768. Максимальное значение: 32767.'
input_0_99 = 'Разрешен ввод только цифр. Минимальное значение: 0. Максимальное значение: 99.'
input_00_05__23_59 = 'Введите допустимые символы. Поле обязательно для заполнения. Минимальное значение: 00:05. Максимальное значение: 23:59'
