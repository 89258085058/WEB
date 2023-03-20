# -*- coding: utf-8 -*-

"""Информация на страницах"""

# Настройки/Объект
data_object = ['Настройки объекта', 'Название объекта', 'Номер объекта', 'Задержка взятия', 'Задержка тревоги входа',
               'Время автовзятия', 'Тревога при потере датчика', 'Взятие при потерянных датчиках',
               'Взятие при датчиках в тревоге', 'Взятие при датчиках в неисправности',
               'Принудительное взятие из тревоги', 'Сохранить']

# Настройки/Дата и время
data_date_time_gsm = ['Дата и время на устройстве', 'Использовать временную зону GSM сети',
                      'Переход на летнее время', 'Сохранить']
data_date_time_ntp = ['Дата и время на устройстве', 'Адрес сервера', 'Часовой пояс', 'Сохранить']
data_date_time_hand = ['Дата и время на устройстве', 'Дата и время', 'Часовой пояс', 'Сохранить']

# Настройки/Прибор
data_device = ['Включить энергосберегающий режим', 'Разрешить настройку при закрытом корпусе',
               'Фиксировать повторные тревоги раздела', 'Фиксировать повторные тревоги датчика',
               'Фиксировать повторные пожарные тревоги раздела', 'Фиксировать повторные пожарные тревоги датчика',
               'Фиксировать повторные события взятия/снятия', 'Управлять выходами при повторном взятии/снятии',
               'Сохранить']

# Настройки/Световая индикация
data_light_indication = ['Режим светодиодов для охранных датчиков', 'Режим светодиодов для пожарных датчиков',
                         'Режим светодиодов для технологических датчиков', 'Режим работы считывателя',
                         'Инверсия индикации считывателя', 'Сохранить']

# Настройки/Звуковая индикация
data_volum_indication = ['Включить', 'Длительность сигнала', 'Громкость событий', 'Громкость тревог', 'Тревога',
                         'Пожар',
                         'Взятие раздела', 'Снятие раздела', 'Задержка взятия', 'Невзятие', 'Разделы частично взяты',
                         'Добавление датчика', 'Колокольчик', 'Сохранить']

# Настройки/Радио
data_radio = ['Включить радиомодуль', 'Время разрешения добавления новых датчиков',
              'Канал', 'Период опроса датчиков', 'Сохранить']

# Настройки/Ethernet
data_ethernet = ['MAC адрес', 'Название сервера', 'Адрес IPv4', 'Маска подсети', 'Основной шлюз',
                 'Предпочтительный DNS сервер', 'Альтернативный DNS сервер',
                 'Получать IPv4 адрес и настройки автоматически', 'Использовать как сервер',
                 'Получать адрес IPv6 от DHCP автоматически', 'Разрешить удаленное управление',
                 'Получать адрес IPv6 от SLAAC автоматически', 'Разрешить незащищенное HTTP-соединение',
                 'Устанавливать сетевые подключения через', 'Локальный IPv6 адрес', 'Глобальный IPv6 адрес',
                 'Предпочтительный IPv6 DNS сервер', 'Альтернативный IPv6 DNS сервер', 'Сохранить']

# Настройки/gsm
data_gsm = ['Настройки GSM', 'Включить модуль GSM', 'Использовать GPRS', 'Использовать резервную SIM', 'Разрешить USSD',
            'Число знаков номера для проверки', 'Порог уведомления о балансе',
            'Разрешить трансляцию событий', 'PIN', 'USSD-код запроса баланса', 'APN', 'Пользователь', 'Пароль',
            'Сохранить', 'SIM 1', 'SIM 2']
# Настройки/gsm/modalsms
data_gsm_sms = ['Отправка тестового SMS', 'Номер телефона', 'Сообщение', 'Отменить', 'Отправить']

# Авторизация
data_auth = ['Добро пожаловать', 'Логин', 'Пароль', 'Войти']
# Положение чекбокса для рандомного выбора


# Пользователи и ключи/Пользователи
data_users = ['Общие настройки', 'Администратор', 'Режим Эгида3', 'Имя пользователя', 'Логин', 'Пароль',
              'Повторите пароль', 'Перенаправление сообщений оператора', 'Отправка вне трансляции', 'Выходы',
              'Группа выходов с управлением по SMS', 'Группа выходов с управлением звонком',
              'Разрешить снятие', 'Разрешить взятие', 'Телефон', 'Пароль SMS', 'Повторите пароль',
              'Управляемые разделы', 'Отменить', 'Сохранить']

# Пользователи и ключи/Ключи
data_keys = ['Идентификатор', 'Пользователь', 'Разрешения', 'Разделы', 'Отменить', 'Сохранить']

