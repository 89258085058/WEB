# -*- coding: utf-8 -*-
import allure
import pytest
from selenium.webdriver.common.by import By

reruns = 1

# directions_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
directions_list = ['1']


@pytest.fixture
def users_settings(app):
    with allure.step("Переход на страницу Пользователи и ключи"):
        app.PO_Navigations.goToUsersKeysPage()
    with allure.step("Переход на вкладку 'Пользователи'"):
        app.PO_Navigations.goToUsersPage()
    with allure.step("Нажать на кнопку 'Настройки'"):
        app.PO_Users_Keys.PushUserSettingsButton()


@pytest.fixture
def keys_settings(app):
    with allure.step("Переход на страницу Пользователи и ключи"):
        app.PO_Navigations.goToUsersKeysPage()
    with allure.step("Переход на вкладку 'Ключи'"):
        app.PO_Navigations.goToKeysPage()
    with allure.step("Нажать на кнопку 'Настройки'"):
        app.PO_Users_Keys.PushKeysSettingsButton()


@pytest.fixture
def add_path(app):
    with allure.step("Переход на страницу Зоны Разделы"):
        app.PO_Navigations.goToZonePathPage()
    with allure.step("Переход на вкладку 'Разделы'"):
        app.PO_Navigations.goToPathPage()
    with allure.step("Нажать на кнопку 'Добавить раздел'"):
        app.PO_Zone_Path.add_path()


@pytest.fixture
def destination(app):
    with allure.step("Переход на страницу направления"):
        app.PO_Navigations.goToDirectionsPage()


@pytest.fixture()
def close_modal(request, app):
    def fin():
        app.method.click((By.XPATH, '(//*[.=" Отменить "]//div)[last()]'))

    request.addfinalizer(fin)


