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
def serena(app):
    with allure.step("Переход на страницу Зоны Разделы"):
        app.PO_Navigations.goToZonePathPage()
    with allure.step("Переход на вкладку 'Реле и сирены'"):
        app.PO_Navigations.goToZonePathRelaySiren()
    with allure.step("Раскрытие настроек"):
        app.PO_Sensors.first_sensor_settings_button()
    # with allure.step("Включение датчика"):
    #     app.PO_Sensors.Serena_sensor_ON()

@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты ДАТЧИКИ")
@pytest.mark.flaky(reruns=reruns)
class TestSensorSerena:

    @allure.story("СИРЕНА")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Название'")
    def test_serena_name_input_positiv(self, app, serena, close_modal_sensor):
        with allure.step("Проверка валидации поля"):
            app.PO_Sensors.input_name_positiv()

    @allure.story("СИРЕНА")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Название")
    def test_serena_name_input_negativ(self, app, serena, close_modal_sensor):
        with allure.step("Проверка валидации поля"):
            app.PO_Sensors.input_name_negativ()

    @allure.story("СИРЕНА")
    @allure.title("Проверка выпадающего списка: Режим индикации")
    def test_serena_dropdown_list_indication_mode(self, app, serena, close_modal_sensor):
        with allure.step("Проверка выбора позиций из выпадающего списка"):
            app.PO_Sensors.dropdown_list_indication_mode()

    @allure.story("СИРЕНА")
    @allure.title("Проверка названий полей Режим работы: Выключен - Световая/Звуковая - индикации")
    def test_serena_titles_modul_off(self, app, serena, close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Sensors.select_working_mode("Выключен")
        with allure.step("Проверка названий полей"):
            app.PO_Sensors.text_off_indication()

    @allure.story("СИРЕНА")
    @allure.title("Проверка названий полей Режим работы: Событийный - Световая/Звуковая - индикации")
    def test_serena_titles_modul_event(self, app, serena, close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Sensors.select_working_mode("Событийный")
        with allure.step("Проверка названий полей"):
            app.PO_Sensors.text_event_indication()

    @allure.story("СИРЕНА")
    @allure.title("Проверка названий полей Режим работы: Температурный -  Световая/Звуковая - индикации")
    def test_serena_titles_modul_temp(self, app, serena, close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Sensors.select_working_mode("Температурный")
        with allure.step("Проверка названий полей"):
            app.PO_Sensors.text_temp_indicationt()

    @allure.story("СИРЕНА")
    @allure.title("Проверка названий полей Режим работы: Управляемый - Световая/Звуковая - индикации")
    def test_serena_titles_modul_managed(self, app, serena, close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Sensors.select_working_mode("Управляемый")
        with allure.step("Проверка названий полей"):
            app.PO_Sensors.text_managed_indicationt()

    @allure.story("СИРЕНА")
    @allure.title("Проверка переключения чек-боксов Режим работы: Событийный - Световая/Звуковая - индикации")
    def test_serena_check_box_operating_mode_event(self, app, serena, close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Sensors.select_working_mode("Событийный")
        with allure.step("Проверка включения чекбоксов"):
            app.PO_Zone_Path.check_box_event_on()
        with allure.step("Проверка выключения чекбоксов"):
            app.PO_Zone_Path.check_box_event_off()
        with allure.step("Проверка частичного выбора чекбоксов"):
            app.PO_Zone_Path.check_box_event_some()

    @allure.story("СИРЕНА")
    @allure.title("Проверка выбора событий Режим работы: Событийный - Световая/Звуковая - индикации")
    def test_serena_event_selection_operating_mode_event(self, app, serena, close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Sensors.select_working_mode("Событийный")
        with allure.step("Проверка активации кнопки событий при клике"):
            app.PO_Zone_Path.check_event_selection_on()

    @allure.story("СИРЕНА")
    @allure.title("Световая индикации - Проверка настроек событий, Режим работы: Событийный - Взятие")
    def test_light_indication_checking_event_settings_operating_mode_Event_Arming(self, app, serena,
                                                                                  close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Sensors.select_working_mode("Событийный")
        with allure.step("Проверка изменения настроек"):
            app.PO_Sensors.Light_check_settings_take_on_event()

    @allure.story("СИРЕНА")
    @allure.title("Световая индикации - Проверка настроек событий, Режим работы: Событийный - Снятие")
    def test_light_checking_event_settings_operating_mode_Event_Arming_off(self, app, serena, close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Sensors.select_working_mode("Событийный")
        with allure.step("Проверка изменения настроек"):
            app.PO_Sensors.Light_check_settings_take_off_event()

    @allure.story("СИРЕНА")
    @allure.title("Световая индикации - Проверка настроек событий, Режим работы: Событийный - Принудительное взятие")
    def test_light_checking_event_settings_operating_mode_Event_forced_take(self, app, serena, close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Sensors.select_working_mode("Событийный")
        with allure.step("Проверка изменения настроек"):
            app.PO_Sensors.Light_check_settings_forced_take_event()

    @allure.story("СИРЕНА")
    @allure.title("Световая индикации - Проверка настроек событий, Режим работы: Событийный - Невзятие")
    def test_light_checking_event_settings_operating_mode_Event_not_taking(self, app, serena, close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Sensors.select_working_mode("Событийный")
        with allure.step("Проверка изменения настроек"):
            app.PO_Sensors.Light_check_settings_not_taking_event()

    @allure.story("СИРЕНА")
    @allure.title("Световая индикации - Проверка настроек событий, Режим работы: Событийный - Пожар")
    def test_light_checking_event_settings_operating_mode_Event_fire(self, app, serena, close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Sensors.select_working_mode("Событийный")
        with allure.step("Проверка изменения настроек"):
            app.PO_Sensors.Light_check_settings_fire_event()

    @allure.story("СИРЕНА")
    @allure.title("Световая индикации - Проверка настроек событий, Режим работы: Событийный - Тревога")
    def test_volum_checking_event_settings_operating_mode_Event_alarm(self, app, serena, close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Sensors.select_working_mode("Событийный")
        with allure.step("Проверка изменения настроек"):
            app.PO_Sensors.Light_check_settings_alarm_event()

    @allure.story("СИРЕНА")
    @allure.title("Звуковая индикации - Проверка настроек событий, Режим работы: Событийный - Взятие")
    def test_volum_indication_checking_event_settings_operating_mode_Event_Arming(self, app, serena,
                                                                                  close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Sensors.select_working_mode("Событийный")
        with allure.step("Проверка изменения настроек"):
            app.PO_Sensors.Volum_check_settings_take_on_event()

    @allure.story("СИРЕНА")
    @allure.title("Звуковая индикации - Проверка настроек событий, Режим работы: Событийный - Снятие")
    def test_volum_checking_event_settings_operating_mode_Event_Arming_off(self, app, serena, close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Sensors.select_working_mode("Событийный")
        with allure.step("Проверка изменения настроек"):
            app.PO_Sensors.Volum_check_settings_take_off_event()

    @allure.story("СИРЕНА")
    @allure.title("Звуковая индикации - Проверка настроек событий, Режим работы: Событийный - Принудительное взятие")
    def test_volum_checking_event_settings_operating_mode_Event_forced_take(self, app, serena, close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Sensors.select_working_mode("Событийный")
        with allure.step("Проверка изменения настроек"):
            app.PO_Sensors.Volum_check_settings_forced_take_event()

    @allure.story("СИРЕНА")
    @allure.title("Звуковая индикации - Проверка настроек событий, Режим работы: Событийный - Невзятие")
    def test_volum_checking_event_settings_operating_mode_Event_not_taking(self, app, serena, close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Sensors.select_working_mode("Событийный")
        with allure.step("Проверка изменения настроек"):
            app.PO_Sensors.Volum_check_settings_not_taking_event()

    @allure.story("СИРЕНА")
    @allure.title("Звуковая индикации - Проверка настроек событий, Режим работы: Событийный - Пожар")
    def test_volum_checking_event_settings_operating_mode_Event_fire(self, app, serena, close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Sensors.select_working_mode("Событийный")
        with allure.step("Проверка изменения настроек"):
            app.PO_Sensors.Volum_check_settings_fire_event()

    @allure.story("СИРЕНА")
    @allure.title("Звуковая индикации - Проверка настроек событий, Режим работы: Событийный - Тревога")
    def test_volum_checking_event_settings_operating_mode_Event_alarm(self, app, serena, close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Sensors.select_working_mode("Событийный")
        with allure.step("Проверка изменения настроек"):
            app.PO_Sensors.Volum_check_settings_alarm_event()

    @allure.story("СИРЕНА")
    @allure.title(
        "Проверка переключения тумблера - 'Инверсия управления', Режим работы: Температурный - Световая/Звуковая - индикации")
    def test_serena_toggle_switch_check_control_inversion_operating_mode_temperature(self, app, serena,
                                                                                     close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Sensors.select_working_mode("Температурный")
        with allure.step("Проверка переключения тумблера Световая индикации"):
            app.PO_Sensors.checked_Inversion_of_control_light()
        with allure.step("Проверка переключения тумблера Звуковая индикации"):
            app.PO_Sensors.checked_Inversion_of_control_volum()

    @allure.story("СИРЕНА")
    @allure.title("Проверка настроек Маски включения Режим работы управляемый Световая индикации")
    def test_serena_checking_the_settings_ON_mask_light(self, app, serena, close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Sensors.select_working_mode("Управляемый")
        with allure.step("Раскрытие модуля: Маска включения Световая индикации"):
            app.PO_Sensors.open_mask_on_light()
        with allure.step("Проверка изменения настроек"):
            app.PO_Sensors.inclusion_mask_01()

    @allure.story("СИРЕНА")
    @allure.title("Проверка настроек Маски выключения Режим работы управляемый Световая индикации")
    def test_serena_checking_the_settings_OFF_mask_light(self, app, serena, close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Sensors.select_working_mode("Управляемый")
        with allure.step("Раскрытие модуля: Маска выключения Световая индикации"):
            app.PO_Sensors.open_mask_off_light()
        with allure.step("Проверка изменения настроек"):
            app.PO_Sensors.inclusion_mask_02()

    @allure.story("СИРЕНА")
    @allure.title("Проверка настроек Маски включения Режим работы управляемый Звуковая индикации")
    def test_serena_checking_the_settings_ON_mask_volum(self, app, serena, close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Sensors.select_working_mode("Управляемый")
        with allure.step("Раскрытие модуля: Маска включения Световая индикации"):
            app.PO_Sensors.open_mask_on_volum()
        with allure.step("Проверка изменения настроек"):
            app.PO_Sensors.inclusion_mask_on_2()

    @allure.story("СИРЕНА")
    @allure.title("Проверка настроек Маски выключения Режим работы управляемый Звуковая индикации")
    def test_serena_checking_the_settings_OFF_mask_volum(self, app, serena, close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Sensors.select_working_mode("Управляемый")
        with allure.step("Раскрытие модуля: Маска выключения Световая индикации"):
            app.PO_Sensors.open_mask_off_volum()
        with allure.step("Проверка изменения настроек"):
            app.PO_Sensors.inclusion_mask_04()

    @allure.story("СИРЕНА")
    @allure.title(
        "Проверка выпадающего списка 'Номер группы выходов' Режим работы управляемый - Световая/Звуковая - индикации")
    def test_serena_manege_made_drop_down_lists_num_group_outs(self, app, serena, close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Sensors.select_working_mode("Управляемый")
        with allure.step("Проверка выбора позиций из выпадающего списка Световая индикация"):
            app.PO_Sensors.drop_list_num_group_outs_1()
        with allure.step("Проверка выбора позиций из выпадающего списка Звуковая индикация"):
            app.PO_Sensors.drop_list_num_group_outs_2()

    @allure.story("СИРЕНА")
    @allure.title("Проверка переключение тумблеров Режим работы управляемый - Световая/Звуковая - индикации")
    def test_serena_manege_made_tumblers_check(self, app, serena, close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Sensors.select_working_mode("Управляемый")
        with allure.step("Проверка переключения тумблеров - Световая индикация"):
            app.PO_Sensors.tumblers_check_manege_mode_light_indication()
        with allure.step("Проверка переключения тумблеров - Звуковая индикация"):
            app.PO_Sensors.tumblers_check_manege_mode_volum_indication()
