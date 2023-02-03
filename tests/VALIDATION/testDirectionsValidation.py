# -*- coding: utf-8 -*-
import random

import allure
import pytest
from selenium.webdriver.common.by import By

reruns = 2

# directions_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']

directions_list = [f'{random.randint(1,16)}']


@pytest.fixture()
def close_modal(request, app):
    def fin():
        app.method.click((By.XPATH, '(//*[.=" Отменить "]//div)[last()]'))

    request.addfinalizer(fin)


@pytest.fixture
def destinations(app):
    with allure.step("Переход на страницу Напавления"):
        app.PO_Navigations.goToDirectionsPage()


@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты НАПРАВЛЕНИЯ")
@allure.feature("Валидация полей ввода")
@pytest.mark.flaky(reruns=reruns)
class Test01ValidationDestinationMainChanel:

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story(f"Название - Направление")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Название'")
    def test_input_data_name_positiv_destination(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_destination_name()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Название - Направление")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Название'")
    def test_input_data_name_negativ_destination(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_destination_name_negativ()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title("Основной канал Позитивные сценарии: Проверка ввода значений в поле 'код' - SMS пользователю")
    def test_input_data_sms_user_cod_positiv_destination(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('SMS пользователю')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_cod_posutiv_sms_user_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title("Основной канал Негативные сценарии: Проверка ввода значений в поле 'код' - SMS пользователю")
    def test_input_data_sms_user_cod_negativ_destination(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('SMS пользователю')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_cod_negativ_sms_user_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title(
        "Основной канал Позитивные сценарии: Проверка ввода значений в поле 'номер телефона' - SMS пользователю")
    def test_input_data_sms_user_tel_number_positiv_destination(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('SMS пользователю')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_tel_number_posutiv_sms_user_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title(
        "Основной канал Негативные сценарии: Проверка ввода значений в поле 'номер телефона' - SMS пользователю")
    def test_input_data_sms_user_tel_number_negativ_destination(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('SMS пользователю')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_tel_number_negativ_sms_user_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title(
        "Основной канал Позитивные сценарии: Проверка ввода значений в поле 'Таймаут при ошибке' - SMS пользователю")
    def test_input_data_sms_user_timeout_error_positiv_destination(self, app, destinations, close_modal,
                                                                   directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('SMS пользователю')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_timeout_error_posutiv_sms_user_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title(
        "Основной канал Негативные сценарии: Проверка ввода значений в поле 'Таймаут при ошибке' - SMS пользователю")
    def test_input_data_sms_user_timeout_error_negativ_destination(self, app, destinations, close_modal,
                                                                   directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('SMS пользователю')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_timeout_error_negativ_sms_user_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title(
        "Основной канал Позитивные сценарии: Проверка ввода значений в поле 'Интервал тестирования' - SMS пользователю")
    def test_input_data_sms_user_test_interval_positiv_destination(self, app, destinations, close_modal,
                                                                   directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('SMS пользователю')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Выбор: тестировать с интервалом"):
            app.PO_Directions.Test_at_intervals_main('С интервалом')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_test_interval_posutiv_sms_user_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title(
        "Основной канал Негативные сценарии: Проверка ввода значений в поле 'Интервал тестирования' - SMS пользователю")
    def test_input_data_sms_user_test_interval_negativ_destination(self, app, destinations, close_modal,
                                                                   directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('SMS пользователю')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Выбор: тестировать с интервалом"):
            app.PO_Directions.Test_at_intervals_main('С интервалом')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_test_interval_posutiv_sms_user_main()

@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты НАПРАВЛЕНИЯ")
@allure.feature("Валидация полей ввода")
@pytest.mark.flaky(reruns=reruns)
class Test02ValidationDestinationMainChanel:

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title("Основной канал Позитивные сценарии: Проверка ввода значений в поле 'код' - SMS Эгида")
    def test_input_data_sms_egida_cod_positiv_destination(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('SMS Эгида')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_cod_posutiv_sms_user_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title("Основной канал Негативные сценарии: Проверка ввода значений в поле 'код' - SMS Эгида")
    def test_input_data_sms_egida_cod_negativ_destination(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('SMS Эгида')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_cod_negativ_sms_user_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title(
        "Основной канал Позитивные сценарии: Проверка ввода значений в поле 'номер телефона' - SMS Эгида")
    def test_input_data_sms_egida_tel_number_positiv_destination(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('SMS Эгида')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_tel_number_posutiv_sms_user_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title(
        "Основной канал Негативные сценарии: Проверка ввода значений в поле 'номер телефона' - SMS Эгида")
    def test_input_data_sms_egida_tel_number_negativ_destination(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('SMS Эгида')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_tel_number_negativ_sms_user_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title(
        "Основной канал Позитивные сценарии: Проверка ввода значений в поле 'Таймаут при ошибке' - SMS Эгида")
    def test_input_data_sms_egida_timeout_error_positiv_destination(self, app, destinations, close_modal,
                                                                    directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('SMS Эгида')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_timeout_error_posutiv_sms_user_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title(
        "Основной канал Негативные сценарии: Проверка ввода значений в поле 'Таймаут при ошибке' - SMS Эгида")
    def test_input_data_sms_egida_timeout_error_negativ_destination(self, app, destinations, close_modal,
                                                                    directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('SMS Эгида')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_timeout_error_negativ_sms_user_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title(
        "Основной канал Позитивные сценарии: Проверка ввода значений в поле 'Интервал тестирования' - SMS Эгида")
    def test_input_data_sms_egida_test_interval_positiv_destination(self, app, destinations, close_modal,
                                                                    directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('SMS Эгида')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Выбор: тестировать с интервалом"):
            app.PO_Directions.Test_at_intervals_main_sms_egida('С интервалом')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_test_interval_posutiv_sms_user_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title(
        "Основной канал Негативные сценарии: Проверка ввода значений в поле 'Интервал тестирования' - SMS Эгида")
    def test_input_data_sms_egida_test_interval_negativ_destination(self, app, destinations, close_modal,
                                                                    directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('SMS Эгида')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Выбор: тестировать с интервалом"):
            app.PO_Directions.Test_at_intervals_main_sms_egida('С интервалом')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_test_interval_posutiv_sms_user_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title("Основной канал Позитивные сценарии: Проверка ввода значений в поле 'код' - Звонок")
    def test_input_data_call_cod_positiv_destination(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('Звонок')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_cod_posutiv_sms_user_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title("Основной канал Негативные сценарии: Проверка ввода значений в поле 'код' - Звонок")
    def test_input_data_call_cod_negativ_destination(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('Звонок')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_cod_negativ_sms_user_main()

@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты НАПРАВЛЕНИЯ")
@allure.feature("Валидация полей ввода")
@pytest.mark.flaky(reruns=reruns)
class Test03ValidationDestinationMainChanel:

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title(
        "Основной канал Позитивные сценарии: Проверка ввода значений в поле 'номер телефона' - Звонок")
    def test_input_data_call_tel_number_positiv_destination(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('Звонок')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_tel_number_posutiv_sms_user_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title(
        "Основной канал Негативные сценарии: Проверка ввода значений в поле 'номер телефона' - Звонок")
    def test_input_data_call_tel_number_negativ_destination(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('Звонок')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_tel_number_negativ_sms_user_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title(
        "Основной канал Позитивные сценарии: Проверка ввода значений в поле 'Количество повторов' - Звонок")
    def test_input_data_call_count_reset_positiv_destination(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('Звонок')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_count_reset_positiv_call_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title(
        "Основной канал Негативные сценарии: Проверка ввода значений в поле 'Количество повторов' - Звонок")
    def test_input_data_call_count_reset_negativ_destination(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('Звонок')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_count_reset_negativ_call_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title(
        "Основной канал Позитивные сценарии: Проверка ввода значений в поле 'Таймаут при ошибке' - Звонок")
    def test_input_data_call_timeout_error_positiv_destination(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('Звонок')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_timeout_error_posutiv_sms_user_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title(
        "Основной канал Негативные сценарии: Проверка ввода значений в поле 'Таймаут при ошибке' - Звонок")
    def test_input_data_call_timeout_error_negativ_destination(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('Звонок')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_timeout_error_negativ_sms_user_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title(
        "Основной канал Позитивные сценарии: Проверка ввода значений в поле 'Интервал тестирования' - Звонок")
    def test_input_data_call_test_interval_positiv_destination(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('Звонок')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Выбор: тестировать с интервалом"):
            app.PO_Directions.Test_at_intervals_main_sms_egida('С интервалом')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_test_interval_posutiv_sms_user_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title(
        "Основной канал Негативные сценарии: Проверка ввода значений в поле 'Интервал тестирования' - Звонок")
    def test_input_data_call_test_interval_negativ_destination(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('Звонок')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Выбор: тестировать с интервалом"):
            app.PO_Directions.Test_at_intervals_main_sms_egida('С интервалом')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_test_interval_posutiv_sms_user_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title("Основной канал Позитивные сценарии: Проверка ввода значений в поле 'Адрес' - DC09")
    def test_input_data_address_DC09_cod_positiv_type_main_destination(self, app, destinations, close_modal,
                                                                       directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('DC09')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_address_posutiv_dc09_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title("Основной канал Негативные сценарии: Проверка ввода значений в поле 'Адрес' - DC09")
    def test_input_data_address_DC09_cod_negativ_type_main_destination(self, app, destinations, close_modal,
                                                                       directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('DC09')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_address_negativ_dc09_main()

@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты НАПРАВЛЕНИЯ")
@allure.feature("Валидация полей ввода")
@pytest.mark.flaky(reruns=reruns)
class Test04ValidationDestinationMainChanel:

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title("Основной канал Позитивные сценарии: Проверка ввода значений в поле 'Порт' - DC09")
    def test_input_data_port_DC09_cod_positiv_type_main_destination(self, app, destinations, close_modal,
                                                                    directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('DC09')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_port_posutiv_dc09_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title("Основной канал Негативные сценарии: Проверка ввода значений в поле 'Порт' - DC09")
    def test_input_data_port_DC09_cod_negativ_type_main_destination(self, app, destinations, close_modal,
                                                                    directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('DC09')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_port_negativ_dc09_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title(
        "Основной канал Позитивные сценарии: Проверка ввода значений в поле 'Таймаут подтверждения, сек' - DC09")
    def test_input_data_confirmation_timeout_DC09_cod_positiv_type_main_destination(self, app, destinations,
                                                                                    close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('DC09')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_confirmation_timeout_posutiv_dc09_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title(
        "Основной канал Негативные сценарии: Проверка ввода значений в поле 'Таймаут подтверждения, сек' - DC09")
    def test_input_data_confirmation_timeout_DC09_cod_negativ_type_main_destination(self, app, destinations,
                                                                                    close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('DC09')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_confirmation_timeout_negativ_dc09_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title("Основной канал Позитивные сценарии: Проверка ввода значений в поле 'Количество повторов' - DC09")
    def test_input_data_number_of_repetitions_DC09_cod_positiv_type_main_destination(self, app, destinations,
                                                                                     close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('DC09')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_number_of_repetitions_posutiv_dc09_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title("Основной канал Негативные сценарии: Проверка ввода значений в поле 'Количество повторов' - DC09")
    def test_input_data_number_of_repetitions_DC09_cod_negativ_type_main_destination(self, app, destinations,
                                                                                     close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('DC09')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_number_of_repetitions_negativ_dc09_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title("Основной канал Позитивные сценарии: Проверка ввода значений в поле 'Ключ шифрования' - DC09")
    def test_input_data_encryption_key_DC09_cod_positiv_type_main_destination(self, app, destinations, close_modal,
                                                                              directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('DC09')
        with allure.step("Включения Шифрование"):
            app.PO_Directions.enableEncryption_main()
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_encryption_key_posutiv_dc09_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title("Основной канал Негативные сценарии: Проверка ввода значений в поле 'Ключ шифрования' - DC09")
    def test_input_data_encryption_key_DC09_cod_negativ_type_main_destination(self, app, destinations, close_modal,
                                                                              directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('DC09')
        with allure.step("Включения Шифрование"):
            app.PO_Directions.enableEncryption_main()
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_encryption_key_negativ_dc09_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title(
        "Основной канал Позитивные сценарии: Проверка ввода значений в поле 'Таймаут при ошибке' - DC09")
    def test_input_data_DC09_timeout_error_positiv_destination(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('DC09')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_timeout_error_posutiv_sms_user_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title(
        "Основной канал Негативные сценарии: Проверка ввода значений в поле 'Таймаут при ошибке' - DC09")
    def test_input_data_DC09_timeout_error_negativ_destination(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('DC09')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_timeout_error_negativ_sms_user_main()


    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title(
        "Основной канал Позитивные сценарии: Проверка ввода значений в поле 'Интервал тестирования' - DC09")
    def test_input_data_DC09_test_interval_positiv_destination(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('DC09')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Выбор: тестировать с интервалом"):
            app.PO_Directions.Test_at_intervals_main_dc09('С интервалом')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_test_interval_posutiv_sms_user_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title(
        "Основной канал Негативные сценарии: Проверка ввода значений в поле 'Интервал тестирования' - DC09")
    def test_input_data_DC09_test_interval_negativ_destination(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('DC09')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Выбор: тестировать с интервалом"):
            app.PO_Directions.Test_at_intervals_main_dc09('С интервалом')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_test_interval_posutiv_sms_user_main()


@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты НАПРАВЛЕНИЯ")
@allure.feature("Валидация полей ввода")
@pytest.mark.flaky(reruns=reruns)
class Test01ValidationDestinationRezerv1Chanel:

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title("Резервный канал 1 Позитивные сценарии: Проверка ввода значений в поле 'код' - SMS пользователю")
    def test_input_data_reserv_1_sms_user_cod_positiv_destination(self, app, destinations, close_modal,
                                                                  directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS пользователю')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('SMS пользователю')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_cod_posutiv_sms_user_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title("Резервный канал 1 Негативные сценарии: Проверка ввода значений в поле 'код' - SMS пользователю")
    def test_input_data_reserv_1_sms_user_cod_negativ_destination(self, app, destinations, close_modal,
                                                                  directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS пользователю')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openType_main('SMS пользователю')
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('SMS пользователю')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_cod_negativ_sms_user_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title(
        "Резервный канал 1 Позитивные сценарии: Проверка ввода значений в поле 'номер телефона' - SMS пользователю")
    def test_input_data_reserv_1_sms_user_tel_number_positiv_destination(self, app, destinations, close_modal,
                                                                         directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS пользователю')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openType_main('SMS пользователю')
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('SMS пользователю')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_tel_number_posutiv_sms_user_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title(
        "Резервный канал 1 Негативные сценарии: Проверка ввода значений в поле 'номер телефона' - SMS пользователю")
    def test_input_data_reserv_1_sms_user_tel_number_negativ_destination(self, app, destinations, close_modal,
                                                                         directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS пользователю')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openType_main('SMS пользователю')
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('SMS пользователю')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_tel_number_negativ_sms_user_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title(
        "Резервный канал 1 Позитивные сценарии: Проверка ввода значений в поле 'Таймаут при ошибке' - SMS пользователю")
    def test_input_data_reserv_1_sms_user_timeout_error_positiv_destination(self, app, destinations, close_modal,
                                                                            directions: str):
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
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_timeout_error_posutiv_sms_user_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title(
        "Резервный канал 1 Негативные сценарии: Проверка ввода значений в поле 'Таймаут при ошибке' - SMS пользователю")
    def test_input_data_reserv_1_sms_user_timeout_error_negativ_destination(self, app, destinations, close_modal,
                                                                            directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS пользователю')
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openType_main('SMS пользователю')
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('SMS пользователю')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_timeout_error_negativ_sms_user_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title(
        "Резервный канал 1 Позитивные сценарии: Проверка ввода значений в поле 'Интервал тестирования' - SMS пользователю")
    def test_input_data_reserv_1_sms_user_test_interval_positiv_destination(self, app, destinations, close_modal,
                                                                            directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS пользователю')
            app.PO_Directions.enableChannelTesting_main()
            app.PO_Directions.Test_at_intervals_main('С интервалом')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openType_main('SMS пользователю')
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('SMS пользователю')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Выбор: тестировать с интервалом"):
            app.PO_Directions.Test_at_intervals_rezerv_1('С интервалом')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_test_interval_posutiv_sms_user_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title(
        "Резервный канал 1 Негативные сценарии: Проверка ввода значений в поле 'Интервал тестирования' - SMS пользователю")
    def test_input_data_reserv_1_sms_user_test_interval_negativ_destination(self, app, destinations, close_modal,
                                                                            directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS пользователю')
            app.PO_Directions.enableChannelTesting_main()
            app.PO_Directions.Test_at_intervals_main('С интервалом')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('SMS пользователю')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Выбор: тестировать с интервалом"):
            app.PO_Directions.Test_at_intervals_rezerv_1('С интервалом')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_test_interval_posutiv_sms_user_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title("Резервный канал 1 Позитивные сценарии: Проверка ввода значений в поле 'код' - SMS Эгида")
    def test_input_data_reserv_1_sms_egida_cod_positiv_destination(self, app, destinations, close_modal,
                                                                   directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS Эгида')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('SMS Эгида')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_cod_posutiv_sms_user_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title("Резервный канал 1 Негативные сценарии: Проверка ввода значений в поле 'код' - SMS Эгида")
    def test_input_data_reserv_1_sms_egida_cod_negativ_destination(self, app, destinations, close_modal,
                                                                   directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS Эгида')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('SMS Эгида')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_cod_negativ_sms_user_rezerv_1()

@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты НАПРАВЛЕНИЯ")
@allure.feature("Валидация полей ввода")
@pytest.mark.flaky(reruns=reruns)
class Test02ValidationDestinationRezerv1Chanel:

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title(
        "Резервный канал 1 Позитивные сценарии: Проверка ввода значений в поле 'номер телефона' - SMS Эгида")
    def test_input_data_reserv_1_sms_egida_tel_number_positiv_destination(self, app, destinations, close_modal,
                                                                          directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS Эгида')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('SMS Эгида')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_tel_number_posutiv_sms_user_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title(
        "Резервный канал 1 Негативные сценарии: Проверка ввода значений в поле 'номер телефона' - SMS Эгида")
    def test_input_data_reserv_1_sms_egida_tel_number_negativ_destination(self, app, destinations, close_modal,
                                                                          directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS Эгида')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('SMS Эгида')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_tel_number_negativ_sms_user_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title(
        "Резервный канал 1 Позитивные сценарии: Проверка ввода значений в поле 'Таймаут при ошибке' - SMS Эгида")
    def test_input_data_reserv_1_sms_egida_timeout_error_positiv_destination(self, app, destinations, close_modal,
                                                                             directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS Эгида')
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('SMS Эгида')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_timeout_error_posutiv_sms_user_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title(
        "Резервный канал 1 Негативные сценарии: Проверка ввода значений в поле 'Таймаут при ошибке' - SMS Эгида")
    def test_input_data_reserv_1_sms_egida_timeout_error_negativ_destination(self, app, destinations, close_modal,
                                                                             directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS Эгида')
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('SMS Эгида')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_timeout_error_negativ_sms_user_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title(
        "Резервный канал 1 Позитивные сценарии: Проверка ввода значений в поле 'Интервал тестирования' - SMS Эгида")
    def test_input_data_reserv_1_sms_egida_test_interval_positiv_destination(self, app, destinations, close_modal,
                                                                             directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS Эгида')
            app.PO_Directions.enableChannelTesting_main()
            app.PO_Directions.Test_at_intervals_main_sms_egida('С интервалом')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('SMS Эгида')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Выбор: тестировать с интервалом"):
            app.PO_Directions.Test_at_intervals_sms_egida_reserv_1('С интервалом')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_test_interval_posutiv_sms_user_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title(
        "Резервный канал 1 Негативные сценарии: Проверка ввода значений в поле 'Интервал тестирования' - SMS Эгида")
    def test_input_data_reserv_1_sms_egida_test_interval_negativ_destination(self, app, destinations, close_modal,
                                                                             directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS Эгида')
            app.PO_Directions.enableChannelTesting_main()
            app.PO_Directions.Test_at_intervals_main_sms_egida('С интервалом')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('SMS Эгида')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Выбор: тестировать с интервалом"):
            app.PO_Directions.Test_at_intervals_sms_egida_reserv_1('С интервалом')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_test_interval_posutiv_sms_user_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title("Резервный канал 1 Позитивные сценарии: Проверка ввода значений в поле 'код' - Звонок")
    def test_input_data_reserv_1_call_cod_positiv_destination(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('Звонок')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('Звонок')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_cod_posutiv_sms_user_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title("Резервный канал 1 Негативные сценарии: Проверка ввода значений в поле 'код' - Звонок")
    def test_input_data_reserv_1_call_cod_negativ_destination(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('Звонок')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('Звонок')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_cod_negativ_sms_user_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title(
        "Резервный канал 1 Позитивные сценарии: Проверка ввода значений в поле 'номер телефона' - Звонок")
    def test_input_data_reserv_1_call_tel_number_positiv_destination(self, app, destinations, close_modal,
                                                                     directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('Звонок')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('Звонок')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_tel_number_posutiv_sms_user_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title(
        "Резервный канал 1 Негативные сценарии: Проверка ввода значений в поле 'номер телефона' - Звонок")
    def test_input_data_reserv_1_call_tel_number_negativ_destination(self, app, destinations, close_modal,
                                                                     directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('Звонок')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('Звонок')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_tel_number_negativ_sms_user_rezerv_1()

@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты НАПРАВЛЕНИЯ")
@allure.feature("Валидация полей ввода")
@pytest.mark.flaky(reruns=reruns)
class Test03ValidationDestinationRezerv1Chanel:

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title(
        "Резервный канал 1 Позитивные сценарии: Проверка ввода значений в поле 'Количество повторов' - Звонок")
    def test_input_data_reserv_1_call_count_reset_positiv_destination(self, app, destinations, close_modal,
                                                                      directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('Звонок')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('Звонок')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_count_reset_positiv_call_reserv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title(
        "Резервный канал 1 Негативные сценарии: Проверка ввода значений в поле 'Количество повторов' - Звонок")
    def test_input_data_reserv_1_call_count_reset_negativ_destination(self, app, destinations, close_modal,
                                                                      directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('Звонок')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('Звонок')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_count_reset_negativ_call_reserv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title(
        "Резервный канал 1 Позитивные сценарии: Проверка ввода значений в поле 'Таймаут при ошибке' - Звонок")
    def test_input_data_reserv_1_call_timeout_error_positiv_destination(self, app, destinations, close_modal,
                                                                        directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('Звонок')
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('Звонок')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_timeout_error_posutiv_sms_user_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title(
        "Резервный канал 1 Негативные сценарии: Проверка ввода значений в поле 'Таймаут при ошибке' - Звонок")
    def test_input_data_reserv_1_call_timeout_error_negativ_destination(self, app, destinations, close_modal,
                                                                        directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('Звонок')
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('Звонок')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_timeout_error_negativ_sms_user_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title(
        "Резервный канал 1 Позитивные сценарии: Проверка ввода значений в поле 'Интервал тестирования' - Звонок")
    def test_input_data_reserv_1_call_test_interval_positiv_destination(self, app, destinations, close_modal,
                                                                        directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('Звонок')
            app.PO_Directions.enableChannelTesting_main()
            app.PO_Directions.Test_at_intervals_main_sms_egida('С интервалом')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('Звонок')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Выбор: тестировать с интервалом"):
            app.PO_Directions.Test_at_intervals_sms_egida_reserv_1('С интервалом')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_test_interval_posutiv_sms_user_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title(
        "Резервный канал 1 Негативные сценарии: Проверка ввода значений в поле 'Интервал тестирования' - Звонок")
    def test_input_data_reserv_1_call_test_interval_negativ_destination(self, app, destinations, close_modal,
                                                                        directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('Звонок')
            app.PO_Directions.enableChannelTesting_main()
            app.PO_Directions.Test_at_intervals_main_sms_egida('С интервалом')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('Звонок')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Выбор: тестировать с интервалом"):
            app.PO_Directions.Test_at_intervals_sms_egida_reserv_1('С интервалом')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_test_interval_posutiv_sms_user_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title("Резервный канал 1 Позитивные сценарии: Проверка ввода значений в поле 'Адрес' - DC09")
    def test_input_data_reserv_1_address_DC09_cod_positiv_type_main_destination(self, app, destinations, close_modal,
                                                                                directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('DC09')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('DC09')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_address_posutiv_dc09_reserv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title("Резервный канал 1 Негативные сценарии: Проверка ввода значений в поле 'Адрес' - DC09")
    def test_input_data_reserv_1_address_DC09_cod_negativ_type_main_destination(self, app, destinations, close_modal,
                                                                                directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('DC09')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('DC09')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_address_negativ_dc09_reserv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title("Резервный канал 1 Позитивные сценарии: Проверка ввода значений в поле 'Порт' - DC09")
    def test_input_data_reserv_1_port_DC09_cod_positiv_type_main_destination(self, app, destinations, close_modal,
                                                                             directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('DC09')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('DC09')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_port_posutiv_dc09_reserv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title("Резервный канал 1 Негативные сценарии: Проверка ввода значений в поле 'Порт' - DC09")
    def test_input_data_reserv_1_port_DC09_cod_negativ_type_main_destination(self, app, destinations, close_modal,
                                                                             directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('DC09')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('DC09')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_port_negativ_dc09_reserv_1()

@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты НАПРАВЛЕНИЯ")
@allure.feature("Валидация полей ввода")
@pytest.mark.flaky(reruns=reruns)
class Test04ValidationDestinationRezerv1Chanel:

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title(
        "Резервный канал 1 Позитивные сценарии: Проверка ввода значений в поле 'Таймаут подтверждения, сек' - DC09")
    def test_input_data_reserv_1_confirmation_timeout_DC09_cod_positiv_type_main_destination(self, app, destinations,
                                                                                             close_modal,
                                                                                             directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('DC09')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('DC09')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_confirmation_timeout_posutiv_dc09_reserv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title(
        "Резервный канал 1 Негативные сценарии: Проверка ввода значений в поле 'Таймаут подтверждения, сек' - DC09")
    def test_input_data_reserv_1_confirmation_timeout_DC09_cod_negativ_type_main_destination(self, app, destinations,
                                                                                             close_modal,
                                                                                             directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('DC09')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('DC09')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_confirmation_timeout_negativ_dc09_reserv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title("Резервный канал 1 Позитивные сценарии: Проверка ввода значений в поле 'Количество повторов' - DC09")
    def test_input_data_reserv_1_number_of_repetitions_DC09_cod_positiv_type_main_destination(self, app, destinations,
                                                                                              close_modal,
                                                                                              directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('DC09')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('DC09')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_number_of_repetitions_posutiv_dc09_reserv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title("Резервный канал 1 Негативные сценарии: Проверка ввода значений в поле 'Количество повторов' - DC09")
    def test_input_data_reserv_1_number_of_repetitions_DC09_cod_negativ_type_main_destination(self, app, destinations,
                                                                                              close_modal,
                                                                                              directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('DC09')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('DC09')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_number_of_repetitions_negativ_dc09_reserv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title("Резервный канал 1 Позитивные сценарии: Проверка ввода значений в поле 'Ключ шифрования' - DC09")
    def test_input_data_reserv_1_encryption_key_DC09_cod_positiv_type_main_destination(self, app, destinations,
                                                                                       close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('DC09')
        with allure.step("Включения Шифрование"):
            app.PO_Directions.enableEncryption_main()
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('DC09')
        with allure.step("Включения Шифрование"):
            app.PO_Directions.enableEncryption_rezerv_1()
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_encryption_key_posutiv_dc09_reserv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title("Резервный канал 1 Негативные сценарии: Проверка ввода значений в поле 'Ключ шифрования' - DC09")
    def test_input_data_reserv_1_encryption_key_DC09_cod_negativ_type_main_destination(self, app, destinations,
                                                                                       close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('DC09')
        with allure.step("Включения Шифрование"):
            app.PO_Directions.enableEncryption_main()
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('DC09')
        with allure.step("Включения Шифрование"):
            app.PO_Directions.enableEncryption_rezerv_1()
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_encryption_key_negativ_dc09_reserv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title(
        "Резервный канал 1 Позитивные сценарии: Проверка ввода значений в поле 'Таймаут при ошибке' - DC09")
    def test_input_data_reserv_1_DC09_timeout_error_positiv_destination(self, app, destinations, close_modal,
                                                                        directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('DC09')
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('DC09')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_timeout_error_posutiv_sms_user_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title(
        "Резервный канал 1 Негативные сценарии: Проверка ввода значений в поле 'Таймаут при ошибке' - DC09")
    def test_input_data_reserv_1_DC09_timeout_error_negativ_destination(self, app, destinations, close_modal,
                                                                        directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('DC09')
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('DC09')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_timeout_error_negativ_sms_user_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title(
        "Резервный канал 1 Позитивные сценарии: Проверка ввода значений в поле 'Интервал тестирования' - DC09")
    def test_input_data_reserv_1_DC09_test_interval_positiv_destination(self, app, destinations, close_modal,
                                                                        directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('DC09')
            app.PO_Directions.enableChannelTesting_main()
            app.PO_Directions.Test_at_intervals_main_dc09('С интервалом')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('DC09')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Выбор: тестировать с интервалом"):
            app.PO_Directions.Test_at_intervals_reserv_1_dc09('С интервалом')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_test_interval_posutiv_sms_user_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title(
        "Резервный канал 1 Негативные сценарии: Проверка ввода значений в поле 'Интервал тестирования' - DC09")
    def test_input_data_reserv_1_DC09_test_interval_negativ_destination(self, app, destinations, close_modal,
                                                                        directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('DC09')
            app.PO_Directions.enableChannelTesting_main()
            app.PO_Directions.Test_at_intervals_main_dc09('С интервалом')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('DC09')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Выбор: тестировать с интервалом"):
            app.PO_Directions.Test_at_intervals_reserv_1_dc09('С интервалом')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_test_interval_posutiv_sms_user_rezerv_1()


@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты НАПРАВЛЕНИЯ")
@allure.feature("Валидация полей ввода")
@pytest.mark.flaky(reruns=reruns)
class Test01ValidationDestinationRezerv2Chanel:

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title("Резервный канал 2 Позитивные сценарии: Проверка ввода значений в поле 'код' - SMS пользователю")
    def test_input_data_reserv_2_sms_user_cod_positiv_destination(self, app, destinations, close_modal,
                                                                  directions: str):
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
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_cod_posutiv_sms_user_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title("Резервный канал 2 Негативные сценарии: Проверка ввода значений в поле 'код' - SMS пользователю")
    def test_input_data_reserv_2_sms_user_cod_negativ_destination(self, app, destinations, close_modal,
                                                                  directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS пользователю')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('SMS пользователю')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openType_main('SMS пользователю')
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('SMS пользователю')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_cod_negativ_sms_user_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title(
        "Резервный канал 2 Позитивные сценарии: Проверка ввода значений в поле 'номер телефона' - SMS пользователю")
    def test_input_data_reserv_2_sms_user_tel_number_positiv_destination(self, app, destinations, close_modal,
                                                                         directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS пользователю')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('SMS пользователю')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openType_main('SMS пользователю')
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('SMS пользователю')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_tel_number_posutiv_sms_user_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title(
        "Резервный канал 2 Негативные сценарии: Проверка ввода значений в поле 'номер телефона' - SMS пользователю")
    def test_input_data_reserv_2_sms_user_tel_number_negativ_destination(self, app, destinations, close_modal,
                                                                         directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS пользователю')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('SMS пользователю')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openType_main('SMS пользователю')
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('SMS пользователю')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_tel_number_negativ_sms_user_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title(
        "Резервный канал 2 Позитивные сценарии: Проверка ввода значений в поле 'Таймаут при ошибке' - SMS пользователю")
    def test_input_data_reserv_2_sms_user_timeout_error_positiv_destination(self, app, destinations, close_modal,
                                                                            directions: str):
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
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_rezerv_2()
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_timeout_error_posutiv_sms_user_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title(
        "Резервный канал 2 Негативные сценарии: Проверка ввода значений в поле 'Таймаут при ошибке' - SMS пользователю")
    def test_input_data_reserv_2_sms_user_timeout_error_negativ_destination(self, app, destinations, close_modal,
                                                                            directions: str):
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
            app.PO_Directions.openType_main('SMS пользователю')
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('SMS пользователю')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_rezerv_2()
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_timeout_error_negativ_sms_user_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title(
        "Резервный канал 2 Позитивные сценарии: Проверка ввода значений в поле 'Интервал тестирования' - SMS пользователю")
    def test_input_data_reserv_2_sms_user_test_interval_positiv_destination(self, app, destinations, close_modal,
                                                                            directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS пользователю')
            app.PO_Directions.enableChannelTesting_main()
            app.PO_Directions.Test_at_intervals_main('С интервалом')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('SMS пользователю')
            app.PO_Directions.enableChannelTesting_rezerv_1()
            app.PO_Directions.Test_at_intervals_rezerv_1('С интервалом')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openType_main('SMS пользователю')
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('SMS пользователю')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_rezerv_2()
        with allure.step("Выбор: тестировать с интервалом"):
            app.PO_Directions.Test_at_intervals_rezerv_2('С интервалом')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_test_interval_posutiv_sms_user_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title(
        "Резервный канал 2 Негативные сценарии: Проверка ввода значений в поле 'Интервал тестирования' - SMS пользователю")
    def test_input_data_reserv_2_sms_user_test_interval_negativ_destination(self, app, destinations, close_modal,
                                                                            directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS пользователю')
            app.PO_Directions.enableChannelTesting_main()
            app.PO_Directions.Test_at_intervals_main('С интервалом')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('SMS пользователю')
            app.PO_Directions.enableChannelTesting_rezerv_1()
            app.PO_Directions.Test_at_intervals_rezerv_1('С интервалом')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('SMS пользователю')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_rezerv_2()
        with allure.step("Выбор: тестировать с интервалом"):
            app.PO_Directions.Test_at_intervals_rezerv_2('С интервалом')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_test_interval_posutiv_sms_user_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title("Резервный канал 2 Позитивные сценарии: Проверка ввода значений в поле 'код' - SMS Эгида")
    def test_input_data_reserv_2_sms_egida_cod_positiv_destination(self, app, destinations, close_modal,
                                                                   directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS Эгида')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('SMS Эгида')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('SMS Эгида')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_cod_posutiv_sms_user_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title("Резервный канал 2 Негативные сценарии: Проверка ввода значений в поле 'код' - SMS Эгида")
    def test_input_data_reserv_2_sms_egida_cod_negativ_destination(self, app, destinations, close_modal,
                                                                   directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS Эгида')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('SMS Эгида')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('SMS Эгида')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_cod_negativ_sms_user_rezerv_2()

@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты НАПРАВЛЕНИЯ")
@allure.feature("Валидация полей ввода")
@pytest.mark.flaky(reruns=reruns)
class Test02ValidationDestinationRezerv2Chanel:

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title(
        "Резервный канал 2 Позитивные сценарии: Проверка ввода значений в поле 'номер телефона' - SMS Эгида")
    def test_input_data_reserv_2_sms_egida_tel_number_positiv_destination(self, app, destinations, close_modal,
                                                                          directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS Эгида')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('SMS Эгида')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('SMS Эгида')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_tel_number_posutiv_sms_user_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title(
        "Резервный канал 2 Негативные сценарии: Проверка ввода значений в поле 'номер телефона' - SMS Эгида")
    def test_input_data_reserv_2_sms_egida_tel_number_negativ_destination(self, app, destinations, close_modal,
                                                                          directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS Эгида')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('SMS Эгида')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('SMS Эгида')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_tel_number_negativ_sms_user_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title(
        "Резервный канал 2 Позитивные сценарии: Проверка ввода значений в поле 'Таймаут при ошибке' - SMS Эгида")
    def test_input_data_reserv_2_sms_egida_timeout_error_positiv_destination(self, app, destinations, close_modal,
                                                                             directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS Эгида')
            app.PO_Directions.enableChannelTesting_main()
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('SMS Эгида')
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('SMS Эгида')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_rezerv_2()
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_timeout_error_posutiv_sms_user_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title(
        "Резервный канал 2 Негативные сценарии: Проверка ввода значений в поле 'Таймаут при ошибке' - SMS Эгида")
    def test_input_data_reserv_2_sms_egida_timeout_error_negativ_destination(self, app, destinations, close_modal,
                                                                             directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS Эгида')
            app.PO_Directions.enableChannelTesting_main()
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('SMS Эгида')
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('SMS Эгида')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_rezerv_2()
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_timeout_error_negativ_sms_user_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title(
        "Резервный канал 2 Позитивные сценарии: Проверка ввода значений в поле 'Интервал тестирования' - SMS Эгида")
    def test_input_data_reserv_2_sms_egida_test_interval_positiv_destination(self, app, destinations, close_modal,
                                                                             directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS Эгида')
            app.PO_Directions.enableChannelTesting_main()
            app.PO_Directions.Test_at_intervals_main_sms_egida('С интервалом')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('SMS Эгида')
            app.PO_Directions.enableChannelTesting_rezerv_1()
            app.PO_Directions.Test_at_intervals_sms_egida_reserv_1('С интервалом')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('SMS Эгида')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_rezerv_2()
        with allure.step("Выбор: тестировать с интервалом"):
            app.PO_Directions.Test_at_intervals_sms_egida_reserv_2('С интервалом')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_test_interval_posutiv_sms_user_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title(
        "Резервный канал 2 Негативные сценарии: Проверка ввода значений в поле 'Интервал тестирования' - SMS Эгида")
    def test_input_data_reserv_2_sms_egida_test_interval_negativ_destination(self, app, destinations, close_modal,
                                                                             directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS Эгида')
            app.PO_Directions.enableChannelTesting_main()
            app.PO_Directions.Test_at_intervals_main_sms_egida('С интервалом')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('SMS Эгида')
            app.PO_Directions.enableChannelTesting_rezerv_1()
            app.PO_Directions.Test_at_intervals_sms_egida_reserv_1('С интервалом')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('SMS Эгида')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_rezerv_2()
        with allure.step("Выбор: тестировать с интервалом"):
            app.PO_Directions.Test_at_intervals_sms_egida_reserv_2('С интервалом')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_test_interval_posutiv_sms_user_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title("Резервный канал 2 Позитивные сценарии: Проверка ввода значений в поле 'код' - Звонок")
    def test_input_data_reserv_2_call_cod_positiv_destination(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('Звонок')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('Звонок')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('Звонок')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_cod_posutiv_sms_user_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title("Резервный канал 2 Негативные сценарии: Проверка ввода значений в поле 'код' - Звонок")
    def test_input_data_reserv_2_call_cod_negativ_destination(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('Звонок')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('Звонок')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('Звонок')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_cod_negativ_sms_user_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title(
        "Резервный канал 2 Позитивные сценарии: Проверка ввода значений в поле 'номер телефона' - Звонок")
    def test_input_data_reserv_2_call_tel_number_positiv_destination(self, app, destinations, close_modal,
                                                                     directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('Звонок')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('Звонок')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('Звонок')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_tel_number_posutiv_sms_user_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title(
        "Резервный канал 2 Негативные сценарии: Проверка ввода значений в поле 'номер телефона' - Звонок")
    def test_input_data_reserv_2_call_tel_number_negativ_destination(self, app, destinations, close_modal,
                                                                     directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('Звонок')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('Звонок')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('Звонок')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_tel_number_negativ_sms_user_rezerv_2()

@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты НАПРАВЛЕНИЯ")
@allure.feature("Валидация полей ввода")
@pytest.mark.flaky(reruns=reruns)
class Test03ValidationDestinationRezerv2Chanel:

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title(
        "Резервный канал 2 Позитивные сценарии: Проверка ввода значений в поле 'Количество повторов' - Звонок")
    def test_input_data_reserv_2_call_count_reset_positiv_destination(self, app, destinations, close_modal,
                                                                      directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('Звонок')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('Звонок')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('Звонок')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_count_reset_positiv_call_reserv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title(
        "Резервный канал 2 Негативные сценарии: Проверка ввода значений в поле 'Количество повторов' - Звонок")
    def test_input_data_reserv_2_call_count_reset_negativ_destination(self, app, destinations, close_modal,
                                                                      directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('Звонок')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('Звонок')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('Звонок')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_count_reset_negativ_call_reserv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title(
        "Резервный канал 2 Позитивные сценарии: Проверка ввода значений в поле 'Таймаут при ошибке' - Звонок")
    def test_input_data_reserv_2_call_timeout_error_positiv_destination(self, app, destinations, close_modal,
                                                                        directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('Звонок')
            app.PO_Directions.enableChannelTesting_main()
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('Звонок')
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('Звонок')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_rezerv_2()
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_timeout_error_posutiv_sms_user_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title(
        "Резервный канал 2 Негативные сценарии: Проверка ввода значений в поле 'Таймаут при ошибке' - Звонок")
    def test_input_data_reserv_2_call_timeout_error_negativ_destination(self, app, destinations, close_modal,
                                                                        directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('Звонок')
            app.PO_Directions.enableChannelTesting_main()
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('Звонок')
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('Звонок')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_rezerv_2()
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_timeout_error_negativ_sms_user_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title(
        "Резервный канал 2 Позитивные сценарии: Проверка ввода значений в поле 'Интервал тестирования' - Звонок")
    def test_input_data_reserv_2_call_test_interval_positiv_destination(self, app, destinations, close_modal,
                                                                        directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('Звонок')
            app.PO_Directions.enableChannelTesting_main()
            app.PO_Directions.Test_at_intervals_main_sms_egida('С интервалом')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('Звонок')
            app.PO_Directions.enableChannelTesting_rezerv_1()
            app.PO_Directions.Test_at_intervals_sms_egida_reserv_1('С интервалом')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('Звонок')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_rezerv_2()
        with allure.step("Выбор: тестировать с интервалом"):
            app.PO_Directions.Test_at_intervals_sms_egida_reserv_2('С интервалом')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_test_interval_posutiv_sms_user_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title(
        "Резервный канал 2 Негативные сценарии: Проверка ввода значений в поле 'Интервал тестирования' - Звонок")
    def test_input_data_reserv_2_call_test_interval_negativ_destination(self, app, destinations, close_modal,
                                                                        directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('Звонок')
            app.PO_Directions.enableChannelTesting_main()
            app.PO_Directions.Test_at_intervals_main_sms_egida('С интервалом')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('Звонок')
            app.PO_Directions.enableChannelTesting_rezerv_1()
            app.PO_Directions.Test_at_intervals_sms_egida_reserv_1('С интервалом')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('Звонок')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_rezerv_2()
        with allure.step("Выбор: тестировать с интервалом"):
            app.PO_Directions.Test_at_intervals_sms_egida_reserv_2('С интервалом')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_test_interval_posutiv_sms_user_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title("Резервный канал 2 Позитивные сценарии: Проверка ввода значений в поле 'Адрес' - DC09")
    def test_input_data_reserv_2_address_DC09_cod_positiv_type_main_destination(self, app, destinations, close_modal,
                                                                                directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('DC09')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('DC09')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('DC09')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_address_posutiv_dc09_reserv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title("Резервный канал 2 Негативные сценарии: Проверка ввода значений в поле 'Адрес' - DC09")
    def test_input_data_reserv_2_address_DC09_cod_negativ_type_main_destination(self, app, destinations, close_modal,
                                                                                directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('DC09')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('DC09')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('DC09')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_address_negativ_dc09_reserv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title("Резервный канал 2 Позитивные сценарии: Проверка ввода значений в поле 'Порт' - DC09")
    def test_input_data_reserv_2_port_DC09_cod_positiv_type_main_destination(self, app, destinations, close_modal,
                                                                             directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('DC09')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('DC09')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('DC09')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_port_posutiv_dc09_reserv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title("Резервный канал 2 Негативные сценарии: Проверка ввода значений в поле 'Порт' - DC09")
    def test_input_data_reserv_2_port_DC09_cod_negativ_type_main_destination(self, app, destinations, close_modal,
                                                                             directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('DC09')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('DC09')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('DC09')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_port_negativ_dc09_reserv_2()

@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты НАПРАВЛЕНИЯ")
@allure.feature("Валидация полей ввода")
@pytest.mark.flaky(reruns=reruns)
class Test04ValidationDestinationRezerv2Chanel:

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title(
        "Резервный канал 2 Позитивные сценарии: Проверка ввода значений в поле 'Таймаут подтверждения, сек' - DC09")
    def test_input_data_reserv_2_confirmation_timeout_DC09_cod_positiv_type_main_destination(self, app, destinations,
                                                                                             close_modal,
                                                                                             directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('DC09')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('DC09')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('DC09')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_confirmation_timeout_posutiv_dc09_reserv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title(
        "Резервный канал 2 Негативные сценарии: Проверка ввода значений в поле 'Таймаут подтверждения, сек' - DC09")
    def test_input_data_reserv_2_confirmation_timeout_DC09_cod_negativ_type_main_destination(self, app, destinations,
                                                                                             close_modal,
                                                                                             directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('DC09')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('DC09')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('DC09')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_confirmation_timeout_negativ_dc09_reserv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title("Резервный канал 2 Позитивные сценарии: Проверка ввода значений в поле 'Количество повторов' - DC09")
    def test_input_data_reserv_2_number_of_repetitions_DC09_cod_positiv_type_main_destination(self, app, destinations,
                                                                                              close_modal,
                                                                                              directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('DC09')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('DC09')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('DC09')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_number_of_repetitions_posutiv_dc09_reserv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title("Резервный канал 2 Негативные сценарии: Проверка ввода значений в поле 'Количество повторов' - DC09")
    def test_input_data_reserv_2_number_of_repetitions_DC09_cod_negativ_type_main_destination(self, app, destinations,
                                                                                              close_modal,
                                                                                              directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('DC09')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('DC09')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('DC09')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_number_of_repetitions_negativ_dc09_reserv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title("Резервный канал 2 Позитивные сценарии: Проверка ввода значений в поле 'Ключ шифрования' - DC09")
    def test_input_data_reserv_2_encryption_key_DC09_cod_positiv_type_main_destination(self, app, destinations,
                                                                                       close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('DC09')
            app.PO_Directions.enableEncryption_main()
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('DC09')
            app.PO_Directions.enableEncryption_rezerv_1()
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('DC09')
            app.PO_Directions.enableEncryption_rezerv_2()
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_encryption_key_posutiv_dc09_reserv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title("Резервный канал 2 Негативные сценарии: Проверка ввода значений в поле 'Ключ шифрования' - DC09")
    def test_input_data_reserv_2_encryption_key_DC09_cod_negativ_type_main_destination(self, app, destinations,
                                                                                       close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('DC09')
            app.PO_Directions.enableEncryption_main()
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('DC09')
            app.PO_Directions.enableEncryption_rezerv_1()
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('DC09')
            app.PO_Directions.enableEncryption_rezerv_2()
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_encryption_key_negativ_dc09_reserv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title(
        "Резервный канал 2 Позитивные сценарии: Проверка ввода значений в поле 'Таймаут при ошибке' - DC09")
    def test_input_data_reserv_2_DC09_timeout_error_positiv_destination(self, app, destinations, close_modal,
                                                                        directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('DC09')
            app.PO_Directions.enableChannelTesting_main()
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('DC09')
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('DC09')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_rezerv_2()
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_timeout_error_posutiv_sms_user_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title(
        "Резервный канал 2 Негативные сценарии: Проверка ввода значений в поле 'Таймаут при ошибке' - DC09")
    def test_input_data_reserv_2_DC09_timeout_error_negativ_destination(self, app, destinations, close_modal,
                                                                        directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('DC09')
            app.PO_Directions.enableChannelTesting_main()
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('DC09')
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('DC09')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_rezerv_2()
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_timeout_error_negativ_sms_user_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title(
        "Резервный канал 2 Позитивные сценарии: Проверка ввода значений в поле 'Интервал тестирования' - DC09")
    def test_input_data_reserv_2_DC09_test_interval_positiv_destination(self, app, destinations, close_modal,
                                                                        directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('DC09')
            app.PO_Directions.enableChannelTesting_main()
            app.PO_Directions.Test_at_intervals_main_dc09('С интервалом')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('DC09')
            app.PO_Directions.enableChannelTesting_rezerv_1()
            app.PO_Directions.Test_at_intervals_reserv_1_dc09('С интервалом')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('DC09')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_rezerv_2()
        with allure.step("Выбор: тестировать с интервалом"):
            app.PO_Directions.Test_at_intervals_reserv_2_dc09('С интервалом')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_test_interval_posutiv_sms_user_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title(
        "Резервный канал 2 Негативные сценарии: Проверка ввода значений в поле 'Интервал тестирования' - DC09")
    def test_input_data_reserv_2_DC09_test_interval_negativ_destination(self, app, destinations, close_modal,
                                                                        directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('DC09')
            app.PO_Directions.enableChannelTesting_main()
            app.PO_Directions.Test_at_intervals_main_dc09('С интервалом')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('DC09')
            app.PO_Directions.enableChannelTesting_rezerv_1()
            app.PO_Directions.Test_at_intervals_reserv_1_dc09('С интервалом')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('DC09')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_rezerv_2()
        with allure.step("Выбор: тестировать с интервалом"):
            app.PO_Directions.Test_at_intervals_reserv_2_dc09('С интервалом')
        with allure.step("Проверка валидации поля"):
            app.PO_Directions.input_test_interval_posutiv_sms_user_rezerv_2()