@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты ВСПЛЫВАЮЩИЕ ПОДСКАЗКИ")
@allure.feature("Настройки")
@pytest.mark.flaky(reruns=reruns)
class Test01TooltipsMassege:

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Объект - Название объекта")
    def test_settings_object_tooltip_1(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Объект'"):
            app.PO_Navigations.goToObjectPage()
        with allure.step("Проверка подсказки: Название объекта"):
            app.PO_Tooltips.tooltip_settings_object_name()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Объект - Номер объекта")
    def test_settings_object_tooltip_2(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Объект'"):
            app.PO_Navigations.goToObjectPage()
        with allure.step("Проверка подсказки: Номер объекта"):
            app.PO_Tooltips.tooltip_settings_object_number()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Объект - Задержка взятия")
    def test_settings_object_tooltip_3(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Объект'"):
            app.PO_Navigations.goToObjectPage()
        with allure.step("Проверка подсказки: Задержка взятия"):
            app.PO_Tooltips.tooltip_settings_take_delay()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Объект - Задержка тревоги входа")
    def test_settings_object_tooltip_4(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Объект'"):
            app.PO_Navigations.goToObjectPage()
        with allure.step("Проверка подсказки: Задержка тревоги входа"):
            app.PO_Tooltips.tooltip_settings_object_delay_alarm_enter()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Объект - Время автовзятия")
    def test_settings_object_tooltip_5(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Объект'"):
            app.PO_Navigations.goToObjectPage()
        with allure.step("Проверка подсказки: Время автовзятия"):
            app.PO_Tooltips.tooltip_settings_object_time_auto_take_on()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Объект - Тревога при потере датчика")
    def test_settings_object_tooltip_6(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Объект'"):
            app.PO_Navigations.goToObjectPage()
        with allure.step("Проверка подсказки: Тревога при потере датчика"):
            app.PO_Tooltips.tooltip_settings_object_sensor_loss_alarm()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Объект - Взятие при потерянных датчиках")
    def test_settings_object_tooltip_7(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Объект'"):
            app.PO_Navigations.goToObjectPage()
        with allure.step("Проверка подсказки: Взятие при потерянных датчиках"):
            app.PO_Tooltips.tooltip_settings_object_taking_with_lost_sensors()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Объект - Взятие при датчиках в тревоге")
    def test_settings_object_tooltip_8(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Объект'"):
            app.PO_Navigations.goToObjectPage()
        with allure.step("Проверка подсказки: Взятие при датчиках в тревоге"):
            app.PO_Tooltips.tooltip_settings_object_taking_with_sensors_in_alarm()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Объект - Взятие при датчиках в неисправности")
    def test_settings_object_tooltip_9(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Объект'"):
            app.PO_Navigations.goToObjectPage()
        with allure.step("Проверка подсказки: Взятие при датчиках в неисправности"):
            app.PO_Tooltips.tooltip_settings_object_capturing_with_sensors_in_error()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Объект - Принудительное взятие из тревогии")
    def test_settings_object_tooltip_9(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Объект'"):
            app.PO_Navigations.goToObjectPage()
        with allure.step("Проверка подсказки: Принудительное взятие из тревогии"):
            app.PO_Tooltips.tooltip_settings_object_forced_take_from_alarm()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Дата и время - Использовать время GSM сети")
    def test_settings_date_time_tooltip_GSM_1(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Дата и время'"):
            app.PO_Navigations.goToDateTimePage()
        with allure.step("Клик по кнопке 'Редактировать'"):
            app.PO_Settings.edit_button_click()
        with allure.step("Выбор: Использовать время GSM сети"):
            app.PO_Settings.Use_GSM_network_time_click()
        with allure.step("Проверка подсказки: Использовать время GSM сети"):
            app.PO_Tooltips.tooltip_settings_date_time_drop_list_gsm()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Дата и время - Использовать время GSM сети - Использовать временную зону GSM сети")
    def test_settings_date_time_tooltip_GSM_2(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Дата и время'"):
            app.PO_Navigations.goToDateTimePage()
        with allure.step("Клик по кнопке 'Редактировать'"):
            app.PO_Settings.edit_button_click()
        with allure.step("Выбор: Использовать время GSM сети"):
            app.PO_Settings.Use_GSM_network_time_click()
        with allure.step("Проверка подсказки: Использовать временную зону GSM сети"):
            app.PO_Tooltips.tooltip_settings_date_time_drop_list_use_gsm()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Дата и время - Использовать время GSM сети - Переход на летнее время")
    def test_settings_date_time_tooltip_GSM_3(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Дата и время'"):
            app.PO_Navigations.goToDateTimePage()
        with allure.step("Клик по кнопке 'Редактировать'"):
            app.PO_Settings.edit_button_click()
        with allure.step("Выбор: Использовать время GSM сети"):
            app.PO_Settings.Use_GSM_network_time_click()
        with allure.step("Проверка подсказки: Переход на летнее время"):
            app.PO_Tooltips.tooltip_settings_date_time_daylight_Saving_Time()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Дата и время - Синхронизация по NTP/HTP")
    def test_settings_date_time_tooltip_ntp_1(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Дата и время'"):
            app.PO_Navigations.goToDateTimePage()
        with allure.step("Клик по кнопке 'Редактировать'"):
            app.PO_Settings.edit_button_click()
        with allure.step("Выбор: Синхронизация по NTP/HTP"):
            app.PO_Settings.Synchronization_via_NTP_HTP_click()
        with allure.step("Проверка подсказки: Синхронизация по NTP/HTP"):
            app.PO_Tooltips.tooltip_settings_date_time_drop_list_ntp()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Дата и время - Синхронизация по NTP/HTP - Адрес сервера")
    def test_settings_date_time_tooltip_ntp_2(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Дата и время'"):
            app.PO_Navigations.goToDateTimePage()
        with allure.step("Клик по кнопке 'Редактировать'"):
            app.PO_Settings.edit_button_click()
        with allure.step("Выбор: Синхронизация по NTP/HTP"):
            app.PO_Settings.Synchronization_via_NTP_HTP_click()
        with allure.step("Проверка подсказки: Адрес сервера"):
            app.PO_Tooltips.tooltip_settings_date_time_drop_list_ntp_adress_server()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Дата и время - Синхронизация по NTP/HTP - Часовой пояс")
    def test_settings_date_time_tooltip_ntp_3(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Дата и время'"):
            app.PO_Navigations.goToDateTimePage()
        with allure.step("Клик по кнопке 'Редактировать'"):
            app.PO_Settings.edit_button_click()
        with allure.step("Выбор: Синхронизация по NTP/HTP"):
            app.PO_Settings.Synchronization_via_NTP_HTP_click()
        with allure.step("Проверка подсказки: Часовой пояс"):
            app.PO_Tooltips.tooltip_settings_date_time_drop_list_ntp_server_time_zone()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Дата и время - Вручную")
    def test_settings_date_time_tooltip_manual_1(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Дата и время'"):
            app.PO_Navigations.goToDateTimePage()
        with allure.step("Клик по кнопке 'Редактировать'"):
            app.PO_Settings.edit_button_click()
        with allure.step("Выбор: Вручную"):
            app.PO_Settings.Manually_click()
        with allure.step("Проверка подсказки: Вручную"):
            app.PO_Tooltips.tooltip_settings_date_time_drop_list_hend()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Дата и время - Вручную - Дата и время")
    def test_settings_date_time_tooltip_manual_2(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Дата и время'"):
            app.PO_Navigations.goToDateTimePage()
        with allure.step("Клик по кнопке 'Редактировать'"):
            app.PO_Settings.edit_button_click()
        with allure.step("Выбор: Вручную"):
            app.PO_Settings.Manually_click()
        with allure.step("Проверка подсказки: Дата и время"):
            app.PO_Tooltips.tooltip_settings_date_time_drop_list_hend_date_time()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Дата и время - Вручную - Часовой пояс")
    def test_settings_date_time_tooltip_manual_3(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Дата и время'"):
            app.PO_Navigations.goToDateTimePage()
        with allure.step("Клик по кнопке 'Редактировать'"):
            app.PO_Settings.edit_button_click()
        with allure.step("Выбор: Вручную"):
            app.PO_Settings.Manually_click()
        with allure.step("Проверка подсказки: Часовой пояс"):
            app.PO_Tooltips.tooltip_settings_date_time_drop_list_hend_time_zone()

    # чекбокс выпилен согласно ТЗ
    # @allure.story("Проверка подсказок наименования поля")
    # @allure.title("Прибор - Включить энергосберегающий режим")
    # def test_settings_device_tooltip_1(self, app):
    #     with allure.step("Переход на страницу Настройки"):
    #         app.PO_Navigations.goToSettingsPage()
    #     with allure.step("Переход на вкладку 'Прибор'"):
    #         app.PO_Navigations.goToDevicePage()
    #     with allure.step("Проверка подсказки: Включить энергосберегающий режим"):
    #         app.PO_Tooltips.tooltip_settings_device_enable_power_saving_mode()


@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты ВСПЛЫВАЮЩИЕ ПОДСКАЗКИ")
@allure.feature("Настройки")
@pytest.mark.flaky(reruns=reruns)
class Test02TooltipsMassege:

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Прибор - Разрешить настройку при закрытом корпусе")
    def test_settings_device_tooltip_2(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Прибор'"):
            app.PO_Navigations.goToDevicePage()
        with allure.step("Проверка подсказки: Разрешить настройку при закрытом корпусе"):
            app.PO_Tooltips.tooltip_settings_device_Allow_configuration_when_the_case_is_closed()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Прибор - Фиксировать повторные тревоги раздела")
    def test_settings_device_tooltip_3(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Прибор'"):
            app.PO_Navigations.goToDevicePage()
        with allure.step("Проверка подсказки: Фиксировать повторные тревоги раздела"):
            app.PO_Tooltips.tooltip_settings_device_Fix_partition_repeated_alarms()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Прибор - Фиксировать повторные тревоги датчика")
    def test_settings_device_tooltip_4(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Прибор'"):
            app.PO_Navigations.goToDevicePage()
        with allure.step("Проверка подсказки: Фиксировать повторные тревоги датчика"):
            app.PO_Tooltips.tooltip_settings_device_Fix_repeated_sensor_alarms()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Прибор - Фиксировать повторные пожарные тревоги раздела")
    def test_settings_device_tooltip_5(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Прибор'"):
            app.PO_Navigations.goToDevicePage()
        with allure.step("Проверка подсказки: Фиксировать повторные пожарные тревоги раздела"):
            app.PO_Tooltips.tooltip_settings_device_Fix_repeated_fire_alarms_in_a_section()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Прибор - Фиксировать повторные пожарные тревоги датчика")
    def test_settings_device_tooltip_6(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Прибор'"):
            app.PO_Navigations.goToDevicePage()
        with allure.step("Проверка подсказки: Фиксировать повторные пожарные тревоги датчика"):
            app.PO_Tooltips.tooltip_settings_device_Fix_repeated_fire_alarms_of_the_sensor()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Прибор - Фиксировать повторные события взятия/снятия")
    def test_settings_device_tooltip_7(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Прибор'"):
            app.PO_Navigations.goToDevicePage()
        with allure.step("Проверка подсказки: Фиксировать повторные события взятия/снятия"):
            app.PO_Tooltips.tooltip_settings_device_Fix_repeated_arming_disarming_events()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Прибор - Управлять выходами при повторном взятии/снятии")
    def test_settings_device_tooltip_8(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Прибор'"):
            app.PO_Navigations.goToDevicePage()
        with allure.step("Проверка подсказки: Управлять выходами при повторном взятии/снятии"):
            app.PO_Tooltips.tooltip_settings_device_Control_exits_when_re_arming_disarming()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Световая индикация - Режим светодиодов для охранных датчиков")
    def test_settings_light_indications_tooltip_1(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Световая индикация'"):
            app.PO_Navigations.goToLightIndicationPage()
        with allure.step("Проверка подсказки: Режим светодиодов для охранных датчиков"):
            app.PO_Tooltips.tooltip_settings_light_indications_LED_mode_for_security_sensors()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Световая индикация - Режим светодиодов для пожарных датчиков")
    def test_settings_light_indications_tooltip_2(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Световая индикация'"):
            app.PO_Navigations.goToLightIndicationPage()
        with allure.step("Проверка подсказки: Режим светодиодов для пожарных датчиков"):
            app.PO_Tooltips.tooltip_settings_light_indications_LED_mode_for_fire_detectors()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Световая индикация - Режим светодиодов для технологических датчиков")
    def test_settings_light_indications_tooltip_3(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Световая индикация'"):
            app.PO_Navigations.goToLightIndicationPage()
        with allure.step("Проверка подсказки: Режим светодиодов для технологических датчиков"):
            app.PO_Tooltips.tooltip_settings_light_indications_LED_mode_for_process_sensors()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Световая индикация - Режим светодиодов для технологических датчиков")
    def test_settings_light_indications_tooltip_4(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Световая индикация'"):
            app.PO_Navigations.goToLightIndicationPage()
        with allure.step("Проверка подсказки: Режим работы считывателя"):
            app.PO_Tooltips.tooltip_settings_light_indications_Reader_operation_mode()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Световая индикация - Инверсия индикации считывателя")
    def test_settings_light_indications_tooltip_5(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Световая индикация'"):
            app.PO_Navigations.goToLightIndicationPage()
        with allure.step("Проверка подсказки: Инверсия индикации считывателя"):
            app.PO_Tooltips.tooltip_settings_light_indications_Reader_indication_inversion()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Звуковая индикация - Включить")
    def test_settings_volume_indications_tooltip_1(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Звуковая индикация'"):
            app.PO_Navigations.goToVolumIndicationPage()
        with allure.step("Проверка подсказки: Включить"):
            app.PO_Tooltips.tooltip_settings_volum_indications_ON()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Звуковая индикация - Длительность сигнала")
    def test_settings_volume_indications_tooltip_2(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Звуковая индикация'"):
            app.PO_Navigations.goToVolumIndicationPage()
        with allure.step("Проверка подсказки: Длительность сигнала"):
            app.PO_Tooltips.tooltip_settings_volum_indications_Signal_duration()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Звуковая индикация - Громкость событий")
    def test_settings_volume_indications_tooltip_3(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Звуковая индикация'"):
            app.PO_Navigations.goToVolumIndicationPage()
        with allure.step("Проверка подсказки: Громкость событий"):
            app.PO_Tooltips.tooltip_settings_volum_indications_Event_volume()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Звуковая индикация - Громкость тревог")
    def test_settings_volume_indications_tooltip_4(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Звуковая индикация'"):
            app.PO_Navigations.goToVolumIndicationPage()
        with allure.step("Проверка подсказки: Громкость тревог"):
            app.PO_Tooltips.tooltip_settings_volum_indications_Alarm_volume()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Звуковая индикация - Тревога")
    def test_settings_volume_indications_tooltip_5(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Звуковая индикация'"):
            app.PO_Navigations.goToVolumIndicationPage()
        with allure.step("Открытие 'Связанные события'"):
            app.PO_Settings.open_volum_indication_events()
        with allure.step("Проверка подсказки: Тревога"):
            app.PO_Tooltips.tooltip_settings_volum_indications_Anxiety()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Звуковая индикация - Пожар")
    def test_settings_volume_indications_tooltip_6(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Звуковая индикация'"):
            app.PO_Navigations.goToVolumIndicationPage()
        with allure.step("Открытие 'Связанные события'"):
            app.PO_Settings.open_volum_indication_events()
        with allure.step("Проверка подсказки: Пожар"):
            app.PO_Tooltips.tooltip_settings_volum_indications_Fire()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Звуковая индикация - Взятие раздела")
    def test_settings_volume_indications_tooltip_7(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Звуковая индикация'"):
            app.PO_Navigations.goToVolumIndicationPage()
        with allure.step("Открытие 'Связанные события'"):
            app.PO_Settings.open_volum_indication_events()
        with allure.step("Проверка подсказки: Взятие раздела"):
            app.PO_Tooltips.tooltip_settings_volum_indications_Taking_section()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Звуковая индикация - Снятие раздела")
    def test_settings_volume_indications_tooltip_8(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Звуковая индикация'"):
            app.PO_Navigations.goToVolumIndicationPage()
        with allure.step("Открытие 'Связанные события'"):
            app.PO_Settings.open_volum_indication_events()
        with allure.step("Проверка подсказки: Снятие раздела"):
            app.PO_Tooltips.tooltip_settings_volum_indications_Removing_partition()


@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты ВСПЛЫВАЮЩИЕ ПОДСКАЗКИ")
@allure.feature("Настройки")
@pytest.mark.flaky(reruns=reruns)
class Test03TooltipsMassege:

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Звуковая индикация - Задержка взятия")
    def test_settings_volume_indications_tooltip_9(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Звуковая индикация'"):
            app.PO_Navigations.goToVolumIndicationPage()
        with allure.step("Открытие 'Связанные события'"):
            app.PO_Settings.open_volum_indication_events()
        with allure.step("Проверка подсказки: Задержка взятия"):
            app.PO_Tooltips.tooltip_settings_volum_indications_Take_Delay()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Звуковая индикация - Невзятие")
    def test_settings_volume_indications_tooltip_10(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Звуковая индикация'"):
            app.PO_Navigations.goToVolumIndicationPage()
        with allure.step("Открытие 'Связанные события'"):
            app.PO_Settings.open_volum_indication_events()
        with allure.step("Проверка подсказки: Невзятие"):
            app.PO_Tooltips.tooltip_settings_volum_indications_Not_taking()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Звуковая индикация - Разделы частично взяты")
    def test_settings_volume_indications_tooltip_11(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Звуковая индикация'"):
            app.PO_Navigations.goToVolumIndicationPage()
        with allure.step("Открытие 'Связанные события'"):
            app.PO_Settings.open_volum_indication_events()
        with allure.step("Проверка подсказки: Разделы частично взяты"):
            app.PO_Tooltips.tooltip_settings_volum_indications_Sections_partially_taken()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Звуковая индикация - Добавление датчика")
    def test_settings_volume_indications_tooltip_12(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Звуковая индикация'"):
            app.PO_Navigations.goToVolumIndicationPage()
        with allure.step("Открытие 'Связанные события'"):
            app.PO_Settings.open_volum_indication_events()
        with allure.step("Проверка подсказки: Добавление датчика"):
            app.PO_Tooltips.tooltip_settings_volum_indications_Adding_sensor()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Звуковая индикация - Колокольчик")
    def test_settings_volume_indications_tooltip_13(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Звуковая индикация'"):
            app.PO_Navigations.goToVolumIndicationPage()
        with allure.step("Открытие 'Связанные события'"):
            app.PO_Settings.open_volum_indication_events()
        with allure.step("Проверка подсказки: Колокольчик"):
            app.PO_Tooltips.tooltip_settings_volum_indications_Bell()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Радио - Включить радиомодуль")
    def test_settings_wireless_tooltip_1(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Радио'"):
            app.PO_Navigations.goToRadioPage()
        with allure.step("Клик по кнопке 'Редактировать'"):
            app.PO_Settings.edit_button_click()
        with allure.step("Включение радиомодуля"):
            app.PO_Settings.check_box_radio_on()
        with allure.step("Проверка подсказки: Включить радиомодуль"):
            app.PO_Tooltips.tooltip_settings_radio_Enable_radio()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Радио - Время разрешения добавления новых датчиков")
    def test_settings_wireless_tooltip_2(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Радио'"):
            app.PO_Navigations.goToRadioPage()
        with allure.step("Клик по кнопке 'Редактировать'"):
            app.PO_Settings.edit_button_click()
        with allure.step("Включение радиомодуля"):
            app.PO_Settings.check_box_radio_on()
        with allure.step("Проверка подсказки: Время разрешения добавления новых датчиков"):
            app.PO_Tooltips.tooltip_settings_radio_Resolution_time_adding_new_sensor()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Радио - Канал")
    def test_settings_wireless_tooltip_3(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Радио'"):
            app.PO_Navigations.goToRadioPage()
        with allure.step("Клик по кнопке 'Редактировать'"):
            app.PO_Settings.edit_button_click()
        with allure.step("Включение радиомодуля"):
            app.PO_Settings.check_box_radio_on()
        with allure.step("Проверка подсказки: Канал"):
            app.PO_Tooltips.tooltip_settings_radio_Channel()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Радио - Период опроса датчиков")
    def test_settings_wireless_tooltip_4(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Радио'"):
            app.PO_Navigations.goToRadioPage()
        with allure.step("Клик по кнопке 'Редактировать'"):
            app.PO_Settings.edit_button_click()
        with allure.step("Включение радиомодуля"):
            app.PO_Settings.check_box_radio_on()
        with allure.step("Проверка подсказки: Период опроса датчиков"):
            app.PO_Tooltips.tooltip_settings_radio_Sensor_polling_period()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("GSM - Включить модуль GSM")
    def test_settings_gsm_tooltip_1(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'GSM'"):
            app.PO_Navigations.goToGSMPage()
        with allure.step("Проверка подсказки: Включить модуль GSM"):
            app.PO_Tooltips.tooltip_settings_gsm_Enable_GSM_module()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("GSM - Использовать GPRS")
    def test_settings_gsm_tooltip_2(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'GSM'"):
            app.PO_Navigations.goToGSMPage()
        with allure.step("Проверка подсказки: Использовать GPRS"):
            app.PO_Tooltips.tooltip_settings_gsm_Use_GPRS()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("GSM - Использовать резервную SIM")
    def test_settings_gsm_tooltip_3(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'GSM'"):
            app.PO_Navigations.goToGSMPage()
        with allure.step("Проверка подсказки: Использовать резервную SIM"):
            app.PO_Tooltips.tooltip_settings_gsm_Use_backup_SIM()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("GSM - Разрешить USSD")
    def test_settings_gsm_tooltip_4(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'GSM'"):
            app.PO_Navigations.goToGSMPage()
        with allure.step("Проверка подсказки: Разрешить USSD"):
            app.PO_Tooltips.tooltip_settings_gsm_Allow_USSD()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("GSM - Число знаков номера для проверки")
    def test_settings_gsm_tooltip_5(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'GSM'"):
            app.PO_Navigations.goToGSMPage()
        with allure.step("Проверка подсказки: Число знаков номера для проверки"):
            app.PO_Tooltips.tooltip_settings_gsm_Number_digits_number_to_check()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("GSM - Порог уведомления о балансе")
    def test_settings_gsm_tooltip_6(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'GSM'"):
            app.PO_Navigations.goToGSMPage()
        with allure.step("Проверка подсказки: Порог уведомления о балансе"):
            app.PO_Tooltips.tooltip_settings_gsm_Balance_Notification_Threshold()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("GSM - Разрешить трансляцию событий")
    def test_settings_gsm_tooltip_7(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'GSM'"):
            app.PO_Navigations.goToGSMPage()
        with allure.step("Проверка подсказки: Разрешить трансляцию событий"):
            app.PO_Tooltips.tooltip_settings_gsm_Allow_Event_Broadcast()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Ethernet - MAC адрес")
    def test_settings_ethernet_tooltip_1(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Ethernet'"):
            app.PO_Navigations.goToEthernetPage()
        with allure.step("Проверка подсказки: MAC адрес"):
            app.PO_Tooltips.tooltip_settings_ethernet_MAC_address()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Ethernet - Название сервера")
    def test_settings_ethernet_tooltip_2(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Ethernet'"):
            app.PO_Navigations.goToEthernetPage()
        with allure.step("Проверка подсказки: Название сервера"):
            app.PO_Tooltips.tooltip_settings_ethernet_Server_name()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Ethernet - Адрес IPv4")
    def test_settings_ethernet_tooltip_3(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Ethernet'"):
            app.PO_Navigations.goToEthernetPage()
        with allure.step("Проверка подсказки: Адрес IPv4"):
            app.PO_Tooltips.tooltip_settings_ethernet_IPv4_address()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Ethernet - Маска подсети")
    def test_settings_ethernet_tooltip_4(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Ethernet'"):
            app.PO_Navigations.goToEthernetPage()
        with allure.step("Проверка подсказки: Маска подсети"):
            app.PO_Tooltips.tooltip_settings_ethernet_Subnet_mask()


@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты ВСПЛЫВАЮЩИЕ ПОДСКАЗКИ")
@allure.feature("Настройки")
@pytest.mark.flaky(reruns=reruns)
class Test04TooltipsMassege:

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Ethernet - Основной шлюз")
    def test_settings_ethernet_tooltip_5(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Ethernet'"):
            app.PO_Navigations.goToEthernetPage()
        with allure.step("Проверка подсказки: Основной шлюз"):
            app.PO_Tooltips.tooltip_settings_ethernet_Main_gate()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Ethernet - Предпочтительный DNS сервер")
    def test_settings_ethernet_tooltip_6(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Ethernet'"):
            app.PO_Navigations.goToEthernetPage()
        with allure.step("Проверка подсказки: Предпочтительный DNS сервер"):
            app.PO_Tooltips.tooltip_settings_ethernet_Preferred_DNS_Server()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Ethernet - Альтернативный DNS сервер")
    def test_settings_ethernet_tooltip_7(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Ethernet'"):
            app.PO_Navigations.goToEthernetPage()
        with allure.step("Проверка подсказки: Альтернативный DNS сервер"):
            app.PO_Tooltips.tooltip_settings_ethernet_Alternative_DNS_Server()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Ethernet - Получать IPv4 адрес и настройки автоматически")
    def test_settings_ethernet_tooltip_8(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Ethernet'"):
            app.PO_Navigations.goToEthernetPage()
        with allure.step("Проверка подсказки: Получать IPv4 адрес и настройки автоматически"):
            app.PO_Tooltips.tooltip_settings_ethernet_Obtain_IPv4_address_settings_automatically()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Ethernet - Использовать как сервер")
    def test_settings_ethernet_tooltip_9(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Ethernet'"):
            app.PO_Navigations.goToEthernetPage()
        with allure.step("Проверка подсказки: Использовать как сервер"):
            app.PO_Tooltips.tooltip_settings_ethernet_Use_as_server()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Ethernet - Получать адрес IPv6 от DHCP автоматически")
    def test_settings_ethernet_tooltip_10(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Ethernet'"):
            app.PO_Navigations.goToEthernetPage()
        with allure.step("Проверка подсказки: Получать адрес IPv6 от DHCP автоматически"):
            app.PO_Tooltips.tooltip_settings_ethernet_Obtain_IPv6_address_DHCP_automatically()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Ethernet - Разрешить удаленное управление")
    def test_settings_ethernet_tooltip_11(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Ethernet'"):
            app.PO_Navigations.goToEthernetPage()
        with allure.step("Проверка подсказки: Разрешить удаленное управление"):
            app.PO_Tooltips.tooltip_settings_ethernet_Allow_remote_control()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Ethernet - Получать адрес IPv6 от SLAAC автоматически")
    def test_settings_ethernet_tooltip_12(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Ethernet'"):
            app.PO_Navigations.goToEthernetPage()
        with allure.step("Проверка подсказки: Получать адрес IPv6 от SLAAC автоматически"):
            app.PO_Tooltips.tooltip_settings_ethernet_Obtain_IPv6_address_SLAAC_automatically()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Ethernet - Разрешить незащищенное HTTP-соединение")
    def test_settings_ethernet_tooltip_13(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Ethernet'"):
            app.PO_Navigations.goToEthernetPage()
        with allure.step("Проверка подсказки: Разрешить незащищенное HTTP-соединение"):
            app.PO_Tooltips.tooltip_settings_ethernet_Allow_insecure_HTTP_connection()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Ethernet - Устанавливать сетевые подключения через")
    def test_settings_ethernet_tooltip_14(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Ethernet'"):
            app.PO_Navigations.goToEthernetPage()
        with allure.step("Проверка подсказки: Устанавливать сетевые подключения через"):
            app.PO_Tooltips.tooltip_settings_ethernet_Establish_network_connections()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Ethernet - Локальный IPv6 адрес")
    def test_settings_ethernet_tooltip_15(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Ethernet'"):
            app.PO_Navigations.goToEthernetPage()
        with allure.step("Проверка подсказки: Локальный IPv6 адрес"):
            app.PO_Tooltips.tooltip_settings_ethernet_Local_IPv6_address()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Ethernet - Глобальный IPv6 адрес")
    def test_settings_ethernet_tooltip_16(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Ethernet'"):
            app.PO_Navigations.goToEthernetPage()
        with allure.step("Проверка подсказки: Глобальный IPv6 адрес"):
            app.PO_Tooltips.tooltip_settings_ethernet_Global_IPv6_Address()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Ethernet - Предпочтительный IPv6 DNS сервер")
    def test_settings_ethernet_tooltip_17(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Ethernet'"):
            app.PO_Navigations.goToEthernetPage()
        with allure.step("Проверка подсказки: Предпочтительный IPv6 DNS сервер"):
            app.PO_Tooltips.tooltip_settings_ethernet_Preferred_IPv6_DNS_Server()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Ethernet - Альтернативный IPv6 DNS сервер")
    def test_settings_ethernet_tooltip_18(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Ethernet'"):
            app.PO_Navigations.goToEthernetPage()
        with allure.step("Проверка подсказки: Альтернативный IPv6 DNS сервер"):
            app.PO_Tooltips.tooltip_settings_ethernet_Alternative_IPv6_DNS_Server()

    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Объект - Название объекта")
    def test_settings_object_tooltip_input_1(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Объект'"):
            app.PO_Navigations.goToObjectPage()
        with allure.step("Клик по кнопке 'Редактировать'"):
            app.PO_Settings.edit_button_click()
        with allure.step("Проверка подсказки: Название объекта"):
            app.PO_Tooltips.tooltip_settings_object_name_input()

    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Объект - Номер объекта")
    def test_settings_object_tooltip_input_2(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Объект'"):
            app.PO_Navigations.goToObjectPage()
        with allure.step("Клик по кнопке 'Редактировать'"):
            app.PO_Settings.edit_button_click()
        with allure.step("Проверка подсказки: Номер объекта"):
            app.PO_Tooltips.tooltip_settings_object_number_input()

    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Объект - Задержка взятия")
    def test_settings_object_tooltip_input_3(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Объект'"):
            app.PO_Navigations.goToObjectPage()
        with allure.step("Клик по кнопке 'Редактировать'"):
            app.PO_Settings.edit_button_click()
        with allure.step("Проверка подсказки: Задержка взятия"):
            app.PO_Tooltips.tooltip_settings_take_delay_input()

    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Объект - Задержка тревоги входа")
    def test_settings_object_tooltip_input_4(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Объект'"):
            app.PO_Navigations.goToObjectPage()
        with allure.step("Клик по кнопке 'Редактировать'"):
            app.PO_Settings.edit_button_click()
        with allure.step("Проверка подсказки: Задержка тревоги входа"):
            app.PO_Tooltips.tooltip_settings_object_delay_alarm_enter_input()

    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Объект - Время автовзятия")
    def test_settings_object_tooltip_input_5(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Объект'"):
            app.PO_Navigations.goToObjectPage()
        with allure.step("Клик по кнопке 'Редактировать'"):
            app.PO_Settings.edit_button_click()
        with allure.step("Проверка подсказки: Время автовзятия"):
            app.PO_Tooltips.tooltip_settings_object_time_auto_take_on_input()

    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Дата и время - Синхронизация по NTP/HTP - Адрес сервера")
    def test_settings_date_time_tooltip_ntp_input(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Дата и время'"):
            app.PO_Navigations.goToDateTimePage()
        with allure.step("Клик по кнопке 'Редактировать'"):
            app.PO_Settings.edit_button_click()
        with allure.step("Выбор: Синхронизация по NTP/HTP"):
            app.PO_Settings.Synchronization_via_NTP_HTP_click()
        with allure.step("Проверка подсказки: Адрес сервера"):
            app.PO_Tooltips.tooltip_settings_date_time_drop_list_ntp_input()


@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты ВСПЛЫВАЮЩИЕ ПОДСКАЗКИ")
@allure.feature("Настройки")
@pytest.mark.flaky(reruns=reruns)
class Test05TooltipsMassege:

    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Звуковая индикация - Длительность сигнала")
    def test_settings_volume_indications_tooltip_input(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Звуковая индикация'"):
            app.PO_Navigations.goToVolumIndicationPage()
        with allure.step("Клик по кнопке 'Редактировать'"):
            app.PO_Settings.edit_button_click()
        with allure.step("Проверка подсказки: Длительность сигнала"):
            app.PO_Tooltips.tooltip_settings_volum_indications_Signal_duration_input()

    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Радио - Время разрешения добавления новых датчиков")
    def test_settings_wireless_tooltip_input_1(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Радио'"):
            app.PO_Navigations.goToRadioPage()
        with allure.step("Клик по кнопке 'Редактировать'"):
            app.PO_Settings.edit_button_click()
        with allure.step("Включение радиомодуля"):
            app.PO_Settings.check_box_radio_on()
        with allure.step("Проверка подсказки: Время разрешения добавления новых датчиков"):
            app.PO_Tooltips.tooltip_settings_radio_Resolution_time_adding_new_sensor_input()

    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Радио - Период опроса датчиков")
    def test_settings_wireless_tooltip_input_2(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Радио'"):
            app.PO_Navigations.goToRadioPage()
        with allure.step("Клик по кнопке 'Редактировать'"):
            app.PO_Settings.edit_button_click()
        with allure.step("Включение радиомодуля"):
            app.PO_Settings.check_box_radio_on()
        with allure.step("Проверка подсказки: Период опроса датчиков"):
            app.PO_Tooltips.tooltip_settings_radio_Sensor_polling_period_input()

    @allure.story("Проверка подсказок полей ввода")
    @allure.title("GSM - Число знаков номера для проверки")
    def test_settings_gsm_tooltip_input_1(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'GSM'"):
            app.PO_Navigations.goToGSMPage()
        with allure.step("Клик по кнопке 'Редактировать'"):
            app.PO_Settings.edit_button_click()
        with allure.step("Проверка подсказки: Число знаков номера для проверки"):
            app.PO_Tooltips.tooltip_settings_gsm_Number_digits_number_to_check_input()

    @allure.story("Проверка подсказок полей ввода")
    @allure.title("GSM - Порог уведомления о балансе")
    def test_settings_gsm_tooltip_input_2(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'GSM'"):
            app.PO_Navigations.goToGSMPage()
        with allure.step("Клик по кнопке 'Редактировать'"):
            app.PO_Settings.edit_button_click()
        with allure.step("Проверка подсказки: Порог уведомления о балансе"):
            app.PO_Tooltips.tooltip_settings_gsm_Balance_Notification_Threshold_input()

    @allure.story("Проверка подсказок полей ввода")
    @allure.title("GSM - SIM 1 PIN")
    def test_settings_gsm_sim_1_tooltip_input_1(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'GSM'"):
            app.PO_Navigations.goToGSMPage()
        with allure.step("Клик по кнопке 'Редактировать'"):
            app.PO_Settings.edit_button_click()
        with allure.step("Проверка подсказки: PIN"):
            app.PO_Tooltips.tooltip_settings_gsm_sim_1_pin_input()

    @allure.story("Проверка подсказок полей ввода")
    @allure.title("GSM - SIM 2 PIN")
    def test_settings_gsm_sim_2_tooltip_input_1(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'GSM'"):
            app.PO_Navigations.goToGSMPage()
        with allure.step("Клик по кнопке 'Редактировать'"):
            app.PO_Settings.edit_button_click()
        with allure.step("Проверка подсказки: PIN"):
            app.PO_Tooltips.tooltip_settings_gsm_sim_2_pin_input()

    @allure.story("Проверка подсказок полей ввода")
    @allure.title("GSM - SIM 1 USSD-код запроса баланса")
    def test_settings_gsm_sim_1_tooltip_input_2(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'GSM'"):
            app.PO_Navigations.goToGSMPage()
        with allure.step("Клик по кнопке 'Редактировать'"):
            app.PO_Settings.edit_button_click()
        with allure.step("Проверка подсказки: USSD-код запроса баланса"):
            app.PO_Tooltips.tooltip_settings_gsm_sim_1_ussd_input()

    @allure.story("Проверка подсказок полей ввода")
    @allure.title("GSM - SIM 2 USSD-код запроса баланса")
    def test_settings_gsm_sim_2_tooltip_input_2(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'GSM'"):
            app.PO_Navigations.goToGSMPage()
        with allure.step("Клик по кнопке 'Редактировать'"):
            app.PO_Settings.edit_button_click()
        with allure.step("Проверка подсказки: USSD-код запроса баланса"):
            app.PO_Tooltips.tooltip_settings_gsm_sim_2_ussd_input()

    @allure.story("Проверка подсказок полей ввода")
    @allure.title("GSM - SIM 1 APN")
    def test_settings_gsm_sim_1_tooltip_input_3(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'GSM'"):
            app.PO_Navigations.goToGSMPage()
        with allure.step("Клик по кнопке 'Редактировать'"):
            app.PO_Settings.edit_button_click()
        with allure.step("Проверка подсказки: APN"):
            app.PO_Tooltips.tooltip_settings_gsm_sim_1_apn_input()

    @allure.story("Проверка подсказок полей ввода")
    @allure.title("GSM - SIM 2 APN")
    def test_settings_gsm_sim_2_tooltip_input_3(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'GSM'"):
            app.PO_Navigations.goToGSMPage()
        with allure.step("Клик по кнопке 'Редактировать'"):
            app.PO_Settings.edit_button_click()
        with allure.step("Проверка подсказки: APN"):
            app.PO_Tooltips.tooltip_settings_gsm_sim_2_apn_input()

    @allure.story("Проверка подсказок полей ввода")
    @allure.title("GSM - SIM 1 Пользователь")
    def test_settings_gsm_sim_1_tooltip_input_4(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'GSM'"):
            app.PO_Navigations.goToGSMPage()
        with allure.step("Клик по кнопке 'Редактировать'"):
            app.PO_Settings.edit_button_click()
        with allure.step("Проверка подсказки: Пользователь"):
            app.PO_Tooltips.tooltip_settings_gsm_sim_1_user_input()

    @allure.story("Проверка подсказок полей ввода")
    @allure.title("GSM - SIM 2 Пользователь")
    def test_settings_gsm_sim_2_tooltip_input_4(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'GSM'"):
            app.PO_Navigations.goToGSMPage()
        with allure.step("Клик по кнопке 'Редактировать'"):
            app.PO_Settings.edit_button_click()
        with allure.step("Проверка подсказки: Пользователь"):
            app.PO_Tooltips.tooltip_settings_gsm_sim_2_user_input()

    @allure.story("Проверка подсказок полей ввода")
    @allure.title("GSM - SIM 1 Пароль")
    def test_settings_gsm_sim_1_tooltip_input_5(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'GSM'"):
            app.PO_Navigations.goToGSMPage()
        with allure.step("Клик по кнопке 'Редактировать'"):
            app.PO_Settings.edit_button_click()
        with allure.step("Проверка подсказки: Пароль"):
            app.PO_Tooltips.tooltip_settings_gsm_sim_1_password_input()

    @allure.story("Проверка подсказок полей ввода")
    @allure.title("GSM - SIM 2 Пароль")
    def test_settings_gsm_sim_2_tooltip_input_5(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'GSM'"):
            app.PO_Navigations.goToGSMPage()
        with allure.step("Клик по кнопке 'Редактировать'"):
            app.PO_Settings.edit_button_click()
        with allure.step("Проверка подсказки: Пароль"):
            app.PO_Tooltips.tooltip_settings_gsm_sim_2_password_input()

    # --------------------------------------------------------------

    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Ethernet - MAC адрес")
    def test_settings_ethernet_tooltip_input_1(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Ethernet'"):
            app.PO_Navigations.goToEthernetPage()
        with allure.step("Клик по кнопке 'Редактировать'"):
            app.PO_Settings.edit_button_click()
        with allure.step("Проверка подсказки: MAC адрес"):
            app.PO_Tooltips.tooltip_settings_ethernet_MAC_address_input()

    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Ethernet - Название сервера")
    def test_settings_ethernet_tooltip_input_2(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Ethernet'"):
            app.PO_Navigations.goToEthernetPage()
        with allure.step("Клик по кнопке 'Редактировать'"):
            app.PO_Settings.edit_button_click()
        with allure.step("Проверка подсказки: Название сервера"):
            app.PO_Tooltips.tooltip_settings_ethernet_Server_name_input()

    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Ethernet - Адрес IPv4")
    def test_settings_ethernet_tooltip_input_3(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Ethernet'"):
            app.PO_Navigations.goToEthernetPage()
        with allure.step("Клик по кнопке 'Редактировать'"):
            app.PO_Settings.edit_button_click()
        with allure.step("Проверка подсказки: Адрес IPv4"):
            app.PO_Tooltips.tooltip_settings_ethernet_IPv4_address_input()

    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Ethernet - Маска подсети")
    def test_settings_ethernet_tooltip_input_4(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Ethernet'"):
            app.PO_Navigations.goToEthernetPage()
        with allure.step("Клик по кнопке 'Редактировать'"):
            app.PO_Settings.edit_button_click()
        with allure.step("Проверка подсказки: Маска подсети"):
            app.PO_Tooltips.tooltip_settings_ethernet_Subnet_mask_input()

    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Ethernet - Основной шлюз")
    def test_settings_ethernet_tooltip_input_5(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Ethernet'"):
            app.PO_Navigations.goToEthernetPage()
        with allure.step("Клик по кнопке 'Редактировать'"):
            app.PO_Settings.edit_button_click()
        with allure.step("Проверка подсказки: Основной шлюз"):
            app.PO_Tooltips.tooltip_settings_ethernet_Main_gate_input()

    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Ethernet - Предпочтительный DNS сервер")
    def test_settings_ethernet_tooltip_input_6(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Ethernet'"):
            app.PO_Navigations.goToEthernetPage()
        with allure.step("Клик по кнопке 'Редактировать'"):
            app.PO_Settings.edit_button_click()
        with allure.step("Проверка подсказки: Предпочтительный DNS сервер"):
            app.PO_Tooltips.tooltip_settings_ethernet_Preferred_DNS_Server_input()

    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Ethernet - Альтернативный DNS сервер")
    def test_settings_ethernet_tooltip_input_7(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Ethernet'"):
            app.PO_Navigations.goToEthernetPage()
        with allure.step("Клик по кнопке 'Редактировать'"):
            app.PO_Settings.edit_button_click()
        with allure.step("Проверка подсказки: Альтернативный DNS сервер"):
            app.PO_Tooltips.tooltip_settings_ethernet_Alternative_DNS_Server_input()


@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты ВСПЛЫВАЮЩИЕ ПОДСКАЗКИ")
@allure.feature("Настройки")
@pytest.mark.flaky(reruns=reruns)
class Test06TooltipsMassege:

    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Ethernet - Локальный IPv6 адрес")
    def test_settings_ethernet_tooltip_input_8(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Ethernet'"):
            app.PO_Navigations.goToEthernetPage()
        with allure.step("Клик по кнопке 'Редактировать'"):
            app.PO_Settings.edit_button_click()
        with allure.step("Проверка подсказки: Локальный IPv6 адрес"):
            app.PO_Tooltips.tooltip_settings_ethernet_Local_IPv6_address_input()

    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Ethernet - Глобальный IPv6 адрес")
    def test_settings_ethernet_tooltip_input_9(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Ethernet'"):
            app.PO_Navigations.goToEthernetPage()
        with allure.step("Клик по кнопке 'Редактировать'"):
            app.PO_Settings.edit_button_click()
        with allure.step("Проверка подсказки: Глобальный IPv6 адрес"):
            app.PO_Tooltips.tooltip_settings_ethernet_Global_IPv6_Address_input()

    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Ethernet - Предпочтительный IPv6 DNS сервер")
    def test_settings_ethernet_tooltip_input_10(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Ethernet'"):
            app.PO_Navigations.goToEthernetPage()
        with allure.step("Клик по кнопке 'Редактировать'"):
            app.PO_Settings.edit_button_click()
        with allure.step("Проверка подсказки: Предпочтительный IPv6 DNS сервер"):
            app.PO_Tooltips.tooltip_settings_ethernet_Preferred_IPv6_DNS_Server_input()

    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Ethernet - Альтернативный IPv6 DNS сервер")
    def test_settings_ethernet_tooltip_input_11(self, app):
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Ethernet'"):
            app.PO_Navigations.goToEthernetPage()
        with allure.step("Клик по кнопке 'Редактировать'"):
            app.PO_Settings.edit_button_click()
        with allure.step("Проверка подсказки: Альтернативный IPv6 DNS сервер"):
            app.PO_Tooltips.tooltip_settings_ethernet_Alternative_IPv6_DNS_Server_input()


@allure.epic("Тесты ВСПЛЫВАЮЩИЕ ПОДСКАЗКИ")
@allure.feature("Пользователи и ключи")
@pytest.mark.flaky(reruns=reruns)
class Test01TooltipsMassegeUsersKeys():

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Пользователь - Администратор")
    def test_users_keys_user_tooltip_1(self, app, users_settings, close_modal):
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_user_keys_administrator()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Пользователь - Режим Эгида3")
    def test_users_keys_user_tooltip_2(self, app, users_settings, close_modal):
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_user_keys_user_egida3()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Пользователь - Имя пользователя")
    def test_users_keys_user_tooltip_3(self, app, users_settings, close_modal):
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_user_keys_user_name()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Пользователь - Логин")
    def test_users_keys_user_tooltip_4(self, app, users_settings, close_modal):
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_user_keys_user_login()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Пользователь - Пароль")
    def test_users_keys_user_tooltip_5(self, app, users_settings, close_modal):
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_user_keys_user_password()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Пользователь - Повторите пароль")
    def test_users_keys_user_tooltip_6(self, app, users_settings, close_modal):
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_user_keys_user_rep_password()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Пользователь - Перенаправление сообщений оператора")
    def test_users_keys_user_tooltip_7(self, app, users_settings, close_modal):
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_user_keys_user_operator_message_forwarding()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Пользователь - Отправка вне трансляции")
    def test_users_keys_user_tooltip_8(self, app, users_settings, close_modal):
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_user_keys_user_sending_out_of_broadcast()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Пользователь - Группа выходов с управлением по SMS")
    def test_users_keys_user_tooltip_9(self, app, users_settings, close_modal):
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_user_keys_user_group_of_outputs_controlled_by_SMS()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Пользователь - Группа выходов с управлением звонком")
    def test_users_keys_user_tooltip_10(self, app, users_settings, close_modal):
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_user_keys_user_group_of_outputs_with_call_control()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Пользователь - Разрешить снятие по SMS")
    def test_users_keys_user_tooltip_11(self, app, users_settings, close_modal):
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_user_keys_user_allow_withdrawal_by_SMS()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Пользователь - Разрешить взятие по SMS")
    def test_users_keys_user_tooltip_12(self, app, users_settings, close_modal):
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_user_keys_user_allow_pickup_by_SMS()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Пользователь - Телефон")
    def test_users_keys_user_tooltip_13(self, app, users_settings, close_modal):
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_user_keys_user_phone()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Пользователь - Пароль SMS")
    def test_users_keys_user_tooltip_14(self, app, users_settings, close_modal):
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_user_keys_user_password_sms()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Пользователь - Повторите пароль SMS")
    def test_users_keys_user_tooltip_15(self, app, users_settings, close_modal):
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_user_keys_user_rep_password_sms()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Пользователь - Управляемые по SMS разделы")
    def test_users_keys_user_tooltip_16(self, app, users_settings, close_modal):
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_user_keys_user_SMS_controlled_sections()

    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Пользователь - Имя пользователя")
    def test_users_keys_user_tooltip_input_1(self, app, users_settings, close_modal):
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_user_keys_user_name_input()

    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Пользователь - Логин")
    def test_users_keys_user_tooltip_input_2(self, app, users_settings, close_modal):
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_user_keys_user_login_input()

    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Пользователь - Пароль")
    def test_users_keys_user_tooltip_input_3(self, app, users_settings, close_modal):
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_user_keys_user_password_input()

    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Пользователь - Повторите пароль")
    def test_users_keys_user_tooltip_input_4(self, app, users_settings, close_modal):
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_user_keys_user_rep_password_input()

    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Пользователь - Телефон - код")
    def test_users_keys_user_tooltip_input_5(self, app, users_settings, close_modal):
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_user_keys_user_phone_input_cod()

    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Пользователь - Телефон - номер")
    def test_users_keys_user_tooltip_input_6(self, app, users_settings, close_modal):
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_user_keys_user_phone_input_number()

    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Пользователь - Пароль SMS")
    def test_users_keys_user_tooltip_input_7(self, app, users_settings, close_modal):
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_user_keys_user_password_sms_input()

    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Пользователь - Повторите пароль SMS")
    def test_users_keys_user_tooltip_input_8(self, app, users_settings, close_modal):
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_user_keys_user_rep_password_sms_input()

    # Для данного поля не предусмотрена задача тикет 132871
    # @allure.story("Проверка подсказок наименования поля")
    # @allure.title("Ключи - ID")
    # def test_users_keys_keys_tooltip_1(self, app, keys_settings, close_modal):
    #     with allure.step("Проверка подсказки"):
    #         app.PO_Tooltips.tooltip_user_keys_keys_id()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Ключи - Пользователь")
    def test_users_keys_keys_tooltip_2(self, app, keys_settings, close_modal):
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_user_keys_keys_user()


@allure.epic("Тесты ВСПЛЫВАЮЩИЕ ПОДСКАЗКИ")
@allure.feature("Пользователи и ключи")
@pytest.mark.flaky(reruns=reruns)
class Test02TooltipsMassegeUsersKeys():

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Ключи - Разрешения")
    def test_users_keys_keys_tooltip_3(self, app, keys_settings, close_modal):
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_user_keys_keys_permissions()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Ключи - Разделы")
    def test_users_keys_keys_tooltip_4(self, app, keys_settings, close_modal):
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_user_keys_keys_path()

    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Ключи - ID")
    def test_users_keys_keys_tooltip_input_1(self, app, keys_settings, close_modal):
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_user_keys_keys_id_input()


@allure.epic("Тесты ВСПЛЫВАЮЩИЕ ПОДСКАЗКИ")
@allure.feature("Разделы")
@pytest.mark.flaky(reruns=reruns)
class TestTooltipsMassegePath():

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Разделы - Номер")
    def test_path_tooltip_1(self, app, add_path, close_modal):
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_path_number()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Разделы - Название")
    def test_path_tooltip_2(self, app, add_path, close_modal):
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_path_name()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Разделы - Управляющие разделы")
    def test_path_tooltip_3(self, app, add_path, close_modal):
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_path_control_sections()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Разделы - Задержка взятия")
    def test_path_tooltip_4(self, app, add_path, close_modal):
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_path_take_delay()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Разделы - Автовзятие из невзятия")
    def test_path_tooltip_5(self, app, add_path, close_modal):
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_path_auto_pickup_from_non_pickup()

    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Разделы - Автовзятие из тревоги")
    def test_path_tooltip_6(self, app, add_path, close_modal):
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_path_auto_arm_from_alarm()

    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Разделы - Номер")
    def test_path_tooltip_input_1(self, app, add_path, close_modal):
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_path_number_input()

    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Разделы - Название")
    def test_path_tooltip_input_2(self, app, add_path, close_modal):
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_path_name_input()


@allure.epic("Тесты ВСПЛЫВАЮЩИЕ ПОДСКАЗКИ")
@allure.feature("Направления")
@pytest.mark.flaky(reruns=reruns)
class Test01TooltipsMassegeDirections():

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Направления - Название")
    def test_directions_tooltip_1(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_name()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Направления - Разделы")
    def test_directions_tooltip_2(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_path()

    # Не актуально 132879
    # @pytest.mark.parametrize("directions", directions_list)
    # @allure.story("Проверка подсказок наименования поля")
    # @allure.title("Направления - Тип управления")
    # def test_directions_main_tooltip_1(self, app, destination, close_modal, directions):
    #     with allure.step("Открытие направления"):
    #         app.PO_Directions.openDestination(directions)
    #     with allure.step("Раскрытие настроек канала"):
    #         app.PO_Directions.openChanel('Основной')
    #     with allure.step("Проверка подсказки"):
    #         app.PO_Tooltips.tooltip_directions_control_type()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Направления - Название")
    def test_directions_tooltip_input_1(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_name_input()

    # Не актуально 132879
    # @pytest.mark.parametrize("directions", directions_list)
    # @allure.story("Проверка подсказок наименования поля")
    # @allure.title("Направления - Текущий пользователь - Основной канал")
    # def test_directions_main_tooltip_2(self, app, destination, close_modal, directions):
    #     with allure.step("Открытие направления"):
    #         app.PO_Directions.openDestination(directions)
    #     with allure.step("Раскрытие настроек канала"):
    #         app.PO_Directions.openChanel('Основной')
    #     with allure.step("Выбор типа управления"):
    #         app.PO_Directions.openType_main('SMS пользователю')
    #     with allure.step("Проверка подсказки"):
    #         app.PO_Tooltips.tooltip_directions_current_user()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Направления - SMS пользователю - Отправлять время события - Основной канал")
    def test_directions_main_tooltip_3(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('SMS пользователю')
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_send_event_time()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Направления - SMS пользователю - Отправлять дату события - Основной канал")
    def test_directions_main_tooltip_4(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('SMS пользователю')
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_send_event_date()

    # Не актуально 132879
    # @pytest.mark.parametrize("directions", directions_list)
    # @allure.story("Проверка подсказок наименования поля")
    # @allure.title("Направления - Включить тестирование канала - Основной канал")
    # def test_directions_main_tooltip_5(self, app, destination, close_modal, directions):
    #     with allure.step("Открытие направления"):
    #         app.PO_Directions.openDestination(directions)
    #     with allure.step("Раскрытие настроек канала"):
    #         app.PO_Directions.openChanel('Основной')
    #     with allure.step("Выбор типа управления"):
    #         app.PO_Directions.openType_main('SMS пользователю')
    #     with allure.step("Проверка подсказки"):
    #         app.PO_Tooltips.tooltip_directions_enable_channel_testing()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Направления - Таймаут при ошибке - Основной канал")
    def test_directions_main_tooltip_6(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('SMS пользователю')
        with allure.step("Включить тестирование канала"):
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_timeout_on_error()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Направления - Тестировать если - Основной канал")
    def test_directions_main_tooltip_7(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('SMS пользователю')
        with allure.step("Включить тестирование канала"):
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_test_if()

    # Не актуально 132879
    # @pytest.mark.parametrize("directions", directions_list)
    # @allure.story("Проверка подсказок наименования поля")
    # @allure.title("Направления - Метод тестирования - Основной канал")
    # def test_directions_main_tooltip_8(self, app, destination, close_modal, directions):
    #     with allure.step("Открытие направления"):
    #         app.PO_Directions.openDestination(directions)
    #     with allure.step("Раскрытие настроек канала"):
    #         app.PO_Directions.openChanel('Основной')
    #     with allure.step("Выбор типа управления"):
    #         app.PO_Directions.openType_main('SMS пользователю')
    #     with allure.step("Включить тестирование канала"):
    #         app.PO_Directions.enableChannelTesting_main()
    #     with allure.step("Проверка подсказки"):
    #         app.PO_Tooltips.tooltip_directions_test_method()


@allure.epic("Тесты ВСПЛЫВАЮЩИЕ ПОДСКАЗКИ")
@allure.feature("Направления")
@pytest.mark.flaky(reruns=reruns)
class Test02TooltipsMassegeDirections():

    # Не актуально 132879
    # @pytest.mark.parametrize("directions", directions_list)
    # @allure.story("Проверка подсказок наименования поля")
    # @allure.title("Направления - Тестировать - Основной канал")
    # def test_directions_main_tooltip_9(self, app, destination, close_modal, directions):
    #     with allure.step("Открытие направления"):
    #         app.PO_Directions.openDestination(directions)
    #     with allure.step("Раскрытие настроек канала"):
    #         app.PO_Directions.openChanel('Основной')
    #     with allure.step("Выбор типа управления"):
    #         app.PO_Directions.openType_main('SMS пользователю')
    #     with allure.step("Включить тестирование канала"):
    #         app.PO_Directions.enableChannelTesting_main()
    #     with allure.step("Проверка подсказки"):
    #         app.PO_Tooltips.tooltip_directions_test()

    # Не актуально 132879
    # @pytest.mark.parametrize("directions", directions_list)
    # @allure.story("Проверка подсказок наименования поля")
    # @allure.title("Направления - Дни недели - Основной канал")
    # def test_directions_main_tooltip_10(self, app, destination, close_modal, directions):
    #     with allure.step("Открытие направления"):
    #         app.PO_Directions.openDestination(directions)
    #     with allure.step("Раскрытие настроек канала"):
    #         app.PO_Directions.openChanel('Основной')
    #     with allure.step("Выбор типа управления"):
    #         app.PO_Directions.openType_main('SMS пользователю')
    #     with allure.step("Включить тестирование канала"):
    #         app.PO_Directions.enableChannelTesting_main()
    #     with allure.step("Проверка подсказки"):
    #         app.PO_Tooltips.tooltip_directions_days_of_th_week()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Направления - Звонок - Количество повторов - Основной канал")
    def test_directions_main_tooltip_11(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('Звонок')
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_number_of_repetitions()

    # Не актуально 132879
    # @pytest.mark.parametrize("directions", directions_list)
    # @allure.story("Проверка подсказок наименования поля")
    # @allure.title("Направления - DC09 - Адрес - Основной канал")
    # def test_directions_main_tooltip_12(self, app, destination, close_modal, directions):
    #     with allure.step("Открытие направления"):
    #         app.PO_Directions.openDestination(directions)
    #     with allure.step("Раскрытие настроек канала"):
    #         app.PO_Directions.openChanel('Основной')
    #     with allure.step("Выбор типа управления"):
    #         app.PO_Directions.openType_main('DC09')
    #     with allure.step("Проверка подсказки"):
    #         app.PO_Tooltips.tooltip_directions_address()

    # Не актуально 132879
    # @pytest.mark.parametrize("directions", directions_list)
    # @allure.story("Проверка подсказок наименования поля")
    # @allure.title("Направления - DC09 - Порт - Основной канал")
    # def test_directions_main_tooltip_13(self, app, destination, close_modal, directions):
    #     with allure.step("Открытие направления"):
    #         app.PO_Directions.openDestination(directions)
    #     with allure.step("Раскрытие настроек канала"):
    #         app.PO_Directions.openChanel('Основной')
    #     with allure.step("Выбор типа управления"):
    #         app.PO_Directions.openType_main('DC09')
    #     with allure.step("Проверка подсказки"):
    #         app.PO_Tooltips.tooltip_directions_port()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Направления - DC09 - Канал соединения - Основной канал")
    def test_directions_main_tooltip_14(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('DC09')
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_connection_channel()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Направления - DC09 - Таймаут подтверждения, сек - Основной канал")
    def test_directions_main_tooltip_15(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('DC09')
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_confirmation_timeout_sec()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Направления - DC09 - Количество повторов - Основной канал")
    def test_directions_main_tooltip_16(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('DC09')
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_number_of_repetitions_DC09()

    # Не актуально 132879
    # @pytest.mark.parametrize("directions", directions_list)
    # @allure.story("Проверка подсказок наименования поля")
    # @allure.title("Направления - DC09 - Шифрование - Основной канал")
    # def test_directions_main_tooltip_17(self, app, destination, close_modal, directions):
    #     with allure.step("Открытие направления"):
    #         app.PO_Directions.openDestination(directions)
    #     with allure.step("Раскрытие настроек канала"):
    #         app.PO_Directions.openChanel('Основной')
    #     with allure.step("Выбор типа управления"):
    #         app.PO_Directions.openType_main('DC09')
    #     with allure.step("Проверка подсказки"):
    #         app.PO_Tooltips.tooltip_directions_encryption()

    # Не актуально 132879
    # @pytest.mark.parametrize("directions", directions_list)
    # @allure.story("Проверка подсказок наименования поля")
    # @allure.title("Направления - DC09 - Ключ шифрования - Основной канал")
    # def test_directions_main_tooltip_18(self, app, destination, close_modal, directions):
    #     with allure.step("Открытие направления"):
    #         app.PO_Directions.openDestination(directions)
    #     with allure.step("Раскрытие настроек канала"):
    #         app.PO_Directions.openChanel('Основной')
    #     with allure.step("Выбор типа управления"):
    #         app.PO_Directions.openType_main('DC09')
    #     with allure.step("Проверка подсказки"):
    #         app.PO_Tooltips.tooltip_directions_encryption_keyn()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Направления - Номер телефона - код - Основной канал")
    def test_directions_tooltip_main_input_2(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('SMS пользователю')
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_phone_cod_input()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Направления - Номер телефона - номер - Основной канал")
    def test_directions_tooltip_main_input_3(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('SMS пользователю')
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_phone_number_input()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Направления - Таймаут при ошибке - Основной канал")
    def test_directions_main_tooltip_input_4(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('SMS пользователю')
        with allure.step("Включить тестирование канала"):
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_timeout_on_error_input()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Направления - Звонок - Количество повторов - Основной канал")
    def test_directions_main_tooltip_input_5(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('Звонок')
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_number_of_repetitions_input()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Направления - DC09 - Адрес - Основной канал")
    def test_directions_main_tooltip_input_6(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('DC09')
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_address_input()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Направления - DC09 - Порт - Основной канал")
    def test_directions_main_tooltip_input_7(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('DC09')
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_port_input()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Направления - DC09 - Таймаут подтверждения, сек - Основной канал")
    def test_directions_main_tooltip_input_8(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('DC09')
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_confirmation_timeout_sec_input()


@allure.epic("Тесты ВСПЛЫВАЮЩИЕ ПОДСКАЗКИ")
@allure.feature("Направления")
@pytest.mark.flaky(reruns=reruns)
class Test03TooltipsMassegeDirections():

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Направления - DC09 - Количество повторов - Основной канал")
    def test_directions_main_input_9(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('DC09')
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_number_of_repetitions_DC09()

    # Не актуально 132879
    # @pytest.mark.parametrize("directions", directions_list)
    # @allure.story("Проверка подсказок наименования поля")
    # @allure.title("Направления - Текущий пользователь - Резервный канал 1")
    # def test_directions_rezerv_1_tooltip_2(self, app, destination, close_modal, directions):
    #     with allure.step("Открытие направления"):
    #         app.PO_Directions.openDestination(directions)
    #     with allure.step("Предусловия раскрытия настроек канала"):
    #         app.PO_Directions.openChanel('Основной')
    #         app.PO_Directions.openType_main('SMS пользователю')
    #     with allure.step("Раскрытие настроек канала"):
    #         app.PO_Directions.openChanel('Резерв 1')
    #     with allure.step("Выбор типа управления"):
    #         app.PO_Directions.openType_rezerv_1('SMS пользователю')
    #     with allure.step("Проверка подсказки"):
    #         app.PO_Tooltips.tooltip_directions_current_user_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Направления - SMS пользователю - Отправлять время события - Резервный канал 1")
    def test_directions_rezerv_1_tooltip_3(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS пользователю')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('SMS пользователю')
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_send_event_time_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Направления - SMS пользователю - Отправлять дату события - Резервный канал 1")
    def test_directions_rezerv_1_tooltip_4(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS пользователю')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('SMS пользователю')
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_send_event_date_rezerv_1()

    # Не актуально 132879
    # @pytest.mark.parametrize("directions", directions_list)
    # @allure.story("Проверка подсказок наименования поля")
    # @allure.title("Направления - Включить тестирование канала - Резервный канал 1")
    # def test_directions_rezerv_1_tooltip_5(self, app, destination, close_modal, directions):
    #     with allure.step("Открытие направления"):
    #         app.PO_Directions.openDestination(directions)
    #     with allure.step("Предусловия раскрытия настроек канала"):
    #         app.PO_Directions.openChanel('Основной')
    #         app.PO_Directions.openType_main('SMS пользователю')
    #     with allure.step("Раскрытие настроек канала"):
    #         app.PO_Directions.openChanel('Резерв 1')
    #     with allure.step("Выбор типа управления"):
    #         app.PO_Directions.openType_rezerv_1('SMS пользователю')
    #     with allure.step("Проверка подсказки"):
    #         app.PO_Tooltips.tooltip_directions_enable_channel_testing_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Направления - Таймаут при ошибке - Резервный канал 1")
    def test_directions_rezerv_1_tooltip_6(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS пользователю')
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('SMS пользователю')
        with allure.step("Включить тестирование канала"):
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_timeout_on_error_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Направления - Тестировать если - Резервный канал 1")
    def test_directions_rezerv_1_tooltip_7(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS пользователю')
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('SMS пользователю')
        with allure.step("Включить тестирование канала"):
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_test_if_rezerv_1()

    # Не актуально 132879
    # @pytest.mark.parametrize("directions", directions_list)
    # @allure.story("Проверка подсказок наименования поля")
    # @allure.title("Направления - Метод тестирования - Резервный канал 1")
    # def test_directions_rezerv_1_tooltip_8(self, app, destination, close_modal, directions):
    #     with allure.step("Открытие направления"):
    #         app.PO_Directions.openDestination(directions)
    #     with allure.step("Предусловия раскрытия настроек канала"):
    #         app.PO_Directions.openChanel('Основной')
    #         app.PO_Directions.openType_main('SMS пользователю')
    #         app.PO_Directions.enableChannelTesting_main()
    #     with allure.step("Раскрытие настроек канала"):
    #         app.PO_Directions.openChanel('Резерв 1')
    #     with allure.step("Выбор типа управления"):
    #         app.PO_Directions.openType_rezerv_1('SMS пользователю')
    #     with allure.step("Включить тестирование канала"):
    #         app.PO_Directions.enableChannelTesting_rezerv_1()
    #     with allure.step("Проверка подсказки"):
    #         app.PO_Tooltips.tooltip_directions_test_method_rezerv_1()

    # Не актуально 132879
    # @pytest.mark.parametrize("directions", directions_list)
    # @allure.story("Проверка подсказок наименования поля")
    # @allure.title("Направления - Тестировать - Резервный канал 1")
    # def test_directions_rezerv_1_tooltip_9(self, app, destination, close_modal, directions):
    #     with allure.step("Открытие направления"):
    #         app.PO_Directions.openDestination(directions)
    #     with allure.step("Предусловия раскрытия настроек канала"):
    #         app.PO_Directions.openChanel('Основной')
    #         app.PO_Directions.openType_main('SMS пользователю')
    #         app.PO_Directions.enableChannelTesting_main()
    #     with allure.step("Раскрытие настроек канала"):
    #         app.PO_Directions.openChanel('Резерв 1')
    #     with allure.step("Выбор типа управления"):
    #         app.PO_Directions.openType_rezerv_1('SMS пользователю')
    #     with allure.step("Включить тестирование канала"):
    #         app.PO_Directions.enableChannelTesting_rezerv_1()
    #     with allure.step("Проверка подсказки"):
    #         app.PO_Tooltips.tooltip_directions_test_rezerv_1()

    # Не актуально 132879
    # @pytest.mark.parametrize("directions", directions_list)
    # @allure.story("Проверка подсказок наименования поля")
    # @allure.title("Направления - Дни недели - Резервный канал 1")
    # def test_directions_rezerv_1_tooltip_10(self, app, destination, close_modal, directions):
    #     with allure.step("Открытие направления"):
    #         app.PO_Directions.openDestination(directions)
    #     with allure.step("Предусловия раскрытия настроек канала"):
    #         app.PO_Directions.openChanel('Основной')
    #         app.PO_Directions.openType_main('SMS пользователю')
    #         app.PO_Directions.enableChannelTesting_main()
    #     with allure.step("Раскрытие настроек канала"):
    #         app.PO_Directions.openChanel('Резерв 1')
    #     with allure.step("Выбор типа управления"):
    #         app.PO_Directions.openType_rezerv_1('SMS пользователю')
    #     with allure.step("Включить тестирование канала"):
    #         app.PO_Directions.enableChannelTesting_rezerv_1()
    #     with allure.step("Проверка подсказки"):
    #         app.PO_Tooltips.tooltip_directions_days_of_th_week_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Направления - Звонок - Количество повторов - Резервный канал 1")
    def test_directions_rezerv_1tooltip_11(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('Звонок')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('Звонок')
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_number_of_repetitions_rezerv_1()

    # Не актуально 132879
    # @pytest.mark.parametrize("directions", directions_list)
    # @allure.story("Проверка подсказок наименования поля")
    # @allure.title("Направления - DC09 - Адрес - Резервный канал 1")
    # def test_directions_rezerv_1_tooltip_12(self, app, destination, close_modal, directions):
    #     with allure.step("Открытие направления"):
    #         app.PO_Directions.openDestination(directions)
    #     with allure.step("Предусловия раскрытия настроек канала"):
    #         app.PO_Directions.openChanel('Основной')
    #         app.PO_Directions.openType_main('DC09')
    #     with allure.step("Раскрытие настроек канала"):
    #         app.PO_Directions.openChanel('Резерв 1')
    #     with allure.step("Выбор типа управления"):
    #         app.PO_Directions.openType_rezerv_1('DC09')
    #     with allure.step("Проверка подсказки"):
    #         app.PO_Tooltips.tooltip_directions_address_rezerv_1()

    # Не актуально 132879
    # @pytest.mark.parametrize("directions", directions_list)
    # @allure.story("Проверка подсказок наименования поля")
    # @allure.title("Направления - DC09 - Порт - Резервный канал 1")
    # def test_directions_rezerv_1_tooltip_13(self, app, destination, close_modal, directions):
    #     with allure.step("Открытие направления"):
    #         app.PO_Directions.openDestination(directions)
    #     with allure.step("Предусловия раскрытия настроек канала"):
    #         app.PO_Directions.openChanel('Основной')
    #         app.PO_Directions.openType_main('DC09')
    #     with allure.step("Раскрытие настроек канала"):
    #         app.PO_Directions.openChanel('Резерв 1')
    #     with allure.step("Выбор типа управления"):
    #         app.PO_Directions.openType_rezerv_1('DC09')
    #     with allure.step("Проверка подсказки"):
    #         app.PO_Tooltips.tooltip_directions_port_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Направления - DC09 - Канал соединения - Резервный канал 1")
    def test_directions_rezerv_1_tooltip_14(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('DC09')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('DC09')
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_connection_channel_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Направления - DC09 - Таймаут подтверждения, сек - Резервный канал 1")
    def test_directions_rezerv_1_tooltip_15(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('DC09')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('DC09')
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_confirmation_timeout_sec_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Направления - DC09 - Количество повторов - Резервный канал 1")
    def test_directions_rezerv_1_tooltip_16(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('DC09')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('DC09')
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_number_of_repetitions_DC09_rezerv_1()

    # Не актуально 132879
    # @pytest.mark.parametrize("directions", directions_list)
    # @allure.story("Проверка подсказок наименования поля")
    # @allure.title("Направления - DC09 - Шифрование - Резервный канал 1")
    # def test_directions_rezerv_1_tooltip_17(self, app, destination, close_modal, directions):
    #     with allure.step("Открытие направления"):
    #         app.PO_Directions.openDestination(directions)
    #     with allure.step("Предусловия раскрытия настроек канала"):
    #         app.PO_Directions.openChanel('Основной')
    #         app.PO_Directions.openType_main('DC09')
    #     with allure.step("Раскрытие настроек канала"):
    #         app.PO_Directions.openChanel('Резерв 1')
    #     with allure.step("Выбор типа управления"):
    #         app.PO_Directions.openType_rezerv_1('DC09')
    #     with allure.step("Проверка подсказки"):
    #         app.PO_Tooltips.tooltip_directions_encryption_rezerv_1()

    # Не актуально 132879
    # @pytest.mark.parametrize("directions", directions_list)
    # @allure.story("Проверка подсказок наименования поля")
    # @allure.title("Направления - DC09 - Ключ шифрования - Резервный канал 1")
    # def test_directions_rezerv_1_tooltip_18(self, app, destination, close_modal, directions):
    #     with allure.step("Открытие направления"):
    #         app.PO_Directions.openDestination(directions)
    #     with allure.step("Предусловия раскрытия настроек канала"):
    #         app.PO_Directions.openChanel('Основной')
    #         app.PO_Directions.openType_main('DC09')
    #     with allure.step("Раскрытие настроек канала"):
    #         app.PO_Directions.openChanel('Резерв 1')
    #     with allure.step("Выбор типа управления"):
    #         app.PO_Directions.openType_rezerv_1('DC09')
    #     with allure.step("Проверка подсказки"):
    #         app.PO_Tooltips.tooltip_directions_encryption_keyn_rezerv_1()


@allure.epic("Тесты ВСПЛЫВАЮЩИЕ ПОДСКАЗКИ")
@allure.feature("Направления")
@pytest.mark.flaky(reruns=reruns)
class Test04TooltipsMassegeDirections():

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Направления - Номер телефона - код - Резервный канал 1")
    def test_directions_rezerv_1_tooltip_input_2(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS пользователю')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('SMS пользователю')
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_phone_cod_input_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Направления - Номер телефона - номер - Резервный канал 1")
    def test_directions_rezerv_1_tooltip_input_3(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS пользователю')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('SMS пользователю')
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_phone_number_input_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Направления - Таймаут при ошибке - Резервный канал 1")
    def test_directions_rezerv_1_tooltip_input_4(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS пользователю')
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('SMS пользователю')
        with allure.step("Включить тестирование канала"):
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_timeout_on_error_input_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Направления - Звонок - Количество повторов - Резервный канал 1")
    def test_directions_rezerv_1_tooltip_input_5(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('Звонок')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('Звонок')
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_number_of_repetitions_input_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Направления - DC09 - Адрес - Резервный канал 1")
    def test_directions_rezerv_1_tooltip_input_6(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('DC09')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('DC09')
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_address_input_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Направления - DC09 - Порт - Резервный канал 1")
    def test_directions_rezerv_1_tooltip_input_7(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('DC09')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('DC09')
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_port_input_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Направления - DC09 - Таймаут подтверждения, сек - Резервный канал 1")
    def test_directions_rezerv_1_tooltip_input_8(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('DC09')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('DC09')
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_confirmation_timeout_sec_input_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Направления - DC09 - Количество повторов - Резервный канал 1")
    def test_directions_rezerv_1_input_9(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('DC09')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('DC09')
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_number_of_repetitions_DC09_rezerv_1()

    # Не актуально 132879
    # @pytest.mark.parametrize("directions", directions_list)
    # @allure.story("Проверка подсказок наименования поля")
    # @allure.title("Направления - Текущий пользователь - Резервный канал 2")
    # def test_directions_rezerv_2_tooltip_2(self, app, destination, close_modal, directions):
    #     with allure.step("Открытие направления"):
    #         app.PO_Directions.openDestination(directions)
    #     with allure.step("Предусловия раскрытия настроек канала"):
    #         app.PO_Directions.openChanel('Основной')
    #         app.PO_Directions.openType_main('SMS пользователю')
    #         app.PO_Directions.openChanel('Резерв 1')
    #         app.PO_Directions.openType_rezerv_1('SMS пользователю')
    #     with allure.step("Раскрытие настроек канала"):
    #         app.PO_Directions.openChanel('Резерв 2')
    #     with allure.step("Выбор типа управления"):
    #         app.PO_Directions.openType_rezerv_2('SMS пользователю')
    #     with allure.step("Проверка подсказки"):
    #         app.PO_Tooltips.tooltip_directions_current_user_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Направления - SMS пользователю - Отправлять время события - Резервный канал 2")
    def test_directions_rezerv_2_tooltip_3(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS пользователю')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('SMS пользователю')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('SMS пользователю')
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_send_event_time_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Направления - SMS пользователю - Отправлять дату события - Резервный канал 2")
    def test_directions_rezerv_2_tooltip_4(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS пользователю')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('SMS пользователю')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('SMS пользователю')
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_send_event_date_rezerv_2()

    # Не актуально 132879
    # @pytest.mark.parametrize("directions", directions_list)
    # @allure.story("Проверка подсказок наименования поля")
    # @allure.title("Направления - Включить тестирование канала - Резервный канал 2")
    # def test_directions_rezerv_2_tooltip_5(self, app, destination, close_modal, directions):
    #     with allure.step("Открытие направления"):
    #         app.PO_Directions.openDestination(directions)
    #     with allure.step("Предусловия раскрытия настроек канала"):
    #         app.PO_Directions.openChanel('Основной')
    #         app.PO_Directions.openType_main('SMS пользователю')
    #         app.PO_Directions.openChanel('Резерв 1')
    #         app.PO_Directions.openType_rezerv_1('SMS пользователю')
    #     with allure.step("Раскрытие настроек канала"):
    #         app.PO_Directions.openChanel('Резерв 2')
    #     with allure.step("Выбор типа управления"):
    #         app.PO_Directions.openType_rezerv_2('SMS пользователю')
    #     with allure.step("Проверка подсказки"):
    #         app.PO_Tooltips.tooltip_directions_enable_channel_testing_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Направления - Таймаут при ошибке - Резервный канал 2")
    def test_directions_rezerv_2_tooltip_6(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS пользователю')
            app.PO_Directions.enableChannelTesting_main()
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('SMS пользователю')
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('SMS пользователю')
        with allure.step("Включить тестирование канала"):
            app.PO_Directions.enableChannelTesting_rezerv_2()
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_timeout_on_error_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Направления - Тестировать если - Резервный канал 2")
    def test_directions_rezerv_2_tooltip_7(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS пользователю')
            app.PO_Directions.enableChannelTesting_main()
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('SMS пользователю')
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('SMS пользователю')
        with allure.step("Включить тестирование канала"):
            app.PO_Directions.enableChannelTesting_rezerv_2()
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_test_if_rezerv_2()

    # Не актуально 132879
    # @pytest.mark.parametrize("directions", directions_list)
    # @allure.story("Проверка подсказок наименования поля")
    # @allure.title("Направления - Метод тестирования - Резервный канал 2")
    # def test_directions_rezerv_2_tooltip_8(self, app, destination, close_modal, directions):
    #     with allure.step("Открытие направления"):
    #         app.PO_Directions.openDestination(directions)
    #     with allure.step("Предусловия раскрытия настроек канала"):
    #         app.PO_Directions.openChanel('Основной')
    #         app.PO_Directions.openType_main('SMS пользователю')
    #         app.PO_Directions.enableChannelTesting_main()
    #         app.PO_Directions.openChanel('Резерв 1')
    #         app.PO_Directions.openType_rezerv_1('SMS пользователю')
    #         app.PO_Directions.enableChannelTesting_rezerv_1()
    #     with allure.step("Раскрытие настроек канала"):
    #         app.PO_Directions.openChanel('Резерв 2')
    #     with allure.step("Выбор типа управления"):
    #         app.PO_Directions.openType_rezerv_2('SMS пользователю')
    #     with allure.step("Включить тестирование канала"):
    #         app.PO_Directions.enableChannelTesting_rezerv_2()
    #     with allure.step("Проверка подсказки"):
    #         app.PO_Tooltips.tooltip_directions_test_method_rezerv_2()

    # Не актуально 132879
    # @pytest.mark.parametrize("directions", directions_list)
    # @allure.story("Проверка подсказок наименования поля")
    # @allure.title("Направления - Тестировать - Резервный канал 2")
    # def test_directions_rezerv_2_tooltip_9(self, app, destination, close_modal, directions):
    #     with allure.step("Открытие направления"):
    #         app.PO_Directions.openDestination(directions)
    #     with allure.step("Предусловия раскрытия настроек канала"):
    #         app.PO_Directions.openChanel('Основной')
    #         app.PO_Directions.openType_main('SMS пользователю')
    #         app.PO_Directions.enableChannelTesting_main()
    #         app.PO_Directions.openChanel('Резерв 1')
    #         app.PO_Directions.openType_rezerv_1('SMS пользователю')
    #         app.PO_Directions.enableChannelTesting_rezerv_1()
    #     with allure.step("Раскрытие настроек канала"):
    #         app.PO_Directions.openChanel('Резерв 2')
    #     with allure.step("Выбор типа управления"):
    #         app.PO_Directions.openType_rezerv_2('SMS пользователю')
    #     with allure.step("Включить тестирование канала"):
    #         app.PO_Directions.enableChannelTesting_rezerv_2()
    #     with allure.step("Проверка подсказки"):
    #         app.PO_Tooltips.tooltip_directions_test_rezerv_2()


@allure.epic("Тесты ВСПЛЫВАЮЩИЕ ПОДСКАЗКИ")
@allure.feature("Направления")
@pytest.mark.flaky(reruns=reruns)
class Test05TooltipsMassegeDirections():

    # Не актуально 132879
    # @pytest.mark.parametrize("directions", directions_list)
    # @allure.story("Проверка подсказок наименования поля")
    # @allure.title("Направления - Дни недели - Резервный канал 2")
    # def test_directions_rezerv_2_tooltip_10(self, app, destination, close_modal, directions):
    #     with allure.step("Открытие направления"):
    #         app.PO_Directions.openDestination(directions)
    #     with allure.step("Предусловия раскрытия настроек канала"):
    #         app.PO_Directions.openChanel('Основной')
    #         app.PO_Directions.openType_main('SMS пользователю')
    #         app.PO_Directions.enableChannelTesting_main()
    #         app.PO_Directions.openChanel('Резерв 1')
    #         app.PO_Directions.openType_rezerv_1('SMS пользователю')
    #         app.PO_Directions.enableChannelTesting_rezerv_1()
    #     with allure.step("Раскрытие настроек канала"):
    #         app.PO_Directions.openChanel('Резерв 2')
    #     with allure.step("Выбор типа управления"):
    #         app.PO_Directions.openType_rezerv_2('SMS пользователю')
    #     with allure.step("Включить тестирование канала"):
    #         app.PO_Directions.enableChannelTesting_rezerv_2()
    #     with allure.step("Проверка подсказки"):
    #         app.PO_Tooltips.tooltip_directions_days_of_th_week_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Направления - Звонок - Количество повторов - Резервный канал 2")
    def test_directions_rezerv_2_tooltip_11(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('Звонок')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('Звонок')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('Звонок')
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_number_of_repetitions_rezerv_2()

    # Не актуально 132879
    # @pytest.mark.parametrize("directions", directions_list)
    # @allure.story("Проверка подсказок наименования поля")
    # @allure.title("Направления - DC09 - Адрес - Резервный канал 2")
    # def test_directions_rezerv_2_tooltip_12(self, app, destination, close_modal, directions):
    #     with allure.step("Открытие направления"):
    #         app.PO_Directions.openDestination(directions)
    #     with allure.step("Предусловия раскрытия настроек канала"):
    #         app.PO_Directions.openChanel('Основной')
    #         app.PO_Directions.openType_main('DC09')
    #         app.PO_Directions.openChanel('Резерв 1')
    #         app.PO_Directions.openType_rezerv_1('DC09')
    #     with allure.step("Раскрытие настроек канала"):
    #         app.PO_Directions.openChanel('Резерв 2')
    #     with allure.step("Выбор типа управления"):
    #         app.PO_Directions.openType_rezerv_2('DC09')
    #     with allure.step("Проверка подсказки"):
    #         app.PO_Tooltips.tooltip_directions_address_rezerv_2()

    # Не актуально 132879
    # @pytest.mark.parametrize("directions", directions_list)
    # @allure.story("Проверка подсказок наименования поля")
    # @allure.title("Направления - DC09 - Порт - Резервный канал 2")
    # def test_directions_rezerv_2_tooltip_13(self, app, destination, close_modal, directions):
    #     with allure.step("Открытие направления"):
    #         app.PO_Directions.openDestination(directions)
    #     with allure.step("Предусловия раскрытия настроек канала"):
    #         app.PO_Directions.openChanel('Основной')
    #         app.PO_Directions.openType_main('DC09')
    #         app.PO_Directions.openChanel('Резерв 1')
    #         app.PO_Directions.openType_rezerv_1('DC09')
    #     with allure.step("Раскрытие настроек канала"):
    #         app.PO_Directions.openChanel('Резерв 2')
    #     with allure.step("Выбор типа управления"):
    #         app.PO_Directions.openType_rezerv_2('DC09')
    #     with allure.step("Проверка подсказки"):
    #         app.PO_Tooltips.tooltip_directions_port_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Направления - DC09 - Канал соединения - Резервный канал 2")
    def test_directions_rezerv_2_tooltip_14(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('DC09')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('DC09')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('DC09')
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_connection_channel_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Направления - DC09 - Таймаут подтверждения, сек - Резервный канал 2")
    def test_directions_rezerv_2_tooltip_15(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('DC09')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('DC09')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('DC09')
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_confirmation_timeout_sec_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок наименования поля")
    @allure.title("Направления - DC09 - Количество повторов - Резервный канал 2")
    def test_directions_rezerv_2_tooltip_16(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('DC09')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('DC09')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('DC09')
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_number_of_repetitions_DC09_rezerv_2()

    # Не актуально 132879
    # @pytest.mark.parametrize("directions", directions_list)
    # @allure.story("Проверка подсказок наименования поля")
    # @allure.title("Направления - DC09 - Шифрование - Резервный канал 2")
    # def test_directions_rezerv_2_tooltip_17(self, app, destination, close_modal, directions):
    #     with allure.step("Открытие направления"):
    #         app.PO_Directions.openDestination(directions)
    #     with allure.step("Предусловия раскрытия настроек канала"):
    #         app.PO_Directions.openChanel('Основной')
    #         app.PO_Directions.openType_main('DC09')
    #         app.PO_Directions.openChanel('Резерв 1')
    #         app.PO_Directions.openType_rezerv_1('DC09')
    #     with allure.step("Раскрытие настроек канала"):
    #         app.PO_Directions.openChanel('Резерв 2')
    #     with allure.step("Выбор типа управления"):
    #         app.PO_Directions.openType_rezerv_2('DC09')
    #     with allure.step("Проверка подсказки"):
    #         app.PO_Tooltips.tooltip_directions_encryption_rezerv_2()

    # Не актуально 132879
    # @pytest.mark.parametrize("directions", directions_list)
    # @allure.story("Проверка подсказок наименования поля")
    # @allure.title("Направления - DC09 - Ключ шифрования - Резервный канал 2")
    # def test_directions_rezerv_2_tooltip_18(self, app, destination, close_modal, directions):
    #     with allure.step("Открытие направления"):
    #         app.PO_Directions.openDestination(directions)
    #     with allure.step("Предусловия раскрытия настроек канала"):
    #         app.PO_Directions.openChanel('Основной')
    #         app.PO_Directions.openType_main('DC09')
    #         app.PO_Directions.openChanel('Резерв 1')
    #         app.PO_Directions.openType_rezerv_1('DC09')
    #     with allure.step("Раскрытие настроек канала"):
    #         app.PO_Directions.openChanel('Резерв 2')
    #     with allure.step("Выбор типа управления"):
    #         app.PO_Directions.openType_rezerv_2('DC09')
    #     with allure.step("Проверка подсказки"):
    #         app.PO_Tooltips.tooltip_directions_encryption_keyn_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Направления - Номер телефона - код - Резервный канал 2")
    def test_directions_rezerv_2_tooltip_input_2(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS пользователю')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('SMS пользователю')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('SMS пользователю')
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_phone_cod_input_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Направления - Номер телефона - номер - Резервный канал 2")
    def test_directions_rezerv_2_tooltip_input_3(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS пользователю')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('SMS пользователю')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('SMS пользователю')
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_phone_number_input_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Направления - Таймаут при ошибке - Резервный канал 2")
    def test_directions_rezerv_2_tooltip_input_4(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS пользователю')
            app.PO_Directions.enableChannelTesting_main()
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('SMS пользователю')
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('SMS пользователю')
        with allure.step("Включить тестирование канала"):
            app.PO_Directions.enableChannelTesting_rezerv_2()
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_timeout_on_error_input_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Направления - Звонок - Количество повторов - Резервный канал 2")
    def test_directions_rezerv_2_tooltip_input_5(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('Звонок')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('Звонок')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('Звонок')
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_number_of_repetitions_input_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Направления - DC09 - Адрес - Резервный канал 2")
    def test_directions_rezerv_2_tooltip_input_6(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('DC09')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('DC09')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('DC09')
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_address_input_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Направления - DC09 - Порт - Резервный канал 2")
    def test_directions_rezerv_2_tooltip_input_7(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('DC09')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('DC09')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('DC09')
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_port_input_rezerv_2()


@allure.epic("Тесты ВСПЛЫВАЮЩИЕ ПОДСКАЗКИ")
@allure.feature("Направления")
@pytest.mark.flaky(reruns=reruns)
class Test06TooltipsMassegeDirections():

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Направления - DC09 - Таймаут подтверждения, сек - Резервный канал 2")
    def test_directions_rezerv_2_tooltip_input_8(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('DC09')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('DC09')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('DC09')
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_confirmation_timeout_sec_input_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Проверка подсказок полей ввода")
    @allure.title("Направления - DC09 - Количество повторов - Резервный канал 2")
    def test_directions_rezerv_2_input_9(self, app, destination, close_modal, directions):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('DC09')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('DC09')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('DC09')
        with allure.step("Проверка подсказки"):
            app.PO_Tooltips.tooltip_directions_number_of_repetitions_DC09_rezerv_2()
