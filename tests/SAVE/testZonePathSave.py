# -*- coding: utf-8 -*-

import allure
import pytest

reruns = 2

# outs_test_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']


outs_test_list = ['1']

@pytest.fixture()
def close_modal(request, app):
    def fin():
        app.PO_Zone_Path.cancel()

    request.addfinalizer(fin)


@pytest.fixture
def outs(app):
    with allure.step("Переход на страницу Зоны Разделы"):
        app.PO_Navigations.goToZonePathPage()
    with allure.step("Переход на вкладку 'Выходы'"):
        app.PO_Navigations.goToZonePathOuts()
    with allure.step("Клик по кнопке 'Редактировать'"):
        app.PO_Navigations.edit_button_click()


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


@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты ЗОНЫ/РАЗДЕЛЫ")
@allure.feature("Сохранение данных")
@pytest.mark.flaky(reruns=reruns)
class TestZonePathOutsSave:

    @allure.story("ВЫХОДЫ")
    @allure.title("Проверка сохранения наименования - ВЫХОД №1")
    def test_out_1_save_name(self, app, outs):
        with allure.step("Генерирование тестовых данных"):
            app.ganerate_data.createData()
        with allure.step("Внесение изменений в наименование выхода"):
            app.PO_Zone_Path.input_name_out_1_for_save()
        with allure.step("Сохранение данных"):
            app.PO_Zone_Path.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToZonePathPage()
            app.PO_Navigations.goToZonePathOuts()
            app.PO_Navigations.edit_button_click()
        with allure.step("Проверка сохраненных данных"):
            app.PO_Zone_Path.assert_input_name_out_1_for_save()

    @allure.story("ВЫХОДЫ")
    @allure.title("Проверка сохранения наименования - ВЫХОД №2")
    def test_out_2_save_name(self, app, outs):
        with allure.step("Генерирование тестовых данных"):
            app.ganerate_data.createData()
        with allure.step("Внесение изменений в наименование выхода"):
            app.PO_Zone_Path.input_name_out_2_for_save()
        with allure.step("Сохранение данных"):
            app.PO_Zone_Path.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToZonePathPage()
            app.PO_Navigations.goToZonePathOuts()
            app.PO_Navigations.edit_button_click()
        with allure.step("Проверка сохраненных данных"):
            app.PO_Zone_Path.assert_input_name_out_2_for_save()

    @allure.story("ВЫХОДЫ")
    @allure.title("Проверка сохранения выбора Режимов работы - ВЫХОД №1")
    @pytest.mark.parametrize("operating_mod",
                             [
                                 ('Выключен'),
                                 ('Событийный'),
                                 ('Управляемый')
                             ])
    def test_out_1_save_operating_mode(self, app, outs, operating_mod):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode_out_2('Выключен')
            app.PO_Zone_Path.select_working_mode_out_1(operating_mod)
        with allure.step("Сохранение данных"):
            app.PO_Zone_Path.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToZonePathPage()
            app.PO_Navigations.goToZonePathOuts()
            app.PO_Navigations.edit_button_click()
        with allure.step("Проверка сохраненных данных Выход №1"):
            app.PO_Zone_Path.assert_operating_mod_out_1(operating_mod)

    @allure.story("ВЫХОДЫ")
    @allure.title("Проверка сохранения выбора Режимов работы - ВЫХОД №1 - Температурный")
    def test_out_1_save_operating_mode_1(self, app, outs):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode_out_2('Выключен')
            app.PO_Zone_Path.select_working_mode_out_1_temp('Температурный')
        with allure.step("Сохранение данных"):
            app.PO_Zone_Path.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToZonePathPage()
            app.PO_Navigations.goToZonePathOuts()
            app.PO_Navigations.edit_button_click()
        with allure.step("Проверка сохраненных данных Выход №1"):
            app.PO_Zone_Path.assert_operating_mod_out_1_temp('Температурный')

    @allure.story("ВЫХОДЫ")
    @allure.title("Проверка сохранения выбора Режимов работы - ВЫХОД №2")
    @pytest.mark.parametrize("operating_mod",
                             [
                                 ('Выключен'),
                                 ('Событийный'),
                                 ('Управляемый')
                             ])
    def test_out_2_save_operating_mode(self, app, outs, operating_mod):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode_out_1('Выключен')
            app.PO_Zone_Path.select_working_mode_out_2(operating_mod)
        with allure.step("Сохранение данных"):
            app.PO_Zone_Path.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToZonePathPage()
            app.PO_Navigations.goToZonePathOuts()
            app.PO_Navigations.edit_button_click()
        with allure.step("Проверка сохраненных данных Выход №2"):
            app.PO_Zone_Path.assert_operating_mod_out_2(operating_mod)

    @allure.story("ВЫХОДЫ")
    @allure.title("Проверка сохранения выбора Режимов работы - ВЫХОД №2 - Температурный")
    def test_out_2_save_operating_mode_1(self, app, outs):
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode_out_1('Выключен')
            app.PO_Zone_Path.select_working_mode_out_2_temp('Температурный')
        with allure.step("Сохранение данных"):
            app.PO_Zone_Path.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToZonePathPage()
            app.PO_Navigations.goToZonePathOuts()
            app.PO_Navigations.edit_button_click()
        with allure.step("Проверка сохраненных данных Выход №2"):
            app.PO_Zone_Path.assert_operating_mod_out_2_temp('Температурный')

    @allure.story("ВЫХОДЫ")
    @allure.title("Проверка сохранения Режима работы - Событийный - ВЫХОД №1")
    @pytest.mark.parametrize("event",
                             [
                                 ('Взятие'),
                                 ('Снятие'),
                                 ('Принудительное взятие'),
                                 ('Невзятие'),
                                 ('Пожар'),
                                 ('Тревога')
                             ])
    def test_out_1_save_operating_mode_event(self, app, outs, event):
        with allure.step("Генерирование тестовых данных"):
            app.ganerate_data.createData()
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode_out_2('Выключен')
            app.PO_Zone_Path.select_working_mode_out_1('Событийный')
        with allure.step("Внесение изменений в настройки выхода"):
            app.PO_Zone_Path.save_out_1_data_event(event)
        with allure.step("Сохранение данных"):
            app.PO_Zone_Path.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToZonePathPage()
            app.PO_Navigations.goToZonePathOuts()
            app.PO_Navigations.edit_button_click()
        with allure.step("Проверка сохраненных данных"):
            app.PO_Zone_Path.assert_save_out_1_data_event(event)

    @allure.story("ВЫХОДЫ")
    @allure.title("Проверка сохранения Режима работы - Событийный - ВЫХОД №2")
    @pytest.mark.parametrize("event",
                             [
                                 ('Взятие'),
                                 ('Снятие'),
                                 ('Принудительное взятие'),
                                 ('Невзятие'),
                                 ('Пожар'),
                                 ('Тревога')
                             ])
    def test_out_2_save_operating_mode_event(self, app, outs, event):
        with allure.step("Генерирование тестовых данных"):
            app.ganerate_data.createData()
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode_out_1('Выключен')
            app.PO_Zone_Path.select_working_mode_out_2('Событийный')
        with allure.step("Внесение изменений в настройки выхода"):
            app.PO_Zone_Path.save_out_2_data_event(event)
        with allure.step("Сохранение данных"):
            app.PO_Zone_Path.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToZonePathPage()
            app.PO_Navigations.goToZonePathOuts()
            app.PO_Navigations.edit_button_click()
        with allure.step("Проверка сохраненных данных"):
            app.PO_Zone_Path.assert_save_out_2_data_event(event)

    @allure.story("ВЫХОДЫ")
    @allure.title("Проверка сохранения Режима работы - Температурный - ВЫХОД №1")
    def test_out_1_save_operating_mode_temp(self, app, outs):
        with allure.step("Генерирование тестовых данных"):
            app.ganerate_data.createData()
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode_out_1('Температурный')
            app.PO_Zone_Path.select_working_mode_out_2('Выключен')
        with allure.step("Внесение изменений в настройки выхода"):
            app.PO_Zone_Path.save_out_1_data_temp()
        with allure.step("Сохранение данных"):
            app.PO_Zone_Path.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToZonePathPage()
            app.PO_Navigations.goToZonePathOuts()
            app.PO_Navigations.edit_button_click()
        with allure.step("Проверка сохраненных данных"):
            app.PO_Zone_Path.assert_save_out_1_data_temp()

    @allure.story("ВЫХОДЫ")
    @allure.title("Проверка сохранения Режима работы - Температурный - ВЫХОД №2")
    def test_out_2_save_operating_mode_temp(self, app, outs):
        with allure.step("Генерирование тестовых данных"):
            app.ganerate_data.createData()
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode_out_2('Температурный')
            app.PO_Zone_Path.select_working_mode_out_1('Выключен')
        with allure.step("Внесение изменений в настройки выхода"):
            app.PO_Zone_Path.save_out_1_data_temp()
        with allure.step("Сохранение данных"):
            app.PO_Zone_Path.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToZonePathPage()
            app.PO_Navigations.goToZonePathOuts()
            app.PO_Navigations.edit_button_click()
        with allure.step("Проверка сохраненных данных"):
            app.PO_Zone_Path.assert_save_out_1_data_temp()

    @allure.story("ВЫХОДЫ")
    @allure.title("Проверка сохранения Режима работы - Управляемый - ВЫХОД №1")
    @pytest.mark.parametrize("Output_group_number", outs_test_list)
    def test_out_1_save_operating_mode_managed(self, app, outs, Output_group_number):
        with allure.step("Генерирование тестовых данных"):
            app.ganerate_data.createData()
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode_out_1('Управляемый')
            app.PO_Zone_Path.select_working_mode_out_2('Выключен')
        with allure.step("Раскрытие модуля: Маска включения Выход 1"):
            app.PO_Zone_Path.open_mask_on_out_1()
        with allure.step("Раскрытие модуля: Маска выключения Выход 1"):
            app.PO_Zone_Path.open_mask_off_out_1()
        with allure.step("Внесение изменений в настройки выхода"):
            app.PO_Zone_Path.save_out_1_data_managed(Output_group_number)
        with allure.step("Сохранение данных"):
            app.PO_Zone_Path.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToZonePathPage()
            app.PO_Navigations.goToZonePathOuts()
            app.PO_Navigations.edit_button_click()
            app.PO_Zone_Path.open_mask_on_out_1()
            app.PO_Zone_Path.open_mask_off_out_1()
        with allure.step("Проверка сохраненных данных"):
            app.PO_Zone_Path.assert_save_out_1_data_managed(Output_group_number)

    @allure.story("ВЫХОДЫ")
    @allure.title("Проверка сохранения Режима работы - Управляемый - ВЫХОД №2")
    @pytest.mark.parametrize("Output_group_number", outs_test_list)
    def test_out_2_save_operating_mode_managed(self, app, outs, Output_group_number):
        with allure.step("Генерирование тестовых данных"):
            app.ganerate_data.createData()
        with allure.step("Выбор режима работы"):
            app.PO_Zone_Path.select_working_mode_out_2('Управляемый')
            app.PO_Zone_Path.select_working_mode_out_1('Выключен')
        with allure.step("Раскрытие модуля: Маска включения Выход 2"):
            app.PO_Zone_Path.open_mask_on_out_1()
        with allure.step("Раскрытие модуля: Маска выключения Выход 2"):
            app.PO_Zone_Path.open_mask_off_out_1()
        with allure.step("Внесение изменений в настройки выхода"):
            app.PO_Zone_Path.save_out_2_data_managed(Output_group_number)
        with allure.step("Сохранение данных"):
            app.PO_Zone_Path.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToZonePathPage()
            app.PO_Navigations.goToZonePathOuts()
            app.PO_Navigations.edit_button_click()
            app.PO_Zone_Path.open_mask_on_out_1()
            app.PO_Zone_Path.open_mask_off_out_1()
        with allure.step("Проверка сохраненных данных"):
            app.PO_Zone_Path.assert_save_out_2_data_managed(Output_group_number)


