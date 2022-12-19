# -*- coding: utf-8 -*-

import allure
import pytest
from selenium.webdriver.common.by import By

reruns = 1


@pytest.fixture()
def close_modal(request, app):
    def fin():
        app.method.click((By.XPATH, '(//*[.=" Отменить "]//div)[last()]'))

    request.addfinalizer(fin)


@pytest.fixture
def object(app):
    with allure.step("Переход на страницу Настройки"):
        app.PO_Navigations.goToSettingsPage()
    with allure.step("Переход на вкладку 'Объект'"):
        app.PO_Navigations.goToObjectPage()
    with allure.step("Клик по кнопке 'Редактировать'"):
        app.PO_Settings.edit_button_click()


@pytest.fixture
def date_time(app):
    with allure.step("Переход на страницу Настройки"):
        app.PO_Navigations.goToSettingsPage()
    with allure.step("Переход на вкладку 'Дата и время'"):
        app.PO_Navigations.goToDateTimePage()
    with allure.step("Клик по кнопке 'Редактировать'"):
        app.PO_Settings.edit_button_click()


@pytest.fixture
def device(app):
    with allure.step("Переход на страницу Настройки"):
        app.PO_Navigations.goToSettingsPage()
    with allure.step("Переход на вкладку 'Прибор'"):
        app.PO_Navigations.goToDevicePage()
    with allure.step("Клик по кнопке 'Редактировать'"):
        app.PO_Settings.edit_button_click()


@pytest.fixture
def radio(app):
    with allure.step("Переход на страницу Настройки"):
        app.PO_Navigations.goToSettingsPage()
    with allure.step("Переход на вкладку 'Прибор'"):
        app.PO_Navigations.goToRadioPage()
    with allure.step("Клик по кнопке 'Редактировать'"):
        app.PO_Settings.edit_button_click()


@pytest.fixture
def ethernet(app):
    with allure.step("Переход на страницу Настройки"):
        app.PO_Navigations.goToSettingsPage()
    with allure.step("Переход на вкладку 'ethernet'"):
        app.PO_Navigations.goToEthernetPage()
    with allure.step("Клик по кнопке 'Редактировать'"):
        app.PO_Settings.edit_button_click()


@pytest.fixture
def light_indication(app):
    with allure.step("Переход на страницу Настройки"):
        app.PO_Navigations.goToSettingsPage()
    with allure.step("Переход на вкладку 'Световая индикация'"):
        app.PO_Navigations.goToLightIndicationPage()
    with allure.step("Клик по кнопке 'Редактировать'"):
        app.PO_Settings.edit_button_click()


@pytest.fixture
def volum_indication(app):
    with allure.step("Переход на страницу Настройки"):
        app.PO_Navigations.goToSettingsPage()
    with allure.step("Переход на вкладку 'Звуковая индикация'"):
        app.PO_Navigations.goToVolumIndicationPage()
    with allure.step("Клик по кнопке 'Редактировать'"):
        app.PO_Settings.edit_button_click()


@pytest.fixture
def GSM(app):
    with allure.step("Переход на страницу Настройки"):
        app.PO_Navigations.goToSettingsPage()
    with allure.step("Переход на вкладку 'GSM'"):
        app.PO_Navigations.goToGSMPage()
    with allure.step("Клик по кнопке 'Редактировать'"):
        app.PO_Settings.edit_button_click()


@pytest.fixture
def exit_enter(app):
    with allure.step("Переход на страницу Настройки"):
        app.PO_Navigations.goToSettingsPage()
    with allure.step("Переход на вкладку 'GSM'"):
        app.PO_Navigations.goToGSMPage()
    with allure.step("Клик по кнопке 'Редактировать'"):
        app.PO_Settings.edit_button_click()

