# -*- coding: utf-8 -*-

import allure
import pytest
from selenium.webdriver.common.by import By

reruns = 0


@pytest.fixture()
def close_modal_sensor(request, app):
    def fin():
        app.method.click((By.XPATH, '(//*[.=" Отменить "]//div)[last()]'))

    request.addfinalizer(fin)


@pytest.fixture
def c_2000p_sdvig(app):
    with allure.step("Переход на страницу Зоны Разделы"):
        app.PO_Navigations.goToZonePathPage()
    with allure.step("Переход на вкладку 'Датчики'"):
        app.PO_Navigations.goToZonePathSensorsZone()
    with allure.step("Раскрытие настроек"):
        app.PO_Sensors.sensor_settings_button()

@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты ДАТЧИКИ")
@pytest.mark.flaky(reruns=reruns)
class TestSensorC_2000P_SDVIG:

    @allure.story("С2000Р_СДВИГ")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Название'")
    def test_c_2000p_sdvig_name_input_positiv(self, app, c_2000p_sdvig, close_modal_sensor):
        with allure.step("Проверка валидации поля"):
            app.PO_Sensors.input_name_positiv()

    @allure.story("С2000Р_СДВИГ")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Название")
    def test_c_2000p_sdvig_name_input_negativ(self, app, c_2000p_sdvig, close_modal_sensor):
        with allure.step("Проверка валидации поля"):
            app.PO_Sensors.input_name_negativ()

    @allure.story("С2000Р_СДВИГ")
    @allure.title("Проверка названий полей")
    def test_c_2000p_sdvig_titles(self, app, c_2000p_sdvig, close_modal_sensor):
        with allure.step("Проверка названий полей"):
            app.PO_Sensors.text_c2000p_sdvig_title()

    @allure.story("С2000Р_СДВИГ")
    @allure.title("Проверка переключения чек-боксов")
    def test_c_2000p_sdvig_check_box(self, app, c_2000p_sdvig, close_modal_sensor):
        with allure.step("Проверка включения чекбоксов"):
            app.PO_Sensors.check_box_c_2000p_sdvig_on()
        with allure.step("Проверка выключения чекбоксов"):
            app.PO_Sensors.check_box_c_2000p_sdvig_on()
        with allure.step("Проверка частичного выбора чекбоксов"):
            app.PO_Sensors.check_box_c_2000p_sdvig_some()

    @allure.story("С2000Р_СДВИГ")
    @allure.title("Проверка выпадающего списка: Раздел")
    def test_c_2000p_sdvig_drop_list_path(self, app, c_2000p_sdvig, close_modal_sensor):
        with allure.step("Проверка выбора позиций из выпадающего списка"):
            app.PO_Sensors.drop_list_path_c_2000p_sdvig()

    @allure.story("С2000Р_СДВИГ")
    @allure.title("Проверка выпадающего списка: Режим индикации")
    def test_c_2000p_sdvig_drop_list_indication_mode(self, app, c_2000p_sdvig, close_modal_sensor):
        with allure.step("Проверка выбора позиций из выпадающего списка"):
            app.PO_Sensors.drop_list_indication_mode_c_2000p_smk()

    @allure.story("С2000Р_СДВИГ")
    @allure.title("Проверка выпадающего списка: Порог тревоги по наклону")
    def test_c_2000p_sdvig_drop_list_tilt_alarm_threshold(self, app, c_2000p_sdvig, close_modal_sensor):
        with allure.step("Проверка выбора позиций из выпадающего списка"):
            app.PO_Sensors.drop_list_tilt_alarm_threshold_c_2000p_sdvig()

    @allure.story("С2000Р_СДВИГ")
    @allure.title("Проверка сохранения данных")
    def test_c_2000p_sdvig_save_data(self, app, c_2000p_sdvig, close_modal_sensor):
        with allure.step("Генерирование тестовых данных"):
            app.ganerate_data.createData()
        with allure.step("Заполнение полей данными"):
            app.PO_Sensors.save_data_c_2000p_sdvig()
        with allure.step("Сохранение данных"):
            app.PO_Directions.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToZonePathPage()
            app.PO_Navigations.goToZonePathSensorsZone()
            app.PO_Sensors.sensor_settings_button()
        with allure.step("Проверка сохранения"):
            app.PO_Sensors.assert_save_data_c_2000p_sdvig()