# Зоны/Разделы - Разделы - Добавить раздел
data_add_path = ['Номер', 'Название', 'Управляющие разделы', 'Задержка взятия', 'Автовзятие из невзятия',
                 'Автовзятие из тревоги', 'Отменить', 'Сохранить']

# Зоны/Разделы - Выходы - Выключен
data_out_off = ['Название', 'Режим работы', 'Выключен']

# Зоны/Разделы - Выходы - Событийный
data_out_event = ['Название', 'Режим работы', 'Событийный', 'Список событий', 'Взятие', 'Снятие',
                  'Принудительное взятие', 'Невзятие', 'Пожар', 'Тревога', 'Время', 'Включить по окончанию', 'Маска',
                  'Код настройки']

# Зоны/Разделы - Выходы - Температурный
data_out_temp = ['Название', 'Режим работы', 'Температурный', 'Гистерезис', 'Управляющий сенсор',
                 'Внутренний сигнал задания', 'Контрольный сенсор', 'Инверсия управления']

# Зоны/Разделы - Выходы - Управляемый
data_out_managed = ['Название', 'Режим работы', 'Управляемый', 'Маска включения', 'Маска выключения',
                    'Номер группы выходов', 'Разрешить управление по SMS', 'Разрешить управление звонком',
                    'Разрешить управление звонком']

# Зоны/Разделы - Сирены - Выключен
data_serena_off_1 = ['Световая индикация', 'Режим работы', 'Выключен']
data_serena_off_2 = ['Звуковая индикация', 'Режим работы', 'Выключен']

# Зоны/Разделы - Реле - Выключен
data_rele_off_1 = ['Выход 1', 'Режим работы', 'Выключен']
data_rele_off_2 = ['Выход 2', 'Режим работы', 'Выключен']

# Зоны/Разделы - Сирены - Событийный
data_serena_event_1 = ['Световая индикация', 'Режим работы', 'Событийный', 'Список событий', 'Взятие', 'Снятие',
                       'Принудительное взятие', 'Невзятие', 'Пожар', 'Тревога', 'Время', 'Включить по окончанию',
                       'Маска', 'Код настройки']

data_serena_event_2 = ['Звуковая индикация', 'Режим работы', 'Событийный', 'Список событий', 'Взятие', 'Снятие',
                       'Принудительное взятие', 'Невзятие', 'Пожар', 'Тревога', 'Время', 'Громкость',
                       'Включить по окончанию',
                       'Модуляция', 'Маска', 'Код настройки']

# Зоны/Разделы - Реле - Событийный
data_rele_event_1 = ['Выход 1', 'Режим работы', 'Событийный', 'Список событий', 'Взятие', 'Снятие',
                     'Принудительное взятие', 'Невзятие', 'Пожар', 'Тревога', 'Время', 'Включить по окончанию',
                     'Маска', 'Код настройки']

data_rele_event_2 = ['Выход 2', 'Режим работы', 'Событийный', 'Список событий', 'Взятие', 'Снятие',
                     'Принудительное взятие', 'Невзятие', 'Пожар', 'Тревога', 'Время', 'Включить по окончанию',
                     'Маска', 'Код настройки']

# Зоны/Разделы - Сирены - Температурный
data_serena_temp_1 = ['Световая индикация', 'Режим работы', 'Температурный', 'Гистерезис', 'Управляющий сенсор',
                      'Внутренний сигнал задания', 'Контрольный сенсор', 'Инверсия управления']
data_serena_temp_2 = ['Звуковая индикация', 'Режим работы', 'Температурный', 'Гистерезис', 'Управляющий сенсор',
                      'Внутренний сигнал задания', 'Контрольный сенсор', 'Инверсия управления']

# Зоны/Разделы - реле - Температурный
data_rele_temp_1 = ['Выход 1', 'Режим работы', 'Температурный', 'Гистерезис', 'Управляющий сенсор',
                    'Внутренний сигнал задания', 'Контрольный сенсор', 'Инверсия управления']
data_rele_temp_2 = ['Выход 2', 'Режим работы', 'Температурный', 'Гистерезис', 'Управляющий сенсор',
                    'Внутренний сигнал задания', 'Контрольный сенсор', 'Инверсия управления']

# Зоны/Разделы - Сирены - Управляемый
data_serena_managed_1 = ['Световая индикация', 'Режим работы', 'Управляемый', 'Маска включения', 'Маска выключения',
                         'Номер группы выходов', 'Разрешить управление по SMS', 'Разрешить управление звонком',
                         'Разрешить управление звонком']
data_serena_managed_2 = ['Звуковая индикация', 'Режим работы', 'Управляемый', 'Маска включения', 'Маска выключения',
                         'Номер группы выходов', 'Разрешить управление по SMS', 'Разрешить управление звонком',
                         'Разрешить управление звонком']