@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты НАСТРОЙКИ")
@allure.feature("Сохранение данных")
@pytest.mark.flaky(reruns=reruns)
class TestSaveSettings:

    @allure.story("ОБЪЕКТ")
    @allure.title("Проверка сохранения настроек объекта: параметризованный тест")
    @pytest.mark.parametrize("randomCB_1, randomCB_2, randomCB_3, randomCB_4, randomCB_5",
                             [
                                 ('ON', 'ON', 'ON', 'ON', 'ON'),
                                 ('OFF', 'ON', 'ON', 'ON', 'ON'),
                                 ('ON', 'OFF', 'ON', 'ON', 'ON'),
                                 ('ON', 'ON', 'OFF', 'ON', 'ON'),
                                 ('ON', 'ON', 'ON', 'OFF', 'ON'),
                                 ('ON', 'ON', 'ON', 'ON', 'OFF'),
                                 ('OFF', 'OFF', 'OFF', 'OFF', 'OFF'),
                                 ('ON', 'OFF', 'OFF', 'OFF', 'OFF'),
                                 ('OFF', 'ON', 'OFF', 'OFF', 'OFF'),
                                 ('OFF', 'OFF', 'ON', 'OFF', 'OFF'),
                                 ('OFF', 'OFF', 'OFF', 'ON', 'OFF'),
                                 ('OFF', 'OFF', 'OFF', 'OFF', 'ON')
                             ])
    def test_data_save_object_01(self, app, object, randomCB_1, randomCB_2, randomCB_3, randomCB_4, randomCB_5):
        with allure.step("Генерирование тестовых данных"):
            app.ganerate_data.createData()
        with allure.step("Заполнение полей данными"):
            app.PO_Settings.save_object_data()
        with allure.step("Выбор чек-боксов"):
            app.PO_Settings.save_object_check_box(randomCB_1, randomCB_2, randomCB_3, randomCB_4, randomCB_5)
        with allure.step("Сохранение данных"):
            app.PO_Settings.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToSettingsPage()
            app.PO_Navigations.goToObjectPage()
            app.PO_Settings.edit_button_click()
        with allure.step("Проверка сохраненных данных в полях ввода"):
            app.PO_Settings.save_object_data_check()
        with allure.step("Проверка сохранения выбора чек-боксов"):
            app.PO_Settings.save_object_check_box_check(randomCB_1, randomCB_2, randomCB_3, randomCB_4, randomCB_5)
        with allure.step("Завершение настроек"):
            app.PO_Settings.finish_setting()

    @allure.story("ОБЪЕКТ")
    @allure.title("Проверка сохранения настроек объекта: граничные значения")
    @pytest.mark.parametrize(
        "name, number, delay_take, delay_alarm, time_take_on, randomCB_1, randomCB_2, randomCB_3, randomCB_4, randomCB_5",
        [
            (('a' * 32), '9999', '65535', '65535', '65535', 'ON', 'ON', 'ON', 'ON', 'ON'),
            ('1', '1', '5', '5', '5', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF')
        ])
    def test_data_save_object_limit_values(self, app, object, name, number, delay_take, delay_alarm, time_take_on,
                                           randomCB_1, randomCB_2, randomCB_3, randomCB_4, randomCB_5):
        with allure.step("Заполнение полей данными"):
            app.PO_Settings.save_object_data_limit(name, number, delay_take, delay_alarm, time_take_on, randomCB_1,
                                                   randomCB_2, randomCB_3, randomCB_4, randomCB_5)
        with allure.step("Сохранение данных"):
            app.PO_Settings.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToSettingsPage()
            app.PO_Navigations.goToObjectPage()
            app.PO_Settings.edit_button_click()
        with allure.step("Проверка сохраненных данных в полях ввода"):
            app.PO_Settings.save_object_data_limit_check(name, number, delay_take, delay_alarm, time_take_on,
                                                         randomCB_1, randomCB_2, randomCB_3, randomCB_4, randomCB_5)
        with allure.step("Завершение настроек"):
            app.PO_Settings.finish_setting()


    @allure.story("ПРИБОР")
    @allure.title("Проверка сохранения настроек прибор: параметризованный тест")
    @pytest.mark.parametrize("power_saving_mode, setting_case_closed, path_alarms, sensor_alarms,"
                             " fire_path_alarms, fire_sensor_alarms, repeat_events, manage_outputs",
                             [
                                 ('ON', 'ON', 'ON', 'ON', 'ON', 'ON', 'ON', 'ON'),
                                 ('ON', 'ON', 'ON', 'OFF', 'ON', 'OFF', 'ON', 'OFF'),
                                 ('ON', 'ON', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF'),
                                 ('ON', 'ON', 'ON', 'ON', 'OFF', 'OFF', 'OFF', 'OFF'),
                                 ('ON', 'ON', 'OFF', 'OFF', 'ON', 'ON', 'OFF', 'OFF'),
                                 ('ON', 'ON', 'OFF', 'OFF', 'OFF', 'OFF', 'ON', 'ON'),
                                 ('OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF')
                             ])
    def test_data_save_device(self, app, device, power_saving_mode, setting_case_closed, path_alarms,
                              sensor_alarms, fire_path_alarms, fire_sensor_alarms, repeat_events, manage_outputs):
        with allure.step("Выбор чек-боксов"):
            app.PO_Settings.save_device_check_box(power_saving_mode, setting_case_closed, path_alarms,
                                                  sensor_alarms, fire_path_alarms, fire_sensor_alarms, repeat_events,
                                                  manage_outputs)
        with allure.step("Сохранение данных"):
            app.PO_Settings.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToSettingsPage()
            app.PO_Navigations.goToDevicePage()
            app.PO_Settings.edit_button_click()
        with allure.step("Проверка сохранения чек-боксов"):
            app.PO_Settings.save_device_check_box_data(power_saving_mode, setting_case_closed, path_alarms,
                                                       sensor_alarms, fire_path_alarms, fire_sensor_alarms,
                                                       repeat_events, manage_outputs)
        with allure.step("Завершение настроек"):
            app.PO_Settings.finish_setting()

    @allure.story("СВЕТОВАЯ ИНДИКАЦИЯ")
    @allure.title("Проверка сохранения настроек Световой индикации: параметризованный тест")
    @pytest.mark.parametrize(
        "security_sensors, fire_detectors, process_sensors, operation_mode, checkbox_reader_indication",
        [
            ('Согласно настройкам прибора', 'Включено для всех', 'Выключено для всех',
             '2 светодиода, 1-ое касание - статус, последующие управляющие',
             'ON'),
            ('Согласно настройкам прибора', 'Согласно настройкам прибора', 'Согласно настройкам прибора',
             '1 светодиод, 1-ое касание - статус, последующие управляющие',
             'ON'),
            ('Включено для всех', 'Включено для всех', 'Включено для всех',
             '1 светодиод, 1-ое касание - статус, 2-ое - управляющее',
             'OFF'),
            ('Выключено для всех', 'Выключено для всех', 'Выключено для всех',
             '2 светодиода, 1-ое касание - статус, последующие управляющие',
             'ON'),
            ('Согласно настройкам прибора', 'Включено для всех', 'Выключено для всех',
             '2 светодиода, 1-ое касание - статус, второе - управляющее',
             'OFF'),
            ('Выключено для всех', 'Согласно настройкам прибора', 'Включено для всех',
             '2 светодиода, любое касание - управляющее',
             'ON')
        ])
    def test_data_save_light_indication(self, app, light_indication, security_sensors, fire_detectors, process_sensors,
                                        operation_mode, checkbox_reader_indication):
        with allure.step("Внесение изменений в настройки световой индикации"):
            app.PO_Settings.save_light_indication_settings(security_sensors, fire_detectors, process_sensors,
                                                           operation_mode, checkbox_reader_indication)
        with allure.step("Сохранение данных"):
            app.PO_Settings.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToSettingsPage()
            app.PO_Navigations.goToLightIndicationPage()
            app.PO_Settings.edit_button_click()
        with allure.step("Проверка сохранения настроек световой индикации"):
            app.PO_Settings.save_light_indication_settings_data(security_sensors, fire_detectors, process_sensors,
                                                                operation_mode, checkbox_reader_indication)

        with allure.step("Завершение настроек"):
            app.PO_Settings.finish_setting()

    @allure.story("РАДИО")
    @allure.title("Проверка сохранения настроек радио")
    @pytest.mark.parametrize("chanel_list",
                             [
                                 ('1'),
                                 ('2'),
                                 ('3'),
                                 ('4'),
                                 ('5'),
                                 ('6'),
                                 ('7'),
                                 ('8'),
                                 ('9'),
                                 ('10')
                             ])
    def test_data_save_radio(self, app, radio, chanel_list):
        with allure.step("Генерирование тестовых данных"):
            app.ganerate_data.createData()
        with allure.step("Внесение изменений в настройки радио"):
            app.PO_Settings.save_radio_data(chanel_list)
        with allure.step("Сохранение данных"):
            app.PO_Settings.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToSettingsPage()
            app.PO_Navigations.goToRadioPage()
            app.PO_Settings.edit_button_click()
        with allure.step("Проверка сохраненных данных"):
            app.PO_Settings.save_radio_data_enter(chanel_list)
        with allure.step("Завершение настроек"):
            app.PO_Settings.finish_setting()

    @allure.story("РАДИО")
    @allure.title("Проверка сохранения настроек радио")
    @pytest.mark.parametrize("randomCB, chanel_list, time_add_sensor, periud_sensor",
                             [
                                 ('ON', '1', '60', '5'),
                                 ('ON', '1', '900', '120')
                             ])
    def test_data_save_radio_limit(self, app, radio, randomCB, chanel_list, time_add_sensor, periud_sensor):
        with allure.step("Внесение изменений в настройки радио"):
            app.PO_Settings.save_radio_data_limit(randomCB, chanel_list, time_add_sensor, periud_sensor)
        with allure.step("Сохранение данных"):
            app.PO_Settings.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToSettingsPage()
            app.PO_Navigations.goToRadioPage()
            app.PO_Settings.edit_button_click()
        with allure.step("Проверка сохраненных данных"):
            app.PO_Settings.save_radio_data_enter_limit(chanel_list, time_add_sensor, periud_sensor)
        with allure.step("Завершение настроек"):
            app.PO_Settings.finish_setting()

    @allure.story("ЗВУКОВАЯ ИНДИКАЦИЯ")
    @allure.title("Проверка сохранения настроек звуковой индикации")
    @pytest.mark.parametrize(
        "main, Alarm, Fire, Taking_section, Removing_partition, Take_Delay, Not_taking, Sections_partially, Adding_sensor, Bell",
        [
            ('ON', 'ON', 'ON', 'ON', 'ON', 'ON', 'ON', 'ON', 'ON', 'ON'),
            ('ON', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF'),
            ('ON', 'OFF', 'ON', 'ON', 'ON', 'ON', 'ON', 'ON', 'ON', 'ON'),
            ('ON', 'ON', 'OFF', 'ON', 'ON', 'ON', 'ON', 'ON', 'ON', 'ON'),
            ('ON', 'ON', 'ON', 'OFF', 'ON', 'ON', 'ON', 'ON', 'ON', 'ON'),
            ('ON', 'ON', 'ON', 'ON', 'OFF', 'ON', 'ON', 'ON', 'ON', 'ON'),
            ('ON', 'ON', 'ON', 'ON', 'ON', 'OFF', 'ON', 'ON', 'ON', 'ON'),
            ('ON', 'ON', 'ON', 'ON', 'ON', 'ON', 'OFF', 'ON', 'ON', 'ON'),
            ('ON', 'ON', 'ON', 'ON', 'ON', 'ON', 'ON', 'OFF', 'ON', 'ON'),
            ('ON', 'ON', 'ON', 'ON', 'ON', 'ON', 'ON', 'ON', 'OFF', 'ON'),
            ('ON', 'ON', 'ON', 'ON', 'ON', 'ON', 'ON', 'ON', 'ON', 'OFF'),
            ('ON', 'ON', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF'),
            ('ON', 'OFF', 'ON', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF'),
            ('ON', 'OFF', 'OFF', 'ON', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF'),
            ('ON', 'OFF', 'OFF', 'OFF', 'ON', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF'),
            ('ON', 'OFF', 'OFF', 'OFF', 'OFF', 'ON', 'OFF', 'OFF', 'OFF', 'OFF'),
            ('ON', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'ON', 'OFF', 'OFF', 'OFF'),
            ('ON', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'ON', 'OFF', 'OFF'),
            ('ON', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'ON', 'OFF'),
            ('ON', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'ON')
        ])
    def test_data_save_01_volum_indication(self, app, volum_indication, main, Alarm, Fire, Taking_section,
                                           Removing_partition, Take_Delay, Not_taking, Sections_partially,
                                           Adding_sensor, Bell):
        with allure.step("Генерирование тестовых данных"):
            app.ganerate_data.createData()
        with allure.step("Открытие 'Связанные события'"):
            app.PO_Settings.open_volum_indication_events()
        with allure.step("Внесение изменений в настройки звуковой индикации"):
            app.PO_Settings.save_volum_indication_data(main, Alarm, Fire, Taking_section,
                                                       Removing_partition, Take_Delay, Not_taking, Sections_partially,
                                                       Adding_sensor, Bell)
        with allure.step("Сохранение данных"):
            app.PO_Settings.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToSettingsPage()
            app.PO_Navigations.goToVolumIndicationPage()
            app.PO_Settings.open_volum_indication_events()
            app.PO_Settings.edit_button_click()
        with allure.step("Проверка сохраненных данных"):
            app.PO_Settings.save_volum_indication_data_enter(main, Alarm, Fire, Taking_section,
                                                             Removing_partition, Take_Delay, Not_taking,
                                                             Sections_partially,
                                                             Adding_sensor, Bell)
        with allure.step("Завершение настроек"):
            app.PO_Settings.finish_setting()

    @allure.story("ЗВУКОВАЯ ИНДИКАЦИЯ")
    @allure.title("Проверка сохранения настроек звуковой индикации граничные значения")
    @pytest.mark.parametrize(
        "signal_duration_value, Event_volume, Alarm_volume, main, Alarm, Fire, Taking_section, Removing_partition, Take_Delay, Not_taking, Sections_partially, Adding_sensor, Bell",
        [
            ('10', '1', '1', 'ON', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF'),
            ('65535', '100', '100', 'ON', 'ON', 'ON', 'ON', 'ON', 'ON', 'ON', 'ON', 'ON', 'ON')

        ])
    def test_data_save_02_volum_indication(self, app, signal_duration_value, Event_volume, Alarm_volume,
                                           volum_indication,
                                           main, Alarm, Fire, Taking_section,
                                           Removing_partition, Take_Delay, Not_taking, Sections_partially,
                                           Adding_sensor, Bell):
        with allure.step("Открытие 'Связанные события'"):
            app.PO_Settings.open_volum_indication_events()
        with allure.step("Внесение изменений в настройки звуковой индикации"):
            app.PO_Settings.save_volum_indication_data_limit(signal_duration_value, Event_volume, Alarm_volume, main,
                                                             Alarm, Fire, Taking_section,
                                                             Removing_partition, Take_Delay, Not_taking,
                                                             Sections_partially,
                                                             Adding_sensor, Bell)
        with allure.step("Сохранение данных"):
            app.PO_Settings.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToSettingsPage()
            app.PO_Navigations.goToVolumIndicationPage()
            app.PO_Settings.open_volum_indication_events()
            app.PO_Settings.edit_button_click()
        with allure.step("Проверка сохраненных данных"):
            app.PO_Settings.save_volum_indication_data_enter_limit(signal_duration_value, Event_volume, Alarm_volume,
                                                                   main, Alarm, Fire, Taking_section,
                                                                   Removing_partition, Take_Delay, Not_taking,
                                                                   Sections_partially,
                                                                   Adding_sensor, Bell)
        with allure.step("Завершение настроек"):
            app.PO_Settings.finish_setting()

    @allure.story("ДАТА И ВРЕМЯ")
    @allure.title("Проверка сохранения настроек даты и времени: Использовать время GSM сети")
    @pytest.mark.parametrize("randomCB_1, randomCB_2, UTC",
                             [
                                 ('OFF', 'ON', 'UTC (GMT)'),
                                 ('OFF', 'OFF', 'UTC +01:00 (СЕТ)'),
                                 ('OFF', 'ON', 'UTC +02:00 (Калининградское время)'),
                                 ('OFF', 'ON', 'UTC +03:00 (Московское время)'),
                                 ('OFF', 'ON', 'UTC +04:00 (Самарское время)'),
                                 ('OFF', 'ON', 'UTC +05:00 (Екатеринбурское время)'),
                                 ('OFF', 'ON', 'UTC +06:00 (Омское время)'),
                                 ('OFF', 'ON', 'UTC +07:00 (Красноярское время)'),
                                 ('OFF', 'ON', 'UTC +08:00 (Иркутское время)'),
                                 ('OFF', 'ON', 'UTC +09:00 (Якутское время)'),
                                 ('OFF', 'ON', 'UTC +10:00 (Владивостокское время)'),
                                 ('OFF', 'ON', 'UTC +11:00 (Среднеколымское время)'),
                                 ('OFF', 'ON', 'UTC +12:00 (Камчатское время)'),
                                 ('OFF', 'ON', 'UTC -01:00'),
                                 ('OFF', 'ON', 'UTC -02:00'),
                                 ('OFF', 'ON', 'UTC -03:00'),
                                 ('OFF', 'ON', 'UTC -04:00'),
                                 ('OFF', 'ON', 'UTC -05:00'),
                                 ('OFF', 'ON', 'UTC -06:00'),
                                 ('OFF', 'ON', 'UTC -07:00'),
                                 ('OFF', 'ON', 'UTC -08:00'),
                                 ('OFF', 'ON', 'UTC -09:00'),
                                 ('OFF', 'ON', 'UTC -10:00'),
                                 ('OFF', 'ON', 'UTC -11:00'),
                                 ('OFF', 'ON', 'UTC -12:00')
                             ])
    def test_data_save_data_time_gsm_time_1(self, app, date_time, randomCB_1, randomCB_2, UTC):
        with allure.step("Выбор из выпадающего списка - Дата и время на устройстве: 'Использовать время GSM сети'"):
            app.PO_Settings.Use_GSM_network_time_click()
        with allure.step("Внесение изменений в настройки даты и время"):
            app.PO_Settings.save_data_time(randomCB_1, randomCB_2, UTC)
        with allure.step("Сохранение данных"):
            app.PO_Settings.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToSettingsPage()
            app.PO_Navigations.goToDateTimePage()
            app.PO_Settings.edit_button_click()
            app.PO_Settings.Use_GSM_network_time_click()
        with allure.step("Проверка сохраненных данных"):
            app.PO_Settings.save_data_time_enter(randomCB_1, randomCB_2, UTC)
        with allure.step("Завершение настроек"):
            app.PO_Settings.finish_setting()

    @allure.story("ДАТА И ВРЕМЯ")
    @allure.title("Проверка сохранения настроек даты и времени: Синхронизация по NTP/HTP")
    @pytest.mark.parametrize("UTC",
                             [
                                 ('UTC (GMT)'),
                                 ('UTC +01:00 (СЕТ)'),
                                 ('UTC +02:00 (Калининградское время)'),
                                 ('UTC +03:00 (Московское время)'),
                                 ('UTC +04:00 (Самарское время)'),
                                 ('UTC +05:00 (Екатеринбурское время)'),
                                 ('UTC +06:00 (Омское время)'),
                                 ('UTC +07:00 (Красноярское время)'),
                                 ('UTC +08:00 (Иркутское время)'),
                                 ('UTC +09:00 (Якутское время)'),
                                 ('UTC +10:00 (Владивостокское время)'),
                                 ('UTC +11:00 (Среднеколымское время)'),
                                 ('UTC +12:00 (Камчатское время)'),
                                 ('UTC -01:00'),
                                 ('UTC -02:00'),
                                 ('UTC -03:00'),
                                 ('UTC -04:00'),
                                 ('UTC -05:00'),
                                 ('UTC -06:00'),
                                 ('UTC -07:00'),
                                 ('UTC -08:00'),
                                 ('UTC -09:00'),
                                 ('UTC -10:00'),
                                 ('UTC -11:00'),
                                 ('UTC -12:00')
                             ])
    def test_data_save_data_time_gsm_time_2(self, app, date_time, UTC):
        with allure.step("Генерирование тестовых данных"):
            app.ganerate_data.createData()
        with allure.step("Выбор из выпадающего списка - Дата и время на устройстве: 'Синхронизация по NTP/HTP'"):
            app.PO_Settings.Synchronization_via_NTP_HTP_click()
        with allure.step("Внесение изменений в настройки даты и время"):
            app.PO_Settings.save_data_time_2(UTC)
        with allure.step("Сохранение данных"):
            app.PO_Settings.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToSettingsPage()
            app.PO_Navigations.goToDateTimePage()
            app.PO_Settings.edit_button_click()
            app.PO_Settings.Synchronization_via_NTP_HTP_click()
        with allure.step("Проверка сохраненных данных"):
            app.PO_Settings.save_data_time_enter_2(UTC)
        with allure.step("Завершение настроек"):
            app.PO_Settings.finish_setting()


    @allure.story("GSM")
    @allure.title("Проверка сохранения настроек gsm: параметризованный тест")
    @pytest.mark.parametrize("modul_on, use_gprs, use_reserv_sim, use_ussd, balans_not, translations_events",

                             [
                                 ('ON', 'ON', 'ON', 'ON', 'ON', 'ON'),
                                 ('ON', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF'),
                                 ('ON', 'ON', 'ON', 'ON', 'ON', 'ON'),
                                 ('ON', 'OFF', 'ON', 'ON', 'ON', 'ON'),
                                 ('ON', 'ON', 'OFF', 'ON', 'ON', 'ON'),
                                 ('ON', 'ON', 'ON', 'OFF', 'ON', 'ON'),
                                 ('ON', 'ON', 'ON', 'ON', 'OFF', 'ON'),
                                 ('ON', 'ON', 'ON', 'ON', 'ON', 'OFF'),
                                 ('ON', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF'),
                                 ('ON', 'ON', 'OFF', 'OFF', 'OFF', 'OFF'),
                                 ('ON', 'OFF', 'ON', 'OFF', 'OFF', 'OFF'),
                                 ('ON', 'OFF', 'OFF', 'ON', 'OFF', 'OFF'),
                                 ('ON', 'OFF', 'OFF', 'OFF', 'ON', 'OFF'),
                                 ('ON', 'OFF', 'OFF', 'OFF', 'OFF', 'ON'),
                             ])
    def test_data_save_gsm(self, app, GSM, modul_on, use_gprs, use_reserv_sim, use_ussd, balans_not,
                           translations_events):
        with allure.step("Генерирование тестовых данных"):
            app.ganerate_data.createData()
        with allure.step("Внесение изменений в настройки gsm"):
            app.ganerate_data.createData()
            app.PO_Settings.save_gsm_data(modul_on, use_gprs, use_reserv_sim, use_ussd, balans_not, translations_events)
        with allure.step("Сохранение данных"):
            app.PO_Settings.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToSettingsPage()
            app.PO_Navigations.goToGSMPage()
            app.PO_Settings.edit_button_click()
        with allure.step("Проверка сохраненных данных"):
            app.PO_Settings.save_gsm_data_enter(modul_on, use_gprs, use_reserv_sim, use_ussd, balans_not,
                                                translations_events)
        with allure.step("Завершение настроек"):
            app.PO_Settings.finish_setting()

    @allure.story("ETHERNET")
    @allure.title("Проверка сохранения настроек ethernet: параметризованный тест")
    @pytest.mark.parametrize(
        "randomCB_1, randomCB_2, randomCB_3, randomCB_4, randomCB_5, randomCB_6, Establish_network_connections",
        [
            ('ON', 'ON', 'ON', 'ON', 'ON', 'ON', 'Авто'),
            ('OFF', 'ON', 'ON', 'ON', 'ON', 'ON', 'Авто'),
            ('ON', 'OFF', 'ON', 'ON', 'ON', 'ON', 'Авто'),
            ('ON', 'ON', 'OFF', 'ON', 'ON', 'ON', 'Авто'),
            ('ON', 'ON', 'ON', 'OFF', 'ON', 'ON', 'Авто'),
            ('ON', 'ON', 'ON', 'ON', 'OFF', 'ON', 'Авто'),
            ('ON', 'ON', 'ON', 'ON', 'ON', 'OFF', 'Авто'),
            ('OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'Ethernet'),
            ('ON', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'Ethernet'),
            ('OFF', 'ON', 'OFF', 'OFF', 'OFF', 'OFF', 'Ethernet'),
            ('OFF', 'OFF', 'ON', 'OFF', 'OFF', 'OFF', 'Ethernet'),
            ('OFF', 'OFF', 'OFF', 'ON', 'OFF', 'OFF', 'Ethernet'),
            ('OFF', 'OFF', 'OFF', 'OFF', 'ON', 'OFF', 'Ethernet'),
            ('OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'ON', 'Ethernet'),
            ('OFF', 'ON', 'OFF', 'ON', 'OFF', 'ON', 'GPRS'),
            ('ON', 'OFF', 'ON', 'OFF', 'ON', 'OFF', 'GPRS')
        ])
    def test_data_save_ethernet(self, app, ethernet, randomCB_1, randomCB_2, randomCB_3, randomCB_4, randomCB_5,
                                randomCB_6, Establish_network_connections):
        with allure.step("Генерирование тестовых данных"):
            app.ganerate_data.createData()
        with allure.step("Внесение изменений в настройки ethernet"):
            app.ganerate_data.createData()
            app.PO_Settings.save_ethernet_data(randomCB_1, randomCB_2, randomCB_3, randomCB_4, randomCB_5, randomCB_6,
                                               Establish_network_connections)
        with allure.step("Сохранение данных"):
            app.PO_Settings.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToSettingsPage()
            app.PO_Navigations.goToEthernetPage()
            app.PO_Settings.edit_button_click()
        with allure.step("Проверка сохраненных данных"):
            app.PO_Settings.save_ethernet_data_enter(randomCB_1, randomCB_2, randomCB_3, randomCB_4, randomCB_5,
                                                     randomCB_6, Establish_network_connections)
        with allure.step("Завершение настроек"):
            app.PO_Settings.finish_setting()
