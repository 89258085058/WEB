# -*- coding: utf-8 -*-
import time

import allure
import pytest
from selenium.webdriver.common.by import By

reruns = 1

# directions_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
directions_list = ['1']


@pytest.fixture()
def close_modal(request, app):
    def fin():
        app.method.click((By.XPATH, '(//*[.=" Отменить "]//div)[last()]'))

    request.addfinalizer(fin)


@pytest.fixture
def destinations(app):
    with allure.step("Переход на страницу направления"):
        app.PO_Navigations.goToDirectionsPage()

@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты НАПРАВЛЕНИЯ")
@allure.feature("Проверки UI")
@pytest.mark.flaky(reruns=reruns)
class TestUIDestinationMainChanel:

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Разделы")
    @allure.title("Выбор раздела из выпадающего списка по одному")
    def test_checking_drop_down_list_path_modul_wind(self, app, destinations, close_modal,
                                                     directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_path_drop_list()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Разделы")
    @allure.title("Выбор раздела из выпадающего списка - все разделы сразу")
    def test_checking_drop_down_list_path_modul_wind_all(self, app, destinations, close_modal,
                                                         directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_path_drop_list_all()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Тумблеры: События разделов")
    @allure.title("Проверка переключения тумблеров по направлениям")
    def test_tumblers_destination_event_path(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек события разделов"):
            app.PO_Directions.openSettingsTumblers('События разделов')
        with allure.step("Проверка включения тумблеров"):
            app.PO_Directions.tumblers_event_path_on()
        with allure.step("Проверка выключения тумблеров"):
            app.PO_Directions.tumblers_event_path_off()
        with allure.step("Проверка частичного выбора тумблеров"):
            app.PO_Directions.tumblers_event_path_some()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Тумблеры: Питание прибора")
    @allure.title("Проверка переключения тумблеров по направлениям")
    def test_tumblers_destination_instrument_power_supply(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек Питание прибора"):
            app.PO_Directions.openSettingsTumblers('Питание прибора')
        with allure.step("Проверка включения тумблеров"):
            app.PO_Directions.tumblers_instrument_power_supply_on()
        with allure.step("Проверка выключения тумблеров"):
            app.PO_Directions.tumblers_instrument_power_supply_off()
        with allure.step("Проверка частичного выбора тумблеров"):
            app.PO_Directions.tumblers_instrument_power_supply_some()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Тумблеры: События зон")
    @allure.title("Проверка переключения тумблеров по направлениям")
    def test_tumblers_destination_zone_events(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек События зон"):
            app.PO_Directions.openSettingsTumblers('События зон')
        with allure.step("Проверка включения тумблеров"):
            app.PO_Directions.tumblers_zone_events_on()
        with allure.step("Проверка выключения тумблеров"):
            app.PO_Directions.tumblers_zone_events_off()
        with allure.step("Проверка частичного выбора тумблеров"):
            app.PO_Directions.tumblers_zone_events_some()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Тумблеры: Системные события прибора")
    @allure.title("Проверка переключения тумблеров по направлениям")
    def test_tumblers_destination_instrument_system_events(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек Системные события прибора"):
            app.PO_Directions.openSettingsTumblers('Системные события прибора')
        with allure.step("Проверка включения тумблеров"):
            app.PO_Directions.tumblers_instrument_system_events_on()
        with allure.step("Проверка выключения тумблеров"):
            app.PO_Directions.tumblers_instrument_system_events_off()
        with allure.step("Проверка частичного выбора тумблеров"):
            app.PO_Directions.tumblers_instrument_system_events_some()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Тумблеры")
    @allure.title("Проверка переключения тумблеров при выборе основного тумблера - Выбрать все")
    def test_tumblers_destination_check_main(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек события разделов"):
            app.PO_Directions.openSettingsTumblers('События разделов')
        with allure.step("Проверка переключения тумблеров"):
            app.PO_Directions.tumblers_event_path_on_main()
        with allure.step("Раскрытие настроек Питание прибора"):
            app.PO_Directions.openSettingsTumblers('Питание прибора')
        with allure.step("Проверка включения тумблеров"):
            app.PO_Directions.tumblers_instrument_power_supply_on_main()
        with allure.step("Раскрытие настроек События зон"):
            app.PO_Directions.openSettingsTumblers('События зон')
        with allure.step("Проверка включения тумблеров"):
            app.PO_Directions.tumblers_zone_events_on_main()
        with allure.step("Раскрытие настроек Системные события прибора"):
            app.PO_Directions.openSettingsTumblers('Системные события прибора')
        with allure.step("Проверка включения тумблеров"):
            app.PO_Directions.tumblers_instrument_system_events_on_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title("Основной канал проверка выпадающего списка: Тип управления")
    def test_checking_drop_down_list_control_type_channel_main(self, app, destinations, close_modal,
                                                               directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_openType_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title("Основной канал - SMS пользователю проверка выпадающего списка: Язык")
    def test_checking_drop_down_list_sms_user_lang_channel_main(self, app, destinations, close_modal,
                                                                directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('SMS пользователю')
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_lang_sms_user_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title("Основной канал - SMS пользователю проверка выпадающего списка: Тестировать если")
    def test_checking_drop_down_list_sms_user_test_if_channel_main(self, app, destinations, close_modal,
                                                                   directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('SMS пользователю')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_test_if_sms_user_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title("Основной канал - SMS пользователю проверка выпадающего списка: Метод тестирования")
    def test_checking_drop_down_list_sms_user_test_method_channel_main(self, app, destinations, close_modal,
                                                                       directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('SMS пользователю')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_test_method_sms_user_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title("Основной канал - SMS пользователю проверка выпадающего списка: Тестировать")
    def test_checking_drop_down_list_sms_user_testing_channel_main(self, app, destinations, close_modal,
                                                                   directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('SMS пользователю')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_testing_sms_user_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title("Основной канал - SMS пользователю проверка выпадающего списка: Дни недели - по одному")
    def test_checking_drop_down_list_sms_user_days_of_the_week_channel_main(self, app, destinations, close_modal,
                                                                            directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('SMS пользователю')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
            time.sleep(1)
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_days_of_the_week_sms_user_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title(
        "Основной канал - SMS пользователю проверка выпадающего списка: Дни недели - все сразу")
    def test_checking_drop_down_list_sms_user_days_of_the_week_all_channel_main(self, app, destinations,
                                                                                close_modal,
                                                                                directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('SMS пользователю')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_days_of_the_week_sms_user_all_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title("Основной канал - SMS пользователю проверка - чек-боксов")
    def test_checking_chesk_box_sms_user_channel_main(self, app, destinations, close_modal,
                                                      directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('SMS пользователю')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('SMS пользователю')
        with allure.step("Проверка включения чекбоксов"):
            app.PO_Directions.check_box_sms_user_on_channel_main()
        with allure.step("Проверка выключения чекбоксов"):
            app.PO_Directions.check_box_sms_user_off_channel_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title("Основной канал - SMS Эгида проверка выпадающего списка: Тестировать если")
    def test_checking_drop_down_list_sms_egida_test_if_channel_main(self, app, destinations, close_modal,
                                                                    directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('SMS Эгида')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_test_if_sms_egida_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title("Основной канал - SMS Эгида проверка выпадающего списка: Метод тестирования")
    def test_checking_drop_down_list_sms_egida_test_method_channel_main(self, app, destinations, close_modal,
                                                                        directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('SMS Эгида')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_test_method_sms_egida_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title("Основной канал - SMS Эгида проверка выпадающего списка: Тестировать")
    def test_checking_drop_down_list_sms_egida_testing_channel_main(self, app, destinations, close_modal,
                                                                    directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('SMS Эгида')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_testing_sms_egida_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title("Основной канал - SMS Эгида проверка выпадающего списка: Дни недели - по одному")
    def test_checking_drop_down_list_sms_egida_days_of_the_week_channel_main(self, app, destinations, close_modal,
                                                                             directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('SMS Эгида')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_days_of_the_week_sms_user_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title("Основной канал - SMS Эгида проверка выпадающего списка: Дни недели - по одному - все сразу")
    def test_checking_drop_down_list_sms_egida_days_of_the_week_all_channel_main(self, app, destinations,
                                                                                 close_modal,
                                                                                 directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('SMS Эгида')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_days_of_the_week_sms_user_all_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title("Основной канал - SMS Эгида проверка - чек-боксов")
    def test_checking_chesk_box_sms_egida_channel_main(self, app, destinations, close_modal,
                                                       directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('SMS Эгида')
        with allure.step("Проверка включения чекбоксов"):
            app.PO_Directions.check_box_call_on_channel_main()
        with allure.step("Проверка выключения чекбоксов"):
            app.PO_Directions.check_box_call_off_channel_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title("Основной канал - ЗВОНОК проверка выпадающего списка: Тестировать если")
    def test_checking_drop_down_list_call_test_if_channel_main(self, app, destinations, close_modal,
                                                               directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('Звонок')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_test_if_sms_egida_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title("Основной канал - ЗВОНОК проверка выпадающего списка: Метод тестирования")
    def test_checking_drop_down_list_call_test_method_channel_main(self, app, destinations, close_modal,
                                                                   directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('Звонок')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_test_method_sms_egida_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title("Основной канал - ЗВОНОК проверка выпадающего списка: Тестировать")
    def test_checking_drop_down_list_call_testing_channel_main(self, app, destinations, close_modal,
                                                               directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('Звонок')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_testing_sms_egida_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title("Основной канал - ЗВОНОК проверка выпадающего списка: Дни недели - по одному")
    def test_checking_drop_down_list_call_days_of_the_week_channel_main(self, app, destinations, close_modal,
                                                                        directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('Звонок')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_days_of_the_week_sms_user_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title("Основной канал - ЗВОНОК проверка выпадающего списка: Дни недели - по одному - все сразу")
    def test_checking_drop_down_list_call_days_of_the_week_all_channel_main(self, app, destinations, close_modal,
                                                                            directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('Звонок')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_days_of_the_week_sms_user_all_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title("Основной канал - ЗВОНОК проверка - чек-боксов")
    def test_checking_chesk_box_call_channel_main(self, app, destinations, close_modal,
                                                  directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('Звонок')
        with allure.step("Проверка включения чекбоксов"):
            app.PO_Directions.check_box_call_on_channel_main()
        with allure.step("Проверка выключения чекбоксов"):
            app.PO_Directions.check_box_call_off_channel_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title("Основной канал - DC09 проверка выпадающего списка: Канал соединения")
    def test_checking_drop_down_list_DC09_connection_channel_main(self, app, destinations, close_modal,
                                                                  directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('DC09')
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_connection_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title("Основной канал - DC09 проверка выпадающего списка: Тестировать если")
    def test_checking_drop_down_list_DC09_test_if_channel_main(self, app, destinations, close_modal,
                                                               directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('DC09')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_test_if_sms_egida_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title("Основной канал - DC09 проверка выпадающего списка: Метод тестирования")
    def test_checking_drop_down_list_DC09_test_method_channel_main(self, app, destinations, close_modal,
                                                                   directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('DC09')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_test_method_sms_egida_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title("Основной канал - DC09 проверка выпадающего списка: Тестировать")
    def test_checking_drop_down_list_DC09_testing_channel_main(self, app, destinations, close_modal,
                                                               directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('DC09')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_testing_sms_egida_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title("Основной канал - DC09 проверка выпадающего списка: Дни недели - по одному")
    def test_checking_drop_down_list_DC09_days_of_the_week_channel_main(self, app, destinations, close_modal,
                                                                        directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('DC09')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_days_of_the_week_sms_user_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title("Основной канал - DC09 проверка выпадающего списка: Дни недели - по одному - все сразу")
    def test_checking_drop_down_list_DC09_days_of_the_week_all_channel_main(self, app, destinations, close_modal,
                                                                            directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('DC09')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_days_of_the_week_sms_user_all_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title("Основной канал - DC09 проверка - чек-боксов")
    def test_checking_chesk_box_DC09_channel_main(self, app, destinations, close_modal,
                                                  directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('DC09')
        with allure.step("Проверка включения чекбоксов"):
            app.PO_Directions.check_box_dc09_on_channel_main()
        with allure.step("Проверка выключения чекбоксов"):
            app.PO_Directions.check_box_dc09_off_channel_main()

@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты НАПРАВЛЕНИЯ")
@allure.feature("Проверки UI")
@pytest.mark.flaky(reruns=reruns)
class TestUIDestinationRezerv1Chanel:

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title("Резервный канал 1 проверка выпадающего списка: Тип управления")
    def test_checking_drop_down_list_control_type_channel_rezerv_1(self, app, destinations, close_modal,
                                                                   directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS пользователю')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_openType_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title("Резервный канал 1 - SMS пользователю проверка выпадающего списка: Язык")
    def test_checking_drop_down_list_sms_user_lang_channel_rezerv_1(self, app, destinations, close_modal,
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
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_lang_sms_user_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title("Резервный канал 1 - SMS пользователю проверка выпадающего списка: Тестировать если")
    def test_checking_drop_down_list_sms_user_test_if_channel_rezerv_1(self, app, destinations, close_modal,
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
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_test_if_sms_user_resrv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title("Резервный канал 1 - SMS пользователю проверка выпадающего списка: Метод тестирования")
    def test_checking_drop_down_list_sms_user_test_method_channel_rezerv_1(self, app, destinations, close_modal,
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
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_test_method_sms_user_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title("Резервный канал 1 - SMS пользователю проверка выпадающего списка: Тестировать")
    def test_checking_drop_down_list_sms_user_testing_channel_rezerv_1(self, app, destinations, close_modal,
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
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_testing_sms_user_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title("Резервный канал 1 - SMS пользователю проверка выпадающего списка: Дни недели - по одному")
    def test_checking_drop_down_list_sms_user_days_of_the_week_channel_rezerv_1(self, app, destinations,
                                                                                close_modal,
                                                                                directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS пользователю')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('SMS пользователю')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_days_of_the_week_sms_user_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title(
        "Резервный канал 1 - SMS пользователю проверка выпадающего списка: Дни недели - все сразу")
    def test_checking_drop_down_list_sms_user_days_of_the_week_all_channel_rezerv_1(self, app, destinations,
                                                                                    close_modal,
                                                                                    directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS пользователю')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('SMS пользователю')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_days_of_the_week_sms_user_all_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title("Резервный канал 1 - SMS пользователю проверка - чек-боксов")
    def test_checking_chesk_box_sms_user_channel_rezerv_1(self, app, destinations, close_modal,
                                                          directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS пользователю')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('SMS пользователю')
        with allure.step("Проверка включения чекбоксов"):
            app.PO_Directions.check_box_sms_user_on_channel_rezerv_1()
        with allure.step("Проверка выключения чекбоксов"):
            app.PO_Directions.check_box_sms_user_off_channel_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title("Резервный канал 1 - SMS Эгида проверка выпадающего списка: Тестировать если")
    def test_checking_drop_down_list_sms_egida_test_if_channel_rezerv_1(self, app, destinations, close_modal,
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
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_test_if_sms_egida_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title("Резервный канал 1 - SMS Эгида проверка выпадающего списка: Метод тестирования")
    def test_checking_drop_down_list_sms_egida_test_method_channel_rezerv_1(self, app, destinations, close_modal,
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
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_test_method_sms_egida_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title("Резервный канал 1 - SMS Эгида проверка выпадающего списка: Тестировать")
    def test_checking_drop_down_list_sms_egida_testing_channel_rezerv_1(self, app, destinations, close_modal,
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
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_testing_sms_egida_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title("Резервный канал 1 - SMS Эгида проверка выпадающего списка: Дни недели - по одному")
    def test_checking_drop_down_list_sms_egida_days_of_the_week_channel_rezerv_1(self, app, destinations,
                                                                                 close_modal,
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
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_days_of_the_week_sms_user_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title("Резервный канал 1 - SMS Эгида проверка выпадающего списка: Дни недели - по одному - все сразу")
    def test_checking_drop_down_list_sms_egida_days_of_the_week_all_channel_rezerv_1(self, app, destinations,
                                                                                     close_modal,
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
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_days_of_the_week_sms_user_all_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title("Резервный канал 1 - SMS Эгида проверка - чек-боксов")
    def test_checking_chesk_box_sms_egida_channel_rezerv_1(self, app, destinations, close_modal,
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
        with allure.step("Проверка включения чекбоксов"):
            app.PO_Directions.check_box_call_on_channel_rezerv_1()
        with allure.step("Проверка выключения чекбоксов"):
            app.PO_Directions.check_box_call_off_channel_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title("Резервный канал 1 - ЗВОНОК проверка выпадающего списка: Тестировать если")
    def test_checking_drop_down_list_call_test_if_channel_rezerv_1(self, app, destinations, close_modal,
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
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_test_if_sms_egida_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title("Резервный канал 1 - ЗВОНОК проверка выпадающего списка: Метод тестирования")
    def test_checking_drop_down_list_call_test_method_channel_rezerv_1(self, app, destinations, close_modal,
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
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_test_method_sms_egida_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title("Резервный канал 1 - ЗВОНОК проверка выпадающего списка: Тестировать")
    def test_checking_drop_down_list_call_testing_channel_rezerv_1(self, app, destinations, close_modal,
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
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_testing_sms_egida_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title("Резервный канал 1 - ЗВОНОК проверка выпадающего списка: Дни недели - по одному")
    def test_checking_drop_down_list_call_days_of_the_week_channel_rezerv_1(self, app, destinations, close_modal,
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
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_days_of_the_week_sms_user_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title("Резервный канал 1 - ЗВОНОК проверка выпадающего списка: Дни недели - по одному - все сразу")
    def test_checking_drop_down_list_call_days_of_the_week_all_channel_rezerv_1(self, app, destinations,
                                                                                close_modal,
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
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_days_of_the_week_sms_user_all_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title("Резервный канал 1 - ЗВОНОК проверка - чек-боксов")
    def test_checking_chesk_box_call_channel_rezerv_1(self, app, destinations, close_modal,
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
        with allure.step("Проверка включения чекбоксов"):
            app.PO_Directions.check_box_call_on_channel_rezerv_1()
        with allure.step("Проверка выключения чекбоксов"):
            app.PO_Directions.check_box_call_off_channel_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title("Резервный канал 1 - DC09 проверка выпадающего списка: Канал соединения")
    def test_checking_drop_down_list_DC09_connection_channel_rezerv_1(self, app, destinations, close_modal,
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
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_connection_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title("Резервный канал 1 - DC09 проверка выпадающего списка: Тестировать если")
    def test_checking_drop_down_list_DC09_test_if_channel_rezerv_1(self, app, destinations, close_modal,
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
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_test_if_sms_egida_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title("Резервный канал 1 - DC09 проверка выпадающего списка: Метод тестирования")
    def test_checking_drop_down_list_DC09_test_method_channel_rezerv_1(self, app, destinations, close_modal,
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
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_test_method_sms_egida_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title("Резервный канал 1 - DC09 проверка выпадающего списка: Тестировать")
    def test_checking_drop_down_list_DC09_testing_channel_rezerv_1(self, app, destinations, close_modal,
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
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_testing_sms_egida_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title("Резервный канал 1 - DC09 проверка выпадающего списка: Дни недели - по одному")
    def test_checking_drop_down_list_DC09_days_of_the_week_channel_rezerv_1(self, app, destinations, close_modal,
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
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_days_of_the_week_sms_user_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title("Резервный канал 1 - DC09 проверка выпадающего списка: Дни недели - по одному - все сразу")
    def test_checking_drop_down_list_DC09_days_of_the_week_all_channel_rezerv_1(self, app, destinations,
                                                                                close_modal,
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
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_days_of_the_week_sms_user_all_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 1")
    @allure.title("Резервный канал 1 - DC09 проверка - чек-боксов")
    def test_checking_chesk_box_DC09_channel_rezerv_1(self, app, destinations, close_modal,
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
        with allure.step("Проверка включения чекбоксов"):
            app.PO_Directions.check_box_dc09_onn_channel_rezerv_1()
        with allure.step("Проверка выключения чекбоксов"):
            app.PO_Directions.check_box_dc09_off_channel_rezerv_1()

@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты НАПРАВЛЕНИЯ")
@allure.feature("Проверки UI")
@pytest.mark.flaky(reruns=reruns)
class TestUIDestinationRezerv2Chanel:

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title("Резервный канал 2 проверка выпадающего списка: Тип управления")
    def test_checking_drop_down_list_control_type_channel_rezerv_2(self, app, destinations, close_modal,
                                                                   directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS пользователю')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('SMS пользователю')
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_openType_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title("Резервный канал 2 - SMS пользователю проверка выпадающего списка: Язык")
    def test_checking_drop_down_list_sms_user_lang_channel_rezerv_2(self, app, destinations, close_modal,
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
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_lang_sms_user_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title("Резервный канал 2 - SMS пользователю проверка выпадающего списка: Тестировать если")
    def test_checking_drop_down_list_sms_user_test_if_channel_rezerv_2(self, app, destinations, close_modal,
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
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_test_if_sms_user_resrv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title("Резервный канал 2 - SMS пользователю проверка выпадающего списка: Метод тестирования")
    def test_checking_drop_down_list_sms_user_test_method_channel_rezerv_2(self, app, destinations, close_modal,
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
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_test_method_sms_user_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title("Резервный канал 2 - SMS пользователю проверка выпадающего списка: Тестировать")
    def test_checking_drop_down_list_sms_user_testing_channel_rezerv_2(self, app, destinations, close_modal,
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
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_testing_sms_user_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title("Резервный канал 2 - SMS пользователю проверка выпадающего списка: Дни недели - по одному")
    def test_checking_drop_down_list_sms_user_days_of_the_week_channel_rezerv_2(self, app, destinations, close_modal,
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
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_days_of_the_week_sms_user_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title(
        "Резервный канал 2 - SMS пользователю проверка выпадающего списка: Дни недели - все сразу")
    def test_checking_drop_down_list_sms_user_days_of_the_week_all_channel_rezerv_2(self, app, destinations,
                                                                                    close_modal,
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
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_days_of_the_week_sms_user_all_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title("Резервный канал 2 - SMS пользователю проверка - чек-боксов")
    def test_checking_chesk_box_sms_user_channel_rezerv_2(self, app, destinations, close_modal,
                                                          directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытия настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS пользователю')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('SMS пользователю')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_2('SMS пользователю')
        with allure.step("Проверка включения чекбоксов"):
            app.PO_Directions.check_box_sms_user_on_channel_rezerv_2()
        with allure.step("Проверка выключения чекбоксов"):
            app.PO_Directions.check_box_sms_user_off_channel_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title("Резервный канал 2 - SMS Эгида проверка выпадающего списка: Тестировать если")
    def test_checking_drop_down_list_sms_egida_test_if_channel_rezerv_2(self, app, destinations, close_modal,
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
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_rezerv_2()
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_test_if_sms_egida_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title("Резервный канал 2 - SMS Эгида проверка выпадающего списка: Метод тестирования")
    def test_checking_drop_down_list_sms_egida_test_method_channel_rezerv_2(self, app, destinations, close_modal,
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
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_test_method_sms_egida_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title("Резервный канал 2 - SMS Эгида проверка выпадающего списка: Тестировать")
    def test_checking_drop_down_list_sms_egida_testing_channel_rezerv_2(self, app, destinations, close_modal,
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
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_testing_sms_egida_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title("Резервный канал 2 - SMS Эгида проверка выпадающего списка: Дни недели - по одному")
    def test_checking_drop_down_list_sms_egida_days_of_the_week_channel_rezerv_2(self, app, destinations, close_modal,
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
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_days_of_the_week_sms_user_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title("Резервный канал 2 - SMS Эгида проверка выпадающего списка: Дни недели - по одному - все сразу")
    def test_checking_drop_down_list_sms_egida_days_of_the_week_all_channel_rezerv_2(self, app, destinations,
                                                                                     close_modal,
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
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_days_of_the_week_sms_user_all_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title("Резервный канал 2 - SMS Эгида проверка - чек-боксов")
    def test_checking_chesk_box_sms_egida_channel_rezerv_2(self, app, destinations, close_modal,
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
        with allure.step("Проверка включения чекбоксов"):
            app.PO_Directions.check_box_call_on_channel_rezerv_2()
        with allure.step("Проверка выключения чекбоксов"):
            app.PO_Directions.check_box_call_off_channel_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title("Резервный канал 2 - ЗВОНОК проверка выпадающего списка: Тестировать если")
    def test_checking_drop_down_list_call_test_if_channel_rezerv_2(self, app, destinations, close_modal,
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
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_test_if_sms_egida_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title("Резервный канал 2 - ЗВОНОК проверка выпадающего списка: Метод тестирования")
    def test_checking_drop_down_list_call_test_method_channel_rezerv_2(self, app, destinations, close_modal,
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
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_test_method_sms_egida_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title("Резервный канал 2 - ЗВОНОК проверка выпадающего списка: Тестировать")
    def test_checking_drop_down_list_call_testing_channel_rezerv_2(self, app, destinations, close_modal,
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
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_testing_sms_egida_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title("Резервный канал 2 - ЗВОНОК проверка выпадающего списка: Дни недели - по одному")
    def test_checking_drop_down_list_call_days_of_the_week_channel_rezerv_2(self, app, destinations, close_modal,
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
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_days_of_the_week_sms_user_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title("Резервный канал 2 - ЗВОНОК проверка выпадающего списка: Дни недели - по одному - все сразу")
    def test_checking_drop_down_list_call_days_of_the_week_all_channel_rezerv_2(self, app, destinations, close_modal,
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
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_days_of_the_week_sms_user_all_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title("Резервный канал 2 - ЗВОНОК проверка - чек-боксов")
    def test_checking_chesk_box_call_channel_rezerv_2(self, app, destinations, close_modal,
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
        with allure.step("Проверка включения чекбоксов"):
            app.PO_Directions.check_box_call_on_channel_rezerv_2()
        with allure.step("Проверка выключения чекбоксов"):
            app.PO_Directions.check_box_call_off_channel_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title("Резервный канал 2 - DC09 проверка выпадающего списка: Канал соединения")
    def test_checking_drop_down_list_DC09_connection_channel_rezerv_2(self, app, destinations, close_modal,
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
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_connection_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title("Резервный канал 2 - DC09 проверка выпадающего списка: Тестировать если")
    def test_checking_drop_down_list_DC09_test_if_channel_rezerv_2(self, app, destinations, close_modal,
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
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_test_if_sms_egida_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title("Резервный канал 2 - DC09 проверка выпадающего списка: Метод тестирования")
    def test_checking_drop_down_list_DC09_test_method_channel_rezerv_2(self, app, destinations, close_modal,
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
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_test_method_sms_egida_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title("Резервный канал 2 - DC09 проверка выпадающего списка: Тестировать")
    def test_checking_drop_down_list_DC09_testing_channel_rezerv_2(self, app, destinations, close_modal,
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
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_testing_sms_egida_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title("Резервный канал 2 - DC09 проверка выпадающего списка: Дни недели - по одному")
    def test_checking_drop_down_list_DC09_days_of_the_week_channel_rezerv_2(self, app, destinations, close_modal,
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
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_days_of_the_week_sms_user_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title("Резервный канал 2 - DC09 проверка выпадающего списка: Дни недели - по одному - все сразу")
    def test_checking_drop_down_list_DC09_days_of_the_week_all_channel_rezerv_2(self, app, destinations, close_modal,
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
        with allure.step("Проверка выбора из выпадающего списка"):
            app.PO_Directions.check_days_of_the_week_sms_user_all_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный канал 2")
    @allure.title("Резервный канал 2 - DC09 проверка - чек-боксов")
    def test_checking_chesk_box_DC09_channel_rezerv_2(self, app, destinations, close_modal,
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
        with allure.step("Проверка включения чекбоксов"):
            app.PO_Directions.check_box_dc09_onn_channel_rezerv_2()
        with allure.step("Проверка выключения чекбоксов"):
            app.PO_Directions.check_box_dc09_off_channel_rezerv_2()
