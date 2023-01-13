# -*- coding: utf-8 -*-
import time

import allure
import pytest
from selenium.webdriver.common.by import By

reruns = 2


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
        time.sleep(1)
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
    with allure.step("Включить модуль GSM"):
        app.PO_Settings.modul_settings_gsm_on()




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
@allure.feature("Проверки UI")
@pytest.mark.flaky(reruns=reruns)
class TestUiSettings:

    @allure.story("ОБЪЕКТ")
    @allure.title("Проверка чекбоксов объекта")
    def test_checkbox_object(self, app, object):
        with allure.step("Проверка включения чекбоксов"):
            app.PO_Settings.check_box_object_on()
        with allure.step("Проверка выключения чекбоксов"):
            app.PO_Settings.check_box_object_off()
        with allure.step("Проверка частичного выбора чекбоксов"):
            app.PO_Settings.check_box_object_some()

    @allure.story("ОБЪЕКТ")
    @allure.title("Проверка названий полей на странице")
    def test_main_title_object(self, app, object):
        with allure.step("Проверка названий полей"):
            app.PO_Settings.text_object_page()

    @allure.story("ОБЪЕКТ")
    @allure.title("Проверка кнопки сохранить при валидном заполнении данных в обязательном поле ввода")
    def test_check_save_button_valid_data_object(self, app, object):
        with allure.step("Проверка кликабельности кнопки СОХРАНИТЬ"):
            app.PO_Settings.data_in_all_entry_field_object()

    @allure.story("ОБЪЕКТ")
    @allure.title("Проверка отсутсвия возможности сохранения при пустом не обязательном поле ввода 'Номер объекта'")
    def test_no_data_number_object(self, app, object):
        with allure.step("Проверка кнопки сохранить"):
            app.PO_Settings.no_data_in_number_object()

    @allure.story("ОБЪЕКТ")
    @allure.title("Проверка отсутсвия возможности сохранения при пустом обязательном поле ввода 'Задержка взятия'")
    def test_no_data_delay_take_on_object(self, app, object):
        with allure.step("Проверка кнопки сохранить"):
            app.PO_Settings.no_data_delay_take_on_object()

    @allure.story("ОБЪЕКТ")
    @allure.title(
        "Проверка отсутсвия возможности сохранения при пустом обязательном поле ввода 'Задержка тревоги входа'")
    def test_no_data_delay_alarm_enter_object(self, app, object):
        with allure.step("Проверка кнопки сохранить"):
            app.PO_Settings.no_data_delay_alarm_enter_object()

    @allure.story("ОБЪЕКТ")
    @allure.title("Проверка отсутсвия возможности сохранения при пустом обязательном поле ввода 'Время автовзятия'")
    def test_no_data_time_auto_take_on_object(self, app, object):
        with allure.step("Проверка кнопки сохранить"):
            app.PO_Settings.no_data_time_auto_take_on_object()

    @allure.story("GSM")
    @allure.title("Проверка названий полей на странице")
    def test_main_title_gsm(self, app, GSM):
        with allure.step("Проверка названий полей"):
            app.PO_Settings.text_gsm_page()

    @allure.story("GSM")
    @allure.title("Проверка названий полей на модальном окне: Отправка тестового SMS SIM 1/2")
    def test_main_title_gsm_sms(self, app, GSM, close_modal):
        with allure.step("Проверка названий полей"):
            app.PO_Settings.text_gsm_page_SMS()

    @allure.story("GSM")
    @allure.title("Проверка чекбоксов gsm")
    def test_checkbox_gsm(self, app, GSM):
        with allure.step("Проверка включения чекбоксов"):
            app.PO_Settings.check_box_gsm_on()
        with allure.step("Проверка выключения чекбоксов"):
            app.PO_Settings.check_box_gsm_off()
        with allure.step("Проверка частичного выбора чекбоксов"):
            app.PO_Settings.check_box_gsm_some()

    @allure.story("ДАТА И ВРЕМЯ")
    @allure.title("Проверка названий полей на странице")
    def test_main_title_data_time(self, app, date_time):
        with allure.step("Проверка названий полей Использовать время GSM сети"):
            app.PO_Settings.text_date_time_page_gsm()
        with allure.step("Проверка названий полей Синхронизация по NTP/HTP"):
            app.PO_Settings.text_date_time_page_ntp()
        with allure.step("Проверка названий полей Вручную"):
            app.PO_Settings.text_date_time_page_hand()

    @allure.story("ДАТА И ВРЕМЯ")
    @allure.title("Проверка выпадающего списка: Дата и время на устройстве")
    def test_checkbox_data_time_on_device(self, app, date_time):
        with allure.step("Проверка выбора позиций из выпадающего списка"):
            app.PO_Settings.drop_list_date_time_on_device()

    @allure.story("ДАТА И ВРЕМЯ")
    @allure.title("Проверка выпадающего списка Использовать время GSM сети: Часовой пояс")
    def test_checkbox_data_time_timezone_1(self, app, date_time):
        with allure.step("Выбор: Использовать время GSM сети"):
            app.PO_Settings.Use_GSM_network_time_click()
        with allure.step("Снятие чекбокса: Использовать временную зону GSM сети"):
            app.PO_Settings.use_gsm_time_off()
        with allure.step("Проверка выбора позиций из выпадающего списка"):
            app.PO_Settings.drop_list_date_time_timezone()

    @allure.story("ДАТА И ВРЕМЯ")
    @allure.title("Проверка чекбоксов выпадающего списка Использовать время GSM сети")
    def test_checkbox_data_time_Use_GSM_network_time(self, app, date_time):
        with allure.step("Выбор: Использовать время GSM сети"):
            app.PO_Settings.Use_GSM_network_time_click()
        with allure.step("Проверка включения чекбоксов"):
            app.PO_Settings.check_box_data_time_on()
        with allure.step("Проверка выключения чекбоксов"):
            app.PO_Settings.check_box_data_time_off()
        with allure.step("Проверка некликабельных чекбоксов"):
            app.PO_Settings.check_box_data_time_some()

    @allure.story("ДАТА И ВРЕМЯ")
    @allure.title(
        "Проверка появления выпадающего списка 'Часовой пояс' при выборе чекбокса: Использовать время GSM сети")
    def test_checkbox_timezone_data_time_Use_GSM_network_time(self, app, date_time):
        with allure.step("Выбор: Использовать время GSM сети"):
            app.PO_Settings.Use_GSM_network_time_click()
        with allure.step("Проверка поля 'Часовой пояс' при включенном чекбоксе"):
            app.PO_Settings.check_box_data_time_Use_time_zone_of_GSM_network_status_on()
        with allure.step("Проверка поля 'Часовой пояс' при отключенном чекбоксе"):
            app.PO_Settings.check_box_data_time_Use_time_zone_of_GSM_network_status_off()

    @allure.story("ДАТА И ВРЕМЯ")
    @allure.title("Проверка выпадающего списка Синхронизация по NTP/HTP: Часовой пояс")
    def test_checkbox_data_time_timezone_2(self, app, date_time):
        with allure.step("Выбор: Синхронизация по NTP/HTP"):
            app.PO_Settings.Synchronization_via_NTP_HTP_click()
        with allure.step("Проверка выбора позиций из выпадающего списка"):
            app.PO_Settings.drop_list_date_time_timezone()

    @allure.story("ДАТА И ВРЕМЯ")
    @allure.title("Проверка выпадающего списка Вручную: Часовой пояс")
    def test_checkbox_data_time_timezone_3(self, app, date_time):
        with allure.step("Выбор: Вручную"):
            app.PO_Settings.Manually_click()
        with allure.step("Проверка выбора позиций из выпадающего списка"):
            app.PO_Settings.drop_list_date_time_timezone()

    @allure.story("ПРИБОР")
    @allure.title("Проверка названий полей на странице")
    def test_main_title_device(self, app, device):
        with allure.step("Проверка названий полей"):
            app.PO_Settings.text_device_page()

    @allure.story("ПРИБОР")
    @allure.title("Проверка названий полей на странице")
    def test_main_title_device(self, app, device):
        with allure.step("Проверка названий полей"):
            app.PO_Settings.text_device_page()

    @allure.story("ПРИБОР")
    @allure.title("Проверка чекбоксов прибора")
    def test_checkbox_device(self, app, device):
        with allure.step("Проверка включения чекбоксов"):
            app.PO_Settings.check_box_device_on()
        with allure.step("Проверка выключения чекбоксов"):
            app.PO_Settings.check_box_device_off()
        with allure.step("Проверка некликабельных чекбоксов"):
            app.PO_Settings.check_box_device_some()
        with allure.step("Проверка частичного включения чекбоксов"):
            app.PO_Settings.check_box_device_some_2()

    @allure.story("Световая индикация")
    @allure.title("Проверка названий полей на странице")
    def test_main_title_light_indication(self, app, light_indication):
        with allure.step("Проверка названий полей"):
            app.PO_Settings.text_light_indication_page()

    @allure.story("Световая индикация")
    @allure.title("Проверка чекбоксов cветовой индикации")
    def test_checkbox_light_indication(self, app, light_indication):
        with allure.step("Проверка включения чекбоксов"):
            app.PO_Settings.check_box_light_indication_on()
        with allure.step("Проверка выключения чекбоксов"):
            app.PO_Settings.check_box_light_indication_off()

    @allure.story("Световая индикация")
    @allure.title("Проверка выпадающего списка: Режим светодиодов для охранных датчиков")
    def test_checkbox_light_indication_LED_mode_for_security_sensors(self, app, light_indication):
        with allure.step("Проверка выбора позиций из выпадающего списка"):
            app.PO_Settings.drop_list_light_indication_LED_mode_for_security_sensors()

    @allure.story("Световая индикация")
    @allure.title("Проверка выпадающего списка: Режим светодиодов для пожарных датчиков")
    def test_checkbox_light_indication_LED_mode_for_fire_detectors(self, app, light_indication):
        with allure.step("Проверка выбора позиций из выпадающего списка"):
            app.PO_Settings.drop_list_light_indication_LED_mode_for_fire_detectors()

    @allure.story("Световая индикация")
    @allure.title("Проверка выпадающего списка: Режим светодиодов для технологических датчиков")
    def test_checkbox_light_indication_LED_mode_for_process_sensors(self, app, light_indication):
        with allure.step("Проверка выбора позиций из выпадающего списка"):
            app.PO_Settings.drop_list_light_indication_LED_mode_for_process_sensors()

    @allure.story("Световая индикация")
    @allure.title("Проверка выпадающего списка: Режим работы считывателя")
    def test_checkbox_light_indication_reader_operation_mode(self, app, light_indication):
        with allure.step("Проверка выбора позиций из выпадающего списка"):
            app.PO_Settings.drop_list_light_indication_reader_operation_mode()

    @allure.story("РАДИО")
    @allure.title("Проверка чекбокса радио")
    def test_check_box_radio(self, app, radio):
        with allure.step("Проверка включения чекбоксов"):
            app.PO_Settings.check_box_radio_on()
        with allure.step("Проверка выключения чекбоксов"):
            app.PO_Settings.check_box_radio_off()

    @allure.story("РАДИО")
    @allure.title("Проверка выпадающего списка")
    def test_checkbox_radio(self, app, radio):
        with allure.step("Проверка выбора позиций из выпадающего списка"):
            app.PO_Settings.drop_list_radio()

    @allure.story("РАДИО")
    @allure.title("Проверка названий полей на странице")
    def test_main_title_radio(self, app, radio):
        with allure.step("Проверка названий полей"):
            app.PO_Settings.text_radio_page()

    @allure.story("Звуковая индикация")
    @allure.title("Проверка виджета ползунка - 'Громкость событий'")
    def test_event_volume_slider_widget(self, app, volum_indication):
        with allure.step("Проверка выбора положения виджета ползунка"):
            app.PO_Settings.input_event_volume_slider_widget()

    @allure.story("Звуковая индикация")
    @allure.title("Проверка виджета ползунка - 'Громкость тревог'")
    def test_alarm_volume_slider_widget(self, app, volum_indication):
        with allure.step("Проверка выбора положения виджета ползунка"):
            app.PO_Settings.input_alarm_volume_slider_widget()

    @allure.story("Звуковая индикация")
    @allure.title("Проверка названий полей на странице")
    def test_main_title_volum_indication(self, app, volum_indication):
        with allure.step("Проверка названий полей"):
            app.PO_Settings.text_volum_indication_page()

    @allure.story("Звуковая индикация")
    @allure.title("Проверка чек-боксов звуковой индикации")
    def test_checkbox_volum_indication(self, app, volum_indication):
        with allure.step("Открытие 'Связанные события'"):
            app.PO_Settings.open_volum_indication_events()
        with allure.step("Проверка включения чекбоксов"):
            app.PO_Settings.check_box_volum_indication_on()
        with allure.step("Проверка выключения чекбоксов"):
            app.PO_Settings.check_box_volum_indication_off()
        with allure.step("Проверка частичного выбора чекбоксов"):
            app.PO_Settings.check_box_volum_indication_some()

    @allure.story("ETHERNET")
    @allure.title("Проверка чек-боксов ETHERNET")
    def test_checkbox_ethernet(self, app, ethernet):
        with allure.step("Проверка включения чекбоксов"):
            app.PO_Settings.check_box_ethernet_on()
        with allure.step("Проверка выключения чекбоксов"):
            app.PO_Settings.check_box_ethernet_off()
        with allure.step("Проверка частичного выбора чекбоксов"):
            app.PO_Settings.check_box_ethernet_some()

    @allure.story("ETHERNET")
    @allure.title("Проверка выпадающего списка")
    def test_dropdown_list_ethernet(self, app, ethernet):
        with allure.step("Проверка выбора позиций из выпадающего списка"):
            app.PO_Settings.drop_list_ethernet()

    @allure.story("ETHERNET")
    @allure.title("Проверка названий полей на странице")
    def test_main_title_ethernet(self, app, ethernet):
        with allure.step("Проверка названий полей"):
            app.PO_Settings.text_ethernet_page()
