# -*- coding: utf-8 -*-
import random
import time
from dataclasses import dataclass

import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from data.pages_text import *
from locators.settings_locators import *


@dataclass
class SettingsHelper:
    app: any

    # Ограничение 9999
    def input_number_9999(self, locator):
        with allure.step("Проверка ввода цифр"):
            for i in range(10):
                self.app.method.assertEqual(i, i, locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual(0, 0, locator)
            self.app.method.assertEqual(1, 1, locator)
            self.app.method.assertEqual(9998, 9998, locator)
            self.app.method.assertEqual(9999, 9999, locator)

    # Ограничение 9999
    def input_number_9999_negativ(self, locator):
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
            self.app.method.assertEqual('123  АБВABC!@#', '123', locator)
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
        with allure.step("Проверка ввода очень большого числа"):
            self.app.method.assertEqual(9 * 10000000000000, 9000, locator)
        with allure.step("Проверка ввода отрицательного числа"):
            self.app.method.assertEqual('-1', '1', locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual(99999, 9999, locator)

    # Проверка ввода поле
    def input_number_65535(self, locator):
        with allure.step("Проверка ввода цифр"):
            for i in range(10):
                self.app.method.assertEqual(i, i, locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual(0, 0, locator)
            self.app.method.assertEqual(1, 1, locator)
            self.app.method.assertEqual(65534, 65534, locator)
            self.app.method.assertEqual(65535, 65535, locator)

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
            self.app.method.assertEqual('123  АБВABC!@#', '123', locator)
        with allure.step("Проверка ввода пробелов"):
            # self.app.method.assertEqual('   ', '', locator)
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
        with allure.step("Проверка ввода очень большого числа"):
            self.app.method.assertEqual(9 * 10000000000000, 90000, locator)
        with allure.step("Проверка ввода отрицательного числа"):
            self.app.method.assertEqual('-1', '1', locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual(999999, 99999, locator)

    # Проверка ввода MAC адрес
    def input_mac_address(self, locator):
        with allure.step("Проверка ввода цифр"):
            for i in range(10):
                self.app.method.assertEqual(i, i, locator)
        with allure.step("Проверка ввода латинских букв в нижнем регистре"):
            self.app.method.assertEqual('ab:cd:ef', 'ab:cd:ef', locator)
        with allure.step("Проверка ввода латинских букв в верхнем регистре"):
            self.app.method.assertEqual('AB:CD:EF', 'AB:CD:EF', locator)
            self.app.method.assertEqual(":-", ":-", locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual(1, 1, locator)
            self.app.method.assertEqual(11111111111, '11:11:11:11:11:1', locator)
            self.app.method.assertEqual(111111111111, '11:11:11:11:11:11', locator)

    # Проверка ввода MAC адрес
    def input_mac_address_negativ(self, locator):
        with allure.step("Проверка ввода цифр"):
            self.app.method.assertEqual('1234567890', '12:34:56:78:90', locator)
        with allure.step("Проверка ввода латинских букв в нижнем регистре"):
            self.app.method.assertEqual('abcdefghijklmnopqrstuvwxyz', 'ab:cd:ef', locator)
        with allure.step("Проверка ввода латинских букв в верхнем регистре"):
            self.app.method.assertEqual('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'AB:CD:EF', locator)
        with allure.step("Проверка ввода Русских букв в нижнем регистре"):
            self.app.method.assertEqual("ёйцукенгшщзхъфывапролджэячсмитьбю", "", locator)
        with allure.step("Проверка ввода Русских букв в верхнем регистре"):
            self.app.method.assertEqual("АПРОЛДЖЭЯЧСМИТЬБЮЁЙЦУКЕНГШЩЗХЪФЫВ", "", locator)
        with allure.step("Проверка ввода спецсимволов"):
            self.app.method.assertEqual("!#$%&'()*+,:-./;<=>?@[]^_`{|}~", ":-", locator)
        with allure.step("Проверка ввода совместных значений(буквы/цифры/спецсимволы)"):
            self.app.method.assertEqual('123  АБВABC!@#-', '12:3A:BC-', locator)
        with allure.step("Проверка ввода пробелов"):
            self.app.method.assertEqual('   ', '', locator)
            self.app.method.assertEqual('123     ', '12:3', locator)
            self.app.method.assertEqual('   123', '12:3', locator)
            self.app.method.assertEqual('1 2 3', '12:3', locator)
        with allure.step("Проверка ввода дробного числа "):
            self.app.method.assertEqual('11.11', '11:11', locator)
            self.app.method.assertEqual('000.1', '00:01', locator)
            self.app.method.assertEqual('11,11', '11:11', locator)
            self.app.method.assertEqual('000,1', '00:01', locator)
        with allure.step("Проверка ввода пустого значения"):
            self.app.method.assertEqual('', '', locator)
        with allure.step("Проверка ввода очень большого числа"):
            self.app.method.assertEqual(9 * 10000000000000, '90:00:00:00:00:00', locator)
        with allure.step("Проверка ввода отрицательного числа"):
            self.app.method.assertEqual('-1', '-1', locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual(1111111111111, '11:11:11:11:11:11', locator)

    # Проверка ввода цифровое поле
    def input_number(self, locator):
        with allure.step("Проверка ввода цифр"):
            for i in range(10):
                self.app.method.assertEqual(i, i, locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual(0, 0, locator)
            self.app.method.assertEqual(1, 1, locator)
            self.app.method.assertEqual(998, 998, locator)
            self.app.method.assertEqual(999, 999, locator)

    # Проверка ввода цифровое поле
    def input_number_negativ(self, locator):
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
            self.app.method.assertEqual('123  АБВABC!@#', '123', locator)
        with allure.step("Проверка ввода пробелов"):
            self.app.method.assertEqual('   ', '', locator)
            self.app.method.assertEqual('123     ', '123', locator)
            self.app.method.assertEqual('   123', '123', locator)
            self.app.method.assertEqual('1 2 3', '123', locator)
        with allure.step("Проверка ввода дробного числа "):
            self.app.method.assertEqual('11.1', '111', locator)
            self.app.method.assertEqual('00.1', '1', locator)
            self.app.method.assertEqual('11,1', '111', locator)
            self.app.method.assertEqual('00,1', '1', locator)
        with allure.step("Проверка ввода пустого значения"):
            self.app.method.assertEqual('', '', locator)
        with allure.step("Проверка ввода очень большого числа"):
            self.app.method.assertEqual(9 * 10000000000000, 900, locator)
        with allure.step("Проверка ввода отрицательного числа"):
            self.app.method.assertEqual('-1', '1', locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual(9999, 999, locator)

    # Проверка ввода поле Название объекта
    def input_object_name(self, locator=object_name):
        with allure.step("Проверка ввода цифр"):
            for i in range(10):
                self.app.method.assertEqual(i, i, locator)
        with allure.step("Проверка ввода латинских букв в нижнем регистре"):
            self.app.method.assertEqual('abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz',
                                        locator)
        with allure.step("Проверка ввода латинских букв в врхнем регистре"):
            self.app.method.assertEqual('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                                        locator)
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
        with allure.step("Проверка ввода граничных значений внутри диапазона"):
            self.app.method.assertEqual(1, 1, locator)
            self.app.method.assertEqual('1' * 30, '1' * 30, locator)
            self.app.method.assertEqual('1' * 31, '1' * 31, locator)

    # Проверка ввода поле Название объекта
    def input_object_name_negativ(self, locator=object_name):
        with allure.step("Проверка ввода пустого значения"):
            self.app.method.assertEqual('', '', locator)
        with allure.step("Проверка ввода граничных значений внутри диапазона"):
            self.app.method.assertEqual('1' * 33, '1' * 31, locator)

    # Проверка ввода поле Название сервера
    def input_server_name(self, locator):
        with allure.step("Проверка ввода цифр"):
            for i in range(10):
                self.app.method.assertEqual(i, i, locator)
        with allure.step("Проверка ввода латинских букв в нижнем регистре"):
            self.app.method.assertEqual('abcdefghijk', 'abcdefghijk', locator)
            self.app.method.assertEqual('lmnopqrstuvwxyz', 'lmnopqrstuvwxyz', locator)
        with allure.step("Проверка ввода латинских букв в верхнем регистре"):
            self.app.method.assertEqual('ABCDEFGHIJK', 'ABCDEFGHIJK', locator)
            self.app.method.assertEqual('LMNOPQRSTUVWXYZ', 'LMNOPQRSTUVWXYZ', locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual(0, 0, locator)
            self.app.method.assertEqual(1, 1, locator)
            self.app.method.assertEqual('1' * 31, '1' * 31, locator)
            self.app.method.assertEqual('1' * 32, '1' * 32, locator)

    # Проверка ввода поле Название сервера
    def input_server_name_negativ(self, locator):
        with allure.step("Проверка ввода Русских букв в нижнем регистре"):
            self.app.method.assertEqual("ёйцукенгшщзхъфыв", "", locator)
            self.app.method.assertEqual("апролджэячсмитьбю", "", locator)
        with allure.step("Проверка ввода Русских букв в верхнем регистре"):
            self.app.method.assertEqual("АПРОЛДЖЭЯЧСМИТЬБЮ", "", locator)
            self.app.method.assertEqual("ЁЙЦУКЕНГШЩЗХЪФЫВ", "", locator)
        with allure.step("Проверка ввода спецсимволов"):
            self.app.method.assertEqual("!#$%&'()*+,-./:;<=>?@[]^_`{|}~", "", locator)
        with allure.step("Проверка ввода совместных значений(буквы/цифры/спецсимволы)"):
            self.app.method.assertEqual('123  АБВABC!@#', '123ABC', locator)
        with allure.step("Проверка ввода пробелов"):
            self.app.method.assertEqual('   ', '', locator)
            self.app.method.assertEqual('123     ', '123', locator)
            self.app.method.assertEqual('   123', '123', locator)
            self.app.method.assertEqual('1 2 3', '123', locator)
        with allure.step("Проверка ввода дробного числа "):
            self.app.method.assertEqual('11.11', '1111', locator)
            self.app.method.assertEqual('000.1', '0001', locator)
            self.app.method.assertEqual('11,11', '1111', locator)
            self.app.method.assertEqual('000,1', '0001', locator)
        with allure.step("Проверка ввода пустого значения"):
            self.app.method.assertEqual('', '', locator)
        with allure.step("Проверка ввода очень большого числа"):
            self.app.method.assertEqual(9999 * 1000000, 9999000000, locator)
        with allure.step("Проверка ввода отрицательного числа"):
            self.app.method.assertEqual('-1', '1', locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual('1' * 33, '1' * 32, locator)

    # Проверка ввода поле Адрес сервера
    def input_server_address(self, locator):
        with allure.step("Проверка ввода цифр"):
            for i in range(10):
                self.app.method.assertEqual(i, i, locator)
        with allure.step("Проверка ввода латинских букв в нижнем регистре"):
            self.app.method.assertEqual('abcdefghijk', 'abcdefghijk', locator)
            self.app.method.assertEqual('lmnopqrstuvwxyz', 'lmnopqrstuvwxyz', locator)
        with allure.step("Проверка ввода латинских букв в верхнем регистре"):
            self.app.method.assertEqual('ABCDEFGHIJK', 'ABCDEFGHIJK', locator)
            self.app.method.assertEqual('LMNOPQRSTUVWXYZ', 'LMNOPQRSTUVWXYZ', locator)
        with allure.step("Проверка ввода спецсимволов"):
            self.app.method.assertEqual("-.", "-.", locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual(0, 0, locator)
            self.app.method.assertEqual(1, 1, locator)
            self.app.method.assertEqual('1' * 22, '1' * 22, locator)
            self.app.method.assertEqual('1' * 23, '1' * 23, locator)

    # Проверка ввода поле Адрес сервера
    def input_server_address_negativ(self, locator):
        with allure.step("Проверка ввода Русских букв в нижнем регистре"):
            self.app.method.assertEqual("ёйцукенгшщзхъфыв", "", locator)
            self.app.method.assertEqual("апролджэячсмитьбю", "", locator)
        with allure.step("Проверка ввода Русских букв в верхнем регистре"):
            self.app.method.assertEqual("АПРОЛДЖЭЯЧСМИТЬБЮ", "", locator)
            self.app.method.assertEqual("ЁЙЦУКЕНГШЩЗХЪФЫВ", "", locator)
        with allure.step("Проверка ввода спецсимволов"):
            self.app.method.assertEqual("!#$%&'()*+,/:;<=>?@[]^_`{|}~", "", locator)
        with allure.step("Проверка ввода совместных значений(буквы/цифры/спецсимволы)"):
            self.app.method.assertEqual('123  АБВABC!@#.', '123ABC.', locator)
        with allure.step("Проверка ввода пробелов"):
            self.app.method.assertEqual('   ', '', locator)
            self.app.method.assertEqual('123     ', '123', locator)
            self.app.method.assertEqual('   123', '123', locator)
            self.app.method.assertEqual('1 2 3', '123', locator)
        with allure.step("Проверка ввода очень большого числа"):
            self.app.method.assertEqual(9 * 100000000000000000000000, 90000000000000000000000, locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual('1' * 24, '1' * 23, locator)

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

    # Проверка ввода поле Номер объекта
    def input_object_number(self, locator=object_number):
        self.input_number_9999(locator)

    # Проверка ввода поле Номер объекта
    def input_object_number_negativ(self, locator=object_number):
        self.input_number_9999_negativ(locator)

    # Проверка ввода поле Задержка взятия
    def input_object_delay_take(self, locator=object_delay_take_on):
        self.input_number_65535(locator)

    # Проверка ввода поле Задержка взятия
    def input_object_delay_take_negativ(self, locator=object_delay_take_on):
        self.input_number_65535_negativ(locator)

    # Проверка ввода поле Задержка тревоги входа
    def input_object_delay_alarm_enter(self, locator=object_delay_alarm_enter):
        self.input_number_65535(locator)

    # Проверка ввода поле Задержка тревоги входа
    def input_object_delay_alarm_enter_negativ(self, locator=object_delay_alarm_enter):
        self.input_number_65535_negativ(locator)

    # Проверка ввода поле Время автовзятия
    def input_object_time_auto_take_on(self, locator=object_time_auto_take_on):
        self.input_number_65535(locator)

    # Проверка ввода поле Время автовзятия
    def input_object_time_auto_take_on_negativ(self, locator=object_time_auto_take_on):
        self.input_number_65535_negativ(locator)

    # Включение чекбоксов объекта
    def check_box_object_on(self):
        self.app.method.checkBox("ON", object_sensor_loss_alarm_click, object_sensor_loss_alarm_status)
        self.app.method.assertCheckBox("ON", object_sensor_loss_alarm_status)
        self.app.method.checkBox("ON", object_taking_with_lost_sensors_click,
                                 object_taking_with_lost_sensors_status)
        self.app.method.assertCheckBox("ON", object_taking_with_lost_sensors_status)
        self.app.method.checkBox("ON", object_taking_sensors_in_alarm_click,
                                 object_taking_sensors_in_alarm_status)
        self.app.method.assertCheckBox("ON", object_taking_sensors_in_alarm_status)
        self.app.method.checkBox("ON", object_capturing_with_sensors_in_error_click,
                                 object_capturing_with_sensors_in_error_status)
        self.app.method.assertCheckBox("ON", object_capturing_with_sensors_in_error_status)
        self.app.method.checkBox("ON", object_forced_take_from_alarm_click,
                                 object_forced_take_from_alarm_status)
        self.app.method.assertCheckBox("ON", object_forced_take_from_alarm_status)

    # Выключение чекбоксов объекта
    def check_box_object_off(self):
        self.app.method.checkBox("OFF", object_sensor_loss_alarm_click, object_sensor_loss_alarm_status)
        self.app.method.assertCheckBox("OFF", object_sensor_loss_alarm_status)
        self.app.method.checkBox("OFF", object_taking_with_lost_sensors_click,
                                 object_taking_with_lost_sensors_status)
        self.app.method.assertCheckBox("OFF", object_taking_with_lost_sensors_status)
        self.app.method.checkBox("OFF", object_taking_sensors_in_alarm_click,
                                 object_taking_sensors_in_alarm_status)
        self.app.method.assertCheckBox("OFF", object_taking_sensors_in_alarm_status)
        self.app.method.checkBox("OFF", object_capturing_with_sensors_in_error_click,
                                 object_capturing_with_sensors_in_error_status)
        self.app.method.assertCheckBox("OFF", object_capturing_with_sensors_in_error_status)
        self.app.method.checkBox("OFF", object_forced_take_from_alarm_click,
                                 object_forced_take_from_alarm_status)
        self.app.method.assertCheckBox("OFF", object_forced_take_from_alarm_status)

    # Частичный выбор чекбоксов объекта
    def check_box_object_some(self):
        self.app.method.checkBox("ON", object_sensor_loss_alarm_click, object_sensor_loss_alarm_status)
        self.app.method.assertCheckBox("ON", object_sensor_loss_alarm_status)
        self.app.method.checkBox("OFF", object_taking_with_lost_sensors_click,
                                 object_taking_with_lost_sensors_status)
        self.app.method.assertCheckBox("OFF", object_taking_with_lost_sensors_status)
        self.app.method.checkBox("ON", object_taking_sensors_in_alarm_click,
                                 object_taking_sensors_in_alarm_status)
        self.app.method.assertCheckBox("ON", object_taking_sensors_in_alarm_status)
        self.app.method.checkBox("OFF", object_capturing_with_sensors_in_error_click,
                                 object_capturing_with_sensors_in_error_status)
        self.app.method.assertCheckBox("OFF", object_capturing_with_sensors_in_error_status)
        self.app.method.checkBox("ON", object_forced_take_from_alarm_click,
                                 object_forced_take_from_alarm_status)
        self.app.method.assertCheckBox("ON", object_forced_take_from_alarm_status)
        self.app.method.checkBox("OFF", object_sensor_loss_alarm_click, object_sensor_loss_alarm_status)
        self.app.method.assertCheckBox("OFF", object_sensor_loss_alarm_status)
        self.app.method.checkBox("ON", object_taking_with_lost_sensors_click,
                                 object_taking_with_lost_sensors_status)
        self.app.method.assertCheckBox("ON", object_taking_with_lost_sensors_status)
        self.app.method.checkBox("OFF", object_taking_sensors_in_alarm_click,
                                 object_taking_sensors_in_alarm_status)
        self.app.method.assertCheckBox("OFF", object_taking_sensors_in_alarm_status)
        self.app.method.checkBox("ON", object_capturing_with_sensors_in_error_click,
                                 object_capturing_with_sensors_in_error_status)
        self.app.method.assertCheckBox("ON", object_capturing_with_sensors_in_error_status)

        self.app.method.checkBox("OFF", object_forced_take_from_alarm_click,
                                 object_forced_take_from_alarm_status)
        self.app.method.assertCheckBox("OFF", object_forced_take_from_alarm_status)

    # Включение чекбоксов gsm
    def check_box_gsm_on(self):
        self.app.method.checkBox("ON", gsm_Enable_GSM_module_click, gsm_Enable_GSM_module_status)
        self.app.method.assertCheckBox("ON", gsm_Enable_GSM_module_status)
        self.app.method.checkBox("ON", gsm_Use_GPRS_click, gsm_Use_GPRS_status)
        self.app.method.assertCheckBox("ON", gsm_Use_GPRS_status)
        self.app.method.checkBox("ON", gsm_Use_backup_SIM_click, gsm_Use_backup_SIM_status)
        self.app.method.assertCheckBox("ON", gsm_Use_backup_SIM_status)
        self.app.method.checkBox("ON", gsm_Allow_USSD_click, gsm_Allow_USSD_status)
        self.app.method.assertCheckBox("ON", gsm_Allow_USSD_status)
        self.app.method.checkBox("ON", gsm_Allow_Event_Broadcast_click, gsm_Allow_Event_Broadcast_status)
        self.app.method.assertCheckBox("ON", gsm_Allow_Event_Broadcast_status)

    # Выключение чекбоксов gsm
    def check_box_gsm_off(self):
        self.app.method.checkBox("ON", gsm_Enable_GSM_module_click, gsm_Enable_GSM_module_status)
        self.app.method.assertCheckBox("ON", gsm_Enable_GSM_module_status)
        self.app.method.checkBox("OFF", gsm_Use_GPRS_click, gsm_Use_GPRS_status)
        self.app.method.assertCheckBox("OFF", gsm_Use_GPRS_status)
        self.app.method.checkBox("OFF", gsm_Use_backup_SIM_click, gsm_Use_backup_SIM_status)
        self.app.method.assertCheckBox("OFF", gsm_Use_backup_SIM_status)
        self.app.method.checkBox("OFF", gsm_Allow_USSD_click, gsm_Allow_USSD_status)
        self.app.method.assertCheckBox("OFF", gsm_Allow_USSD_status)
        self.app.method.checkBox("OFF", gsm_Allow_Event_Broadcast_click, gsm_Allow_Event_Broadcast_status)
        self.app.method.assertCheckBox("OFF", gsm_Allow_Event_Broadcast_status)

    # Включение чекбоксов gsm выборочно
    def check_box_gsm_some(self):
        self.app.method.checkBox("ON", gsm_Enable_GSM_module_click, gsm_Enable_GSM_module_status)
        self.app.method.assertCheckBox("ON", gsm_Enable_GSM_module_status)
        self.app.method.checkBox("ON", gsm_Use_GPRS_click, gsm_Use_GPRS_status)
        self.app.method.assertCheckBox("ON", gsm_Use_GPRS_status)
        self.app.method.checkBox("OFF", gsm_Use_backup_SIM_click, gsm_Use_backup_SIM_status)
        self.app.method.assertCheckBox("OFF", gsm_Use_backup_SIM_status)
        self.app.method.checkBox("ON", gsm_Allow_USSD_click, gsm_Allow_USSD_status)
        self.app.method.assertCheckBox("ON", gsm_Allow_USSD_status)
        self.app.method.checkBox("ON", gsm_Allow_Event_Broadcast_click, gsm_Allow_Event_Broadcast_status)
        self.app.method.assertCheckBox("ON", gsm_Allow_Event_Broadcast_status)
        self.app.method.checkBox("ON", gsm_Enable_GSM_module_click, gsm_Enable_GSM_module_status)
        self.app.method.assertCheckBox("ON", gsm_Enable_GSM_module_status)
        self.app.method.checkBox("OFF", gsm_Use_GPRS_click, gsm_Use_GPRS_status)
        self.app.method.assertCheckBox("OFF", gsm_Use_GPRS_status)
        self.app.method.checkBox("ON", gsm_Use_backup_SIM_click, gsm_Use_backup_SIM_status)
        self.app.method.assertCheckBox("ON", gsm_Use_backup_SIM_status)
        self.app.method.checkBox("OFF", gsm_Allow_USSD_click, gsm_Allow_USSD_status)
        self.app.method.assertCheckBox("OFF", gsm_Allow_USSD_status)
        self.app.method.checkBox("OFF", gsm_Allow_Event_Broadcast_click, gsm_Allow_Event_Broadcast_status)
        self.app.method.assertCheckBox("OFF", gsm_Allow_Event_Broadcast_status)

    # Проверка полей на странице ОБЪЕКТ
    def text_object_page(self):
        self.app.method.assertTextOnPage(object_text, data_object)

    # Проверка полей на странице GSM
    def text_gsm_page(self):
        self.app.method.assertTextOnPage(GSM_text, data_gsm)

    # Проверка полей на странице GSM - SMS
    def text_gsm_page_SMS(self):
        self.SIM_1_goToSendSMS()
        self.app.method.assertTextOnPage(GSM_SMS_modal_text, data_gsm_sms)
        self.app.method.click((By.XPATH, button_cancel))
        self.SIM_2_goToSendSMS()
        self.app.method.assertTextOnPage(GSM_SMS_modal_text, data_gsm_sms)

    # Выбор позиции: Использовать время GSM сети ДАТА И ВРЕМЯ
    def Use_GSM_network_time_click(self):
        self.app.method.selectDropdownList(date_time_dropdown_1, Use_GSM_network_time)
        self.app.method.assertSelectionDropdownList('Использовать время GSM сети', date_time_dropdown_1)

    # Выбор позиции: Синхронизация по NTP/HTP ДАТА И ВРЕМЯ
    def Synchronization_via_NTP_HTP_click(self):
        self.app.method.selectDropdownList(date_time_dropdown_1, Synchronization_via_NTP_HTP)
        self.app.method.assertSelectionDropdownList('Синхронизация по NTP/HTP', date_time_dropdown_1)

    # Выбор позиции: Вручную ДАТА И ВРЕМЯ
    def Manually_click(self):
        self.app.method.selectDropdownList(date_time_dropdown_1, Manually)
        self.app.method.assertSelectionDropdownList('Вручную', date_time_dropdown_1)

    # Проверка полей на странице ДАТА и ВРЕМЯ - Использовать время GSM сети
    def text_date_time_page_gsm(self):
        self.Use_GSM_network_time_click()
        self.app.method.assertTextOnPage(data_time_text, data_date_time_gsm)

    # Проверка полей на странице ДАТА и ВРЕМЯ - Синхронизация по NTP/HTP
    def text_date_time_page_ntp(self):
        self.Synchronization_via_NTP_HTP_click()
        self.app.method.assertTextOnPage(data_time_text, data_date_time_ntp)

    # Проверка полей на странице ДАТА и ВРЕМЯ - Вручную
    def text_date_time_page_hand(self):
        self.Manually_click()
        self.app.method.assertTextOnPage(data_time_text, data_date_time_hand)

    # Проверка полей на странице ПРИБОР
    def text_device_page(self):
        self.app.method.assertTextOnPage(device_text, data_device)

    # Проверка полей на странице Световая индикация
    def text_light_indication_page(self):
        self.app.method.assertTextOnPage(light_indication_text, data_light_indication)

    # Проверка полей на странице РАДИО
    def text_radio_page(self):
        self.app.method.assertTextOnPage(radio_text, data_radio)

    # Проверка полей на странице ETHERNET
    def text_ethernet_page(self):
        self.app.method.assertTextOnPage(ethernet_text, data_ethernet)

    # Проверка полей на странице Звуковая индикация
    def text_volum_indication_page(self):
        self.app.method.click((By.XPATH, button_related_events))
        time.sleep(1)
        self.app.method.assertTextOnPage(volum_indication_text, data_volum_indication)

    # Переход на модальное окно - Отправка тестового SMS SIM_1
    def SIM_1_goToSendSMS(self):
        self.app.method.click((By.XPATH, button_verify_1))

    # Переход на модальное окно - Отправка тестового SMS SIM_2
    def SIM_2_goToSendSMS(self):
        self.app.method.click((By.XPATH, button_verify_2))

    # Проверка кнопки сохранить при вводе данных в обязательные поля
    def data_in_all_entry_field_object(self):
        self.app.method.inputValues('111', object_number)
        self.app.method.inputValues('111', object_delay_take_on)
        self.app.method.inputValues('111', object_delay_alarm_enter)
        self.app.method.inputValues('111', object_time_auto_take_on)
        status = self.app.method.attributeStatusButton(save_button)
        assert status is None, f"\nОшибка Кнопка 'Сохранить' должна быть кликабельной!\nФактический статус кнопки:{status}"

    # Проверка кнопки сохранить при вводе данных в обязательные поля
    def no_data_in_number_object(self):
        self.app.method.inputValues('1' + Keys.BACKSPACE, object_number)
        self.app.method.inputValues('111', object_delay_take_on)
        self.app.method.inputValues('111', object_delay_alarm_enter)
        self.app.method.inputValues('111', object_time_auto_take_on)
        status = self.app.method.attributeStatusButton(save_button)
        assert status == 'true', f"\nОшибка Кнопка 'Сохранить' должна быть кликабельной!\nФактический статус кнопки:{status}"

    # Проверка кнопки сохранить при вводе данных в обязательные поля
    def no_data_delay_take_on_object(self):
        self.app.method.inputValues('111', object_number)
        self.app.method.inputValues('1' + Keys.BACKSPACE, object_delay_take_on)
        self.app.method.inputValues('111', object_delay_alarm_enter)
        self.app.method.inputValues('111', object_time_auto_take_on)
        status = self.app.method.attributeStatusButton(save_button)
        assert status == 'true', f"\nОшибка Кнопка 'Сохранить' должна быть не кликабельной!" \
                                 f"\nФактический статус кнопки:{status}"

    # Проверка кнопки сохранить при вводе данных в обязательные поля
    def no_data_delay_alarm_enter_object(self):
        self.app.method.inputValues('111', object_number)
        self.app.method.inputValues('111', object_delay_take_on)
        self.app.method.inputValues('1' + Keys.BACKSPACE, object_delay_alarm_enter)
        self.app.method.inputValues('111', object_time_auto_take_on)
        status = self.app.method.attributeStatusButton(save_button)
        assert status == 'true', f"\nОшибка Кнопка 'Сохранить' должна быть не кликабельной!" \
                                 f"\nФактический статус кнопки:{status}"

        # Проверка кнопки сохранить при вводе данных в обязательные поля

    def no_data_time_auto_take_on_object(self):
        self.app.method.inputValues('111', object_number)
        self.app.method.inputValues('111', object_delay_take_on)
        self.app.method.inputValues('111', object_delay_alarm_enter)
        self.app.method.inputValues('1' + Keys.BACKSPACE, object_time_auto_take_on)
        status = self.app.method.attributeStatusButton(save_button)
        assert status == 'true', f"\nОшибка Кнопка 'Сохранить' должна быть не кликабельной!" \
                                 f"\nФактический статус кнопки:{status}"

    # Включение чекбоксов радио - РАДИО
    def check_box_radio_on(self):
        self.app.method.checkBox("ON", radio_modul_on_click, radio_modul_on_status)
        self.app.method.assertCheckBox("ON", radio_modul_on_status)

    # Включение чекбоксов радио - РАДИО
    def check_box_radio_off(self):
        self.app.method.checkBox("OFF", radio_modul_on_click, radio_modul_on_status)
        self.app.method.assertCheckBox("OFF", radio_modul_on_status)

    # Проверка ввода поле Время разрешения добавления новых датчиков - РАДИО
    def input_data_resolution_time_for_adding_new_sensors(self, locator=resolution_time_for_adding_new_sensors):
        self.check_box_radio_on()
        self.input_number(locator)

    # Проверка ввода поле Время разрешения добавления новых датчиков - РАДИО
    def input_data_resolution_time_for_adding_new_sensors_negativ(self, locator=resolution_time_for_adding_new_sensors):
        self.check_box_radio_on()
        self.input_number_negativ(locator)

    # Период опроса датчиков - РАДИО
    def input_data_sensor_polling_period(self, locator=sensor_polling_period):
        self.check_box_radio_on()
        self.input_number(locator)

    # Период опроса датчиков - РАДИО
    def input_data_sensor_polling_period_negativ(self, locator=sensor_polling_period):
        self.check_box_radio_on()
        self.input_number_negativ(locator)

    # Выпадающий список Канал - РАДИО
    def drop_list_radio(self, button=radio_chanel_button, possition=radio_chanel):
        for i in range(1, 11):
            self.app.method.selectDropdownList(button, possition + f'[{i}]')
            self.app.method.assertSelectionDropdownList(i, button)

    # MAC адрес - Ethernet
    def input_data_ethernet_mac(self, locator=ethernet_mac_address):
        self.input_mac_address(locator)

    # MAC адрес - Ethernet
    def input_data_ethernet_mac_negativ(self, locator=ethernet_mac_address):
        self.input_mac_address_negativ(locator)

    # Название сервера - Ethernet
    def input_data_ethernet_name_server(self, locator=ethernet_name_server):
        self.input_server_name(locator)

    # Название сервера - Ethernet
    def input_data_ethernet_name_server_negativ(self, locator=ethernet_name_server):
        self.input_server_name_negativ(locator)

    # Адрес IPv4 - Ethernet
    def input_data_ethernet_ipv4_address(self, locator=ethernet_address_IPv4):
        with allure.step("Проверка ввода цифр"):
            for i in range(10):
                self.app.method.assertEqual(i, i, locator)
        with allure.step("Проверка ввода спецсимволов"):
            self.app.method.assertEqual(".", ".", locator)
        with allure.step("Проверка ввода дробного числа "):
            self.app.method.assertEqual('11.11', '11.11', locator)
        with allure.step("Ограничения по вводу IP по маске"):
            for i in range(7, 10):
                self.app.method.assertEqual(('25' + str(i)), (f'25.{i}'), locator)
            for i in range(7, 10):
                self.app.method.assertEqual(('255.25' + str(i)), (f'255.25.{i}'), locator)
            for i in range(7, 10):
                self.app.method.assertEqual(('255.255.25' + str(i)), (f'255.255.25.{i}'), locator)
            for i in range(7, 10):
                self.app.method.assertEqual(('255.255.255.25' + str(i)), (f'255.255.255.25'), locator)
        with allure.step("Проверка валидных значений"):
            for x in ip_list:
                self.app.method.assertEqual(x, x, locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual(0, '0', locator)
            self.app.method.assertEqual(1, '1', locator)
            self.app.method.assertEqual(11111111111, '111.111.111.11', locator)

    # Адрес IPv4 - Ethernet
    def input_data_ethernet_ipv4_address_negativ(self, locator=ethernet_address_IPv4):
        with allure.step("Проверка ввода латинских букв в нижнем регистре"):
            self.app.method.assertEqual('abcdefghijklmnopqrstuvwxyz', '', locator)
        with allure.step("Проверка ввода латинских букв в верхнем регистре"):
            self.app.method.assertEqual('ABCDEFGHIJKLMNOPQRSTUVWXYZ', '', locator)
        with allure.step("Проверка ввода Русских букв в нижнем регистре"):
            self.app.method.assertEqual("ёйцукенгшщзхъфывапролджэячсмитьбю", "", locator)
        with allure.step("Проверка ввода Русских букв в верхнем регистре"):
            self.app.method.assertEqual("АПРОЛДЖЭЯЧСМИТЬБЮЁЙЦУКЕНГШЩЗХЪФЫВ", "", locator)
        with allure.step("Проверка ввода спецсимволов"):
            self.app.method.assertEqual("!#$%&'()*+,-./:;<=>?@[]^_`{|}~", ".", locator)
        with allure.step("Проверка ввода совместных значений(буквы/цифры/спецсимволы)"):
            self.app.method.assertEqual('123  АБВABC.!@#1', '123.1', locator)
        with allure.step("Проверка ввода пробелов"):
            self.app.method.assertEqual('   ', '', locator)
            self.app.method.assertEqual('123     ', '123', locator)
            self.app.method.assertEqual('   123', '123', locator)
            self.app.method.assertEqual('1 2 3', '123', locator)
        with allure.step("Проверка ввода дробного числа "):
            self.app.method.assertEqual('000.1', '0.0.0.1', locator)
            self.app.method.assertEqual('11,11', '111.1', locator)
            self.app.method.assertEqual('000,1', '0.0.0.1', locator)
        with allure.step("Проверка ввода пустого значения"):
            self.app.method.assertEqual('', '', locator)
        with allure.step("Проверка ввода очень большого числа"):
            self.app.method.assertEqual('1' * 100, '111.111.111.111', locator)
        with allure.step("Проверка ввода отрицательного числа"):
            self.app.method.assertEqual('-1', '1', locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual(111111111111, '111.111.111.111', locator)

    # IP позитив
    def input_ip_data_mask_positiv(self, locator):
        with allure.step("Проверка ввода цифр"):
            for i in range(10):
                self.app.method.assertEqual(i, i, locator)
        with allure.step("Проверка ввода спецсимволов"):
            self.app.method.assertEqual(".", ".", locator)
        with allure.step("Проверка ввода дробного числа "):
            self.app.method.assertEqual('11.11', '11.11', locator)
        with allure.step("Ограничения по вводу IP по маске"):
            for i in range(7, 10):
                self.app.method.assertEqual(('25' + str(i)), (f'25.{i}'), locator)
            for i in range(7, 10):
                self.app.method.assertEqual(('255.25' + str(i)), (f'255.25.{i}'), locator)
            for i in range(7, 10):
                self.app.method.assertEqual(('255.255.25' + str(i)), (f'255.255.25.{i}'), locator)
            for i in range(7, 10):
                self.app.method.assertEqual(('255.255.255.25' + str(i)), (f'255.255.255.25'), locator)
        with allure.step("Проверка валидных значений"):
            for x in list_mask:
                self.app.method.assertEqual(x, x, locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual(0, '0', locator)
            self.app.method.assertEqual(1, '1', locator)
            self.app.method.assertEqual(11111111111, '111.111.111.11', locator)

    # IP негатив
    def input_ip_data_mask_negativ(self, locator):
        with allure.step("Проверка ввода латинских букв в нижнем регистре"):
            self.app.method.assertEqual('abcdefghijklmnopqrstuvwxyz', '', locator)
        with allure.step("Проверка ввода латинских букв в верхнем регистре"):
            self.app.method.assertEqual('ABCDEFGHIJKLMNOPQRSTUVWXYZ', '', locator)
        with allure.step("Проверка ввода Русских букв в нижнем регистре"):
            self.app.method.assertEqual("ёйцукенгшщзхъфывапролджэячсмитьбю", "", locator)
        with allure.step("Проверка ввода Русских букв в верхнем регистре"):
            self.app.method.assertEqual("АПРОЛДЖЭЯЧСМИТЬБЮЁЙЦУКЕНГШЩЗХЪФЫВ", "", locator)
        with allure.step("Проверка ввода спецсимволов"):
            self.app.method.assertEqual("!#$%&'()*+,-./:;<=>?@[]^_`{|}~", ".", locator)
        with allure.step("Проверка ввода совместных значений(буквы/цифры/спецсимволы)"):
            self.app.method.assertEqual('123  АБВABC.!@#1', '123.1', locator)
        with allure.step("Проверка ввода пробелов"):
            self.app.method.assertEqual('   ', '', locator)
            self.app.method.assertEqual('123     ', '123', locator)
            self.app.method.assertEqual('   123', '123', locator)
            self.app.method.assertEqual('1 2 3', '123', locator)
        with allure.step("Проверка ввода дробного числа "):
            self.app.method.assertEqual('000.1', '0.0.0.1', locator)
            self.app.method.assertEqual('11,11', '111.1', locator)
            self.app.method.assertEqual('000,1', '0.0.0.1', locator)
        with allure.step("Проверка ввода пустого значения"):
            self.app.method.assertEqual('', '', locator)
        with allure.step("Проверка ввода очень большого числа"):
            self.app.method.assertEqual('1' * 100, '111.111.111.111', locator)
        with allure.step("Проверка ввода отрицательного числа"):
            self.app.method.assertEqual('-1', '1', locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual(111111111111, '111.111.111.111', locator)

    # IPv6
    def input_data_ipv6_positiv(self, locator):
        with allure.step("Проверка ввода цифр"):
            for i in range(10):
                self.app.method.assertEqual(i, i, locator)
        with allure.step("Проверка ввода латинских букв в нижнем регистре"):
            self.app.method.assertEqual('abcd:ef', 'abcd:ef', locator)
        with allure.step("Проверка ввода латинских букв в верхнем регистре"):
            self.app.method.assertEqual('ABCD:EF', 'ABCD:EF', locator)
        with allure.step("Проверка ввода спецсимволов"):
            self.app.method.assertEqual(":", ":", locator)
        with allure.step("Проверка валидных значений"):
            for x in ip_v6_list:
                self.app.method.assertEqual(x, x, locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual('f', 'f', locator)
            self.app.method.assertEqual('fffffffffffffffffffffffffffffff',
                                        'ffff:ffff:ffff:ffff:ffff:ffff:ffff:fff', locator)

    # IPv6
    def input_data_ipv6_negativ(self, locator):
        with allure.step("Проверка ввода латинских букв в нижнем регистре"):
            self.app.method.assertEqual('abcdefghijklmnopqrstuvwxyz', 'abcd:ef', locator)
        with allure.step("Проверка ввода латинских букв в верхнем регистре"):
            self.app.method.assertEqual('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ABCD:EF', locator)
        with allure.step("Проверка ввода Русских букв в нижнем регистре"):
            self.app.method.assertEqual("ёйцукенгшщзхъфывапролджэячсмитьбю", "", locator)
        with allure.step("Проверка ввода Русских букв в верхнем регистре"):
            self.app.method.assertEqual("АПРОЛДЖЭЯЧСМИТЬБЮЁЙЦУКЕНГШЩЗХЪФЫВ", "", locator)
        with allure.step("Проверка ввода спецсимволов"):
            self.app.method.assertEqual("!#$%&'()*+,-./:;<=>?@[]^_`{|}~", ":", locator)
        with allure.step("Проверка ввода совместных значений(буквы/цифры/спецсимволы)"):
            self.app.method.assertEqual('123  АБВABC:.!@#1', '123A:BC:1', locator)
        with allure.step("Проверка ввода пробелов"):
            self.app.method.assertEqual('   ', '', locator)
            self.app.method.assertEqual('123     ', '123', locator)
            self.app.method.assertEqual('   123', '123', locator)
            self.app.method.assertEqual('1 2 3', '123', locator)
        with allure.step("Проверка ввода дробного числа "):
            self.app.method.assertEqual('000.1', '0001', locator)
            self.app.method.assertEqual('11,11', '1111', locator)
            self.app.method.assertEqual('000,1', '0001', locator)
        with allure.step("Проверка ввода пустого значения"):
            self.app.method.assertEqual('', '', locator)
        with allure.step("Проверка ввода очень большого числа"):
            self.app.method.assertEqual('1' * 100, '1111:1111:1111:1111:1111:1111:1111:1111', locator)
        with allure.step("Проверка ввода отрицательного числа"):
            self.app.method.assertEqual('-1', '1', locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual('ffffffffffffffffffffffffffffffff',
                                        'ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff', locator)

    # Проверка ввода поле
    def input_number_32768(self, locator):
        with allure.step("Проверка ввода цифр"):
            for i in range(10):
                self.app.method.assertEqual(i, i, locator)
        with allure.step("Проверка ввода спецсимволов"):
            self.app.method.assertEqual("-", "-", locator)
        with allure.step("Проверка ввода отрицательного числа"):
            self.app.method.assertEqual('-1', '-1', locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual('-32768', '-32768', locator)
            self.app.method.assertEqual('-32767', '-32767', locator)
            self.app.method.assertEqual(32767, 32767, locator)
            self.app.method.assertEqual(32768, 32768, locator)

        # Проверка ввода поле

    def input_number_32768_negativ(self, locator):
        with allure.step("Проверка ввода латинских букв в нижнем регистре"):
            self.app.method.assertEqual('abcdefghijklmnopqrstuvwxyz', '', locator)
        with allure.step("Проверка ввода латинских букв в верхнем регистре"):
            self.app.method.assertEqual('ABCDEFGHIJKLMNOPQRSTUVWXYZ', '', locator)
        with allure.step("Проверка ввода Русских букв в нижнем регистре"):
            self.app.method.assertEqual("ёйцукенгшщзхъфывапролджэячсмитьбю", "", locator)
        with allure.step("Проверка ввода Русских букв в верхнем регистре"):
            self.app.method.assertEqual("АПРОЛДЖЭЯЧСМИТЬБЮЁЙЦУКЕНГШЩЗХЪФЫВ", "", locator)
        with allure.step("Проверка ввода спецсимволов"):
            self.app.method.assertEqual("!#$%&'()*+,-./:;<=>?@[]^_`{|}~", "-", locator)
        with allure.step("Проверка ввода совместных значений(буквы/цифры/спецсимволы)"):
            self.app.method.assertEqual('123  АБВABC!@#', '123', locator)
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
        with allure.step("Проверка ввода очень большого числа"):
            self.app.method.assertEqual(9 * 10000000000000, 900000, locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual(1111111, 111111, locator)

    # Маска подсети - Ethernet
    def input_data_ethernet_subnet_mask(self, locator=ethernet_subnet_mask):
        self.input_ip_data_mask_positiv(locator)

    # Маска подсети - Ethernet
    def input_data_ethernet_subnet_mask_negativ(self, locator=ethernet_subnet_mask):
        self.input_ip_data_mask_negativ(locator)

    # Основной шлюз - Ethernet
    def input_data_ethernet_main_gate(self, locator=ethernet_main_gate):
        self.input_ip_data_mask_positiv(locator)

    # Основной шлюз - Ethernet
    def input_data_ethernet_main_gate_negativ(self, locator=ethernet_main_gate):
        self.input_ip_data_mask_negativ(locator)

    # Предпочтительный DNS сервер - Ethernet
    def input_data_ethernet_preferred_DNS_servere(self, locator=ethernet_preferred_DNS_server):
        self.input_ip_data_mask_positiv(locator)

    # Предпочтительный DNS сервер - Ethernet
    def input_data_ethernet_preferred_DNS_servere_negativ(self, locator=ethernet_preferred_DNS_server):
        self.input_ip_data_mask_negativ(locator)

    # Альтернативный DNS сервер - Ethernet
    def input_data_ethernet_alternative_DNS_server(self, locator=ethernet_alternative_DNS_server):
        self.input_ip_data_mask_positiv(locator)

    # Альтернативный DNS сервер - Ethernet
    def input_data_ethernet_alternative_DNS_server_negativ(self, locator=ethernet_alternative_DNS_server):
        self.input_ip_data_mask_negativ(locator)

    # Локальный IPv6 адрес - Ethernet
    def input_data_ethernet_local_ipv6(self, locator=ethernet_local_ipv6):
        self.input_data_ipv6_positiv(locator)

    # Локальный IPv6 адрес - Ethernet
    def input_data_ethernet_local_ipv6_negativ(self, locator=ethernet_local_ipv6):
        self.input_data_ipv6_negativ(locator)

    # Глобальный IPv6 адрес - Ethernet
    def input_data_ethernet_global_ipv6(self, locator=ethernet_global_ipv6):
        self.input_data_ipv6_positiv(locator)

    # Глобальный IPv6 адрес - Ethernet
    def input_data_ethernet_global_ipv6_negativ(self, locator=ethernet_global_ipv6):
        self.input_data_ipv6_negativ(locator)

    # Предпочтительный IPv6 DNS сервер - Ethernet
    def input_data_ethernet_preferred_ipv6(self, locator=ethernet_preferred_IPv6_DNS_server):
        self.input_data_ipv6_positiv(locator)

    # Предпочтительный IPv6 DNS сервер - Ethernet
    def input_data_ethernet_preferred_ipv6_negativ(self, locator=ethernet_preferred_IPv6_DNS_server):
        self.input_data_ipv6_negativ(locator)

    # Альтернативный IPv6 DNS сервер - Ethernet
    def input_data_ethernet_alternative_ipv6(self, locator=ethernet_alternative_IPv6_DNS_server):
        self.input_data_ipv6_positiv(locator)

    # Альтернативный IPv6 DNS сервер - Ethernet
    def input_data_ethernet_alternative_ipv6_negativ(self, locator=ethernet_alternative_IPv6_DNS_server):
        self.input_data_ipv6_negativ(locator)

    # Число знаков номера для проверки - GSM
    def input_data_gsm_number_of_digits_of_the_number_to_check(self, locator=number_of_digits_of_the_number_to_check):
        with allure.step("Проверка ввода цифр"):
            for i in range(10):
                self.app.method.assertEqual(i, i, locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual(0, 0, locator)
            self.app.method.assertEqual(1, 1, locator)
            self.app.method.assertEqual(98, 98, locator)
            self.app.method.assertEqual(99, 99, locator)

    # Число знаков номера для проверки - GSM
    def input_data_gsm_number_of_digits_of_the_number_to_check_negativ(self,
                                                                       locator=number_of_digits_of_the_number_to_check):
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
            self.app.method.assertEqual('123  АБВABC!@#', '12', locator)
        with allure.step("Проверка ввода пробелов"):
            self.app.method.assertEqual('   ', '', locator)
            self.app.method.assertEqual('12     ', '12', locator)
            self.app.method.assertEqual('   12', '12', locator)
            self.app.method.assertEqual('1 2 ', '12', locator)
        with allure.step("Проверка ввода дробного числа "):
            self.app.method.assertEqual('1.1', '11', locator)
            self.app.method.assertEqual('0.1', '1', locator)
            self.app.method.assertEqual('1,1', '11', locator)
            self.app.method.assertEqual('0,1', '1', locator)
        with allure.step("Проверка ввода пустого значения"):
            self.app.method.assertEqual('', '', locator)
        with allure.step("Проверка ввода очень большого числа"):
            self.app.method.assertEqual(9 * 10000000000000, 90, locator)
        with allure.step("Проверка ввода отрицательного числа"):
            self.app.method.assertEqual('-1', '1', locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual(999, 99, locator)

    # Порог уведомления о балансе - GSM
    def input_data_gsm_balance_notification_threshold(self, locator=balance_notification_threshold):
        self.input_number_32768(locator)

    # Порог уведомления о балансе - GSM
    def input_data_gsm_balance_notification_threshold_negativ(self, locator=balance_notification_threshold):
        self.input_number_32768_negativ(locator)

    # PIN positiv
    def input_pin_positiv(self, locator):
        with allure.step("Проверка ввода цифр"):
            for i in range(10):
                self.app.method.assertEqual(i, i, locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual(1111, 1111, locator)
            self.app.method.assertEqual(11111, 11111, locator)
            self.app.method.assertEqual('1' * 8, '1' * 8, locator)
            self.app.method.assertEqual('1' * 9, '1' * 9, locator)

    # PIN negativ
    def input_pin_negativ(self, locator):
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
            self.app.method.assertEqual('1234  АБВABC!@#', '1234', locator)
        with allure.step("Проверка ввода пробелов"):
            self.app.method.assertEqual('   ', '', locator)
            self.app.method.assertEqual('1234     ', '1234', locator)
            self.app.method.assertEqual('   1234', '1234', locator)
            self.app.method.assertEqual('1 2 3 4', '1234', locator)
        with allure.step("Проверка ввода дробного числа "):
            self.app.method.assertEqual('11.11', '1111', locator)
            self.app.method.assertEqual('00.11', '0011', locator)
            self.app.method.assertEqual('11,11', '1111', locator)
            self.app.method.assertEqual('00,11', '0011', locator)
        with allure.step("Проверка ввода пустого значения"):
            self.app.method.assertEqual('', '', locator)
        with allure.step("Проверка ввода очень большого числа"):
            self.app.method.assertEqual(9 * 10000000000000, 900000000, locator)
        with allure.step("Проверка ввода отрицательного числа"):
            self.app.method.assertEqual('-1', '1', locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual('1' * 10, '1' * 9, locator)

    # PIN - SIM_1 - GSM
    def input_data_sim_1_pin(self, locator=PIN_SIM_1):
        self.input_pin_positiv(locator)

    # PIN - SIM_1 - GSM
    def input_data_sim_1_pin_negativ(self, locator=PIN_SIM_1):
        self.input_pin_negativ(locator)

    # PIN - SIM_2 - GSM
    def input_data_sim_2_pin(self, locator=PIN_SIM_2):
        self.input_pin_positiv(locator)

    # PIN - SIM_2 - GSM
    def input_data_sim_2_pin_negativ(self, locator=PIN_SIM_2):
        self.input_pin_negativ(locator)

    # USSD - positiv
    def input_USSD_positiv(self, locator):
        with allure.step("Проверка ввода цифр"):
            for i in range(10):
                self.app.method.assertEqual(i, i, locator)
        with allure.step("Проверка ввода спецсимволов"):
            self.app.method.assertEqual("#*", "#*", locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual('1' * 31, '1' * 31, locator)
            self.app.method.assertEqual('1' * 30, '1' * 30, locator)

    # USSD - SIM_1 - GSM
    def input_USSD_negativ(self, locator):
        with allure.step("Проверка ввода латинских букв в нижнем регистре"):
            self.app.method.assertEqual('abcdefghijklmnopqrstuvwxyz', '', locator)
        with allure.step("Проверка ввода латинских букв в верхнем регистре"):
            self.app.method.assertEqual('ABCDEFGHIJKLMNOPQRSTUVWXYZ', '', locator)
        with allure.step("Проверка ввода Русских букв в нижнем регистре"):
            self.app.method.assertEqual("ёйцукенгшщзхъфывапролджэячсмитьбю", "", locator)
        with allure.step("Проверка ввода Русских букв в верхнем регистре"):
            self.app.method.assertEqual("АПРОЛДЖЭЯЧСМИТЬБЮЁЙЦУКЕНГШЩЗХЪФЫВ", "", locator)
        with allure.step("Проверка ввода спецсимволов"):
            self.app.method.assertEqual("!#$%&'()*+,-./:;<=>?@[]^_`{|}~", "#*", locator)
        with allure.step("Проверка ввода совместных значений(буквы/цифры/спецсимволы)"):
            self.app.method.assertEqual('123  АБВABC!@#', '123#', locator)
        with allure.step("Проверка ввода пробелов"):
            self.app.method.assertEqual('   ', '', locator)
            self.app.method.assertEqual('123     ', '123', locator)
            self.app.method.assertEqual('   123', '123', locator)
            self.app.method.assertEqual('1 2 3', '123', locator)
        with allure.step("Проверка ввода дробного числа "):
            self.app.method.assertEqual('11.1', '111', locator)
            self.app.method.assertEqual('00.1', '001', locator)
            self.app.method.assertEqual('11,1', '111', locator)
            self.app.method.assertEqual('00,1', '001', locator)
        with allure.step("Проверка ввода пустого значения"):
            self.app.method.assertEqual('', '', locator)
        with allure.step("Проверка ввода очень большого числа"):
            self.app.method.assertEqual('1' * 1000, '1' * 31, locator)
        with allure.step("Проверка ввода отрицательного числа"):
            self.app.method.assertEqual('-1', '1', locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual('1' * 32, '1' * 31, locator)

    # Ограничение в 63 символа
    def input_all_63_positiv(self, locator):
        with allure.step("Проверка ввода цифр"):
            for i in range(10):
                self.app.method.assertEqual(i, i, locator)
        with allure.step("Проверка ввода латинских букв в нижнем регистре"):
            self.app.method.assertEqual('abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz', locator)
        with allure.step("Проверка ввода латинских букв в верхнем регистре"):
            self.app.method.assertEqual('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual(1, 1, locator)
            self.app.method.assertEqual('1' * 62, '1' * 62, locator)
            self.app.method.assertEqual('1' * 63, '1' * 63, locator)

    # Ограничение в 63 символа
    def input_all_63_negativ(self, locator):
        with allure.step("Проверка ввода Русских букв в нижнем регистре"):
            self.app.method.assertEqual("ёйцукенгшщзхъфывапролджэячсмитьбю", "", locator)
        with allure.step("Проверка ввода Русских букв в верхнем регистре"):
            self.app.method.assertEqual("АПРОЛДЖЭЯЧСМИТЬБЮЁЙЦУКЕНГШЩЗХЪФЫВ", "", locator)
        with allure.step("Проверка ввода спецсимволов"):
            self.app.method.assertEqual("!#$%&'()*+,-./:;<=>?@[]^_`{|}~", "", locator)
        with allure.step("Проверка ввода совместных значений(буквы/цифры/спецсимволы)"):
            self.app.method.assertEqual('123  АБВABC!@#', '123ABC', locator)
        with allure.step("Проверка ввода пробелов"):
            self.app.method.assertEqual('   ', '', locator)
            self.app.method.assertEqual('123     ', '123', locator)
            self.app.method.assertEqual('   123', '123', locator)
            self.app.method.assertEqual('1 2 3', '123', locator)
        with allure.step("Проверка ввода дробного числа "):
            self.app.method.assertEqual('11.1', '111', locator)
            self.app.method.assertEqual('00.1', '001', locator)
            self.app.method.assertEqual('11,1', '111', locator)
            self.app.method.assertEqual('00,1', '001', locator)
        with allure.step("Проверка ввода пустого значения"):
            self.app.method.assertEqual('', '', locator)
        with allure.step("Проверка ввода очень большого числа"):
            self.app.method.assertEqual('1' * 1000, '1' * 63, locator)
        with allure.step("Проверка ввода отрицательного числа"):
            self.app.method.assertEqual('-1', '1', locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual('1' * 64, '1' * 63, locator)

    # Ограничение в 63 символа + специальные символы
    def input_63_positiv_spec_chars(self, locator):
        with allure.step("Проверка ввода цифр"):
            for i in range(10):
                self.app.method.assertEqual(i, i, locator)
        with allure.step("Проверка ввода латинских букв в нижнем регистре"):
            self.app.method.assertEqual('abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz', locator)
        with allure.step("Проверка ввода латинских букв в верхнем регистре"):
            self.app.method.assertEqual('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', locator)
        with allure.step("Проверка ввода спецсимволов"):
            self.app.method.assertEqual("№_~!@#$%^&*-+=|(){}[]:;<>,.?", "№_~!@#$%^&*-+=|(){}[]:;<>,.?", locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual(1, 1, locator)
            self.app.method.assertEqual('1' * 62, '1' * 62, locator)
            self.app.method.assertEqual('1' * 63, '1' * 63, locator)

    # Ограничение в 63 символа + специальные символы
    def input_all_63_negativ_spec_chars(self, locator):
        with allure.step("Проверка ввода Русских букв в нижнем регистре"):
            self.app.method.assertEqual("ёйцукенгшщзхъфывапролджэячсмитьбю", "", locator)
        with allure.step("Проверка ввода Русских букв в верхнем регистре"):
            self.app.method.assertEqual("АПРОЛДЖЭЯЧСМИТЬБЮЁЙЦУКЕНГШЩЗХЪФЫВ", "", locator)
        with allure.step("Проверка ввода совместных значений(буквы/цифры/спецсимволы)"):
            self.app.method.assertEqual('123  АБВABC!@#', '123ABC!@#', locator)
        with allure.step("Проверка ввода пробелов"):
            self.app.method.assertEqual('   ', '', locator)
            self.app.method.assertEqual('123     ', '123', locator)
            self.app.method.assertEqual('   123', '123', locator)
            self.app.method.assertEqual('1 2 3', '123', locator)
        with allure.step("Проверка ввода дробного числа "):
            self.app.method.assertEqual('11.1', '11.1', locator)
            self.app.method.assertEqual('00.1', '00.1', locator)
            self.app.method.assertEqual('11,1', '11,1', locator)
            self.app.method.assertEqual('00,1', '00,1', locator)
        with allure.step("Проверка ввода пустого значения"):
            self.app.method.assertEqual('', '', locator)
        with allure.step("Проверка ввода очень большого числа"):
            self.app.method.assertEqual('1' * 1000, '1' * 63, locator)
        with allure.step("Проверка ввода отрицательного числа"):
            self.app.method.assertEqual('-1', '-1', locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual('1' * 64, '1' * 63, locator)

    # Проверка поля Телефон КОД
    def input_phone_cod_positiv(self, locator):
        with allure.step("Проверка ввода цифр"):
            for i in range(10):
                self.app.method.assertEqual(i, i, locator)
        with allure.step("Проверка ввода спецсимполов"):
            self.app.method.assertEqual("+", "+", locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual('0', '0', locator)
            self.app.method.assertEqual('1', '1', locator)
            self.app.method.assertEqual('1' * 4, '1' * 4, locator)
            self.app.method.assertEqual('1' * 5, '1' * 5, locator)

    # Проверка поля Телефон КОД
    def input_phone_cod_negativ(self, locator):
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
            self.app.method.assertEqual("!#$%&'()*+,-./:;<=>?@[]^_`{|}~", "+", locator)
        with allure.step("Проверка ввода совместных значений"):
            self.app.method.assertEqual('+123  АБВABC!@#', '+123', locator)
        with allure.step("Проверка ввода пробелов"):
            self.app.method.assertEqual('   ', '', locator)
            self.app.method.assertEqual('123     ', '123', locator)
            self.app.method.assertEqual('   123', '123', locator)
            self.app.method.assertEqual('1 2 3', '123', locator)
        with allure.step("Проверка ввода дробного числа "):
            self.app.method.assertEqual('11.11', '1111', locator)
            self.app.method.assertEqual('000.1', '0001', locator)
            self.app.method.assertEqual('11,11', '1111', locator)
            self.app.method.assertEqual('000,1', '0001', locator)
        with allure.step("Проверка ввода пустого значения"):
            self.app.method.assertEqual('', '', locator)
        with allure.step("Проверка ввода отрицательного числа"):
            self.app.method.assertEqual('-1', '1', locator)
        with allure.step("Проверка ввода очень большого числа"):
            self.app.method.assertEqual('1' * 1000, '11111', locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual('1' * 6, '1' * 5, locator)

    # Проверка поля Телефон НОМЕР
    def input_phone_number(self, locator):
        with allure.step("Проверка ввода цифр"):
            for i in range(10):
                self.app.method.assertEqual(i, '(' + str(i), locator)
        with allure.step("Проверка ввода спецсимполов"):
            self.app.method.assertEqual("()- ", "()- ", locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual('0', '(0', locator)
            self.app.method.assertEqual('1', '(1', locator)
            self.app.method.assertEqual('1' * 9, '(111) 111-11-1', locator)
            self.app.method.assertEqual('1' * 10, '(111) 111-11-11', locator)

    # Проверка поля Телефон НОМЕР
    def input_phone_number_negativ(self, locator):
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
            self.app.method.assertEqual("!#$%&'()*+,-./:;<=>?@[]^_`{|}~", "()-", locator)
        with allure.step("Проверка ввода совместных значений"):
            self.app.method.assertEqual('(123  АБВABC!@#', '(123  ', locator)
        with allure.step("Проверка ввода пробелов"):
            self.app.method.assertEqual('   ', '   ', locator)
            self.app.method.assertEqual('123   ', '(123   ', locator)
            self.app.method.assertEqual('   123', '   123', locator)
            self.app.method.assertEqual('1 2 3', '(1 2 3', locator)
        with allure.step("Проверка ввода дробного числа "):
            self.app.method.assertEqual('11.1', '(111', locator)
            self.app.method.assertEqual('00.1', '(001', locator)
            self.app.method.assertEqual('11,1', '(111', locator)
            self.app.method.assertEqual('00,1', '(001', locator)
        with allure.step("Проверка ввода пустого значения"):
            self.app.method.assertEqual('', '', locator)
        with allure.step("Проверка ввода отрицательного числа"):
            self.app.method.assertEqual('-1', '-1', locator)
        with allure.step("Проверка ввода очень большого числа"):
            self.app.method.assertEqual('1' * 1000, '(111) 111-11-11', locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual('1' * 11, '(111) 111-11-11', locator)

    # USSD - SIM_1 - GSM
    def input_data_sim_1_USSD(self, locator=USSD_SIM_1):
        self.input_USSD_positiv(locator)

    # USSD - SIM_1 - GSM
    def input_data_sim_1_USSD_negativ(self, locator=USSD_SIM_1):
        self.input_USSD_negativ(locator)

    # USSD - SIM_2 - GSM
    def input_data_sim_2_USSD(self, locator=USSD_SIM_2):
        self.input_USSD_positiv(locator)

    # USSD - SIM_2 - GSM
    def input_data_sim_2_USSD_negativ(self, locator=USSD_SIM_2):
        self.input_USSD_negativ(locator)

    # APN - SIM_1 - GSM
    def input_data_sim_1_APN(self, locator=APN_SIM_1):
        self.input_all_63_positiv(locator)

    # APN - SIM_1 - GSM
    def input_data_sim_1_APN_negativ(self, locator=APN_SIM_1):
        self.input_all_63_negativ(locator)

    # APN - SIM_2 - GSM
    def input_data_sim_2_APN(self, locator=APN_SIM_2):
        self.input_all_63_positiv(locator)

    # APN - SIM_2 - GSM
    def input_data_sim_2_APN_negativ(self, locator=APN_SIM_2):
        self.input_all_63_negativ(locator)

    # USER - SIM_1 - GSM
    def input_data_sim_1_user(self, locator=USER_SIM_1):
        self.input_all_63_positiv(locator)

    # USER - SIM_1 - GSM
    def input_data_sim_1_user_negativ(self, locator=USER_SIM_1):
        self.input_all_63_negativ(locator)

    # USER - SIM_2 - GSM
    def input_data_sim_2_user(self, locator=USER_SIM_2):
        self.input_all_63_positiv(locator)

    # USER - SIM_2 - GSM
    def input_data_sim_2_user_negativ(self, locator=USER_SIM_2):
        self.input_all_63_negativ(locator)

    # PASSWORD - SIM_1 - GSM
    def input_data_sim_1_password(self, locator=PASSWORD_SIM_1):
        self.input_63_positiv_spec_chars(locator)

    # PASSWORD - SIM_1 - GSM
    def input_data_sim_1_password_negativ(self, locator=PASSWORD_SIM_1):
        self.input_all_63_negativ_spec_chars(locator)

    # PASSWORD - SIM_2 - GSM
    def input_data_sim_2_password(self, locator=PASSWORD_SIM_2):
        self.input_63_positiv_spec_chars(locator)

    # PASSWORD - SIM_2 - GSM
    def input_data_sim_2_password_negativ(self, locator=PASSWORD_SIM_2):
        self.input_all_63_negativ_spec_chars(locator)

    # Номер телефона КОД - GSM
    def input_data_tel_cod(self, locator=TEL_COD):
        self.input_phone_cod_positiv(locator)

    # Номер телефона КОД - GSM
    def input_data_tel_cod_negativ(self, locator=TEL_COD):
        self.input_phone_cod_negativ(locator)

    # Номер телефона - GSM
    def input_data_tel(self, locator=TEL_NUM):
        self.input_phone_number(locator)

    # Номер телефона - GSM
    def input_data_tel_negativ(self, locator=TEL_NUM):
        self.input_phone_number_negativ(locator)

    # Сообщение - GSM
    def input_data_massege(self, locator=MESSEGE):
        self.input_all(locator)

    # Длительность сигнала - Звуковая индикация
    def input_data_volum_indication_signal_duration(self, locator=volum_indication_signal_duration):
        self.input_number_65535(locator)

    # Длительность сигнала - Звуковая индикация
    def input_data_volum_indication_signal_duration_negativ(self, locator=volum_indication_signal_duration):
        self.input_number_65535_negativ(locator)

    # Громкость событий - Звуковая индикация (Виджет ползунок)
    def input_event_volume_slider_widget(self, locator=event_volume_slider_widget):
        position = random.randint(1, 100)
        self.app.method.sliderWidget(position, locator)
        self.app.method.assertSliderWidget(position, locator)

    # Громкость тревог - Звуковая индикация (Виджет ползунок)
    def input_alarm_volume_slider_widget(self, locator=alarm_volume_slider_widget):
        position = random.randint(1, 100)
        self.app.method.sliderWidget(position, locator)
        self.app.method.assertSliderWidget(position, locator)

    # Включение чекбоксов ethernet
    def check_box_ethernet_on(self):
        self.app.method.checkBox("ON", ethernet_obtain_IPv4_address_and_settings_automatically_click,
                                 ethernet_obtain_IPv4_address_and_settings_automatically_status)
        self.app.method.assertCheckBox("ON", ethernet_obtain_IPv4_address_and_settings_automatically_status)

        self.app.method.checkBox("ON", ethernet_use_as_server_click, ethernet_use_as_server_status)
        self.app.method.assertCheckBox("ON", ethernet_use_as_server_status)

        self.app.method.checkBox("ON", ethernet_obtain_an_IPv6_address_from_DHCP_automatically_click,
                                 ethernet_obtain_an_IPv6_address_from_DHCP_automatically_status)
        self.app.method.assertCheckBox("ON", ethernet_obtain_an_IPv6_address_from_DHCP_automatically_status)

        self.app.method.checkBox("ON", ethernet_allow_remote_control_click,
                                 ethernet_allow_remote_control_status)
        self.app.method.assertCheckBox("ON", ethernet_allow_remote_control_status)

        self.app.method.checkBox("ON", ethernet_obtain_an_IPv6_address_from_SLAAC_automatically_click,
                                 ethernet_obtain_an_IPv6_address_from_SLAAC_automatically_status)
        self.app.method.assertCheckBox("ON", ethernet_obtain_an_IPv6_address_from_SLAAC_automatically_status)

        self.app.method.checkBox("ON", ethernet_allow_insecure_HTTP_connection_click,
                                 ethernet_allow_insecure_HTTP_connection_status)
        self.app.method.assertCheckBox("ON", ethernet_allow_insecure_HTTP_connection_status)

    # Выключение чекбоксов ethernet
    def check_box_ethernet_off(self):
        self.app.method.checkBox("OFF", ethernet_obtain_IPv4_address_and_settings_automatically_click,
                                 ethernet_obtain_IPv4_address_and_settings_automatically_status)
        self.app.method.assertCheckBox("OFF", ethernet_obtain_IPv4_address_and_settings_automatically_status)

        self.app.method.checkBox("OFF", ethernet_use_as_server_click, ethernet_use_as_server_status)
        self.app.method.assertCheckBox("OFF", ethernet_use_as_server_status)

        self.app.method.checkBox("OFF", ethernet_obtain_an_IPv6_address_from_DHCP_automatically_click,
                                 ethernet_obtain_an_IPv6_address_from_DHCP_automatically_status)
        self.app.method.assertCheckBox("OFF", ethernet_obtain_an_IPv6_address_from_DHCP_automatically_status)

        self.app.method.checkBox("OFF", ethernet_allow_remote_control_click,
                                 ethernet_allow_remote_control_status)
        self.app.method.assertCheckBox("OFF", ethernet_allow_remote_control_status)

        self.app.method.checkBox("OFF", ethernet_obtain_an_IPv6_address_from_SLAAC_automatically_click,
                                 ethernet_obtain_an_IPv6_address_from_SLAAC_automatically_status)
        self.app.method.assertCheckBox("OFF", ethernet_obtain_an_IPv6_address_from_SLAAC_automatically_status)

        self.app.method.checkBox("OFF", ethernet_allow_insecure_HTTP_connection_click,
                                 ethernet_allow_insecure_HTTP_connection_status)
        self.app.method.assertCheckBox("OFF", ethernet_allow_insecure_HTTP_connection_status)

    # Включение частичное чекбоксов ethernet
    def check_box_ethernet_some(self):
        self.app.method.checkBox("ON", ethernet_obtain_IPv4_address_and_settings_automatically_click,
                                 ethernet_obtain_IPv4_address_and_settings_automatically_status)
        self.app.method.assertCheckBox("ON", ethernet_obtain_IPv4_address_and_settings_automatically_status)

        self.app.method.checkBox("OFF", ethernet_use_as_server_click, ethernet_use_as_server_status)
        self.app.method.assertCheckBox("OFF", ethernet_use_as_server_status)

        self.app.method.checkBox("ON", ethernet_obtain_an_IPv6_address_from_DHCP_automatically_click,
                                 ethernet_obtain_an_IPv6_address_from_DHCP_automatically_status)
        self.app.method.assertCheckBox("ON", ethernet_obtain_an_IPv6_address_from_DHCP_automatically_status)

        self.app.method.checkBox("OFF", ethernet_allow_remote_control_click,
                                 ethernet_allow_remote_control_status)
        self.app.method.assertCheckBox("OFF", ethernet_allow_remote_control_status)

        self.app.method.checkBox("ON", ethernet_obtain_an_IPv6_address_from_SLAAC_automatically_click,
                                 ethernet_obtain_an_IPv6_address_from_SLAAC_automatically_status)
        self.app.method.assertCheckBox("ON", ethernet_obtain_an_IPv6_address_from_SLAAC_automatically_status)

        self.app.method.checkBox("OFF", ethernet_allow_insecure_HTTP_connection_click,
                                 ethernet_allow_insecure_HTTP_connection_status)
        self.app.method.assertCheckBox("OFF", ethernet_allow_insecure_HTTP_connection_status)

        self.app.method.checkBox("OFF", ethernet_obtain_IPv4_address_and_settings_automatically_click,
                                 ethernet_obtain_IPv4_address_and_settings_automatically_status)
        self.app.method.assertCheckBox("OFF", ethernet_obtain_IPv4_address_and_settings_automatically_status)

        self.app.method.checkBox("ON", ethernet_use_as_server_click, ethernet_use_as_server_status)
        self.app.method.assertCheckBox("ON", ethernet_use_as_server_status)

        self.app.method.checkBox("OFF", ethernet_obtain_an_IPv6_address_from_DHCP_automatically_click,
                                 ethernet_obtain_an_IPv6_address_from_DHCP_automatically_status)
        self.app.method.assertCheckBox("OFF", ethernet_obtain_an_IPv6_address_from_DHCP_automatically_status)

        self.app.method.checkBox("ON", ethernet_allow_remote_control_click,
                                 ethernet_allow_remote_control_status)
        self.app.method.assertCheckBox("ON", ethernet_allow_remote_control_status)

        self.app.method.checkBox("OFF", ethernet_obtain_an_IPv6_address_from_SLAAC_automatically_click,
                                 ethernet_obtain_an_IPv6_address_from_SLAAC_automatically_status)
        self.app.method.assertCheckBox("OFF", ethernet_obtain_an_IPv6_address_from_SLAAC_automatically_status)

        self.app.method.checkBox("ON", ethernet_allow_insecure_HTTP_connection_click,
                                 ethernet_allow_insecure_HTTP_connection_status)
        self.app.method.assertCheckBox("ON", ethernet_allow_insecure_HTTP_connection_status)

    # Выпадающий список: Устанавливать сетевые подключения через - ETHERNET
    def drop_list_ethernet(self, button=ethernet_network_connections_button,
                           possition=ethernet_network_connection_positions):
        self.app.method.selectDropdownList(button, possition + '[1]')
        self.app.method.assertSelectionDropdownList("Отсутствует", button)
        self.app.method.selectDropdownList(button, possition + '[2]')
        self.app.method.assertSelectionDropdownList("Авто", button)
        self.app.method.selectDropdownList(button, possition + '[3]')
        self.app.method.assertSelectionDropdownList("Ethernet", button)
        self.app.method.selectDropdownList(button, possition + '[4]')
        self.app.method.assertSelectionDropdownList("GPRS", button)

    # Включение чекбоксов прибора
    def check_box_device_on(self):
        # Выпилено с устройства
        # self.app.method.checkBox("ON", enable_power_saving_mode_click, enable_power_saving_mode_status)
        # self.app.method.assertCheckBox("ON", enable_power_saving_mode_status)
        self.app.method.checkBox("ON", allow_configuration_when_the_case_is_closed_click,
                                 allow_configuration_when_the_case_is_closed_status)
        self.app.method.assertCheckBox("ON", allow_configuration_when_the_case_is_closed_status)
        self.app.method.checkBox("ON", fix_partition_repeated_alarms_click, fix_partition_repeated_alarms_status)
        self.app.method.assertCheckBox("ON", fix_partition_repeated_alarms_status)
        self.app.method.checkBox("ON", fix_repeated_sensor_alarms_click, fix_repeated_sensor_alarms_status)
        self.app.method.assertCheckBox("ON", fix_repeated_sensor_alarms_status)
        self.app.method.checkBox("ON", fix_repeated_fire_alarms_in_a_section_click,
                                 fix_repeated_fire_alarms_in_a_section_status)
        self.app.method.assertCheckBox("ON", fix_repeated_fire_alarms_in_a_section_status)
        self.app.method.checkBox("ON", fix_repeated_fire_alarms_of_the_sensor_click,
                                 fix_repeated_fire_alarms_of_the_sensor_status)
        self.app.method.assertCheckBox("ON", fix_repeated_fire_alarms_of_the_sensor_status)
        self.app.method.checkBox("ON", fix_repeated_arming_disarming_events_click,
                                 fix_repeated_arming_disarming_events_status)
        self.app.method.assertCheckBox("ON", fix_repeated_arming_disarming_events_status)
        self.app.method.checkBox("ON", control_exits_when_re_arming_disarming_click,
                                 control_exits_when_re_arming_disarming_status)
        self.app.method.assertCheckBox("ON", control_exits_when_re_arming_disarming_status)

    # Выключение чекбоксов прибора
    def check_box_device_off(self):
        # Выпилено с устройства
        # self.app.method.checkBox("OFF", enable_power_saving_mode_click, enable_power_saving_mode_status)
        # self.app.method.assertCheckBox("OFF", enable_power_saving_mode_status)
        self.app.method.checkBox("OFF", allow_configuration_when_the_case_is_closed_click,
                                 allow_configuration_when_the_case_is_closed_status)
        self.app.method.assertCheckBox("OFF", allow_configuration_when_the_case_is_closed_status)
        self.app.method.checkBox("OFF", fix_partition_repeated_alarms_click, fix_partition_repeated_alarms_status)
        self.app.method.assertCheckBox("OFF", fix_partition_repeated_alarms_status)
        self.app.method.checkBox("OFF", fix_repeated_sensor_alarms_click, fix_repeated_sensor_alarms_status)
        self.app.method.assertCheckBox("OFF", fix_repeated_sensor_alarms_status)
        self.app.method.checkBox("OFF", fix_repeated_fire_alarms_in_a_section_click,
                                 fix_repeated_fire_alarms_in_a_section_status)
        self.app.method.assertCheckBox("OFF", fix_repeated_fire_alarms_in_a_section_status)
        self.app.method.checkBox("OFF", fix_repeated_fire_alarms_of_the_sensor_click,
                                 fix_repeated_fire_alarms_of_the_sensor_status)
        self.app.method.assertCheckBox("OFF", fix_repeated_fire_alarms_of_the_sensor_status)
        self.app.method.checkBox("OFF", fix_repeated_arming_disarming_events_click,
                                 fix_repeated_arming_disarming_events_status)
        self.app.method.assertCheckBox("OFF", fix_repeated_arming_disarming_events_status)
        self.app.method.checkBox("OFF", control_exits_when_re_arming_disarming_click,
                                 control_exits_when_re_arming_disarming_status)
        self.app.method.assertCheckBox("OFF", control_exits_when_re_arming_disarming_status)

    # Некликабельные чекбоксы
    def check_box_device_some(self):
        # выпилено с устройства
        # self.app.method.checkBox("ON", enable_power_saving_mode_click, enable_power_saving_mode_status)
        # self.app.method.assertCheckBox("ON", enable_power_saving_mode_status)
        self.app.method.checkBox("ON", allow_configuration_when_the_case_is_closed_click,
                                 allow_configuration_when_the_case_is_closed_status)
        self.app.method.assertCheckBox("ON", allow_configuration_when_the_case_is_closed_status)
        self.app.method.checkBox("OFF", fix_partition_repeated_alarms_click, fix_partition_repeated_alarms_status)
        self.app.method.assertCheckBox("OFF", fix_partition_repeated_alarms_status)
        self.app.method.checkBox("ON", fix_repeated_sensor_alarms_click, fix_repeated_sensor_alarms_status)
        self.app.method.assertCheckBox("OFF", fix_repeated_sensor_alarms_status)
        self.app.method.checkBox("OFF", fix_repeated_fire_alarms_in_a_section_click,
                                 fix_repeated_fire_alarms_in_a_section_status)
        self.app.method.assertCheckBox("OFF", fix_repeated_fire_alarms_in_a_section_status)
        self.app.method.checkBox("ON", fix_repeated_fire_alarms_of_the_sensor_click,
                                 fix_repeated_fire_alarms_of_the_sensor_status)
        self.app.method.assertCheckBox("OFF", fix_repeated_fire_alarms_of_the_sensor_status)
        self.app.method.checkBox("OFF", fix_repeated_arming_disarming_events_click,
                                 fix_repeated_arming_disarming_events_status)
        self.app.method.assertCheckBox("OFF", fix_repeated_arming_disarming_events_status)
        self.app.method.checkBox("ON", control_exits_when_re_arming_disarming_click,
                                 control_exits_when_re_arming_disarming_status)
        self.app.method.assertCheckBox("OFF", control_exits_when_re_arming_disarming_status)

    # Частичное включение чекбоксов прибора
    def check_box_device_some_2(self):
        # выпилено с устройства
        # self.app.method.checkBox("ON", enable_power_saving_mode_click, enable_power_saving_mode_status)
        # self.app.method.assertCheckBox("ON", enable_power_saving_mode_status)
        self.app.method.checkBox("OFF", allow_configuration_when_the_case_is_closed_click,
                                 allow_configuration_when_the_case_is_closed_status)
        self.app.method.assertCheckBox("OFF", allow_configuration_when_the_case_is_closed_status)
        self.app.method.checkBox("ON", fix_partition_repeated_alarms_click, fix_partition_repeated_alarms_status)
        self.app.method.assertCheckBox("ON", fix_partition_repeated_alarms_status)
        self.app.method.checkBox("OFF", fix_repeated_sensor_alarms_click, fix_repeated_sensor_alarms_status)
        self.app.method.assertCheckBox("OFF", fix_repeated_sensor_alarms_status)
        self.app.method.checkBox("ON", fix_repeated_fire_alarms_in_a_section_click,
                                 fix_repeated_fire_alarms_in_a_section_status)
        self.app.method.assertCheckBox("ON", fix_repeated_fire_alarms_in_a_section_status)
        self.app.method.checkBox("OFF", fix_repeated_fire_alarms_of_the_sensor_click,
                                 fix_repeated_fire_alarms_of_the_sensor_status)
        self.app.method.assertCheckBox("OFF", fix_repeated_fire_alarms_of_the_sensor_status)
        self.app.method.checkBox("ON", fix_repeated_arming_disarming_events_click,
                                 fix_repeated_arming_disarming_events_status)
        self.app.method.assertCheckBox("ON", fix_repeated_arming_disarming_events_status)
        self.app.method.checkBox("OFF", control_exits_when_re_arming_disarming_click,
                                 control_exits_when_re_arming_disarming_status)
        self.app.method.assertCheckBox("OFF", control_exits_when_re_arming_disarming_status)

    # Включение чекбокса световой индикации
    def check_box_light_indication_on(self):
        self.app.method.checkBox("ON", reader_indication_inversion_click, reader_indication_inversion_status)
        self.app.method.assertCheckBox("ON", reader_indication_inversion_status)

    # Выключение чекбокса световой индикации
    def check_box_light_indication_off(self):
        self.app.method.checkBox("ON", reader_indication_inversion_click, reader_indication_inversion_status)
        self.app.method.assertCheckBox("ON", reader_indication_inversion_status)

    # Выпадающий список: Режим светодиодов для охранных датчиков - Световая индикация
    def drop_list_light_indication_LED_mode_for_security_sensors(self, button=LED_mode_for_security_sensors,
                                                                 possition=options):
        self.app.method.selectDropdownList(button, possition + '[1]')
        self.app.method.assertSelectionDropdownList('Согласно настройкам прибора', button)
        self.app.method.selectDropdownList(button, possition + '[2]')
        self.app.method.assertSelectionDropdownList('Включено для всех', button)
        self.app.method.selectDropdownList(button, possition + '[3]')
        self.app.method.assertSelectionDropdownList('Выключено для всех', button)

    # Выпадающий список: Режим светодиодов для пожарных датчиков - Световая индикация
    def drop_list_light_indication_LED_mode_for_fire_detectors(self, button=LED_mode_for_fire_detectors,
                                                               possition=options):
        self.app.method.selectDropdownList(button, possition + '[1]')
        self.app.method.assertSelectionDropdownList('Согласно настройкам прибора', button)
        self.app.method.selectDropdownList(button, possition + '[2]')
        self.app.method.assertSelectionDropdownList('Включено для всех', button)
        self.app.method.selectDropdownList(button, possition + '[3]')
        self.app.method.assertSelectionDropdownList('Выключено для всех', button)

    # Выпадающий список: Режим светодиодов для технологических датчиков - Световая индикация
    def drop_list_light_indication_LED_mode_for_process_sensors(self, button=LED_mode_for_process_sensors,
                                                                possition=options):
        self.app.method.selectDropdownList(button, possition + '[1]')
        self.app.method.assertSelectionDropdownList('Согласно настройкам прибора', button)
        self.app.method.selectDropdownList(button, possition + '[2]')
        self.app.method.assertSelectionDropdownList('Включено для всех', button)
        self.app.method.selectDropdownList(button, possition + '[3]')
        self.app.method.assertSelectionDropdownList('Выключено для всех', button)

    # Выпадающий список: Режим работы считывателя - Световая индикация
    def drop_list_light_indication_reader_operation_mode(self, button=Reader_operation_mode, possition=options):
        self.app.method.selectDropdownList(button, possition + '[1]')
        self.app.method.assertSelectionDropdownList(
            '1 светодиод, 1-ое касание - статус, последующие управляющие', button)
        self.app.method.selectDropdownList(button, possition + '[2]')
        self.app.method.assertSelectionDropdownList(
            '1 светодиод, 1-ое касание - статус, 2-ое - управляющее', button)
        self.app.method.selectDropdownList(button, possition + '[3]')
        self.app.method.assertSelectionDropdownList(
            '2 светодиода, 1-ое касание - статус, последующие управляющие', button)
        self.app.method.selectDropdownList(button, possition + '[4]')
        self.app.method.assertSelectionDropdownList(
            '2 светодиода, 1-ое касание - статус, второе - управляющее', button)
        self.app.method.selectDropdownList(button, possition + '[5]')
        self.app.method.assertSelectionDropdownList('2 светодиода, любое касание - управляющее', button)

    def open_volum_indication_events(self):
        self.app.method.click((By.XPATH, button_related_events))
        time.sleep(1)

    # Включение чекбоксов звуковой индикации
    def check_box_volum_indication_on(self):
        self.app.method.checkBox("ON", volum_on_click, volum_on_status)
        self.app.method.assertCheckBox("ON", volum_on_status)
        self.app.method.checkBox("ON", volum_alarm_click, volum_alarm_status)
        self.app.method.assertCheckBox("ON", volum_alarm_status)
        self.app.method.checkBox("ON", volum_fire_click, volum_fire_status)
        self.app.method.assertCheckBox("ON", volum_fire_status)
        self.app.method.checkBox("ON", volum_take_path_click, volum_take_path_status)
        self.app.method.assertCheckBox("ON", volum_take_path_status)
        self.app.method.checkBox("ON", volum_take_off_path_click, volum_take_off_path_status)
        self.app.method.assertCheckBox("ON", volum_take_off_path_status)
        self.app.method.checkBox("ON", volum_delay_take_click, volum_delay_take_status)
        self.app.method.assertCheckBox("ON", volum_delay_take_status)
        self.app.method.checkBox("ON", volum_no_take_click, volum_no_take_status)
        self.app.method.assertCheckBox("ON", volum_no_take_status)
        self.app.method.checkBox("ON", volum_some_take_on_click, volum_some_take_on_status)
        self.app.method.assertCheckBox("ON", volum_some_take_on_status)
        self.app.method.checkBox("ON", volum_add_sensor_click, volum_add_sensor_status)
        self.app.method.assertCheckBox("ON", volum_add_sensor_status)
        self.app.method.checkBox("ON", volum_bang_click, volum_bang_status)
        self.app.method.assertCheckBox("ON", volum_bang_status)

    # Выключение чекбоксов звуковой индикации
    def check_box_volum_indication_off(self):
        self.app.method.checkBox("ON", volum_on_click, volum_on_status)
        self.app.method.assertCheckBox("ON", volum_on_status)
        self.app.method.checkBox("OFF", volum_alarm_click, volum_alarm_status)
        self.app.method.assertCheckBox("OFF", volum_alarm_status)
        self.app.method.checkBox("OFF", volum_fire_click, volum_fire_status)
        self.app.method.assertCheckBox("OFF", volum_fire_status)
        self.app.method.checkBox("OFF", volum_take_path_click, volum_take_path_status)
        self.app.method.assertCheckBox("OFF", volum_take_path_status)
        self.app.method.checkBox("OFF", volum_take_off_path_click, volum_take_off_path_status)
        self.app.method.assertCheckBox("OFF", volum_take_off_path_status)
        self.app.method.checkBox("OFF", volum_delay_take_click, volum_delay_take_status)
        self.app.method.assertCheckBox("OFF", volum_delay_take_status)
        self.app.method.checkBox("OFF", volum_no_take_click, volum_no_take_status)
        self.app.method.assertCheckBox("OFF", volum_no_take_status)
        self.app.method.checkBox("OFF", volum_some_take_on_click, volum_some_take_on_status)
        self.app.method.assertCheckBox("OFF", volum_some_take_on_status)
        self.app.method.checkBox("OFF", volum_add_sensor_click, volum_add_sensor_status)
        self.app.method.assertCheckBox("OFF", volum_add_sensor_status)
        self.app.method.checkBox("OFF", volum_bang_click, volum_bang_status)
        self.app.method.assertCheckBox("OFF", volum_bang_status)

    # Частичное включение чекбоксов звуковой индикации
    def check_box_volum_indication_some(self):
        self.app.method.checkBox("ON", volum_on_click, volum_on_status)
        self.app.method.assertCheckBox("ON", volum_on_status)
        self.app.method.checkBox("OFF", volum_alarm_click, volum_alarm_status)
        self.app.method.assertCheckBox("OFF", volum_alarm_status)
        self.app.method.checkBox("ON", volum_fire_click, volum_fire_status)
        self.app.method.assertCheckBox("ON", volum_fire_status)
        self.app.method.checkBox("OFF", volum_take_path_click, volum_take_path_status)
        self.app.method.assertCheckBox("OFF", volum_take_path_status)
        self.app.method.checkBox("ON", volum_take_off_path_click, volum_take_off_path_status)
        self.app.method.assertCheckBox("ON", volum_take_off_path_status)
        self.app.method.checkBox("OFF", volum_delay_take_click, volum_delay_take_status)
        self.app.method.assertCheckBox("OFF", volum_delay_take_status)
        self.app.method.checkBox("ON", volum_no_take_click, volum_no_take_status)
        self.app.method.assertCheckBox("ON", volum_no_take_status)
        self.app.method.checkBox("OFF", volum_some_take_on_click, volum_some_take_on_status)
        self.app.method.assertCheckBox("OFF", volum_some_take_on_status)
        self.app.method.checkBox("ON", volum_add_sensor_click, volum_add_sensor_status)
        self.app.method.assertCheckBox("ON", volum_add_sensor_status)
        self.app.method.checkBox("OFF", volum_bang_click, volum_bang_status)
        self.app.method.assertCheckBox("OFF", volum_bang_status)
        self.app.method.checkBox("ON", volum_on_click, volum_on_status)
        self.app.method.assertCheckBox("ON", volum_on_status)
        self.app.method.checkBox("ON", volum_alarm_click, volum_alarm_status)
        self.app.method.assertCheckBox("ON", volum_alarm_status)
        self.app.method.checkBox("OFF", volum_fire_click, volum_fire_status)
        self.app.method.assertCheckBox("OFF", volum_fire_status)
        self.app.method.checkBox("ON", volum_take_path_click, volum_take_path_status)
        self.app.method.assertCheckBox("ON", volum_take_path_status)
        self.app.method.checkBox("OFF", volum_take_off_path_click, volum_take_off_path_status)
        self.app.method.assertCheckBox("OFF", volum_take_off_path_status)
        self.app.method.checkBox("ON", volum_delay_take_click, volum_delay_take_status)
        self.app.method.assertCheckBox("ON", volum_delay_take_status)
        self.app.method.checkBox("OFF", volum_no_take_click, volum_no_take_status)
        self.app.method.assertCheckBox("OFF", volum_no_take_status)
        self.app.method.checkBox("ON", volum_some_take_on_click, volum_some_take_on_status)
        self.app.method.assertCheckBox("ON", volum_some_take_on_status)
        self.app.method.checkBox("OFF", volum_add_sensor_click, volum_add_sensor_status)
        self.app.method.assertCheckBox("OFF", volum_add_sensor_status)
        self.app.method.checkBox("ON", volum_bang_click, volum_bang_status)
        self.app.method.assertCheckBox("ON", volum_bang_status)

    # Выпадающий список: Дата и время на устройстве - ДАТА и ВРЕМЯ
    def drop_list_date_time_on_device(self, button=date_time_dropdown_1):
        self.app.method.selectDropdownList(button, Use_GSM_network_time)
        self.app.method.assertSelectionDropdownList('Использовать время GSM сети', button)
        self.app.method.selectDropdownList(button, Synchronization_via_NTP_HTP)
        self.app.method.assertSelectionDropdownList('Синхронизация по NTP/HTP', button)
        self.app.method.selectDropdownList(button, Manually)
        self.app.method.assertSelectionDropdownList('Вручную', button)
        self.app.method.assertTextOnPage(data_time_text, data_date_time_hand)

    # Выпадающий список: Часовой пояс- ДАТА и ВРЕМЯ
    def drop_list_date_time_timezone(self, button=date_time_dropdown_2, position=utc):
        self.app.method.selectDropdownList(button, position + '[1]')
        self.app.method.assertSelectionDropdownList('UTC (GMT)', button)
        self.app.method.selectDropdownList(button, position + '[2]')
        self.app.method.assertSelectionDropdownList('UTC +01:00 (СЕТ)', button)
        self.app.method.selectDropdownList(button, position + '[3]')
        self.app.method.assertSelectionDropdownList('UTC +02:00 (Калининградское время)', button)
        self.app.method.selectDropdownList(button, position + '[4]')
        self.app.method.assertSelectionDropdownList('UTC +03:00 (Московское время)', button)
        self.app.method.selectDropdownList(button, position + '[5]')
        self.app.method.assertSelectionDropdownList('UTC +04:00 (Самарское время)', button)
        self.app.method.selectDropdownList(button, position + '[6]')
        self.app.method.assertSelectionDropdownList('UTC +05:00 (Екатеринбурское время)', button)
        self.app.method.selectDropdownList(button, position + '[7]')
        self.app.method.assertSelectionDropdownList('UTC +06:00 (Омское время)', button)
        self.app.method.selectDropdownList(button, position + '[8]')
        self.app.method.assertSelectionDropdownList('UTC +07:00 (Красноярское время)', button)
        self.app.method.selectDropdownList(button, position + '[9]')
        self.app.method.assertSelectionDropdownList('UTC +08:00 (Иркутское время)', button)
        self.app.method.selectDropdownList(button, position + '[10]')
        self.app.method.assertSelectionDropdownList('UTC +09:00 (Якутское время)', button)
        self.app.method.selectDropdownList(button, position + '[11]')
        self.app.method.assertSelectionDropdownList('UTC +10:00 (Владивостокское время)', button)
        self.app.method.selectDropdownList(button, position + '[12]')
        self.app.method.assertSelectionDropdownList('UTC +11:00 (Среднеколымское время)', button)
        self.app.method.selectDropdownList(button, position + '[13]')
        self.app.method.assertSelectionDropdownList('UTC +12:00 (Камчатское время)', button)
        self.app.method.selectDropdownList(button, position + '[14]')
        self.app.method.assertSelectionDropdownList('UTC -01:00', button)
        self.app.method.selectDropdownList(button, position + '[15]')
        self.app.method.assertSelectionDropdownList('UTC -02:00', button)
        self.app.method.selectDropdownList(button, position + '[16]')
        self.app.method.assertSelectionDropdownList('UTC -03:00', button)
        self.app.method.selectDropdownList(button, position + '[17]')
        self.app.method.assertSelectionDropdownList('UTC -04:00', button)
        self.app.method.selectDropdownList(button, position + '[18]')
        self.app.method.assertSelectionDropdownList('UTC -05:00', button)
        self.app.method.selectDropdownList(button, position + '[19]')
        self.app.method.assertSelectionDropdownList('UTC -06:00', button)
        self.app.method.selectDropdownList(button, position + '[20]')
        self.app.method.assertSelectionDropdownList('UTC -07:00', button)
        self.app.method.selectDropdownList(button, position + '[21]')
        self.app.method.assertSelectionDropdownList('UTC -08:00', button)
        self.app.method.selectDropdownList(button, position + '[22]')
        self.app.method.assertSelectionDropdownList('UTC -09:00', button)
        self.app.method.selectDropdownList(button, position + '[23]')
        self.app.method.assertSelectionDropdownList('UTC -10:00', button)
        self.app.method.selectDropdownList(button, position + '[24]')
        self.app.method.assertSelectionDropdownList('UTC -11:00', button)
        self.app.method.selectDropdownList(button, position + '[25]')
        self.app.method.assertSelectionDropdownList('UTC -12:00', button)

    # Включение чекбоксов ДАТА И ВРЕМЯ
    def check_box_data_time_on(self):
        self.app.method.checkBox("ON", Use_time_zone_of_GSM_network_click, Use_time_zone_of_GSM_network_status)
        self.app.method.assertCheckBox("ON", Use_time_zone_of_GSM_network_status)
        self.app.method.checkBox("ON", Daylight_Saving_Time_click, Daylight_Saving_Time_status)
        self.app.method.assertCheckBox("ON", Daylight_Saving_Time_status)

    # Выключение чекбоксов ДАТА И ВРЕМЯ
    def check_box_data_time_off(self):
        self.app.method.checkBox("OFF", Use_time_zone_of_GSM_network_click, Use_time_zone_of_GSM_network_status)
        self.app.method.assertCheckBox("OFF", Use_time_zone_of_GSM_network_status)
        self.app.method.checkBox("OFF", Daylight_Saving_Time_click, Daylight_Saving_Time_status)
        self.app.method.assertCheckBox("OFF", Daylight_Saving_Time_status)

    # Частичное включение чекбоксов ДАТА И ВРЕМЯ
    def check_box_data_time_some(self):
        self.app.method.checkBox("ON", Use_time_zone_of_GSM_network_click, Use_time_zone_of_GSM_network_status)
        self.app.method.assertCheckBox("ON", Use_time_zone_of_GSM_network_status)
        self.app.method.checkBox("OFF", Daylight_Saving_Time_click, Daylight_Saving_Time_status)
        self.app.method.assertCheckBox("OFF", Daylight_Saving_Time_status)
        self.app.method.checkBox("OFF", Use_time_zone_of_GSM_network_click, Use_time_zone_of_GSM_network_status)
        self.app.method.assertCheckBox("OFF", Use_time_zone_of_GSM_network_status)
        self.app.method.checkBox("ON", Daylight_Saving_Time_click, Daylight_Saving_Time_status)
        self.app.method.assertCheckBox("ON", Daylight_Saving_Time_status)

    # Проверка появления выпадающего списка 'Часовой пояс' при выборе чекбокса: Использовать время GSM сети ДАТА И ВРЕМЯ
    def check_box_data_time_Use_time_zone_of_GSM_network_status_on(self):
        self.app.method.checkBox("ON", Use_time_zone_of_GSM_network_click, Use_time_zone_of_GSM_network_status)
        self.app.method.assertCheckBox("ON", Use_time_zone_of_GSM_network_status)
        _data_date_time_gsm = ['Часовой пояс']
        self.app.method.assertotMissingTextOnPage(data_time_text, _data_date_time_gsm)

    # Проверка появления выпадающего списка 'Часовой пояс' при отключении чекбокса: Использовать время GSM сети ДАТА И ВРЕМЯ
    def check_box_data_time_Use_time_zone_of_GSM_network_status_off(self):
        self.app.method.checkBox("OFF", Use_time_zone_of_GSM_network_click, Use_time_zone_of_GSM_network_status)
        self.app.method.assertCheckBox("OFF", Use_time_zone_of_GSM_network_status)
        _data_date_time_gsm = ['Часовой пояс']
        self.app.method.assertTextOnPage(data_time_text, _data_date_time_gsm)

    # Адрес сервера - ДАТА И ВРЕМЯ
    def input_data_time_address_server(self, locator=address_server_data_time):
        self.input_server_address(locator)

    # Адрес сервера - ДАТА И ВРЕМЯ
    def input_data_time_address_server_negativ(self, locator=address_server_data_time):
        self.input_server_address_negativ(locator)

    # Проверка сохранения объекта поля ввода
    def save_object_data(self):
        _object = self.app.read_data.data_object()
        with allure.step(f"Ввод данных в поле 'Название объекта: '{_object['name_object']}'"):
            self.app.method.inputValues(value=_object["name_object"], locator=object_name)

        with allure.step(f"Ввод данных в поле Номер объекта: '{_object['number_object']}'"):
            self.app.method.inputValues(value=_object["number_object"], locator=object_number)

        with allure.step(f"Ввод данных в поле Задержка взятия: '{_object['Take_Delay']}'"):
            self.app.method.inputValues(value=_object["Take_Delay"], locator=object_delay_take_on)

        with allure.step(f"Ввод данных в поле Задержка тревоги входа: '{_object['Input_Alarm_Delay']}'"):
            self.app.method.inputValues(value=_object["Input_Alarm_Delay"], locator=object_delay_alarm_enter)

        with allure.step(f"Ввод данных в поле Время автовзятия: '{_object['Auto_arm_time']}'"):
            self.app.method.inputValues(value=_object["Auto_arm_time"], locator=object_time_auto_take_on)

    # Проверка сохранения объекта чекбоксы
    def save_object_check_box(self, randomCB_1, randomCB_2, randomCB_3, randomCB_4):
        with allure.step(f"Перевод чекбокса - Тревога при потере датчика в положение: '{randomCB_1}'"):
            self.app.method.checkBox(randomCB_1, object_sensor_loss_alarm_click, object_sensor_loss_alarm_status)
        with allure.step(f"Перевод чекбокса - Взятие при потерянных датчиках: '{randomCB_2}'"):
            self.app.method.checkBox(randomCB_2, object_taking_with_lost_sensors_click,
                                     object_taking_with_lost_sensors_status)
        # with allure.step(f"Перевод чекбокса - Взятие при датчиках в тревоге: '{randomCB_3}'"):
        #     self.app.method.checkBox(randomCB_3, object_taking_sensors_in_alarm_click,
        #                              object_taking_sensors_in_alarm_status)
        with allure.step(f"Перевод чекбокса - Взятие при датчиках в неисправности: '{randomCB_3}'"):
            self.app.method.checkBox(randomCB_3, object_capturing_with_sensors_in_error_click,
                                     object_capturing_with_sensors_in_error_status)
        with allure.step(f"Перевод чекбокса - Принудительное взятие из тревоги: '{randomCB_4}'"):
            self.app.method.checkBox(randomCB_4, object_forced_take_from_alarm_click,
                                     object_forced_take_from_alarm_status)

    # Проверка сохранения объекта поля ввода
    def save_object_data_limit(self, name, number, delay_take, delay_alarm, time_take_on, randomCB_1,
                               randomCB_2, randomCB_3, randomCB_4):
        with allure.step(f"Ввод данных в поле 'Название объекта: '{name}'"):
            self.app.method.inputValues(value=name, locator=object_name)
        with allure.step(f"Ввод данных в поле Номер объекта: '{number}'"):
            self.app.method.inputValues(value=number, locator=object_number)
        with allure.step(f"Ввод данных в поле Задержка взятия: '{delay_take}'"):
            self.app.method.inputValues(value=delay_take, locator=object_delay_take_on)
        with allure.step(f"Ввод данных в поле Задержка тревоги входа: '{delay_alarm}'"):
            self.app.method.inputValues(value=delay_alarm, locator=object_delay_alarm_enter)
        with allure.step(f"Ввод данных в поле Время автовзятия: '{time_take_on}'"):
            self.app.method.inputValues(value=time_take_on, locator=object_time_auto_take_on)
        with allure.step(f"Перевод чекбокса - Тревога при потере датчика в положение: '{randomCB_1}'"):
            self.app.method.checkBox(randomCB_1, object_sensor_loss_alarm_click, object_sensor_loss_alarm_status)
        with allure.step(f"Перевод чекбокса - Взятие при потерянных датчиках: '{randomCB_2}'"):
            self.app.method.checkBox(randomCB_2, object_taking_with_lost_sensors_click,
                                     object_taking_with_lost_sensors_status)
        # with allure.step(f"Перевод чекбокса - Взятие при датчиках в тревоге: '{randomCB_3}'"):
        #     self.app.method.checkBox(randomCB_3, object_taking_sensors_in_alarm_click,
        #                              object_taking_sensors_in_alarm_status)
        with allure.step(f"Перевод чекбокса - Взятие при датчиках в неисправности: '{randomCB_3}'"):
            self.app.method.checkBox(randomCB_3, object_capturing_with_sensors_in_error_click,
                                     object_capturing_with_sensors_in_error_status)
        with allure.step(f"Перевод чекбокса - Принудительное взятие из тревоги: '{randomCB_4}'"):
            self.app.method.checkBox(randomCB_4, object_forced_take_from_alarm_click,
                                     object_forced_take_from_alarm_status)

    def save_button_click(self):
        with allure.step("Клик по кнопке СОХРАНИТЬ"):
            self.app.method.click((By.XPATH, save_button))
        with allure.step("Проверка всплывающего окна сохранено"):
            self.app.method.click((By.XPATH, '/html/body//button[@class="toast-message-btn-close close-icon"]'))

    def edit_button_click(self):
        with allure.step("Клик по кнопке Редактировать"):
            try:
                time.sleep(0.3)
                self.app.method.click((By.XPATH, edit_button))
                time.sleep(0.1)
            except:
                time.sleep(0.3)
                self.reset_button_click()
                time.sleep(0.1)
                self.app.method.click((By.XPATH, edit_button))
                time.sleep(0.1)

    def set_checkbox_gsm(self):
        self.app.method.checkBox('ON', gsm_Enable_GSM_module_click, gsm_Enable_GSM_module_status)

    def reset_button_click(self):
        with allure.step("Клик по кнопке Редактировать"):
            time.sleep(0.1)
            self.app.method.click((By.XPATH, reset_button))
            time.sleep(0.1)

    def finish_setting(self):
        try:
            with allure.step("Клик по кнопке 'Сбросить'"):
                self.reset_button_click()
        except:
            self.edit_button_click()
            self.reset_button_click()

    # Проверка сохранения объекта поля ввода после входа
    def save_object_data_check(self):
        _object = self.app.read_data.data_object()
        with allure.step(f"Название объекта"):
            self.app.method.assertValues(value=_object["name_object"], locator=object_name)
        with allure.step(f"Номер объекта"):
            self.app.method.assertValues(value=_object["number_object"], locator=object_number)
        with allure.step(f"Задержка взятия"):
            self.app.method.assertValues(value=_object["Take_Delay"], locator=object_delay_take_on)
        with allure.step(f"Задержка тревоги входа"):
            self.app.method.assertValues(value=_object["Input_Alarm_Delay"], locator=object_delay_alarm_enter)
        with allure.step(f"Время автовзятия"):
            self.app.method.assertValues(value=_object["Auto_arm_time"], locator=object_time_auto_take_on)

    # Проверка сохранения объекта чекбоксы после входа
    def save_object_check_box_check(self, randomCB_1, randomCB_2, randomCB_3, randomCB_4):
        with allure.step("Чекбокс: Тревога при потере датчика в положение"):
            self.app.method.assertCheckBox(randomCB_1, object_sensor_loss_alarm_status)
        with allure.step("Чекбокс: Взятие при потерянных датчиках"):
            self.app.method.assertCheckBox(randomCB_2, object_taking_with_lost_sensors_status)
        # with allure.step("Чекбокс: Взятие при датчиках в тревоге"):
        #     self.app.method.assertCheckBox(randomCB_3, object_taking_sensors_in_alarm_status)
        with allure.step("Чекбокс: Взятие при датчиках в неисправности"):
            self.app.method.assertCheckBox(randomCB_3, object_capturing_with_sensors_in_error_status)
        with allure.step("Чекбокс: Принудительное взятие из тревоги"):
            self.app.method.assertCheckBox(randomCB_4, object_forced_take_from_alarm_status)

    def save_object_data_limit_check(self, name, number, delay_take, delay_alarm, time_take_on,
                                     randomCB_1, randomCB_2, randomCB_3, randomCB_4):
        _object = self.app.read_data.data_object()
        with allure.step(f"Название объекта"):
            self.app.method.assertValues(value=name, locator=object_name)
        with allure.step(f"Номер объекта"):
            self.app.method.assertValues(value=number, locator=object_number)
        with allure.step(f"Задержка взятия"):
            self.app.method.assertValues(value=delay_take, locator=object_delay_take_on)
        with allure.step(f"Задержка тревоги входа"):
            self.app.method.assertValues(value=delay_alarm, locator=object_delay_alarm_enter)
        with allure.step(f"Время автовзятия"):
            self.app.method.assertValues(value=time_take_on, locator=object_time_auto_take_on)

        with allure.step("Чекбокс: Тревога при потере датчика в положение"):
            self.app.method.assertCheckBox(randomCB_1, object_sensor_loss_alarm_status)
        with allure.step("Чекбокс: Взятие при потерянных датчиках"):
            self.app.method.assertCheckBox(randomCB_2, object_taking_with_lost_sensors_status)
        # with allure.step("Чекбокс: Взятие при датчиках в тревоге"):
        #     self.app.method.assertCheckBox(randomCB_3, object_taking_sensors_in_alarm_status)
        with allure.step("Чекбокс: Взятие при датчиках в неисправности"):
            self.app.method.assertCheckBox(randomCB_3, object_capturing_with_sensors_in_error_status)
        with allure.step("Чекбокс: Принудительное взятие из тревоги"):
            self.app.method.assertCheckBox(randomCB_4, object_forced_take_from_alarm_status)

    # Проверка сохранения чекбоксов прибора
    def save_device_check_box(self, setting_case_closed, path_alarms,
                              sensor_alarms, fire_path_alarms, fire_sensor_alarms, repeat_events, manage_outputs):
        # with allure.step(f"Перевод чекбокса - 'Включить энергосберегающий режим' в положение: '{power_saving_mode}'"):
        #     self.app.method.checkBox(power_saving_mode, enable_power_saving_mode_click,
        #                              enable_power_saving_mode_status)
        with allure.step(
                f"Перевод чекбокса - 'Разрешить настройку при закрытом корпусе' в положение: '{setting_case_closed}'"):
            self.app.method.checkBox(setting_case_closed, allow_configuration_when_the_case_is_closed_click,
                                     allow_configuration_when_the_case_is_closed_status)
        with allure.step(f"Перевод чекбокса - 'Фиксировать повторные тревоги раздела' в положение: '{path_alarms}'"):
            self.app.method.checkBox(path_alarms, fix_partition_repeated_alarms_click,
                                     fix_partition_repeated_alarms_status)
        with allure.step(f"Перевод чекбокса - 'Фиксировать повторные тревоги датчика' в положение: '{sensor_alarms}'"):
            self.app.method.checkBox(sensor_alarms, fix_repeated_sensor_alarms_click,
                                     fix_repeated_sensor_alarms_status)
        with allure.step(
                f"Перевод чекбокса - 'Фиксировать повторные пожарные тревоги раздела' в положение: '{fire_path_alarms}'"):
            self.app.method.checkBox(fire_path_alarms, fix_repeated_fire_alarms_in_a_section_click,
                                     fix_repeated_fire_alarms_in_a_section_status)
        with allure.step(
                f"Перевод чекбокса - 'Фиксировать повторные пожарные тревоги датчика' в положение: '{fire_sensor_alarms}'"):
            self.app.method.checkBox(fire_sensor_alarms, fix_repeated_fire_alarms_of_the_sensor_click,
                                     fix_repeated_fire_alarms_of_the_sensor_status)
        with allure.step(
                f"Перевод чекбокса - 'Фиксировать повторные события взятия/снятия' в положение: '{repeat_events}'"):
            self.app.method.checkBox(repeat_events, fix_repeated_arming_disarming_events_click,
                                     fix_repeated_arming_disarming_events_status)
        with allure.step(
                f"Перевод чекбокса - 'Управлять выходами при повторном взятии/снятии' в положение: '{manage_outputs}'"):
            self.app.method.checkBox(manage_outputs, control_exits_when_re_arming_disarming_click,
                                     control_exits_when_re_arming_disarming_status)

    # Проверка сохранения чекбоесов прибора после входа
    def save_device_check_box_data(self, setting_case_closed, path_alarms,
                                   sensor_alarms, fire_path_alarms, fire_sensor_alarms, repeat_events, manage_outputs):
        # with allure.step("Чекбокс: Включить энергосберегающий режим"):
        #     self.app.method.assertCheckBox(power_saving_mode, enable_power_saving_mode_status)
        with allure.step("Чекбокс: Разрешить настройку при закрытом корпусе"):
            self.app.method.assertCheckBox(setting_case_closed, allow_configuration_when_the_case_is_closed_status)
        with allure.step("Чекбокс: Фиксировать повторные тревоги раздела"):
            self.app.method.assertCheckBox(path_alarms, fix_partition_repeated_alarms_status)
        with allure.step("Чекбокс: Фиксировать повторные тревоги датчика"):
            self.app.method.assertCheckBox(sensor_alarms, fix_repeated_sensor_alarms_status)
        with allure.step("Чекбокс: Фиксировать повторные пожарные тревоги раздела"):
            self.app.method.assertCheckBox(fire_path_alarms, fix_repeated_fire_alarms_in_a_section_status)
        with allure.step("Чекбокс: Фиксировать повторные пожарные тревоги датчика"):
            self.app.method.assertCheckBox(fire_sensor_alarms, fix_repeated_fire_alarms_of_the_sensor_status)
        with allure.step("Чекбокс: Фиксировать повторные события взятия/снятия"):
            self.app.method.assertCheckBox(repeat_events, fix_repeated_arming_disarming_events_status)
        with allure.step("Чекбокс: Управлять выходами при повторном взятии/снятии"):
            self.app.method.assertCheckBox(manage_outputs, control_exits_when_re_arming_disarming_status)

    # Проверка сохранения настройки световой индикации
    def save_light_indication_settings(self, security_sensors, fire_detectors, process_sensors,
                                       operation_mode, checkbox_reader_indication):
        with allure.step(
                f"Выпадающий список - 'Режим светодиодов для охранных датчиков' выбор позиции: '{security_sensors}'"):
            self.app.method.selectDropdownListByName(LED_mode_for_security_sensors, security_sensors)
        with allure.step(
                f"Выпадающий список - 'Режим светодиодов для пожарных датчиков' выбор позиции: '{fire_detectors}'"):
            self.app.method.selectDropdownListByName(LED_mode_for_fire_detectors, fire_detectors)
        with allure.step(
                f"Выпадающий список - 'Режим светодиодов для технологических датчиков' выбор позиции: '{process_sensors}'"):
            self.app.method.selectDropdownListByName(LED_mode_for_process_sensors, process_sensors)
        with allure.step(f"Выпадающий список - 'Режим работы считывателя' выбор позиции: '{operation_mode}'"):
            self.app.method.selectDropdownListByName(Reader_operation_mode, operation_mode)
        with allure.step(
                f"Перевод чекбокса - 'Инверсия индикации считывателя' в положение: '{checkbox_reader_indication}'"):
            self.app.method.checkBox(checkbox_reader_indication, reader_indication_inversion_click,
                                     reader_indication_inversion_status)

    # Проверка сохранения настроек световой индикации
    def save_light_indication_settings_data(self, security_sensors, fire_detectors, process_sensors,
                                            operation_mode, checkbox_reader_indication):
        with allure.step("Выпадающий список: Режим светодиодов для охранных датчиков"):
            self.app.method.assertSelectionDropdownList(security_sensors, LED_mode_for_security_sensors)
        with allure.step("Выпадающий список: Режим светодиодов для пожарных датчиков"):
            self.app.method.assertSelectionDropdownList(fire_detectors, LED_mode_for_fire_detectors)
        with allure.step("Выпадающий список: Режим светодиодов для технологических датчиков"):
            self.app.method.assertSelectionDropdownList(process_sensors, LED_mode_for_process_sensors)
        with allure.step("Выпадающий список: Режим работы считывателя"):
            self.app.method.assertSelectionDropdownList(operation_mode, Reader_operation_mode)
        with allure.step("Чекбокс: Инверсия индикации считывателя"):
            self.app.method.assertCheckBox(checkbox_reader_indication, reader_indication_inversion_status)

    # Проверка данных радио
    def save_radio_data(self, chanel_list):
        with allure.step(f"Перевод чекбокса - Включить радиомодуль: 'ON'"):
            self.app.method.checkBox('ON', radio_modul_on_click, radio_modul_on_status)
        with allure.step(f"Выпадающий список - 'Канал выбор позиции: '{chanel_list}'"):
            self.app.method.selectDropdownListByName(radio_chanel_button, chanel_list)
        _radio = self.app.read_data.data_radio()
        with allure.step(
                f"Ввод данных в поле - Время разрешения добавления новых датчиков: '{_radio['Resolution_time_for_adding_new_sensors']}'"):
            self.app.method.inputValues(value=_radio["Resolution_time_for_adding_new_sensors"],
                                        locator=resolution_time_for_adding_new_sensors)

        with allure.step(f"Ввод данных в поле - Период опроса датчиков: '{_radio['Sensor_polling_period']}'"):
            self.app.method.inputValues(value=_radio["Sensor_polling_period"], locator=sensor_polling_period)

    # Проверка данных радио
    def save_radio_data_limit(self, randomCB, chanel_list, time_add_sensor, periud_sensor):
        with allure.step(f"Перевод чекбокса - Включить радиомодуль: '{randomCB}'"):
            self.app.method.checkBox(randomCB, radio_modul_on_click, radio_modul_on_status)
        with allure.step(f"Выпадающий список - 'Канал выбор позиции: '{chanel_list}'"):
            self.app.method.selectDropdownListByName(radio_chanel_button, chanel_list)
        _radio = self.app.read_data.data_radio()
        with allure.step(
                f"Ввод данных в поле - Время разрешения добавления новых датчиков: '{time_add_sensor}'"):
            self.app.method.inputValues(value=time_add_sensor,
                                        locator=resolution_time_for_adding_new_sensors)
        with allure.step(f"Ввод данных в поле - Период опроса датчиков: '{periud_sensor}'"):
            self.app.method.inputValues(value=periud_sensor, locator=sensor_polling_period)

    # Проверка сохранения радио после входа
    def save_radio_data_enter(self, chanel_list):
        # with allure.step("Чекбокс: Включить радиомодуль"):
        #     self.app.method.assertCheckBox('ON', radio_modul_on_status)
        with allure.step("Выпадающий список: Канал"):
            self.app.method.assertSelectionDropdownList(chanel_list, radio_chanel_button)
        _radio = self.app.read_data.data_radio()
        with allure.step("Время разрешения добавления новых датчиков"):
            self.app.method.assertValues(value=_radio["Resolution_time_for_adding_new_sensors"],
                                         locator=resolution_time_for_adding_new_sensors)
        with allure.step("Период опроса датчиков"):
            self.app.method.assertValues(value=_radio["Sensor_polling_period"], locator=sensor_polling_period)

    # Проверка сохранения радио после входа
    def save_radio_data_enter_limit(self, chanel_list, time_add_sensor, periud_sensor):
        with allure.step("Выпадающий список: Канал"):
            self.app.method.assertSelectionDropdownList(chanel_list, radio_chanel_button)
        with allure.step("Время разрешения добавления новых датчиков"):
            self.app.method.assertValues(value=time_add_sensor,
                                         locator=resolution_time_for_adding_new_sensors)
        with allure.step("Период опроса датчиков"):
            self.app.method.assertValues(value=periud_sensor, locator=sensor_polling_period)

    # Проверка данных ethernet
    def save_ethernet_data(self, randomCB_1, randomCB_2, randomCB_3, randomCB_4, randomCB_5, randomCB_6,
                           Establish_network_connections):
        _ethernet = self.app.read_data.data_ethernet()
        with allure.step(f"Ввод данных в поле - MAC адрес: '{(_ethernet['MAC_address']).upper()}'"):
            self.app.method.inputValues(value=_ethernet['MAC_address'], locator=ethernet_mac_address)
        with allure.step(f"Ввод данных в поле - Название сервера: '{_ethernet['Server_name']}'"):
            self.app.method.inputValues(value=_ethernet['Server_name'], locator=ethernet_name_server)
        with allure.step(f"Ввод данных в поле - Адрес IPv4: '{_ethernet['Address_IPv4']}'"):
            self.app.method.inputValues(value=_ethernet['Address_IPv4'], locator=ethernet_address_IPv4)
        with allure.step(f"Ввод данных в поле - Маска подсети: '{_ethernet['Subnet_mask']}'"):
            self.app.method.inputValues(value=_ethernet['Subnet_mask'], locator=ethernet_subnet_mask)
        with allure.step(f"Ввод данных в поле - Основной шлюз: '{_ethernet['Main_gate']}'"):
            self.app.method.inputValues(value=_ethernet['Main_gate'], locator=ethernet_main_gate)
        with allure.step(f"Ввод данных в поле - Предпочтительный DNS сервер: '{_ethernet['Preferred_DNS_Server']}'"):
            self.app.method.inputValues(value=_ethernet['Preferred_DNS_Server'],
                                        locator=ethernet_preferred_DNS_server)
        with allure.step(f"Ввод данных в поле - Альтернативный DNS сервер: '{_ethernet['Alternative_DNS_Server']}'"):
            self.app.method.inputValues(value=_ethernet['Alternative_DNS_Server'],
                                        locator=ethernet_alternative_DNS_server)
        with allure.step(f"Ввод данных в поле - Локальный IPv6 адрес: '{_ethernet['Local_IPv6_address']}'"):
            self.app.method.inputValues(value=_ethernet['Local_IPv6_address'], locator=ethernet_local_ipv6)
        with allure.step(f"Ввод данных в поле - Глобальный IPv6 адрес: '{_ethernet['Global_IPv6_address']}'"):
            self.app.method.inputValues(value=_ethernet['Global_IPv6_address'], locator=ethernet_global_ipv6)
        with allure.step(
                f"Ввод данных в поле - Предпочтительный IPv6 DNS сервер: '{_ethernet['Preferred_IPv6_DNS_Server']}'"):
            self.app.method.inputValues(value=_ethernet['Preferred_IPv6_DNS_Server'],
                                        locator=ethernet_preferred_IPv6_DNS_server)
        with allure.step(
                f"Ввод данных в поле - Альтернативный IPv6 DNS сервер: '{_ethernet['Alternative_IPv6_DNS_Server']}'"):
            self.app.method.inputValues(value=_ethernet['Alternative_IPv6_DNS_Server'],
                                        locator=ethernet_alternative_IPv6_DNS_server)
        with allure.step(
                f"Выпадающий список - 'Устанавливать сетевые подключения через: '{Establish_network_connections}'"):
            self.app.method.selectDropdownListByName(ethernet_network_connections_button, Establish_network_connections)
        with allure.step(f"Перевод чекбокса - Получать IPv4 адрес и настройки автоматически: '{randomCB_1}'"):
            self.app.method.checkBox(randomCB_1, ethernet_obtain_IPv4_address_and_settings_automatically_click,
                                     ethernet_obtain_IPv4_address_and_settings_automatically_status)
        with allure.step(f"Перевод чекбокса - Использовать как сервер: '{randomCB_2}'"):
            self.app.method.checkBox(randomCB_2, ethernet_use_as_server_click, ethernet_use_as_server_status)
        with allure.step(f"Перевод чекбокса - Получать адрес IPv6 от DHCP автоматически: '{randomCB_3}'"):
            self.app.method.checkBox(randomCB_3, ethernet_obtain_an_IPv6_address_from_DHCP_automatically_click,
                                     ethernet_obtain_an_IPv6_address_from_DHCP_automatically_status)
        with allure.step(f"Перевод чекбокса - Разрешить удаленное управление: '{randomCB_4}'"):
            self.app.method.checkBox(randomCB_4, ethernet_allow_remote_control_click,
                                     ethernet_allow_remote_control_status)
        with allure.step(f"Перевод чекбокса - Получать адрес IPv6 от SLAAC автоматически: '{randomCB_5}'"):
            self.app.method.checkBox(randomCB_5, ethernet_obtain_an_IPv6_address_from_SLAAC_automatically_click,
                                     ethernet_obtain_an_IPv6_address_from_SLAAC_automatically_status)
        with allure.step(f"Перевод чекбокса - Разрешить незащищенное HTTP-соединение: '{randomCB_6}'"):
            self.app.method.checkBox(randomCB_6, ethernet_allow_insecure_HTTP_connection_click,
                                     ethernet_allow_insecure_HTTP_connection_status)

    # Проверка сохранения ethernet после входа
    def save_ethernet_data_enter(self, randomCB_1, randomCB_2, randomCB_3, randomCB_4, randomCB_5, randomCB_6,
                                 Establish_network_connections):
        _ethernet = self.app.read_data.data_ethernet()
        with allure.step("Поле ввода: MAC адрес"):
            self.app.method.assertValues(value=(_ethernet['MAC_address']).upper(), locator=ethernet_mac_address)
        with allure.step("Поле ввода: Название сервера"):
            self.app.method.assertValues(value=_ethernet['Server_name'], locator=ethernet_name_server)
        with allure.step("Поле ввода: Адрес IPv4"):
            self.app.method.assertValues(value=_ethernet['Address_IPv4'], locator=ethernet_address_IPv4)
        with allure.step("Поле ввода: Маска подсети"):
            self.app.method.assertValues(value=_ethernet['Subnet_mask'], locator=ethernet_subnet_mask)
        with allure.step("Поле ввода: Основной шлюз"):
            self.app.method.assertValues(value=_ethernet['Main_gate'], locator=ethernet_main_gate)
        with allure.step("Поле ввода: Предпочтительный DNS сервер"):
            self.app.method.assertValues(value=_ethernet['Preferred_DNS_Server'],
                                         locator=ethernet_preferred_DNS_server)
        with allure.step("Поле ввода: Альтернативный DNS сервер"):
            self.app.method.assertValues(value=_ethernet['Alternative_DNS_Server'],
                                         locator=ethernet_alternative_DNS_server)
        with allure.step("Поле ввода: Локальный IPv6 адрес"):
            self.app.method.assertValues(value=_ethernet['Local_IPv6_address'], locator=ethernet_local_ipv6)
        with allure.step("Поле ввода: Глобальный IPv6 адрес"):
            self.app.method.assertValues(value=_ethernet['Global_IPv6_address'], locator=ethernet_global_ipv6)
        with allure.step("Поле ввода: Предпочтительный IPv6 DNS сервер"):
            self.app.method.assertValues(value=_ethernet['Preferred_IPv6_DNS_Server'],
                                         locator=ethernet_preferred_IPv6_DNS_server)
        with allure.step("Поле ввода: Альтернативный IPv6 DNS сервер"):
            self.app.method.assertValues(value=_ethernet['Alternative_IPv6_DNS_Server'],
                                         locator=ethernet_alternative_IPv6_DNS_server)

        with allure.step("Выпадающий список: Канал"):
            self.app.method.assertSelectionDropdownList(Establish_network_connections,
                                                        ethernet_network_connections_button)

        with allure.step("Чекбокс: Получать IPv4 адрес и настройки автоматически"):
            self.app.method.assertCheckBox(randomCB_1, ethernet_obtain_IPv4_address_and_settings_automatically_status)
        with allure.step("Чекбокс: Использовать как сервер"):
            self.app.method.assertCheckBox(randomCB_2, ethernet_use_as_server_status)
        with allure.step("Чекбокс: Получать адрес IPv6 от DHCP автоматически"):
            self.app.method.assertCheckBox(randomCB_3, ethernet_obtain_an_IPv6_address_from_DHCP_automatically_status)
        with allure.step("Чекбокс: Разрешить удаленное управление"):
            self.app.method.assertCheckBox(randomCB_4, ethernet_allow_remote_control_status)
        with allure.step("Чекбокс: Получать адрес IPv6 от SLAAC автоматически"):
            self.app.method.assertCheckBox(randomCB_5,
                                           ethernet_obtain_an_IPv6_address_from_SLAAC_automatically_status)
        with allure.step("Чекбокс: Разрешить незащищенное HTTP-соединение"):
            self.app.method.assertCheckBox(randomCB_6, ethernet_allow_insecure_HTTP_connection_status)

    # ввод данных для сохранения настройки звуковой индикации
    def save_volum_indication_data(self, main, Alarm, Fire, Taking_section,
                                   Removing_partition, Take_Delay, Not_taking, Sections_partially,
                                   Adding_sensor, Bell):
        _volum_indication = self.app.read_data.data_volum_indication()
        with allure.step(f"Перевод чекбокса - Включить: '{main}'"):
            self.app.method.checkBox(main, volum_on_click, volum_on_status)
        with allure.step(f"Перевод чекбокса - Тревога: '{Alarm}'"):
            self.app.method.checkBox(Alarm, volum_alarm_click, volum_alarm_status)
        with allure.step(f"Перевод чекбокса - Пожар: '{Fire}'"):
            self.app.method.checkBox(Fire, volum_fire_click, volum_fire_status)
        with allure.step(f"Перевод чекбокса - Взятие раздела: '{Taking_section}'"):
            self.app.method.checkBox(Taking_section, volum_take_path_click, volum_take_path_status)
        with allure.step(f"Перевод чекбокса - Снятие раздела: '{Removing_partition}'"):
            self.app.method.checkBox(Removing_partition, volum_take_off_path_click, volum_take_off_path_status)
        with allure.step(f"Перевод чекбокса - Задержка взятия: '{Take_Delay}'"):
            self.app.method.checkBox(Take_Delay, volum_delay_take_click, volum_delay_take_status)
        with allure.step(f"Перевод чекбокса - Невзятие: '{Not_taking}'"):
            self.app.method.checkBox(Not_taking, volum_no_take_click, volum_no_take_status)
        with allure.step(f"Перевод чекбокса - Разделы частично взяты: '{Sections_partially}'"):
            self.app.method.checkBox(Sections_partially, volum_some_take_on_click, volum_some_take_on_status)
        with allure.step(f"Перевод чекбокса - Добавление датчика: '{Adding_sensor}'"):
            self.app.method.checkBox(Adding_sensor, volum_add_sensor_click, volum_add_sensor_status)
        with allure.step(f"Перевод чекбокса - Колокольчик: '{Bell}'"):
            self.app.method.checkBox(Bell, volum_bang_click, volum_bang_status)
        with allure.step(f"Ввод данных в поле - Длительность сигнала: '{_volum_indication['Signal_duration']}'"):
            self.app.method.inputValues(value=_volum_indication["Signal_duration"],
                                        locator=volum_indication_signal_duration)
        with allure.step(f"Перевод виджета - Громкость событий в положение: '{_volum_indication['Event_volume']}'"):
            self.app.method.sliderWidget(_volum_indication["Event_volume"], event_volume_slider_widget)
        with allure.step(f"Перевод виджета - Громкость тревог в положение: '{_volum_indication['Alarm_volume']}'"):
            self.app.method.sliderWidget(_volum_indication["Alarm_volume"], alarm_volume_slider_widget)

    # ввод данных для сохранения настройки звуковой индикации
    def save_volum_indication_data_limit(self, signal_duration_value, Event_volume, Alarm_volume, main, Alarm, Fire,
                                         Taking_section,
                                         Removing_partition, Take_Delay, Not_taking, Sections_partially,
                                         Adding_sensor, Bell):
        with allure.step(f"Перевод чекбокса - Включить: '{main}'"):
            self.app.method.checkBox(main, volum_on_click, volum_on_status)
        with allure.step(f"Перевод чекбокса - Тревога: '{Alarm}'"):
            self.app.method.checkBox(Alarm, volum_alarm_click, volum_alarm_status)
        with allure.step(f"Перевод чекбокса - Пожар: '{Fire}'"):
            self.app.method.checkBox(Fire, volum_fire_click, volum_fire_status)
        with allure.step(f"Перевод чекбокса - Взятие раздела: '{Taking_section}'"):
            self.app.method.checkBox(Taking_section, volum_take_path_click, volum_take_path_status)
        with allure.step(f"Перевод чекбокса - Снятие раздела: '{Removing_partition}'"):
            self.app.method.checkBox(Removing_partition, volum_take_off_path_click, volum_take_off_path_status)
        with allure.step(f"Перевод чекбокса - Задержка взятия: '{Take_Delay}'"):
            self.app.method.checkBox(Take_Delay, volum_delay_take_click, volum_delay_take_status)
        with allure.step(f"Перевод чекбокса - Невзятие: '{Not_taking}'"):
            self.app.method.checkBox(Not_taking, volum_no_take_click, volum_no_take_status)
        with allure.step(f"Перевод чекбокса - Разделы частично взяты: '{Sections_partially}'"):
            self.app.method.checkBox(Sections_partially, volum_some_take_on_click, volum_some_take_on_status)
        with allure.step(f"Перевод чекбокса - Добавление датчика: '{Adding_sensor}'"):
            self.app.method.checkBox(Adding_sensor, volum_add_sensor_click, volum_add_sensor_status)
        with allure.step(f"Перевод чекбокса - Колокольчик: '{Bell}'"):
            self.app.method.checkBox(Bell, volum_bang_click, volum_bang_status)
        with allure.step(f"Ввод данных в поле - Длительность сигнала: '{signal_duration_value}'"):
            self.app.method.inputValues(value=signal_duration_value,
                                        locator=volum_indication_signal_duration)
        with allure.step(f"Перевод виджета - Громкость событий в положение: '{Event_volume}'"):
            self.app.method.sliderWidget(Event_volume, event_volume_slider_widget)
        with allure.step(f"Перевод виджета - Громкость тревог в положение: '{Alarm_volume}'"):
            self.app.method.sliderWidget(Alarm_volume, alarm_volume_slider_widget)

    # Проверка сохранения настроек звуковой индикации после входа
    def save_volum_indication_data_enter(self, main, Alarm, Fire, Taking_section,
                                         Removing_partition, Take_Delay, Not_taking, Sections_partially,
                                         Adding_sensor, Bell):
        _volum_indication = self.app.read_data.data_volum_indication()
        with allure.step("Чекбокс: Включить"):
            self.app.method.assertCheckBox(main, volum_on_status)
        with allure.step("Чекбокс: Тревога"):
            self.app.method.assertCheckBox(Alarm, volum_alarm_status)
        with allure.step("Чекбокс: Пожар"):
            self.app.method.assertCheckBox(Fire, volum_fire_status)
        with allure.step("Чекбокс: Взятие раздела"):
            self.app.method.assertCheckBox(Taking_section, volum_take_path_status)
        with allure.step("Чекбокс: Снятие раздела"):
            self.app.method.assertCheckBox(Removing_partition, volum_take_off_path_status)
        with allure.step("Чекбокс: Задержка взятия"):
            self.app.method.assertCheckBox(Take_Delay, volum_delay_take_status)
        with allure.step("Чекбокс: Невзятие"):
            self.app.method.assertCheckBox(Not_taking, volum_no_take_status)
        with allure.step("Чекбокс: Разделы частично взяты"):
            self.app.method.assertCheckBox(Sections_partially, volum_some_take_on_status)
        with allure.step("Чекбокс: Добавление датчика"):
            self.app.method.assertCheckBox(Adding_sensor, volum_add_sensor_status)
        with allure.step("Чекбокс: Колокольчик"):
            self.app.method.assertCheckBox(Bell, volum_bang_status)

        with allure.step("Поле ввода: Длительность сигнала"):
            self.app.method.assertValues(value=_volum_indication['Signal_duration'],
                                         locator=volum_indication_signal_duration)
        with allure.step("Виджет ползунок: Громкость событий"):
            self.app.method.assertSliderWidget(_volum_indication["Event_volume"], event_volume_slider_widget)
        with allure.step("Виджет ползунок: Громкость тревог в положение"):
            self.app.method.assertSliderWidget(_volum_indication["Alarm_volume"], alarm_volume_slider_widget)

    # Проверка сохранения настроек звуковой индикации после входа
    def save_volum_indication_data_enter_limit(self, signal_duration_value, Event_volume, Alarm_volume, main, Alarm,
                                               Fire, Taking_section,
                                               Removing_partition, Take_Delay, Not_taking, Sections_partially,
                                               Adding_sensor, Bell):
        with allure.step("Чекбокс: Включить"):
            self.app.method.assertCheckBox(main, volum_on_status)
        with allure.step("Чекбокс: Тревога"):
            self.app.method.assertCheckBox(Alarm, volum_alarm_status)
        with allure.step("Чекбокс: Пожар"):
            self.app.method.assertCheckBox(Fire, volum_fire_status)
        with allure.step("Чекбокс: Взятие раздела"):
            self.app.method.assertCheckBox(Taking_section, volum_take_path_status)
        with allure.step("Чекбокс: Снятие раздела"):
            self.app.method.assertCheckBox(Removing_partition, volum_take_off_path_status)
        with allure.step("Чекбокс: Задержка взятия"):
            self.app.method.assertCheckBox(Take_Delay, volum_delay_take_status)
        with allure.step("Чекбокс: Невзятие"):
            self.app.method.assertCheckBox(Not_taking, volum_no_take_status)
        with allure.step("Чекбокс: Разделы частично взяты"):
            self.app.method.assertCheckBox(Sections_partially, volum_some_take_on_status)
        with allure.step("Чекбокс: Добавление датчика"):
            self.app.method.assertCheckBox(Adding_sensor, volum_add_sensor_status)
        with allure.step("Чекбокс: Колокольчик"):
            self.app.method.assertCheckBox(Bell, volum_bang_status)
        with allure.step("Поле ввода: Длительность сигнала"):
            self.app.method.assertValues(value=signal_duration_value,
                                         locator=volum_indication_signal_duration)
        with allure.step("Виджет ползунок: Громкость событий"):
            self.app.method.assertSliderWidget(Event_volume, event_volume_slider_widget)
        with allure.step("Виджет ползунок: Громкость тревог в положение"):
            self.app.method.assertSliderWidget(Alarm_volume, alarm_volume_slider_widget)

    # Сохранение настроек даты и время
    def save_data_time(self, randomCB_1, randomCB_2, UTC):
        with allure.step(f"Перевод чекбокса - Использовать временную зону GSM сети: '{randomCB_1}'"):
            self.app.method.checkBox(randomCB_1, Use_time_zone_of_GSM_network_click,
                                     Use_time_zone_of_GSM_network_status)
        with allure.step(f"Выпадающий список - Часовой пояс: '{UTC}'"):
            self.app.method.selectDropdownListByName(date_time_dropdown_2, UTC)

        with allure.step(f"Перевод чекбокса - Переход на летнее время: '{randomCB_2}'"):
            self.app.method.checkBox(randomCB_2, Daylight_Saving_Time_click, Daylight_Saving_Time_status)

    # Проверка настроек даты и время после входа
    def save_data_time_enter(self, randomCB_1, randomCB_2, UTC):
        with allure.step("Чекбокс: Использовать временную зону GSM сети"):
            self.app.method.assertCheckBox(randomCB_1, Use_time_zone_of_GSM_network_status)
        with allure.step("Чекбокс: Переход на летнее время"):
            self.app.method.assertCheckBox(randomCB_2, Daylight_Saving_Time_status)
        with allure.step("Выпадающий список: Часовой пояс"):
            self.app.method.assertSelectionDropdownList(UTC, date_time_dropdown_2)

    # Сохранение настроек даты и время
    def save_data_time_2(self, UTC):
        _data_date_time = self.app.read_data.data_date_time()
        with allure.step(f"Выпадающий список - Часовой пояс: '{UTC}'"):
            self.app.method.selectDropdownListByName(date_time_dropdown_2, UTC)
        with allure.step(f"Ввод данных в поле - Адрес сервера: '{_data_date_time['server_address']}'"):
            self.app.method.inputValues(value=_data_date_time["server_address"],
                                        locator=address_server_data_time)

    # Проверка настроек даты и время после входа
    def save_data_time_enter_2(self, UTC):
        _data_date_time = self.app.read_data.data_date_time()
        with allure.step("Выпадающий список: Часовой пояс"):
            self.app.method.assertSelectionDropdownList(UTC, date_time_dropdown_2)
        with allure.step("Поле ввода: Адрес сервера"):
            self.app.method.assertValues(value=_data_date_time['server_address'],
                                         locator=address_server_data_time)

    def use_gsm_time_off(self):
        self.app.method.checkBox("OFF", Use_time_zone_of_GSM_network_click, Use_time_zone_of_GSM_network_status)

    # Проверка данных gsm
    def save_gsm_data(self, modul_on, use_gprs, use_reserv_sim, use_ussd, balans_not, translations_event):
        _gsm = self.app.read_data.data_gsm()
        with allure.step(f"Перевод чекбокса - Включить модуль GSM: '{modul_on}'"):
            self.app.method.checkBox(modul_on, gsm_Enable_GSM_module_click, gsm_Enable_GSM_module_status)
        with allure.step(f"Перевод чекбокса - Использовать GPRS: '{use_gprs}'"):
            self.app.method.checkBox(use_gprs, gsm_Use_GPRS_click, gsm_Use_GPRS_status)
        with allure.step(f"Перевод чекбокса - Использовать резервную SIM: '{use_reserv_sim}'"):
            self.app.method.checkBox(use_reserv_sim, gsm_Use_backup_SIM_click, gsm_Use_backup_SIM_status)
        with allure.step(f"Перевод чекбокса - Разрешить USSD: '{use_ussd}'"):
            self.app.method.checkBox(use_ussd, gsm_Allow_USSD_click, gsm_Allow_USSD_status)
        with allure.step(f"Перевод чекбокса - Разрешить трансляцию событий: '{translations_event}'"):
            self.app.method.checkBox(translations_event, gsm_Allow_Event_Broadcast_click,
                                     gsm_Allow_Event_Broadcast_status)
        with allure.step(
                f"Ввод данных в поле - Число знаков номера для проверки: '{_gsm['Resolution_time_for_adding_new_sensors']}'"):
            self.app.method.inputValues(value=_gsm['Resolution_time_for_adding_new_sensors'],
                                        locator=number_of_digits_of_the_number_to_check)
        with allure.step(f"Ввод данных в поле - Порог уведомления о балансе: '{_gsm['Sensor_polling_period']}'"):
            self.app.method.inputValues(value=_gsm['Sensor_polling_period'],
                                        locator=balance_notification_threshold)
        with allure.step(f"Ввод данных в поле SIM 1 - PIN: '{_gsm['SIM_1_PIN']}'"):
            self.app.method.inputValues(value=_gsm['SIM_1_PIN'], locator=PIN_SIM_1)
        with allure.step(f"Ввод данных в поле SIM 2 - PIN: '{_gsm['SIM_2_PIN']}'"):
            self.app.method.inputValues(value=_gsm['SIM_2_PIN'], locator=PIN_SIM_2)
        with allure.step(f"Ввод данных в поле SIM 1 - USSD-код запроса баланса: '{_gsm['SIM_1_USSD']}'"):
            self.app.method.inputValues(value=_gsm['SIM_1_USSD'], locator=USSD_SIM_1)
        with allure.step(f"Ввод данных в поле SIM 2 - USSD-код запроса баланса: '{_gsm['SIM_2_USSD']}'"):
            self.app.method.inputValues(value=_gsm['SIM_2_USSD'], locator=USSD_SIM_2)
        with allure.step(f"Ввод данных в поле SIM 1 - APN: '{_gsm['APN_1']}'"):
            self.app.method.inputValues(value=_gsm['APN_1'], locator=APN_SIM_1)
        with allure.step(f"Ввод данных в поле SIM 2 - APN: '{_gsm['APN_2']}'"):
            self.app.method.inputValues(value=_gsm['APN_2'], locator=APN_SIM_2)
        with allure.step(f"Ввод данных в поле SIM 1 - Пользователь: '{_gsm['login_sim_1']}'"):
            self.app.method.inputValues(value=_gsm['login_sim_1'], locator=USER_SIM_1)
        with allure.step(f"Ввод данных в поле SIM 2 - Пользователь: '{_gsm['login_sim_2']}'"):
            self.app.method.inputValues(value=_gsm['login_sim_2'], locator=USER_SIM_2)
        with allure.step(f"Ввод данных в поле SIM 1 - Пароль: '{_gsm['password_sim_1']}'"):
            self.app.method.inputValues(value=_gsm['password_sim_1'], locator=PASSWORD_SIM_1)
        with allure.step(f"Ввод данных в поле SIM 2 - Пароль: '{_gsm['password_sim_2']}'"):
            self.app.method.inputValues(value=_gsm['password_sim_2'], locator=PASSWORD_SIM_2)

    # Проверка данных gsm - после входа
    def save_gsm_data_enter(self, modul_on, use_gprs, use_reserv_sim, use_ussd, balans_not, translations_event):
        _gsm = self.app.read_data.data_gsm()
        with allure.step("Чекбокс: Включить модуль GSM"):
            self.app.method.assertCheckBox(modul_on, gsm_Enable_GSM_module_status)
        with allure.step("Чекбокс: Использовать GPRS"):
            self.app.method.assertCheckBox(use_gprs, gsm_Use_GPRS_status)
        with allure.step("Чекбокс: Использовать резервную SIM"):
            self.app.method.assertCheckBox(use_reserv_sim, gsm_Use_backup_SIM_status)
        with allure.step("Чекбокс: Разрешить USSD"):
            self.app.method.assertCheckBox(use_ussd, gsm_Allow_USSD_status)
        with allure.step("Чекбокс: Разрешить трансляцию событий"):
            self.app.method.assertCheckBox(translations_event, gsm_Allow_Event_Broadcast_status)

        with allure.step("Поле ввода: Число знаков номера для проверки"):
            self.app.method.assertValues(value=_gsm['Resolution_time_for_adding_new_sensors'],
                                         locator=number_of_digits_of_the_number_to_check)
        with allure.step("Поле ввода: Порог уведомления о балансе"):
            self.app.method.assertValues(value=_gsm['Sensor_polling_period'],
                                         locator=balance_notification_threshold)
        with allure.step("Поле ввода: SIM 1 - PIN"):
            self.app.method.assertValues(value=_gsm['SIM_1_PIN'], locator=PIN_SIM_1)
        with allure.step("Поле ввода: SIM 2 - PIN"):
            self.app.method.assertValues(value=_gsm['SIM_2_PIN'], locator=PIN_SIM_2)
        with allure.step("Поле ввода: SIM 1 - USSD-код запроса баланса"):
            self.app.method.assertValues(value=_gsm['SIM_1_USSD'], locator=USSD_SIM_1)
        with allure.step("Поле ввода: SIM 2 - USSD-код запроса баланса"):
            self.app.method.assertValues(value=_gsm['SIM_2_USSD'], locator=USSD_SIM_2)
        with allure.step("Поле ввода: SIM 1 - APN"):
            self.app.method.assertValues(value=_gsm['APN_1'], locator=APN_SIM_1)
        with allure.step("Поле ввода: SIM 2 - APN"):
            self.app.method.assertValues(value=_gsm['APN_2'], locator=APN_SIM_2)
        with allure.step("Поле ввода: SIM 1 - Пользователь"):
            self.app.method.assertValues(value=_gsm['login_sim_1'], locator=USER_SIM_1)
        with allure.step("Поле ввода: SIM 2 - Пользователь"):
            self.app.method.assertValues(value=_gsm['login_sim_2'], locator=USER_SIM_2)
        with allure.step("Поле ввода: SIM 1 - Пароль"):
            self.app.method.assertValues(value=_gsm['password_sim_1'], locator=PASSWORD_SIM_1)
        with allure.step("Поле ввода: Пароль"):
            self.app.method.assertValues(value=_gsm['password_sim_2'], locator=PASSWORD_SIM_2)

    def modul_settings_gsm_on(self):
        self.app.method.checkBox("ON", gsm_Enable_GSM_module_click, gsm_Enable_GSM_module_status)
