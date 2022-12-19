# -*- coding: utf-8 -*-

import allure
import pytest

reruns = 0


@pytest.fixture()
def close_modal(request, app):
    def fin():
        app.PO_Zone_Path.cancel()

    request.addfinalizer(fin)


@pytest.fixture
def add_path(app):
    with allure.step("Переход на страницу Зоны Разделы"):
        app.PO_Navigations.goToZonePathPage()
    with allure.step("Переход на вкладку 'Разделы'"):
        app.PO_Navigations.goToPathPage()
    with allure.step("Нажать на кнопку 'Добавить раздел'"):
        app.PO_Zone_Path.add_path()


@pytest.fixture
def settings_path(app):
    with allure.step("Переход на страницу Зоны Разделы"):
        app.PO_Navigations.goToZonePathPage()
    with allure.step("Переход на вкладку 'Разделы'"):
        app.PO_Navigations.goToPathPage()
    with allure.step("Добавление раздела при его отсутствии"):
        app.PO_Zone_Path.Add_path_if_not()
    with allure.step("Нажать на кнопку 'Настройки первого раздела'"):
        app.PO_Zone_Path.settings_first_path_button()


@pytest.fixture
def outs(app):
    with allure.step("Переход на страницу Зоны Разделы"):
        app.PO_Navigations.goToZonePathPage()
    with allure.step("Переход на вкладку 'Выходы'"):
        app.PO_Navigations.goToZonePathOuts()
    with allure.step("Клик по кнопке 'Редактировать'"):
        app.PO_Settings.edit_button_click()

@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты ЗОНЫ/РАЗДЕЛЫ")
@allure.feature("Валидация полей ввода")
@pytest.mark.flaky(reruns=reruns)
class TestZonePathValidationPath:

    @allure.story("РАЗДЕЛЫ")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Поиск'")
    def test_path_input_search(self, app):
        with allure.step("Переход на страницу Зоны Разделы"):
            app.PO_Navigations.goToZonePathPage()
        with allure.step("Переход на вкладку 'Разделы'"):
            app.PO_Navigations.goToPathPage()
        with allure.step("Проверка валидации поля"):
            app.PO_Zone_Path.input_seach()

    @allure.story("РАЗДЕЛЫ")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Номер'")
    def test_path_input_number_positiv(self, app, add_path, close_modal):
        with allure.step("Проверка валидации поля"):
            app.PO_Zone_Path.input_data_namber_path_positv()

    @allure.story("РАЗДЕЛЫ")
    @allure.title("Негитивные сценарии: Проверка ввода значений в поле 'Номер'")
    def test_path_input_number_negativ(self, app, add_path, close_modal):
        with allure.step("Проверка валидации поля"):
            app.PO_Zone_Path.input_data_namber_path_negativ()

    @allure.story("РАЗДЕЛЫ")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Название'")
    def test_path_input_name_positiv(self, app, add_path, close_modal):
        with allure.step("Проверка валидации поля"):
            app.PO_Zone_Path.input_data_name_path_positv()

    @allure.story("РАЗДЕЛЫ")
    @allure.title("Негитивные сценарии: Проверка ввода значений в поле 'Название'")
    def test_path_input_name_negativ(self, app, add_path, close_modal):
        with allure.step("Проверка валидации поля"):
            app.PO_Zone_Path.input_data_name_path_negativ()

    @allure.story("РАЗДЕЛЫ")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Номер' Настройки")
    def test_path_input_number_positiv_settings_path(self, app, settings_path, close_modal):
        with allure.step("Проверка валидации поля"):
            app.PO_Zone_Path.input_data_namber_path_positv()

    @allure.story("РАЗДЕЛЫ")
    @allure.title("Негитивные сценарии: Проверка ввода значений в поле 'Номер' Настройки")
    def test_path_input_number_negativ_settings_path(self, app, settings_path, close_modal):
        with allure.step("Проверка валидации поля"):
            app.PO_Zone_Path.input_data_namber_path_negativ()

    @allure.story("РАЗДЕЛЫ")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Название' Настройки")
    def test_path_input_name_positiv_settings_path(self, app, settings_path, close_modal):
        with allure.step("Проверка валидации поля"):
            app.PO_Zone_Path.input_data_name_path_positv()

    @allure.story("РАЗДЕЛЫ")
    @allure.title("Негитивные сценарии: Проверка ввода значений в поле 'Название' Настройки")
    def test_path_input_name_negativ_settings_path(self, app, settings_path, close_modal):
        with allure.step("Проверка валидации поля"):
            app.PO_Zone_Path.input_data_name_path_negativ()

