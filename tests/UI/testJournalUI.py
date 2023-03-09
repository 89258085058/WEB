# -*- coding: utf-8 -*-
import allure
import pytest

reruns = 1


@pytest.fixture()
def open_tab_journal(app):
    with allure.step("Открытие вкладки 'Журнал'"):
        app.PO_Navigations.goToJournalPage()
    with allure.step("Зачистка журнала от событий"):
        app.endpoint.delete_all_events()


@pytest.fixture(scope='class')
def set_name_for_exit_two(app):
    with allure.step("Установка имнени для второго выхода"):
        app.PO_Journal.set_name_for_exit_two()


@allure.label("owner", 'Александр Санталов')
@allure.epic("Тесты Журнал")
@allure.feature("Проверки UI")
@pytest.mark.flaky(reruns=reruns)
class TestUIJournalChapter1:

    @allure.story("Проверка события EvtFromSensor")
    @pytest.mark.parametrize("z_event, description",
                             [
                                 (0, 'Неизвестно'),
                                 (1, 'Не присвоен раздел'),
                                 (2, 'Готов'),
                                 (3, 'Тревога'),
                                 (4, 'Тревога входа'),
                                 (5, 'Нападение'),
                                 (6, 'Пожар!'),
                                 (7, 'Пожар! Ручной извещатель'),
                                 (8, 'ШС замкнут'),
                                 (9, 'ШС оборван'),
                                 (10, 'ШС низкое сопротивление'),
                                 (11, 'ШС высокое сопротивление'),
                                 (12, 'ШС в норме'),
                                 (13, 'Корпус открыт'),
                                 (14, 'Корпус закрыт'),
                                 (15, 'Потерян'),
                                 (16, 'Связь восстановлена'),
                                 (17, 'Основная батарея в норме'),
                                 (18, 'Низкий заряд батареи'),
                                 (19, 'Резервная батарея в норме'),
                                 (20, 'Ошибка резервной батареи'),
                                 (21, 'Ошибка устройства'),
                                 (22, 'Проверка связи'),
                                 (23, 'Обрыв шлейфа датчика воды'),
                                 (24, 'Протечка'),
                                 (25, 'Датчик выключен'),
                                 (26, 'Отметка наряда'),
                                 (27, 'Взятие разделов на охрану'),
                                 (28, 'Снятие разделов с охраны'),
                                 (29, 'Перезагрузка датчика'),
                                 (30, 'Принудительное взятие разделов на охрану'),
                                 (34, 'Событие саботажа по СМК'),
                                 (35, 'Событие \"Колокольчик\"'),
                                 (36, 'Количество событий по зоне')
                             ])
    def test_evt_from_sensor(self, app, extend_time, open_tab_journal, z_event, description):
        with allure.step(f"Проверка события"):
            app.PO_Journal.event_evt_from_sensor(z_event, description)

    @allure.story("Проверка события EvtFromSensor")
    @pytest.mark.parametrize("z_event, description",
                             [
                                 (31, 'Событие по температуре'),
                                 (32, 'Событие по влажности'),
                                 (33, 'Событие по датчику CO')
                             ])
    @pytest.mark.parametrize("type_evt, value_type_evt",
                             [
                                 ('Переход в норму.', 0),
                                 ('Ниже нормы.', 1),
                                 ('Выше нормы.', 2),
                             ])
    def test_evt_from_sensor_climate(self, app, extend_time, open_tab_journal, z_event, description, type_evt, value_type_evt):
        with allure.step(f"Проверка события"):
            app.PO_Journal.event_evt_from_sensor_climate(z_event, description, type_evt, value_type_evt)

    @allure.story("Проверка события EvtFromKey")
    @pytest.mark.parametrize("p_event, description",
                             [
                                 (0, 'События нет'),
                                 (1, 'Раздел не используется'),
                                 (2, 'Невзятие'),
                                 (3, 'Ожидание квитанции'),
                                 (4, 'Раздел снят'),
                                 (5, 'Автовзятие'),
                                 (6, 'Задержка взятия'),
                                 (7, 'Принудительное взятие раздела'),
                                 (8, 'Квитанция получена'),
                                 (9, 'Раздел взят'),
                                 (10, 'Тревога входа'),
                                 (11, 'Тревога'),
                                 (12, 'Пожара нет'),
                                 (13, 'Пожар'),
                                 (14, 'Пожар по ручному извещателю'),
                                 (15, 'Тихая тревога'),
                                 (16, 'Включение выхода'),
                                 (17, 'Выключение выхода'),
                                 (18, 'Отметка наряда'),
                                 (19, 'Протечка воды'),
                                 (20, 'Сброс оповещателей тревоги и пожара'),
                                 (21, 'Свободное событие'),
                                 (22, 'Переключение выхода')
                             ])
    def test_evt_from_key(self, app, extend_time, open_tab_journal, p_event, description):
        with allure.step(f"Проверка события"):
            app.PO_Journal.event_evt_from_key(p_event, description)

    @allure.story("Проверка событий EvtFromGSM, EvtFromAutotake, EvtFromKeychain, EvtFromWebInterface, "
                  "EvtFromRemoteWebInterface, EvtFromOrion, EvtFromUsb")
    @pytest.mark.parametrize("p_event, description",
                             [
                                 (0, 'События нет'),
                                 (1, 'Раздел не используется'),
                                 (2, 'Невзятие'),
                                 (3, 'Ожидание квитанции'),
                                 (4, 'Раздел снят'),
                                 (5, 'Автовзятие'),
                                 (6, 'Задержка взятия'),
                                 (7, 'Принудительное взятие раздела'),
                                 (8, 'Квитанция получена'),
                                 (9, 'Раздел взят'),
                                 (10, 'Тревога входа'),
                                 (11, 'Тревога'),
                                 (12, 'Пожара нет'),
                                 (13, 'Пожар'),
                                 (14, 'Пожар по ручному извещателю'),
                                 (15, 'Тихая тревога'),
                                 (16, 'Включение выхода'),
                                 (17, 'Выключение выхода'),
                                 (18, 'Отметка наряда'),
                                 (19, 'Протечка воды'),
                                 (20, 'Сброс оповещателей тревоги и пожара'),
                                 (21, 'Свободное событие'),
                                 (22, 'Переключение выхода')
                             ])
    @pytest.mark.parametrize("type_evt, value_type_evt",
                             [
                                 ('Управление по SMS', 4),
                                 ('Автовзятие', 14),
                                 ('Брелок', 2),
                                 ('Локальный Web-интерфейс', 17),
                                 ('Удалённое управление через Web-интерфейс', 22),
                                 ('Орион', 18),
                                 ('Управление по USB', 21)
                             ])
    def test_evt_from_matrix(self, app, extend_time, open_tab_journal, p_event, description, type_evt, value_type_evt):
        with allure.step(f"Проверка события"):
            app.PO_Journal.event_evt_from_matrix(p_event, description, type_evt, value_type_evt)

    '''События для приборов'''

    @allure.story("Проверка события EvtFromBL")
    @pytest.mark.parametrize("value_bievent, description",
                             [
                                 (36, 'Команда отмены запуска процесса обновления ПО загрузчиком'),
                                 (37, 'Команда однократной отмены отката ПО на базовую или резервную'),
                                 (38, 'Запись нового значения CRC без отката ПО на резервную'),
                                 (39, 'Полное отключение отката ПО. Использовать только при отладке'),
                                 (40, 'Команда ручного обновления на новую версию ПО'),
                                 (41, 'Команда ручного обновления на базовую версию ПО'),
                                 (42, 'Обновление ПО на новую версию из внешней памяти'),
                                 (43, 'Обновление ПО на базовую копию'),
                                 (44, 'Откат ПО на новую версию из внешней памяти'),
                                 (45, 'Откат ПО на базовую копию'),
                                 (46, 'Все копии ПО повреждены, возможно новая версия ПО просто ещё не имеет CRC и '
                                      'её надо перезаписать'),
                                 (47, 'Обновление ПО загрузчика'),
                                 (48, 'Автоматическая запись новой базовой версии ПО во внешнюю память при её '
                                      'повреждении или отсутствии'),
                                 (49, 'Автоматическая запись новой версии ПО во внешнюю память при её повреждении '
                                      'или отсутствии'),
                                 (50, 'Автоматическая запись базовой версии ПО в память при её повреждении или'
                                      ' отсутствии'),
                                 (51, 'Внешняя копия ПО повреждена, обновление невозможно'),
                                 (52, 'Базовая копия ПО повреждена, обновление невозможно'),
                                 (53, 'Новая копия ПО загрузчика повреждена, обновление невозможно'),
                                 (54, 'Статус работы загрузчика, при отсутствии событий записи/обновления/отката '
                                      'прошивок'),
                                 (55, 'Очистка основной копии ПО'),
                                 (56, 'Очистка базовой копии ПО'),
                                 (57, 'Очистка внешней копии ПО'),
                                 (58, 'Обновление ПО загрузчика начато'),
                                 (59, 'Обновление ПО на новую внешнюю копию прошло успешно'),
                                 (60, 'Обновление ПО на базовую копию прошло успешно'),
                                 (61, 'Ошибка проверки CRC у внешних данных'),
                                 (62, 'Ошибка обновления на новую внешнюю копию ПО'),
                                 (63, 'Ошибка обновления на базовую копию ПО'),
                                 (64, 'Ошибка восстановления базовой копии ПО'),
                                 (65, 'Ошибка восстановления внешней копии ПО'),
                                 (66, 'Ошибка обновления на новую прошивку из-за несоответствия аппаратной версии'),
                                 (67, 'Ошибка проверки CRC')
                             ])
    def test_evt_from_bl(self, app, extend_time, open_tab_journal, value_bievent, description):
        with allure.step(f"Проверка события"):
            app.PO_Journal.event_evt_from_bl(value_bievent, description)

    @allure.story("Проверка события EvtFromFW")
    @pytest.mark.parametrize("value_event, description",
                             [
                                 (1, 'ПО радио успешно обновлено'),
                                 (2, 'Ошибка обновления ПО радио'),
                                 (3, 'ПО радио успешно восстановлено'),
                                 (4, 'Ошибка восстановления ПО радио'),
                                 (5, 'ПО РУ успешно обновлено'),
                                 (6, 'Ошибка обновления ПО РУ'),
                                 (7, 'Отмена обновления ПО РУ'),

                             ])
    def test_evt_from_fw(self, app, extend_time, open_tab_journal, value_event, description):
        with allure.step(f"Проверка события {description}"):
            app.PO_Journal.event_evt_from_fw(value_event, description)

    @allure.story("Проверка события EvtFromTimeSync")
    @pytest.mark.parametrize("value_event, description",
                             [
                                 (0, 'Успешная синхронизация по NITZ'),
                                 (1, 'Успешная синхронизация по NTP'),
                                 (2, 'Успешная синхронизация по HTP'),
                                 (3, 'Часовой пояс синхронизирован'),
                                 (4, 'Летнее время синхронизировано'),
                                 (5, 'Ошибка синхронизации (не используется)'),
                                 (6, 'Ошибка синхронизации по NITZ'),
                                 (7, 'Ошибка синхронизации по NTP'),
                                 (8, 'Ошибка синхронизации по HTP'),
                                 (9, 'Ошибка синхронизации часового пояса'),
                                 (10, 'Ошибка синхронизации летнего времени'),
                                 (11, 'Синхронизация времени по PSUTTZ выполнена успешно'),
                                 (12, 'Ошибка синхронизации времени по PSUTTZ'),
                             ])
    def test_evt_from_time_sync(self, app, extend_time, open_tab_journal, value_event, description):
        with allure.step(f"Проверка события"):
            app.PO_Journal.event_evt_from_time_sync(value_event, description)


