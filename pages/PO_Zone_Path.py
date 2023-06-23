# -*- coding: utf-8 -*-
import random
import time
from dataclasses import dataclass

import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from data.pages_text import *
from locators.zone_path_locators import *


@dataclass
class ZonePathHelper:
    app: any

    # ---------------------- ОБЩИЕ МЕТОДЫ ----------------------------------------------------------------------

    # Проверка ввода поле принимает все символы
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

    # Проверка Поиск
    def input_seach(self, locator=Search):
        try:
            self.input_all(locator)
            with allure.step("Проверка ввода очень большого числа"):
                self.app.method.assertEqual(9999 * 1000000, 9999 * 1000000, locator)
        finally:
            self.app.method.click((By.XPATH, cross_close_button))

    # Проверка ввода поле
    def input_number_65535(self, locator):
        with allure.step("Проверка ввода цифр"):
            for i in range(10):
                self.app.method.assertEqual(i, i, locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual(0, 0, locator)
            self.app.method.assertEqual(1, 1, locator)
            self.app.method.assertEqual(98, 98, locator)
            self.app.method.assertEqual(99, 99, locator)

    # Проверка ввода поле
    def input_number_65535_negativ(self, locator):
        with allure.step("Проверка ввода латинских букв в нижнем регистре"):
            self.app.method.assertEqual('abcdefghijklmnopqrstuvwxyz', '', locator)
        with allure.step("Проверка ввода латинских букв в верхнем регистре"):
            self.app.method.assertEqual('ABCDEFGHIJKLMNOPQRSTUVWXYZ', '', locator)
        with allure.step("Проверка ввода Русских букв в нижнем регистре"):
            self.app.method.assertEqual("ёйцукенгшщзхъфывапролджэячсмитьбю", "", locator)
        with allure.step("Проверка ввода Русских букв в верхнем регистре"):
            self.app.method.assertEqual("АПРОЛДЖЭЯЧСМИТЬБЮЁЙЦУКЕНГШЩЗХЪФЫВ", "", locator)
        with allure.step("Проверка ввода спецсимволов"):
            self.app.method.assertEqual("!#$%&'()*+,-./:;<=>?@[]^_`{|}~", "", locator)
        with allure.step("Проверка ввода совместных значений(буквы/цифры/спецсимволы)"):
            self.app.method.assertEqual('12  АБВABC!@#', '12', locator)
        with allure.step("Проверка ввода пробелов"):
            self.app.method.assertEqual('   ', '', locator)
            self.app.method.assertEqual('80     ', '80', locator)
            self.app.method.assertEqual('   80', '80', locator)
            self.app.method.assertEqual('8 0', '80', locator)
        with allure.step("Проверка ввода дробного числа "):
            self.app.method.assertEqual('9.0', '90', locator)
            self.app.method.assertEqual('000.1', '1', locator)
            self.app.method.assertEqual('1,1', '11', locator)
            self.app.method.assertEqual('000,1', '1', locator)
        with allure.step("Проверка ввода пустого значения"):
            self.app.method.assertEqual('', '', locator)
            self.app.method.assertEqual('', '', locator)
        with allure.step("Проверка ввода очень большого числа"):
            self.app.method.assertEqual(9 * 10000000000000, 90, locator)
        with allure.step("Проверка ввода отрицательного числа"):
            self.app.method.assertEqual('-1', '1', locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual(999999, 99, locator)

    # Позитивные проверки ввода значений 99.99
    def input_99_99_positiv(self, locator):
        with allure.step("Проверка ввода цифр"):
            for i in range(10):
                self.app.method.assertEqual(i, i, locator)
        with allure.step("Проверка ввода спецсимполов"):
            self.app.method.assertEqual(".,", ".,", locator)
        with allure.step("Проверка ввода дробного числа "):
            self.app.method.assertEqual('11.11', '11.11', locator)
            self.app.method.assertEqual('11,11', '11,11', locator)
        with allure.step("Проверка ввода пустого значения"):
            self.app.method.assertEqual('', '', locator)
        with allure.step("Проверка ввода отрицательного числа"):
            self.app.method.assertEqual('-1', '1', locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual(0, 0, locator)
            self.app.method.assertEqual(1, 1, locator)
            self.app.method.assertEqual(99.98, 99.98, locator)
            self.app.method.assertEqual(99.99, 99.99, locator)

    # Негативные проверки ввода значений 99.99
    def input_99_99_negativ(self, locator):
        with allure.step("Проверка ввода латинских букв в нижнем регистре"):
            self.app.method.assertEqual('abcdefghijklmnopqrstuvwxyz', '', locator)
        with allure.step("Проверка ввода латинских букв в врхнем регистре"):
            self.app.method.assertEqual('ABCDEFGHIJKLMNOPQRSTUVWXYZ', '', locator)
        with allure.step("Проверка ввода Русских букв в нижнем регистре"):
            self.app.method.assertEqual("ёйцукенгшщзхъфыв", "", locator)
            self.app.method.assertEqual("апролджэячсмитьбю", "", locator)
        with allure.step("Проверка ввода Русских букв в верхнем регистре"):
            self.app.method.assertEqual("АПРОЛДЖЭЯЧСМИТЬБЮ", "", locator)
            self.app.method.assertEqual("ЁЙЦУКЕНГШЩЗХЪФЫВ", "", locator)
        with allure.step("Проверка ввода спецсимполов"):
            self.app.method.assertEqual("!#$%&'()*+,-./:;<=>?@[]^_`{|}~", ",.", locator)
        with allure.step("Проверка ввода совместных значений"):
            self.app.method.assertEqual('12.  АБВABC!@#', '12.', locator)
        with allure.step("Проверка ввода пробелов"):
            self.app.method.assertEqual('   ', '', locator)
            self.app.method.assertEqual('12     ', '12', locator)
            self.app.method.assertEqual('   12', '12', locator)
            self.app.method.assertEqual('1 2', '12', locator)
        with allure.step("Проверка ввода дробного числа "):
            self.app.method.assertEqual('11.11', '11.11', locator)
            self.app.method.assertEqual('00.1', '00.1', locator)
            self.app.method.assertEqual('11,11', '11,11', locator)
            self.app.method.assertEqual('00,1', '00,1', locator)
        with allure.step("Проверка ввода пустого значения"):
            self.app.method.assertEqual('', '', locator)
        with allure.step("Проверка ввода отрицательного числа"):
            self.app.method.assertEqual('-1', '1', locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual(99.98, 99.98, locator)
            self.app.method.assertEqual(99.99, 99.99, locator)

    # Позитивные проверки ввода значений 10
    def input_10_positiv(self, locator):
        with allure.step("Проверка ввода цифр"):
            for i in range(10):
                self.app.method.assertEqual(i, i, locator)
        with allure.step("Проверка ввода спецсимполов"):
            self.app.method.assertEqual(".,", ".,", locator)
        with allure.step("Проверка ввода дробного числа "):
            self.app.method.assertEqual('9.10', '9.10', locator)
            self.app.method.assertEqual('9,10', '9,10', locator)
        with allure.step("Проверка ввода пустого значения"):
            self.app.method.assertEqual('', '', locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual(0, 0, locator)
            self.app.method.assertEqual(1, 1, locator)
            self.app.method.assertEqual(9.98, 9.98, locator)
            self.app.method.assertEqual(9.99, 9.99, locator)

    # Негативные проверки ввода значений 10
    def input_10_negativ(self, locator):
        with allure.step("Проверка ввода латинских букв в нижнем регистре"):
            self.app.method.assertEqual('abcdefghijklmnopqrstuvwxyz', '', locator)
        with allure.step("Проверка ввода латинских букв в врхнем регистре"):
            self.app.method.assertEqual('ABCDEFGHIJKLMNOPQRSTUVWXYZ', '', locator)
        with allure.step("Проверка ввода Русских букв в нижнем регистре"):
            self.app.method.assertEqual("ёйцукенгшщзхъфыв", "", locator)
            self.app.method.assertEqual("апролджэячсмитьбю", "", locator)
        with allure.step("Проверка ввода Русских букв в верхнем регистре"):
            self.app.method.assertEqual("АПРОЛДЖЭЯЧСМИТЬБЮ", "", locator)
            self.app.method.assertEqual("ЁЙЦУКЕНГШЩЗХЪФЫВ", "", locator)
        with allure.step("Проверка ввода спецсимполов"):
            self.app.method.assertEqual("!#$%&'()*+,-./:;<=>?@[]^_`{|}~", ",.", locator)
        with allure.step("Проверка ввода совместных значений"):
            self.app.method.assertEqual('9.  АБВABC!@#', '9.', locator)
        with allure.step("Проверка ввода пробелов"):
            self.app.method.assertEqual('   ', '', locator)
            self.app.method.assertEqual('10     ', '10', locator)
            self.app.method.assertEqual('   10', '10', locator)
            self.app.method.assertEqual('1 0', '10', locator)
        with allure.step("Проверка ввода отрицательного числа"):
            self.app.method.assertEqual('-1', '1', locator)

    # Позитивные проверки ввода значений 100
    def input_100_positiv(self, locator):
        with allure.step("Проверка ввода цифр"):
            for i in range(10):
                self.app.method.assertEqual(i, i, locator)
        with allure.step("Проверка ввода спецсимполов"):
            self.app.method.assertEqual(".,", ".,", locator)
        with allure.step("Проверка ввода дробного числа "):
            self.app.method.assertEqual('99.99', '99.99', locator)
            self.app.method.assertEqual('99.99', '99.99', locator)
        with allure.step("Проверка ввода пустого значения"):
            self.app.method.assertEqual('', '', locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual(0, 0, locator)
            self.app.method.assertEqual(1, 1, locator)
            self.app.method.assertEqual(100, 100, locator)

    # Негативные проверки ввода значений 100
    def input_100_negativ(self, locator):
        with allure.step("Проверка ввода латинских букв в нижнем регистре"):
            self.app.method.assertEqual('abcdefghijklmnopqrstuvwxyz', '', locator)
        with allure.step("Проверка ввода латинских букв в врхнем регистре"):
            self.app.method.assertEqual('ABCDEFGHIJKLMNOPQRSTUVWXYZ', '', locator)
        with allure.step("Проверка ввода Русских букв в нижнем регистре"):
            self.app.method.assertEqual("ёйцукенгшщзхъфыв", "", locator)
            self.app.method.assertEqual("апролджэячсмитьбю", "", locator)
        with allure.step("Проверка ввода Русских букв в верхнем регистре"):
            self.app.method.assertEqual("АПРОЛДЖЭЯЧСМИТЬБЮ", "", locator)
            self.app.method.assertEqual("ЁЙЦУКЕНГШЩЗХЪФЫВ", "", locator)
        with allure.step("Проверка ввода спецсимполов"):
            self.app.method.assertEqual("!#$%&'()*+,-./:;<=>?@[]^_`{|}~", ",.", locator)
        with allure.step("Проверка ввода совместных значений"):
            self.app.method.assertEqual('9.  АБВABC!@#', '9.', locator)
        with allure.step("Проверка ввода пробелов"):
            self.app.method.assertEqual('   ', '', locator)
            self.app.method.assertEqual('10     ', '10', locator)
            self.app.method.assertEqual('   10', '10', locator)
            self.app.method.assertEqual('1 0', '10', locator)
        with allure.step("Проверка ввода отрицательного числа"):
            self.app.method.assertEqual('-1', '1', locator)

    # ---------------------- РАЗДЕЛЫ ----------------------------------------------------------------------

    # Проверка полей Добавить раздел
    def text_add_path(self):
        self.app.method.assertTextOnPage(data_add_path_modal_text, data_add_path)

    # Выпадающий список: Управляющие разделы
    def drop_list_controlled_sections(self, button=controlled_sections_button, possition=positions_check_box):
        for i in range(9):
            self.app.method.selectDropdownListCheckBox(button, possition + f'[{i + 1}]',
                                                       status_drop_list_check_box + f'[{i + 1}]')
            self.app.method.assertSelectionDropdownListCheckBox('Раздел № 0' + str(i + 1), button)

        for i in range(9, 16):
            self.app.method.selectDropdownListCheckBox(button, possition + f'[{i + 1}]',
                                                       status_drop_list_check_box + f'[{i + 1}]')
            self.app.method.assertSelectionDropdownListCheckBox('Раздел № ' + str(i + 1), button)

    # Включение чекбоксов Добавить раздел
    def add_path_check_box_on(self):
        self.app.method.checkBox("ON", Take_Delay_click, Take_Delay_status)
        self.app.method.assertCheckBox("ON", Take_Delay_status)
        self.app.method.checkBox("ON", Auto_pickup_from_non_pickup_click, Auto_pickup_from_non_pickup_status)
        self.app.method.assertCheckBox("ON", Auto_pickup_from_non_pickup_status)
        self.app.method.checkBox("ON", Auto_arm_from_alarm_click, Auto_arm_from_alarm_status)
        self.app.method.assertCheckBox("ON", Auto_arm_from_alarm_status)

    # Выключение чекбоксов Добавить раздел
    def add_path_check_box_off(self):
        self.app.method.checkBox("OFF", Take_Delay_click, Take_Delay_status)
        self.app.method.assertCheckBox("OFF", Take_Delay_status)
        self.app.method.checkBox("OFF", Auto_pickup_from_non_pickup_click, Auto_pickup_from_non_pickup_status)
        self.app.method.assertCheckBox("OFF", Auto_pickup_from_non_pickup_status)
        self.app.method.checkBox("OFF", Auto_arm_from_alarm_click, Auto_arm_from_alarm_status)
        self.app.method.assertCheckBox("OFF", Auto_arm_from_alarm_status)

    # Включение чекбоксов выборочно
    def add_path_check_box_some(self):
        self.app.method.checkBox("ON", Take_Delay_click, Take_Delay_status)
        self.app.method.assertCheckBox("ON", Take_Delay_status)
        self.app.method.checkBox("OFF", Auto_pickup_from_non_pickup_click, Auto_pickup_from_non_pickup_status)
        self.app.method.assertCheckBox("OFF", Auto_pickup_from_non_pickup_status)
        self.app.method.checkBox("ON", Auto_arm_from_alarm_click, Auto_arm_from_alarm_status)
        self.app.method.assertCheckBox("ON", Auto_arm_from_alarm_status)
        self.app.method.checkBox("OFF", Take_Delay_click, Take_Delay_status)
        self.app.method.assertCheckBox("OFF", Take_Delay_status)
        self.app.method.checkBox("ON", Auto_pickup_from_non_pickup_click, Auto_pickup_from_non_pickup_status)
        self.app.method.assertCheckBox("ON", Auto_pickup_from_non_pickup_status)
        self.app.method.checkBox("OFF", Auto_arm_from_alarm_click, Auto_arm_from_alarm_status)
        self.app.method.assertCheckBox("OFF", Auto_arm_from_alarm_status)

    # Клик по кнопке Добавить раздел
    def add_path(self):
        with allure.step("Клик по кнопке Добавить раздел"):
            self.app.method.click((By.XPATH, add_path_button))

    # Клик по кнопке Настройки - первый раздел
    def settings_first_path_button(self):
        with allure.step("Клик по кнопке Настройки"):
            # Если раздел взят то снимаем его
            if self.app.method.is_element_present_xpath(action_first_path_button):
                self.app.method.click((By.XPATH, action_first_path_button))
            self.app.method.click((By.XPATH, settings_first_path_button))

    # Клик по кнопке Настройки -  второй раздел
    def settings_2_path_button(self):
        with allure.step("Клик по кнопке Настройки"):
            self.app.method.click((By.XPATH, settings_first_path_button))

    # Добавить раздел если его нет
    def Add_path_if_not(self):
        with allure.step("Получение списка разделов"):
            path = self.app.method.getElementsLen(path_row)
            if path == 0:
                with allure.step("Добавление раздела"):
                    self.app.method.click((By.XPATH, add_path_button))
                    self.app.method.inputValues((random.randint(111, 999)), namber_path)
                    self.app.method.inputValues((random.randint(111, 999)), name_path)
                    self.app.method.click((By.XPATH, save_button_path))

    # Клик по кнопке Отменить
    def cancel(self):
        with allure.step("Клик по кнопке Отменить"):
            self.app.method.click((By.XPATH, cancel_button))

    # Номер - Разделы
    def input_data_namber_path_positv(self, locator=namber_path):
        self.input_number_65535(locator)

    # Номер - Разделы
    def input_data_namber_path_negativ(self, locator=namber_path):
        self.input_number_65535_negativ(locator)

    # Название - Разделы
    def input_data_name_path_positv(self, locator=name_path):
        self.input_all(locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual(1, 1, locator)
            self.app.method.assertEqual('1' * 62, '1' * 62, locator)
            self.app.method.assertEqual('1' * 63, '1' * 63, locator)
            self.app.method.assertEqual('г' * 31 + "1", 'г' * 31 + "1", locator)

    # Название - Разделы
    def input_data_name_path_negativ(self, locator_actual=name_path, locator_expected=name_path_error):
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assert_field('1' * 64, locator_actual, locator_expected)
            self.app.method.assert_field('г' * 32, locator_actual, locator_expected)

    # ---------------------- ВЫХОДЫ ----------------------------------------------------------------------

    # Проверка полей выходы - выключен
    def text_off_out(self):
        with allure.step("Проверка названий полей Выход 1"):
            self.app.method.assertTextOnPage(locator_out_1_text, data_out_off)
        with allure.step("Проверка названий полей Выход 2"):
            self.app.method.assertTextOnPage(locator_out_2_text, data_out_off)

    # Проверка полей выходы - Событийный
    def text_event_out(self):
        with allure.step("Проверка названий полей Выход 1"):
            self.app.method.assertTextOnPage(locator_out_1_text, data_out_event)
        with allure.step("Проверка названий полей Выход 2"):
            self.app.method.assertTextOnPage(locator_out_2_text, data_out_event)

    # Проверка полей выходы - Температурный
    def text_temp_out(self):
        with allure.step("Проверка названий полей Выход 1"):
            self.app.method.assertTextOnPage(locator_out_1_text, data_out_temp)
        with allure.step("Проверка названий полей Выход 2"):
            self.app.method.assertTextOnPage(locator_out_2_text, data_out_temp)

    # Проверка полей выходы - Управляемый
    def text_managed_out(self):
        with allure.step("Проверка названий полей Выход 1"):
            self.app.method.assertTextOnPage(locator_out_1_text, data_out_managed)
        with allure.step("Проверка названий полей Выход 2"):
            self.app.method.assertTextOnPage(locator_out_2_text, data_out_managed)

    # Проверка полей выходы - Управляемый
    def text_managed_out_rele(self):
        with allure.step("Проверка названий полей Выход 1"):
            self.app.method.assertTextOnPage(locator_out_1_text, data_out_managed)
        with allure.step("Проверка названий полей Выход 2"):
            self.app.method.assertTextOnPage(locator_out_2_text, data_out_managed)

    # Выбор Температурного режима работы - ВЫХОД № 1
    def select_temperature_mode_out_1(self):
        with allure.step("Выключение режима 2"):
            self.app.method.Select_from_the_dropdown_list_by_name(button=Working_mode_out_2, position='Выключен')
        with allure.step("Выбор режима 'Температурный' в выходе № 1"):
            self.app.method.Select_from_the_dropdown_list_by_name(button=Working_mode_out_1, position='Температурный')

    # Выбор Температурного режима работы - ВЫХОД № 2
    def select_temperature_mode_out_2(self):
        with allure.step("Выключение режима 2"):
            self.app.method.Select_from_the_dropdown_list_by_name(button=Working_mode_out_1, position='Выключен')
        with allure.step("Выбор режима 'Температурный' в выходе № 2"):
            self.app.method.Select_from_the_dropdown_list_by_name(button=Working_mode_out_2, position='Температурный')

    # Выбор режима работы - ВЫХОД № 1/2
    def select_working_mode_out(self, position: str):
        with allure.step(f"ВЫХОД № 1 - {position}"):
            self.app.method.Select_from_the_dropdown_list_by_name(button=Working_mode_out_1, position=position)
        with allure.step(f"ВЫХОД № 2 - {position}"):
            self.app.method.Select_from_the_dropdown_list_by_name(button=Working_mode_out_2, position=position)

    # Выбор режима работы - ВЫХОД № 1
    def select_working_mode_out_1(self, position: str):
        with allure.step(f"ВЫХОД № 1 - {position}"):
            self.app.method.Select_from_the_dropdown_list_by_name(button=Working_mode_out_1, position=position)

    # Выбор режима работы - ВЫХОД № 1 - Температурный
    def select_working_mode_out_1_temp(self, position: str):
        _out = self.app.read_data.data_out()
        with allure.step(f"ВЫХОД № 1 - {position}"):
            self.app.method.Select_from_the_dropdown_list_by_name(button=Working_mode_out_1, position=position)
        with allure.step(f"Ввод данных в поле 'Гистерезис : '{_out['Gisteresis_outs']}'"):
            self.app.method.inputValues(value=_out["Gisteresis_outs"], locator=hysteresis_out)

    # Выбор режима работы - ВЫХОД № 2
    def select_working_mode_out_2(self, position: str):
        with allure.step(f"ВЫХОД № 2 - {position}"):
            self.app.method.Select_from_the_dropdown_list_by_name(button=Working_mode_out_2, position=position)

    # Выбор режима работы - ВЫХОД № 2 - ТЕМПЕРАТУРНЫЙ
    def select_working_mode_out_2_temp(self, position: str):
        _out = self.app.read_data.data_out()
        with allure.step(f"ВЫХОД № 2 - {position}"):
            self.app.method.Select_from_the_dropdown_list_by_name(button=Working_mode_out_2, position=position)
        with allure.step(f"Ввод данных в поле 'Гистерезис : '{_out['Gisteresis_outs']}'"):
            self.app.method.inputValues(value=_out["Gisteresis_outs"], locator=hysteresis_out)

    # Название - Выходы1
    def input_data_name_out_1_positv(self, locator=name_out_1):
        self.input_all(locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual(1, 1, locator)
            self.app.method.assertEqual('1' * 62, '1' * 62, locator)
            self.app.method.assertEqual('1' * 63, '1' * 63, locator)
            self.app.method.assertEqual('г' * 31 + "1", 'г' * 31 + "1", locator)

    # Название - Выходы1
    def input_data_name_out_1_negativ(self, locator_actual=name_out_1, locator_expected=name_out_1_error):
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assert_field('1' * 64, locator_actual, locator_expected)
            self.app.method.assert_field('г' * 32, locator_actual, locator_expected)

    # Название - Выходы2
    def input_data_name_out_2_positv(self, locator=name_out_2):
        self.input_all(locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual(1, 1, locator)
            self.app.method.assertEqual('1' * 62, '1' * 62, locator)
            self.app.method.assertEqual('1' * 63, '1' * 63, locator)
            self.app.method.assertEqual('г' * 31 + "1", 'г' * 31 + "1", locator)

    def save_button_click(self):
        with allure.step("Клик по кнопке СОХРАНИТЬ"):
            self.app.method.click((By.XPATH, save_button))
        with allure.step("Проверка всплывающего окна сохранено"):
            self.app.method.click((By.XPATH, '/html/body//button[@class="toast-message-btn-close close-icon"]'))

    def save_button_settings_click(self):
        with allure.step("Клик по кнопке СОХРАНИТЬ"):
            self.app.method.click((By.XPATH, save_button_path))
        with allure.step("Проверка всплывающего окна сохранено"):
            self.app.method.click((By.XPATH, '/html/body//button[@class="toast-message-btn-close close-icon"]'))

    # Название - Выходы2
    def input_data_name_out_2_negativ(self, locator_actual=name_out_2, locator_expected=name_out_2_error):
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assert_field('1' * 64, locator_actual, locator_expected)
            self.app.method.assert_field('г' * 32, locator_actual, locator_expected)

    # Гистерезис
    def input_hysteresis_positiv(self, locator=hysteresis_out):
        self.input_10_positiv(locator)

    # Гистерезис
    def input_hysteresis_negativ(self, locator=hysteresis_out):
        self.input_10_negativ(locator)

    # Управляющий сенсор
    def input_control_sensor_1_positiv(self, locator=control_sensor_out):
        self.input_100_positiv(locator)

    # Управляющий сенсор
    def input_control_sensor_1_negativ(self, locator=control_sensor_out):
        self.input_100_negativ(locator)

    # Управляющий сенсор
    def input_control_sensor_2_positiv(self, locator=control_sensor_out):
        self.input_100_positiv(locator)

    # Управляющий сенсор
    def input_control_sensor_2_negativ(self, locator=control_sensor_out):
        self.input_100_negativ(locator)

    # Раскрытие Список событий Выход 1/2
    def open_list_of_events(self):
        with allure.step("Раскрытие Список событий  - Выход 1"):
            self.app.method.click((By.XPATH, list_of_events_1))
        with allure.step("Раскрытие Список событий  - Выход 2"):
            self.app.method.click((By.XPATH, list_of_events_2))

    # Раскрытие маска включения Выход 1
    def open_mask_on_out_1(self):
        with allure.step("Раскрытие маска включения - Выход 1"):
            time.sleep(0.5)
            self.app.method.click((By.XPATH, mask_on_settings_out_1))
            time.sleep(0.5)

    # Выбор режима работы - ВЫХОД № 1/2
    def select_working_mode(self, position: str):
        with allure.step(f"Световая индикация - {position}"):
            self.app.method.Select_from_the_dropdown_list_by_name(button=Working_mode_out_1, position=position)
        with allure.step(f"Звуковая индикация - {position}"):
            self.app.method.Select_from_the_dropdown_list_by_name(button=Working_mode_out_2, position=position)

    # Раскрытие маска включения Выход 2
    def open_mask_on_out_2(self):
        with allure.step("Раскрытие маска включения  - Выход 2"):
            self.app.method.click((By.XPATH, mask_on_settings_out_2))

    # Раскрытие маска выключения Выход 1
    def open_mask_off_out_1(self):
        with allure.step("Раскрытие маска выключения - Выход 1"):
            time.sleep(0.5)
            self.app.method.click((By.XPATH, mask_off_settings_out_1))
            time.sleep(0.5)

    # Раскрытие маска выключения Выход 2
    def open_mask_off_out_2(self):
        with allure.step("Раскрытие маска выключения  - Выход 2"):
            self.app.method.click((By.XPATH, mask_off_settings_out_2))

    # Включение чекбоксов Режим работы: Событийный - Выходы - 1/2
    def check_box_event_on(self):
        with allure.step("Чекбокс: Взятие"):
            self.app.method.checkBox("ON", out_1_take_on_click, out_1_take_on_status)
            self.app.method.assertCheckBox("ON", out_1_take_on_status)
            self.app.method.checkBox("ON", out_2_take_on_click, out_2_take_on_status)
            self.app.method.assertCheckBox("ON", out_2_take_on_status)
        with allure.step("Чекбокс: Снятие"):
            self.app.method.checkBox("ON", out_1_take_off_click, out_1_take_off_status)
            self.app.method.assertCheckBox("ON", out_1_take_off_status)
            self.app.method.checkBox("ON", out_2_take_off_click, out_2_take_off_status)
            self.app.method.assertCheckBox("ON", out_2_take_off_status)
        with allure.step("Чекбокс: Принудительное взятие"):
            self.app.method.checkBox("ON", out_1_forced_take_click, out_1_forced_take_status)
            self.app.method.assertCheckBox("ON", out_1_forced_take_status)
            self.app.method.checkBox("ON", out_2_forced_take_click, out_2_forced_take_status)
            self.app.method.assertCheckBox("ON", out_2_forced_take_status)
        with allure.step("Чекбокс: Невзятие"):
            self.app.method.checkBox("ON", out_1_not_taking_click, out_1_not_taking_status)
            self.app.method.assertCheckBox("ON", out_1_not_taking_status)
            self.app.method.checkBox("ON", out_2_not_taking_click, out_2_not_taking_status)
            self.app.method.assertCheckBox("ON", out_2_not_taking_status)
        with allure.step("Чекбокс: Пожар"):
            self.app.method.checkBox("ON", out_1_fire_click, out_1_fire_status)
            self.app.method.assertCheckBox("ON", out_1_fire_status)
            self.app.method.checkBox("ON", out_2_fire_click, out_2_fire_status)
            self.app.method.assertCheckBox("ON", out_2_fire_status)
        with allure.step("Чекбокс: Тревога"):
            self.app.method.checkBox("ON", out_1_alarm_click, out_1_alarm_status)
            self.app.method.assertCheckBox("ON", out_1_alarm_status)
            self.app.method.checkBox("ON", out_2_alarm_click, out_2_alarm_status)
            self.app.method.assertCheckBox("ON", out_2_alarm_status)

    # Выключение чекбоксов Режим работы: Событийный - Выходы - 1/2
    def check_box_event_off(self):
        with allure.step("Чекбокс: Взятие"):
            self.app.method.checkBox("OFF", out_1_take_on_click, out_1_take_on_status)
            self.app.method.assertCheckBox("OFF", out_1_take_on_status)
            self.app.method.checkBox("OFF", out_2_take_on_click, out_2_take_on_status)
            self.app.method.assertCheckBox("OFF", out_2_take_on_status)
        with allure.step("Чекбокс: Снятие"):
            self.app.method.checkBox("OFF", out_1_take_off_click, out_1_take_off_status)
            self.app.method.assertCheckBox("OFF", out_1_take_off_status)
            self.app.method.checkBox("OFF", out_2_take_off_click, out_2_take_off_status)
            self.app.method.assertCheckBox("OFF", out_2_take_off_status)
        with allure.step("Чекбокс: Принудительное взятие"):
            self.app.method.checkBox("OFF", out_1_forced_take_click, out_1_forced_take_status)
            self.app.method.assertCheckBox("OFF", out_1_forced_take_status)
            self.app.method.checkBox("OFF", out_2_forced_take_click, out_2_forced_take_status)
            self.app.method.assertCheckBox("OFF", out_2_forced_take_status)
        with allure.step("Чекбокс: Невзятие"):
            self.app.method.checkBox("OFF", out_1_not_taking_click, out_1_not_taking_status)
            self.app.method.assertCheckBox("OFF", out_1_not_taking_status)
            self.app.method.checkBox("OFF", out_2_not_taking_click, out_2_not_taking_status)
            self.app.method.assertCheckBox("OFF", out_2_not_taking_status)
        with allure.step("Чекбокс: Пожар"):
            self.app.method.checkBox("OFF", out_1_fire_click, out_1_fire_status)
            self.app.method.assertCheckBox("OFF", out_1_fire_status)
            self.app.method.checkBox("OFF", out_2_fire_click, out_2_fire_status)
            self.app.method.assertCheckBox("OFF", out_2_fire_status)
        with allure.step("Чекбокс: Тревога"):
            self.app.method.checkBox("OFF", out_1_alarm_click, out_1_alarm_status)
            self.app.method.assertCheckBox("OFF", out_1_alarm_status)
            self.app.method.checkBox("OFF", out_2_alarm_click, out_2_alarm_status)
            self.app.method.assertCheckBox("OFF", out_2_alarm_status)

    # Частичное включение чекбоксов Режим работы: Событийный - Выходы - 1/2
    def check_box_event_some(self):
        with allure.step("Чекбокс: Взятие"):
            self.app.method.checkBox("ON", out_1_take_on_click, out_1_take_on_status)
            self.app.method.assertCheckBox("ON", out_1_take_on_status)
            self.app.method.checkBox("ON", out_2_take_on_click, out_2_take_on_status)
            self.app.method.assertCheckBox("ON", out_2_take_on_status)
        with allure.step("Чекбокс: Снятие"):
            self.app.method.checkBox("OFF", out_1_take_off_click, out_1_take_off_status)
            self.app.method.assertCheckBox("OFF", out_1_take_off_status)
            self.app.method.checkBox("OFF", out_2_take_off_click, out_2_take_off_status)
            self.app.method.assertCheckBox("OFF", out_2_take_off_status)
        with allure.step("Чекбокс: Принудительное взятие"):
            self.app.method.checkBox("ON", out_1_forced_take_click, out_1_forced_take_status)
            self.app.method.assertCheckBox("ON", out_1_forced_take_status)
            self.app.method.checkBox("ON", out_2_forced_take_click, out_2_forced_take_status)
            self.app.method.assertCheckBox("ON", out_2_forced_take_status)
        with allure.step("Чекбокс: Невзятие"):
            self.app.method.checkBox("OFF", out_1_not_taking_click, out_1_not_taking_status)
            self.app.method.assertCheckBox("OFF", out_1_not_taking_status)
            self.app.method.checkBox("OFF", out_2_not_taking_click, out_2_not_taking_status)
            self.app.method.assertCheckBox("OFF", out_2_not_taking_status)
        with allure.step("Чекбокс: Пожар"):
            self.app.method.checkBox("ON", out_1_fire_click, out_1_fire_status)
            self.app.method.assertCheckBox("ON", out_1_fire_status)
            self.app.method.checkBox("ON", out_2_fire_click, out_2_fire_status)
            self.app.method.assertCheckBox("ON", out_2_fire_status)
        with allure.step("Чекбокс: Тревога"):
            self.app.method.checkBox("OFF", out_1_alarm_click, out_1_alarm_status)
            self.app.method.assertCheckBox("OFF", out_1_alarm_status)
            self.app.method.checkBox("OFF", out_2_alarm_click, out_2_alarm_status)
            self.app.method.assertCheckBox("OFF", out_2_alarm_status)

        with allure.step("Чекбокс: Взятие"):
            self.app.method.checkBox("OFF", out_1_take_on_click, out_1_take_on_status)
            self.app.method.assertCheckBox("OFF", out_1_take_on_status)
            self.app.method.checkBox("OFF", out_2_take_on_click, out_2_take_on_status)
            self.app.method.assertCheckBox("OFF", out_2_take_on_status)
        with allure.step("Чекбокс: Снятие"):
            self.app.method.checkBox("ON", out_1_take_off_click, out_1_take_off_status)
            self.app.method.assertCheckBox("ON", out_1_take_off_status)
            self.app.method.checkBox("ON", out_2_take_off_click, out_2_take_off_status)
            self.app.method.assertCheckBox("ON", out_2_take_off_status)
        with allure.step("Чекбокс: Принудительное взятие"):
            self.app.method.checkBox("OFF", out_1_forced_take_click, out_1_forced_take_status)
            self.app.method.assertCheckBox("OFF", out_1_forced_take_status)
            self.app.method.checkBox("OFF", out_2_forced_take_click, out_2_forced_take_status)
            self.app.method.assertCheckBox("OFF", out_2_forced_take_status)
        with allure.step("Чекбокс: Невзятие"):
            self.app.method.checkBox("ON", out_1_not_taking_click, out_1_not_taking_status)
            self.app.method.assertCheckBox("ON", out_1_not_taking_status)
            self.app.method.checkBox("ON", out_2_not_taking_click, out_2_not_taking_status)
            self.app.method.assertCheckBox("ON", out_2_not_taking_status)
        with allure.step("Чекбокс: Пожар"):
            self.app.method.checkBox("OFF", out_1_fire_click, out_1_fire_status)
            self.app.method.assertCheckBox("OFF", out_1_fire_status)
            self.app.method.checkBox("OFF", out_2_fire_click, out_2_fire_status)
            self.app.method.assertCheckBox("OFF", out_2_fire_status)
        with allure.step("Чекбокс: Тревога"):
            self.app.method.checkBox("ON", out_1_alarm_click, out_1_alarm_status)
            self.app.method.assertCheckBox("ON", out_1_alarm_status)
            self.app.method.checkBox("ON", out_2_alarm_click, out_2_alarm_status)
            self.app.method.assertCheckBox("ON", out_2_alarm_status)

        with allure.step("Чекбокс: Взятие"):
            self.app.method.checkBox("ON", out_1_take_on_click, out_1_take_on_status)
            self.app.method.assertCheckBox("ON", out_1_take_on_status)
            self.app.method.checkBox("OFF", out_2_take_on_click, out_2_take_on_status)
            self.app.method.assertCheckBox("OFF", out_2_take_on_status)
        with allure.step("Чекбокс: Снятие"):
            self.app.method.checkBox("ON", out_1_take_off_click, out_1_take_off_status)
            self.app.method.assertCheckBox("ON", out_1_take_off_status)
            self.app.method.checkBox("OFF", out_2_take_off_click, out_2_take_off_status)
            self.app.method.assertCheckBox("OFF", out_2_take_off_status)
        with allure.step("Чекбокс: Принудительное взятие"):
            self.app.method.checkBox("ON", out_1_forced_take_click, out_1_forced_take_status)
            self.app.method.assertCheckBox("ON", out_1_forced_take_status)
            self.app.method.checkBox("OFF", out_2_forced_take_click, out_2_forced_take_status)
            self.app.method.assertCheckBox("OFF", out_2_forced_take_status)
        with allure.step("Чекбокс: Невзятие"):
            self.app.method.checkBox("ON", out_1_not_taking_click, out_1_not_taking_status)
            self.app.method.assertCheckBox("ON", out_1_not_taking_status)
            self.app.method.checkBox("OFF", out_2_not_taking_click, out_2_not_taking_status)
            self.app.method.assertCheckBox("OFF", out_2_not_taking_status)
        with allure.step("Чекбокс: Пожар"):
            self.app.method.checkBox("ON", out_1_fire_click, out_1_fire_status)
            self.app.method.assertCheckBox("ON", out_1_fire_status)
            self.app.method.checkBox("OFF", out_2_fire_click, out_2_fire_status)
            self.app.method.assertCheckBox("OFF", out_2_fire_status)
        with allure.step("Чекбокс: Тревога"):
            self.app.method.checkBox("ON", out_1_alarm_click, out_1_alarm_status)
            self.app.method.assertCheckBox("ON", out_1_alarm_status)
            self.app.method.checkBox("OFF", out_2_alarm_click, out_2_alarm_status)
            self.app.method.assertCheckBox("OFF", out_2_alarm_status)

        with allure.step("Чекбокс: Взятие"):
            self.app.method.checkBox("OFF", out_1_take_on_click, out_1_take_on_status)
            self.app.method.assertCheckBox("OFF", out_1_take_on_status)
            self.app.method.checkBox("ON", out_2_take_on_click, out_2_take_on_status)
            self.app.method.assertCheckBox("ON", out_2_take_on_status)
        with allure.step("Чекбокс: Снятие"):
            self.app.method.checkBox("OFF", out_1_take_off_click, out_1_take_off_status)
            self.app.method.assertCheckBox("OFF", out_1_take_off_status)
            self.app.method.checkBox("ON", out_2_take_off_click, out_2_take_off_status)
            self.app.method.assertCheckBox("ON", out_2_take_off_status)
        with allure.step("Чекбокс: Принудительное взятие"):
            self.app.method.checkBox("OFF", out_1_forced_take_click, out_1_forced_take_status)
            self.app.method.assertCheckBox("OFF", out_1_forced_take_status)
            self.app.method.checkBox("ON", out_2_forced_take_click, out_2_forced_take_status)
            self.app.method.assertCheckBox("ON", out_2_forced_take_status)
        with allure.step("Чекбокс: Невзятие"):
            self.app.method.checkBox("OFF", out_1_not_taking_click, out_1_not_taking_status)
            self.app.method.assertCheckBox("OFF", out_1_not_taking_status)
            self.app.method.checkBox("ON", out_2_not_taking_click, out_2_not_taking_status)
            self.app.method.assertCheckBox("ON", out_2_not_taking_status)
        with allure.step("Чекбокс: Пожар"):
            self.app.method.checkBox("OFF", out_1_fire_click, out_1_fire_status)
            self.app.method.assertCheckBox("OFF", out_1_fire_status)
            self.app.method.checkBox("ON", out_2_fire_click, out_2_fire_status)
            self.app.method.assertCheckBox("ON", out_2_fire_status)
        with allure.step("Чекбокс: Тревога"):
            self.app.method.checkBox("OFF", out_1_alarm_click, out_1_alarm_status)
            self.app.method.assertCheckBox("OFF", out_1_alarm_status)
            self.app.method.checkBox("ON", out_2_alarm_click, out_2_alarm_status)
            self.app.method.assertCheckBox("ON", out_2_alarm_status)

    # Проверка активации кнопки Выходы Режим работы: Событийный
    def check_button_activation(self, locator):
        with allure.step("Клик по кнопке"):
            self.app.method.click((By.XPATH, locator))
        with allure.step("Проверка активации кнопки"):
            self.app.method.status_outs_button((By.XPATH, locator))

    # Выбор событий при нажатии на кнопку
    def check_event_selection_on(self):
        with allure.step("Проверка активации кнопки: Взятие"):
            with allure.step("Выход 1"):
                self.check_button_activation(out_1_take_on_button)
            with allure.step("Выход 2"):
                self.check_button_activation(out_2_take_on_button)
        with allure.step("Проверка активации кнопки: Снятие"):
            with allure.step("Выход 1"):
                self.check_button_activation(out_1_take_off_button)
            with allure.step("Выход 2"):
                self.check_button_activation(out_2_take_off_button)
        with allure.step("Проверка активации кнопки: Принудительное взятие"):
            with allure.step("Выход 1"):
                self.check_button_activation(out_1_forced_take_button)
            with allure.step("Выход 2"):
                self.check_button_activation(out_2_forced_take_button)
        with allure.step("Проверка активации кнопки: Невзятие"):
            with allure.step("Выход 1"):
                self.check_button_activation(out_1_not_taking_button)
            with allure.step("Выход 2"):
                self.check_button_activation(out_2_not_taking_button)
        with allure.step("Проверка активации кнопки: Пожар"):
            with allure.step("Выход 1"):
                self.check_button_activation(out_1_fire_button)
            with allure.step("Выход 2"):
                self.check_button_activation(out_2_fire_button)
        with allure.step("Проверка активации кнопки: Тревога"):
            with allure.step("Выход 1"):
                self.check_button_activation(out_1_alarm_button)
            with allure.step("Выход 2"):
                self.check_button_activation(out_2_alarm_button)

    # Изменение настроек Выходы Режим работы: Событийный
    def change_settings_outs_events(self):
        with allure.step("Проверка отсутствия возможности внести настройки при деактивированном состоянии"):
            with allure.step("Выход 1"):
                self.check_button_activation(out_1_take_on_button)
                self.app.method.checkBox("OFF", out_1_take_on_click, out_1_take_on_status)
            # with allure.step("Выход 2"):

    # Изменение настроек Выходы Режим работы: Событийный
    def settings_outs_events_off(self):
        with allure.step("Проверка отсутствия возможности внести настройки при деактивированном состоянии Выход 1"):
            with allure.step("Взятие"):
                self.deactivated_check_outs_1(out_1_take_on_button)
            with allure.step("Снятие"):
                self.deactivated_check_outs_1(out_1_take_off_button)
            with allure.step("Принудительное взятие"):
                self.deactivated_check_outs_1(out_1_forced_take_button)
            with allure.step("Невзятие"):
                self.deactivated_check_outs_1(out_1_not_taking_button)
            with allure.step("Пожар"):
                self.deactivated_check_outs_1(out_1_fire_button)
            with allure.step("Тревога"):
                self.deactivated_check_outs_1(out_1_alarm_button)
        with allure.step("Проверка отсутствия возможности внести настройки при деактивированном состоянии Выход 2"):
            with allure.step("Взятие"):
                self.deactivated_check_outs_2(out_2_take_on_button)
            with allure.step("Снятие"):
                self.deactivated_check_outs_2(out_2_take_off_button)
            with allure.step("Принудительное взятие"):
                self.deactivated_check_outs_2(out_2_forced_take_button)
            with allure.step("Невзятие"):
                self.deactivated_check_outs_2(out_2_not_taking_button)
            with allure.step("Пожар"):
                self.deactivated_check_outs_2(out_2_fire_button)
            with allure.step("Тревога"):
                self.deactivated_check_outs_2(out_2_alarm_button)

    # Проверка настроек ВЫХОД 1
    def deactivated_check_outs_1(self, locator):
        self.check_button_activation(locator)
        self.settings_out_1_status()

    # Проверка настроек ВЫХОД 2
    def deactivated_check_outs_2(self, locator):
        self.check_button_activation(locator)
        self.settings_out_2_status()

    # Проверка дизактивированных настроек выход 1
    def settings_out_1_status(self):
        wd = self.app.wd
        with allure.step("Проверка дезактивации настроек виджета ползунка"):
            widget = wd.find_element(By.XPATH, time_widget_out_1_class)
            assert widget.get_property("className") == "b-range-slider b-range-slider-disabled", \
                f"Ошибка настройки виджета ползунка доступны для изменений"
        with allure.step("Проверка дезактивации настроек тумблера"):
            tumbler = wd.find_element(By.XPATH, off_end_tumbler_out_1_status)
            assert tumbler.get_attribute("disabled") == "true", f"Ошибка настройки тумблера доступны для изменений"
        with allure.step("Проверка дезактивации настроек маски"):
            mask = wd.find_element(By.XPATH, (str(mask_settings_status + '[1]')))
            assert mask.get_attribute("disabled") == "true", f"Ошибка настройки маски доступны для изменений"
        with allure.step("Проверка дезактивации настроек кода"):
            code_setting = wd.find_element(By.XPATH, code_setting_out_1)
            assert code_setting.get_attribute("disabled") == "true", f"Ошибка настройки поля код доступны для изменений"

    # Проверка дизактивированных настроек выход 2
    def settings_out_2_status(self):
        wd = self.app.wd
        with allure.step("Проверка дезактивации настроек виджета ползунка"):
            widget = wd.find_element(By.XPATH, time_widget_out_2_class)
            assert widget.get_property(
                "className") == "b-range-slider b-range-slider-disabled", f"Ошибка настройки виджета ползунка доступны для изменений"
        with allure.step("Проверка дезактивации настроек тумблера"):
            tumbler = wd.find_element(By.XPATH, off_end_tumbler_out_2_status)
            assert tumbler.get_attribute("disabled") == "true", f"Ошибка настройки тумблера доступны для изменений"
        with allure.step("Проверка дезактивации настроек маски"):
            mask = wd.find_element(By.XPATH, (str(mask_settings_status + '[17]')))
            assert mask.get_attribute("disabled") == "true", f"Ошибка настройки маски доступны для изменений"
        with allure.step("Проверка дезактивации настроек кода"):
            code_setting = wd.find_element(By.XPATH, code_setting_out_2)
            assert code_setting.get_attribute("disabled") == "true", f"Ошибка настройки поля код доступны для изменений"

    # Проверка виджета ползунка
    def widget_volum(self, locator):
        try:
            for i in range(1, 1023, 500):
                self.app.method.sliderWidgetExit(i, locator)
                self.app.method.assertSliderWidget(i, locator)
        except Exception as exc:
            assert exc == TimeoutException, f"Ошибка виджета ползунка!\nНе найден локатор: '{locator}'"

    # Проверка тумблера Включить по окончанию
    def tumbler_check(self, t_status, t_click):
        self.app.method.checkBox("ON", t_click, t_status)
        self.app.method.assertCheckBox("ON", t_status)
        self.app.method.checkBox("OFF", t_click, t_status)
        self.app.method.assertCheckBox("OFF", t_status)

    # Маска выход 1
    def mask_out_1(self):
        try:
            for i in range(1, 17):
                self.app.method.checkBox("ON", (mask_settings_click + f"[{i}]"), (mask_settings_status + f"[{i}]"))
                self.app.method.assertCheckBox("ON", (mask_settings_status + f"[{i}]"))
            for i in range(1, 17):
                self.app.method.checkBox("OFF", (mask_settings_click + f"[{i}]"), (mask_settings_status + f"[{i}]"))
                self.app.method.assertCheckBox("OFF", (mask_settings_status + f"[{i}]"))
        except Exception as exc:
            assert exc == TimeoutException, f"Ошибка Выбора маски!\nНе найден локатор: '{mask_settings_click}' + index"

    # Маска выход 1
    def mask_out_2(self):
        try:
            for i in range(17, 33):
                self.app.method.checkBox("ON", (mask_settings_click + f"[{i}]"), (mask_settings_status + f"[{i}]"))
                self.app.method.assertCheckBox("ON", (mask_settings_status + f"[{i}]"))
            for i in range(17, 33):
                self.app.method.checkBox("OFF", (mask_settings_click + f"[{i}]"), (mask_settings_status + f"[{i}]"))
                self.app.method.assertCheckBox("OFF", (mask_settings_status + f"[{i}]"))
        except Exception as exc:
            assert exc == TimeoutException, f"Ошибка Выбора маски!\nНе найден локатор: '{mask_settings_click}' + index"

    # Маска выход 2 -маска включения
    def mask_out_2_mask_on(self):
        try:
            for i in range(33, 49):
                self.app.method.checkBox("ON", (mask_settings_click + f"[{i}]"), (mask_settings_status + f"[{i}]"))
                self.app.method.assertCheckBox("ON", (mask_settings_status + f"[{i}]"))
            for i in range(33, 49):
                self.app.method.checkBox("OFF", (mask_settings_click + f"[{i}]"), (mask_settings_status + f"[{i}]"))
                self.app.method.assertCheckBox("OFF", (mask_settings_status + f"[{i}]"))
        except Exception as exc:
            assert exc == TimeoutException, f"Ошибка Выбора маски!\nНе найден локатор: '{mask_settings_click}' + index"

    # Маска выход 2 -маска выключения
    def mask_out_2_mask_off(self):
        try:
            for i in range(49, 65):
                self.app.method.checkBox("ON", (mask_settings_click + f"[{i}]"), (mask_settings_status + f"[{i}]"))
                self.app.method.assertCheckBox("ON", (mask_settings_status + f"[{i}]"))
            for i in range(49, 65):
                self.app.method.checkBox("OFF", (mask_settings_click + f"[{i}]"), (mask_settings_status + f"[{i}]"))
                self.app.method.assertCheckBox("OFF", (mask_settings_status + f"[{i}]"))
        except Exception as exc:
            assert exc == TimeoutException, f"Ошибка Выбора маски!\nНе найден локатор: '{mask_settings_click}' + index"

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

    # Поле ввода Код настройки
    def input_cod_setting(self, locator):
        with allure.step("Позитивные проверки ввода"):
            self.input_cod_posutiv(locator)
        with allure.step("Негативные проверки ввода"):
            self.input_cod_negativ(locator)

    # Общий метод для проверки настроек выход 1
    def settings_out_1(self):
        with allure.step("Проверка виджета ползунка"):
            self.widget_volum(widget_out_1)
        with allure.step("Проверка переключения тумблера"):
            self.tumbler_check(off_end_tumbler_out_1_status, off_end_tumbler_out_1_click)
        with allure.step("Проверка выбора маски"):
            self.mask_out_1()
        with allure.step("Проверка ввода значений в поле код настройки"):
            self.input_cod_setting(code_setting_out_1)

    # Общий метод для проверки настроек выход 1
    def settings_out_2(self):
        with allure.step("Проверка виджета ползунка"):
            self.widget_volum(widget_out_2)
        with allure.step("Проверка переключения тумблера"):
            self.tumbler_check(off_end_tumbler_out_2_status, off_end_tumbler_out_2_click)
        with allure.step("Проверка выбора маски"):
            self.mask_out_2()
        with allure.step("Проверка ввода значений в поле код настройки"):
            self.input_cod_setting(code_setting_out_2)

    # Общий метод для проверки настроек выход 2
    def settings_inclusion_masks_out_2_off(self):
        with allure.step("Проверка виджета ползунка"):
            self.widget_volum(widget_out_2_mask_settings_off)
        with allure.step("Проверка переключения тумблера"):
            self.tumbler_check(mask_settings_tumbler_out_1_status_off, mask_settings_tumbler_out_1_click_off)
        with allure.step("Проверка выбора маски"):
            self.mask_out_2_mask_off()
        with allure.step("Проверка ввода значений в поле код настройки"):
            self.input_cod_setting(code_setting_out_mask_2_off)

    # Общий метод для проверки настроек выход 2
    def settings_inclusion_masks_out_2_on(self):
        with allure.step("Проверка виджета ползунка"):
            self.widget_volum(widget_out_2_mask_settings_on)
        with allure.step("Проверка переключения тумблера"):
            self.tumbler_check(mask_settings_tumbler_out_1_status_on, mask_settings_tumbler_out_1_click_on)
        with allure.step("Проверка выбора маски"):
            self.mask_out_2_mask_on()
        with allure.step("Проверка ввода значений в поле код настройки"):
            self.input_cod_setting(code_setting_out_mask_2_on)

    # ВЫХОД 1 - Проверка настроек Взятие
    def out_1_check_settings_take_on_event(self):
        with allure.step("Активация настроек"):
            self.check_button_activation(out_1_take_on_button)
            self.app.method.checkBox("ON", out_1_take_on_click, out_1_take_on_status)
            self.settings_out_1()

    # ВЫХОД 1 - Проверка настроек Снятие
    def out_1_check_settings_take_off_event(self):
        with allure.step("Активация настроек"):
            self.check_button_activation(out_1_take_off_button)
            self.app.method.checkBox("ON", out_1_take_off_click, out_1_take_off_status)
            self.settings_out_1()

    # ВЫХОД 1 - Проверка настроек Принудительное взятие
    def out_1_check_settings_forced_take_event(self):
        with allure.step("Активация настроек"):
            self.check_button_activation(out_1_forced_take_button)
            self.app.method.checkBox("ON", out_1_forced_take_click, out_1_forced_take_status)
            self.settings_out_1()

    # ВЫХОД 1 - Проверка настроек Невзятие
    def out_1_check_settings_not_taking_event(self):
        with allure.step("Активация настроек"):
            self.check_button_activation(out_1_not_taking_button)
            self.app.method.checkBox("ON", out_1_not_taking_click, out_1_not_taking_status)
            self.settings_out_1()

    # ВЫХОД 1 - Проверка настроек Пожар
    def out_1_check_settings_fire_event(self):
        with allure.step("Активация настроек"):
            self.check_button_activation(out_1_fire_button)
            self.app.method.checkBox("ON", out_1_fire_click, out_1_fire_status)
            self.settings_out_1()

    # ВЫХОД 1 - Проверка настроек Тревога
    def out_1_check_settings_alarm_event(self):
        with allure.step("Активация настроек"):
            self.check_button_activation(out_1_alarm_button)
            self.app.method.checkBox("ON", out_1_alarm_click, out_1_alarm_status)
            self.settings_out_1()

    # ВЫХОД 2 - Проверка настроек Взятие
    def out_2_check_settings_take_on_event(self):
        with allure.step("Активация настроек"):
            self.check_button_activation(out_2_take_on_button)
            self.app.method.checkBox("ON", out_2_take_on_click, out_2_take_on_status)
            self.settings_out_2()

    # ВЫХОД 2 - Проверка настроек Снятие
    def out_2_check_settings_take_off_event(self):
        with allure.step("Активация настроек"):
            self.check_button_activation(out_2_take_off_button)
            self.app.method.checkBox("ON", out_2_take_off_click, out_2_take_off_status)
            self.settings_out_2()

    # ВЫХОД 2 - Проверка настроек Принудительное взятие
    def out_2_check_settings_forced_take_event(self):
        with allure.step("Активация настроек"):
            self.check_button_activation(out_2_forced_take_button)
            self.app.method.checkBox("ON", out_2_forced_take_click, out_2_forced_take_status)
            self.settings_out_2()

    # ВЫХОД 2 - Проверка настроек Невзятие
    def out_2_check_settings_not_taking_event(self):
        with allure.step("Активация настроек"):
            self.check_button_activation(out_2_not_taking_button)
            self.app.method.checkBox("ON", out_2_not_taking_click, out_2_not_taking_status)
            self.settings_out_2()

    # ВЫХОД 2 - Проверка настроек Пожар
    def out_2_check_settings_fire_event(self):
        with allure.step("Активация настроек"):
            self.check_button_activation(out_2_fire_button)
            self.app.method.checkBox("ON", out_2_fire_click, out_2_fire_status)
            self.settings_out_2()

    # ВЫХОД 2 - Проверка настроек Тревога
    def out_2_check_settings_alarm_event(self):
        with allure.step("Активация настроек"):
            self.check_button_activation(out_2_alarm_button)
            self.app.method.checkBox("ON", out_2_alarm_click, out_2_alarm_status)
            self.settings_out_2()

    # Проверка тумблеров
    def checked_Inversion_of_control_out_1(self):
        self.tumbler_check(Inversion_of_control_tumbler_out_1_status, Inversion_of_control_tumbler_out_1_click)

    # Проверка тумблеров
    def checked_Inversion_of_control_out_2(self):
        self.tumbler_check(Inversion_of_control_tumbler_out_2_status, Inversion_of_control_tumbler_out_2_click)

    # Настройка маски
    def out_1_inclusion_mask(self):
        self.settings_out_1()

    # Настройка маски
    def out_2_inclusion_mask(self):
        self.settings_out_2()

    # Настройка маски
    def out_1_shutdown_mask(self):
        self.settings_out_2()

    # Тумблеры Выход 1
    def tumblers_check_manege_mode_out_1(self):
        with allure.step("Проверка переключения тумблера - Разрешить управление по SMS"):
            self.tumbler_check(Allow_control_by_SMS_1_status, Allow_control_by_SMS_1_click)
        with allure.step("Проверка переключения тумблера - Разрешить управление звонком"):
            self.tumbler_check(Allow_call_control_1_status, Allow_call_control_1_click)
        with allure.step("Проверка переключения тумблера - Разрешить управление брелоком"):
            self.tumbler_check(Allow_key_control_1_status, Allow_key_control_1_click)

    # Тумблеры Выход 2
    def tumblers_check_manege_mode_out_2(self):
        with allure.step("Проверка переключения тумблера - Разрешить управление по SMS"):
            self.tumbler_check(Allow_control_by_SMS_2_status, Allow_control_by_SMS_2_click)
        with allure.step("Проверка переключения тумблера - Разрешить управление звонком"):
            self.tumbler_check(Allow_call_control_2_status, Allow_call_control_2_click)
        with allure.step("Проверка переключения тумблера - Разрешить управление брелоком"):
            self.tumbler_check(Allow_key_control_2_status, Allow_key_control_2_click)

    # Поверка сохранения режима работы выход 1
    def assert_operating_mod_out_1(self, operating_mod):
        with allure.step("Выпадающий список: Канал"):
            self.app.method.assertSelectionDropdownList(operating_mod, Working_mode_out_1)

    # Поверка сохранения режима работы выход 1 - Температурный
    def assert_operating_mod_out_1_temp(self, operating_mod):
        _out = self.app.read_data.data_out()
        with allure.step("Выпадающий список: Канал"):
            self.app.method.assertSelectionDropdownList(operating_mod, Working_mode_out_1)
        with allure.step(f"Гистерезис"):
            self.app.method.assertValues(value=_out['Gisteresis_outs'], locator=hysteresis_out)

    # Поверка сохранения режима работы выход 2
    def assert_operating_mod_out_2(self, operating_mod):
        with allure.step("Выпадающий список: Канал"):
            self.app.method.assertSelectionDropdownList(operating_mod, Working_mode_out_2)

    # Поверка сохранения режима работы выход 2 - ТЕМПЕРАТУРНЫЙ
    def assert_operating_mod_out_2_temp(self, operating_mod):
        _out = self.app.read_data.data_out()
        with allure.step("Выпадающий список: Канал"):
            self.app.method.assertSelectionDropdownList(operating_mod, Working_mode_out_2)
        with allure.step(f"Гистерезис"):
            self.app.method.assertValues(value=_out['Gisteresis_outs'], locator=hysteresis_out)

    # Ввод данных для сохранения режим работы: Событийный - Выход 1
    def save_out_1_data_event(self, event):
        self.operating_mod_event(event)

    # Поверка сохранения режим работы: Событийный - Выход 1
    def assert_save_out_1_data_event(self, event):
        self.assert_operating_mod_event(event)

    # Ввод данных для сохранения режим работы: Событийный - Выход 2
    def save_out_2_data_event(self, event):
        self.operating_mod_event(event)

    # Поверка сохранения режим работы: Событийный - Выход 2
    def assert_save_out_2_data_event(self, event):
        self.assert_operating_mod_event(event)

    # Метод ввод данных для сохранения режим работы: Событийный
    def operating_mod_event(self, event):
        with allure.step("Парсинг сгенерированных данных"):
            _out = self.app.read_data.data_out()
        with allure.step(f"Выбор кнопки: {event}"):
            self.check_button_activation(f'(//*[.="{event}"]//button)[1]')
        with allure.step(f"Выбор чек-бокса: {event}"):
            self.app.method.checkBox("ON",
                                     f'(//*[.="{event}"]//span[@class="checkmark-container"][1])[1]',
                                     f'(//*[.="{event}"]//label/input)[1]')
        with allure.step("Выбор виджета ползунка"):
            self.app.method.sliderWidgetExit(_out['Time_widget'], widget_out_1)
        with allure.step(
                f"Переключения тумблера 'Включить по окончанию' в положение: {_out['Tumbler_turn_on_when_finished']}"):
            self.app.method.checkBox(_out['Tumbler_turn_on_when_finished'],
                                     off_end_tumbler_out_1_click,
                                     off_end_tumbler_out_1_status)
        with allure.step("Выбора маски"):
            for i in range(1, 17):
                self.app.method.checkBox("OFF", (mask_settings_click + f"[{i}]"), (mask_settings_status + f"[{i}]"))
            self.app.method.checkBox("ON",
                                     (mask_settings_click + f"[{_out['Mask_random_out_1']}]"),
                                     (mask_settings_status + f"[{_out['Mask_random_out_1']}]"))

    # Метод проверки ввода данных для сохранения режим работы: Событийный
    def assert_operating_mod_event(self, event):
        with allure.step("Парсинг сгенерированных данных"):
            _out = self.app.read_data.data_out()
        with allure.step(f"Проверка выбора кнопки: {event}"):
            self.check_button_activation(f'(//*[.="{event}"]//button)[1]')
        with allure.step(f"Проверка выбор чек-бокса: {event}"):
            self.app.method.assertCheckBox("ON", f'(//*[.="{event}"]//label/input)[1]')
        with allure.step("Выбор виджета ползунка"):
            self.app.method.assertSliderWidget(_out['Time_widget'], widget_out_1)
        with allure.step("Проверка переключения тумблера"):
            self.app.method.assertCheckBox(_out['Tumbler_turn_on_when_finished'], off_end_tumbler_out_1_status)
        with allure.step("Проверка выбора маски"):
            self.app.method.assertCheckBox("ON", (mask_settings_status + f"[{_out['Mask_random_out_1']}]"))

    # Ввод данных для сохранения режим работы: Температурный - Выход 1
    def save_out_1_data_temp(self, ):
        self.operating_mod_temp()

    # Поверка сохранения режим работы: Температурный - Выход 1
    def assert_save_out_1_data_temp(self):
        self.assert_operating_mod_temp()

    # Метод ввод данных для сохранения режим работы: Температурный
    def operating_mod_temp(self):
        with allure.step("Парсинг сгенерированных данных"):
            _out = self.app.read_data.data_out()
        with allure.step(f"Ввод данных в поле Гистерезис:'{_out['Gisteresis_outs']}'"):
            self.app.method.inputValues(value=_out['Gisteresis_outs'], locator=hysteresis_out)
        with allure.step(f"Ввод данных в поле Внутренний сигнал задания:'{_out['Internal_reference_signal']}'"):
            self.app.method.inputValues(value=_out['Internal_reference_signal'], locator=control_sensor_out)
        with allure.step(
                f"Переключения тумблера 'Инверсия управления' в положение: {_out['Tumbler_inversion_of_control']}"):
            self.app.method.checkBox(_out['Tumbler_inversion_of_control'],
                                     Inversion_of_control_tumbler_out_1_click,
                                     Inversion_of_control_tumbler_out_1_status)

    # Метод проверки ввода данных для сохранения режим работы: Температурный
    def assert_operating_mod_temp(self):
        with allure.step("Парсинг сгенерированных данных"):
            _out = self.app.read_data.data_out()
        with allure.step(f"Проверка ввода данных в поле Гистерезис:'{_out['Gisteresis_outs']}'"):
            self.app.method.assertValues(value=_out['Gisteresis_outs'], locator=hysteresis_out)
        with allure.step(
                f"Проверка ввода данных в поле Внутренний сигнал задания:'{_out['Internal_reference_signal']}'"):
            self.app.method.assertValues(value=_out['Internal_reference_signal'], locator=control_sensor_out)
        with allure.step(
                f"Проверка переключения тумблера 'Инверсия управления' в положение: {_out['Tumbler_inversion_of_control']}"):
            self.app.method.assertCheckBox(_out['Tumbler_inversion_of_control'],
                                           Inversion_of_control_tumbler_out_1_status)

    # Ввод имя Выход 1
    def input_name_out_1_for_save(self):
        with allure.step("Парсинг сгенерированных данных"):
            _out = self.app.read_data.data_out()
        with allure.step(f"Ввод данных в поле Имя:'{_out['Out_name']}'"):
            self.app.method.inputValues(value=_out['Out_name'], locator=name_out_1)

    # Ввод имя Выход 2
    def input_name_out_2_for_save(self):
        with allure.step("Парсинг сгенерированных данных"):
            _out = self.app.read_data.data_out()
        with allure.step(f"Ввод данных в поле Имя:'{_out['Out_name']}'"):
            self.app.method.inputValues(value=_out['Out_name'], locator=name_out_2)

    # Проверка ввода имени выхода - Выход 1
    def assert_input_name_out_1_for_save(self):
        with allure.step("Парсинг сгенерированных данных"):
            _out = self.app.read_data.data_out()
        with allure.step(f"Проверка ввода данных в поле Гистерезис:'{_out['Out_name']}'"):
            self.app.method.assertValues(value=_out['Out_name'], locator=name_out_1)

    # Проверка ввода имени выхода - Выход 2
    def assert_input_name_out_2_for_save(self):
        with allure.step("Парсинг сгенерированных данных"):
            _out = self.app.read_data.data_out()
        with allure.step(f"Проверка ввода данных в поле Гистерезис:'{_out['Out_name']}'"):
            self.app.method.assertValues(value=_out['Out_name'], locator=name_out_2)

    # Ввод данных для сохранения режим работы: Управляемый - Выход 1
    def save_out_1_data_managed(self, Output_group_number):
        self.operating_mod_managed(Output_group_number)

    # Проверка ввода данных для сохранения режим работы: Управляемый - Выход 1
    def assert_save_out_1_data_managed(self, Output_group_number):
        self.assert_operating_mod_managed(Output_group_number)

    # Ввод данных для сохранения режим работы: Управляемый - Выход 2
    def save_out_2_data_managed(self, Output_group_number):
        self.operating_mod_managed(Output_group_number)

    # Проверка ввода данных для сохранения режим работы: Управляемый - Выход 2
    def assert_save_out_2_data_managed(self, Output_group_number):
        self.assert_operating_mod_managed(Output_group_number)

    # Метод ввод данных для сохранения режим работы: Управляемый
    def operating_mod_managed(self, position):
        with allure.step("Парсинг сгенерированных данных"):
            _out = self.app.read_data.data_out()

        with allure.step("Выбор виджета ползунка"):
            self.app.method.sliderWidgetExit(_out['Time_widget'], widget_out_1)
        with allure.step(
                f"Переключения тумблера 'Включить по окончанию' в положение: {_out['Tumbler_turn_on_when_finished']}"):
            self.app.method.checkBox(_out['Tumbler_turn_on_when_finished'],
                                     off_end_tumbler_out_1_click,
                                     off_end_tumbler_out_1_status)
        with allure.step("Выбор маски включения"):
            for i in range(1, 17):
                self.app.method.checkBox("OFF", (mask_settings_click + f"[{i}]"), (mask_settings_status + f"[{i}]"))
            self.app.method.checkBox("ON",
                                     (mask_settings_click + f"[{_out['Mask_random_out_1']}]"),
                                     (mask_settings_status + f"[{_out['Mask_random_out_1']}]"))

        with allure.step("Выбор виджета ползунка"):
            self.app.method.sliderWidgetExit(_out['Time_widget'], widget_out_2)
        with allure.step(
                f"Переключения тумблера 'Включить по окончанию' в положение: {_out['Tumbler_turn_on_when_finished']}"):
            self.app.method.checkBox(_out['Tumbler_turn_on_when_finished'],
                                     off_end_tumbler_out_2_click,
                                     off_end_tumbler_out_2_status)

        with allure.step("Выбор маски выключения"):
            for i in range(17, 33):
                self.app.method.checkBox("OFF", (mask_settings_click + f"[{i}]"), (mask_settings_status + f"[{i}]"))
            self.app.method.checkBox("ON",
                                     (mask_settings_click + f"[{_out['Mask_random_out_2']}]"),
                                     (mask_settings_status + f"[{_out['Mask_random_out_2']}]"))

        with allure.step(f"Выбор из выпадающего списка 'Номер группы выходов' - {position}"):
            self.app.method.Select_from_the_dropdown_list_by_name(button=Output_group_number, position=position)

        with allure.step(
                f"Переключения тумблера 'Разрешить управление по SMS' в положение: {_out['Tumbler_inversion_of_control']}"):
            self.app.method.checkBox(_out['Tumbler_inversion_of_control'],
                                     Allow_control_by_SMS_1_click,
                                     Allow_control_by_SMS_1_status)

        with allure.step(
                f"Переключения тумблера 'Разрешить управление звонком' в положение: {_out['tumbler_1']}"):
            self.app.method.checkBox(_out['tumbler_1'],
                                     Allow_call_control_1_click,
                                     Allow_call_control_1_status)

        with allure.step(
                f"Переключения тумблера 'Разрешить управление звонком' в положение: {_out['tumbler_2']}"):
            self.app.method.checkBox(_out['tumbler_2'],
                                     Allow_key_control_1_click,
                                     Allow_key_control_1_status)

    # Метод проверки ввода данных для сохранения режим работы: Управляемый
    def assert_operating_mod_managed(self, position):
        with allure.step("Парсинг сгенерированных данных"):
            _out = self.app.read_data.data_out()
        with allure.step("Проверка выбора виджета ползунка"):
            self.app.method.assertSliderWidget(_out['Time_widget'], widget_out_1)
        with allure.step(
                f"Проверка переключения тумблера 'Включить по окончанию' в положение: {_out['Tumbler_turn_on_when_finished']}"):
            self.app.method.assertCheckBox(_out['Tumbler_turn_on_when_finished'], off_end_tumbler_out_1_status)

        with allure.step("Проверка выбора маски включения"):
            self.app.method.assertCheckBox("ON", (mask_settings_status + f"[{_out['Mask_random_out_1']}]"))

        with allure.step("Проверка выбора виджета ползунка"):
            self.app.method.assertSliderWidget(_out['Time_widget'], widget_out_2)
        with allure.step(
                f"Проверка переключения тумблера 'Включить по окончанию' в положение: {_out['Tumbler_turn_on_when_finished']}"):
            self.app.method.assertCheckBox(_out['Tumbler_turn_on_when_finished'], off_end_tumbler_out_2_status)
        with allure.step("Проверка выбора маски выключения"):
            self.app.method.assertCheckBox("ON", (mask_settings_status + f"[{_out['Mask_random_out_2']}]"))

        with allure.step(f"Проверка выбора из выпадающего списка 'Номер группы выходов' - {position}"):
            self.app.method.assertSelectionDropdownList(position, Output_group_number)

        with allure.step(
                f"Проверка переключения тумблера 'Разрешить управление по SMS' в положение: {_out['Tumbler_inversion_of_control']}"):
            self.app.method.assertCheckBox(_out['Tumbler_inversion_of_control'], Allow_control_by_SMS_1_status)
        with allure.step(
                f"Проверка переключения тумблера 'Разрешить управление звонком' в положение: {_out['tumbler_1']}"):
            self.app.method.assertCheckBox(_out['tumbler_1'], Allow_call_control_1_status)
        with allure.step(
                f"Проверка переключения тумблера 'Разрешить управление звонком' в положение: {_out['tumbler_2']}"):
            self.app.method.assertCheckBox(_out['tumbler_2'], Allow_key_control_1_status)

    # Метод ввода данных для проверки сохранения раздела
    def input_path_data_for_save(self, tumbler_1, tumbler_2, tumbler_3):
        with allure.step("Парсинг сгенерированных данных"):
            _path = self.app.read_data.data_path()
        with allure.step(f"Ввод данных в поле Номер:'{_path['Number_path']}'"):
            self.app.method.inputValues(value=_path['Number_path'], locator=namber_path)
        with allure.step(f"Ввод данных в поле Название:'{_path['Name_path']}'"):
            self.app.method.inputValues(value=_path['Name_path'], locator=name_path)
        with allure.step(f"Переключение тумблера 'Задержка взятия' в положение: {tumbler_1}"):
            self.app.method.checkBox(tumbler_1, Take_Delay_click, Take_Delay_status)
        with allure.step(f"Переключение тумблера 'Автовзятие из невзятия' в положение: {tumbler_2}"):
            self.app.method.checkBox(tumbler_2, Auto_pickup_from_non_pickup_click, Auto_pickup_from_non_pickup_status)
        with allure.step(f"Переключение тумблера 'Автовзятие из тревоги' в положение: {tumbler_3}"):
            self.app.method.checkBox(tumbler_3, Auto_arm_from_alarm_click, Auto_arm_from_alarm_status)

    # Метод проверки  ввода данных для проверки сохранения раздела на странице
    def assert_input_path_for_save_on_page(self):
        with allure.step("Парсинг сгенерированных данных"):
            _path = self.app.read_data.data_path()
        with allure.step(f"Проверка данных на странице. Поле Номер:'{_path['Number_path']}'"):
            self.app.method.assertValuesOnPage(value=_path['Number_path'], locator=namber_path_on_page)
        with allure.step(f"Проверка данных на странице. Поле Название:'{_path['Name_path']}'"):
            self.app.method.assertValuesOnPage(value=_path['Name_path'], locator=name_path_on_page)

    # Метод проверки ввода данных для проверки сохранения раздела в настройках
    def assert_input_path_for_save_settings(self, tumbler_1, tumbler_2, tumbler_3):
        with allure.step("Парсинг сгенерированных данных"):
            _path = self.app.read_data.data_path()
        with allure.step(f"Проверка ввода данных в поле Номер:'{_path['Number_path']}'"):
            self.app.method.assertValues(value=_path['Number_path'], locator=namber_path)
        with allure.step(f"Проверка ввода данных в поле Название:'{_path['Name_path']}'"):
            self.app.method.assertValues(value=_path['Name_path'], locator=name_path)
        with allure.step(f"Проверка переключения тумблера 'Задержка взятия' в положение: {tumbler_1}"):
            self.app.method.assertCheckBox(tumbler_1, Take_Delay_status)
        with allure.step(f"Проверка переключения тумблера 'Автовзятие из невзятия' в положение: {tumbler_2}"):
            self.app.method.assertCheckBox(tumbler_2, Auto_pickup_from_non_pickup_status)
        with allure.step(f"Проверка переключения тумблера 'Автовзятие из тревоги' в положение: {tumbler_3}"):
            self.app.method.assertCheckBox(tumbler_3, Auto_arm_from_alarm_status)

    # Добавление разделов
    def assert_add_path_1(self):
        with allure.step("Генерация данных"):
            path_list = self.app.method.getElementsLen(path_row)
            for i in range(path_list, 16):
                with allure.step(f"Добавление раздела №{i}"):
                    self.app.ganerate_data.createData()
                    _path = self.app.read_data.data_path()
                    old_path_list = self.app.method.getElementsLen(path_row)
                    self.app.method.click((By.XPATH, add_path_button))
                    self.app.method.check_hide_element('div.modal.card button.BTN-indigo', save_button_path)
                    self.app.method.click((By.CSS_SELECTOR, 'button.close-icon'))
                    new_path_list = self.app.method.getElementsLen(path_row)
                    assert str(old_path_list + 1) == str(new_path_list), \
                        f"Раздел не добавлен!\n" \
                        f"Список разделов до дабовление:{old_path_list}\n" \
                        f"Список разделов после добавления{new_path_list}"

    # Добавление разделов
    def assert_add_path_2(self):
        with allure.step("Генерация данных"):
            path_list = self.app.method.getElementsLen(path_row)
            for i in range(path_list, 16):
                with allure.step(f"Добавление раздела №{i}"):
                    self.app.ganerate_data.createData()
                    _path = self.app.read_data.data_path()
                    old_path_list = self.app.method.getElementsLen(path_row)
                    self.app.method.click((By.XPATH, add_path_button))
                    # self.app.method.inputValues(value=_path['Number_path'], locator=namber_path)
                    self.app.method.inputValues(value=_path['Name_path'], locator=name_path)
                    self.app.method.click((By.XPATH, save_button_path))
                    with allure.step("Проверка всплывающего окна сохранено"):
                        self.app.method.click(
                            (By.XPATH, '/html/body//button[@class="toast-message-btn-close close-icon"]'))
                    time.sleep(1)
                    new_path_list = self.app.method.getElementsLen(path_row)
                    assert str(old_path_list + 1) == str(new_path_list), \
                        f"Раздел не добавлен!\n" \
                        f"Список разделов до дабовление:{old_path_list}\n" \
                        f"Список разделов после добавления{new_path_list}"

    # Добавление разделов для проверки ошибок
    def assert_error_window(self):
        with allure.step("Генерация данных"):
            path_list = self.app.method.getElementsLen(path_row)
            for i in range(path_list, 17):
                with allure.step(f"Добавление раздела №{i}"):
                    self.app.ganerate_data.createData()
                    # _path = self.app.read_data.data_path()
                    self.app.method.click((By.XPATH, add_path_button))
                    if i == 16:
                        self.app.method.inputValues(value=55, locator=namber_path)
                        self.app.method.click((By.XPATH, save_button_path))
                        break
                    # self.app.method.inputValues(value=_path['Number_path'], locator=namber_path)
                    # self.app.method.inputValues(value=_path['Name_path'], locator=name_path)
                    self.app.method.click((By.XPATH, save_button_path))
                    with allure.step("Проверка всплывающего окна сохранено"):
                        self.app.method.click(
                            (By.XPATH, '/html/body//button[@class="toast-message-btn-close close-icon"]'))
                    time.sleep(1)

        with allure.step("Проверка всплывающей подсказки"):
            text = 'Максимально допустимое количество ключей: 16.'
            actual_text = self.app.method.getText('//*[@class="toast-message-detail"]')
            assert text == actual_text, f"\nОшибка при проверке всплывающей подсказки!" \
                                        f"\nОжидаемый текст: '{text}'\nФактический текст: '{actual_text}'"
