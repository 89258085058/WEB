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
def rele(app):
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
class TestSensorRele:

    @allure.story("РЕЛЕ")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Название'")
    def test_rele_name_input_positiv(self, app, rele, close_modal_sensor):
        with allure.step("Проверка валидации поля"):
            app.PO_Sensors.input_name_positiv()

    @allure.story("РЕЛЕ")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Название")
    def test_rele_name_input_negativ(self, app, rele, close_modal_sensor):
        with allure.step("Проверка валидации поля"):
            app.PO_Sensors.input_name_negativ()

    @allure.story("РЕЛЕ")
    @allure.title("Проверка названий полей Режим работы: Выключен - Выходы - 1/2")
    def test_rele_titles_outs_modul_off(self, app, rele, close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Выключен")
        with allure.step("Проверка названий полей"):
            app.PO_Sensors.text_off_indication_rele()

    @allure.story("РЕЛЕ")
    @allure.title("Проверка названий полей Режим работы: Событийный -  Выходы - 1/2")
    def test_rele_titles_outs_modul_event(self, app, rele, close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Событийный")
        with allure.step("Проверка названий полей"):
            app.PO_Sensors.text_event_indication_rele()

    @allure.story("РЕЛЕ")
    @allure.title("Проверка названий полей Режим работы: Температурный -  Выходы - 1/2")
    def test_rele_titles_outs_modul_temp(self, app, rele, close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Температурный")
        with allure.step("Проверка названий полей"):
            app.PO_Sensors.text_temp_indicationt_rele()

    @allure.story("РЕЛЕ")
    @allure.title("Проверка названий полей Режим работы: Управляемый -  Выходы - 1/2")
    def test_rele_titles_outs_modul_managed(self, app, rele, close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Управляемый")
        with allure.step("Проверка названий полей"):
            app.PO_Sensors.text_managed_indicationt_rele()

    @allure.story("РЕЛЕ")
    @allure.title("Проверка переключения чек-боксов Режим работы: Событийный - Выходы - 1/2")
    def test_rele_check_box_operating_mode_event(self, app, rele, close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Событийный")
        with allure.step("Проверка включения чекбоксов"):
            app.PO_Zone_Path.check_box_event_on()
        with allure.step("Проверка выключения чекбоксов"):
            app.PO_Zone_Path.check_box_event_off()
        with allure.step("Проверка частичного выбора чекбоксов"):
            app.PO_Zone_Path.check_box_event_some()

    @allure.story("РЕЛЕ")
    @allure.title("Проверка выбора событий Режим работы: Событийный - Выходы - 1/2")
    def test_rele_event_selection_operating_mode_event(self, app, rele, close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Событийный")
        with allure.step("Проверка активации кнопки событий при клике"):
            app.PO_Zone_Path.check_event_selection_on()

    @allure.story("РЕЛЕ")
    @allure.title("Проверка отсутствия возможности внести настройки при деактивированном состоянии - Выходы - 1/2")
    def test_rele_event_settings_operating_mode_event_disactivate(self, app, rele, close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Событийный")
        with allure.step("Выключение чекбоксов"):
            app.PO_Zone_Path.check_box_event_off()
        with allure.step("Проверка недоступности изменения настроек"):
            app.PO_Zone_Path.settings_outs_events_off()

    @allure.story("РЕЛЕ")
    @allure.title("Выход №1 Проверка настроек событий, Режим работы: Событийный - Взятие")
    def test_rele_outputs_1_checking_event_settings_operating_mode_Event_Arming(self, app, rele, close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Событийный")
        with allure.step("Проверка изменения настроек"):
            app.PO_Zone_Path.out_1_check_settings_take_on_event()

    @allure.story("РЕЛЕ")
    @allure.title("Выход №1 Проверка настроек событий, Режим работы: Событийный - Снятие")
    def test_rele_outputs_1_checking_event_settings_operating_mode_Event_Arming_off(self, app, rele,
                                                                                    close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Событийный")
        with allure.step("Проверка изменения настроек"):
            app.PO_Zone_Path.out_1_check_settings_take_off_event()


    @allure.story("РЕЛЕ")
    @allure.title("Выход №1 Проверка настроек событий, Режим работы: Событийный - Принудительное взятие")
    def test_rele_outputs_1_checking_event_settings_operating_mode_Event_forced_take(self, app, rele,
                                                                                     close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Событийный")
        with allure.step("Проверка изменения настроек"):
            app.PO_Zone_Path.out_1_check_settings_forced_take_event()

    @allure.story("РЕЛЕ")
    @allure.title("Выход №1 Проверка настроек событий, Режим работы: Событийный - Невзятие")
    def test_rele_outputs_1_checking_event_settings_operating_mode_Event_not_taking(self, app, rele,
                                                                                    close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Событийный")
        with allure.step("Проверка изменения настроек"):
            app.PO_Zone_Path.out_1_check_settings_not_taking_event()

    @allure.story("РЕЛЕ")
    @allure.title("Выход №1 Проверка настроек событий, Режим работы: Событийный - Пожар")
    def test_rele_outputs_1_checking_event_settings_operating_mode_Event_fire(self, app, rele, close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Событийный")
        with allure.step("Проверка изменения настроек"):
            app.PO_Zone_Path.out_1_check_settings_fire_event()

    @allure.story("РЕЛЕ")
    @allure.title("Выход №1 Проверка настроек событий, Режим работы: Событийный - Тревога")
    def test_rele_outputs_1_checking_event_settings_operating_mode_Event_alarm(self, app, rele, close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Событийный")
        with allure.step("Проверка изменения настроек"):
            app.PO_Zone_Path.out_1_check_settings_alarm_event()

    @allure.story("РЕЛЕ")
    @allure.title("Выход №2 Проверка настроек событий, Режим работы: Событийный - Взятие")
    def test_rele_outputs_2_checking_event_settings_operating_mode_Event_Arming(self, app, rele, close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Событийный")
        with allure.step("Проверка изменения настроек"):
            app.PO_Zone_Path.out_2_check_settings_take_on_event()

    @allure.story("РЕЛЕ")
    @allure.title("Выход №2 Проверка настроек событий, Режим работы: Событийный - Снятие")
    def test_rele_outputs_2_checking_event_settings_operating_mode_Event_Arming_off(self, app, rele,
                                                                                    close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Событийный")
        with allure.step("Проверка изменения настроек"):
            app.PO_Zone_Path.out_2_check_settings_take_off_event()

    @allure.story("РЕЛЕ")
    @allure.title("Выход №2 Проверка настроек событий, Режим работы: Событийный - Принудительное взятие")
    def test_rele_outputs_2_checking_event_settings_operating_mode_Event_forced_take(self, app, rele,
                                                                                     close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Событийный")
        with allure.step("Проверка изменения настроек"):
            app.PO_Zone_Path.out_2_check_settings_forced_take_event()

    @allure.story("РЕЛЕ")
    @allure.title("Выход №2 Проверка настроек событий, Режим работы: Событийный - Невзятие")
    def test_rele_outputs_2_checking_event_settings_operating_mode_Event_not_taking(self, app, rele,
                                                                                    close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Событийный")
        with allure.step("Проверка изменения настроек"):
            app.PO_Zone_Path.out_2_check_settings_not_taking_event()

    @allure.story("РЕЛЕ")
    @allure.title("Выход №2 Проверка настроек событий, Режим работы: Событийный - Пожар")
    def test_rele_outputs_2_checking_event_settings_operating_mode_Event_fire(self, app, rele, close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Событийный")
        with allure.step("Проверка изменения настроек"):
            app.PO_Zone_Path.out_2_check_settings_fire_event()

    @allure.story("РЕЛЕ")
    @allure.title("Выход №2 Проверка настроек событий, Режим работы: Событийный - Тревога")
    def test_rele_outputs_2_checking_event_settings_operating_mode_Event_alarm(self, app, rele, close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Событийный")
        with allure.step("Проверка изменения настроек"):
            app.PO_Zone_Path.out_2_check_settings_alarm_event()

    @allure.story("РЕЛЕ")
    @allure.title("Проверка переключения тумблера - 'Инверсия управления', Режим работы: Температурный - Выходы 1/2")
    def test_rele_toggle_switch_check_control_inversion_operating_mode_temperature(self, app, rele, close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Температурный")
        with allure.step("Проверка переключения тумблера выход 1"):
            app.PO_Zone_Path.checked_Inversion_of_control_out_1()
        with allure.step("Проверка переключения тумблера выход 2"):
            app.PO_Zone_Path.checked_Inversion_of_control_out_2()

    @allure.story("РЕЛЕ")
    @allure.title("Проверка настроек Маски включения Выход 1")
    def test_rele_checking_the_settings_of_the_Enable_mask_output_1(self, app, rele, close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Управляемый")
        with allure.step("Раскрытие модуля: Маска включения Выход 1"):
            app.PO_Zone_Path.open_mask_on_out_1()
        with allure.step("Проверка изменения настроек"):
            app.PO_Zone_Path.out_1_inclusion_mask()

    @allure.story("РЕЛЕ")
    @allure.title("Проверка настроек Маски выключения Выход 1")
    def test_rele_checking_the_settings_of_the_shutdown_masks_output_1(self, app, rele, close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Управляемый")
        with allure.step("Раскрытие модуля: Маска выключения Выход 1"):
            app.PO_Zone_Path.open_mask_off_out_1()
        with allure.step("Проверка изменения настроек"):
            app.PO_Zone_Path.out_2_inclusion_mask()

    @allure.story("РЕЛЕ")
    @allure.title("Проверка настроек Маски включения Выход 2")
    def test_rele_checking_the_settings_of_the_Enable_mask_output_2(self, app, rele, close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Управляемый")
        with allure.step("Раскрытие модуля: Маска включения Выход 2"):
            app.PO_Zone_Path.open_mask_on_out_2()
        with allure.step("Проверка изменения настроек"):
            app.PO_Zone_Path.settings_inclusion_masks_out_2_on()

    @allure.story("РЕЛЕ")
    @allure.title("Проверка настроек Маски выключения Выход 2")
    def test_rele_checking_the_settings_of_the_shutdown_masks_output_2(self, app, rele, close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Управляемый")
        with allure.step("Раскрытие модуля: Маска выключения Выход 2"):
            app.PO_Zone_Path.open_mask_off_out_2()
        with allure.step("Проверка изменения настроек"):
            app.PO_Zone_Path.settings_inclusion_masks_out_2_off()

    @allure.story("РЕЛЕ")
    @allure.title("Проверка переключение тумблеров Режим работы управляемый - Выходы 1/2")
    def test_rele_manege_made_tumblers_check_outs(self, app, rele, close_modal_sensor):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Управляемый")
        with allure.step("Проверка переключения тумблеров - Выходы 1"):
            app.PO_Zone_Path.tumblers_check_manege_mode_out_1()
        with allure.step("Проверка переключения тумблеров - Выходы 2"):
            app.PO_Zone_Path.tumblers_check_manege_mode_out_2()
