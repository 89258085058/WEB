# -*- coding: utf-8 -*-
import time

import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from data.pages_text import *
from locators.sensors_locators import *


class SensorsHelper():

    def __init__(self, app):
        self.app = app

    # Проверка выпадающего списка Раздел
    def drop_list_path(self, locator):
        path_list = ['Раздел № 01', 'Раздел № 02', 'Раздел № 03', 'Раздел № 04', 'Раздел № 05', 'Раздел № 06',
                     'Раздел № 07', 'Раздел № 08', 'Раздел № 09', 'Раздел № 10', 'Раздел № 11', 'Раздел № 12',
                     'Раздел № 13', 'Раздел № 14', 'Раздел № 15', 'Раздел № 16']
        for i in path_list:
            self.app.method.selectDropdownListByName(locator, i)
            self.app.method.assertSelectionDropdownList(i, locator)

    # Проверка 63 positiv
    def input_all(self, locator):
        with allure.step("Проверка ввода цифр"):
            for i in range(10):
                self.app.method.assertEqual(i, i, locator)
        with allure.step("Проверка ввода латинских букв в нижнем регистре"):
            self.app.method.assertEqual('abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz', locator)
        with allure.step("Проверка ввода латинских букв в врхнем регистре"):
            self.app.method.assertEqual('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', locator)
        with allure.step("Проверка ввода Русских букв в нижнем регистре"):
            self.app.method.assertEqual("ёйцукенгшщзхъфыв", "ёйцукенгшщзхъфыв", locator)
            self.app.method.assertEqual("апролджэячсмитьбю", "апролджэячсмитьбю", locator)
        with allure.step("Проверка ввода Русских букв в верхнем регистре"):
            self.app.method.assertEqual("АПРОЛДЖЭЯЧСМИТЬБЮ", "АПРОЛДЖЭЯЧСМИТЬБЮ", locator)
            self.app.method.assertEqual("ЁЙЦУКЕНГШЩЗХЪФЫВ", "ЁЙЦУКЕНГШЩЗХЪФЫВ", locator)
        with allure.step("Проверка ввода спецсимполов"):
            self.app.method.assertEqual("!#$%&'()*+,-./:;<=>?@[]^_`{|}~", "!#$%&'()*+,-./:;<=>?@[]^_`{|}~", locator)
        with allure.step("Проверка ввода совместных значений"):
            self.app.method.assertEqual('123  АБВABC!@#', '123  АБВABC!@#', locator)
        with allure.step("Проверка ввода пробелов"):
            self.app.method.assertEqual('   ', '   ', locator)
            self.app.method.assertEqual('123     ', '123     ', locator)
            self.app.method.assertEqual('   123', '   123', locator)
            self.app.method.assertEqual('1 2 3', '1 2 3', locator)
        with allure.step("Проверка ввода дробного числа "):
            self.app.method.assertEqual('11.11', '11.11', locator)
            self.app.method.assertEqual('000.1', '000.1', locator)
            self.app.method.assertEqual('11,11', '11,11', locator)
            self.app.method.assertEqual('000,1', '000,1', locator)
        with allure.step("Проверка ввода пустого значения"):
            self.app.method.assertEqual('', '', locator)
        with allure.step("Проверка ввода отрицательного числа"):
            self.app.method.assertEqual('-1', '-1', locator)

    # Проверка ввода Код настройки
    def input_cod_posutiv(self, locator):
        with allure.step("Проверка ввода цифр"):
            for i in range(10):
                self.app.method.assertEqual(i, i, locator)
        with allure.step("Проверка ввода латинских букв в нижнем регистре"):
            self.app.method.assertEqual('abcdef', 'abcdef', locator)
        with allure.step("Проверка ввода латинских букв в врхнем регистре"):
            self.app.method.assertEqual('ABCDEF', 'abcdef', locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual('0', '0', locator)
            self.app.method.assertEqual('1', '1', locator)
            self.app.method.assertEqual('1' * 7, '1' * 7, locator)
            self.app.method.assertEqual('1' * 8, '1' * 8, locator)

    # Проверка ввода Код настройки
    def input_cod_negativ(self, locator):
        with allure.step("Проверка ввода цифр"):
            for i in range(10):
                self.app.method.assertEqual(i, i, locator)
        with allure.step("Проверка ввода латинских букв в нижнем регистре"):
            self.app.method.assertEqual('abcdefghijklmnopqrstuvwxyz', 'abcdef', locator)
        with allure.step("Проверка ввода латинских букв в врхнем регистре"):
            self.app.method.assertEqual('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdef', locator)
        with allure.step("Проверка ввода Русских букв в нижнем регистре"):
            self.app.method.assertEqual("ёйцукенгшщзхъфыв", "", locator)
            self.app.method.assertEqual("апролджэячсмитьбю", "", locator)
        with allure.step("Проверка ввода Русских букв в верхнем регистре"):
            self.app.method.assertEqual("АПРОЛДЖЭЯЧСМИТЬБЮ", "", locator)
            self.app.method.assertEqual("ЁЙЦУКЕНГШЩЗХЪФЫВ", "", locator)
        with allure.step("Проверка ввода спецсимполов"):
            self.app.method.assertEqual("!#$%&'()*+,-./:;<=>?@[]^_`{|}~", "", locator)
        with allure.step("Проверка ввода совместных значений"):
            self.app.method.assertEqual('123  АБВABCadb!@#', '123abcad', locator)
        with allure.step("Проверка ввода пробелов"):
            self.app.method.assertEqual('   ', '', locator)
            self.app.method.assertEqual('123     ', '123', locator)
            self.app.method.assertEqual('   123', '123', locator)
            self.app.method.assertEqual('1 2 3', '123', locator)
        with allure.step("Проверка ввода дробного числа "):
            self.app.method.assertEqual('11.11', '1111', locator)
            self.app.method.assertEqual('000.1', '1', locator)
            self.app.method.assertEqual('11,11', '1111', locator)
            self.app.method.assertEqual('000,1', '1', locator)
        with allure.step("Проверка ввода пустого значения"):
            self.app.method.assertEqual('', '', locator)
        with allure.step("Проверка ввода отрицательного числа"):
            self.app.method.assertEqual('-1', '1', locator)
        with allure.step("Проверка ввода очень большого числа"):
            self.app.method.assertEqual('1' * 1000, '1' * 8, locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual('1' * 9, '1' * 8, locator)

    # Клик по кнопке Настройки последняя
    def first_sensor_settings_button(self):
        with allure.step("Клик по кнопке Настройки"):
            time.sleep(0.3)
            self.app.method.click((By.XPATH, settings_button))

    # Клик по кнопке Настройки первая
    def sensor_settings_button(self):
        with allure.step("Клик по кнопке Настройки"):
            time.sleep(0.3)
            self.app.method.click((By.XPATH, settings_button_first))

    # Включение сирены
    def Serena_sensor_ON(self):
        with allure.step("Включение датчика"):
            self.app.method.checkBox("ON", sirena_main_click, sirena_main_status)

    # Проверка поля Название негатив
    def input_name_positiv(self, locator=name):
        self.input_all(locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual('1', '1', locator)
            self.app.method.assertEqual('1' * 62, '1' * 62, locator)
            self.app.method.assertEqual('1' * 63, '1' * 63, locator)

    # Проверка поля Название негатив
    def input_name_negativ(self, locator=name):
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual('1' * 64, '1' * 63, locator)

    # Выпадающий список: Режим светодиодов для охранных датчиков - Световая индикация
    def dropdown_list_indication_mode(self, button=indication_mode, possition=options):
        self.app.method.selectDropdownList(button, possition + '[1]')
        self.app.method.assertSelectionDropdownList('Авто', button)
        self.app.method.selectDropdownList(button, possition + '[2]')
        self.app.method.assertSelectionDropdownList('Всегда включен', button)
        self.app.method.selectDropdownList(button, possition + '[3]')
        self.app.method.assertSelectionDropdownList('Всегда выключен', button)

    # Выбор режима работы - ВЫХОД № 1/2
    def select_working_mode(self, position: str):
        with allure.step(f"Световая индикация - {position}"):
            self.app.method.Select_from_the_dropdown_list_by_name(button=Working_mode_out_1, position=position)
        with allure.step(f"Звуковая индикация - {position}"):
            self.app.method.Select_from_the_dropdown_list_by_name(button=Working_mode_out_2, position=position)

    # Проверка полей выходы - выключен
    def text_off_indication(self):
        with allure.step("Проверка названий полей Световая индикация"):
            self.app.method.assertTextOnPage(locator_out_1_text, data_serena_off_1)
        with allure.step("Проверка названий полей Звуковая индикация"):
            self.app.method.assertTextOnPage(locator_out_2_text, data_serena_off_2)

    # Проверка полей выходы - выключен
    def text_off_indication_rele(self):
        with allure.step("Проверка названий полей Световая индикация"):
            self.app.method.assertTextOnPage(locator_out_1_text, data_rele_off_1)
        with allure.step("Проверка названий полей Звуковая индикация"):
            self.app.method.assertTextOnPage(locator_out_2_text, data_rele_off_2)

    # Проверка полей выходы - Событийный
    def text_event_indication(self):
        with allure.step("Проверка названий полей Световая индикация"):
            self.app.method.assertTextOnPage(locator_out_1_text, data_serena_event_1)
        with allure.step("Проверка названий полей Звуковая индикация"):
            self.app.method.assertTextOnPage(locator_out_2_text, data_serena_event_2)

    # Проверка полей выходы - Событийный
    def text_event_indication_rele(self):
        with allure.step("Проверка названий полей Световая индикация"):
            self.app.method.assertTextOnPage(locator_out_1_text, data_rele_event_1)
        with allure.step("Проверка названий полей Звуковая индикация"):
            self.app.method.assertTextOnPage(locator_out_2_text, data_rele_event_2)

    # Проверка полей выходы - Температурный
    def text_temp_indicationt(self):
        with allure.step("Проверка названий полей Световая индикация"):
            self.app.method.assertTextOnPage(locator_out_1_text, data_serena_temp_1)
        with allure.step("Проверка названий полей Звуковая индикация"):
            self.app.method.assertTextOnPage(locator_out_2_text, data_serena_temp_2)

    # Проверка полей выходы - Температурный
    def text_temp_indicationt_rele(self):
        with allure.step("Проверка названий полей Световая индикация"):
            self.app.method.assertTextOnPage(locator_out_1_text, data_rele_temp_1)
        with allure.step("Проверка названий полей Звуковая индикация"):
            self.app.method.assertTextOnPage(locator_out_2_text, data_rele_temp_2)

    # Проверка полей выходы - Управляемый
    def text_managed_indicationt(self):
        with allure.step("Проверка названий полей Световая индикация"):
            self.app.method.assertTextOnPage(locator_out_1_text, data_serena_managed_1)
        with allure.step("Проверка названий полей Звуковая индикация"):
            self.app.method.assertTextOnPage(locator_out_2_text, data_serena_managed_2)

    # Проверка полей выходы - Управляемый
    def text_managed_indicationt_rele(self):
        with allure.step("Проверка названий полей Световая индикация"):
            self.app.method.assertTextOnPage(locator_out_1_text, data_rele_managed_1)
        with allure.step("Проверка названий полей Звуковая индикация"):
            self.app.method.assertTextOnPage(locator_out_2_text, data_rele_managed_2)

    # Световая индикация - Проверка настроек Взятие
    def Light_check_settings_take_on_event(self):
        with allure.step("Активация настроек"):
            self.check_button_activation(light_take_on_button)
            self.app.method.checkBox("ON", light_take_on_click, light_take_on_status)
            self.settings_light()

    # Световая индикация - Проверка настроек Снятие
    def Light_check_settings_take_off_event(self):
        with allure.step("Активация настроек"):
            self.check_button_activation(light_take_off_button)
            self.app.method.checkBox("ON", light_take_off_click, light_take_off_status)
            self.settings_light()

    # Световая индикация - Проверка настроек Принудительное взятие
    def Light_check_settings_forced_take_event(self):
        with allure.step("Активация настроек"):
            self.check_button_activation(light_forced_take_button)
            self.app.method.checkBox("ON", light_forced_take_click, light_forced_take_status)
            self.settings_light()

    # Световая индикация - Проверка настроек Невзятие
    def Light_check_settings_not_taking_event(self):
        with allure.step("Активация настроек"):
            self.check_button_activation(light_not_taking_button)
            self.app.method.checkBox("ON", light_not_taking_click, light_not_taking_status)
            self.settings_light()

    # Световая индикация - Проверка настроек Пожар
    def Light_check_settings_fire_event(self):
        with allure.step("Активация настроек"):
            self.check_button_activation(light_fire_button)
            self.app.method.checkBox("ON", light_fire_click, light_fire_status)
            self.settings_light()

    # Световая индикация - Проверка настроек Тревога
    def Light_check_settings_alarm_event(self):
        with allure.step("Активация настроек"):
            self.check_button_activation(light_alarm_button)
            self.app.method.checkBox("ON", light_alarm_click, light_alarm_status)
            self.settings_light()

    # Зыуковая индикация - Проверка настроек Взятие
    def Volum_check_settings_take_on_event(self):
        with allure.step("Активация настроек"):
            self.check_button_activation(volum_take_on_button)
            self.app.method.checkBox("ON", volum_take_on_click, volum_take_on_status)
            self.settings_volum()

    # Зыуковая индикация - Проверка настроек Снятие
    def Volum_check_settings_take_off_event(self):
        with allure.step("Активация настроек"):
            self.check_button_activation(volum_take_off_button)
            self.app.method.checkBox("ON", volum_take_off_click, volum_take_off_status)
            self.settings_volum()

    # Зыуковая индикация - Проверка настроек Принудительное взятие
    def Volum_check_settings_forced_take_event(self):
        with allure.step("Активация настроек"):
            self.check_button_activation(volum_forced_take_button)
            self.app.method.checkBox("ON", volum_forced_take_click, volum_forced_take_status)
            self.settings_volum()

    # Зыуковая индикация - Проверка настроек Невзятие
    def Volum_check_settings_not_taking_event(self):
        with allure.step("Активация настроек"):
            self.check_button_activation(volum_not_taking_button)
            self.app.method.checkBox("ON", volum_not_taking_click, volum_not_taking_status)
            self.settings_volum()

    # Зыуковая индикация - Проверка настроек Пожар
    def Volum_check_settings_fire_event(self):
        with allure.step("Активация настроек"):
            self.check_button_activation(volum_fire_button)
            self.app.method.checkBox("ON", volum_fire_click, volum_fire_status)
            self.settings_volum()

    # Зыуковая индикация - Проверка настроек Тревога
    def Volum_check_settings_alarm_event(self):
        with allure.step("Активация настроек"):
            self.check_button_activation(volum_alarm_button)
            self.app.method.checkBox("ON", volum_alarm_click, volum_alarm_status)
            self.settings_volum()

    # Проверка активации кнопки Выходы Режим работы: Событийный
    def check_button_activation(self, locator):
        with allure.step("Клик по кнопке"):
            self.app.method.click((By.XPATH, locator))
        with allure.step("Проверка активации кнопки"):
            self.app.method.status_outs_button((By.XPATH, locator))

    # Общий метод для проверки настроек световая индикация
    def settings_light(self):
        with allure.step("Проверка виджета ползунка"):
            self.widget_volum(widget_light)
        with allure.step("Проверка переключения тумблера - Включить по окончанию"):
            self.tumbler_check(off_end_tumbler_light_status, off_end_tumbler_light_click)
        with allure.step("Проверка выбора маски"):
            self.mask_light()
        with allure.step("Проверка ввода значений в поле код настройки"):
            self.input_cod_setting(code_setting_light)

    # Общий метод для проверки настроек Маски
    def settings_serena_mask(self):
        with allure.step("Проверка виджета ползунка"):
            self.widget_volum(widget_light)
        with allure.step("Проверка переключения тумблера - Включить по окончанию"):
            self.tumbler_check(off_end_tumbler_light_status, off_end_tumbler_light_click)
        with allure.step("Проверка выбора маски"):
            self.mask_light()
        with allure.step("Проверка ввода значений в поле код настройки"):
            self.input_cod_setting(code_setting_light)

    # Общий метод для проверки настроек Маски
    def settings_volumn_mask_on(self):
        with allure.step("Проверка виджета ползунка"):
            self.widget_volum(widget_light_mask)
        with allure.step("Проверка переключения тумблера - Включить по окончанию"):
            self.tumbler_check(off_end_tumbler_volum_status_mask_on, off_end_tumbler_volum_click_mask_on)
        with allure.step("Проверка выбора маски"):
            self.mask_volum_2()
        with allure.step("Проверка ввода значений в поле код настройки"):
            self.input_cod_setting(code_setting_out_mask_2_on)

    # Общий метод для проверки настроек Маски
    def settings_light_mask_on(self):
        with allure.step("Проверка виджета ползунка"):
            self.widget_volum(widget_light)
        with allure.step("Проверка переключения тумблера - Включить по окончанию"):
            self.tumbler_check(off_end_tumbler_light_status, off_end_tumbler_light_click)
        with allure.step("Проверка выбора маски"):
            self.mask_light()
        with allure.step("Проверка ввода значений в поле код настройки"):
            self.input_cod_setting(code_setting_light)

        # Общий метод для проверки настроек Маски

    def settings_light_mask_on_04(self):
        with allure.step("Проверка виджета ползунка"):
            self.widget_volum(widget_light_mask_2)
        with allure.step("Проверка переключения тумблера - Включить по окончанию"):
            self.tumbler_check(mask_settings_tumbler_volum_status_off, mask_settings_tumbler_volum_click_off)
        with allure.step("Проверка выбора маски"):
            self.mask_volum_66()
        with allure.step("Проверка ввода значений в поле код настройки"):
            self.input_cod_setting(code_setting_out_mask_2_off)

    # Общий метод для проверки настроек Маски

    def settings_light_mask_off(self):
        with allure.step("Проверка виджета ползунка"):
            self.widget_volum(widget_volum)
        with allure.step("Проверка переключения тумблера - Включить по окончанию"):
            self.tumbler_check(off_end_tumbler_volum_status, off_end_tumbler_volum_click)
        with allure.step("Проверка выбора маски"):
            self.mask_light_17()
        with allure.step("Проверка ввода значений в поле код настройки"):
            self.input_cod_setting(code_setting_volum)

    # Общий метод для проверки настроек звуковая индикация
    def settings_volum(self):
        with allure.step("Проверка виджета ползунка"):
            self.widget_volum(widget_volum)
        with allure.step("Проверка виджета ползунка"):
            self.widget_volum_2(widget_volum_volum)
        with allure.step("Проверка переключения тумблера - Включить по окончанию"):
            self.tumbler_check(off_end_tumbler_volum_status, off_end_tumbler_volum_click)
        with allure.step("Проверка переключения тумблера - Модуляция"):
            self.tumbler_check(modulation_tumbler_volum_status, modulation_tumbler_volum_click)
        with allure.step("Проверка выбора маски"):
            self.mask_volum()
        with allure.step("Проверка ввода значений в поле код настройки"):
            self.input_cod_setting(code_setting_volum)

    # Проверка виджета ползунка
    def widget_volum(self, locator):
        try:
            for i in range(1, 1023, 500):
                self.app.method.sliderWidget(i, locator)
                self.app.method.assertSliderWidget(i, locator)
        except Exception as exc:
            assert exc == TimeoutException, f"Ошибка виджета ползунка!\nНе найден локатор: '{locator}'"

    # Проверка виджета ползунка
    def widget_volum_2(self, locator):
        try:
            for i in range(1, 15, 5):
                self.app.method.sliderWidget(i, locator)
                self.app.method.assertSliderWidget(i, locator)
        except Exception as exc:
            assert exc == TimeoutException, f"Ошибка виджета ползунка!\nНе найден локатор: '{locator}'"

    # Проверка тумблера Включить по окончанию
    def tumbler_check(self, t_status, t_click):
        self.app.method.checkBox("ON", t_click, t_status)
        self.app.method.assertCheckBox("ON", t_status)
        self.app.method.checkBox("OFF", t_click, t_status)
        self.app.method.assertCheckBox("OFF", t_status)

    # Маска световая индикация
    def mask_light(self):
        try:
            for i in range(1, 17):
                self.app.method.checkBox("ON", (mask_settings_click + f"[{i}]"), (mask_settings_status + f"[{i}]"))
                self.app.method.assertCheckBox("ON", (mask_settings_status + f"[{i}]"))
            for i in range(1, 17):
                self.app.method.checkBox("OFF", (mask_settings_click + f"[{i}]"), (mask_settings_status + f"[{i}]"))
                self.app.method.assertCheckBox("OFF", (mask_settings_status + f"[{i}]"))
        except Exception as exc:
            assert exc == TimeoutException, f"Ошибка Выбора маски!\nНе найден локатор: '{mask_settings_click}' + index"

    # Маска световая индикация
    def mask_light_17(self):
        try:
            for i in range(17, 33):
                self.app.method.checkBox("ON", (mask_settings_click + f"[{i}]"), (mask_settings_status + f"[{i}]"))
                self.app.method.assertCheckBox("ON", (mask_settings_status + f"[{i}]"))
            for i in range(17, 33):
                self.app.method.checkBox("OFF", (mask_settings_click + f"[{i}]"), (mask_settings_status + f"[{i}]"))
                self.app.method.assertCheckBox("OFF", (mask_settings_status + f"[{i}]"))
        except Exception as exc:
            assert exc == TimeoutException, f"Ошибка Выбора маски!\nНе найден локатор: '{mask_settings_click}' + index"

    # Маска световая индикация
    def mask_volum_2(self):
        try:
            for i in range(33, 49):
                self.app.method.checkBox("ON", (mask_settings_click + f"[{i}]"), (mask_settings_status + f"[{i}]"))
                self.app.method.assertCheckBox("ON", (mask_settings_status + f"[{i}]"))
            for i in range(33, 49):
                self.app.method.checkBox("OFF", (mask_settings_click + f"[{i}]"), (mask_settings_status + f"[{i}]"))
                self.app.method.assertCheckBox("OFF", (mask_settings_status + f"[{i}]"))
        except Exception as exc:
            assert exc == TimeoutException, f"Ошибка Выбора маски!\nНе найден локатор: '{mask_settings_click}' + index"

    # Маска световая индикация
    def mask_volum_66(self):
        try:
            for i in range(49, 65):
                self.app.method.checkBox("ON", (mask_settings_click + f"[{i}]"), (mask_settings_status + f"[{i}]"))
                self.app.method.assertCheckBox("ON", (mask_settings_status + f"[{i}]"))
            for i in range(49, 65):
                self.app.method.checkBox("OFF", (mask_settings_click + f"[{i}]"), (mask_settings_status + f"[{i}]"))
                self.app.method.assertCheckBox("OFF", (mask_settings_status + f"[{i}]"))
        except Exception as exc:
            assert exc == TimeoutException, f"Ошибка Выбора маски!\nНе найден локатор: '{mask_settings_click}' + index"

    # Маска звуковая индикация
    def mask_volum(self):
        try:
            for i in range(17, 33):
                self.app.method.checkBox("ON", (mask_settings_click + f"[{i}]"), (mask_settings_status + f"[{i}]"))
                self.app.method.assertCheckBox("ON", (mask_settings_status + f"[{i}]"))
            for i in range(17, 33):
                self.app.method.checkBox("OFF", (mask_settings_click + f"[{i}]"), (mask_settings_status + f"[{i}]"))
                self.app.method.assertCheckBox("OFF", (mask_settings_status + f"[{i}]"))
        except Exception as exc:
            assert exc == TimeoutException, f"Ошибка Выбора маски!\nНе найден локатор: '{mask_settings_click}' + index"

    # Поле ввода Код настройки
    def input_cod_setting(self, locator):
        with allure.step("Позитивные проверки ввода"):
            self.input_cod_posutiv(locator)
        with allure.step("Негативные проверки ввода"):
            self.input_cod_negativ(locator)

    # переключения тумблера
    def checked_Inversion_of_control_light(self):
        self.tumbler_check(Inversion_of_control_tumbler_light_status, Inversion_of_control_tumbler_light_click)

    # переключения тумблера
    def checked_Inversion_of_control_volum(self):
        self.tumbler_check(Inversion_of_control_tumbler_volum_status, Inversion_of_control_tumbler_volum_click)

    # Раскрытие маска включения Световая индикация
    def open_mask_on_light(self):
        with allure.step("Раскрытие маска включения - Световая индикация"):
            self.app.method.click((By.XPATH, mask_on_settings_light))

    # Раскрытие маска включения Световая индикация
    def open_mask_off_light(self):
        with allure.step("Раскрытие маска включения - Световая индикация"):
            self.app.method.click((By.XPATH, mask_off_settings_light))

    # Раскрытие маска включения Звуковая индикация
    def open_mask_on_volum(self):
        with allure.step("Раскрытие маска включения  - Звуковая индикация"):
            self.app.method.click((By.XPATH, mask_on_settings_volum))

    # Раскрытие маска выключения Звуковая индикация
    def open_mask_off_volum(self):
        with allure.step("Раскрытие маска включения  - Звуковая индикация"):
            self.app.method.click((By.XPATH, mask_off_settings_volum))

    # Настройки маски
    def inclusion_mask_01(self):
        self.settings_light_mask_on()

    # Настройки маски
    def inclusion_mask_04(self):
        self.settings_light_mask_on_04()

    # Настройки маски
    def inclusion_mask_on_2(self):
        self.settings_volumn_mask_on()

    # Настройки маски
    def inclusion_mask_02(self):
        self.settings_light_mask_off()

    # Выпадающий список Номер группы выходов
    def drop_list_num_group_outs_1(self, button=num_group_outs_1, possition=options):
        for i in range(1, 11):
            time.sleep(0.1)
            self.app.method.selectDropdownList(button, possition + f'[{i}]')

            self.app.method.assertSelectionDropdownList(i, button)

    # Выпадающий список Номер группы выходов
    def drop_list_num_group_outs_2(self, button=num_group_outs_2, possition=options):
        for i in range(1, 11):
            time.sleep(0.1)
            self.app.method.selectDropdownList(button, possition + f'[{i}]')

            self.app.method.assertSelectionDropdownList(i, button)

    # Тумблеры Световая индикация
    def tumblers_check_manege_mode_light_indication(self):
        with allure.step("Проверка переключения тумблера - Разрешить управление по SMS"):
            self.tumbler_check(Allow_control_by_SMS_1_status, Allow_control_by_SMS_1_click)
        with allure.step("Проверка переключения тумблера - Разрешить управление звонком"):
            self.tumbler_check(Allow_call_control_1_status, Allow_call_control_1_click)
        with allure.step("Проверка переключения тумблера - Разрешить управление брелоком"):
            self.tumbler_check(Allow_key_control_1_status, Allow_key_control_1_click)

    # Тумблеры Звуковая индикация
    def tumblers_check_manege_mode_volum_indication(self):
        with allure.step("Проверка переключения тумблера - Разрешить управление по SMS"):
            self.tumbler_check(Allow_control_by_SMS_2_status, Allow_control_by_SMS_2_click)
        with allure.step("Проверка переключения тумблера - Разрешить управление звонком"):
            self.tumbler_check(Allow_call_control_2_status, Allow_call_control_2_click)
        with allure.step("Проверка переключения тумблера - Разрешить управление брелоком"):
            self.tumbler_check(Allow_key_control_2_status, Allow_key_control_2_click)

    # Проверка полей брелок
    def text_brelok_title(self):
        self.app.method.assertTextOnPage(modal_window, data_brelok)

    # Раскрытие Права управления
    def select_management_rights(self, name):
        self.app.method.click_element_locate(f'//*[@class="b-panel__header-text"][.="{name}"]')
        time.sleep(0.3)

    # Проверка чек-боксов брелка - включение
    def check_box_brelok_on(self):
        with allure.step("Включение датчика - ON"):
            self.app.method.checkBox("ON", brelock_senser_on_click, brelock_senser_on_status)
            self.app.method.assertCheckBox("ON", brelock_senser_on_status)
        with allure.step("Снятие - ON"):
            self.app.method.checkBox("ON", brelock_senser_off_click, brelock_senser_off_status)
            self.app.method.assertCheckBox("ON", brelock_senser_off_status)
        with allure.step("Взятие - ON"):
            self.app.method.checkBox("ON", brelock_senser_take_click, brelock_senser_take_status)
            self.app.method.assertCheckBox("ON", brelock_senser_take_status)
        with allure.step("Отключить сирену - ON"):
            self.app.method.checkBox("ON", brelock_senser_off_sirena_click, brelock_senser_off_sirena_status)
            self.app.method.assertCheckBox("ON", brelock_senser_off_sirena_status)

    # Проверка чек-боксов брелка - выключение
    def check_box_brelok_off(self):
        with allure.step("Включение датчика - OFF"):
            self.app.method.checkBox("OFF", brelock_senser_on_click, brelock_senser_on_status)
            self.app.method.assertCheckBox("OFF", brelock_senser_on_status)
        with allure.step("Снятие - OFF"):
            self.app.method.checkBox("OFF", brelock_senser_off_click, brelock_senser_off_status)
            self.app.method.assertCheckBox("OFF", brelock_senser_off_status)
        with allure.step("Взятие - OFF"):
            self.app.method.checkBox("OFF", brelock_senser_take_click, brelock_senser_take_status)
            self.app.method.assertCheckBox("OFF", brelock_senser_take_status)
        with allure.step("Отключить сирену - OFF"):
            self.app.method.checkBox("OFF", brelock_senser_off_sirena_click, brelock_senser_off_sirena_status)
            self.app.method.assertCheckBox("OFF", brelock_senser_off_sirena_status)

    # Проверка чек-боксов брелка - частичное включение
    def check_box_brelok_some(self):
        with allure.step("Включение датчика - ON"):
            self.app.method.checkBox("ON", brelock_senser_on_click, brelock_senser_on_status)
            self.app.method.assertCheckBox("ON", brelock_senser_on_status)
        with allure.step("Снятие - OFF"):
            self.app.method.checkBox("OFF", brelock_senser_off_click, brelock_senser_off_status)
            self.app.method.assertCheckBox("OFF", brelock_senser_off_status)
        with allure.step("Взятие - ON"):
            self.app.method.checkBox("ON", brelock_senser_take_click, brelock_senser_take_status)
            self.app.method.assertCheckBox("ON", brelock_senser_take_status)
        with allure.step("Отключить сирену - OFF"):
            self.app.method.checkBox("OFF", brelock_senser_off_sirena_click, brelock_senser_off_sirena_status)
            self.app.method.assertCheckBox("OFF", brelock_senser_off_sirena_status)
        with allure.step("Включение датчика - OFF"):
            self.app.method.checkBox("OFF", brelock_senser_on_click, brelock_senser_on_status)
            self.app.method.assertCheckBox("OFF", brelock_senser_on_status)
        with allure.step("Снятие - ON"):
            self.app.method.checkBox("ON", brelock_senser_off_click, brelock_senser_off_status)
            self.app.method.assertCheckBox("ON", brelock_senser_off_status)
        with allure.step("Взятие - OFF"):
            self.app.method.checkBox("OFF", brelock_senser_take_click, brelock_senser_take_status)
            self.app.method.assertCheckBox("OFF", brelock_senser_take_status)
        with allure.step("Отключить сирену - ON"):
            self.app.method.checkBox("ON", brelock_senser_off_sirena_click, brelock_senser_off_sirena_status)
            self.app.method.assertCheckBox("ON", brelock_senser_off_sirena_status)

    # Проверка выпадающего списка Пользователь
    def drop_list_user(self):
        self.app.method.selectDropdownListByName(brelok_DL_user, 'Администратор')
        self.app.method.assertSelectionDropdownList('Администратор', brelok_DL_user)

    # Проверка выпадающего списка Раздел
    def drop_list_path_brelok(self):
        self.drop_list_path(brelok_DL_path)

    # Проверка выпадающего списка Способ вызова тихой тревоги
    def drop_list_silent_alarm_method(self):
        list_data = ['Зажать на 3-10 сек', 'Зажать на 3 сек, нажать 1 раз']
        for i in list_data:
            self.app.method.selectDropdownListByName(brelok_DL_silent_alarm_method, i)
            self.app.method.assertSelectionDropdownList(i, brelok_DL_silent_alarm_method)

    # Проверка выпадающего списка Группа выходов кнопки 1
    def drop_list_button_output_group_1(self):
        list_data = ['Выкл.', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
        for i in list_data:
            self.app.method.selectDropdownListByName(brelok_DL_button_output_group_1, i)
            self.app.method.assertSelectionDropdownList(i, brelok_DL_button_output_group_1)

    # Проверка выпадающего списка Группа выходов кнопки 2
    def drop_list_button_output_group_2(self):
        list_data = ['Выкл.', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
        for i in list_data:
            self.app.method.selectDropdownListByName(brelok_DL_button_output_group_2, i)
            self.app.method.assertSelectionDropdownList(i, brelok_DL_button_output_group_2)

    # Проверка выпадающего списка Управляемые разделы
    def drop_list_path_with_check_box(self, button=brelok_controlled_sections, possition=positions_check_box):
        for i in range(9):
            self.app.method.selectDropdownListCheckBox(button, possition + f'[{i + 1}]',
                                                       status_drop_list_check_box + f'[{i + 1}]')
            self.app.method.assertSelectionDropdownListCheckBox('Раздел № 0' + str(i + 1), button)

        for i in range(9, 16):
            self.app.method.selectDropdownListCheckBox(button, possition + f'[{i + 1}]',
                                                       status_drop_list_check_box + f'[{i + 1}]')
            self.app.method.assertSelectionDropdownListCheckBox('Раздел № ' + str(i + 1), button)

    # Метод сохранения настроек брелка
    def save_data_brelok(self):
        _brelok = self.app.read_data.data_brelok()
        with allure.step(f"Выбор чекбокса Включение датчика: - {_brelok['brelok_CB_sensor_on']}"):
            self.app.method.checkBox(_brelok['brelok_CB_sensor_on'], brelock_senser_on_click,
                                     brelock_senser_on_status)
        with allure.step(f"Поле Название ввод: '{_brelok['brelok_name']}'"):
            self.app.method.inputValues(_brelok['brelok_name'], name)
        with allure.step(f"Выпадающий список - 'Пользователь' выбор позиции: 'Администратор'"):
            self.app.method.selectDropdownListByName(brelok_DL_user, 'Администратор')
        with allure.step(f"Выпадающий список - 'Раздел' выбор позиции: {_brelok['brelok_path']}"):
            self.app.method.selectDropdownListByName(brelok_DL_path, _brelok['brelok_path'])
        with allure.step(f"Выпадающий список - 'Управляемые разделы' выбор позиции: {_brelok['brelok_pathList_1']}"):
            path = _brelok['brelok_pathList_1']
            self.app.method.close_cross(brelok_controlled_sections)
            self.app.method.click((By.XPATH, f'/html/body//div[@class="b-multiselect-item"]/span[.="{path}"]'))
            self.app.method.click((By.XPATH, brelok_controlled_sections))
        with allure.step(f"Выпадающий список - 'Способ вызова тихой тревоги' выбор позиции:"
                         f" {_brelok['brelok_silent_larm_method']}"):
            self.app.method.selectDropdownListByName(brelok_DL_silent_alarm_method,
                                                     _brelok['brelok_silent_larm_method'])
        with allure.step(
                f"Выпадающий список - 'Группа выходов кнопки 1' выбор позиции: {_brelok['brelok_button_output_group_1']}"):
            self.app.method.selectDropdownListByName(brelok_DL_button_output_group_1,
                                                     _brelok['brelok_button_output_group_1'])
        with allure.step(
                f"Выпадающий список - 'Группа выходов кнопки 2' выбор позиции: {_brelok['brelok_button_output_group_2']}"):
            self.app.method.selectDropdownListByName(brelok_DL_button_output_group_2,
                                                     _brelok['brelok_button_output_group_2'])
        with allure.step(f"Выбор чекбокса Снятие: - {_brelok['brelok_CB_take_off']}"):
            self.app.method.checkBox(_brelok['brelok_CB_take_off'], brelock_senser_off_click, brelock_senser_off_status)
        with allure.step(f"Выбор чекбокса Взятие: - {_brelok['brelok_CB_take_on']}"):
            self.app.method.checkBox(_brelok['brelok_CB_take_on'], brelock_senser_take_click,
                                     brelock_senser_take_status)
        with allure.step(f"Выбор чекбокса Отключить сирену: - {_brelok['brelok_CB_sirena_off']}"):
            self.app.method.checkBox(_brelok['brelok_CB_sirena_off'], brelock_senser_off_sirena_click,
                                     brelock_senser_off_sirena_status)

    # Метод проверки сохранения настроек брелка
    def assert_save_data_brelok(self):
        _brelok = self.app.read_data.data_brelok()
        with allure.step(
                f"Проверка выбора чекбокса Включение датчика: - ожидаемое положение: {_brelok['brelok_CB_sensor_on']}"):
            self.app.method.assertCheckBox(_brelok['brelok_CB_sensor_on'], brelock_senser_on_status)
        with allure.step(f"Проверка поля Название ожидаемое значение: '{_brelok['brelok_name']}'"):
            self.app.method.assertValues(_brelok['brelok_name'], name)
        with allure.step(f"Проверка выпадающего списка - 'Пользователь' ожидаемое значение: 'Администратор'"):
            self.app.method.assertSelectionDropdownList('Администратор', brelok_DL_user)
        with allure.step(f"Проверка выпадающего списка  - 'Раздел' ожидаемое значение: {_brelok['brelok_path']}"):
            self.app.method.assertSelectionDropdownList(_brelok['brelok_path'], brelok_DL_path)
        with allure.step(
                f"Проверка выпадающего списка  - 'Управляемые разделы' ожидаемое значение: {_brelok['brelok_pathList_1']}"):
            self.app.method.assertSelectionDropdownList(_brelok['brelok_pathList_1'], brelok_controlled_sections)
        with allure.step(f"Проверка выпадающего списка  - 'Способ вызова тихой тревоги' ожидаемое значение:"
                         f" {_brelok['brelok_silent_larm_method']}"):
            self.app.method.assertSelectionDropdownList(_brelok['brelok_silent_larm_method'],
                                                        brelok_DL_silent_alarm_method)
        with allure.step(
                f"Проверка выпадающего списка - 'Группа выходов кнопки 1' ожидаемое значение: {_brelok['brelok_button_output_group_1']}"):
            self.app.method.assertSelectionDropdownList(_brelok['brelok_button_output_group_1'],
                                                        brelok_DL_button_output_group_1)
        with allure.step(
                f"Проверка выпадающего списка - 'Группа выходов кнопки 2' ожидаемое значение: {_brelok['brelok_button_output_group_2']}"):
            self.app.method.assertSelectionDropdownList(_brelok['brelok_button_output_group_2'],
                                                        brelok_DL_button_output_group_2)
        with allure.step(f"Проверка выбора чекбокса Снятие: - ожидаемое положение: {_brelok['brelok_CB_take_off']}"):
            self.app.method.assertCheckBox(_brelok['brelok_CB_take_off'], brelock_senser_off_status)
        with allure.step(f"Проверка выбора чекбокса Взятие: - ожидаемое положение: {_brelok['brelok_CB_take_on']}"):
            self.app.method.assertCheckBox(_brelok['brelok_CB_take_on'], brelock_senser_take_status)
        with allure.step(
                f"Проверка выбора чекбокса Отключить сирену: - ожидаемое положение: {_brelok['brelok_CB_sirena_off']}"):
            self.app.method.assertCheckBox(_brelok['brelok_CB_sirena_off'], brelock_senser_off_sirena_status)

    # Проверка полей c2000p_ik
    def text_c2000p_ik_title(self):
        self.app.method.assertTextOnPage(modal_window, data_c_2000p_ik)

    # Проверка полей c2000p_ik
    def text_c2000p_smk_title(self):
        self.app.method.assertTextOnPage(modal_window, data_c_2000p_smk)

    # Проверка полей c2000p_sdvig
    def text_c2000p_sdvig_title(self):
        self.app.method.assertTextOnPage(modal_window, data_c_2000p_sdvig)

    # Проверка полей c2000p_irp
    def text_c2000p_irp_title(self):
        self.app.method.assertTextOnPage(modal_window, data_c_2000p_irp)

    # Проверка полей c2000p_irp
    def text_c2000p_dip_title(self):
        self.app.method.assertTextOnPage(modal_window, data_c_2000p_dip)

    # Проверка полей c2000p_ip
    def text_c2000p_ip_title(self):
        self.app.method.assertTextOnPage(modal_window, data_c_2000p_ip)

    # Проверка полей c2000p_irp
    def text_sensor_kc_title(self):
        self.app.method.assertTextOnPage(modal_window, data_sensor_kc)

    # Проверка полей c2000p_ik
    def text_c2000p_ik_widget(self):
        wd = self.app.wd
        widget = wd.find_element(By.XPATH, '//*[@id="modalSettings"]//div[@class="b-range-slider"]')

    # Проверка чек-боксов - c_2000p
    def check_box_c_2000p_on(self):
        with allure.step("Включение датчика - ON"):
            self.app.method.checkBox("ON", c_2000p_senser_on_click, c_2000p_senser_on_status)
            self.app.method.assertCheckBox("ON", c_2000p_senser_on_status)
        with allure.step("Режим 'Колокольчик' - ON"):
            self.app.method.checkBox("ON", c_2000p_bell_mode_click, c_2000p_bell_mode_status)
            self.app.method.assertCheckBox("ON", c_2000p_bell_mode_status)
        with allure.step("Энергосберегающий режим - ON"):
            self.app.method.checkBox("ON", c_2000p_energy_saving_mode_click, c_2000p_energy_saving_mode_status)
            self.app.method.assertCheckBox("ON", c_2000p_energy_saving_mode_status)
        with allure.step("Режим тестирования - ON"):
            self.app.method.checkBox("ON", c_2000p_power_mode_click, c_2000p_power_mode_status)
            self.app.method.assertCheckBox("ON", c_2000p_power_mode_status)

    # Проверка чек-боксов - c_2000p
    def check_box_c_2000p_off(self):
        with allure.step("Включение датчика - OFF"):
            self.app.method.checkBox("OFF", c_2000p_senser_on_click, c_2000p_senser_on_status)
            self.app.method.assertCheckBox("OFF", c_2000p_senser_on_status)
        with allure.step("Режим 'Колокольчик' - OFF"):
            self.app.method.checkBox("OFF", c_2000p_bell_mode_click, c_2000p_bell_mode_status)
            self.app.method.assertCheckBox("OFF", c_2000p_bell_mode_status)
        with allure.step("Энергосберегающий режим - OFF"):
            self.app.method.checkBox("OFF", c_2000p_energy_saving_mode_click, c_2000p_energy_saving_mode_status)
            self.app.method.assertCheckBox("OFF", c_2000p_energy_saving_mode_status)
        with allure.step("Режим тестирования - OFF"):
            self.app.method.checkBox("OFF", c_2000p_power_mode_click, c_2000p_power_mode_status)
            self.app.method.assertCheckBox("OFF", c_2000p_power_mode_status)

    # Проверка чек-боксов - c_2000p
    def check_box_c_2000p_some(self):
        with allure.step("Включение датчика - ON"):
            self.app.method.checkBox("ON", c_2000p_senser_on_click, c_2000p_senser_on_status)
            self.app.method.assertCheckBox("ON", c_2000p_senser_on_status)
        with allure.step("Режим 'Колокольчик' - OFF"):
            self.app.method.checkBox("OFF", c_2000p_bell_mode_click, c_2000p_bell_mode_status)
            self.app.method.assertCheckBox("OFF", c_2000p_bell_mode_status)
        with allure.step("Энергосберегающий режим - ON"):
            self.app.method.checkBox("ON", c_2000p_energy_saving_mode_click, c_2000p_energy_saving_mode_status)
            self.app.method.assertCheckBox("ON", c_2000p_energy_saving_mode_status)
        with allure.step("Режим тестирования - OFF"):
            self.app.method.checkBox("OFF", c_2000p_power_mode_click, c_2000p_power_mode_status)
            self.app.method.assertCheckBox("OFF", c_2000p_power_mode_status)
        with allure.step("Включение датчика - OFF"):
            self.app.method.checkBox("OFF", c_2000p_senser_on_click, c_2000p_senser_on_status)
            self.app.method.assertCheckBox("OFF", c_2000p_senser_on_status)
        with allure.step("Режим 'Колокольчик' - ON"):
            self.app.method.checkBox("ON", c_2000p_bell_mode_click, c_2000p_bell_mode_status)
            self.app.method.assertCheckBox("ON", c_2000p_bell_mode_status)
        with allure.step("Энергосберегающий режим - OFF"):
            self.app.method.checkBox("OFF", c_2000p_energy_saving_mode_click, c_2000p_energy_saving_mode_status)
            self.app.method.assertCheckBox("OFF", c_2000p_energy_saving_mode_status)
        with allure.step("Режим тестирования - ON"):
            self.app.method.checkBox("ON", c_2000p_power_mode_click, c_2000p_power_mode_status)
            self.app.method.assertCheckBox("ON", c_2000p_power_mode_status)

    # Проверка выпадающего списка c_2000p
    def drop_list_path_c_2000p(self):
        self.drop_list_path(c_2000p_DL_path)

    # Проверка выпадающего списка Режим индикации
    def drop_list_indication_mode_c_2000p(self):
        path_list = ['Автоматический режим индикации', 'Индикация включена', 'Индикация выключена',
                     'Мигание по маске, согласно протоколу ДПЛС']
        for i in path_list:
            self.app.method.selectDropdownListByName(c_2000p_DL_indication_mod, i)
            self.app.method.assertSelectionDropdownList(i, c_2000p_DL_indication_mod)

    # Проверка виджета ползунка c_2000p
    def widget_slider_sensitivity_c_2000p(self, locator=c_2000p_widget_sensitivity):
        try:
            for i in range(1, 255, 100):
                self.app.method.sliderWidgetExit(i, locator)
                self.app.method.assertSliderWidget(i, locator)
        except Exception as exc:
            assert exc == TimeoutException, f"Ошибка виджета ползунка!\nНе найден локатор: '{locator}'"

    # Виджет ползунок
    def sliderWidgetExit(self, volum, identifier):
        from selenium.webdriver import ActionChains, Keys
        wd = self.app.wd
        slider = wd.find_element(By.XPATH, identifier)
        actions = ActionChains(wd)
        actions.move_to_element(slider)
        actions.click(slider)
        for i in range(255):
            actions.key_down(Keys.LEFT)
        for i in range(int(volum)):
            actions.key_down(Keys.RIGHT)
        actions.perform()

    # Метод сохранения настроек c_2000p
    def save_data_c_2000p_ik(self):
        _c_2000p_ik = self.app.read_data.data_c_2000p_ik()
        with allure.step(f"Выбор чекбокса Включение датчика: - {_c_2000p_ik['c_2000p_ik_CB_sensor_on']}"):
            self.app.method.checkBox(_c_2000p_ik['c_2000p_ik_CB_sensor_on'], c_2000p_senser_on_click,
                                     c_2000p_senser_on_status)
        with allure.step(f"Поле Название ввод: '{_c_2000p_ik['c_2000p_ik_name']}'"):
            self.app.method.inputValues(_c_2000p_ik['c_2000p_ik_name'], name)
        with allure.step(f"Выпадающий список - 'Раздел' выбор позиции: {_c_2000p_ik['c_2000p_ik_path']}"):
            self.app.method.selectDropdownListByName(c_2000p_DL_path, _c_2000p_ik['c_2000p_ik_path'])
        with allure.step(
                f"Выпадающий список - 'Режим индикации' выбор позиции: {_c_2000p_ik['c_2000p_ik_display_mode']}"):
            self.app.method.selectDropdownListByName(c_2000p_DL_indication_mod, _c_2000p_ik['c_2000p_ik_display_mode'])
        with allure.step(f"Выбор чекбокса Режим 'Колокольчик': - {_c_2000p_ik['c_2000p_ik_CB_bell_mode']}"):
            self.app.method.checkBox(_c_2000p_ik['c_2000p_ik_CB_bell_mode'], c_2000p_bell_mode_click,
                                     c_2000p_bell_mode_status)
        with allure.step(
                f"Выбор чекбокса Энергосберегающий режим: - {_c_2000p_ik['c_2000p_ik_CB_energy_saving_mode']}"):
            self.app.method.checkBox(_c_2000p_ik['c_2000p_ik_CB_energy_saving_mode'], c_2000p_energy_saving_mode_click,
                                     c_2000p_energy_saving_mode_status)
        with allure.step(f"Выбор чекбокса Режим тестирования: - {_c_2000p_ik['c_2000p_ik_CB_test_mode']}"):
            self.app.method.checkBox(_c_2000p_ik['c_2000p_ik_CB_test_mode'], c_2000p_power_mode_click,
                                     c_2000p_power_mode_status)
        with allure.step(f"Выбор виджета ползунка Чувствительность: - {_c_2000p_ik['c_2000p_ik_W_Sensitivity']}"):
            self.sliderWidgetExit(_c_2000p_ik['c_2000p_ik_W_Sensitivity'], c_2000p_widget_sensitivity)

    # Метод проверки сохранения настроек c_2000p
    def assert_save_data_c_2000p_ik(self):
        _c_2000p_ik = self.app.read_data.data_c_2000p_ik()
        with allure.step(
                f"Проверка выбора чекбокса Включение датчика ожидаемое положение: - {_c_2000p_ik['c_2000p_ik_CB_sensor_on']}"):
            self.app.method.assertCheckBox(_c_2000p_ik['c_2000p_ik_CB_sensor_on'], c_2000p_senser_on_status)
        with allure.step(f"Проверка поля Название ожидаемое значение: '{_c_2000p_ik['c_2000p_ik_name']}'"):
            self.app.method.assertValues(_c_2000p_ik['c_2000p_ik_name'], name)
        with allure.step(
                f"Проверка выпадающего списка - 'Раздел' ожидаемое положение: {_c_2000p_ik['c_2000p_ik_path']}"):
            self.app.method.assertSelectionDropdownList(_c_2000p_ik['c_2000p_ik_path'], c_2000p_DL_path)
        with allure.step(
                f"Проверка выпадающего списка - 'Режим индикации' ожидаемое положение: {_c_2000p_ik['c_2000p_ik_display_mode']}"):
            self.app.method.assertSelectionDropdownList(_c_2000p_ik['c_2000p_ik_display_mode'],
                                                        c_2000p_DL_indication_mod)
        with allure.step(
                f"Проверка выбора чекбокса Режим 'Колокольчик' ожидаемое положение: - {_c_2000p_ik['c_2000p_ik_CB_bell_mode']}"):
            self.app.method.assertCheckBox(_c_2000p_ik['c_2000p_ik_CB_bell_mode'], c_2000p_bell_mode_status)
        with allure.step(
                f"Проверка выбора чекбокса Энергосберегающий режим ожидаемое положение: - {_c_2000p_ik['c_2000p_ik_CB_energy_saving_mode']}"):
            self.app.method.assertCheckBox(_c_2000p_ik['c_2000p_ik_CB_energy_saving_mode'],
                                           c_2000p_energy_saving_mode_status)
        with allure.step(
                f"Проверка выбора чекбокса Режим тестирования ожидаемое положение: - {_c_2000p_ik['c_2000p_ik_CB_test_mode']}"):
            self.app.method.assertCheckBox(_c_2000p_ik['c_2000p_ik_CB_test_mode'], c_2000p_power_mode_status)
        with allure.step(
                f"Проверка выбора виджета ползунка Чувствительность ожидаемое положение: - {_c_2000p_ik['c_2000p_ik_W_Sensitivity']}"):
            self.app.method.assertSliderWidget(_c_2000p_ik['c_2000p_ik_W_Sensitivity'], c_2000p_widget_sensitivity)

    # Проверка чек-боксов - c_2000p СМК
    def check_box_c_2000p_smk_on(self):
        with allure.step("Включение датчика - ON"):
            self.app.method.checkBox("ON", c_2000p_senser_on_click, c_2000p_senser_on_status)
            self.app.method.assertCheckBox("ON", c_2000p_senser_on_status)
        with allure.step("Режим 'Колокольчик' - ON"):
            self.app.method.checkBox("ON", c_2000p_bell_mode_click, c_2000p_bell_mode_status)
            self.app.method.assertCheckBox("ON", c_2000p_bell_mode_status)
        with allure.step('Включение режима "Антисаботаж" - ON'):
            self.app.method.checkBox("ON", c_2000p_smk_enabling_the_anti_sabotage_click,
                                     c_2000p_smk_enabling_the_anti_sabotage_status)
            self.app.method.assertCheckBox("ON", c_2000p_smk_enabling_the_anti_sabotage_status)

    # Проверка чек-боксов - c_2000p СМК
    def check_box_c_2000p_smk_off(self):
        with allure.step("Включение датчика - OFF"):
            self.app.method.checkBox("OFF", c_2000p_senser_on_click, c_2000p_senser_on_status)
            self.app.method.assertCheckBox("OFF", c_2000p_senser_on_status)
        with allure.step("Режим 'Колокольчик' - OFF"):
            self.app.method.checkBox("OFF", c_2000p_bell_mode_click, c_2000p_bell_mode_status)
            self.app.method.assertCheckBox("OFF", c_2000p_bell_mode_status)
        with allure.step('Включение режима "Антисаботаж" - OFF'):
            self.app.method.checkBox("OFF", c_2000p_smk_enabling_the_anti_sabotage_click,
                                     c_2000p_smk_enabling_the_anti_sabotage_status)
            self.app.method.assertCheckBox("OFF", c_2000p_smk_enabling_the_anti_sabotage_status)

    # Проверка чек-боксов - c_2000p СМК
    def check_box_c_2000p_smk_some(self):
        with allure.step("Включение датчика - OFF"):
            self.app.method.checkBox("OFF", c_2000p_senser_on_click, c_2000p_senser_on_status)
            self.app.method.assertCheckBox("OFF", c_2000p_senser_on_status)
        with allure.step("Режим 'Колокольчик' - ON"):
            self.app.method.checkBox("ON", c_2000p_bell_mode_click, c_2000p_bell_mode_status)
            self.app.method.assertCheckBox("ON", c_2000p_bell_mode_status)
        with allure.step('Включение режима "Антисаботаж" - OFF'):
            self.app.method.checkBox("OFF", c_2000p_smk_enabling_the_anti_sabotage_click,
                                     c_2000p_smk_enabling_the_anti_sabotage_status)
            self.app.method.assertCheckBox("OFF", c_2000p_smk_enabling_the_anti_sabotage_status)
        with allure.step("Включение датчика - ON"):
            self.app.method.checkBox("ON", c_2000p_senser_on_click, c_2000p_senser_on_status)
            self.app.method.assertCheckBox("ON", c_2000p_senser_on_status)
        with allure.step("Режим 'Колокольчик' - OFF"):
            self.app.method.checkBox("OFF", c_2000p_bell_mode_click, c_2000p_bell_mode_status)
            self.app.method.assertCheckBox("OFF", c_2000p_bell_mode_status)
        with allure.step('Включение режима "Антисаботаж" - ON'):
            self.app.method.checkBox("ON", c_2000p_smk_enabling_the_anti_sabotage_click,
                                     c_2000p_smk_enabling_the_anti_sabotage_status)
            self.app.method.assertCheckBox("ON", c_2000p_smk_enabling_the_anti_sabotage_status)

    # Проверка выпадающего списка c_2000p СМК
    def drop_list_path_c_2000p_smk(self):
        self.drop_list_path(c_2000p_DL_path)

    # Проверка выпадающего списка c_2000p СДВИГ
    def drop_list_path_c_2000p_sdvig(self):
        self.drop_list_path(c_2000p_DL_path)

    # Проверка выпадающего списка Режим индикации СМК
    def drop_list_indication_mode_c_2000p_smk(self):
        path_list = ['Автоматический режим индикации', 'Индикация включена', 'Индикация выключена',
                     'Мигание по маске, согласно протоколу ДПЛС']
        for i in path_list:
            self.app.method.selectDropdownListByName(c_2000p_DL_indication_mod, i)
            self.app.method.assertSelectionDropdownList(i, c_2000p_DL_indication_mod)

    # Проверка выпадающего списка Включаемые модули СМК
    def drop_list_included_modules_c_2000p_smk(self):
        path_list = ['Герконы', 'Шлейф', 'Геркон и шлейф']
        for i in path_list:
            self.app.method.selectDropdownListByName(c_2000p_DL_included_modules, i)
            self.app.method.assertSelectionDropdownList(i, c_2000p_DL_included_modules)

    # Метод сохранения настроек c_2000p СМК
    def save_data_c_2000p_smk(self):
        _c_2000p_smk = self.app.read_data.data_c_2000p_smk()
        with allure.step(f"Выбор чекбокса Включение датчика: - {_c_2000p_smk['c_2000p_smk_CB_sensor_on']}"):
            self.app.method.checkBox(_c_2000p_smk['c_2000p_smk_CB_sensor_on'], c_2000p_senser_on_click,
                                     c_2000p_senser_on_status)
        with allure.step(f"Поле Название ввод: '{_c_2000p_smk['c_2000p_smk_name']}'"):
            self.app.method.inputValues(_c_2000p_smk['c_2000p_smk_name'], name)
        with allure.step(f"Выпадающий список - 'Раздел' выбор позиции: {_c_2000p_smk['c_2000p_smk_path']}"):
            self.app.method.selectDropdownListByName(c_2000p_DL_path, _c_2000p_smk['c_2000p_smk_path'])
        with allure.step(
                f"Выпадающий список - 'Режим индикации' выбор позиции: {_c_2000p_smk['c_2000p_smk_display_mode']}"):
            self.app.method.selectDropdownListByName(c_2000p_DL_indication_mod,
                                                     _c_2000p_smk['c_2000p_smk_display_mode'])

        with allure.step(f"Выбор чекбокса Режим 'Колокольчик': - {_c_2000p_smk['c_2000p_smk__CB_bell_mode']}"):
            self.app.method.checkBox(_c_2000p_smk['c_2000p_smk__CB_bell_mode'], c_2000p_bell_mode_click,
                                     c_2000p_bell_mode_status)
        with allure.step(
                f"Выбор чекбокса Включение режима 'Антисаботаж': - {_c_2000p_smk['c_2000p_smk_CB_enabling_the_Anti_sabotage_mode']}"):
            self.app.method.checkBox(_c_2000p_smk['c_2000p_smk_CB_enabling_the_Anti_sabotage_mode'],
                                     c_2000p_smk_enabling_the_anti_sabotage_click,
                                     c_2000p_smk_enabling_the_anti_sabotage_status)
        with allure.step(
                f"Выпадающий список - 'Включаемые модули' выбор позиции: {_c_2000p_smk['c_2000p_smk_W_Sensitivity']}"):
            self.app.method.selectDropdownListByName(c_2000p_DL_included_modules,
                                                     _c_2000p_smk['c_2000p_smk_W_Sensitivity'])

    # Метод проверки сохранения настроек c_2000p СМК
    def assert_save_data_c_2000p_smk(self):
        _c_2000p_smk = self.app.read_data.data_c_2000p_smk()
        with allure.step(
                f"Проверка выбора чекбокса Включение датчика ожидаемое положение: - {_c_2000p_smk['c_2000p_smk_CB_sensor_on']}"):
            self.app.method.assertCheckBox(_c_2000p_smk['c_2000p_smk_CB_sensor_on'], c_2000p_senser_on_status)
        with allure.step(f"Проверка поля Название ожидаемое значение: '{_c_2000p_smk['c_2000p_smk_name']}'"):
            self.app.method.assertValues(_c_2000p_smk['c_2000p_smk_name'], name)
        with allure.step(
                f"Проверка выпадающего списка - 'Раздел' ожидаемое положение: {_c_2000p_smk['c_2000p_smk_path']}"):
            self.app.method.assertSelectionDropdownList(_c_2000p_smk['c_2000p_smk_path'], c_2000p_DL_path)
        with allure.step(
                f"Проверка выпадающего списка - 'Режим индикации' ожидаемое положение: {_c_2000p_smk['c_2000p_smk_display_mode']}"):
            self.app.method.assertSelectionDropdownList(_c_2000p_smk['c_2000p_smk_display_mode'],
                                                        c_2000p_DL_indication_mod)
        with allure.step(
                f"Проверка выбора чекбокса Режим 'Колокольчик' ожидаемое положение: - {_c_2000p_smk['c_2000p_smk__CB_bell_mode']}"):
            self.app.method.assertCheckBox(_c_2000p_smk['c_2000p_smk__CB_bell_mode'], c_2000p_bell_mode_status)
        with allure.step(
                f"Проверка выбора чекбокса Включение режима 'Антисаботаж' ожидаемое положение: - {_c_2000p_smk['c_2000p_smk_CB_enabling_the_Anti_sabotage_mode']}"):
            self.app.method.assertCheckBox(_c_2000p_smk['c_2000p_smk_CB_enabling_the_Anti_sabotage_mode'],
                                           c_2000p_smk_enabling_the_anti_sabotage_status)
        with allure.step(
                f"Проверка выпадающего списка - 'Включаемые модули' ожидаемое положение: {_c_2000p_smk['c_2000p_smk_W_Sensitivity']}"):
            self.app.method.assertSelectionDropdownList(_c_2000p_smk['c_2000p_smk_W_Sensitivity'],
                                                        c_2000p_DL_included_modules)

    # Проверка чек-боксов - c_2000p ИРП
    def check_box_c_2000p_irp_on(self):
        with allure.step("Включение датчика - ON"):
            self.app.method.checkBox("ON", c_2000p_senser_on_click, c_2000p_senser_on_status)
            self.app.method.assertCheckBox("ON", c_2000p_senser_on_status)
        with allure.step("Режим 'Колокольчик' - ON"):
            self.app.method.checkBox("ON", c_2000p_bell_mode_click, c_2000p_bell_mode_status)
            self.app.method.assertCheckBox("ON", c_2000p_bell_mode_status)

    # Проверка чек-боксов - c_2000p ИРП
    def check_box_c_2000p_irp_off(self):
        with allure.step("Включение датчика - OFF"):
            self.app.method.checkBox("OFF", c_2000p_senser_on_click, c_2000p_senser_on_status)
            self.app.method.assertCheckBox("OFF", c_2000p_senser_on_status)
        with allure.step("Режим 'Колокольчик' - OFF"):
            self.app.method.checkBox("OFF", c_2000p_bell_mode_click, c_2000p_bell_mode_status)
            self.app.method.assertCheckBox("OFF", c_2000p_bell_mode_status)

    # Проверка чек-боксов - c_2000p ИРП
    def check_box_c_2000p_irp_some(self):
        with allure.step("Включение датчика - OFF"):
            self.app.method.checkBox("OFF", c_2000p_senser_on_click, c_2000p_senser_on_status)
            self.app.method.assertCheckBox("OFF", c_2000p_senser_on_status)
        with allure.step("Режим 'Колокольчик' - ON"):
            self.app.method.checkBox("ON", c_2000p_bell_mode_click, c_2000p_bell_mode_status)
            self.app.method.assertCheckBox("ON", c_2000p_bell_mode_status)
        with allure.step("Включение датчика - ON"):
            self.app.method.checkBox("ON", c_2000p_senser_on_click, c_2000p_senser_on_status)
            self.app.method.assertCheckBox("ON", c_2000p_senser_on_status)
        with allure.step("Режим 'Колокольчик' - OFF"):
            self.app.method.checkBox("OFF", c_2000p_bell_mode_click, c_2000p_bell_mode_status)
            self.app.method.assertCheckBox("OFF", c_2000p_bell_mode_status)

    # Проверка выпадающего списка c_2000p ИРП
    def drop_list_path_c_2000p_irp(self):
        self.drop_list_path(c_2000p_DL_path)

    # Проверка выпадающего списка c_2000p ИП
    def drop_list_path_c_2000p_ip(self):
        self.drop_list_path(c_2000p_DL_path)

    # Проверка выпадающего списка КЦ Сигнал-GSM
    def drop_list_path_sensor_kc(self):
        self.drop_list_path(kc_DL_path)

    # Проверка выпадающего списка Режим индикации ИРП
    def drop_list_indication_mode_c_2000p_irp(self):
        path_list = ['Автоматический режим индикации', 'Индикация включена', 'Индикация выключена',
                     'Мигание по маске, согласно протоколу ДПЛС']
        for i in path_list:
            self.app.method.selectDropdownListByName(c_2000p_DL_indication_mod, i)
            self.app.method.assertSelectionDropdownList(i, c_2000p_DL_indication_mod)

    # Проверка выпадающего списка Режим индикации ИП
    def drop_list_indication_mode_c_2000p_ip(self):
        path_list = ['Автоматический режим индикации', 'Индикация включена', 'Индикация выключена',
                     'Мигание по маске, согласно протоколу ДПЛС']
        for i in path_list:
            self.app.method.selectDropdownListByName(c_2000p_DL_indication_mod, i)
            self.app.method.assertSelectionDropdownList(i, c_2000p_DL_indication_mod)

    # Проверка выпадающего списка Режим уведомлений ИП
    def drop_list_notification_mode_c_2000p_ip(self):
        path_list = ['Без уведомлений', 'Только по снижению', 'Только по повышению', 'По снижению и повышению']
        for i in path_list:
            self.app.method.selectDropdownListByName(c_2000p_DL_notification_mod, i)
            self.app.method.assertSelectionDropdownList(i, c_2000p_DL_notification_mod)

    # Метод сохранения настроек c_2000p ИРП
    def save_data_c_2000p_irp(self):
        _c_2000p_smk = self.app.read_data.data_c_2000p_smk()
        with allure.step(f"Выбор чекбокса Включение датчика: - {_c_2000p_smk['c_2000p_smk_CB_sensor_on']}"):
            self.app.method.checkBox(_c_2000p_smk['c_2000p_smk_CB_sensor_on'], c_2000p_senser_on_click,
                                     c_2000p_senser_on_status)
        with allure.step(f"Поле Название ввод: '{_c_2000p_smk['c_2000p_smk_name']}'"):
            self.app.method.inputValues(_c_2000p_smk['c_2000p_smk_name'], name)
        with allure.step(f"Выпадающий список - 'Раздел' выбор позиции: {_c_2000p_smk['c_2000p_smk_path']}"):
            self.app.method.selectDropdownListByName(c_2000p_DL_path, _c_2000p_smk['c_2000p_smk_path'])
        with allure.step(
                f"Выпадающий список - 'Режим индикации' выбор позиции: {_c_2000p_smk['c_2000p_smk_display_mode']}"):
            self.app.method.selectDropdownListByName(c_2000p_DL_indication_mod,
                                                     _c_2000p_smk['c_2000p_smk_display_mode'])

        with allure.step(f"Выбор чекбокса Режим 'Колокольчик': - {_c_2000p_smk['c_2000p_smk__CB_bell_mode']}"):
            self.app.method.checkBox(_c_2000p_smk['c_2000p_smk__CB_bell_mode'], c_2000p_bell_mode_click,
                                     c_2000p_bell_mode_status)

    # Метод проверки сохранения настроек c_2000p ИРП
    def assert_save_data_c_2000p_irp(self):
        _c_2000p_smk = self.app.read_data.data_c_2000p_smk()
        with allure.step(
                f"Проверка выбора чекбокса Включение датчика ожидаемое положение: - {_c_2000p_smk['c_2000p_smk_CB_sensor_on']}"):
            self.app.method.assertCheckBox(_c_2000p_smk['c_2000p_smk_CB_sensor_on'], c_2000p_senser_on_status)
        with allure.step(f"Проверка поля Название ожидаемое значение: '{_c_2000p_smk['c_2000p_smk_name']}'"):
            self.app.method.assertValues(_c_2000p_smk['c_2000p_smk_name'], name)
        with allure.step(
                f"Проверка выпадающего списка - 'Раздел' ожидаемое положение: {_c_2000p_smk['c_2000p_smk_path']}"):
            self.app.method.assertSelectionDropdownList(_c_2000p_smk['c_2000p_smk_path'], c_2000p_DL_path)
        with allure.step(
                f"Проверка выпадающего списка - 'Режим индикации' ожидаемое положение: {_c_2000p_smk['c_2000p_smk_display_mode']}"):
            self.app.method.assertSelectionDropdownList(_c_2000p_smk['c_2000p_smk_display_mode'],
                                                        c_2000p_DL_indication_mod)
        with allure.step(
                f"Проверка выбора чекбокса Режим 'Колокольчик' ожидаемое положение: - {_c_2000p_smk['c_2000p_smk__CB_bell_mode']}"):
            self.app.method.assertCheckBox(_c_2000p_smk['c_2000p_smk__CB_bell_mode'], c_2000p_bell_mode_status)

    # Проверка чек-боксов - КЦ Сигнал-GSM
    def check_box_sensor_kc_on(self):
        with allure.step("Включение датчика - ON"):
            self.app.method.checkBox("ON", c_2000p_senser_on_click, c_2000p_senser_on_status)
            self.app.method.assertCheckBox("ON", c_2000p_senser_on_status)
        with allure.step("Режим 'Колокольчик' - ON"):
            self.app.method.checkBox("ON", c_2000p_bell_mode_click, c_2000p_bell_mode_status)
            self.app.method.assertCheckBox("ON", c_2000p_bell_mode_status)

    # Проверка чек-боксов - КЦ Сигнал-GSM
    def check_box_sensor_kc_off(self):
        with allure.step("Включение датчика - OFF"):
            self.app.method.checkBox("OFF", c_2000p_senser_on_click, c_2000p_senser_on_status)
            self.app.method.assertCheckBox("OFF", c_2000p_senser_on_status)
        with allure.step("Режим 'Колокольчик' - OFF"):
            self.app.method.checkBox("OFF", c_2000p_bell_mode_click, c_2000p_bell_mode_status)
            self.app.method.assertCheckBox("OFF", c_2000p_bell_mode_status)

    # Проверка чек-боксов - КЦ Сигнал-GSM
    def check_box_sensor_kc_some(self):
        with allure.step("Включение датчика - OFF"):
            self.app.method.checkBox("OFF", c_2000p_senser_on_click, c_2000p_senser_on_status)
            self.app.method.assertCheckBox("OFF", c_2000p_senser_on_status)
        with allure.step("Режим 'Колокольчик' - ON"):
            self.app.method.checkBox("ON", c_2000p_bell_mode_click, c_2000p_bell_mode_status)
            self.app.method.assertCheckBox("ON", c_2000p_bell_mode_status)
        with allure.step("Включение датчика - ON"):
            self.app.method.checkBox("ON", c_2000p_senser_on_click, c_2000p_senser_on_status)
            self.app.method.assertCheckBox("ON", c_2000p_senser_on_status)
        with allure.step("Режим 'Колокольчик' - OFF"):
            self.app.method.checkBox("OFF", c_2000p_bell_mode_click, c_2000p_bell_mode_status)
            self.app.method.assertCheckBox("OFF", c_2000p_bell_mode_status)

    # Проверка выпадающего списка Тип зоны
    def drop_list_type_zone(self, locator=kc_DL_type_zone):
        zone_list = ['Охранный', 'Тревожный', 'Вход', 'Пожарный']
        for i in zone_list:
            self.app.method.selectDropdownListByName(locator, i)
            self.app.method.assertSelectionDropdownList(i, locator)

    # Метод сохранения настроек КЦ
    def save_data_sensor_kc(self):
        _sensor_kc = self.app.read_data.data_sensor_kc()
        with allure.step(
                f"Выпадающий список - 'Тип зоны' выбор позиции: {_sensor_kc['sensor_kc_DL_type_zone']}"):
            self.app.method.selectDropdownListByName(kc_DL_type_zone, _sensor_kc['sensor_kc_DL_type_zone'])

        with allure.step(f"Выбор чекбокса Включение датчика: - {_sensor_kc['sensor_kc_CB_sensor_on']}"):
            self.app.method.checkBox(_sensor_kc['sensor_kc_CB_sensor_on'], c_2000p_senser_on_click,
                                     c_2000p_senser_on_status)
        with allure.step(f"Поле Название ввод: '{_sensor_kc['sensor_kc_name']}'"):
            self.app.method.inputValues(_sensor_kc['sensor_kc_name'], name)
        with allure.step(f"Выпадающий список - 'Раздел' выбор позиции: {_sensor_kc['sensor_kc_path']}"):
            self.app.method.selectDropdownListByName(kc_DL_path, _sensor_kc['sensor_kc_path'])
        with allure.step(f"Выбор чекбокса Режим 'Колокольчик': - {_sensor_kc['sensor_kc_CB_bell_mode']}"):
            self.app.method.checkBox(_sensor_kc['sensor_kc_CB_bell_mode'], c_2000p_bell_mode_click,
                                     c_2000p_bell_mode_status)

    # Метод проверки сохранения настроек КЦ
    def assert_save_data_sensor_kc(self):
        _sensor_kc = self.app.read_data.data_sensor_kc()
        with allure.step(
                f"Проверка выпадающего списка - 'Тип зоны' ожидаемое положение: {_sensor_kc['sensor_kc_DL_type_zone']}"):
            self.app.method.assertSelectionDropdownList(_sensor_kc['sensor_kc_DL_type_zone'], kc_DL_type_zone)

        with allure.step(
                f"Проверка выбора чекбокса Включение датчика ожидаемое положение: - {_sensor_kc['sensor_kc_CB_sensor_on']}"):
            self.app.method.assertCheckBox(_sensor_kc['sensor_kc_CB_sensor_on'], c_2000p_senser_on_status)
        with allure.step(f"Проверка поля Название ожидаемое значение: '{_sensor_kc['sensor_kc_name']}'"):
            self.app.method.assertValues(_sensor_kc['sensor_kc_name'], name)
        with allure.step(
                f"Проверка выпадающего списка - 'Раздел' ожидаемое положение: {_sensor_kc['sensor_kc_path']}"):
            self.app.method.assertSelectionDropdownList(_sensor_kc['sensor_kc_path'], kc_DL_path)
        with allure.step(
                f"Проверка выбора чекбокса Режим 'Колокольчик' ожидаемое положение: - {_sensor_kc['sensor_kc_CB_bell_mode']}"):
            self.app.method.assertCheckBox(_sensor_kc['sensor_kc_CB_bell_mode'], c_2000p_bell_mode_status)

    # Проверка чек-боксов - c_2000p СДВИГ
    def check_box_c_2000p_sdvig_on(self):
        with allure.step("Включение датчика - ON"):
            self.app.method.checkBox("ON", c_2000p_senser_on_click, c_2000p_senser_on_status)
            self.app.method.assertCheckBox("ON", c_2000p_senser_on_status)
        with allure.step("Режим 'Колокольчик' - ON"):
            self.app.method.checkBox("ON", c_2000p_bell_mode_click, c_2000p_bell_mode_status)
            self.app.method.assertCheckBox("ON", c_2000p_bell_mode_status)
        with allure.step('Контроль сдвига - ON'):
            self.app.method.checkBox("ON", c_2000p_sdvig_shear_control_click, c_2000p_sdvig_shear_control_status)
            self.app.method.assertCheckBox("ON", c_2000p_sdvig_shear_control_status)
        with allure.step('Контроль наклона - ON'):
            self.app.method.checkBox("ON", c_2000p_sdvig_tilt_control_click, c_2000p_sdvig_tilt_control_status)
            self.app.method.assertCheckBox("ON", c_2000p_sdvig_tilt_control_status)
        with allure.step('Фиксирование датчика наклона - ON'):
            self.app.method.checkBox("ON", c_2000p_sdvig_fixing_the_tilt_sensor_click,
                                     c_2000p_sdvig_fixing_the_tilt_sensor_status)
            self.app.method.assertCheckBox("ON", c_2000p_sdvig_fixing_the_tilt_sensor_status)
        with allure.step('Энергосберегающий режим - ON'):
            self.app.method.checkBox("ON", c_2000p_sdvig_energy_saving_mode_click,
                                     c_2000p_sdvig_energy_saving_mode_status)
            self.app.method.assertCheckBox("ON", c_2000p_sdvig_energy_saving_mode_status)
        with allure.step('Зафиксировать текущее положение - ON'):
            self.app.method.checkBox("ON", c_2000p_sdvig_lock_current_position_click,
                                     c_2000p_sdvig_lock_current_position_status)
            self.app.method.assertCheckBox("ON", c_2000p_sdvig_lock_current_position_status)
        with allure.step('Контроль геркона- ON'):
            self.app.method.checkBox("ON", c_2000p_sdvig_reed_switch_control_click,
                                     c_2000p_sdvig_reed_switch_control_status)
            self.app.method.assertCheckBox("ON", c_2000p_sdvig_reed_switch_control_status)

    # Проверка чек-боксов - c_2000p СДВИГ
    def check_box_c_2000p_sdvig_off(self):
        with allure.step("Включение датчика - OFF"):
            self.app.method.checkBox("OFF", c_2000p_senser_on_click, c_2000p_senser_on_status)
            self.app.method.assertCheckBox("OFF", c_2000p_senser_on_status)
        with allure.step("Режим 'Колокольчик' - OFF"):
            self.app.method.checkBox("OFF", c_2000p_bell_mode_click, c_2000p_bell_mode_status)
            self.app.method.assertCheckBox("OFF", c_2000p_bell_mode_status)
        with allure.step('Контроль сдвига - OFF'):
            self.app.method.checkBox("OFF", c_2000p_sdvig_shear_control_click, c_2000p_sdvig_shear_control_status)
            self.app.method.assertCheckBox("OFF", c_2000p_sdvig_shear_control_status)
        with allure.step('Контроль наклона - OFF'):
            self.app.method.checkBox("OFF", c_2000p_sdvig_tilt_control_click, c_2000p_sdvig_tilt_control_status)
            self.app.method.assertCheckBox("OFF", c_2000p_sdvig_tilt_control_status)
        with allure.step('Фиксирование датчика наклона - OFF'):
            self.app.method.checkBox("OFF", c_2000p_sdvig_fixing_the_tilt_sensor_click,
                                     c_2000p_sdvig_fixing_the_tilt_sensor_status)
            self.app.method.assertCheckBox("OFF", c_2000p_sdvig_fixing_the_tilt_sensor_status)
        with allure.step('Энергосберегающий режим - OFF'):
            self.app.method.checkBox("OFF", c_2000p_sdvig_energy_saving_mode_click,
                                     c_2000p_sdvig_energy_saving_mode_status)
            self.app.method.assertCheckBox("OFF", c_2000p_sdvig_energy_saving_mode_status)
        with allure.step('Зафиксировать текущее положение - OFF'):
            self.app.method.checkBox("OFF", c_2000p_sdvig_lock_current_position_click,
                                     c_2000p_sdvig_lock_current_position_status)
            self.app.method.assertCheckBox("OFF", c_2000p_sdvig_lock_current_position_status)
        with allure.step('Контроль геркона- OFF'):
            self.app.method.checkBox("OFF", c_2000p_sdvig_reed_switch_control_click,
                                     c_2000p_sdvig_reed_switch_control_status)
            self.app.method.assertCheckBox("OFF", c_2000p_sdvig_reed_switch_control_status)

    # Проверка чек-боксов - c_2000p СДВИГ
    def check_box_c_2000p_sdvig_some(self):
        with allure.step("Включение датчика - OFF"):
            self.app.method.checkBox("OFF", c_2000p_senser_on_click, c_2000p_senser_on_status)
            self.app.method.assertCheckBox("OFF", c_2000p_senser_on_status)
        with allure.step("Режим 'Колокольчик' - ON"):
            self.app.method.checkBox("ON", c_2000p_bell_mode_click, c_2000p_bell_mode_status)
            self.app.method.assertCheckBox("ON", c_2000p_bell_mode_status)
        with allure.step('Контроль сдвига - OFF'):
            self.app.method.checkBox("OFF", c_2000p_sdvig_shear_control_click, c_2000p_sdvig_shear_control_status)
            self.app.method.assertCheckBox("OFF", c_2000p_sdvig_shear_control_status)
        with allure.step('Контроль наклона - ON'):
            self.app.method.checkBox("ON", c_2000p_sdvig_tilt_control_click, c_2000p_sdvig_tilt_control_status)
            self.app.method.assertCheckBox("ON", c_2000p_sdvig_tilt_control_status)
        with allure.step('Фиксирование датчика наклона - OFF'):
            self.app.method.checkBox("OFF", c_2000p_sdvig_fixing_the_tilt_sensor_click,
                                     c_2000p_sdvig_fixing_the_tilt_sensor_status)
            self.app.method.assertCheckBox("OFF", c_2000p_sdvig_fixing_the_tilt_sensor_status)
        with allure.step('Энергосберегающий режим - ON'):
            self.app.method.checkBox("ON", c_2000p_sdvig_energy_saving_mode_click,
                                     c_2000p_sdvig_energy_saving_mode_status)
            self.app.method.assertCheckBox("ON", c_2000p_sdvig_energy_saving_mode_status)
        with allure.step('Зафиксировать текущее положение - OFF'):
            self.app.method.checkBox("OFF", c_2000p_sdvig_lock_current_position_click,
                                     c_2000p_sdvig_lock_current_position_status)
            self.app.method.assertCheckBox("OFF", c_2000p_sdvig_lock_current_position_status)
        with allure.step('Контроль геркона- ON'):
            self.app.method.checkBox("ON", c_2000p_sdvig_reed_switch_control_click,
                                     c_2000p_sdvig_reed_switch_control_status)
            self.app.method.assertCheckBox("ON", c_2000p_sdvig_reed_switch_control_status)
        with allure.step("Включение датчика - ON"):
            self.app.method.checkBox("ON", c_2000p_senser_on_click, c_2000p_senser_on_status)
            self.app.method.assertCheckBox("ON", c_2000p_senser_on_status)
        with allure.step("Режим 'Колокольчик' - OFF"):
            self.app.method.checkBox("OFF", c_2000p_bell_mode_click, c_2000p_bell_mode_status)
            self.app.method.assertCheckBox("OFF", c_2000p_bell_mode_status)
        with allure.step('Контроль сдвига - ON'):
            self.app.method.checkBox("ON", c_2000p_sdvig_shear_control_click, c_2000p_sdvig_shear_control_status)
            self.app.method.assertCheckBox("ON", c_2000p_sdvig_shear_control_status)
        with allure.step('Контроль наклона - OFF'):
            self.app.method.checkBox("OFF", c_2000p_sdvig_tilt_control_click, c_2000p_sdvig_tilt_control_status)
            self.app.method.assertCheckBox("OFF", c_2000p_sdvig_tilt_control_status)
        with allure.step('Фиксирование датчика наклона - ON'):
            self.app.method.checkBox("ON", c_2000p_sdvig_fixing_the_tilt_sensor_click,
                                     c_2000p_sdvig_fixing_the_tilt_sensor_status)
            self.app.method.assertCheckBox("ON", c_2000p_sdvig_fixing_the_tilt_sensor_status)
        with allure.step('Энергосберегающий режим - OFF'):
            self.app.method.checkBox("OFF", c_2000p_sdvig_energy_saving_mode_click,
                                     c_2000p_sdvig_energy_saving_mode_status)
            self.app.method.assertCheckBox("OFF", c_2000p_sdvig_energy_saving_mode_status)
        with allure.step('Зафиксировать текущее положение - ON'):
            self.app.method.checkBox("ON", c_2000p_sdvig_lock_current_position_click,
                                     c_2000p_sdvig_lock_current_position_status)
            self.app.method.assertCheckBox("ON", c_2000p_sdvig_lock_current_position_status)
        with allure.step('Контроль геркона- OFF'):
            self.app.method.checkBox("OFF", c_2000p_sdvig_reed_switch_control_click,
                                     c_2000p_sdvig_reed_switch_control_status)
            self.app.method.assertCheckBox("OFF", c_2000p_sdvig_reed_switch_control_status)

    # Проверка выпадающего списка Порог тревоги по наклону СДВИГ
    def drop_list_tilt_alarm_threshold_c_2000p_sdvig(self):
        path_list = ['3', '5', '10', '15', '20', '25', '30', '45']
        for i in path_list:
            self.app.method.selectDropdownListByName(c_2000p_sdvig_DL_tilt_alarm_threshold, i)
            self.app.method.assertSelectionDropdownList(i, c_2000p_sdvig_DL_tilt_alarm_threshold)

    # Проверка выпадающего списка Порог тревоги по перемещению СДВИГ
    def drop_list_movement_alarm_threshold_c_2000p_sdvig(self):
        path_list = ['50', '100', '150', '200', '250', '300', '450', '500']
        for i in path_list:
            self.app.method.selectDropdownListByName(c_2000p_sdvig_DL_movement_alarm_threshold, i)
            self.app.method.assertSelectionDropdownList(i, c_2000p_sdvig_DL_movement_alarm_threshold)

    # Метод сохранения настроек c_2000p СДВИГ
    def save_data_c_2000p_sdvig(self):
        _c_2000p_sdvig = self.app.read_data.data_sensor_sdvig()
        with allure.step(f"Выбор чекбокса Включение датчика: - {_c_2000p_sdvig['c_2000p_sdvig_CB_sensor_on']}"):
            self.app.method.checkBox(_c_2000p_sdvig['c_2000p_sdvig_CB_sensor_on'], c_2000p_senser_on_click,
                                     c_2000p_senser_on_status)
        with allure.step(f"Поле Название ввод: '{_c_2000p_sdvig['c_2000p_sdvig_name']}'"):
            self.app.method.inputValues(_c_2000p_sdvig['c_2000p_sdvig_name'], name)
        with allure.step(f"Выпадающий список - 'Раздел' выбор позиции: {_c_2000p_sdvig['c_2000p_sdvig_path']}"):
            self.app.method.selectDropdownListByName(c_2000p_DL_path, _c_2000p_sdvig['c_2000p_sdvig_path'])
        with allure.step(
                f"Выпадающий список - 'Режим индикации' выбор позиции: {_c_2000p_sdvig['c_2000p_sdvig_display_mode']}"):
            self.app.method.selectDropdownListByName(c_2000p_DL_indication_mod,
                                                     _c_2000p_sdvig['c_2000p_sdvig_display_mode'])
        with allure.step(f"Выбор чекбокса Режим 'Колокольчик': - {_c_2000p_sdvig['c_2000p_sdvig_CB_bell_mode']}"):
            self.app.method.checkBox(_c_2000p_sdvig['c_2000p_sdvig_CB_bell_mode'], c_2000p_bell_mode_click,
                                     c_2000p_bell_mode_status)
        with allure.step(f"Выбор чекбокса Контроль сдвига: - {_c_2000p_sdvig['c_2000p_sdvig_CB_tilt_sdvig']}"):
            self.app.method.checkBox(_c_2000p_sdvig['c_2000p_sdvig_CB_tilt_sdvig'], c_2000p_sdvig_shear_control_click,
                                     c_2000p_sdvig_shear_control_status)
        with allure.step(f"Выбор чекбокса Контроль наклона: - {_c_2000p_sdvig['c_2000p_sdvig_CB_tilt_control']}"):
            self.app.method.checkBox(_c_2000p_sdvig['c_2000p_sdvig_CB_tilt_control'], c_2000p_sdvig_tilt_control_click,
                                     c_2000p_sdvig_tilt_control_status)
        with allure.step(
                f"Выбор чекбокса Фиксирование датчика наклона: - {_c_2000p_sdvig['c_2000p_sdvig_CB_fix_tilt_control']}"):
            self.app.method.checkBox(_c_2000p_sdvig['c_2000p_sdvig_CB_fix_tilt_control'],
                                     c_2000p_sdvig_fixing_the_tilt_sensor_click,
                                     c_2000p_sdvig_fixing_the_tilt_sensor_status)
        with allure.step(f"Выбор чекбокса Энергосберегающий режим: - {_c_2000p_sdvig['c_2000p_sdvig_CB_energo_mode']}"):
            self.app.method.checkBox(_c_2000p_sdvig['c_2000p_sdvig_CB_energo_mode'],
                                     c_2000p_sdvig_energy_saving_mode_click, c_2000p_sdvig_energy_saving_mode_status)
        with allure.step(
                f"Выбор чекбокса Зафиксировать текущее положение: - {_c_2000p_sdvig['c_2000p_sdvig_CB_fix_position']}"):
            self.app.method.checkBox(_c_2000p_sdvig['c_2000p_sdvig_CB_fix_position'],
                                     c_2000p_sdvig_lock_current_position_click,
                                     c_2000p_sdvig_lock_current_position_status)
        with allure.step(f"Выбор чекбокса Контроль геркона: - {_c_2000p_sdvig['c_2000p_sdvig_CB_control_gerkon']}"):
            self.app.method.checkBox(_c_2000p_sdvig['c_2000p_sdvig_CB_control_gerkon'],
                                     c_2000p_sdvig_reed_switch_control_click, c_2000p_sdvig_reed_switch_control_status)
        with allure.step(
                f"Выпадающий список - 'Порог тревоги по наклону' выбор позиции: {_c_2000p_sdvig['c_2000p_DL_sdvig_tilt_alarm_threshold']}"):
            self.app.method.selectDropdownListByName(c_2000p_sdvig_DL_tilt_alarm_threshold,
                                                     _c_2000p_sdvig['c_2000p_DL_sdvig_tilt_alarm_threshold'])
        with allure.step(
                f"Выпадающий список - 'Порог тревоги по перемещению' выбор позиции: {_c_2000p_sdvig['c_2000p_DL_sdvig_movement_alarm_threshold']}"):
            self.app.method.selectDropdownListByName(c_2000p_sdvig_DL_movement_alarm_threshold,
                                                     _c_2000p_sdvig['c_2000p_DL_sdvig_movement_alarm_threshold'])

    # Метод проверки сохранения настроек c_2000p СДВИГ
    def assert_save_data_c_2000p_sdvig(self):
        _c_2000p_sdvig = self.app.read_data.data_sensor_sdvig()
        with allure.step(
                f"Проверка выбора чекбокса Включение датчика ожидаемое положение: - {_c_2000p_sdvig['c_2000p_sdvig_CB_sensor_on']}"):
            self.app.method.assertCheckBox(_c_2000p_sdvig['c_2000p_sdvig_CB_sensor_on'], c_2000p_senser_on_status)
        with allure.step(f"Проверка ввода поле Название ожиданемое значение: '{_c_2000p_sdvig['c_2000p_sdvig_name']}'"):
            self.app.method.assertValues(_c_2000p_sdvig['c_2000p_sdvig_name'], name)
        with allure.step(
                f"Проверка выпадающего списка - 'Раздел' проверка выбора позиции: {_c_2000p_sdvig['c_2000p_sdvig_path']}"):
            self.app.method.assertSelectionDropdownList(_c_2000p_sdvig['c_2000p_sdvig_path'], c_2000p_DL_path)
        with allure.step(
                f"Проверка выпадающего списка - 'Режим индикации'  проверка выбора позиции: {_c_2000p_sdvig['c_2000p_sdvig_display_mode']}"):
            self.app.method.assertSelectionDropdownList(_c_2000p_sdvig['c_2000p_sdvig_display_mode'],
                                                        c_2000p_DL_indication_mod)
        with allure.step(
                f"Проверка выбора чекбокса Режим 'Колокольчик' ожидаемое положение: - {_c_2000p_sdvig['c_2000p_sdvig_CB_bell_mode']}"):
            self.app.method.assertCheckBox(_c_2000p_sdvig['c_2000p_sdvig_CB_bell_mode'], c_2000p_bell_mode_status)
        with allure.step(
                f"Проверка выбора чекбокса Контроль сдвига ожидаемое положение: - {_c_2000p_sdvig['c_2000p_sdvig_CB_tilt_sdvig']}"):
            self.app.method.assertCheckBox(_c_2000p_sdvig['c_2000p_sdvig_CB_tilt_sdvig'],
                                           c_2000p_sdvig_shear_control_status)
        with allure.step(
                f"Проверка выбора чекбокса Контроль наклона ожидаемое положение: - {_c_2000p_sdvig['c_2000p_sdvig_CB_tilt_control']}"):
            self.app.method.assertCheckBox(_c_2000p_sdvig['c_2000p_sdvig_CB_tilt_control'],
                                           c_2000p_sdvig_tilt_control_status)
        with allure.step(
                f"Проверка выбора чекбокса Фиксирование датчика наклона ожидаемое положение: - {_c_2000p_sdvig['c_2000p_sdvig_CB_fix_tilt_control']}"):
            self.app.method.assertCheckBox(_c_2000p_sdvig['c_2000p_sdvig_CB_fix_tilt_control'],
                                           c_2000p_sdvig_fixing_the_tilt_sensor_status)
        with allure.step(
                f"Проверка выбора чекбокса Энергосберегающий режим ожидаемое положение: - {_c_2000p_sdvig['c_2000p_sdvig_CB_energo_mode']}"):
            self.app.method.assertCheckBox(_c_2000p_sdvig['c_2000p_sdvig_CB_energo_mode'],
                                           c_2000p_sdvig_energy_saving_mode_status)
        with allure.step(
                f"Проверка выбора чекбокса Зафиксировать текущее положение ожидаемое положение: - {_c_2000p_sdvig['c_2000p_sdvig_CB_fix_position']}"):
            self.app.method.assertCheckBox(_c_2000p_sdvig['c_2000p_sdvig_CB_fix_position'],
                                           c_2000p_sdvig_lock_current_position_status)
        with allure.step(
                f"Проверка выбора чекбокса Контроль геркона ожидаемое положение: - {_c_2000p_sdvig['c_2000p_sdvig_CB_control_gerkon']}"):
            self.app.method.assertCheckBox(_c_2000p_sdvig['c_2000p_sdvig_CB_control_gerkon'],
                                           c_2000p_sdvig_reed_switch_control_status)
        with allure.step(
                f"Проверка выпадающего списка - 'Порог тревоги по наклону' проверка выбора позиции: {_c_2000p_sdvig['c_2000p_DL_sdvig_tilt_alarm_threshold']}"):
            self.app.method.assertSelectionDropdownList(_c_2000p_sdvig['c_2000p_DL_sdvig_tilt_alarm_threshold'], c_2000p_sdvig_DL_tilt_alarm_threshold)
        with allure.step(
                f"Проверка выпадающего списка - 'Порог тревоги по перемещению' проверка выбора позиции: {_c_2000p_sdvig['c_2000p_DL_sdvig_movement_alarm_threshold']}"):
            self.app.method.assertSelectionDropdownList(_c_2000p_sdvig['c_2000p_DL_sdvig_movement_alarm_threshold'], c_2000p_sdvig_DL_movement_alarm_threshold)

    # Проверка чек-боксов - c_2000p ИП
    def check_box_c_2000p_ip_on(self):
        with allure.step("Включение датчика - ON"):
            self.app.method.checkBox("ON", c_2000p_senser_on_click, c_2000p_senser_on_status)
            self.app.method.assertCheckBox("ON", c_2000p_senser_on_status)
        with allure.step("Режим 'Колокольчик' - ON"):
            self.app.method.checkBox("ON", c_2000p_bell_mode_click, c_2000p_bell_mode_status)
            self.app.method.assertCheckBox("ON", c_2000p_bell_mode_status)
        with allure.step("Вскрытие корпуса - ON"):
            self.app.method.checkBox("ON", c_2000p_ip_senser_open_click, c_2000p_ip_senser_open_status)
            self.app.method.assertCheckBox("ON", c_2000p_ip_senser_open_status)

    # Проверка чек-боксов - c_2000p ИП
    def check_box_c_2000p_ip_off(self):
        with allure.step("Включение датчика - ON"):
            self.app.method.checkBox("ON", c_2000p_senser_on_click, c_2000p_senser_on_status)
            self.app.method.assertCheckBox("ON", c_2000p_senser_on_status)
        with allure.step("Режим 'Колокольчик' - OFF"):
            self.app.method.checkBox("OFF", c_2000p_bell_mode_click, c_2000p_bell_mode_status)
            self.app.method.assertCheckBox("OFF", c_2000p_bell_mode_status)
        with allure.step("Вскрытие корпуса - OFF"):
            self.app.method.checkBox("OFF", c_2000p_ip_senser_open_click, c_2000p_ip_senser_open_status)
            self.app.method.assertCheckBox("OFF", c_2000p_ip_senser_open_status)

    # Проверка чек-боксов - c_2000p ИП
    def check_box_c_2000p_ip_some(self):
        with allure.step("Включение датчика - ON"):
            self.app.method.checkBox("ON", c_2000p_senser_on_click, c_2000p_senser_on_status)
            self.app.method.assertCheckBox("ON", c_2000p_senser_on_status)
        with allure.step("Режим 'Колокольчик' - OFF"):
            self.app.method.checkBox("OFF", c_2000p_bell_mode_click, c_2000p_bell_mode_status)
            self.app.method.assertCheckBox("OFF", c_2000p_bell_mode_status)
        with allure.step("Вскрытие корпуса - ON"):
            self.app.method.checkBox("ON", c_2000p_ip_senser_open_click, c_2000p_ip_senser_open_status)
            self.app.method.assertCheckBox("ON", c_2000p_ip_senser_open_status)
        with allure.step("Включение датчика - ON"):
            self.app.method.checkBox("ON", c_2000p_senser_on_click, c_2000p_senser_on_status)
            self.app.method.assertCheckBox("ON", c_2000p_senser_on_status)
        with allure.step("Режим 'Колокольчик' - ON"):
            self.app.method.checkBox("ON", c_2000p_bell_mode_click, c_2000p_bell_mode_status)
            self.app.method.assertCheckBox("ON", c_2000p_bell_mode_status)
        with allure.step("Вскрытие корпуса - OFF"):
            self.app.method.checkBox("OFF", c_2000p_ip_senser_open_click, c_2000p_ip_senser_open_status)
            self.app.method.assertCheckBox("OFF", c_2000p_ip_senser_open_status)

    # Метод сохранения настроек c_2000p ИП
    def save_data_c_2000p_ip(self):
        _c_2000p_ip = self.app.read_data.data_sensor_c_2000p_ip()
        with allure.step(f"Выбор чекбокса Включение датчика: - {_c_2000p_ip['C_2000P_IP_CB_sensor_on']}"):
            self.app.method.checkBox(_c_2000p_ip['C_2000P_IP_CB_sensor_on'], c_2000p_senser_on_click,
                                     c_2000p_senser_on_status)
        with allure.step(f"Поле Название ввод: '{_c_2000p_ip['C_2000P_IP_name']}'"):
            self.app.method.inputValues(_c_2000p_ip['C_2000P_IP_name'], name)
        with allure.step(f"Выпадающий список - 'Раздел' выбор позиции: {_c_2000p_ip['C_2000P_IP_path']}"):
            self.app.method.selectDropdownListByName(c_2000p_DL_path, _c_2000p_ip['C_2000P_IP_path'])
        with allure.step(
                f"Выпадающий список - 'Режим индикации' выбор позиции: {_c_2000p_ip['C_2000P_IP_display_mode']}"):
            self.app.method.selectDropdownListByName(c_2000p_DL_indication_mod, _c_2000p_ip['C_2000P_IP_display_mode'])
        with allure.step(f"Выбор чекбокса Режим 'Колокольчик': - {_c_2000p_ip['C_2000P_IP_CB_bell_mode']}"):
            self.app.method.checkBox(_c_2000p_ip['C_2000P_IP_CB_bell_mode'], c_2000p_bell_mode_click,
                                     c_2000p_bell_mode_status)
        with allure.step(f"Поле Гистерезис ввод: '{_c_2000p_ip['C_2000P_IP_gisteresis']}'"):
            self.app.method.inputValues(_c_2000p_ip['C_2000P_IP_gisteresis'], c_2000p_ip_gisteresis)
        with allure.step(f"Поле Нижний порог по температуре ввод: '{_c_2000p_ip['C_2000P_IP_temp_min']}'"):
            self.app.method.inputValues(_c_2000p_ip['C_2000P_IP_temp_min'], c_2000p_ip_temp_min)
        with allure.step(f"Поле Верхний порог по температуре ввод: '{_c_2000p_ip['C_2000P_IP_temp_max']}'"):
            self.app.method.inputValues(_c_2000p_ip['C_2000P_IP_temp_max'], c_2000p_ip_temp_max)
        with allure.step(
                f"Выпадающий список - 'Режим уведомлений' выбор позиции: {_c_2000p_ip['C_2000P_IP_notification_mode']}"):
            self.app.method.selectDropdownListByName(c_2000p_DL_notification_mod,
                                                     _c_2000p_ip['C_2000P_IP_notification_mode'])
        with allure.step(f"Выбор чекбокса Режим 'Вскрытие корпуса': - {_c_2000p_ip['C_2000P_IP_CB_open']}"):
            self.app.method.checkBox(_c_2000p_ip['C_2000P_IP_CB_open'], c_2000p_ip_senser_open_click,
                                     c_2000p_ip_senser_open_status)

    # Метод проверки сохранения настроек c_2000p ИП
    def assert_save_data_c_2000p_ip(self):
        _c_2000p_ip = self.app.read_data.data_sensor_c_2000p_ip()
        with allure.step(
                f"Проверка выбора чекбокса Включение датчика ожидаемое значение: - {_c_2000p_ip['C_2000P_IP_CB_sensor_on']}"):
            self.app.method.assertCheckBox(_c_2000p_ip['C_2000P_IP_CB_sensor_on'], c_2000p_senser_on_status)
        with allure.step(f"Проверка ввода в поле Название ожидаемое значение: '{_c_2000p_ip['C_2000P_IP_name']}'"):
            self.app.method.assertValues(_c_2000p_ip['C_2000P_IP_name'], name)
        with allure.step(f"Проверка выпадающего списка - 'Раздел' выбор позиции: {_c_2000p_ip['C_2000P_IP_path']}"):
            self.app.method.assertSelectionDropdownList(_c_2000p_ip['C_2000P_IP_path'], c_2000p_DL_path)
        with allure.step(
                f"Проверка выпадающего списка - 'Режим индикации' выбор позиции: {_c_2000p_ip['C_2000P_IP_display_mode']}"):
            self.app.method.assertSelectionDropdownList(_c_2000p_ip['C_2000P_IP_display_mode'],
                                                        c_2000p_DL_indication_mod)
        with allure.step(
                f"Проверка выбора чекбокса Режим 'Колокольчик'ожидаемое значение: - {_c_2000p_ip['C_2000P_IP_CB_bell_mode']}"):
            self.app.method.assertCheckBox(_c_2000p_ip['C_2000P_IP_CB_bell_mode'], c_2000p_bell_mode_status)
        with allure.step(
                f"Проверка ввода в поле Гистерезис ожидаемое значение: '{_c_2000p_ip['C_2000P_IP_gisteresis']}'"):
            self.app.method.assertValues(_c_2000p_ip['C_2000P_IP_gisteresis'], c_2000p_ip_gisteresis)
        with allure.step(
                f"Проверка ввода в поле Нижний порог по температуре ожидаемое значение: '{_c_2000p_ip['C_2000P_IP_temp_min']}'"):
            self.app.method.assertValues(_c_2000p_ip['C_2000P_IP_temp_min'], c_2000p_ip_temp_min)
        with allure.step(
                f"Проверка ввода в поле Верхний порог по температуре ожидаемое значение: '{_c_2000p_ip['C_2000P_IP_temp_max']}'"):
            self.app.method.assertValues(_c_2000p_ip['C_2000P_IP_temp_max'], c_2000p_ip_temp_max)
        with allure.step(
                f"Проверка выпадающего списка - 'Режим уведомлений' выбор позиции: {_c_2000p_ip['C_2000P_IP_notification_mode']}"):
            self.app.method.assertSelectionDropdownList(_c_2000p_ip['C_2000P_IP_notification_mode'],
                                                        c_2000p_DL_notification_mod)
        with allure.step(
                f"Проверка выбора чекбокса Режим 'Вскрытие корпуса'ожидаемое значение: - {_c_2000p_ip['C_2000P_IP_CB_open']}"):
            self.app.method.assertCheckBox(_c_2000p_ip['C_2000P_IP_CB_open'], c_2000p_ip_senser_open_status)
