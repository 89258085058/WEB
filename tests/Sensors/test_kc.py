# -*- coding: utf-8 -*-

import allure
import pytest
from selenium.webdriver.common.by import By

reruns = 1


@pytest.fixture()
def close_modal_sensor(request, app):
    def fin():
        app.method.click((By.XPATH, '(//*[.=" Отменить "]//div)[last()]'))

    request.addfinalizer(fin)


@pytest.fixture
def sensor_kc(app):
    with allure.step("Переход на страницу Зоны Разделы"):
        app.PO_Navigations.goToZonePathPage()
    with allure.step("Переход на вкладку 'Датчики'"):
        app.PO_Navigations.goToZonePathSensorsZone()
    with allure.step("Раскрытие настроек"):
        app.PO_Sensors.sensor_settings_button()

@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты ДАТЧИКИ")
@pytest.mark.flaky(reruns=reruns)
class TestSensorKC:

    @allure.story("КЦ Сигнал-GSM")
    @allure.title("Проверка выпадающего списка: Тип зоны")
    def test_sensor_kc_drop_list_type_zone(self, app, sensor_kc, close_modal_sensor):
        with allure.step("Проверка выбора позиций из выпадающего списка"):
            app.PO_Sensors.drop_list_type_zone()

    @allure.story("КЦ Сигнал-GSM")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Название'")
    def test_sensor_kc_name_input_positiv(self, app, sensor_kc, close_modal_sensor):
        with allure.step("Проверка валидации поля"):
            app.PO_Sensors.input_name_positiv()

    @allure.story("КЦ Сигнал-GSM")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Название")
    def test_sensor_kc_name_input_negativ(self, app, sensor_kc, close_modal_sensor):
        with allure.step("Проверка валидации поля"):
            app.PO_Sensors.input_name_negativ()

    @allure.story("КЦ Сигнал-GSM")
    @allure.title("Проверка названий полей")
    def test_sensor_kc_titles(self, app, sensor_kc, close_modal_sensor):
        with allure.step("Проверка названий полей"):
            app.PO_Sensors.text_sensor_kc_title()

    @allure.story("КЦ Сигнал-GSM")
    @allure.title("Проверка переключения чек-боксов")
    def test_sensor_kc_check_box(self, app, sensor_kc, close_modal_sensor):
        with allure.step("Проверка включения чекбоксов"):
            app.PO_Sensors.check_box_sensor_kc_on()
        with allure.step("Проверка выключения чекбоксов"):
            app.PO_Sensors.check_box_sensor_kc_off()
        with allure.step("Проверка частичного выбора чекбоксов"):
            app.PO_Sensors.check_box_sensor_kc_some()

    @allure.story("КЦ Сигнал-GSM")
    @allure.title("Проверка выпадающего списка: Раздел")
    def test_sensor_kc_drop_list_path(self, app, sensor_kc, close_modal_sensor):
        with allure.step("Проверка выбора позиций из выпадающего списка"):
            app.PO_Sensors.drop_list_path_sensor_kc()

    @allure.story("КЦ Сигнал-GSM")
    @allure.title("Проверка сохранения данных")
    def test_sensor_kc_save_data(self, app, sensor_kc, close_modal_sensor):
        with allure.step("Генерирование тестовых данных"):
            app.ganerate_data.createData()
        with allure.step("Заполнение полей данными"):
            app.PO_Sensors.save_data_sensor_kc()
        with allure.step("Сохранение данных"):
            app.PO_Directions.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToZonePathPage()
            app.PO_Navigations.goToZonePathSensorsZone()
            app.PO_Sensors.sensor_settings_button()
        with allure.step("Проверка сохранения"):
            app.PO_Sensors.assert_save_data_sensor_kc()
