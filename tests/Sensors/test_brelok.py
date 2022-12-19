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
def brelok(app):
    with allure.step("Переход на страницу Зоны Разделы"):
        app.PO_Navigations.goToZonePathPage()
    with allure.step("Переход на вкладку 'Брелоки'"):
        app.PO_Navigations.goToZonePathKeyring()
    with allure.step("Раскрытие настроек"):
        app.PO_Sensors.first_sensor_settings_button()
    with allure.step("Раскрытие - Права управления"):
        app.PO_Sensors.select_management_rights('Права управления')

@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты ДАТЧИКИ")
@pytest.mark.flaky(reruns=reruns)
class TestSensorBrelok:

    @allure.story("БРЕЛОК")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Название'")
    def test_brelok_name_input_positiv(self, app, brelok, close_modal_sensor):
        with allure.step("Проверка валидации поля"):
            app.PO_Sensors.input_name_positiv()

    @allure.story("БРЕЛОК")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Название")
    def test_brelok_name_input_negativ(self, app, brelok, close_modal_sensor):
        with allure.step("Проверка валидации поля"):
            app.PO_Sensors.input_name_negativ()

    @allure.story("БРЕЛОК")
    @allure.title("Проверка названий полей")
    def test_brelok_titles(self, app, brelok, close_modal_sensor):
        with allure.step("Проверка названий полей"):
            app.PO_Sensors.text_brelok_title()

    @allure.story("БРЕЛОК")
    @allure.title("Проверка переключения чек-боксов")
    def test_brelok_check_box(self, app, brelok, close_modal_sensor):
        with allure.step("Проверка включения чекбоксов"):
            app.PO_Sensors.check_box_brelok_on()
        with allure.step("Проверка выключения чекбоксов"):
            app.PO_Sensors.check_box_brelok_off()
        with allure.step("Проверка частичного выбора чекбоксов"):
            app.PO_Sensors.check_box_brelok_some()

    @allure.story("БРЕЛОК")
    @allure.title("Проверка выпадающего списка: Пользователь")
    def test_brelok_drop_list_user(self, app, brelok, close_modal_sensor):
        with allure.step("Проверка выбора позиций из выпадающего списка"):
            app.PO_Sensors.drop_list_user()

    @allure.story("БРЕЛОК")
    @allure.title("Проверка выпадающего списка: Раздел")
    def test_brelok_drop_list_path(self, app, brelok, close_modal_sensor):
        with allure.step("Проверка выбора позиций из выпадающего списка"):
            app.PO_Sensors.drop_list_path_brelok()

    @allure.story("БРЕЛОК")
    @allure.title("Проверка выпадающего списка: Способ вызова тихой тревоги")
    def test_brelok_drop_list_silent_alarm_method(self, app, brelok, close_modal_sensor):
        with allure.step("Проверка выбора позиций из выпадающего списка"):
            app.PO_Sensors.drop_list_silent_alarm_method()

    @allure.story("БРЕЛОК")
    @allure.title("Проверка выпадающего списка: Группа выходов кнопки 1")
    def test_brelok_drop_list_button_output_group_1(self, app, brelok, close_modal_sensor):
        with allure.step("Проверка выбора позиций из выпадающего списка"):
            app.PO_Sensors.drop_list_button_output_group_1()

    @allure.story("БРЕЛОК")
    @allure.title("Проверка выпадающего списка: Группа выходов кнопки 2")
    def test_brelok_drop_list_button_output_group_2(self, app, brelok, close_modal_sensor):
        with allure.step("Проверка выбора позиций из выпадающего списка"):
            app.PO_Sensors.drop_list_button_output_group_2()

    @allure.story("БРЕЛОК")
    @allure.title("Проверка выпадающего списка с чек-боксом: Управляемые разделы")
    def test_brelok_drop_list_path_with_check_box(self, app, brelok, close_modal_sensor):
        with allure.step("Проверка выбора позиций из выпадающего списка"):
            app.PO_Sensors.drop_list_path_with_check_box()

    @allure.story("БРЕЛОК")
    @allure.title("Проверка сохранения данных")
    def test_brelok_save_data(self, app, brelok, close_modal_sensor):
        with allure.step("Генерирование тестовых данных"):
            app.ganerate_data.createData()
        with allure.step("Заполнение полей данными"):
            app.PO_Sensors.save_data_brelok()
        with allure.step("Сохранение данных"):
            app.PO_Directions.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToZonePathPage()
            app.PO_Navigations.goToZonePathKeyring()
            app.PO_Sensors.first_sensor_settings_button()
            app.PO_Sensors.select_management_rights('Права управления')
        with allure.step("Проверка сохранения"):
            app.PO_Sensors.assert_save_data_brelok()







