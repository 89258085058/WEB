# -*- coding: utf-8 -*-

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
@allure.feature("Сохранение данных")
@pytest.mark.flaky(reruns=reruns)
class TestSaveDestinationTumblers:

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Тумблеры")
    @allure.title("Проверка сохранения тумблеров События разделов (Включение)")
    def test_directions_save_tumblers_section_events_ON(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек события разделов"):
            app.PO_Directions.openSettingsTumblers('События разделов')
        with allure.step("Переключение всех тумблеров в положение ON"):
            app.PO_Directions.tumblers_event_path_on_save()
        with allure.step("Сохранение данных"):
            app.PO_Directions.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToDirectionsPage()
            app.PO_Directions.openDestination(directions)
            app.PO_Directions.openSettingsTumblers('События разделов')
        with allure.step("Проверка сохранения выбора тумблеров"):
            app.PO_Directions.assert_save_tumblers_event_path_on()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Тумблеры")
    @allure.title("Проверка сохранения тумблеров События разделов (Выключение)")
    def test_directions_save_tumblers_section_events_OFF(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек события разделов"):
            app.PO_Directions.openSettingsTumblers('События разделов')
        with allure.step("Переключение всех тумблеров в положение OFF"):
            app.PO_Directions.tumblers_event_path_off_save()
        with allure.step("Сохранение данных"):
            app.PO_Directions.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToDirectionsPage()
            app.PO_Directions.openDestination(directions)
            app.PO_Directions.openSettingsTumblers('События разделов')
        with allure.step("Проверка сохранения выбора тумблеров"):
            app.PO_Directions.assert_save_tumblers_event_path_off()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Тумблеры")
    @allure.title("Проверка сохранения тумблеров События разделов (Частичное Включение 1)")
    def test_directions_save_tumblers_section_events_SOME_1(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек события разделов"):
            app.PO_Directions.openSettingsTumblers('События разделов')
        with allure.step("Частичное переключение тумблеров"):
            app.PO_Directions.tumblers_event_path_some_save()
        with allure.step("Сохранение данных"):
            app.PO_Directions.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToDirectionsPage()
            app.PO_Directions.openDestination(directions)
            app.PO_Directions.openSettingsTumblers('События разделов')
        with allure.step("Проверка сохранения выбора тумблеров"):
            app.PO_Directions.assert_save_tumblers_event_path_some()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Тумблеры")
    @allure.title("Проверка сохранения тумблеров События разделов (Частичное Включение 2)")
    def test_directions_save_tumblers_section_events_SOME_2(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек события разделов"):
            app.PO_Directions.openSettingsTumblers('События разделов')
        with allure.step("Частичное переключение тумблеров"):
            app.PO_Directions.tumblers_event_path_some_2_save()
        with allure.step("Сохранение данных"):
            app.PO_Directions.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToDirectionsPage()
            app.PO_Directions.openDestination(directions)
            app.PO_Directions.openSettingsTumblers('События разделов')
        with allure.step("Проверка сохранения выбора тумблеров"):
            app.PO_Directions.assert_save_tumblers_event_path_some_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Тумблеры")
    @allure.title("Проверка сохранения тумблеров События разделов (Выбор основного тумблера)")
    def test_directions_save_tumblers_section_events_main(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек события разделов"):
            app.PO_Directions.openSettingsTumblers('События разделов')
        with allure.step("Переключение основного тумблера"):
            app.PO_Directions.tumblers_event_path_main()
        with allure.step("Сохранение данных"):
            app.PO_Directions.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToDirectionsPage()
            app.PO_Directions.openDestination(directions)
            app.PO_Directions.openSettingsTumblers('События разделов')
        with allure.step("Проверка сохранения выбора тумблеров"):
            app.PO_Directions.assert_save_tumblers_event_path_on()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Тумблеры")
    @allure.title("Проверка сохранения тумблеров События зон (Включение)")
    def test_directions_save_tumblers_zone_events_ON(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек события зон"):
            app.PO_Directions.openSettingsTumblers('События зон')
        with allure.step("Переключение всех тумблеров в положение ON"):
            app.PO_Directions.tumblers_zone_events_save_on()
        with allure.step("Сохранение данных"):
            app.PO_Directions.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToDirectionsPage()
            app.PO_Directions.openDestination(directions)
            app.PO_Directions.openSettingsTumblers('События зон')
        with allure.step("Проверка сохранения выбора тумблеров"):
            app.PO_Directions.assert_tumblers_zone_events_save_on()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Тумблеры")
    @allure.title("Проверка сохранения тумблеров События зон (Выключение)")
    def test_directions_save_tumblers_zone_events_OFF(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек события зон"):
            app.PO_Directions.openSettingsTumblers('События зон')
        with allure.step("Переключение всех тумблеров в положение OFF"):
            app.PO_Directions.tumblers_zone_events_save_off()
        with allure.step("Сохранение данных"):
            app.PO_Directions.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToDirectionsPage()
            app.PO_Directions.openDestination(directions)
            app.PO_Directions.openSettingsTumblers('События зон')
        with allure.step("Проверка сохранения выбора тумблеров"):
            app.PO_Directions.assert_tumblers_zone_events_save_off()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Тумблеры")
    @allure.title("Проверка сохранения тумблеров События зон (Частичное Включение 1)")
    def test_directions_save_tumblers_zone_events_SOME_1(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек события зон"):
            app.PO_Directions.openSettingsTumblers('События зон')
        with allure.step("Частичное переключение тумблеров"):
            app.PO_Directions.tumblers_zone_events_save_some_1()
        with allure.step("Сохранение данных"):
            app.PO_Directions.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToDirectionsPage()
            app.PO_Directions.openDestination(directions)
            app.PO_Directions.openSettingsTumblers('События зон')
        with allure.step("Проверка сохранения выбора тумблеров"):
            app.PO_Directions.assert_tumblers_zone_events_save_some_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Тумблеры")
    @allure.title("Проверка сохранения тумблеров События зон (Частичное Включение 2)")
    def test_directions_save_tumblers_zone_events_SOME_2(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек события зон"):
            app.PO_Directions.openSettingsTumblers('События зон')
        with allure.step("Частичное переключение тумблеров"):
            app.PO_Directions.tumblers_zone_events_save_some_2()
        with allure.step("Сохранение данных"):
            app.PO_Directions.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToDirectionsPage()
            app.PO_Directions.openDestination(directions)
            app.PO_Directions.openSettingsTumblers('События зон')
        with allure.step("Проверка сохранения выбора тумблеров"):
            app.PO_Directions.assert_tumblers_zone_events_save_some_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Тумблеры")
    @allure.title("Проверка сохранения тумблеров События зон (Выбор основного тумблера)")
    def test_directions_save_tumblers_zone_events_main(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек события зон"):
            app.PO_Directions.openSettingsTumblers('События зон')
        with allure.step("Переключение основного тумблера"):
            app.PO_Directions.tumblers_zone_events_save_on_main()
        with allure.step("Сохранение данных"):
            app.PO_Directions.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToDirectionsPage()
            app.PO_Directions.openDestination(directions)
            app.PO_Directions.openSettingsTumblers('События зон')
        with allure.step("Проверка сохранения выбора тумблеров"):
            app.PO_Directions.assert_tumblers_zone_events_save_on()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Тумблеры")
    @allure.title("Проверка сохранения тумблеров Питание прибора (Включение)")
    def test_directions_save_tumblers_instrument_power_supply_ON(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек Питание прибора"):
            app.PO_Directions.openSettingsTumblers('Питание прибора')
        with allure.step("Переключение всех тумблеров в положение ON"):
            app.PO_Directions.tumblers_instrument_power_supply_save_on()
        with allure.step("Сохранение данных"):
            app.PO_Directions.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToDirectionsPage()
            app.PO_Directions.openDestination(directions)
            app.PO_Directions.openSettingsTumblers('Питание прибора')
        with allure.step("Проверка сохранения выбора тумблеров"):
            app.PO_Directions.assert_tumblers_instrument_power_supply_save_on()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Тумблеры")
    @allure.title("Проверка сохранения тумблеров Питание прибора (Выключение)")
    def test_directions_save_tumblers_instrument_power_supply_OFF(self, app, destinations, close_modal,
                                                                  directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек Питание прибора"):
            app.PO_Directions.openSettingsTumblers('Питание прибора')
        with allure.step("Переключение всех тумблеров в положение OFF"):
            app.PO_Directions.tumblers_instrument_power_supply_save_off()
        with allure.step("Сохранение данных"):
            app.PO_Directions.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToDirectionsPage()
            app.PO_Directions.openDestination(directions)
            app.PO_Directions.openSettingsTumblers('Питание прибора')
        with allure.step("Проверка сохранения выбора тумблеров"):
            app.PO_Directions.assert_tumblers_instrument_power_supply_save_off()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Тумблеры")
    @allure.title("Проверка сохранения тумблеров Питание прибора (Частичное Включение 1)")
    def test_directions_save_tumblers_instrument_power_supply_ON_some_1(self, app, destinations, close_modal,
                                                                        directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек Питание прибора"):
            app.PO_Directions.openSettingsTumblers('Питание прибора')
        with allure.step("Частичное переключение тумблеров"):
            app.PO_Directions.tumblers_instrument_power_supply_save_on_some_1()
        with allure.step("Сохранение данных"):
            app.PO_Directions.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToDirectionsPage()
            app.PO_Directions.openDestination(directions)
            app.PO_Directions.openSettingsTumblers('Питание прибора')
        with allure.step("Проверка сохранения выбора тумблеров"):
            app.PO_Directions.assert_tumblers_instrument_power_supply_save_on_some_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Тумблеры")
    @allure.title("Проверка сохранения тумблеров Питание прибора (Частичное Включение 2)")
    def test_directions_save_tumblers_instrument_power_supply_ON_some_2(self, app, destinations, close_modal,
                                                                        directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек Питание прибора"):
            app.PO_Directions.openSettingsTumblers('Питание прибора')
        with allure.step("Частичное переключение тумблеров"):
            app.PO_Directions.tumblers_instrument_power_supply_save_on_some_2()
        with allure.step("Сохранение данных"):
            app.PO_Directions.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToDirectionsPage()
            app.PO_Directions.openDestination(directions)
            app.PO_Directions.openSettingsTumblers('Питание прибора')
        with allure.step("Проверка сохранения выбора тумблеров"):
            app.PO_Directions.assert_tumblers_instrument_power_supply_save_on_some_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Тумблеры")
    @allure.title("Проверка сохранения тумблеров Питание прибора (Выбор основного тумблера)")
    def test_directions_save_tumblers_instrument_power_supply_main(self, app, destinations, close_modal,
                                                                   directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек Питание прибора"):
            app.PO_Directions.openSettingsTumblers('Питание прибора')
        with allure.step("Переключение основного тумблера"):
            app.PO_Directions.tumblers_instrument_power_supply_save_main()
        with allure.step("Сохранение данных"):
            app.PO_Directions.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToDirectionsPage()
            app.PO_Directions.openDestination(directions)
            app.PO_Directions.openSettingsTumblers('Питание прибора')
        with allure.step("Проверка сохранения выбора тумблеров"):
            app.PO_Directions.assert_tumblers_instrument_power_supply_save_on()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Тумблеры")
    @allure.title("Проверка сохранения тумблеров Системные события прибора (Включение)")
    def test_directions_save_tumblers_instrument_system_events_ON(self, app, destinations, close_modal,
                                                                  directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек Системные события прибора"):
            app.PO_Directions.openSettingsTumblers('Системные события прибора')
        with allure.step("Переключение всех тумблеров в положение ON"):
            app.PO_Directions.tumblers_instrument_system_events_save_on()
        with allure.step("Сохранение данных"):
            app.PO_Directions.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToDirectionsPage()
            app.PO_Directions.openDestination(directions)
            app.PO_Directions.openSettingsTumblers('Системные события прибора')
        with allure.step("Проверка сохранения выбора тумблеров"):
            app.PO_Directions.assert_tumblers_instrument_system_events_save_on()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Тумблеры")
    @allure.title("Проверка сохранения тумблеров Системные события прибора (Выключение)")
    def test_directions_save_tumblers_instrument_system_events_OFF(self, app, destinations, close_modal,
                                                                   directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек Системные события прибора"):
            app.PO_Directions.openSettingsTumblers('Системные события прибора')
        with allure.step("Переключение всех тумблеров в положение OFF"):
            app.PO_Directions.tumblers_instrument_system_events_save_off()
        with allure.step("Сохранение данных"):
            app.PO_Directions.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToDirectionsPage()
            app.PO_Directions.openDestination(directions)
            app.PO_Directions.openSettingsTumblers('Системные события прибора')
        with allure.step("Проверка сохранения выбора тумблеров"):
            app.PO_Directions.assert_tumblers_instrument_system_events_save_off()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Тумблеры")
    @allure.title("Проверка сохранения тумблеров Системные события прибора (Частичное Включение 1)")
    def test_directions_save_tumblers_instrument_system_events_ON_some_1(self, app, destinations, close_modal,
                                                                         directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек Системные события прибора"):
            app.PO_Directions.openSettingsTumblers('Системные события прибора')
        with allure.step("Частичное переключение тумблеров"):
            app.PO_Directions.tumblers_instrument_system_events_save_on_some_1()
        with allure.step("Сохранение данных"):
            app.PO_Directions.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToDirectionsPage()
            app.PO_Directions.openDestination(directions)
            app.PO_Directions.openSettingsTumblers('Системные события прибора')
        with allure.step("Проверка сохранения выбора тумблеров"):
            app.PO_Directions.assert_tumblers_instrument_system_events_save_on_some_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Тумблеры")
    @allure.title("Проверка сохранения тумблеров Системные события прибора (Частичное Включение 2)")
    def test_directions_save_tumblers_instrument_system_events_ON_some_2(self, app, destinations, close_modal,
                                                                         directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек Системные события прибора"):
            app.PO_Directions.openSettingsTumblers('Системные события прибора')
        with allure.step("Частичное переключение тумблеров"):
            app.PO_Directions.tumblers_instrument_system_events_save_on_some_2()
        with allure.step("Сохранение данных"):
            app.PO_Directions.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToDirectionsPage()
            app.PO_Directions.openDestination(directions)
            app.PO_Directions.openSettingsTumblers('Системные события прибора')
        with allure.step("Проверка сохранения выбора тумблеров"):
            app.PO_Directions.assert_tumblers_instrument_system_events_save_on_some_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Тумблеры")
    @allure.title("Проверка сохранения тумблеров Системные события прибора (Выбор основного тумблера)")
    def test_directions_save_tumblers_instrument_system_events_main(self, app, destinations, close_modal,
                                                                    directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек Системные события прибора"):
            app.PO_Directions.openSettingsTumblers('Системные события прибора')
        with allure.step("Переключение основного тумблера"):
            app.PO_Directions.tumblers_instrument_system_events_save_main()
        with allure.step("Сохранение данных"):
            app.PO_Directions.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToDirectionsPage()
            app.PO_Directions.openDestination(directions)
            app.PO_Directions.openSettingsTumblers('Системные события прибора')
        with allure.step("Проверка сохранения выбора тумблеров"):
            app.PO_Directions.assert_tumblers_instrument_system_events_save_on()


@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты НАПРАВЛЕНИЯ")
@allure.feature("Сохранение данных")
@pytest.mark.flaky(reruns=reruns)
class TestSaveDestinationChanels:

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story(f"Название - Направление")
    @allure.title("Проверка сохранения наименования")
    def test_save_name_directions(self, app, destinations, close_modal, directions: str):
        with allure.step("Генерирование тестовых данных"):
            app.ganerate_data.createData()
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Ввод данных в поле"):
            app.PO_Directions.input_destination_name_for_save()
        with allure.step("Сохранение данных"):
            app.PO_Directions.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToDirectionsPage()
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Проверка сохранения поля"):
            app.PO_Directions.assert_input_destination_name_for_save()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Разделы")
    @allure.title("Проверка сохранения раздела из выпадающего списка")
    def test_save_path_directions(self, app, destinations, close_modal, directions: str):
        with allure.step("Генерирование тестовых данных"):
            app.ganerate_data.createData()
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Выбора из выпадающего списка"):
            app.PO_Directions.path_select()
        with allure.step("Сохранение данных"):
            app.PO_Directions.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToDirectionsPage()
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Проверка сохранения поля"):
            app.PO_Directions.assert_path_select_save()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title("Основной канал - SMS пользователю - тестировать интервалом")
    def test_checking_save_sms_user_interval_main(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('SMS пользователю')
            app.PO_Directions.openType_rezerv_1('Отключено')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Ввод данных для сохранения"):
            app.PO_Directions.save_sms_user_main()
        with allure.step("Сохранение данных"):
            app.PO_Directions.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToDirectionsPage()
            app.PO_Directions.openDestination(directions)
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS пользователю')
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Проверка сохранения поля"):
            app.PO_Directions.assert_save_sms_user_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title("Основной канал - SMS пользователю - тестировать по расписанию")
    def test_checking_save_sms_user_time_table_main(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('SMS пользователю')
            app.PO_Directions.openType_rezerv_1('Отключено')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Ввод данных для сохранения"):
            app.PO_Directions.save_sms_user_timetable_main()
        with allure.step("Сохранение данных"):
            app.PO_Directions.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToDirectionsPage()
            app.PO_Directions.openDestination(directions)
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS пользователю')
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Проверка сохранения поля"):
            app.PO_Directions.assert_save_sms_user_timetable_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный 1 канал")
    @allure.title("Резервный 2 канал - SMS пользователю - тестировать интервалом")
    def test_checking_save_sms_user_interval_rezerv_1(self, app, destinations, close_modal, directions: str):
        with allure.step("Генерирование тестовых данных"):
            app.ganerate_data.createData()
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS пользователю')
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('SMS пользователю')
            app.PO_Directions.openType_rezerv_2('Отключено')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Ввод данных для сохранения"):
            app.PO_Directions.save_sms_user_rezerv_1()
        with allure.step("Сохранение данных"):
            app.PO_Directions.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToDirectionsPage()
            app.PO_Directions.openDestination(directions)
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_main('SMS пользователю')
            app.PO_Directions.openType_rezerv_1('SMS пользователю')
            app.PO_Directions.enableChannelTesting_main()
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Проверка сохранения поля"):
            app.PO_Directions.assert_save_sms_user_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный 1 канал")
    @allure.title("Резервный 1 канал - SMS пользователю - тестировать по расписанию")
    def test_checking_save_sms_user_time_table_rezerv_1(self, app, destinations, close_modal, directions: str):
        with allure.step("Генерирование тестовых данных"):
            app.ganerate_data.createData()
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS пользователю')
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_rezerv_1('SMS пользователю')
            app.PO_Directions.openType_rezerv_2('Отключено')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Ввод данных для сохранения"):
            app.PO_Directions.save_sms_user_timetable_rezerv_1()
        with allure.step("Сохранение данных"):
            app.PO_Directions.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToDirectionsPage()
            app.PO_Directions.openDestination(directions)
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS пользователю')
            app.PO_Directions.enableChannelTesting_main()
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('SMS пользователю')
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Проверка сохранения поля"):
            app.PO_Directions.assert_save_sms_user_timetable_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный 2 канал")
    @allure.title("Резервный 2 канал - SMS пользователю - тестировать интервалом")
    def test_checking_save_sms_user_interval_rezerv_2(self, app, destinations, close_modal, directions: str):
        with allure.step("Генерирование тестовых данных"):
            app.ganerate_data.createData()
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
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
        with allure.step("Ввод данных для сохранения"):
            app.PO_Directions.save_sms_user_rezerv_2()
        with allure.step("Сохранение данных"):
            app.PO_Directions.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToDirectionsPage()
            app.PO_Directions.openDestination(directions)
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS пользователю')
            app.PO_Directions.enableChannelTesting_main()
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('SMS пользователю')
            app.PO_Directions.enableChannelTesting_rezerv_1()
            app.PO_Directions.openChanel('Резерв 2')
            app.PO_Directions.openType_rezerv_2('SMS пользователю')
            app.PO_Directions.enableChannelTesting_rezerv_2()
        with allure.step("Проверка сохранения поля"):
            app.PO_Directions.assert_save_sms_user_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный 2 канал")
    @allure.title("Резервный 2 канал - SMS пользователю - тестировать по расписанию")
    def test_checking_save_sms_user_time_table_rezerv_2(self, app, destinations, close_modal, directions: str):
        with allure.step("Генерирование тестовых данных"):
            app.ganerate_data.createData()
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Предусловия раскрытие настроек канала"):
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
        with allure.step("Ввод данных для сохранения"):
            app.PO_Directions.save_sms_user_timetable_rezerv_2()
        with allure.step("Сохранение данных"):
            app.PO_Directions.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToDirectionsPage()
            app.PO_Directions.openDestination(directions)
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS пользователю')
            app.PO_Directions.enableChannelTesting_main()
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_rezerv_1('SMS пользователю')
            app.PO_Directions.enableChannelTesting_rezerv_1()
            app.PO_Directions.openChanel('Резерв 2')
            app.PO_Directions.openType_rezerv_2('SMS пользователю')
            app.PO_Directions.enableChannelTesting_rezerv_2()
        with allure.step("Проверка сохранения поля"):
            app.PO_Directions.assert_save_sms_user_timetable_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title("Основной канал - SMS Эгида - тестировать интервалом")
    def test_checking_save_sms_egida_interval_main(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('SMS Эгида')
            app.PO_Directions.openType_rezerv_1('Отключено')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Ввод данных для сохранения"):
            app.PO_Directions.save_sms_egida_main()
        with allure.step("Сохранение данных"):
            app.PO_Directions.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToDirectionsPage()
            app.PO_Directions.openDestination(directions)
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS Эгида')
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Проверка сохранения поля"):
            app.PO_Directions.assert_save_sms_egida_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Основной канал")
    @allure.title("Основной канал - SMS Эгида - тестировать по расписанию")
    def test_checking_save_sms_egida_time_table_main(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('SMS Эгида')
            app.PO_Directions.openType_rezerv_1('Отключено')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Ввод данных для сохранения"):
            app.PO_Directions.save_sms_egida_timetable_main()
        with allure.step("Сохранение данных"):
            app.PO_Directions.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToDirectionsPage()
            app.PO_Directions.openDestination(directions)
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openType_main('SMS Эгида')
            app.PO_Directions.enableChannelTesting_main()
        with allure.step("Проверка сохранения поля"):
            app.PO_Directions.assert_save_sms_egida_timetable_main()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный 1 канал")
    @allure.title("Резервный 1 канал - SMS Эгида - тестировать интервалом")
    def test_checking_save_sms_egida_interval_rezerv_1(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('SMS Эгида')
            app.PO_Directions.openType_rezerv_1('SMS Эгида')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Ввод данных для сохранения"):
            app.PO_Directions.save_sms_egida_rezerv_1()
        with allure.step("Сохранение данных"):
            app.PO_Directions.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToDirectionsPage()
            app.PO_Directions.openDestination(directions)
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_main('SMS Эгида')
            app.PO_Directions.openType_rezerv_1('SMS Эгида')
            app.PO_Directions.enableChannelTesting_main()
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Проверка сохранения поля"):
            app.PO_Directions.assert_save_sms_egida_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный 1 канал")
    @allure.title("Резервный 1 канал - SMS Эгида - тестировать по расписанию")
    def test_checking_save_sms_egida_time_table_rezerv_1(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openChanel('Резерв 1')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('SMS Эгида')
            app.PO_Directions.openType_rezerv_1('SMS Эгида')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Ввод данных для сохранения"):
            app.PO_Directions.save_sms_egida_timetable_rezerv_1()
        with allure.step("Сохранение данных"):
            app.PO_Directions.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToDirectionsPage()
            app.PO_Directions.openDestination(directions)
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openType_main('SMS Эгида')
            app.PO_Directions.openType_rezerv_1('SMS Эгида')
            app.PO_Directions.enableChannelTesting_main()
            app.PO_Directions.enableChannelTesting_rezerv_1()
        with allure.step("Проверка сохранения поля"):
            app.PO_Directions.assert_save_sms_egida_timetable_rezerv_1()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный 2 канал")
    @allure.title("Резервный 2 канал - SMS Эгида - тестировать интервалом")
    def test_checking_save_sms_egida_interval_rezerv_2(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('SMS Эгида')
            app.PO_Directions.openType_rezerv_1('SMS Эгида')
            app.PO_Directions.openType_rezerv_2('SMS Эгида')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
            app.PO_Directions.enableChannelTesting_rezerv_1()
            app.PO_Directions.enableChannelTesting_rezerv_2()
        with allure.step("Ввод данных для сохранения"):
            app.PO_Directions.save_sms_egida_rezerv_2()
        with allure.step("Сохранение данных"):
            app.PO_Directions.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToDirectionsPage()
            app.PO_Directions.openDestination(directions)
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openChanel('Резерв 2')
            app.PO_Directions.openType_main('SMS Эгида')
            app.PO_Directions.openType_rezerv_1('SMS Эгида')
            app.PO_Directions.openType_rezerv_2('SMS Эгида')
            app.PO_Directions.enableChannelTesting_main()
            app.PO_Directions.enableChannelTesting_rezerv_1()
            app.PO_Directions.enableChannelTesting_rezerv_2()
        with allure.step("Проверка сохранения поля"):
            app.PO_Directions.assert_save_sms_egida_rezerv_2()

    @pytest.mark.parametrize("directions", directions_list)
    @allure.story("Резервный 2 канал")
    @allure.title("Резервный 2 канал - SMS Эгида - тестировать по расписанию")
    def test_checking_save_sms_egida_time_table_rezerv_2(self, app, destinations, close_modal, directions: str):
        with allure.step("Открытие направления"):
            app.PO_Directions.openDestination(directions)
        with allure.step("Раскрытие настроек канала"):
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openChanel('Резерв 2')
        with allure.step("Выбор типа управления"):
            app.PO_Directions.openType_main('SMS Эгида')
            app.PO_Directions.openType_rezerv_1('SMS Эгида')
            app.PO_Directions.openType_rezerv_2('SMS Эгида')
        with allure.step("Включения тестирования канала"):
            app.PO_Directions.enableChannelTesting_main()
            app.PO_Directions.enableChannelTesting_rezerv_1()
            app.PO_Directions.enableChannelTesting_rezerv_2()
        with allure.step("Ввод данных для сохранения"):
            app.PO_Directions.save_sms_egida_timetable_rezerv_2()
        with allure.step("Сохранение данных"):
            app.PO_Directions.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToDirectionsPage()
            app.PO_Directions.openDestination(directions)
            app.PO_Directions.openChanel('Основной')
            app.PO_Directions.openChanel('Резерв 1')
            app.PO_Directions.openChanel('Резерв 2')
            app.PO_Directions.openType_main('SMS Эгида')
            app.PO_Directions.openType_rezerv_1('SMS Эгида')
            app.PO_Directions.openType_rezerv_2('SMS Эгида')
            app.PO_Directions.enableChannelTesting_main()
            app.PO_Directions.enableChannelTesting_rezerv_1()
            app.PO_Directions.enableChannelTesting_rezerv_2()
        with allure.step("Проверка сохранения поля"):
            app.PO_Directions.assert_save_sms_egida_timetable_rezerv_2()
