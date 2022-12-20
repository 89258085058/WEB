# -*- coding: utf-8 -*-

import allure
import pytest

reruns = 1


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
@allure.feature("Проверки UI")
@pytest.mark.flaky(reruns=reruns)
class TestZonePathPathUI:

    @allure.story("РАЗДЕЛЫ")
    @allure.title("Проверка названий полей в окне Добавить раздел")
    def test_titles_add_path_modul(self, app, add_path, close_modal):
        with allure.step("Проверка названий полей"):
            app.PO_Zone_Path.text_add_path()

    # @allure.story("РАЗДЕЛЫ")
    # @allure.title("Проверка выпадающего списка: Управляющие разделы в окне Добавить раздел")
    # def test_dropdown_list_control_sections(self, app, add_path, close_modal):
    #     with allure.step("Проверка выбора позиций из выпадающего списка"):
    #         app.PO_Zone_Path.drop_list_controlled_sections()

    @allure.story("РАЗДЕЛЫ")
    @allure.title("Проверка чек-боксов в окне Добавить раздел")
    def test_add_path_check_box(self, app, add_path, close_modal):
        with allure.step("Проверка включения чекбоксов"):
            app.PO_Zone_Path.add_path_check_box_on()
        with allure.step("Проверка выключения чекбоксов"):
            app.PO_Zone_Path.add_path_check_box_off()
        with allure.step("Проверка частичного выбора чекбоксов"):
            app.PO_Zone_Path.add_path_check_box_some()

    @allure.story("РАЗДЕЛЫ")
    @allure.title("Проверка названий полей в окне Настройки раздела")
    def test_titles_settings_path_modul(self, app, settings_path, close_modal):
        with allure.step("Проверка названий полей"):
            app.PO_Zone_Path.text_add_path()

    # @allure.story("РАЗДЕЛЫ")
    # @allure.title("Проверка выпадающего списка: Управляющие разделы в окне Настройки раздела")
    # def test_settings_path_dropdown_list_control_sections(self, app, settings_path, close_modal):
    #     with allure.step("Проверка выбора позиций из выпадающего списка"):
    #         app.PO_Zone_Path.drop_list_controlled_sections()

    @allure.story("РАЗДЕЛЫ")
    @allure.title("Проверка чек-боксов в окне Настройки раздела")
    def test_settings_path_check_box(self, app, settings_path, close_modal):
        with allure.step("Проверка включения чекбоксов"):
            app.PO_Zone_Path.add_path_check_box_on()
        with allure.step("Проверка выключения чекбоксов"):
            app.PO_Zone_Path.add_path_check_box_off()
        with allure.step("Проверка частичного выбора чекбоксов"):
            app.PO_Zone_Path.add_path_check_box_some()