@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты ЗОНЫ/РАЗДЕЛЫ")
@allure.feature("Валидация полей ввода")
@pytest.mark.flaky(reruns=reruns)
class TestZonePathValidationOuts:

    @allure.story("ВЫХОДЫ")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Название' ВЫХОД № 1")
    def test_out_1_input_name_positiv(self, app, outs):
        with allure.step("Проверка валидации поля"):
            app.PO_Zone_Path.input_data_name_out_1_positv()

    @allure.story("ВЫХОДЫ")
    @allure.title("Негитивные сценарии: Проверка ввода значений в поле 'Название' ВЫХОД № 1")
    def test_out_1_input_name_negativ(self, app, outs):
        with allure.step("Проверка валидации поля"):
            app.PO_Zone_Path.input_data_name_out_1_negativ()

    @allure.story("ВЫХОДЫ")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Название' ВЫХОД № 2")
    def test_out_2_input_name_positiv(self, app, outs):
        with allure.step("Проверка валидации поля"):
            app.PO_Zone_Path.input_data_name_out_2_positv()

    @allure.story("ВЫХОДЫ")
    @allure.title("Негитивные сценарии: Проверка ввода значений в поле 'Название' ВЫХОД № 2")
    def test_out_2_input_name_negativ(self, app, outs):
        with allure.step("Проверка валидации поля"):
            app.PO_Zone_Path.input_data_name_out_2_negativ()

    @allure.story("ВЫХОДЫ")
    @allure.title(
        "Позитивные сценарии: Проверка ввода значений в поле 'Гистерзис' ВЫХОД № 1, Режим работы: Температурный")
    def test_out_1_input_temperature_hysteresis_positiv(self, app, outs):
        with allure.step("Выбор режима работы: Температурный"):
            app.PO_Zone_Path.select_temperature_mode_out_1()
        with allure.step("Проверка валидации поля"):
            app.PO_Zone_Path.input_hysteresis_positiv()

    @allure.story("ВЫХОДЫ")
    @allure.title(
        "Негитивные сценарии: Проверка ввода значений в поле 'Гистерзис' ВЫХОД № 1, Режим работы: Температурный")
    def test_out_1_input_temperature_hysteresis_negativ(self, app, outs):
        with allure.step("Выбор режима работы: Температурный"):
            app.PO_Zone_Path.select_temperature_mode_out_1()
        with allure.step("Проверка валидации поля"):
            app.PO_Zone_Path.input_hysteresis_negativ()

    @allure.story("ВЫХОДЫ")
    @allure.title(
        "Позитивные сценарии: Проверка ввода значений в поле 'Гистерзис' ВЫХОД № 2, Режим работы: Температурный")
    def test_out_2_input_temperature_hysteresis_positiv(self, app, outs):
        with allure.step("Выбор режима работы: Температурный"):
            app.PO_Zone_Path.select_temperature_mode_out_2()
        with allure.step("Проверка валидации поля"):
            app.PO_Zone_Path.input_hysteresis_positiv()

    @allure.story("ВЫХОДЫ")
    @allure.title(
        "Негитивные сценарии: Проверка ввода значений в поле 'Гистерзис' ВЫХОД № 2, Режим работы: Температурный")
    def test_out_2_input_temperature_hysteresis_negativ(self, app, outs):
        with allure.step("Выбор режима работы: Температурный"):
            app.PO_Zone_Path.select_temperature_mode_out_2()
        with allure.step("Проверка валидации поля"):
            app.PO_Zone_Path.input_hysteresis_negativ()

    @allure.story("ВЫХОДЫ")
    @allure.title(
        "Позитивные сценарии: Проверка ввода значений в поле 'Внутренний сигнал задания' ВЫХОД № 1, Режим работы: Температурный")
    def test_out_1_input_temperature_control_sensor_positiv(self, app, outs):
        with allure.step("Выбор режима работы: Температурный"):
            app.PO_Zone_Path.select_temperature_mode_out_1()
        with allure.step("Проверка валидации поля"):
            app.PO_Zone_Path.input_control_sensor_1_positiv()

    @allure.story("ВЫХОДЫ")
    @allure.title(
        "Негитивные сценарии: Проверка ввода значений в поле 'Внутренний сигнал задания' ВЫХОД № 1, Режим работы: Температурный")
    def test_out_1_input_temperature_control_sensor_negativ(self, app, outs):
        with allure.step("Выбор режима работы: Температурный"):
            app.PO_Zone_Path.select_temperature_mode_out_1()
        with allure.step("Проверка валидации поля"):
            app.PO_Zone_Path.input_control_sensor_1_negativ()

    @allure.story("ВЫХОДЫ")
    @allure.title(
        "Позитивные сценарии: Проверка ввода значений в поле 'Внутренний сигнал задания' ВЫХОД № 2, Режим работы: Температурный")
    def test_out_2_input_temperature_control_sensor_positiv(self, app, outs):
        with allure.step("Выбор режима работы: Температурный"):
            app.PO_Zone_Path.select_temperature_mode_out_2()
        with allure.step("Проверка валидации поля"):
            app.PO_Zone_Path.input_control_sensor_2_positiv()

    @allure.story("ВЫХОДЫ")
    @allure.title(
        "Негитивные сценарии: Проверка ввода значений в поле 'Внутренний сигнал задания' ВЫХОД № 2, Режим работы: Температурный")
    def test_out_2_input_temperature_control_sensor_negativ(self, app, outs):
        with allure.step("Выбор режима работы: Температурный"):
            app.PO_Zone_Path.select_temperature_mode_out_2()
        with allure.step("Проверка валидации поля"):
            app.PO_Zone_Path.input_control_sensor_2_negativ()