# Зоны/Разделы - реле - Управляемый
data_rele_managed_1 = ['Выход 1', 'Режим работы', 'Управляемый', 'Маска включения', 'Маска выключения',
                       'Номер группы выходов', 'Разрешить управление по SMS', 'Разрешить управление звонком',
                       'Разрешить управление звонком']
data_rele_managed_2 = ['Выход 2', 'Режим работы', 'Управляемый', 'Маска включения', 'Маска выключения',
                       'Номер группы выходов', 'Разрешить управление по SMS', 'Разрешить управление звонком',
                       'Разрешить управление звонком']

# Статус
path_status_text_content = ['Разделы']
batteries_status_text_content = ['Батареи', 'Состояние', 'Уровень заряда', 'Сопротивление', 'Ток', 'Напряжение']
gsm_status_text_content = ['Состояние GSM модуля', 'Питание', 'Активная SIM', 'Состояние сети', 'GPRS',
                           'Уровень сигнала', 'SIM 1', 'SIM 2']
power_status_text_content = ['Источник питания', 'Состояние', 'Напряжение']
ethernet_status_text_content = ['Сеть', 'Состояние', 'Напряжение']
device_status_text_content = ['Состояние прибора', 'Корпус', 'Энергосберегающий режим']
others_status_text_content = ['Прочее', 'Основной источник питания', 'Напряжение']
device_option_status_text_content = ['Прибор', 'Перезагрузка прибора', 'Сброс к заводским настройкам',
                                     'Перезагрузить', 'Сбросить']
gsm_status_text_content_SIM = ['Оператор', 'Баланс', 'Запросить баланс', 'Тестовое SMS']

# Обнавления
update_device_text_content = ['Текущая версия ПО', 'Сигнал GSM P:', 'Загрузчик',
                              'Базовая:', 'Радио', 'Сборка:']
update_louder_text_content = ['Обновление прошивки',
                              'Кликните сюда для выбора файла прошивки или перетащите его на страницу']

# Зоны/Разделы - Брелоки
data_brelok = ['Тип датчика', 'Включение датчика', 'Название', 'Пользователь', 'Раздел',
               'Управляемые разделы', 'Способ вызова тихой тревоги', 'Группа выходов кнопки 1',
               'Группа выходов кнопки 2', 'Снятие', 'Взятие', 'Отключить сирену']

# Зоны/Разделы - Датчики - с2000р ИК
data_c_2000p_ik = ['Тип датчика', 'Тип зоны', 'Включение датчика', 'Название', 'Раздел', 'Режим "Колокольчик"',
                   'Режим индикации', 'Энергосберегающий режим', 'Чувствительность', 'Режим тестирования']

# Зоны/Разделы - Датчики - с2000р СМК
data_c_2000p_smk = ['Тип датчика', 'Тип зоны', 'Включение датчика', 'Название', 'Раздел', 'Режим "Колокольчик"',
                    'Режим индикации', 'Состояние КЦ', 'Сопротивление КЦ', 'Включение режима "Антисаботаж"',
                    'Включаемые модули']

# Зоны/Разделы - Датчики - с2000р ИРП
data_c_2000p_irp = ['Тип датчика', 'Тип зоны', 'Включение датчика', 'Название', 'Раздел', 'Режим "Колокольчик"',
                    'Режим индикации']

# Зоны/Разделы - Датчики - КЦ Сигнал-GSM
data_sensor_kc = ['Тип датчика', 'Тип зоны', 'Включение датчика', 'Название', 'Раздел', 'Режим "Колокольчик"',
                  'Сопротивление КЦ', 'Период перехода датчика в норму']

# Зоны/Разделы - Датчики - с2000р СДВИГ
data_c_2000p_sdvig = ['Тип датчика', 'Тип зоны', 'Включение датчика', 'Название', 'Раздел', 'Режим индикации',
                      'Режим "Колокольчик"', 'Контроль сдвига', 'Контроль наклона', 'Фиксирование датчика наклона',
                      'Энергосберегающий режим', 'Зафиксировать текущее положение', 'Контроль геркона',
                      'Порог тревоги по наклону', 'Порог тревоги по перемещению']

# Зоны/Разделы - Датчики - с2000р ДИП
data_c_2000p_dip = ['Тип датчика', 'Тип зоны', 'Включение датчика', 'Название', 'Раздел', 'Режим "Колокольчик"',
                    'Режим индикации', 'Запылённость', 'Задымлённость']

# Зоны/Разделы - Датчики - с2000р ИП
data_c_2000p_ip = ['Тип датчика', 'Тип зоны', 'Включение датчика', 'Название', 'Раздел', 'Режим "Колокольчик"',
                   'Режим индикации', 'Температура', 'Гистерезис', 'Нижний порог по температуре',
                   'Верхний порог по температуре', 'Режим уведомлений', 'Вскрытие корпуса']