@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты ЗОНЫ/РАЗДЕЛЫ")
@allure.feature("Проверки UI")
@pytest.mark.flaky(reruns=reruns)
class TestZonePathOutsUI:

    @allure.story("ВЫХОДЫ")
    @allure.title("Проверка названий полей Режим работы: Выключен - Выходы - 1/2")
    def test_titles_outs_modul_off(self, app, outs):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Выключен")
        with allure.step("Проверка названий полей"):
            app.PO_Zone_Path.text_off_out()

    @allure.story("ВЫХОДЫ")
    @allure.title("Проверка названий полей Режим работы: Событийный -  Выходы - 1/2")
    def test_titles_outs_modul_event(self, app, outs):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Событийный")
        with allure.step("Проверка названий полей"):
            app.PO_Zone_Path.text_event_out()

    @allure.story("ВЫХОДЫ")
    @allure.title("Проверка названий полей Режим работы: Температурный -  Выходы - 1/2")
    def test_titles_outs_modul_temp(self, app, outs):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Температурный")
        with allure.step("Проверка названий полей"):
            app.PO_Zone_Path.text_temp_out()

    @allure.story("ВЫХОДЫ")
    @allure.title("Проверка названий полей Режим работы: Управляемый -  Выходы - 1/2")
    def test_titles_outs_modul_managed(self, app, outs):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Управляемый")
        with allure.step("Проверка названий полей"):
            app.PO_Zone_Path.text_managed_out()

    @allure.story("ВЫХОДЫ")
    @allure.title("Проверка переключения чек-боксов Режим работы: Событийный - Выходы - 1/2")
    def test_check_box_operating_mode_event(self, app, outs):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Событийный")
        # with allure.step("Раскрытие модуля: Список событий"):
        #     app_class.PO_Zone_Path.open_list_of_events()
        with allure.step("Проверка включения чекбоксов"):
            app.PO_Zone_Path.check_box_event_on()
        with allure.step("Проверка выключения чекбоксов"):
            app.PO_Zone_Path.check_box_event_off()
        with allure.step("Проверка частичного выбора чекбоксов"):
            app.PO_Zone_Path.check_box_event_some()

    @allure.story("ВЫХОДЫ")
    @allure.title("Проверка выбора событий Режим работы: Событийный - Выходы - 1/2")
    def test_event_selection_operating_mode_event(self, app, outs):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Событийный")
        # with allure.step("Раскрытие модуля: Список событий"):
        #     app_class.PO_Zone_Path.open_list_of_events()
        with allure.step("Проверка активации кнопки событий при клике"):
            app.PO_Zone_Path.check_event_selection_on()

    @allure.story("ВЫХОДЫ")
    @allure.title("Проверка отсутствия возможности внести настройки при деактивированном состоянии - Выходы - 1/2")
    def test_event_settings_operating_mode_event_disactivate(self, app, outs):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Событийный")
        # with allure.step("Раскрытие модуля: Список событий"):
        #     app_class.PO_Zone_Path.open_list_of_events()
        with allure.step("Выключение чекбоксов"):
            app.PO_Zone_Path.check_box_event_off()
        with allure.step("Проверка недоступности изменения настроек"):
            app.PO_Zone_Path.settings_outs_events_off()

    @allure.story("ВЫХОДЫ")
    @allure.title("Выход №1 Проверка настроек событий, Режим работы: Событийный - Взятие")
    def test_outputs_1_checking_event_settings_operating_mode_Event_Arming(self, app, outs):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Событийный")
        with allure.step("Проверка изменения настроек"):
            app.PO_Zone_Path.out_1_check_settings_take_on_event()

    @allure.story("ВЫХОДЫ")
    @allure.title("Выход №1 Проверка настроек событий, Режим работы: Событийный - Снятие")
    def test_outputs_1_checking_event_settings_operating_mode_Event_Arming_off(self, app, outs):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Событийный")
        with allure.step("Проверка изменения настроек"):
            app.PO_Zone_Path.out_1_check_settings_take_off_event()

    @allure.story("ВЫХОДЫ")
    @allure.title("Выход №1 Проверка настроек событий, Режим работы: Событийный - Принудительное взятие")
    def test_outputs_1_checking_event_settings_operating_mode_Event_forced_take(self, app, outs):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Событийный")
        with allure.step("Проверка изменения настроек"):
            app.PO_Zone_Path.out_1_check_settings_forced_take_event()

    @allure.story("ВЫХОДЫ")
    @allure.title("Выход №1 Проверка настроек событий, Режим работы: Событийный - Невзятие")
    def test_outputs_1_checking_event_settings_operating_mode_Event_not_taking(self, app, outs):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Событийный")
        with allure.step("Проверка изменения настроек"):
            app.PO_Zone_Path.out_1_check_settings_not_taking_event()

    @allure.story("ВЫХОДЫ")
    @allure.title("Выход №1 Проверка настроек событий, Режим работы: Событийный - Пожар")
    def test_outputs_1_checking_event_settings_operating_mode_Event_fire(self, app, outs):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Событийный")
        with allure.step("Проверка изменения настроек"):
            app.PO_Zone_Path.out_1_check_settings_fire_event()

    @allure.story("ВЫХОДЫ")
    @allure.title("Выход №1 Проверка настроек событий, Режим работы: Событийный - Тревога")
    def test_outputs_1_checking_event_settings_operating_mode_Event_alarm(self, app, outs):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Событийный")
        with allure.step("Проверка изменения настроек"):
            app.PO_Zone_Path.out_1_check_settings_alarm_event()

    @allure.story("ВЫХОДЫ")
    @allure.title("Выход №2 Проверка настроек событий, Режим работы: Событийный - Взятие")
    def test_outputs_2_checking_event_settings_operating_mode_Event_Arming(self, app, outs):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Событийный")
        with allure.step("Проверка изменения настроек"):
            app.PO_Zone_Path.out_2_check_settings_take_on_event()

    @allure.story("ВЫХОДЫ")
    @allure.title("Выход №2 Проверка настроек событий, Режим работы: Событийный - Снятие")
    def test_outputs_2_checking_event_settings_operating_mode_Event_Arming_off(self, app, outs):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Событийный")
        with allure.step("Проверка изменения настроек"):
            app.PO_Zone_Path.out_2_check_settings_take_off_event()

    @allure.story("ВЫХОДЫ")
    @allure.title("Выход №2 Проверка настроек событий, Режим работы: Событийный - Принудительное взятие")
    def test_outputs_2_checking_event_settings_operating_mode_Event_forced_take(self, app, outs):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Событийный")
        with allure.step("Проверка изменения настроек"):
            app.PO_Zone_Path.out_2_check_settings_forced_take_event()

    @allure.story("ВЫХОДЫ")
    @allure.title("Выход №2 Проверка настроек событий, Режим работы: Событийный - Невзятие")
    def test_outputs_2_checking_event_settings_operating_mode_Event_not_taking(self, app, outs):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Событийный")
        with allure.step("Проверка изменения настроек"):
            app.PO_Zone_Path.out_2_check_settings_not_taking_event()

    @allure.story("ВЫХОДЫ")
    @allure.title("Выход №2 Проверка настроек событий, Режим работы: Событийный - Пожар")
    def test_outputs_2_checking_event_settings_operating_mode_Event_fire(self, app, outs):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Событийный")
        with allure.step("Проверка изменения настроек"):
            app.PO_Zone_Path.out_2_check_settings_fire_event()

    @allure.story("ВЫХОДЫ")
    @allure.title("Выход №2 Проверка настроек событий, Режим работы: Событийный - Тревога")
    def test_outputs_2_checking_event_settings_operating_mode_Event_alarm(self, app, outs):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Событийный")
        with allure.step("Проверка изменения настроек"):
            app.PO_Zone_Path.out_2_check_settings_alarm_event()

    @allure.story("ВЫХОДЫ")
    @allure.title("Проверка переключения тумблера - 'Инверсия управления', Режим работы: Температурный - Выходы 1/2")
    def test_toggle_switch_check_control_inversion_operating_mode_temperature(self, app, outs):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Температурный")
        with allure.step("Проверка переключения тумблера выход 1"):
            app.PO_Zone_Path.checked_Inversion_of_control_out_1()
        with allure.step("Проверка переключения тумблера выход 2"):
            app.PO_Zone_Path.checked_Inversion_of_control_out_2()

    @allure.story("ВЫХОДЫ")
    @allure.title("Проверка настроек Маски включения Выход 1")
    def test_checking_the_settings_of_the_Enable_mask_output_1(self, app, outs):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Управляемый")
        with allure.step("Раскрытие модуля: Маска включения Выход 1"):
            app.PO_Zone_Path.open_mask_on_out_1()
        with allure.step("Проверка изменения настроек"):
            app.PO_Zone_Path.out_1_inclusion_mask()

    @allure.story("ВЫХОДЫ")
    @allure.title("Проверка настроек Маски выключения Выход 1")
    def test_checking_the_settings_of_the_shutdown_masks_output_1(self, app, outs):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Управляемый")
        with allure.step("Раскрытие модуля: Маска выключения Выход 1"):
            app.PO_Zone_Path.open_mask_off_out_1()
        with allure.step("Проверка изменения настроек"):
            app.PO_Zone_Path.out_2_inclusion_mask()

    @allure.story("ВЫХОДЫ")
    @allure.title("Проверка настроек Маски включения Выход 2")
    def test_checking_the_settings_of_the_Enable_mask_output_2(self, app, outs):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Управляемый")
        with allure.step("Раскрытие модуля: Маска включения Выход 2"):
            app.PO_Zone_Path.open_mask_on_out_2()
        with allure.step("Проверка изменения настроек"):
            app.PO_Zone_Path.settings_inclusion_masks_out_2_on()

    @allure.story("ВЫХОДЫ")
    @allure.title("Проверка настроек Маски выключения Выход 2")
    def test_checking_the_settings_of_the_shutdown_masks_output_2(self, app, outs):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Управляемый")
        with allure.step("Раскрытие модуля: Маска выключения Выход 2"):
            app.PO_Zone_Path.open_mask_off_out_2()
        with allure.step("Проверка изменения настроек"):
            app.PO_Zone_Path.settings_inclusion_masks_out_2_off()

    @allure.story("ВЫХОДЫ")
    @allure.title("Проверка переключение тумблеров Режим работы управляемый - Выходы 1/2")
    def test_manege_made_tumblers_check_outs(self, app, outs):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode("Управляемый")
        with allure.step("Проверка переключения тумблеров - Выходы 1"):
            app.PO_Zone_Path.tumblers_check_manege_mode_out_1()
        with allure.step("Проверка переключения тумблеров - Выходы 2"):
            app.PO_Zone_Path.tumblers_check_manege_mode_out_2()