@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты ЗОНЫ/РАЗДЕЛЫ")
@allure.feature("Сохранение данных")
@pytest.mark.flaky(reruns=reruns)
class TestZonePathOutsPATHSave:

    @allure.story("РАЗДЕЛЫ")
    @allure.title("Проверка сохранения настроек раздела")
    @pytest.mark.parametrize("tumbler_1, tumbler_2, tumbler_3,",
                             [
                                 ('ON', 'ON', 'ON'),
                                 ('OFF', 'OFF', 'OFF'),
                                 ('ON', 'OFF', 'OFF'),
                                 ('OFF', 'ON', 'OFF'),
                                 ('OFF', 'OFF', 'ON')
                             ])
    def test_path_save_data(self, app, settings_path, close_modal, tumbler_1, tumbler_2, tumbler_3):
        with allure.step("Генерирование тестовых данных"):
            app.ganerate_data.createData()
        with allure.step("Внесение изменений в настройках раздела"):
            app.PO_Zone_Path.input_path_data_for_save(tumbler_1, tumbler_2, tumbler_3)
        with allure.step("Сохранение данных"):
            app.PO_Zone_Path.save_button_settings_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToZonePathPage()
            app.PO_Navigations.goToPathPage()
        with allure.step("Проверка сохраненных данных в списке разделов на главной странице"):
            app.PO_Zone_Path.assert_input_path_for_save_on_page()
        with allure.step("Проверка сохраненных данных в настройках"):
            app.PO_Zone_Path.settings_first_path_button()
            app.PO_Zone_Path.assert_input_path_for_save_settings(tumbler_1, tumbler_2, tumbler_3)

    @allure.story("РАЗДЕЛЫ")
    @allure.title("Проверка добавления максимального количества разделов c данными по умолчанию")
    def test_path_add_max_path_1(self, app):
        with allure.step("Переход на страницу Зоны Разделы"):
            app.PO_Navigations.goToZonePathPage()
        with allure.step("Переход на вкладку 'Разделы'"):
            app.PO_Navigations.goToPathPage()
        with allure.step("Проверка добавления разделов"):
            app.PO_Zone_Path.assert_add_path_1()

    @allure.story("РАЗДЕЛЫ")
    @allure.title("Проверка добавления максимального количества разделов c заполнением данных")
    def test_path_add_max_path_2(self, app):
        with allure.step("Переход на страницу Зоны Разделы"):
            app.PO_Navigations.goToZonePathPage()
        with allure.step("Переход на вкладку 'Разделы'"):
            app.PO_Navigations.goToPathPage()
        with allure.step("Проверка добавления разделов"):
            app.PO_Zone_Path.assert_add_path_2()

    @allure.story("РАЗДЕЛЫ")
    @allure.title("Проверка всплывающей ошибки при добавлении максимального количества разделов")
    def test_path_add_max_error_window(self, app):
        with allure.step("Переход на страницу Зоны Разделы"):
            app.PO_Navigations.goToZonePathPage()
        with allure.step("Переход на вкладку 'Разделы'"):
            app.PO_Navigations.goToPathPage()
        with allure.step("Проверка всплывающей ошибки"):
            app.PO_Zone_Path.assert_error_window()