@allure.label("owner", 'Александр Санталов')
@allure.epic("Тесты Журнал")
@allure.feature("Проверки UI")
@pytest.mark.flaky(reruns=reruns)
class TestUIJournalChapter2:

    @allure.story("Проверка события EvtFromPS")
    @pytest.mark.parametrize("value_event, description",
                             [
                                 (1, 'Сетевое питание отключено'),
                                 (2, 'Слишком низкое напряжение сетевого питания'),
                                 (3, 'Слишком высокое напряжение сетевого питания'),
                                 (4, 'Сетевое питание в норме'),
                                 (5, 'Внешний источник питания отключен'),
                                 (6, 'Слишком низкое напряжение внешнего источника питания'),
                                 (7, 'Слишком высокое напряжение внешнего источника питания'),
                                 (8, 'Внешний источник питания в норме'),
                                 (9, 'Внешняя батарея отключена'),
                                 (10, 'Внешняя батарея разряжена'),
                                 (11, 'Слишком низкое напряжение внешней батареи'),
                                 (12, 'Слишком высокое напряжение внешней батареи'),
                                 (13, 'Внешняя батарея в норме'),
                                 (14, 'Аккумулятор разряжен'),
                                 (15, 'Высокое внутреннее сопротивление аккумулятора'),
                                 (16, 'Аккумулятор не подключен или подключен неверно'),
                                 (17, 'Аккумулятор в норме'),
                                 (18, 'Аккумулятор заряжен'),
                                 (19, 'Аккумулятор заряжается'),
                                 (20, 'Аккумулятор балансируется'),
                                 (21, 'Питание от сети не предусмотрено в этом исполнении прибора'),
                                 (22, 'Питание от внешнего источника не предусмотрено в этом исполнении прибора'),
                                 (23, 'Питание от внешней батареи не предусмотрено в этом исполнении прибора')
                             ])
    def test_evt_from_ps(self, app, extend_time, open_tab_journal, value_event, description):
        with allure.step(f"Проверка события"):
            app.PO_Journal.event_evt_from_ps(value_event, description)

    @allure.story("Проверка события EvtFromLogin")
    @pytest.mark.parametrize("value_login_status, description",
                             [
                                 (1, 'Успешная аутентификация'),
                                 (2, 'Выход пользователя'),
                                 (3, 'Автоматический выход при бездействии пользователя в течении одной минуты'),
                                 (4, 'Ошибка аутентификации'),
                             ])
    @pytest.mark.parametrize("type_auth, value_type_auth",
                             [
                                 ('USB', 0),
                                 ('SMS', 1),
                                 ('WEB', 2),
                             ])
    def test_evt_from_login(self, app, extend_time, open_tab_journal, value_login_status, description, type_auth, value_type_auth):
        with allure.step(f"Проверка события"):
            app.PO_Journal.event_evt_from_login(value_login_status, description, type_auth, value_type_auth)

    @allure.story("Проверка события EvtFromGSMmodule")
    @pytest.mark.parametrize("value_event, description",
                             [
                                 (0, 'Связь восcтановлена'),
                                 (1, 'GSM включен'),
                                 (2, 'GSM выключен'),
                                 (3, 'Низкий уровень сигнала'),
                                 (4, 'Уровень сигнала перешёл в норму'),
                                 (5, 'Зарегистрирован в домашней сети'),
                                 (6, 'Отсутствует регистрация в домашней сети'),
                                 (7, 'SIM-карта отсутствует или неизвестная сеть'),
                                 (8, 'Поиск сети'),
                                 (9, 'SIM-карта изменена'),
                                 (10, 'Зарегистрирован в роуминге'),
                                 (11, 'Имя оператора'),
                                 (12, 'Ошибка ввода PIN'),
                                 (13, 'Ошибка ввода PUK'),
                                 (14, 'PIN введен успешно'),
                                 (15, 'PUK введен успешно'),
                                 (16, 'Отключение по причине перехода основного питания на USB'),
                                 (17, 'Модуль перезагружен'),
                                 (18, 'PIN успешно изменён'),
                                 (19, 'Ошибка изменения PIN кода'),
                                 (20, 'Включена защита доступа к GSM по PIN коду'),
                                 (21, 'Ошибка включения защиты доступа к GSM по PIN коду'),
                                 (22, 'Выключена защита доступа к GSM по PIN коду'),
                                 (23, 'Ошибка выключения защиты доступа к GSM по PIN коду'),
                                 (24, 'Ошибка. Сим-карта не готова'),
                                 (25, 'Ошибка. Сим-карта отсутствует')
                             ])
    def test_evt_from_gsm_module(self, app, extend_time, open_tab_journal, value_event, description):
        with allure.step(f"Проверка события"):
            app.PO_Journal.event_evt_from_gsm_module(value_event, description)

    @allure.story("Проверка события EvtFromChannel")
    @pytest.mark.parametrize("value_status, description",
                             [
                                 (0, 'Событие передано'),
                                 (1, 'Ошибка передачи'),
                                 (2, 'Передача не удалась'),
                                 (4, 'Отсутствует направление'),
                                 (5, 'Повторная попытка отправки'),
                             ])
    def test_evt_from_channel(self, app, extend_time, open_tab_journal, value_status, description):
        with allure.step(f"Проверка события"):
            app.PO_Journal.event_evt_from_channel(value_status, description)

    @allure.story("Проверка события EvtFromTest")
    @pytest.mark.parametrize("value_test_type, description",
                             [
                                 (0, 'Смс'),
                                 (1, 'Звонок'),
                                 (2, 'Смс эгида 3'),
                             ])
    @pytest.mark.parametrize("state, value_state",
                             [
                                 ('Успешная передача', 0),
                                 ('Ошибка передачи', 1),
                             ])
    @pytest.mark.parametrize("channel, value_channel",
                             [
                                 ('Основной', 0),
                                 ('Резервный', 1),
                                 ('Второй резервный', 2),
                             ])
    def test_evt_from_test(self, app, extend_time, open_tab_journal, value_test_type, description, state, value_state, channel, value_channel):
        with allure.step(f"Проверка события"):
            app.PO_Journal.event_evt_from_test(value_test_type, description, state, value_state, channel, value_channel)

    @allure.story("Проверка события EvtTextString")
    @pytest.mark.parametrize("value_source, description",
                             [
                                 (0, 'Источник неизвестен'),
                                 (1, 'Неподдерживаемое СМС от пользователя')
                             ])
    def test_evt_from_text_string(self, app, extend_time, open_tab_journal, value_source, description):
        with allure.step(f"Проверка события"):
            app.PO_Journal.event_evt_from_text_string(value_source, description)

    @allure.story("Проверка события EvtFromOutput")
    @pytest.mark.parametrize("value_out_event_type, description_out_event_type, value, description",
                             [
                                 (0, 'Внешнее управление', 0, 'Выход Выключен'),
                                 (0, 'Внешнее управление', 1, 'Выход Включен'),
                                 (1, 'Событийное', 0, 'События нет'),
                                 (1, 'Событийное', 1, 'Раздел не используется'),
                                 (1, 'Событийное', 2, 'Невзятие'),
                                 (1, 'Событийное', 3, 'Ожидание квитанции'),
                                 (1, 'Событийное', 4, 'Раздел снят'),
                                 (1, 'Событийное', 5, 'Автовзятие'),
                                 (1, 'Событийное', 6, 'Задержка взятия'),
                                 (1, 'Событийное', 7, 'Принудительное взятие раздела'),
                                 (1, 'Событийное', 8, 'Квитанция получена'),
                                 (1, 'Событийное', 9, 'Раздел взят'),
                                 (1, 'Событийное', 10, 'Тревога входа'),
                                 (1, 'Событийное', 11, 'Тревога'),
                                 (1, 'Событийное', 12, 'Пожара нет'),
                                 (1, 'Событийное', 13, 'Пожар'),
                                 (1, 'Событийное', 14, 'Пожар по ручному извещателю'),
                                 (1, 'Событийное', 15, 'Тихая тревога'),
                                 (1, 'Событийное', 16, 'Включение выхода'),
                                 (1, 'Событийное', 17, 'Выключение выхода'),
                                 (1, 'Событийное', 18, 'Отметка наряда'),
                                 (1, 'Событийное', 19, 'Протечка воды'),
                                 (1, 'Событийное', 20, 'Сброс оповещателей тревоги и пожара'),
                                 (1, 'Событийное', 21, 'Свободное событие'),
                                 (1, 'Событийное', 22, 'Переключение выхода'),
                                 (2, 'Cобытие по температуре', 0, 'Выход Выключен'),
                                 (2, 'Cобытие по температуре', 1, 'Выход Включен'),
                                 (3, 'Неисправность', 0, 'Cостояние выхода ещё не определено'),
                                 (3, 'Неисправность', 1, 'Аварии выхода нет'),
                                 (3, 'Неисправность', 2, 'Выход перегружен'),
                                 (3, 'Неисправность', 3, 'Выход замкнут'),
                                 (3, 'Неисправность', 4, 'На выходе низкое напряжение'),
                                 (3, 'Неисправность', 5, 'Обрыв выхода')
                             ])
    def test_evt_from_output(self, app, extend_time, set_name_for_exit_two, open_tab_journal, value_out_event_type,
                             description_out_event_type, value, description):
        with allure.step(f"Проверка события"):
            app.PO_Journal.event_evt_from_output(value_out_event_type, description_out_event_type, value, description)

    @allure.story("Проверка события EvtSystem")
    @allure.title("Проверка отображение событий для EvtSystem по параметрам "
                  "SYS_EVENT_ADD_SENSOR и SYS_EVENT_DEL_SENSOR")
    @pytest.mark.parametrize("value_sys_evt_type, description_sys_evt_type",
                             [(1, 'Добавлен датчик'),
                              (2, 'Удалён датчик')])
    @pytest.mark.parametrize("value_sensor_type, description_sensor_type",
                             [(0, 'С2000Р-АРР32/Сигнал GSM'),
                              (1, 'С2000Р-АРР32'),
                              (3, 'С2000Р-ИПР'),
                              (4, 'С2000Р-СМК'),
                              (5, 'С2000Р-ДИП'),
                              (6, 'С2000Р-ИК'),
                              (7, 'С2000Р-Сирена'),
                              (8, 'Сигнал GSM Р исп. 0 Основной модуль'),
                              (9, 'КЦ'),
                              (10, 'С2000Р-ВТИ'),
                              (11, 'С2000Р-БУ'),
                              (13, 'С2000Р-АСР2'),
                              (14, 'С2000Р-РМ'),
                              (15, 'С2000Р-РМ исп. 1'),
                              (16, 'С2000Р-Сдвиг'),
                              (17, 'С2000Р-СТ'),
                              (18, 'С2000Р-ШИК'),
                              (19, 'С2000Р-АСР1'),
                              (20, 'С2000Р-ОСТ'),
                              (21, 'С2000Р-Датчик пламени 207'),
                              (22, 'С2000Р-Датчик пламени 609'),
                              (23, 'С2000Р-СП'),
                              (24, 'С2000Р-Сдвиг исп.01'),
                              (25, 'С2000Р-Сдвиг исп.02'),
                              (26, 'С2000Р-ИК исп.02'),
                              (27, 'С2000Р-ПИРОН'),
                              (28, 'С2000Р-ПИРОН-Ш'),
                              (29, 'С2000Р-ДЗ'),
                              (30, 'С2000Р-РР'),
                              (31, 'С2000Р-ВТИ исп.01'),
                              (32, 'С2000Р-КТ'),
                              (33, 'С2000Р-Грация исп.53'),
                              (34, 'С2000Р-СТ исп.01'),
                              (35, 'Сигнал GSM Р исп. 1 Основной модуль'),
                              (36, 'Сигнал GSM Р исп. 2 Основной модуль'),
                              (37, 'Сигнал GSM Р исп. 0 Радиоканальный модуль'),
                              (38, 'Сигнал GSM Р исп. 1 Радиоканальный модуль'),
                              (39, 'Сигнал GSM Р исп. 2 Радиоканальный модуль'),
                              (40, 'C2000-КРСПИ + АРР32(127) Радиоканальный модуль'),
                              (41, 'C2000-КРСПИ + АРР32(127) Основной модуль'),
                              (46, 'Загрузчик для Сигнал GSM Р исп. 0'),
                              (47, 'Загрузчик для Сигнал GSM Р исп. 1'),
                              (48, 'Загрузчик для Сигнал GSM Р исп. 2'),
                              (49, 'С2000Р-ОСТ (220В)'),
                              (50, 'С2000Р-ОСТ (24В)'),
                              (51, 'С2000Р-РР исп.01'),
                              (52, 'С2000Р-Грация исп.55'),
                              (53, 'С2000Р-ДЗ сер.01'),
                              (54, 'С2000-РПИ исп. 2'),
                              (55, 'С2000Р-ДЗ исп.01'),
                              (56, 'С2000Р-АСР1 исп 01'),
                              (57, 'С2000Р-Розетка'),
                              (63, 'С2000Р-УДП'),
                              (64, 'С2000Р-УДП исп.02'),
                              (65, 'С2000Р-ОПР'),
                              (66, 'Количество поддерживаемых типов устройств С2000Р')
                              ])
    def test_evt_from_system_action_sensor(self, app, extend_time, open_tab_journal, value_sys_evt_type,
                                           description_sys_evt_type, value_sensor_type, description_sensor_type):
        with allure.step(f"Проверка события"):
            app.PO_Journal.event_evt_from_system_action_sensor(value_sys_evt_type, description_sys_evt_type,
                                                               value_sensor_type, description_sensor_type)

    @allure.story("Проверка события EvtSystem")
    @allure.title("Проверка отображение событий для EvtSystem по параметрам "
                  "SYS_EVENT_ADD_KEY, SYS_EVENT_UPD_KEY и SYS_EVENT_DEL_KEY")
    @pytest.mark.parametrize("value_sys_evt_type, description_sys_evt_type",
                             [
                                 (3, 'Добавлен ключ'),
                                 (4, 'Обновлён ключ'),
                                 (5, 'Удалён ключ')
                             ])
    @pytest.mark.parametrize("value_access_law, description_access_law",
                             [
                                 (1, 'Не настроен уровень доступа ключа. Данный ключ занесён в память прибора, '
                                     'однако ему не назначены какие-либо права управления'),
                                 (2, 'Взятие/снятие разделов. Данному ключу разрешено брать '
                                     'и снимать с охраны указанные разделы'),
                                 (3, 'Взятие разделов. Данному ключу разрешено только взятие '
                                     'на охрану выбранных разделов'),
                                 (4, 'Снятие разделов. Данному ключу разрешено только снятие '
                                     'с охраны выбранных разделов'),
                                 (5, 'Отметка наряда. По факту приложения ключа к считывателю формируется событие '
                                     '"Отметка наряда", которое может передаваться по каналам трансляции')
                             ])
    def test_evt_from_system_action_key(self, app, extend_time, open_tab_journal, value_sys_evt_type,
                                        description_sys_evt_type, value_access_law, description_access_law):
        with allure.step(f"Проверка события "):
            app.PO_Journal.event_evt_from_system_action_key(value_sys_evt_type, description_sys_evt_type,
                                                            value_access_law, description_access_law)

    @allure.story("Проверка события EvtSystem")
    @allure.title("Проверка отображение событий для EvtSystem")
    @pytest.mark.parametrize("value_sys_evt_type, description_sys_evt_type",
                             [
                                 (8, 'Добавлено или изменено направление'),
                                 (9, 'Удалено направление'),
                                 (10, 'Событие от загрузчика'),
                                 (13, 'Устройство было перезагружено'),
                                 (14, 'Баланс ниже порога')
                             ])
    def test_evt_from_system(self, app, extend_time, open_tab_journal, value_sys_evt_type, description_sys_evt_type):
        with allure.step(f"Проверка события {description_sys_evt_type}"):
            app.PO_Journal.event_evt_from_system(value_sys_evt_type, description_sys_evt_type)

    @allure.story("Проверка события EvtSystem")
    @allure.title("Проверка отображение событий для EvtSystem")
    @pytest.mark.parametrize("value_sys_evt_type, description_sys_evt_type, value_settings_changes",
                             [
                                 (6, 'Добавлен или изменен пользователь', 0),
                                 (6, 'Добавлен или изменен пользователь', 255),
                                 (7, 'Удалён пользователь', 0),
                             ])
    def test_evt_from_system_add_and_delete_user(self, app, extend_time, open_tab_journal, value_sys_evt_type,
                                                 description_sys_evt_type, value_settings_changes):
        with allure.step(f"Проверка события {description_sys_evt_type}"):
            app.PO_Journal.event_evt_from_system_add_and_delete_user(value_sys_evt_type, description_sys_evt_type,
                                                                     value_settings_changes)

    @allure.story("Проверка события EvtSystem")
    @allure.title("Проверка отображение событий для EvtSystem по параметру SYS_EVENT_CASE_STATE")
    @pytest.mark.parametrize("value_sys_evt_type, description_sys_evt_type, value_state, value_description",
                             [
                                 (11, 'Событие открытия корпуса прибора', 0, 'Вскрытие корпуса'),
                                 (12, 'Событие закрытия корпуса прибора', 1, 'Закрытие корпуса')
                             ])
    @pytest.mark.parametrize("p_event, description",
                             [
                                 (2, 'Невзятие'),
                                 (3, 'Ожидание квитанции'),
                                 (4, 'Раздел снят'),
                                 (5, 'Автовзятие'),
                                 (6, 'Задержка взятия'),
                                 (7, 'Принудительное взятие раздела'),
                                 (8, 'Квитанция получена'),
                                 (9, 'Раздел взят'),
                                 (10, 'Тревога входа'),
                                 (11, 'Тревога'),
                                 (12, 'Пожара нет'),
                                 (13, 'Пожар'),
                                 (14, 'Пожар по ручному извещателю'),
                                 (15, 'Тихая тревога'),
                                 (16, 'Включение выхода'),
                                 (17, 'Выключение выхода'),
                                 (18, 'Отметка наряда'),
                                 (19, 'Протечка воды'),
                                 (20, 'Сброс оповещателей тревоги и пожара'),
                                 (21, 'Свободное событие'),
                                 (22, 'Переключение выхода')
                             ])
    def test_evt_from_system_case_state(self, app, extend_time, open_tab_journal, value_sys_evt_type, description_sys_evt_type,
                                        value_state, value_description, p_event, description):
        with allure.step(f"Проверка события"):
            app.PO_Journal.event_evt_from_system_case_state(value_sys_evt_type, description_sys_evt_type,
                                                            value_state, value_description, p_event, description)

    @pytest.mark.skip('Не разработано на фронте')
    @allure.story("Проверка события EvtFromControlCommand")
    @allure.title("Проверка отображение событий для EvtFromControlCommand")
    @pytest.mark.parametrize("value_state, description_state",
                             [
                                 (4000, 'Ошибка разбора'),
                                 (4001, 'Ошибка параметров'),
                                 (4002, 'Не поддерживаемая команда'),
                                 (4003, 'Не исполненная команда'),
                                 (4004, 'Неправильный пароль'),
                                 (4006, 'Нет прав администратора')
                             ])
    def test_evt_from_control_command(self, app, extend_time, open_tab_journal, value_state, description_state):
        with allure.step(f"Проверка события"):
            app.PO_Journal.event_evt_from_сontrol_сommand(value_state, description_state)

# *********************************************************************************************************************

    @allure.title("Проверка отображение страницы")
    def test_display_items_on_journal_page(self, app, extend_time, open_tab_journal):
        with allure.step("Проверка элементов на страницу"):
            app.PO_Journal.display_items_on_journal_page()

    @allure.title("Результаты фильтрации по разным полям")
    def test_result_filters_for_fields(self, app, extend_time, open_tab_journal):
        with allure.step("Проверка результата фильтрации"):
            app.PO_Journal.assert_result_filters_for_fields()

    @allure.title("Сброс результатов фильтрации")
    def test_reset_result_filters(self, app, extend_time, open_tab_journal):
        with allure.step("Проверка сброса"):
            app.PO_Journal.assert_reset_result_filters()


@allure.label("owner", 'Александр Санталов')
@allure.epic("Тесты Журнал")
@allure.feature("Валидация полей ввода")
@pytest.mark.flaky(reruns=reruns)
class TestJournalValidation:

    @allure.story("Журнал")
    @allure.title("Проверка ввода значений в поле 'Поиск'")
    def test_display_items_on_journal_page(self, app, extend_time, open_tab_journal):
        with allure.step("Проверка валидации поля"):
            app.PO_Zone_Path.input_seach()
