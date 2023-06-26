# -*- coding: utf-8 -*-
import time
from dataclasses import dataclass

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from locators.destinations_locators import *


@dataclass
class DirectionsHelper:
    app: any

    # Проверка ввода поле Название
    def input_destination_name(self, locator=destination_name):
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
            self.app.method.assertEqual('1' * 62, '1' * 62, locator)
            self.app.method.assertEqual('1' * 63, '1' * 63, locator)
            self.app.method.assertEqual('г' * 31 + '1', 'г' * 31 + '1', locator)

    # Проверка ввода поле Название
    def input_destination_name_negativ(self, locator=destination_name):
        with allure.step("Проверка ввода пустого значения"):
            self.app.method.assertEqual('', '', locator)
        with allure.step("Проверка ввода граничных значений внутри диапазона"):
            self.app.method.assert_field('1' * 64, locator, destination_name_error)
            self.app.method.assert_field('г' * 32, locator, destination_name_error)

    # Проверка ввода Код настройки
    def input_cod_posutiv(self, locator):
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

    # Проверка ввода Код настройки
    def input_cod_negativ(self, locator):
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
    def input_phone_number_positiv(self, locator):
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

    # Проверка поля Количество повторов
    def input_count_num_99_positiv(self, locator):
        with allure.step("Проверка ввода цифр"):
            for i in range(10):
                self.app.method.assertEqual(i, i, locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual('0', '0', locator)
            self.app.method.assertEqual(1, 1, locator)
            self.app.method.assertEqual(98, 98, locator)
            self.app.method.assertEqual(99, 99, locator)

    # Проверка поля Количество
    def input_count_num_99_negativ(self, locator):
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
            self.app.method.assertEqual("!#$%&'()*+,-./:;<=>?@[]^_`{|}~", "", locator)
        with allure.step("Проверка ввода совместных значений"):
            self.app.method.assertEqual('(123  АБВABC!@#', '12', locator)
        with allure.step("Проверка ввода пробелов"):
            self.app.method.assertEqual('   ', '', locator)
            self.app.method.assertEqual('12   ', '12', locator)
            self.app.method.assertEqual('   12', '12', locator)
            self.app.method.assertEqual('1 2', '12', locator)
        with allure.step("Проверка ввода дробного числа "):
            self.app.method.assertEqual('1.1', '11', locator)
            self.app.method.assertEqual('0.1', '1', locator)
            self.app.method.assertEqual('1,1', '11', locator)
            self.app.method.assertEqual('0,1', '1', locator)
        with allure.step("Проверка ввода пустого значения"):
            self.app.method.assertEqual('', '', locator)
        with allure.step("Проверка ввода отрицательного числа"):
            self.app.method.assertEqual('-1', '1', locator)
        with allure.step("Проверка ввода очень большого числа"):
            self.app.method.assertEqual('1' * 1000, '11', locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual('100', '10', locator)

    # Проверка поля время 24_00
    def input_time_positiv(self, locator):
        with allure.step("Проверка ввода цифр"):
            for i in range(10):
                self.app.method.assertEqual(i, i, locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual('00:00', '00:00', locator)
            self.app.method.assertEqual('00:01', '00:01', locator)
            self.app.method.assertEqual('23:59', '23:59', locator)

    # Проверка поля время 24_00
    def input_time_negativ(self, locator):
        with allure.step("Проверка ввода латинских букв в нижнем регистре"):
            self.app.method.assertEqual('abcdefghijklmnopqrstuvwxyz', '', locator)
        with allure.step("Проверка ввода латинских букв в верхнем регистре"):
            self.app.method.assertEqual('ABCDEFGHIJKLMNOPQRSTUVWXYZ', '', locator)
        with allure.step("Проверка ввода Русских букв в нижнем регистре"):
            self.app.method.assertEqual("ёйцукенгшщзхъфывапролджэячсмитьбю", "", locator)
        with allure.step("Проверка ввода Русских букв в верхнем регистре"):
            self.app.method.assertEqual("АПРОЛДЖЭЯЧСМИТЬБЮЁЙЦУКЕНГШЩЗХЪФЫВ", "", locator)
        with allure.step("Проверка ввода спецсимволов"):
            self.app.method.assertEqual("!#$%&'()*+,-./:;<=>?@[]^_`{|}~", ":", locator)
        with allure.step("Проверка ввода совместных значений(буквы/цифры/спецсимволы)"):
            self.app.method.assertEqual('123  АБВABC!@#', '12:3', locator)
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
            self.app.method.assertEqual(9 * 10000000000000, '90:00', locator)
        with allure.step("Проверка ввода отрицательного числа"):
            self.app.method.assertEqual('-1', '1', locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual(99999, '99:99', locator)

    # Проверка поля Адрес
    def input_adress_domen_positiv(self, locator):
        with allure.step("Проверка ввода цифр"):
            for i in range(10):
                self.app.method.assertEqual(i, i, locator)
        with allure.step("Проверка ввода латинских букв в нижнем регистре"):
            self.app.method.assertEqual('abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz', locator)
        with allure.step("Проверка ввода латинских букв в верхнем регистре"):
            self.app.method.assertEqual('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', locator)
        with allure.step("Проверка ввода Русских букв в нижнем регистре"):
            self.app.method.assertEqual("ёйцукенгшщзхъфыв", "ёйцукенгшщзхъфыв", locator)
            self.app.method.assertEqual("апролджэячсмитьбю", "апролджэячсмитьбю", locator)
        with allure.step("Проверка ввода Русских букв в верхнем регистре"):
            self.app.method.assertEqual("ЮЁЙЦУКЕНГШЩЗХЪФЫВ", "ЮЁЙЦУКЕНГШЩЗХЪФЫВ", locator)
            self.app.method.assertEqual("АПРОЛДЖЭЯЧСМИТЬБ", "АПРОЛДЖЭЯЧСМИТЬБ", locator)
        with allure.step("Проверка ввода спецсимволов"):
            self.app.method.assertEqual("!#$%&'()*+,-./:;<=>?@[]^_`{|}~", "!#$%&'()*+,-./:;<=>?@[]^_`{|}~", locator)
        with allure.step("Проверка ввода совместных значений(буквы/цифры/спецсимволы)"):
            self.app.method.assertEqual('123  АБВABC!@#', '123  АБВABC!@#', locator)
        with allure.step("Проверка ввода пробелов"):
            self.app.method.assertEqual('   ', '   ', locator)
            self.app.method.assertEqual('123    ', '123    ', locator)
            self.app.method.assertEqual('   123', '   123', locator)
            self.app.method.assertEqual('1 2 3', '1 2 3', locator)
        with allure.step("Проверка ввода дробного числа "):
            self.app.method.assertEqual('11.11', '11.11', locator)
            self.app.method.assertEqual('000.1', '000.1', locator)
        with allure.step("Проверка ввода пустого значения"):
            self.app.method.assertEqual('', '', locator)
        with allure.step("Проверка ввода отрицательного числа"):
            self.app.method.assertEqual('-1', '-1', locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual(1, 1, locator)
            self.app.method.assertEqual(('9' * 30), ('9' * 30), locator)
            self.app.method.assertEqual(('9' * 31), ('9' * 31), locator)

    # Проверка поля Адрес
    def input_adress_domen_negativ(self, locator):
        with allure.step("Проверка ввода очень большого числа"):
            self.app.method.assertEqual(9 * 10000000000000, '90000000000000', locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual(('9' * 32), ('9' * 31), locator)

    # Проверка ввода поле 65535
    def input_number_65535(self, locator):
        with allure.step("Проверка ввода цифр"):
            for i in range(10):
                self.app.method.assertEqual(i, i, locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual(0, 0, locator)
            self.app.method.assertEqual(1, 1, locator)
            self.app.method.assertEqual(65534, 65534, locator)
            self.app.method.assertEqual(65535, 65535, locator)

    # Проверка ввода поле 99
    def input_number_99(self, locator):
        with allure.step("Проверка ввода цифр"):
            for i in range(10):
                self.app.method.assertEqual(i, i, locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual(0, 0, locator)
            self.app.method.assertEqual(1, 1, locator)
            self.app.method.assertEqual(98, 98, locator)
            self.app.method.assertEqual(99, 99, locator)

    # Проверка ввода поле 65535
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
            self.app.method.assertEqual(9 * 10000000000000, 90000, locator)
        with allure.step("Проверка ввода отрицательного числа"):
            self.app.method.assertEqual('-1', '1', locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual(999999, 99999, locator)

    # Проверка ввода поле 65535
    def input_number_99_negativ(self, locator):
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
            self.app.method.assertEqual('12     ', '12', locator)
            self.app.method.assertEqual('   12', '12', locator)
            self.app.method.assertEqual('1 2', '12', locator)
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

    # Проверка ввода поле 255
    def input_number_255(self, locator):
        with allure.step("Проверка ввода цифр"):
            for i in range(10):
                self.app.method.assertEqual(i, i, locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual(1, 1, locator)
            self.app.method.assertEqual(254, 254, locator)
            self.app.method.assertEqual(255, 255, locator)
            self.app.method.assertEqual(('1' * 3), ('1' * 3), locator)

    # Проверка ввода поле 255
    def input_number_255_negativ(self, locator):
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
            self.app.method.assertEqual('000.1', '0001', locator)
            self.app.method.assertEqual('11,11', '1111', locator)
            self.app.method.assertEqual('000,1', '0001', locator)
        with allure.step("Проверка ввода пустого значения"):
            self.app.method.assertEqual('', '', locator)
        with allure.step("Проверка ввода очень большого числа"):
            self.app.method.assertEqual(2 * 10000000000000, 200, locator)
        with allure.step("Проверка ввода отрицательного числа"):
            self.app.method.assertEqual('-1', '1', locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual(('1' * 4), ('1' * 3), locator)

    # Проверка ввода Код настройки
    def input_encryption_key_positiv(self, locator):
        with allure.step("Проверка ввода цифр"):
            for i in range(10):
                self.app.method.assertEqual(i, i, locator)
        with allure.step("Проверка ввода латинских букв в нижнем регистре"):
            self.app.method.assertEqual('abcdef', 'ab:cd:ef', locator)
        with allure.step("Проверка ввода латинских букв в врхнем регистре"):
            self.app.method.assertEqual('ABCDEF', 'AB:CD:EF', locator)
        with allure.step("Проверка ввода спецсимполов"):
            self.app.method.assertEqual(":", ":", locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual('1', '1', locator)
            self.app.method.assertEqual('1' * 31, '11:11:11:11:11:11:11:11:11:11:11:11:11:11:11:1', locator)
            self.app.method.assertEqual('1' * 32, '11:11:11:11:11:11:11:11:11:11:11:11:11:11:11:11', locator)

    # Проверка ввода Код настройки
    def input_encryption_key_negativ(self, locator):
        with allure.step("Проверка ввода латинских букв в нижнем регистре"):
            self.app.method.assertEqual('abcdefghijklmnopqrstuvwxyz', 'ab:cd:ef', locator)
        with allure.step("Проверка ввода латинских букв в врхнем регистре"):
            self.app.method.assertEqual('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'AB:CD:EF', locator)
        with allure.step("Проверка ввода Русских букв в нижнем регистре"):
            self.app.method.assertEqual("ёйцукенгшщзхъфыв", "", locator)
            self.app.method.assertEqual("апролджэячсмитьбю", "", locator)
        with allure.step("Проверка ввода Русских букв в верхнем регистре"):
            self.app.method.assertEqual("АПРОЛДЖЭЯЧСМИТЬБЮ", "", locator)
            self.app.method.assertEqual("ЁЙЦУКЕНГШЩЗХЪФЫВ", "", locator)
        with allure.step("Проверка ввода спецсимполов"):
            self.app.method.assertEqual("!#$%&'()*+,-./:;<=>?@[]^_`{|}~", ":", locator)
        with allure.step("Проверка ввода совместных значений"):
            self.app.method.assertEqual('+123  АБВABC!@#', '12:3A:BC', locator)
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
        with allure.step("Проверка ввода отрицательного числа"):
            self.app.method.assertEqual('-1', '1', locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual('1' * 33, '11:11:11:11:11:11:11:11:11:11:11:11:11:11:11:11', locator)

    # Проверка выпадающего списка Разделы все разделы
    def check_path_drop_list_all(self):
        pathList = ['Раздел № 01', 'Раздел № 02', 'Раздел № 03', 'Раздел № 04', 'Раздел № 05', 'Раздел № 06',
                    'Раздел № 07', 'Раздел № 08', 'Раздел № 09', 'Раздел № 10', 'Раздел № 11', 'Раздел № 12',
                    'Раздел № 13', 'Раздел № 14', 'Раздел № 15', 'Раздел № 16']

        self.app.method.assert_drop_wown_list_with_check_box(path_main, main_check_box_drop_down_path, pathList)

    # Проверка выпадающего списка Разделы
    def check_path_drop_list(self):
        daysList = ['Раздел № 01', 'Раздел № 02', 'Раздел № 03', 'Раздел № 04', 'Раздел № 05', 'Раздел № 06',
                    'Раздел № 07', 'Раздел № 08', 'Раздел № 09', 'Раздел № 10', 'Раздел № 11', 'Раздел № 12',
                    'Раздел № 13', 'Раздел № 14', 'Раздел № 15', 'Раздел № 16']
        self.app.method.check_dropdown_list_with_check_box(path_main, daysList)

    # Выбор из выпадающего списка Тестировать
    def Test_at_intervals_main(self, name):
        self.app.method.selectDropdownListByName(Test_at_intervals_main, name)

    # Выбор из выпадающего списка Тестировать - смс эгида
    def Test_at_intervals_main_sms_egida(self, name):
        self.app.method.selectDropdownListByName(Test_at_intervals_sms_egida_main, name)

    # Выбор из выпадающего списка Тестировать - dc09
    def Test_at_intervals_main_dc09(self, name):
        self.app.method.selectDropdownListByName(Test_at_intervals_dc_09_main, name)

    # Выбор из выпадающего списка Тестировать - смс эгида
    def Test_at_intervals_sms_egida_reserv_1(self, name):
        self.app.method.selectDropdownListByName(Test_at_intervals_sms_egida_rezerv_1, name)

    def Test_at_intervals_reserv_1_dc09(self, name):
        self.app.method.selectDropdownListByName(Test_at_intervals_dc_09_rezerv_1, name)

    # Выбор из выпадающего списка Тестировать - смс эгида
    def Test_at_intervals_sms_egida_reserv_2(self, name):
        self.app.method.selectDropdownListByName(Test_at_intervals_sms_egida_rezerv_2, name)

    def Test_at_intervals_reserv_2_dc09(self, name):
        self.app.method.selectDropdownListByName(Test_at_intervals_dc_09_rezerv_2, name)

    # Выбор из выпадающего списка Тестировать
    def Test_at_intervals_rezerv_1(self, name):
        self.app.method.selectDropdownListByName(Test_at_intervals_rezerv_1, name)

    # Выбор из выпадающего списка Тестировать
    def Test_at_intervals_rezerv_2(self, name):
        self.app.method.selectDropdownListByName(Test_at_intervals_rezerv_2, name)

    # Рвскрытие настроек направления по индексу
    def openDestination(self, number):
        self.app.method.click_element_locate(maim_settings_button + f'[{number}]')

    # Раскрытие настроек канала
    def openChanel(self, name):
        wd = self.app.wd
        if name == 'Основной':
            text = wd.find_element(By.XPATH, '//*[@id="modalSettings"]/div/div[2]/div[1]/div[3]/div[1]/div/div')
            if text.get_attribute('class') != "b-panel__header b-panel__header--open":
                self.app.method.click_element_locate(f'//*[@class="b-panel__header-text"][.="{name}"]')
        if name == 'Резерв 1':
            text = wd.find_element(By.XPATH, '//*[@id="modalSettings"]/div/div[2]/div[1]/div[3]/div[2]/div/div')
            if text.get_attribute('class') != "b-panel__header b-panel__header--open":
                self.app.method.click_element_locate(f'//*[@class="b-panel__header-text"][.="{name}"]')
        if name == 'Резерв 2':
            text = wd.find_element(By.XPATH, '//*[@id="modalSettings"]/div/div[2]/div[1]/div[3]/div[3]/div/div')
            if text.get_attribute('class') != "b-panel__header b-panel__header--open":
                self.app.method.click_element_locate(f'//*[@class="b-panel__header-text"][.="{name}"]')

    def checkChanel(self, name):
        self.app.method.click_element_locate(f'//*[@class="b-panel__header-text"][.="{name}"]')
        self.app.method.click_element_locate(f'//*[@class="b-panel__header-text"][.="{name}"]')

    # Раскрытие настроек канала
    def openSettingsTumblers(self, name):
        self.app.method.click_element_locate(f'//*[@class="b-panel__header-text"][.="{name}"]')

    # Выбор из выпадающего списка Тип управления - Основной
    def openType_main(self, name):
        self.app.method.selectDropdownListByName(type_main, name)

    # Выбор из выпадающего списка Тип управления - Резерв 1
    def openType_rezerv_1(self, name):
        self.app.method.selectDropdownListByName(type_rezerv_1, name)

    # Выбор из выпадающего списка Тип управления - Резерв 2
    def openType_rezerv_2(self, name):
        self.app.method.selectDropdownListByName(type_rezerv_2, name)

    # Включить Шифрование - Основной
    def enableEncryption_main(self):
        self.app.method.checkBox("ON", main_Encryption_click, main_Encryption_status)
        self.app.method.assertCheckBox("ON", main_Encryption_status)

    # Включить Шифрование - Основной
    def enableEncryption_rezerv_1(self):
        self.app.method.checkBox("ON", rezerv_1_Encryption_click, rezerv_1_Encryption_status)
        self.app.method.assertCheckBox("ON", rezerv_1_Encryption_status)

    # Включить Шифрование - Основной
    def enableEncryption_rezerv_2(self):
        self.app.method.checkBox("ON", rezerv_2_Encryption_click, rezerv_2_Encryption_status)
        self.app.method.assertCheckBox("ON", rezerv_2_Encryption_status)

    # Включить тестирование канала - Основной
    def enableChannelTesting_main(self):
        self.app.method.checkBox("ON", main_Enable_channel_testing_click, main_Enable_channel_testing_status)
        self.app.method.assertCheckBox("ON", main_Enable_channel_testing_status)

    # Выключить тестирование канала - Основной
    def offChannelTesting_main(self):
        self.app.method.checkBox("OFF", main_Enable_channel_testing_click, main_Enable_channel_testing_status)
        self.app.method.assertCheckBox("OFF", main_Enable_channel_testing_status)

    # Включить тестирование канала - Резерв 1
    def enableChannelTesting_rezerv_1(self):
        self.app.method.checkBox("ON", rezerv_1_Enable_channel_testing_click, rezerv_1_Enable_channel_testing_status)
        self.app.method.assertCheckBox("ON", rezerv_1_Enable_channel_testing_status)

    # Выключить тестирование канала - Резерв 1
    def offChannelTesting_rezerv_1(self):
        self.app.method.checkBox("OFF", rezerv_1_Enable_channel_testing_click, rezerv_1_Enable_channel_testing_status)
        self.app.method.assertCheckBox("OFF", rezerv_1_Enable_channel_testing_status)

    # Включить тестирование канала - Резерв 2
    def enableChannelTesting_rezerv_2(self):
        self.app.method.checkBox("ON", rezerv_2_Enable_channel_testing_click, rezerv_2_Enable_channel_testing_status)
        self.app.method.assertCheckBox("ON", rezerv_2_Enable_channel_testing_status)

    # Проверка ввода Ключ шифрования канал - ОСНОВНОЙ
    def input_encryption_key_posutiv_dc09_main(self):
        self.input_encryption_key_positiv(encryption_key_DC09_main)

    # Проверка ввода Ключ шифрования канал - ОСНОВНОЙ
    def input_encryption_key_negativ_dc09_main(self):
        self.input_encryption_key_negativ(encryption_key_DC09_main)

    # Проверка ввода Ключ шифрования канал - ОСНОВНОЙ
    def input_encryption_key_posutiv_dc09_reserv_1(self):
        self.input_encryption_key_positiv(encryption_key_DC09_reserv_1)

    # Проверка ввода Ключ шифрования канал - ОСНОВНОЙ
    def input_encryption_key_negativ_dc09_reserv_1(self):
        self.input_encryption_key_negativ(encryption_key_DC09_reserv_1)

    # Проверка ввода Ключ шифрования канал - ОСНОВНОЙ
    def input_encryption_key_posutiv_dc09_reserv_2(self):
        self.input_encryption_key_positiv(encryption_key_DC09_reserv_2)

    # Проверка ввода Ключ шифрования канал - ОСНОВНОЙ
    def input_encryption_key_negativ_dc09_reserv_2(self):
        self.input_encryption_key_negativ(encryption_key_DC09_reserv_2)

    # Проверка ввода Количество повторов канал - ОСНОВНОЙ
    def input_number_of_repetitions_posutiv_dc09_main(self):
        self.input_count_num_99_positiv(number_of_repetitions_DC09_main)

    # Проверка ввода Количество повторов канал - ОСНОВНОЙ
    def input_number_of_repetitions_negativ_dc09_main(self):
        self.input_count_num_99_negativ(number_of_repetitions_DC09_main)

    # Проверка ввода Количество повторовканал - ОСНОВНОЙ
    def input_number_of_repetitions_posutiv_dc09_reserv_1(self):
        self.input_count_num_99_positiv(number_of_repetitions_DC09_reserv_1)

    # Проверка ввода Количество повторов канал - ОСНОВНОЙ
    def input_number_of_repetitions_negativ_dc09_reserv_1(self):
        self.input_count_num_99_negativ(number_of_repetitions_DC09_reserv_1)

    # Проверка ввода Количество повторов канал - ОСНОВНОЙ
    def input_number_of_repetitions_posutiv_dc09_reserv_2(self):
        self.input_count_num_99_positiv(number_of_repetitions_DC09_reserv_2)

    # Проверка ввода Количество повторов канал - ОСНОВНОЙ
    def input_number_of_repetitions_negativ_dc09_reserv_2(self):
        self.input_count_num_99_negativ(number_of_repetitions_DC09_reserv_2)

    # Проверка ввода Таймаут подтверждения, сек канал - ОСНОВНОЙ
    def input_confirmation_timeout_posutiv_dc09_main(self):
        self.input_count_num_99_positiv(confirmation_timeout_DC09_main)

    # Проверка ввода Таймаут подтверждения, сек канал - ОСНОВНОЙ
    def input_confirmation_timeout_negativ_dc09_main(self):
        self.input_count_num_99_negativ(confirmation_timeout_DC09_main)

    # Проверка ввода Таймаут подтверждения, сек канал - ОСНОВНОЙ
    def input_confirmation_timeout_posutiv_dc09_reserv_1(self):
        self.input_count_num_99_positiv(confirmation_timeout_DC09_reserv_1)

    # Проверка ввода Таймаут подтверждения, сек канал - ОСНОВНОЙ
    def input_confirmation_timeout_negativ_dc09_reserv_1(self):
        self.input_count_num_99_negativ(confirmation_timeout_DC09_reserv_1)

    # Проверка ввода Таймаут подтверждения, сек канал - ОСНОВНОЙ
    def input_confirmation_timeout_posutiv_dc09_reserv_2(self):
        self.input_count_num_99_positiv(confirmation_timeout_DC09_reserv_2)

    # Проверка ввода Таймаут подтверждения, сек канал - ОСНОВНОЙ
    def input_confirmation_timeout_negativ_dc09_reserv_2(self):
        self.input_count_num_99_negativ(confirmation_timeout_DC09_reserv_2)

    # Проверка ввода Порт канал - ОСНОВНОЙ
    def input_port_posutiv_dc09_main(self):
        self.input_number_65535(port_DC09_main)

    # Проверка ввода Порт канал - ОСНОВНОЙ
    def input_port_negativ_dc09_main(self):
        self.input_number_65535_negativ(port_DC09_main)

    # Проверка ввода Порт канал - ОСНОВНОЙ
    def input_port_posutiv_dc09_reserv_1(self):
        self.input_number_65535(port_DC09_reserv_1)

    # Проверка ввода Порт канал - ОСНОВНОЙ
    def input_port_negativ_dc09_reserv_1(self):
        self.input_number_65535_negativ(port_DC09_reserv_1)

    # Проверка ввода Порт канал - ОСНОВНОЙ
    def input_port_posutiv_dc09_reserv_2(self):
        self.input_number_65535(port_DC09_reserv_2)

    # Проверка ввода Порт канал - ОСНОВНОЙ
    def input_port_negativ_dc09_reserv_2(self):
        self.input_number_65535_negativ(port_DC09_reserv_2)

    # Проверка ввода Адрес канал - ОСНОВНОЙ
    def input_address_posutiv_dc09_main(self):
        self.input_adress_domen_positiv(address_DC09_main)

    def input_address_negativ_dc09_main(self):
        self.input_adress_domen_negativ(address_DC09_main)

    # Проверка ввода Адрес канал - ОСНОВНОЙ
    def input_address_posutiv_dc09_reserv_1(self):
        self.input_adress_domen_positiv(address_DC09_reserv_1)

    def input_address_negativ_dc09_reserv_1(self):
        self.input_adress_domen_negativ(address_DC09_reserv_1)

    # Проверка ввода Адрес канал - ОСНОВНОЙ
    def input_address_posutiv_dc09_reserv_2(self):
        self.input_adress_domen_positiv(address_DC09_reserv_2)

    def input_address_negativ_dc09_reserv_2(self):
        self.input_adress_domen_negativ(address_DC09_reserv_2)

    # Проверка ввода код телефона канал - ОСНОВНОЙ
    def input_cod_posutiv_sms_user_main(self):
        self.input_cod_posutiv(TEL_COD_main)

    # Проверка ввода код телефона канал - ОСНОВНОЙ
    def input_cod_negativ_sms_user_main(self):
        self.input_cod_negativ(TEL_COD_main)

    # Проверка ввода код телефона канал - РЕЗЕРВ 1
    def input_cod_posutiv_sms_user_rezerv_1(self):
        self.input_cod_posutiv(TEL_COD_rezerv_1)

    # Проверка ввода код телефона канал - РЕЗЕРВ 1
    def input_cod_negativ_sms_user_rezerv_1(self):
        self.input_cod_negativ(TEL_COD_rezerv_1)

    # Проверка ввода код телефона канал - РЕЗЕРВ 2
    def input_cod_posutiv_sms_user_rezerv_2(self):
        self.input_cod_posutiv(TEL_COD_rezerv_2)

    # Проверка ввода код телефона канал - РЕЗЕРВ 2
    def input_cod_negativ_sms_user_rezerv_2(self):
        self.input_cod_negativ(TEL_COD_rezerv_2)

    # Проверка ввода Количество повторов канал - ОСНОВНОЙ
    def input_count_reset_posutiv_main(self):
        time.sleep(0.5)
        self.input_number_65535_negativ(TEL_NUM_main)

    # Проверка ввода номера Количество повторов - ОСНОВНОЙ
    def input_count_reset_positiv_call_main(self):
        time.sleep(0.3)
        self.input_number_99(count_reset_main)

    # Проверка ввода номера Количество повторов - ОСНОВНОЙ
    def input_count_reset_negativ_call_main(self):
        time.sleep(0.3)
        self.input_number_99_negativ(count_reset_main)

    # Проверка ввода номера Количество повторов - ОСНОВНОЙ
    def input_count_reset_positiv_call_reserv_1(self):
        time.sleep(0.3)
        self.input_number_99(count_reset_rezerv_1)

    # Проверка ввода номера Количество повторов - ОСНОВНОЙ
    def input_count_reset_negativ_call_reserv_1(self):
        time.sleep(0.3)
        self.input_number_99_negativ(count_reset_rezerv_1)

    # Проверка ввода номера Количество повторов - ОСНОВНОЙ
    def input_count_reset_positiv_call_reserv_2(self):
        time.sleep(0.3)
        self.input_number_99(count_reset_rezerv_2)

    # Проверка ввода номера Количество повторов - ОСНОВНОЙ
    def input_count_reset_negativ_call_reserv_2(self):
        time.sleep(0.3)
        self.input_number_99_negativ(count_reset_rezerv_2)

    # Проверка ввода номера телефона канал - ОСНОВНОЙ
    def input_tel_number_posutiv_sms_user_main(self):
        time.sleep(0.5)
        self.input_phone_number_positiv(TEL_NUM_main)

    # Проверка ввода номера телефона канал - ОСНОВНОЙ
    def input_tel_number_negativ_sms_user_main(self):
        time.sleep(0.3)
        self.input_phone_number_negativ(TEL_NUM_main)

    # Проверка ввода номера телефона канал - РЕЗЕРВ 1
    def input_tel_number_posutiv_sms_user_rezerv_1(self):
        time.sleep(0.5)
        self.input_phone_number_positiv(TEL_NUM_rezerv_1)

    # Проверка ввода номера телефона канал - РЕЗЕРВ 1
    def input_tel_number_negativ_sms_user_rezerv_1(self):
        time.sleep(0.3)
        self.input_phone_number_negativ(TEL_NUM_rezerv_1)

    # Проверка ввода номера телефона канал - РЕЗЕРВ 2
    def input_tel_number_posutiv_sms_user_rezerv_2(self):
        time.sleep(0.5)
        self.input_phone_number_positiv(TEL_NUM_rezerv_2)

    # Проверка ввода номера телефона канал - РЕЗЕРВ 2
    def input_tel_number_negativ_sms_user_rezerv_2(self):
        time.sleep(0.3)
        self.input_phone_number_negativ(TEL_NUM_rezerv_2)

    # Проверка ввода Таймаут при ошибке канал - ОСНОВНОЙ
    def input_timeout_error_posutiv_sms_user_main(self):
        time.sleep(0.5)
        self.input_time_positiv(Timeout_on_error_main)

    # Проверка ввода Таймаут при ошибке канал - ОСНОВНОЙ
    def input_timeout_error_negativ_sms_user_main(self):
        time.sleep(0.5)
        self.input_time_negativ(Timeout_on_error_main)

    # Проверка ввода Таймаут при ошибке канал - РЕЗЕРВ 1
    def input_timeout_error_posutiv_sms_user_rezerv_1(self):
        time.sleep(0.5)
        self.input_time_positiv(Timeout_on_error_rezerv_1)

    # Проверка ввода Таймаут при ошибке канал - РЕЗЕРВ 1
    def input_timeout_error_negativ_sms_user_rezerv_1(self):
        time.sleep(0.5)
        self.input_time_negativ(Timeout_on_error_rezerv_1)

    # Проверка ввода Таймаут при ошибке канал - РЕЗЕРВ 2
    def input_timeout_error_posutiv_sms_user_rezerv_2(self):
        time.sleep(0.5)
        self.input_time_positiv(Timeout_on_error_rezerv_2)

    # Проверка ввода Таймаут при ошибке канал - РЕЗЕРВ 2
    def input_timeout_error_negativ_sms_user_rezerv_2(self):
        time.sleep(0.5)
        self.input_time_negativ(Timeout_on_error_rezerv_2)

    # Проверка ввода Интервал тестирования - ОСНОВНОЙ
    def input_test_interval_posutiv_sms_user_main(self):
        time.sleep(0.5)
        self.input_time_positiv(Test_interval_main)

    # Проверка ввода Интервал тестирования - ОСНОВНОЙ
    def input_test_interval_posutiv_sms_user_rezerv_1(self):
        time.sleep(0.5)
        self.input_time_positiv(Test_interval_rezerv_1)

    # Проверка ввода Интервал тестирования - ОСНОВНОЙ
    def input_test_interval_posutiv_sms_user_rezerv_2(self):
        time.sleep(0.5)
        self.input_time_positiv(Test_interval_rezerv_2)

    # Включение тумблеров события разделов
    def tumblers_event_path_on(self):
        self.app.method.checkBox("OFF", Take_all_event_path_click, Take_all_event_path_status)
        self.app.method.assertCheckBox("OFF", Take_all_event_path_status)
        self.app.method.checkBox("ON", No_take_click, No_takel_status)
        self.app.method.assertCheckBox("ON", No_takel_status)
        self.app.method.checkBox("ON", Outfit_mark_click, Outfit_mark_status)
        self.app.method.assertCheckBox("ON", Outfit_mark_status)
        self.app.method.checkBox("ON", Fire_click, Fire_status)
        self.app.method.assertCheckBox("ON", Fire_status)
        self.app.method.checkBox("ON", Fire_by_manual_call_point_click, Fire_by_manual_call_point_status)
        self.app.method.assertCheckBox("ON", Fire_by_manual_call_point_status)
        self.app.method.checkBox("ON", No_Fire_click, No_Fire_status)
        self.app.method.assertCheckBox("ON", No_Fire_status)
        self.app.method.checkBox("ON", Forcing_Partition_click, Forcing_Partition_status)
        self.app.method.assertCheckBox("ON", Forcing_Partition_status)
        self.app.method.checkBox("ON", Water_leak_click, Water_leak_status)
        self.app.method.assertCheckBox("ON", Water_leak_status)
        self.app.method.checkBox("ON", Section_taken_click, Section_taken_status)
        self.app.method.assertCheckBox("ON", Section_taken_status)
        self.app.method.checkBox("ON", Section_taken_off_click, Section_taken_off_status)
        self.app.method.assertCheckBox("ON", Section_taken_off_status)
        self.app.method.checkBox("ON", Silent_alarm_click, Silent_alarm_status)
        self.app.method.assertCheckBox("ON", Silent_alarm_status)
        self.app.method.checkBox("ON", Alarm_click, Alarm_status)
        self.app.method.assertCheckBox("ON", Alarm_status)
        self.app.method.checkBox("ON", Alarm_enter_click, Alarm_enter_status)
        self.app.method.assertCheckBox("ON", Alarm_enter_status)

    # Выключение тумблеров события разделов
    def tumblers_event_path_off(self):
        self.app.method.checkBox("OFF", Take_all_event_path_click, Take_all_event_path_status)
        self.app.method.assertCheckBox("OFF", Take_all_event_path_status)
        self.app.method.checkBox("OFF", No_take_click, No_takel_status)
        self.app.method.assertCheckBox("OFF", No_takel_status)
        self.app.method.checkBox("OFF", Outfit_mark_click, Outfit_mark_status)
        self.app.method.assertCheckBox("OFF", Outfit_mark_status)
        self.app.method.checkBox("OFF", Fire_click, Fire_status)
        self.app.method.assertCheckBox("OFF", Fire_status)
        self.app.method.checkBox("OFF", Fire_by_manual_call_point_click, Fire_by_manual_call_point_status)
        self.app.method.assertCheckBox("OFF", Fire_by_manual_call_point_status)
        self.app.method.checkBox("OFF", No_Fire_click, No_Fire_status)
        self.app.method.assertCheckBox("OFF", No_Fire_status)
        self.app.method.checkBox("OFF", Forcing_Partition_click, Forcing_Partition_status)
        self.app.method.assertCheckBox("OFF", Forcing_Partition_status)
        self.app.method.checkBox("OFF", Water_leak_click, Water_leak_status)
        self.app.method.assertCheckBox("OFF", Water_leak_status)
        self.app.method.checkBox("OFF", Section_taken_click, Section_taken_status)
        self.app.method.assertCheckBox("OFF", Section_taken_status)
        self.app.method.checkBox("OFF", Section_taken_off_click, Section_taken_off_status)
        self.app.method.assertCheckBox("OFF", Section_taken_off_status)
        self.app.method.checkBox("OFF", Silent_alarm_click, Silent_alarm_status)
        self.app.method.assertCheckBox("OFF", Silent_alarm_status)
        self.app.method.checkBox("OFF", Alarm_click, Alarm_status)
        self.app.method.assertCheckBox("OFF", Alarm_status)
        self.app.method.checkBox("OFF", Alarm_enter_click, Alarm_enter_status)
        self.app.method.assertCheckBox("OFF", Alarm_enter_status)

    # Частичное включение/выключение тумблеров события разделов
    def tumblers_event_path_some(self):
        self.app.method.checkBox("OFF", Take_all_event_path_click, Take_all_event_path_status)
        self.app.method.assertCheckBox("OFF", Take_all_event_path_status)
        self.app.method.checkBox("OFF", No_take_click, No_takel_status)
        self.app.method.assertCheckBox("OFF", No_takel_status)
        self.app.method.checkBox("ON", Outfit_mark_click, Outfit_mark_status)
        self.app.method.assertCheckBox("ON", Outfit_mark_status)
        self.app.method.checkBox("OFF", Fire_click, Fire_status)
        self.app.method.assertCheckBox("OFF", Fire_status)
        self.app.method.checkBox("ON", Fire_by_manual_call_point_click, Fire_by_manual_call_point_status)
        self.app.method.assertCheckBox("ON", Fire_by_manual_call_point_status)
        self.app.method.checkBox("OFF", No_Fire_click, No_Fire_status)
        self.app.method.assertCheckBox("OFF", No_Fire_status)
        self.app.method.checkBox("ON", Forcing_Partition_click, Forcing_Partition_status)
        self.app.method.assertCheckBox("ON", Forcing_Partition_status)
        self.app.method.checkBox("OFF", Water_leak_click, Water_leak_status)
        self.app.method.assertCheckBox("OFF", Water_leak_status)
        self.app.method.checkBox("ON", Section_taken_click, Section_taken_status)
        self.app.method.assertCheckBox("ON", Section_taken_status)
        self.app.method.checkBox("OFF", Section_taken_off_click, Section_taken_off_status)
        self.app.method.assertCheckBox("OFF", Section_taken_off_status)
        self.app.method.checkBox("ON", Silent_alarm_click, Silent_alarm_status)
        self.app.method.assertCheckBox("ON", Silent_alarm_status)
        self.app.method.checkBox("OFF", Alarm_click, Alarm_status)
        self.app.method.assertCheckBox("OFF", Alarm_status)
        self.app.method.checkBox("ON", Alarm_enter_click, Alarm_enter_status)
        self.app.method.assertCheckBox("ON", Alarm_enter_status)
        self.app.method.checkBox("OFF", Take_all_event_path_click, Take_all_event_path_status)
        self.app.method.assertCheckBox("OFF", Take_all_event_path_status)
        self.app.method.checkBox("ON", No_take_click, No_takel_status)
        self.app.method.assertCheckBox("ON", No_takel_status)
        self.app.method.checkBox("OFF", Outfit_mark_click, Outfit_mark_status)
        self.app.method.assertCheckBox("OFF", Outfit_mark_status)
        self.app.method.checkBox("ON", Fire_click, Fire_status)
        self.app.method.assertCheckBox("ON", Fire_status)
        self.app.method.checkBox("OFF", Fire_by_manual_call_point_click, Fire_by_manual_call_point_status)
        self.app.method.assertCheckBox("OFF", Fire_by_manual_call_point_status)
        self.app.method.checkBox("ON", No_Fire_click, No_Fire_status)
        self.app.method.assertCheckBox("ON", No_Fire_status)
        self.app.method.checkBox("OFF", Forcing_Partition_click, Forcing_Partition_status)
        self.app.method.assertCheckBox("OFF", Forcing_Partition_status)
        self.app.method.checkBox("ON", Water_leak_click, Water_leak_status)
        self.app.method.assertCheckBox("ON", Water_leak_status)
        self.app.method.checkBox("OFF", Section_taken_click, Section_taken_status)
        self.app.method.assertCheckBox("OFF", Section_taken_status)
        self.app.method.checkBox("ON", Section_taken_off_click, Section_taken_off_status)
        self.app.method.assertCheckBox("ON", Section_taken_off_status)
        self.app.method.checkBox("OFF", Silent_alarm_click, Silent_alarm_status)
        self.app.method.assertCheckBox("OFF", Silent_alarm_status)
        self.app.method.checkBox("ON", Alarm_click, Alarm_status)
        self.app.method.assertCheckBox("ON", Alarm_status)
        self.app.method.checkBox("OFF", Alarm_enter_click, Alarm_enter_status)
        self.app.method.assertCheckBox("OFF", Alarm_enter_status)

    # Включение тумблеров Питание прибора
    def tumblers_instrument_power_supply_on(self):
        self.app.method.checkBox("OFF", Take_all_power_device_click, Take_all_power_device_status)
        self.app.method.assertCheckBox("OFF", Take_all_power_device_status)
        self.app.method.checkBox("ON", Battery_is_OK_click, Battery_is_OK_status)
        self.app.method.assertCheckBox("ON", Battery_is_OK_status)
        self.app.method.checkBox("ON", The_battery_is_charging_click, The_battery_is_charging_status)
        self.app.method.assertCheckBox("ON", The_battery_is_charging_status)
        self.app.method.checkBox("ON", Battery_is_charged_click, Battery_is_charged_status)
        self.app.method.assertCheckBox("ON", Battery_is_charged_status)
        self.app.method.checkBox("ON", Battery_not_connected_or_connected_incorrectly_click,
                                 Battery_not_connected_or_connected_incorrectly_status)
        self.app.method.assertCheckBox("ON", Battery_not_connected_or_connected_incorrectly_status)
        self.app.method.checkBox("ON", Battery_low_click, Battery_low_status)
        self.app.method.assertCheckBox("ON", Battery_low_status)
        self.app.method.checkBox("ON", High_internal_battery_resistance_click, High_internal_battery_resistance_status)
        self.app.method.assertCheckBox("ON", High_internal_battery_resistance_status)
        self.app.method.checkBox("ON", Mains_power_is_OK_click, Mains_power_is_OK_status)
        self.app.method.assertCheckBox("ON", Mains_power_is_OK_status)
        self.app.method.checkBox("ON", Mains_power_off_click, Mains_power_off_status)
        self.app.method.assertCheckBox("ON", Mains_power_off_status)

    # Выключение тумблеров Питание прибора
    def tumblers_instrument_power_supply_off(self):
        self.app.method.checkBox("OFF", Take_all_power_device_click, Take_all_power_device_status)
        self.app.method.assertCheckBox("OFF", Take_all_power_device_status)
        self.app.method.checkBox("OFF", Battery_is_OK_click, Battery_is_OK_status)
        self.app.method.assertCheckBox("OFF", Battery_is_OK_status)
        self.app.method.checkBox("OFF", The_battery_is_charging_click, The_battery_is_charging_status)
        self.app.method.assertCheckBox("OFF", The_battery_is_charging_status)
        self.app.method.checkBox("OFF", Battery_is_charged_click, Battery_is_charged_status)
        self.app.method.assertCheckBox("OFF", Battery_is_charged_status)
        self.app.method.checkBox("OFF", Battery_not_connected_or_connected_incorrectly_click,
                                 Battery_not_connected_or_connected_incorrectly_status)
        self.app.method.assertCheckBox("OFF", Battery_not_connected_or_connected_incorrectly_status)
        self.app.method.checkBox("OFF", Battery_low_click, Battery_low_status)
        self.app.method.assertCheckBox("OFF", Battery_low_status)
        self.app.method.checkBox("OFF", High_internal_battery_resistance_click, High_internal_battery_resistance_status)
        self.app.method.assertCheckBox("OFF", High_internal_battery_resistance_status)
        self.app.method.checkBox("OFF", Mains_power_is_OK_click, Mains_power_is_OK_status)
        self.app.method.assertCheckBox("OFF", Mains_power_is_OK_status)
        self.app.method.checkBox("OFF", Mains_power_off_click, Mains_power_off_status)
        self.app.method.assertCheckBox("OFF", Mains_power_off_status)

    # Частичное включение/выключение тумблеров Питание прибора
    def tumblers_instrument_power_supply_some(self):
        self.app.method.checkBox("OFF", Take_all_power_device_click, Take_all_power_device_status)
        self.app.method.assertCheckBox("OFF", Take_all_power_device_status)
        self.app.method.checkBox("OFF", Battery_is_OK_click, Battery_is_OK_status)
        self.app.method.assertCheckBox("OFF", Battery_is_OK_status)
        self.app.method.checkBox("ON", The_battery_is_charging_click, The_battery_is_charging_status)
        self.app.method.assertCheckBox("ON", The_battery_is_charging_status)
        self.app.method.checkBox("OFF", Battery_is_charged_click, Battery_is_charged_status)
        self.app.method.assertCheckBox("OFF", Battery_is_charged_status)
        self.app.method.checkBox("ON", Battery_not_connected_or_connected_incorrectly_click,
                                 Battery_not_connected_or_connected_incorrectly_status)
        self.app.method.assertCheckBox("ON", Battery_not_connected_or_connected_incorrectly_status)
        self.app.method.checkBox("OFF", Battery_low_click, Battery_low_status)
        self.app.method.assertCheckBox("OFF", Battery_low_status)
        self.app.method.checkBox("ON", High_internal_battery_resistance_click, High_internal_battery_resistance_status)
        self.app.method.assertCheckBox("ON", High_internal_battery_resistance_status)
        self.app.method.checkBox("OFF", Mains_power_is_OK_click, Mains_power_is_OK_status)
        self.app.method.assertCheckBox("OFF", Mains_power_is_OK_status)
        self.app.method.checkBox("ON", Mains_power_off_click, Mains_power_off_status)
        self.app.method.assertCheckBox("ON", Mains_power_off_status)

        self.app.method.checkBox("OFF", Take_all_power_device_click, Take_all_power_device_status)
        self.app.method.assertCheckBox("OFF", Take_all_power_device_status)
        self.app.method.checkBox("ON", Battery_is_OK_click, Battery_is_OK_status)
        self.app.method.assertCheckBox("ON", Battery_is_OK_status)
        self.app.method.checkBox("OFF", The_battery_is_charging_click, The_battery_is_charging_status)
        self.app.method.assertCheckBox("OFF", The_battery_is_charging_status)
        self.app.method.checkBox("ON", Battery_is_charged_click, Battery_is_charged_status)
        self.app.method.assertCheckBox("ON", Battery_is_charged_status)
        self.app.method.checkBox("OFF", Battery_not_connected_or_connected_incorrectly_click,
                                 Battery_not_connected_or_connected_incorrectly_status)
        self.app.method.assertCheckBox("OFF", Battery_not_connected_or_connected_incorrectly_status)
        self.app.method.checkBox("ON", Battery_low_click, Battery_low_status)
        self.app.method.assertCheckBox("ON", Battery_low_status)
        self.app.method.checkBox("OFF", High_internal_battery_resistance_click, High_internal_battery_resistance_status)
        self.app.method.assertCheckBox("OFF", High_internal_battery_resistance_status)
        self.app.method.checkBox("ON", Mains_power_is_OK_click, Mains_power_is_OK_status)
        self.app.method.assertCheckBox("ON", Mains_power_is_OK_status)
        self.app.method.checkBox("OFF", Mains_power_off_click, Mains_power_off_status)
        self.app.method.assertCheckBox("OFF", Mains_power_off_status)

    # Включение тумблеров События зон
    def tumblers_zone_events_on(self):
        self.app.method.checkBox("OFF", zone_events_device_click, zone_events_device_status)
        self.app.method.assertCheckBox("OFF", zone_events_device_status)
        self.app.method.checkBox("ON", Battery_OK_zone_events_device_click, Battery_OK_zone_events_device_status)
        self.app.method.assertCheckBox("ON", Battery_OK_zone_events_device_status)
        self.app.method.checkBox("ON", ready_click, ready_status)
        self.app.method.assertCheckBox("ON", ready_status)
        self.app.method.checkBox("ON", Case_closed_click, Case_closed_status)
        self.app.method.assertCheckBox("ON", Case_closed_status)
        self.app.method.checkBox("ON", Case_open_click, Case_open_status)
        self.app.method.assertCheckBox("ON", Case_open_status)
        self.app.method.checkBox("ON", Low_battery_zone_events_click, Low_battery_zone_events_status)
        self.app.method.assertCheckBox("ON", Low_battery_zone_events_status)
        self.app.method.checkBox("ON", Backup_battery_error_zone_events_click, Backup_battery_error_zone_events_status)
        self.app.method.assertCheckBox("ON", Backup_battery_error_zone_events_status)
        self.app.method.checkBox("ON", Device_error_zone_events_click, Device_error_zone_events_status)
        self.app.method.assertCheckBox("ON", Device_error_zone_events_status)
        self.app.method.checkBox("ON", Sensor_reset_zone_events_click, Sensor_reset_zone_events_status)
        self.app.method.assertCheckBox("ON", Sensor_reset_zone_events_status)
        self.app.method.checkBox("ON", Lost_zone_events_click, Lost_zone_events_status)
        self.app.method.assertCheckBox("ON", Lost_zone_events_status)
        self.app.method.checkBox("ON", Check_connection_zone_events_click, Check_connection_zone_events_status)
        self.app.method.assertCheckBox("ON", Check_connection_zone_events_status)
        self.app.method.checkBox("ON", Backup_battery_is_OK_zone_events_click, Backup_battery_is_OK_zone_events_status)
        self.app.method.assertCheckBox("ON", Backup_battery_is_OK_zone_events_status)
        self.app.method.checkBox("ON", Sabotage_zone_events_click, Sabotage_zone_events_status)
        self.app.method.assertCheckBox("ON", Sabotage_zone_events_status)
        self.app.method.checkBox("ON", Communication_restored_zone_events_click,
                                 Communication_restored_zone_events_status)
        self.app.method.assertCheckBox("ON", Communication_restored_zone_events_status)
        self.app.method.checkBox("ON", Humidity_event_zone_events_click, Humidity_event_zone_events_status)
        self.app.method.assertCheckBox("ON", Humidity_event_zone_events_status)
        self.app.method.checkBox("ON", CO_sensor_event_zone_events_click, CO_sensor_event_zone_events_status)
        self.app.method.assertCheckBox("ON", CO_sensor_event_zone_events_status)
        self.app.method.checkBox("ON", Temperature_event_zone_events_click, Temperature_event_zone_events_status)
        self.app.method.assertCheckBox("ON", Temperature_event_zone_events_status)
        self.app.method.checkBox("ON", Sensor_activation_Bell_mode_zone_events_click,
                                 Sensor_activation_Bell_mode_zone_events_status)
        self.app.method.assertCheckBox("ON", Sensor_activation_Bell_mode_zone_events_status)
        self.app.method.checkBox("ON", SS_is_normal_zone_events_click, SS_is_normal_zone_events_status)
        self.app.method.assertCheckBox("ON", SS_is_normal_zone_events_status)
        self.app.method.checkBox("ON", AL_is_closed_zone_events_click, AL_is_closed_zone_events_status)
        self.app.method.assertCheckBox("ON", AL_is_closed_zone_events_status)
        self.app.method.checkBox("ON", AL_interrupted_zone_events_click, AL_interrupted_zone_events_status)
        self.app.method.assertCheckBox("ON", AL_interrupted_zone_events_status)

    # Выключение тумблеров События зон
    def tumblers_zone_events_off(self):
        self.app.method.checkBox("OFF", zone_events_device_click, zone_events_device_status)
        self.app.method.assertCheckBox("OFF", zone_events_device_status)
        self.app.method.checkBox("OFF", Battery_OK_zone_events_device_click, Battery_OK_zone_events_device_status)
        self.app.method.assertCheckBox("OFF", Battery_OK_zone_events_device_status)
        self.app.method.checkBox("OFF", ready_click, ready_status)
        self.app.method.assertCheckBox("OFF", ready_status)
        self.app.method.checkBox("OFF", Case_closed_click, Case_closed_status)
        self.app.method.assertCheckBox("OFF", Case_closed_status)
        self.app.method.checkBox("OFF", Case_open_click, Case_open_status)
        self.app.method.assertCheckBox("OFF", Case_open_status)
        self.app.method.checkBox("OFF", Low_battery_zone_events_click, Low_battery_zone_events_status)
        self.app.method.assertCheckBox("OFF", Low_battery_zone_events_status)
        self.app.method.checkBox("OFF", Backup_battery_error_zone_events_click, Backup_battery_error_zone_events_status)
        self.app.method.assertCheckBox("OFF", Backup_battery_error_zone_events_status)
        self.app.method.checkBox("OFF", Device_error_zone_events_click, Device_error_zone_events_status)
        self.app.method.assertCheckBox("OFF", Device_error_zone_events_status)
        self.app.method.checkBox("OFF", Sensor_reset_zone_events_click, Sensor_reset_zone_events_status)
        self.app.method.assertCheckBox("OFF", Sensor_reset_zone_events_status)
        self.app.method.checkBox("OFF", Lost_zone_events_click, Lost_zone_events_status)
        self.app.method.assertCheckBox("OFF", Lost_zone_events_status)
        self.app.method.checkBox("OFF", Check_connection_zone_events_click, Check_connection_zone_events_status)
        self.app.method.assertCheckBox("OFF", Check_connection_zone_events_status)
        self.app.method.checkBox("OFF", Backup_battery_is_OK_zone_events_click, Backup_battery_is_OK_zone_events_status)
        self.app.method.assertCheckBox("OFF", Backup_battery_is_OK_zone_events_status)
        self.app.method.checkBox("OFF", Sabotage_zone_events_click, Sabotage_zone_events_status)
        self.app.method.assertCheckBox("OFF", Sabotage_zone_events_status)
        self.app.method.checkBox("OFF", Communication_restored_zone_events_click,
                                 Communication_restored_zone_events_status)
        self.app.method.assertCheckBox("OFF", Communication_restored_zone_events_status)
        self.app.method.checkBox("OFF", Humidity_event_zone_events_click, Humidity_event_zone_events_status)
        self.app.method.assertCheckBox("OFF", Humidity_event_zone_events_status)
        self.app.method.checkBox("OFF", CO_sensor_event_zone_events_click, CO_sensor_event_zone_events_status)
        self.app.method.assertCheckBox("OFF", CO_sensor_event_zone_events_status)
        self.app.method.checkBox("OFF", Temperature_event_zone_events_click, Temperature_event_zone_events_status)
        self.app.method.assertCheckBox("OFF", Temperature_event_zone_events_status)
        self.app.method.checkBox("OFF", Sensor_activation_Bell_mode_zone_events_click,
                                 Sensor_activation_Bell_mode_zone_events_status)
        self.app.method.assertCheckBox("OFF", Sensor_activation_Bell_mode_zone_events_status)
        self.app.method.checkBox("OFF", SS_is_normal_zone_events_click, SS_is_normal_zone_events_status)
        self.app.method.assertCheckBox("OFF", SS_is_normal_zone_events_status)
        self.app.method.checkBox("OFF", AL_is_closed_zone_events_click, AL_is_closed_zone_events_status)
        self.app.method.assertCheckBox("OFF", AL_is_closed_zone_events_status)
        self.app.method.checkBox("OFF", AL_interrupted_zone_events_click, AL_interrupted_zone_events_status)
        self.app.method.assertCheckBox("OFF", AL_interrupted_zone_events_status)

    # Частичное включение/выключение тумблеров События зон
    def tumblers_zone_events_some(self):
        self.app.method.checkBox("OFF", zone_events_device_click, zone_events_device_status)
        self.app.method.assertCheckBox("OFF", zone_events_device_status)
        self.app.method.checkBox("ON", Battery_OK_zone_events_device_click, Battery_OK_zone_events_device_status)
        self.app.method.assertCheckBox("ON", Battery_OK_zone_events_device_status)
        self.app.method.checkBox("OFF", ready_click, ready_status)
        self.app.method.assertCheckBox("OFF", ready_status)
        self.app.method.checkBox("ON", Case_closed_click, Case_closed_status)
        self.app.method.assertCheckBox("ON", Case_closed_status)
        self.app.method.checkBox("OFF", Case_open_click, Case_open_status)
        self.app.method.assertCheckBox("OFF", Case_open_status)
        self.app.method.checkBox("ON", Low_battery_zone_events_click, Low_battery_zone_events_status)
        self.app.method.assertCheckBox("ON", Low_battery_zone_events_status)
        self.app.method.checkBox("ON", Backup_battery_error_zone_events_click, Backup_battery_error_zone_events_status)
        self.app.method.assertCheckBox("ON", Backup_battery_error_zone_events_status)
        self.app.method.checkBox("OFF", Device_error_zone_events_click, Device_error_zone_events_status)
        self.app.method.assertCheckBox("OFF", Device_error_zone_events_status)
        self.app.method.checkBox("ON", Sensor_reset_zone_events_click, Sensor_reset_zone_events_status)
        self.app.method.assertCheckBox("ON", Sensor_reset_zone_events_status)
        self.app.method.checkBox("OFF", Lost_zone_events_click, Lost_zone_events_status)
        self.app.method.assertCheckBox("OFF", Lost_zone_events_status)
        self.app.method.checkBox("ON", Check_connection_zone_events_click, Check_connection_zone_events_status)
        self.app.method.assertCheckBox("ON", Check_connection_zone_events_status)
        self.app.method.checkBox("OFF", Backup_battery_is_OK_zone_events_click, Backup_battery_is_OK_zone_events_status)
        self.app.method.assertCheckBox("OFF", Backup_battery_is_OK_zone_events_status)
        self.app.method.checkBox("ON", Sabotage_zone_events_click, Sabotage_zone_events_status)
        self.app.method.assertCheckBox("ON", Sabotage_zone_events_status)
        self.app.method.checkBox("OFF", Communication_restored_zone_events_click,
                                 Communication_restored_zone_events_status)
        self.app.method.assertCheckBox("OFF", Communication_restored_zone_events_status)
        self.app.method.checkBox("ON", Humidity_event_zone_events_click, Humidity_event_zone_events_status)
        self.app.method.assertCheckBox("ON", Humidity_event_zone_events_status)
        self.app.method.checkBox("OFF", CO_sensor_event_zone_events_click, CO_sensor_event_zone_events_status)
        self.app.method.assertCheckBox("OFF", CO_sensor_event_zone_events_status)
        self.app.method.checkBox("ON", Temperature_event_zone_events_click, Temperature_event_zone_events_status)
        self.app.method.assertCheckBox("ON", Temperature_event_zone_events_status)
        self.app.method.checkBox("OFF", Sensor_activation_Bell_mode_zone_events_click,
                                 Sensor_activation_Bell_mode_zone_events_status)
        self.app.method.assertCheckBox("OFF", Sensor_activation_Bell_mode_zone_events_status)
        self.app.method.checkBox("ON", SS_is_normal_zone_events_click, SS_is_normal_zone_events_status)
        self.app.method.assertCheckBox("ON", SS_is_normal_zone_events_status)
        self.app.method.checkBox("ON", AL_is_closed_zone_events_click, AL_is_closed_zone_events_status)
        self.app.method.assertCheckBox("ON", AL_is_closed_zone_events_status)
        self.app.method.checkBox("ON", AL_interrupted_zone_events_click, AL_interrupted_zone_events_status)
        self.app.method.assertCheckBox("ON", AL_interrupted_zone_events_status)

        self.app.method.checkBox("OFF", zone_events_device_click, zone_events_device_status)
        self.app.method.assertCheckBox("OFF", zone_events_device_status)
        self.app.method.checkBox("OFF", Battery_OK_zone_events_device_click, Battery_OK_zone_events_device_status)
        self.app.method.assertCheckBox("OFF", Battery_OK_zone_events_device_status)
        self.app.method.checkBox("ON", ready_click, ready_status)
        self.app.method.assertCheckBox("ON", ready_status)
        self.app.method.checkBox("OFF", Case_closed_click, Case_closed_status)
        self.app.method.assertCheckBox("OFF", Case_closed_status)
        self.app.method.checkBox("ON", Case_open_click, Case_open_status)
        self.app.method.assertCheckBox("ON", Case_open_status)
        self.app.method.checkBox("OFF", Low_battery_zone_events_click, Low_battery_zone_events_status)
        self.app.method.assertCheckBox("OFF", Low_battery_zone_events_status)
        self.app.method.checkBox("OFF", Backup_battery_error_zone_events_click, Backup_battery_error_zone_events_status)
        self.app.method.assertCheckBox("OFF", Backup_battery_error_zone_events_status)
        self.app.method.checkBox("ON", Device_error_zone_events_click, Device_error_zone_events_status)
        self.app.method.assertCheckBox("ON", Device_error_zone_events_status)
        self.app.method.checkBox("OFF", Sensor_reset_zone_events_click, Sensor_reset_zone_events_status)
        self.app.method.assertCheckBox("OFF", Sensor_reset_zone_events_status)
        self.app.method.checkBox("ON", Lost_zone_events_click, Lost_zone_events_status)
        self.app.method.assertCheckBox("ON", Lost_zone_events_status)
        self.app.method.checkBox("OFF", Check_connection_zone_events_click, Check_connection_zone_events_status)
        self.app.method.assertCheckBox("OFF", Check_connection_zone_events_status)
        self.app.method.checkBox("ON", Backup_battery_is_OK_zone_events_click, Backup_battery_is_OK_zone_events_status)
        self.app.method.assertCheckBox("ON", Backup_battery_is_OK_zone_events_status)
        self.app.method.checkBox("OFF", Sabotage_zone_events_click, Sabotage_zone_events_status)
        self.app.method.assertCheckBox("OFF", Sabotage_zone_events_status)
        self.app.method.checkBox("ON", Communication_restored_zone_events_click,
                                 Communication_restored_zone_events_status)
        self.app.method.assertCheckBox("ON", Communication_restored_zone_events_status)
        self.app.method.checkBox("OFF", Humidity_event_zone_events_click, Humidity_event_zone_events_status)
        self.app.method.assertCheckBox("OFF", Humidity_event_zone_events_status)
        self.app.method.checkBox("ON", CO_sensor_event_zone_events_click, CO_sensor_event_zone_events_status)
        self.app.method.assertCheckBox("ON", CO_sensor_event_zone_events_status)
        self.app.method.checkBox("OFF", Temperature_event_zone_events_click, Temperature_event_zone_events_status)
        self.app.method.assertCheckBox("OFF", Temperature_event_zone_events_status)
        self.app.method.checkBox("ON", Sensor_activation_Bell_mode_zone_events_click,
                                 Sensor_activation_Bell_mode_zone_events_status)
        self.app.method.assertCheckBox("ON", Sensor_activation_Bell_mode_zone_events_status)
        self.app.method.checkBox("OFF", SS_is_normal_zone_events_click, SS_is_normal_zone_events_status)
        self.app.method.assertCheckBox("OFF", SS_is_normal_zone_events_status)
        self.app.method.checkBox("OFF", AL_is_closed_zone_events_click, AL_is_closed_zone_events_status)
        self.app.method.assertCheckBox("OFF", AL_is_closed_zone_events_status)
        self.app.method.checkBox("OFF", AL_interrupted_zone_events_click, AL_interrupted_zone_events_status)
        self.app.method.assertCheckBox("OFF", AL_interrupted_zone_events_status)

    # Включение тумблеров Системные события прибора
    def tumblers_instrument_system_events_on(self):
        self.app.method.checkBox("OFF", instrument_system_events_click, instrument_system_events_status)
        self.app.method.assertCheckBox("OFF", instrument_system_events_status)
        self.app.method.checkBox("ON", Opening_the_case_of_the_device_click, Opening_the_case_of_the_device_status)
        self.app.method.assertCheckBox("ON", Opening_the_case_of_the_device_status)
        self.app.method.checkBox("ON", Closing_the_instrument_housing_click, Closing_the_instrument_housing_status)
        self.app.method.assertCheckBox("ON", Closing_the_instrument_housing_status)
        self.app.method.checkBox("ON", The_device_has_been_rebooted_click, The_device_has_been_rebooted_status)
        self.app.method.assertCheckBox("ON", The_device_has_been_rebooted_status)

    # Выключение тумблеров Системные события прибора
    def tumblers_instrument_system_events_off(self):
        self.app.method.checkBox("OFF", instrument_system_events_click, instrument_system_events_status)
        self.app.method.assertCheckBox("OFF", instrument_system_events_status)
        self.app.method.checkBox("OFF", Opening_the_case_of_the_device_click, Opening_the_case_of_the_device_status)
        self.app.method.assertCheckBox("OFF", Opening_the_case_of_the_device_status)
        self.app.method.checkBox("OFF", Closing_the_instrument_housing_click, Closing_the_instrument_housing_status)
        self.app.method.assertCheckBox("OFF", Closing_the_instrument_housing_status)
        self.app.method.checkBox("OFF", The_device_has_been_rebooted_click, The_device_has_been_rebooted_status)
        self.app.method.assertCheckBox("OFF", The_device_has_been_rebooted_status)

    # Частичное включение/выключение тумблеров Системные события прибора
    def tumblers_instrument_system_events_some(self):
        self.app.method.checkBox("OFF", instrument_system_events_click, instrument_system_events_status)
        self.app.method.assertCheckBox("OFF", instrument_system_events_status)
        self.app.method.checkBox("OFF", Opening_the_case_of_the_device_click, Opening_the_case_of_the_device_status)
        self.app.method.assertCheckBox("OFF", Opening_the_case_of_the_device_status)
        self.app.method.checkBox("OFF", Closing_the_instrument_housing_click, Closing_the_instrument_housing_status)
        self.app.method.assertCheckBox("OFF", Closing_the_instrument_housing_status)
        self.app.method.checkBox("OFF", The_device_has_been_rebooted_click, The_device_has_been_rebooted_status)
        self.app.method.assertCheckBox("OFF", The_device_has_been_rebooted_status)
        self.app.method.checkBox("OFF", instrument_system_events_click, instrument_system_events_status)
        self.app.method.assertCheckBox("OFF", instrument_system_events_status)
        self.app.method.checkBox("ON", Opening_the_case_of_the_device_click, Opening_the_case_of_the_device_status)
        self.app.method.assertCheckBox("ON", Opening_the_case_of_the_device_status)
        self.app.method.checkBox("ON", Closing_the_instrument_housing_click, Closing_the_instrument_housing_status)
        self.app.method.assertCheckBox("ON", Closing_the_instrument_housing_status)
        self.app.method.checkBox("ON", The_device_has_been_rebooted_click, The_device_has_been_rebooted_status)
        self.app.method.assertCheckBox("ON", The_device_has_been_rebooted_status)

    # Включение тумблеров события разделов
    def tumblers_event_path_on_main(self):
        self.app.method.checkBox("ON", Take_all_event_path_click, Take_all_event_path_status)
        self.app.method.assertCheckBox("ON", Take_all_event_path_status)
        self.app.method.assertCheckBox("ON", No_takel_status)
        self.app.method.assertCheckBox("ON", Outfit_mark_status)
        self.app.method.assertCheckBox("ON", Fire_status)
        self.app.method.assertCheckBox("ON", Fire_by_manual_call_point_status)
        self.app.method.assertCheckBox("ON", No_Fire_status)
        self.app.method.assertCheckBox("ON", Forcing_Partition_status)
        self.app.method.assertCheckBox("ON", Water_leak_status)
        self.app.method.assertCheckBox("ON", Section_taken_status)
        self.app.method.assertCheckBox("ON", Section_taken_off_status)
        self.app.method.assertCheckBox("ON", Silent_alarm_status)
        self.app.method.assertCheckBox("ON", Alarm_status)
        self.app.method.assertCheckBox("ON", Alarm_enter_status)

    # Включение тумблеров Питание прибора
    def tumblers_instrument_power_supply_on_main(self):
        self.app.method.checkBox("ON", Take_all_power_device_click, Take_all_power_device_status)
        self.app.method.assertCheckBox("ON", Take_all_power_device_status)
        self.app.method.assertCheckBox("ON", Battery_is_OK_status)
        self.app.method.assertCheckBox("ON", The_battery_is_charging_status)
        self.app.method.assertCheckBox("ON", Battery_is_charged_status)
        self.app.method.assertCheckBox("ON", Battery_not_connected_or_connected_incorrectly_status)
        self.app.method.assertCheckBox("ON", Battery_low_status)
        self.app.method.assertCheckBox("ON", High_internal_battery_resistance_status)
        self.app.method.assertCheckBox("ON", Mains_power_is_OK_status)
        self.app.method.assertCheckBox("ON", Mains_power_off_status)

    # Включение тумблеров События зон
    def tumblers_zone_events_on_main(self):
        self.app.method.checkBox("ON", zone_events_device_click, zone_events_device_status)
        self.app.method.assertCheckBox("ON", zone_events_device_status)
        self.app.method.assertCheckBox("ON", Battery_OK_zone_events_device_status)
        self.app.method.assertCheckBox("ON", ready_status)
        self.app.method.assertCheckBox("ON", Case_closed_status)
        self.app.method.assertCheckBox("ON", Case_open_status)
        self.app.method.assertCheckBox("ON", Low_battery_zone_events_status)
        self.app.method.assertCheckBox("ON", Backup_battery_error_zone_events_status)
        self.app.method.assertCheckBox("ON", Device_error_zone_events_status)
        self.app.method.assertCheckBox("ON", Sensor_reset_zone_events_status)
        self.app.method.assertCheckBox("ON", Lost_zone_events_status)
        self.app.method.assertCheckBox("ON", Check_connection_zone_events_status)
        self.app.method.assertCheckBox("ON", Backup_battery_is_OK_zone_events_status)
        self.app.method.assertCheckBox("ON", Sabotage_zone_events_status)
        self.app.method.assertCheckBox("ON", Communication_restored_zone_events_status)
        self.app.method.assertCheckBox("ON", Humidity_event_zone_events_status)
        self.app.method.assertCheckBox("ON", CO_sensor_event_zone_events_status)
        self.app.method.assertCheckBox("ON", Temperature_event_zone_events_status)
        self.app.method.assertCheckBox("ON", Sensor_activation_Bell_mode_zone_events_status)
        self.app.method.assertCheckBox("ON", SS_is_normal_zone_events_status)
        self.app.method.assertCheckBox("ON", AL_is_closed_zone_events_status)
        self.app.method.assertCheckBox("ON", AL_interrupted_zone_events_status)

    # Включение тумблеров Системные события прибора
    def tumblers_instrument_system_events_on_main(self):
        self.app.method.checkBox("ON", instrument_system_events_click, instrument_system_events_status)
        self.app.method.assertCheckBox("ON", instrument_system_events_status)
        self.app.method.assertCheckBox("ON", Opening_the_case_of_the_device_status)
        self.app.method.assertCheckBox("ON", Closing_the_instrument_housing_status)
        self.app.method.assertCheckBox("ON", The_device_has_been_rebooted_status)

    # Проверка выпадающего списка Тип управления - ОСНОВНОЙ
    def check_openType_main(self):
        nameTypeList = ['SMS пользователю', 'SMS Эгида', 'Звонок', 'DC09']
        self.app.method.check_dropdown_list(type_main, nameTypeList)

    # Проверка выпадающего списка Тип управления - Резерв 1
    def check_openType_rezerv_1(self):
        nameTypeList = ['SMS пользователю', 'SMS Эгида', 'Звонок', 'DC09']
        self.app.method.check_dropdown_list(type_rezerv_1, nameTypeList)

    # Проверка выпадающего списка Тип управления - Резерв 2
    def check_openType_rezerv_2(self):
        nameTypeList = ['SMS пользователю', 'SMS Эгида', 'Звонок', 'DC09']
        self.app.method.check_dropdown_list(type_rezerv_2, nameTypeList)

    # Проверка выпадающего списка Язык - ОСНОВНОЙ
    def check_lang_sms_user_main(self):
        langList = ['Русский', 'Английский']
        self.app.method.check_dropdown_list(lang_main, langList)

    # Проверка выпадающего списка Язык - Резерв 1
    def check_lang_sms_user_rezerv_1(self):
        langList = ['Русский', 'Английский']
        self.app.method.check_dropdown_list(lang_rezerv_1, langList)

    # Проверка выпадающего списка Язык - Резерв 2
    def check_lang_sms_user_rezerv_2(self):
        langList = ['Русский', 'Английский']
        self.app.method.check_dropdown_list(lang_rezerv_2, langList)

    # Проверка выпадающего списка тестировать если - ОСНОВНОЙ
    def check_test_if_sms_user_main(self):
        testIfList = ['Всегда', 'Канал активен']
        self.app.method.check_dropdown_list(test_IF_main, testIfList)

    # Проверка выпадающего списка тестировать если - Резерв 1
    def check_test_if_sms_user_resrv_1(self):
        testIfList = ['Всегда', 'Канал активен']
        self.app.method.check_dropdown_list(test_IF_rezerv_1, testIfList)

    # Проверка выпадающего списка тестировать если - Резерв 2
    def check_test_if_sms_user_resrv_2(self):
        testIfList = ['Всегда', 'Канал активен']
        self.app.method.check_dropdown_list(test_IF_rezerv_2, testIfList)

    # Проверка выпадающего списка тестировать если sms egida - ОСНОВНОЙ
    def check_test_if_sms_egida_main(self):
        testIfList = ['Всегда', 'Канал активен']
        self.app.method.check_dropdown_list(test_IF_sms_egida_main, testIfList)

    # Проверка выпадающего списка тестировать если sms egida - Резерв 1
    def check_test_if_sms_egida_rezerv_1(self):
        testIfList = ['Всегда', 'Канал активен']
        self.app.method.check_dropdown_list(test_IF_sms_egidrezerv_1, testIfList)

    # Проверка выпадающего списка тестировать если sms egida - Резерв 2
    def check_test_if_sms_egida_rezerv_2(self):
        testIfList = ['Всегда', 'Канал активен']
        self.app.method.check_dropdown_list(test_IF_sms_egidrezerv_2, testIfList)

    # Проверка выпадающего списка метод тестирования - ОСНОВНОЙ
    def check_test_method_sms_user_main(self):
        testMethodList = ['SMS', 'Звонок', 'SMS Эгида']
        self.app.method.check_dropdown_list(test_method_main, testMethodList)

    # Проверка выпадающего списка метод тестирования - Резерв 1
    def check_test_method_sms_user_rezerv_1(self):
        testMethodList = ['SMS', 'Звонок', 'SMS Эгида']
        self.app.method.check_dropdown_list(test_method_rezerv_1, testMethodList)

    # Проверка выпадающего списка метод тестирования - Резерв 2
    def check_test_method_sms_user_rezerv_2(self):
        testMethodList = ['SMS', 'Звонок', 'SMS Эгида']
        self.app.method.check_dropdown_list(test_method_rezerv_2, testMethodList)

    # Проверка выпадающего списка метод тестирования СМС ЭГИДА - ОСНОВНОЙ
    def check_test_method_sms_egida_main(self):
        testMethodList = ['SMS', 'Звонок', 'SMS Эгида']
        self.app.method.check_dropdown_list(test_method_sms_egida_main, testMethodList)

    # Проверка выпадающего списка метод тестирования СМС ЭГИДА - Резерв 1
    def check_test_method_sms_egida_rezerv_1(self):
        testMethodList = ['SMS', 'Звонок', 'SMS Эгида']
        self.app.method.check_dropdown_list(test_method_sms_egida_rezerv_1, testMethodList)

    # Проверка выпадающего списка метод тестирования СМС ЭГИДА - Резерв 2
    def check_test_method_sms_egida_rezerv_2(self):
        testMethodList = ['SMS', 'Звонок', 'SMS Эгида']
        self.app.method.check_dropdown_list(test_method_sms_egida_rezerv_2, testMethodList)

    # Проверка выпадающего списка Тестировать - ОСНОВНОЙ
    def check_testing_sms_user_main(self):
        testMethodList = ['С интервалом', 'По расписанию']
        self.app.method.check_dropdown_list(testing_main, testMethodList)

    # Проверка выпадающего списка Тестировать - Резерв 1
    def check_testing_sms_user_rezerv_1(self):
        testMethodList = ['С интервалом', 'По расписанию']
        self.app.method.check_dropdown_list(testing_rezerv_1, testMethodList)

    # Проверка выпадающего списка Тестировать - Резерв 2
    def check_testing_sms_user_rezerv_2(self):
        testMethodList = ['С интервалом', 'По расписанию']
        self.app.method.check_dropdown_list(testing_rezerv_2, testMethodList)

    # Проверка выпадающего списка Тестировать SMS ЭГИДА - ОСНОВНОЙ
    def check_testing_sms_egida_main(self):
        testMethodList = ['С интервалом', 'По расписанию']
        self.app.method.check_dropdown_list(testing_sms_egida_main, testMethodList)

    # Проверка выпадающего списка Тестировать dc09 - ОСНОВНОЙ
    def check_testing_dc09_main(self):
        testMethodList = ['С интервалом', 'По расписанию']
        self.app.method.check_dropdown_list(testing_dco9_main, testMethodList)

    # Проверка выпадающего списка Тестировать SMS ЭГИДА - Резерв 1
    def check_testing_sms_egida_rezerv_1(self):
        testMethodList = ['С интервалом', 'По расписанию']
        self.app.method.check_dropdown_list(testing_sms_egida_rezerv_1, testMethodList)

    def check_testing_dc09_rezerv_1(self):
        testMethodList = ['С интервалом', 'По расписанию']
        self.app.method.check_dropdown_list(testing_sdco9_rezerv_1, testMethodList)

    # Проверка выпадающего списка Тестировать SMS ЭГИДА - Резерв 2
    def check_testing_sms_egida_rezerv_2(self):
        testMethodList = ['С интервалом', 'По расписанию']
        self.app.method.check_dropdown_list(testing_sms_egida_rezerv_2, testMethodList)

    # Проверка выпадающего списка Тестировать SMS ЭГИДА - dc09
    def check_testing_dc09_rezerv_2(self):
        testMethodList = ['С интервалом', 'По расписанию']
        self.app.method.check_dropdown_list(testing_dco9_rezerv_2, testMethodList)

    # Проверка выпадающего списка Дни недели - ОСНОВНОЙ
    def check_days_of_the_week_sms_user_main(self):
        daysList = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
        self.app.method.check_dropdown_list_with_check_box(days_of_the_week_main, daysList)

    # Проверка выпадающего списка Дни недели - Резерв 1
    def check_days_of_the_week_sms_user_rezerv_1(self):
        daysList = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
        self.app.method.check_dropdown_list_with_check_box(days_of_the_week_rezerv_1, daysList)

    def scrol(self):
        wd = self.app.wd
        target = wd.find_element(By.XPATH, '//*[@id="modalSettings"]/div/div[2]/div[2]/button[1]')
        actions = ActionChains(wd)
        actions.move_to_element(target)
        actions.perform()

    # Проверка выпадающего списка Дни недели - Резерв 2
    def check_days_of_the_week_sms_user_rezerv_2(self):
        self.scrol()
        daysList = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
        self.app.method.check_dropdown_list_with_check_box_double_click(days_of_the_week_rezerv_2, daysList)

    # Проверка выпадающего списка Дни недели - ОСНОВНОЙ
    def check_days_of_the_week_sms_user_all_main(self):
        daysList = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
        self.app.method.assert_drop_wown_list_with_check_box(days_of_the_week_main, main_check_box_drop_down_days,
                                                             daysList)

    # Проверка выпадающего списка Дни недели - Резерв 1
    def check_days_of_the_week_sms_user_all_rezerv_1(self):
        daysList = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
        self.app.method.assert_drop_wown_list_with_check_box(days_of_the_week_rezerv_1, main_check_box_drop_down_days,
                                                             daysList)

    # Проверка выпадающего списка Дни недели - Резерв 2
    def check_days_of_the_week_sms_user_all_rezerv_2(self):
        daysList = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
        self.app.method.assert_drop_wown_list_with_check_box(days_of_the_week_rezerv_2, main_check_box_drop_down_days,
                                                             daysList)

    # Включение чекбоксов звонок - основной
    def check_box_call_on_channel_main(self):
        self.app.method.check_box_verification("ON", main_Enable_channel_testing_click,
                                               main_Enable_channel_testing_status)

    # Включение чекбоксов звонок - основной
    def check_box_call_off_channel_main(self):
        self.app.method.check_box_verification("OFF", main_Enable_channel_testing_click,
                                               main_Enable_channel_testing_status)

    # Включение чекбоксов звонок - резерв 1
    def check_box_call_on_channel_rezerv_1(self):
        self.app.method.check_box_verification("ON", rezerv_1_Enable_channel_testing_click,
                                               rezerv_1_Enable_channel_testing_status)

    # Включение чекбоксов звонок - резерв 1
    def check_box_call_off_channel_rezerv_1(self):
        self.app.method.check_box_verification("OFF", rezerv_1_Enable_channel_testing_click,
                                               rezerv_1_Enable_channel_testing_status)

    # Включение чекбоксов звонок - резерв 2
    def check_box_call_on_channel_rezerv_2(self):
        self.app.method.check_box_verification("ON", rezerv_2_Enable_channel_testing_click,
                                               rezerv_2_Enable_channel_testing_status)

    # Включение чекбоксов звонок - резерв 2
    def check_box_call_off_channel_rezerv_2(self):
        self.app.method.check_box_verification("OFF", rezerv_2_Enable_channel_testing_click,
                                               rezerv_2_Enable_channel_testing_status)

    # Включение чекбоксов смс пользователю - основной
    def check_box_sms_user_on_channel_main(self):
        self.app.method.check_box_verification("ON", main_Send_event_time_click, main_Send_event_time_status)
        self.app.method.check_box_verification("ON", main_Send_event_data_click, main_Send_event_data_status)
        self.app.method.check_box_verification("ON", main_Enable_channel_testing_click,
                                               main_Enable_channel_testing_status)

    # Выключение чекбоксов смс пользователю - основной
    def check_box_sms_user_off_channel_main(self):
        self.app.method.check_box_verification("OFF", main_Send_event_time_click, main_Send_event_time_status)
        self.app.method.check_box_verification("OFF", main_Send_event_data_click, main_Send_event_data_status)
        self.app.method.check_box_verification("OFF", main_Enable_channel_testing_click,
                                               main_Enable_channel_testing_status)

    # Включение чекбоксов смс пользователю - резерв 1
    def check_box_sms_user_on_channel_rezerv_1(self):
        self.app.method.check_box_verification("ON", rezerv_1_Send_event_time_click, rezerv_1_Send_event_time_status)
        self.app.method.check_box_verification("ON", rezerv_1_Send_event_data_click, rezerv_1_Send_event_data_status)
        self.app.method.check_box_verification("ON", rezerv_1_Enable_channel_testing_click,
                                               rezerv_1_Enable_channel_testing_status)

    # Выключение чекбоксов смс пользователю - резерв 1
    def check_box_sms_user_off_channel_rezerv_1(self):
        self.app.method.check_box_verification("OFF", rezerv_1_Send_event_time_click, rezerv_1_Send_event_time_status)
        self.app.method.check_box_verification("OFF", rezerv_1_Send_event_data_click, rezerv_1_Send_event_data_status)
        self.app.method.check_box_verification("OFF", rezerv_1_Enable_channel_testing_click,
                                               rezerv_1_Enable_channel_testing_status)

    # Включение чекбоксов смс пользователю - резерв 2
    def check_box_sms_user_on_channel_rezerv_2(self):
        self.app.method.check_box_verification("ON", rezerv_2_Send_event_time_click, rezerv_2_Send_event_time_status)
        self.app.method.check_box_verification("ON", rezerv_2_Send_event_data_click, rezerv_2_Send_event_data_status)
        self.app.method.check_box_verification("ON", rezerv_2_Enable_channel_testing_click,
                                               rezerv_2_Enable_channel_testing_status)

    # Выключение чекбоксов смс пользователю - резерв 2
    def check_box_sms_user_off_channel_rezerv_2(self):
        self.app.method.check_box_verification("OFF", rezerv_2_Send_event_time_click, rezerv_2_Send_event_time_status)
        self.app.method.check_box_verification("OFF", rezerv_2_Send_event_data_click, rezerv_2_Send_event_data_status)
        self.app.method.check_box_verification("OFF", rezerv_2_Enable_channel_testing_click,
                                               rezerv_2_Enable_channel_testing_status)

    # Включение чекбоксов смс пользователю - основной
    def check_box_dc09_on_channel_main(self):
        self.app.method.check_box_verification("ON", main_Encryption_click, main_Encryption_status)
        self.app.method.check_box_verification("ON", main_Enable_channel_testing_click,
                                               main_Enable_channel_testing_status)

    # Выключение чекбоксов dc09 - основной
    def check_box_dc09_off_channel_main(self):
        self.app.method.check_box_verification("OFF", main_Encryption_click, main_Encryption_status)
        self.app.method.check_box_verification("OFF", main_Enable_channel_testing_click,
                                               main_Enable_channel_testing_status)

    # Включение чекбоксов dc09- Резерв 1
    def check_box_dc09_onn_channel_rezerv_1(self):
        self.app.method.check_box_verification("ON", rezerv_1_Encryption_click, rezerv_1_Encryption_status)
        self.app.method.check_box_verification("ON", rezerv_1_Enable_channel_testing_click,
                                               rezerv_1_Enable_channel_testing_status)

    # Выключение чекбоксов dc09- Резерв 1
    def check_box_dc09_off_channel_rezerv_1(self):
        self.app.method.check_box_verification("OFF", rezerv_1_Encryption_click, rezerv_1_Encryption_status)
        self.app.method.check_box_verification("OFF", rezerv_1_Enable_channel_testing_click,
                                               rezerv_1_Enable_channel_testing_status)

    # Включение чекбоксов dc09- Резерв 2
    def check_box_dc09_onn_channel_rezerv_2(self):
        self.app.method.check_box_verification("ON", rezerv_2_Encryption_click, rezerv_2_Encryption_status)
        self.app.method.check_box_verification("ON", rezerv_2_Enable_channel_testing_click,
                                               rezerv_2_Enable_channel_testing_status)

    # Выключение чекбоксов dc09- Резерв 2
    def check_box_dc09_off_channel_rezerv_2(self):
        self.app.method.check_box_verification("OFF", rezerv_2_Encryption_click, rezerv_1_Encryption_status)
        self.app.method.check_box_verification("OFF", rezerv_2_Enable_channel_testing_click,
                                               rezerv_2_Enable_channel_testing_status)

    # Проверка выпадающего списка Канал соединения - ОСНОВНОЙ
    def check_connection_main(self):
        connectionList = ['Авто', 'Ethernet', 'GPRS']
        self.app.method.check_dropdown_list(connection_main, connectionList)

    # Проверка выпадающего списка Канал соединения - Резерв 1
    def check_connection_rezerv_1(self):
        connectionList = ['Авто', 'Ethernet', 'GPRS']
        self.app.method.check_dropdown_list(connection_rezerv_1, connectionList)

    # Проверка выпадающего списка Канал соединения - Резерв 2
    def check_connection_rezerv_2(self):
        connectionList = ['Авто', 'Ethernet', 'GPRS']
        self.app.method.check_dropdown_list(connection_rezerv_2, connectionList)

    def save_button_click(self):
        with allure.step("Клик по кнопке СОХРАНИТЬ"):
            self.app.method.click((By.XPATH, save_button))
        with allure.step("Проверка всплывающего окна сохранено"):
            self.app.method.click((By.XPATH, '/html/body//button[@class="toast-message-btn-close close-icon"]'))

        # Включение тумблеров события разделов для сохранения

    def tumblers_event_path_on_save(self, type_control):
        self.app.method.checkBox("OFF", Take_all_event_path_click, Take_all_event_path_status)
        self.app.method.checkBox("ON", Outfit_mark_click, Outfit_mark_status)
        self.app.method.checkBox("ON", Fire_by_manual_call_point_click, Fire_by_manual_call_point_status)
        self.app.method.checkBox("ON", Forcing_Partition_click, Forcing_Partition_status)
        self.app.method.checkBox("ON", Section_taken_click, Section_taken_status)
        self.app.method.checkBox("ON", Silent_alarm_click, Silent_alarm_status)
        self.app.method.checkBox("ON", Alarm_click, Alarm_status)
        self.app.method.checkBox("ON", Alarm_enter_click, Alarm_enter_status)
        if type_control != 'DC09':
            self.app.method.checkBox("ON", No_take_click, No_takel_status)
            self.app.method.checkBox("ON", Fire_click, Fire_status)
            self.app.method.checkBox("ON", No_Fire_click, No_Fire_status)
            self.app.method.checkBox("ON", Water_leak_click, Water_leak_status)
            self.app.method.checkBox("ON", Section_taken_off_click, Section_taken_off_status)


        # Проверка включение тумблеров события разделов - сохранение

    def assert_save_tumblers_event_path_on(self, type_control):
        self.app.method.assertCheckBox("ON", Take_all_event_path_status)
        self.app.method.assertCheckBox("ON", Outfit_mark_status)
        self.app.method.assertCheckBox("ON", Fire_by_manual_call_point_status)
        self.app.method.assertCheckBox("ON", Forcing_Partition_status)
        self.app.method.assertCheckBox("ON", Section_taken_status)
        self.app.method.assertCheckBox("ON", Silent_alarm_status)
        self.app.method.assertCheckBox("ON", Alarm_status)
        self.app.method.assertCheckBox("ON", Alarm_enter_status)
        if type_control != 'DC09':
            self.app.method.assertCheckBox("ON", No_takel_status)
            self.app.method.assertCheckBox("ON", Fire_status)
            self.app.method.assertCheckBox("ON", No_Fire_status)
            self.app.method.assertCheckBox("ON", Water_leak_status)
            self.app.method.assertCheckBox("ON", Section_taken_off_status)

        # Выключение тумблеров события разделов для сохранения

    def tumblers_event_path_off_save(self, type_control):
        self.app.method.checkBox("OFF", Take_all_event_path_click, Take_all_event_path_status)
        self.app.method.checkBox("OFF", Outfit_mark_click, Outfit_mark_status)
        self.app.method.checkBox("OFF", Fire_by_manual_call_point_click, Fire_by_manual_call_point_status)
        self.app.method.checkBox("OFF", Forcing_Partition_click, Forcing_Partition_status)
        self.app.method.checkBox("OFF", Section_taken_click, Section_taken_status)
        self.app.method.checkBox("OFF", Silent_alarm_click, Silent_alarm_status)
        self.app.method.checkBox("OFF", Alarm_click, Alarm_status)
        self.app.method.checkBox("OFF", Alarm_enter_click, Alarm_enter_status)
        if type_control != 'DC09':
            self.app.method.checkBox("OFF", No_take_click, No_takel_status)
            self.app.method.checkBox("OFF", Fire_click, Fire_status)
            self.app.method.checkBox("OFF", No_Fire_click, No_Fire_status)
            self.app.method.checkBox("OFF", Water_leak_click, Water_leak_status)
            self.app.method.checkBox("OFF", Section_taken_off_click, Section_taken_off_status)

        # Проверка выключение тумблеров события разделов - сохранение

    def assert_save_tumblers_event_path_off(self, type_control):
        self.app.method.assertCheckBox("OFF", Take_all_event_path_status)
        self.app.method.assertCheckBox("OFF", Outfit_mark_status)
        self.app.method.assertCheckBox("OFF", Fire_by_manual_call_point_status)
        self.app.method.assertCheckBox("OFF", Forcing_Partition_status)
        self.app.method.assertCheckBox("OFF", Section_taken_status)
        self.app.method.assertCheckBox("OFF", Silent_alarm_status)
        self.app.method.assertCheckBox("OFF", Alarm_status)
        self.app.method.assertCheckBox("OFF", Alarm_enter_status)
        if type_control != 'DC09':
            self.app.method.assertCheckBox("OFF", No_takel_status)
            self.app.method.assertCheckBox("OFF", Fire_status)
            self.app.method.assertCheckBox("OFF", No_Fire_status)
            self.app.method.assertCheckBox("OFF", Water_leak_status)
            self.app.method.assertCheckBox("OFF", Section_taken_off_status)

        # Частичное включение тумблеров события разделов для сохранения

    def tumblers_event_path_some_save(self, type_control):
        self.app.method.checkBox("OFF", Take_all_event_path_click, Take_all_event_path_status)
        if type_control == 'DC09':
            self.app.method.checkBox("ON", Outfit_mark_click, Outfit_mark_status)
            self.app.method.checkBox("OFF", Fire_by_manual_call_point_click, Fire_by_manual_call_point_status)
            self.app.method.checkBox("ON", Forcing_Partition_click, Forcing_Partition_status)
            self.app.method.checkBox("OFF", Section_taken_click, Section_taken_status)
            self.app.method.checkBox("ON", Silent_alarm_click, Silent_alarm_status)
            self.app.method.checkBox("OFF", Alarm_click, Alarm_status)
            self.app.method.checkBox("ON", Alarm_enter_click, Alarm_enter_status)
        else:
            self.app.method.checkBox("ON", No_take_click, No_takel_status)
            self.app.method.checkBox("OFF", Outfit_mark_click, Outfit_mark_status)
            self.app.method.checkBox("ON", Fire_click, Fire_status)
            self.app.method.checkBox("OFF", Fire_by_manual_call_point_click, Fire_by_manual_call_point_status)
            self.app.method.checkBox("ON", No_Fire_click, No_Fire_status)
            self.app.method.checkBox("OFF", Forcing_Partition_click, Forcing_Partition_status)
            self.app.method.checkBox("ON", Water_leak_click, Water_leak_status)
            self.app.method.checkBox("OFF", Section_taken_click, Section_taken_status)
            self.app.method.checkBox("ON", Section_taken_off_click, Section_taken_off_status)
            self.app.method.checkBox("OFF", Silent_alarm_click, Silent_alarm_status)
            self.app.method.checkBox("ON", Alarm_click, Alarm_status)
            self.app.method.checkBox("OFF", Alarm_enter_click, Alarm_enter_status)

        # Проверка частичного включение тумблеров события разделов - сохранение

    def assert_save_tumblers_event_path_some(self, type_control):
        self.app.method.assertCheckBox("OFF", Take_all_event_path_status)
        if type_control == 'DC09':
            self.app.method.assertCheckBox("ON", Outfit_mark_status)
            self.app.method.assertCheckBox("OFF", Fire_by_manual_call_point_status)
            self.app.method.assertCheckBox("ON", Forcing_Partition_status)
            self.app.method.assertCheckBox("OFF", Section_taken_status)
            self.app.method.assertCheckBox("ON", Silent_alarm_status)
            self.app.method.assertCheckBox("OFF", Alarm_status)
            self.app.method.assertCheckBox("ON", Alarm_enter_status)
        else:
            self.app.method.assertCheckBox("ON", No_takel_status)
            self.app.method.assertCheckBox("OFF", Outfit_mark_status)
            self.app.method.assertCheckBox("ON", Fire_status)
            self.app.method.assertCheckBox("OFF", Fire_by_manual_call_point_status)
            self.app.method.assertCheckBox("ON", No_Fire_status)
            self.app.method.assertCheckBox("OFF", Forcing_Partition_status)
            self.app.method.assertCheckBox("ON", Water_leak_status)
            self.app.method.assertCheckBox("OFF", Section_taken_status)
            self.app.method.assertCheckBox("ON", Section_taken_off_status)
            self.app.method.assertCheckBox("OFF", Silent_alarm_status)
            self.app.method.assertCheckBox("ON", Alarm_status)
            self.app.method.assertCheckBox("OFF", Alarm_enter_status)

        # Частичное включение тумблеров события разделов для сохранения

    def tumblers_event_path_some_2_save(self, type_control):
        self.app.method.checkBox("OFF", Take_all_event_path_click, Take_all_event_path_status)
        if type_control == 'DC09':
            self.app.method.checkBox("OFF", Outfit_mark_click, Outfit_mark_status)
            self.app.method.checkBox("ON", Fire_by_manual_call_point_click, Fire_by_manual_call_point_status)
            self.app.method.checkBox("OFF", Forcing_Partition_click, Forcing_Partition_status)
            self.app.method.checkBox("ON", Section_taken_click, Section_taken_status)
            self.app.method.checkBox("OFF", Silent_alarm_click, Silent_alarm_status)
            self.app.method.checkBox("ON", Alarm_click, Alarm_status)
            self.app.method.checkBox("OFF", Alarm_enter_click, Alarm_enter_status)
        else:
            self.app.method.checkBox("OFF", No_take_click, No_takel_status)
            self.app.method.checkBox("ON", Outfit_mark_click, Outfit_mark_status)
            self.app.method.checkBox("OFF", Fire_click, Fire_status)
            self.app.method.checkBox("ON", Fire_by_manual_call_point_click, Fire_by_manual_call_point_status)
            self.app.method.checkBox("OFF", No_Fire_click, No_Fire_status)
            self.app.method.checkBox("ON", Forcing_Partition_click, Forcing_Partition_status)
            self.app.method.checkBox("OFF", Water_leak_click, Water_leak_status)
            self.app.method.checkBox("ON", Section_taken_click, Section_taken_status)
            self.app.method.checkBox("OFF", Section_taken_off_click, Section_taken_off_status)
            self.app.method.checkBox("ON", Silent_alarm_click, Silent_alarm_status)
            self.app.method.checkBox("OFF", Alarm_click, Alarm_status)
            self.app.method.checkBox("ON", Alarm_enter_click, Alarm_enter_status)

        # Проверка частичного включение тумблеров события разделов - сохранение

    def assert_save_tumblers_event_path_some_2(self, type_control):
        self.app.method.assertCheckBox("OFF", Take_all_event_path_status)
        if type_control == 'DC09':
            self.app.method.assertCheckBox("OFF", Outfit_mark_status)
            self.app.method.assertCheckBox("ON", Fire_by_manual_call_point_status)
            self.app.method.assertCheckBox("OFF", Forcing_Partition_status)
            self.app.method.assertCheckBox("ON", Section_taken_status)
            self.app.method.assertCheckBox("OFF", Silent_alarm_status)
            self.app.method.assertCheckBox("ON", Alarm_status)
            self.app.method.assertCheckBox("OFF", Alarm_enter_status)
        else:
            self.app.method.assertCheckBox("OFF", No_takel_status)
            self.app.method.assertCheckBox("ON", Outfit_mark_status)
            self.app.method.assertCheckBox("OFF", Fire_status)
            self.app.method.assertCheckBox("ON", Fire_by_manual_call_point_status)
            self.app.method.assertCheckBox("OFF", No_Fire_status)
            self.app.method.assertCheckBox("ON", Forcing_Partition_status)
            self.app.method.assertCheckBox("OFF", Water_leak_status)
            self.app.method.assertCheckBox("ON", Section_taken_status)
            self.app.method.assertCheckBox("OFF", Section_taken_off_status)
            self.app.method.assertCheckBox("ON", Silent_alarm_status)
            self.app.method.assertCheckBox("OFF", Alarm_status)
            self.app.method.assertCheckBox("ON", Alarm_enter_status)

        # Включение основного тумблера - события разделов для сохранения

    def tumblers_event_path_main(self):
        self.app.method.checkBox("ON", Take_all_event_path_click, Take_all_event_path_status)

    # Включение тумблеров События зон - сохранение
    def tumblers_zone_events_save_on(self, type_control):
        self.app.method.checkBox("OFF", zone_events_device_click, zone_events_device_status)
        self.app.method.checkBox("ON", Battery_OK_zone_events_device_click, Battery_OK_zone_events_device_status)
        self.app.method.checkBox("ON", ready_click, ready_status)
        self.app.method.checkBox("ON", Case_closed_click, Case_closed_status)
        self.app.method.checkBox("ON", Case_open_click, Case_open_status)
        self.app.method.checkBox("ON", Low_battery_zone_events_click, Low_battery_zone_events_status)
        self.app.method.checkBox("ON", Backup_battery_error_zone_events_click, Backup_battery_error_zone_events_status)
        self.app.method.checkBox("ON", Device_error_zone_events_click, Device_error_zone_events_status)
        self.app.method.checkBox("ON", Sensor_reset_zone_events_click, Sensor_reset_zone_events_status)
        self.app.method.checkBox("ON", Lost_zone_events_click, Lost_zone_events_status)
        self.app.method.checkBox("ON", Backup_battery_is_OK_zone_events_click, Backup_battery_is_OK_zone_events_status)
        self.app.method.checkBox("ON", Sabotage_zone_events_click, Sabotage_zone_events_status)
        self.app.method.checkBox("ON", Communication_restored_zone_events_click,
                                 Communication_restored_zone_events_status)
        self.app.method.checkBox("ON", Humidity_event_zone_events_click, Humidity_event_zone_events_status)
        self.app.method.checkBox("ON", CO_sensor_event_zone_events_click, CO_sensor_event_zone_events_status)
        self.app.method.checkBox("ON", Temperature_event_zone_events_click, Temperature_event_zone_events_status)
        self.app.method.checkBox("ON", SS_is_normal_zone_events_click, SS_is_normal_zone_events_status)
        self.app.method.checkBox("ON", AL_is_closed_zone_events_click, AL_is_closed_zone_events_status)
        self.app.method.checkBox("ON", AL_interrupted_zone_events_click, AL_interrupted_zone_events_status)
        if type_control == 'Звонок' or type_control == 'SMS пользователю' or type_control == 'SMS Эгида':
            self.app.method.checkBox("ON", Check_connection_zone_events_click, Check_connection_zone_events_status)
            self.app.method.checkBox("ON", Sensor_activation_Bell_mode_zone_events_click,
                                     Sensor_activation_Bell_mode_zone_events_status)
            if type_control != 'SMS Эгида':
                self.app.method.checkBox("ON", water_sensor_loop_breakage_click, water_sensor_loop_breakage_status)
        elif type_control == 'DC09':
            self.app.method.checkBox("ON", water_sensor_loop_breakage_click, water_sensor_loop_breakage_status)

    # Проверка Включение тумблеров События зон - сохранение
    def assert_tumblers_zone_events_save_on(self, type_control):
        self.app.method.assertCheckBox("ON", zone_events_device_status)
        self.app.method.assertCheckBox("ON", Battery_OK_zone_events_device_status)
        self.app.method.assertCheckBox("ON", ready_status)
        self.app.method.assertCheckBox("ON", Case_closed_status)
        self.app.method.assertCheckBox("ON", Case_open_status)
        self.app.method.assertCheckBox("ON", Low_battery_zone_events_status)
        self.app.method.assertCheckBox("ON", Backup_battery_error_zone_events_status)
        self.app.method.assertCheckBox("ON", Device_error_zone_events_status)
        self.app.method.assertCheckBox("ON", Sensor_reset_zone_events_status)
        self.app.method.assertCheckBox("ON", Lost_zone_events_status)
        self.app.method.assertCheckBox("ON", Backup_battery_is_OK_zone_events_status)
        self.app.method.assertCheckBox("ON", Sabotage_zone_events_status)
        self.app.method.assertCheckBox("ON", Communication_restored_zone_events_status)
        self.app.method.assertCheckBox("ON", Humidity_event_zone_events_status)
        self.app.method.assertCheckBox("ON", CO_sensor_event_zone_events_status)
        self.app.method.assertCheckBox("ON", Temperature_event_zone_events_status)
        self.app.method.assertCheckBox("ON", SS_is_normal_zone_events_status)
        self.app.method.assertCheckBox("ON", AL_is_closed_zone_events_status)
        self.app.method.assertCheckBox("ON", AL_interrupted_zone_events_status)
        if type_control == 'Звонок' or type_control == 'SMS пользователю' or type_control == 'SMS Эгида':
            self.app.method.assertCheckBox("ON", Check_connection_zone_events_status)
            self.app.method.assertCheckBox("ON", Sensor_activation_Bell_mode_zone_events_status)
            if type_control != 'SMS Эгида':
                self.app.method.assertCheckBox("ON", water_sensor_loop_breakage_status)
        elif type_control == 'DC09':
            self.app.method.assertCheckBox("ON", water_sensor_loop_breakage_status)

    # Выключение тумблеров События зон - сохранение
    def tumblers_zone_events_save_off(self, type_control):
        self.app.method.checkBox("ON", zone_events_device_click, zone_events_device_status)
        self.app.method.checkBox("OFF", Battery_OK_zone_events_device_click, Battery_OK_zone_events_device_status)
        self.app.method.checkBox("OFF", ready_click, ready_status)
        self.app.method.checkBox("OFF", Case_closed_click, Case_closed_status)
        self.app.method.checkBox("OFF", Case_open_click, Case_open_status)
        self.app.method.checkBox("OFF", Low_battery_zone_events_click, Low_battery_zone_events_status)
        self.app.method.checkBox("OFF", Backup_battery_error_zone_events_click, Backup_battery_error_zone_events_status)
        self.app.method.checkBox("OFF", Device_error_zone_events_click, Device_error_zone_events_status)
        self.app.method.checkBox("OFF", Sensor_reset_zone_events_click, Sensor_reset_zone_events_status)
        self.app.method.checkBox("OFF", Lost_zone_events_click, Lost_zone_events_status)
        self.app.method.checkBox("OFF", Backup_battery_is_OK_zone_events_click, Backup_battery_is_OK_zone_events_status)
        self.app.method.checkBox("OFF", Sabotage_zone_events_click, Sabotage_zone_events_status)
        self.app.method.checkBox("OFF", Communication_restored_zone_events_click,
                                 Communication_restored_zone_events_status)
        self.app.method.checkBox("OFF", Humidity_event_zone_events_click, Humidity_event_zone_events_status)
        self.app.method.checkBox("OFF", CO_sensor_event_zone_events_click, CO_sensor_event_zone_events_status)
        self.app.method.checkBox("OFF", Temperature_event_zone_events_click, Temperature_event_zone_events_status)
        self.app.method.checkBox("OFF", SS_is_normal_zone_events_click, SS_is_normal_zone_events_status)
        self.app.method.checkBox("OFF", AL_is_closed_zone_events_click, AL_is_closed_zone_events_status)
        self.app.method.checkBox("OFF", AL_interrupted_zone_events_click, AL_interrupted_zone_events_status)
        if type_control == 'Звонок' or type_control == 'SMS пользователю' or type_control == 'SMS Эгида':
            self.app.method.checkBox("OFF", Check_connection_zone_events_click, Check_connection_zone_events_status)
            self.app.method.checkBox("OFF", Sensor_activation_Bell_mode_zone_events_click,
                                     Sensor_activation_Bell_mode_zone_events_status)
            if type_control != 'SMS Эгида':
                self.app.method.checkBox("OFF", water_sensor_loop_breakage_click, water_sensor_loop_breakage_status)
        elif type_control == 'DC09':
            self.app.method.checkBox("OFF", water_sensor_loop_breakage_click, water_sensor_loop_breakage_status)

    # Проверка Выключение тумблеров События зон - сохранение
    def assert_tumblers_zone_events_save_off(self, type_control):
        self.app.method.assertCheckBox("OFF", zone_events_device_status)
        self.app.method.assertCheckBox("OFF", Battery_OK_zone_events_device_status)
        self.app.method.assertCheckBox("OFF", ready_status)
        self.app.method.assertCheckBox("OFF", Case_closed_status)
        self.app.method.assertCheckBox("OFF", Case_open_status)
        self.app.method.assertCheckBox("OFF", Low_battery_zone_events_status)
        self.app.method.assertCheckBox("OFF", Backup_battery_error_zone_events_status)
        self.app.method.assertCheckBox("OFF", Device_error_zone_events_status)
        self.app.method.assertCheckBox("OFF", Sensor_reset_zone_events_status)
        self.app.method.assertCheckBox("OFF", Lost_zone_events_status)
        self.app.method.assertCheckBox("OFF", Backup_battery_is_OK_zone_events_status)
        self.app.method.assertCheckBox("OFF", Sabotage_zone_events_status)
        self.app.method.assertCheckBox("OFF", Communication_restored_zone_events_status)
        self.app.method.assertCheckBox("OFF", Humidity_event_zone_events_status)
        self.app.method.assertCheckBox("OFF", CO_sensor_event_zone_events_status)
        self.app.method.assertCheckBox("OFF", Temperature_event_zone_events_status)
        self.app.method.assertCheckBox("OFF", SS_is_normal_zone_events_status)
        self.app.method.assertCheckBox("OFF", AL_is_closed_zone_events_status)
        self.app.method.assertCheckBox("OFF", AL_interrupted_zone_events_status)
        if type_control == 'Звонок' or type_control == 'SMS пользователю' or type_control == 'SMS Эгида':
            self.app.method.assertCheckBox("OFF", Check_connection_zone_events_status)
            self.app.method.assertCheckBox("OFF", Sensor_activation_Bell_mode_zone_events_status)
            if type_control != 'SMS Эгида':
                self.app.method.assertCheckBox("OFF", water_sensor_loop_breakage_status)
        elif type_control == 'DC09':
            self.app.method.assertCheckBox("OFF", water_sensor_loop_breakage_status)

    # Частичное включение тумблеров События зон - сохранение - 1
    def tumblers_zone_events_save_some_1(self, type_control):
        self.app.method.checkBox("OFF", zone_events_device_click, zone_events_device_status)
        self.app.method.checkBox("ON", Battery_OK_zone_events_device_click, Battery_OK_zone_events_device_status)
        self.app.method.checkBox("OFF", ready_click, ready_status)
        self.app.method.checkBox("ON", Case_closed_click, Case_closed_status)
        self.app.method.checkBox("OFF", Case_open_click, Case_open_status)
        self.app.method.checkBox("ON", Low_battery_zone_events_click, Low_battery_zone_events_status)
        self.app.method.checkBox("ON", Backup_battery_error_zone_events_click, Backup_battery_error_zone_events_status)
        self.app.method.checkBox("OFF", Device_error_zone_events_click, Device_error_zone_events_status)
        self.app.method.checkBox("ON", Sensor_reset_zone_events_click, Sensor_reset_zone_events_status)
        self.app.method.checkBox("OFF", Lost_zone_events_click, Lost_zone_events_status)
        self.app.method.checkBox("OFF", Backup_battery_is_OK_zone_events_click, Backup_battery_is_OK_zone_events_status)
        self.app.method.checkBox("ON", Sabotage_zone_events_click, Sabotage_zone_events_status)
        self.app.method.checkBox("OFF", Communication_restored_zone_events_click,
                                 Communication_restored_zone_events_status)
        self.app.method.checkBox("ON", Humidity_event_zone_events_click, Humidity_event_zone_events_status)
        self.app.method.checkBox("OFF", CO_sensor_event_zone_events_click, CO_sensor_event_zone_events_status)
        self.app.method.checkBox("ON", Temperature_event_zone_events_click, Temperature_event_zone_events_status)
        self.app.method.checkBox("ON", SS_is_normal_zone_events_click, SS_is_normal_zone_events_status)
        self.app.method.checkBox("OFF", AL_is_closed_zone_events_click, AL_is_closed_zone_events_status)
        self.app.method.checkBox("ON", AL_interrupted_zone_events_click, AL_interrupted_zone_events_status)
        if type_control == 'Звонок' or type_control == 'SMS пользователю' or type_control == 'SMS Эгида':
            self.app.method.checkBox("OFF", Check_connection_zone_events_click, Check_connection_zone_events_status)
            self.app.method.checkBox("ON", Sensor_activation_Bell_mode_zone_events_click,
                                     Sensor_activation_Bell_mode_zone_events_status)
            if type_control != 'SMS Эгида':
                self.app.method.checkBox("OFF", water_sensor_loop_breakage_click, water_sensor_loop_breakage_status)
        elif type_control == 'DC09':
            self.app.method.checkBox("ON", water_sensor_loop_breakage_click, water_sensor_loop_breakage_status)

    # Проверка частичного включение тумблеров События зон - сохранение - 1
    def assert_tumblers_zone_events_save_some_1(self, type_control):
        self.app.method.assertCheckBox("OFF", zone_events_device_status)
        self.app.method.assertCheckBox("ON", Battery_OK_zone_events_device_status)
        self.app.method.assertCheckBox("OFF", ready_status)
        self.app.method.assertCheckBox("ON", Case_closed_status)
        self.app.method.assertCheckBox("OFF", Case_open_status)
        self.app.method.assertCheckBox("ON", Low_battery_zone_events_status)
        self.app.method.assertCheckBox("ON", Backup_battery_error_zone_events_status)
        self.app.method.assertCheckBox("OFF", Device_error_zone_events_status)
        self.app.method.assertCheckBox("ON", Sensor_reset_zone_events_status)
        self.app.method.assertCheckBox("OFF", Lost_zone_events_status)
        self.app.method.assertCheckBox("OFF", Backup_battery_is_OK_zone_events_status)
        self.app.method.assertCheckBox("ON", Sabotage_zone_events_status)
        self.app.method.assertCheckBox("OFF", Communication_restored_zone_events_status)
        self.app.method.assertCheckBox("ON", Humidity_event_zone_events_status)
        self.app.method.assertCheckBox("OFF", CO_sensor_event_zone_events_status)
        self.app.method.assertCheckBox("ON", Temperature_event_zone_events_status)
        self.app.method.assertCheckBox("ON", SS_is_normal_zone_events_status)
        self.app.method.assertCheckBox("OFF", AL_is_closed_zone_events_status)
        self.app.method.assertCheckBox("ON", AL_interrupted_zone_events_status)
        if type_control == 'Звонок' or type_control == 'SMS пользователю' or type_control == 'SMS Эгида':
            self.app.method.assertCheckBox("OFF", Check_connection_zone_events_status)
            self.app.method.assertCheckBox("ON", Sensor_activation_Bell_mode_zone_events_status)
            if type_control != 'SMS Эгида':
                self.app.method.assertCheckBox("OFF", water_sensor_loop_breakage_status)
        elif type_control == 'DC09':
            self.app.method.assertCheckBox("ON", water_sensor_loop_breakage_status)

    # Частичное включение тумблеров События зон - сохранение - 2
    def tumblers_zone_events_save_some_2(self, type_control):
        self.app.method.checkBox("OFF", zone_events_device_click, zone_events_device_status)
        self.app.method.checkBox("OFF", Battery_OK_zone_events_device_click, Battery_OK_zone_events_device_status)
        self.app.method.checkBox("ON", ready_click, ready_status)
        self.app.method.checkBox("OFF", Case_closed_click, Case_closed_status)
        self.app.method.checkBox("ON", Case_open_click, Case_open_status)
        self.app.method.checkBox("OFF", Low_battery_zone_events_click, Low_battery_zone_events_status)
        self.app.method.checkBox("OFF", Backup_battery_error_zone_events_click, Backup_battery_error_zone_events_status)
        self.app.method.checkBox("ON", Device_error_zone_events_click, Device_error_zone_events_status)
        self.app.method.checkBox("OFF", Sensor_reset_zone_events_click, Sensor_reset_zone_events_status)
        self.app.method.checkBox("ON", Lost_zone_events_click, Lost_zone_events_status)
        self.app.method.checkBox("ON", Backup_battery_is_OK_zone_events_click, Backup_battery_is_OK_zone_events_status)
        self.app.method.checkBox("OFF", Sabotage_zone_events_click, Sabotage_zone_events_status)
        self.app.method.checkBox("ON", Communication_restored_zone_events_click,
                                 Communication_restored_zone_events_status)
        self.app.method.checkBox("OFF", Humidity_event_zone_events_click, Humidity_event_zone_events_status)
        self.app.method.checkBox("ON", CO_sensor_event_zone_events_click, CO_sensor_event_zone_events_status)
        self.app.method.checkBox("OFF", Temperature_event_zone_events_click, Temperature_event_zone_events_status)
        self.app.method.checkBox("OFF", SS_is_normal_zone_events_click, SS_is_normal_zone_events_status)
        self.app.method.checkBox("ON", AL_is_closed_zone_events_click, AL_is_closed_zone_events_status)
        self.app.method.checkBox("OFF", AL_interrupted_zone_events_click, AL_interrupted_zone_events_status)
        if type_control == 'Звонок' or type_control == 'SMS пользователю' or type_control == 'SMS Эгида':
            self.app.method.checkBox("ON", Check_connection_zone_events_click, Check_connection_zone_events_status)
            self.app.method.checkBox("OFF", Sensor_activation_Bell_mode_zone_events_click,
                                     Sensor_activation_Bell_mode_zone_events_status)
            if type_control != 'SMS Эгида':
                self.app.method.checkBox("ON", water_sensor_loop_breakage_click, water_sensor_loop_breakage_status)
        elif type_control == 'DC09':
            self.app.method.checkBox("OFF", water_sensor_loop_breakage_click, water_sensor_loop_breakage_status)

    # Проверка частичного включение тумблеров События зон - сохранение - 2
    def assert_tumblers_zone_events_save_some_2(self, type_control):
        self.app.method.assertCheckBox("OFF", zone_events_device_status)
        self.app.method.assertCheckBox("OFF", Battery_OK_zone_events_device_status)
        self.app.method.assertCheckBox("ON", ready_status)
        self.app.method.assertCheckBox("OFF", Case_closed_status)
        self.app.method.assertCheckBox("ON", Case_open_status)
        self.app.method.assertCheckBox("OFF", Low_battery_zone_events_status)
        self.app.method.assertCheckBox("OFF", Backup_battery_error_zone_events_status)
        self.app.method.assertCheckBox("ON", Device_error_zone_events_status)
        self.app.method.assertCheckBox("OFF", Sensor_reset_zone_events_status)
        self.app.method.assertCheckBox("ON", Lost_zone_events_status)
        self.app.method.assertCheckBox("ON", Backup_battery_is_OK_zone_events_status)
        self.app.method.assertCheckBox("OFF", Sabotage_zone_events_status)
        self.app.method.assertCheckBox("ON", Communication_restored_zone_events_status)
        self.app.method.assertCheckBox("OFF", Humidity_event_zone_events_status)
        self.app.method.assertCheckBox("ON", CO_sensor_event_zone_events_status)
        self.app.method.assertCheckBox("OFF", Temperature_event_zone_events_status)
        self.app.method.assertCheckBox("OFF", SS_is_normal_zone_events_status)
        self.app.method.assertCheckBox("ON", AL_is_closed_zone_events_status)
        self.app.method.assertCheckBox("OFF", AL_interrupted_zone_events_status)
        if type_control == 'Звонок' or type_control == 'SMS пользователю' or type_control == 'SMS Эгида':
            self.app.method.assertCheckBox("ON", Check_connection_zone_events_status)
            self.app.method.assertCheckBox("OFF", Sensor_activation_Bell_mode_zone_events_status)
            if type_control != 'SMS Эгида':
                self.app.method.assertCheckBox("ON", water_sensor_loop_breakage_status)
        elif type_control == 'DC09':
            self.app.method.assertCheckBox("OFF", water_sensor_loop_breakage_status)

    # Включение основного тумблеров События зон - сохранение
    def tumblers_zone_events_save_on_main(self):
        self.app.method.checkBox("ON", zone_events_device_click, zone_events_device_status)

    # Включение тумблеров Питание прибора - сохранение
    def tumblers_instrument_power_supply_save_on(self, type_control):
        self.app.method.checkBox("OFF", Take_all_power_device_click, Take_all_power_device_status)
        self.app.method.checkBox("ON", Battery_is_OK_click, Battery_is_OK_status)
        self.app.method.checkBox("ON", The_battery_is_charging_click, The_battery_is_charging_status)
        self.app.method.checkBox("ON", Battery_is_charged_click, Battery_is_charged_status)
        self.app.method.checkBox("ON", Battery_not_connected_or_connected_incorrectly_click,
                                 Battery_not_connected_or_connected_incorrectly_status)
        self.app.method.checkBox("ON", Battery_low_click, Battery_low_status)
        self.app.method.checkBox("ON", High_internal_battery_resistance_click, High_internal_battery_resistance_status)
        self.app.method.checkBox("ON", Mains_power_is_OK_click, Mains_power_is_OK_status)
        self.app.method.checkBox("ON", Mains_power_off_click, Mains_power_off_status)
        if type_control != 'SMS Эгида':
            self.app.method.checkBox("ON", max_voltage_power_click, max_voltage_power_status)
            self.app.method.checkBox("ON", min_voltage_power_click, min_voltage_power_status)

    # Проверка включение тумблеров Питание прибора - сохранение
    def assert_tumblers_instrument_power_supply_save_on(self, type_control):
        self.app.method.assertCheckBox("ON", Take_all_power_device_status)
        self.app.method.assertCheckBox("ON", Battery_is_OK_status)
        self.app.method.assertCheckBox("ON", The_battery_is_charging_status)
        self.app.method.assertCheckBox("ON", Battery_is_charged_status)
        self.app.method.assertCheckBox("ON", Battery_not_connected_or_connected_incorrectly_status)
        self.app.method.assertCheckBox("ON", Battery_low_status)
        self.app.method.assertCheckBox("ON", High_internal_battery_resistance_status)
        self.app.method.assertCheckBox("ON", Mains_power_is_OK_status)
        self.app.method.assertCheckBox("ON", Mains_power_off_status)
        if type_control != 'SMS Эгида':
            self.app.method.assertCheckBox("ON", max_voltage_power_status)
            self.app.method.assertCheckBox("ON", min_voltage_power_status)

    # Выключение тумблеров Питание прибора - сохранение
    def tumblers_instrument_power_supply_save_off(self, type_control):
        self.app.method.checkBox("ON", Take_all_power_device_click, Take_all_power_device_status)
        self.app.method.checkBox("OFF", Battery_is_OK_click, Battery_is_OK_status)
        self.app.method.checkBox("OFF", The_battery_is_charging_click, The_battery_is_charging_status)
        self.app.method.checkBox("OFF", Battery_is_charged_click, Battery_is_charged_status)
        self.app.method.checkBox("OFF", Battery_not_connected_or_connected_incorrectly_click,
                                 Battery_not_connected_or_connected_incorrectly_status)
        self.app.method.checkBox("OFF", Battery_low_click, Battery_low_status)
        self.app.method.checkBox("OFF", High_internal_battery_resistance_click, High_internal_battery_resistance_status)
        self.app.method.checkBox("OFF", Mains_power_is_OK_click, Mains_power_is_OK_status)
        self.app.method.checkBox("OFF", Mains_power_off_click, Mains_power_off_status)
        if type_control != 'SMS Эгида':
            self.app.method.checkBox("OFF", max_voltage_power_click, max_voltage_power_status)
            self.app.method.checkBox("OFF", min_voltage_power_click, min_voltage_power_status)

    # Проверка выключение тумблеров Питание прибора - сохранение
    def assert_tumblers_instrument_power_supply_save_off(self, type_control):
        self.app.method.assertCheckBox("OFF", Take_all_power_device_status)
        self.app.method.assertCheckBox("OFF", Battery_is_OK_status)
        self.app.method.assertCheckBox("OFF", The_battery_is_charging_status)
        self.app.method.assertCheckBox("OFF", Battery_is_charged_status)
        self.app.method.assertCheckBox("OFF", Battery_not_connected_or_connected_incorrectly_status)
        self.app.method.assertCheckBox("OFF", Battery_low_status)
        self.app.method.assertCheckBox("OFF", High_internal_battery_resistance_status)
        self.app.method.assertCheckBox("OFF", Mains_power_is_OK_status)
        self.app.method.assertCheckBox("OFF", Mains_power_off_status)
        if type_control != 'SMS Эгида':
            self.app.method.assertCheckBox("OFF", max_voltage_power_status)
            self.app.method.assertCheckBox("OFF", min_voltage_power_status)

    # Частичное включение тумблеров Питание прибора - сохранение
    def tumblers_instrument_power_supply_save_on_some_1(self, type_control):
        self.app.method.checkBox("OFF", Take_all_power_device_click, Take_all_power_device_status)
        self.app.method.checkBox("ON", Battery_is_OK_click, Battery_is_OK_status)
        self.app.method.checkBox("OFF", The_battery_is_charging_click, The_battery_is_charging_status)
        self.app.method.checkBox("ON", Battery_is_charged_click, Battery_is_charged_status)
        self.app.method.checkBox("OFF", Battery_not_connected_or_connected_incorrectly_click,
                                 Battery_not_connected_or_connected_incorrectly_status)
        self.app.method.checkBox("ON", Battery_low_click, Battery_low_status)
        self.app.method.checkBox("OFF", High_internal_battery_resistance_click, High_internal_battery_resistance_status)
        self.app.method.checkBox("ON", Mains_power_is_OK_click, Mains_power_is_OK_status)
        self.app.method.checkBox("OFF", Mains_power_off_click, Mains_power_off_status)
        if type_control != 'SMS Эгида':
            self.app.method.checkBox("OFF", max_voltage_power_click, max_voltage_power_status)
            self.app.method.checkBox("ON", min_voltage_power_click, min_voltage_power_status)

    # Проверка частичного включение тумблеров Питание прибора - сохранение
    def assert_tumblers_instrument_power_supply_save_on_some_1(self, type_control):
        self.app.method.assertCheckBox("OFF", Take_all_power_device_status)
        self.app.method.assertCheckBox("ON", Battery_is_OK_status)
        self.app.method.assertCheckBox("OFF", The_battery_is_charging_status)
        self.app.method.assertCheckBox("ON", Battery_is_charged_status)
        self.app.method.assertCheckBox("OFF", Battery_not_connected_or_connected_incorrectly_status)
        self.app.method.assertCheckBox("ON", Battery_low_status)
        self.app.method.assertCheckBox("OFF", High_internal_battery_resistance_status)
        self.app.method.assertCheckBox("ON", Mains_power_is_OK_status)
        self.app.method.assertCheckBox("OFF", Mains_power_off_status)
        if type_control != 'SMS Эгида':
            self.app.method.assertCheckBox("OFF", max_voltage_power_status)
            self.app.method.assertCheckBox("ON", min_voltage_power_status)

    # Частичное включение тумблеров Питание прибора - сохранение
    def tumblers_instrument_power_supply_save_on_some_2(self, type_control):
        self.app.method.checkBox("OFF", Take_all_power_device_click, Take_all_power_device_status)
        self.app.method.checkBox("OFF", Battery_is_OK_click, Battery_is_OK_status)
        self.app.method.checkBox("ON", The_battery_is_charging_click, The_battery_is_charging_status)
        self.app.method.checkBox("OFF", Battery_is_charged_click, Battery_is_charged_status)
        self.app.method.checkBox("ON", Battery_not_connected_or_connected_incorrectly_click,
                                 Battery_not_connected_or_connected_incorrectly_status)
        self.app.method.checkBox("OFF", Battery_low_click, Battery_low_status)
        self.app.method.checkBox("ON", High_internal_battery_resistance_click, High_internal_battery_resistance_status)
        self.app.method.checkBox("OFF", Mains_power_is_OK_click, Mains_power_is_OK_status)
        self.app.method.checkBox("ON", Mains_power_off_click, Mains_power_off_status)
        if type_control != 'SMS Эгида':
            self.app.method.checkBox("ON", max_voltage_power_click, max_voltage_power_status)
            self.app.method.checkBox("OFF", min_voltage_power_click, min_voltage_power_status)

    # Проверка частичного включение тумблеров Питание прибора - сохранение
    def assert_tumblers_instrument_power_supply_save_on_some_2(self, type_control):
        self.app.method.assertCheckBox("OFF", Take_all_power_device_status)
        self.app.method.assertCheckBox("OFF", Battery_is_OK_status)
        self.app.method.assertCheckBox("ON", The_battery_is_charging_status)
        self.app.method.assertCheckBox("OFF", Battery_is_charged_status)
        self.app.method.assertCheckBox("ON", Battery_not_connected_or_connected_incorrectly_status)
        self.app.method.assertCheckBox("OFF", Battery_low_status)
        self.app.method.assertCheckBox("ON", High_internal_battery_resistance_status)
        self.app.method.assertCheckBox("OFF", Mains_power_is_OK_status)
        self.app.method.assertCheckBox("ON", Mains_power_off_status)
        if type_control != 'SMS Эгида':
            self.app.method.assertCheckBox("ON", max_voltage_power_status)
            self.app.method.assertCheckBox("OFF", min_voltage_power_status)

    # Включение тумблера Питание прибора - сохранение
    def tumblers_instrument_power_supply_save_main(self):
        self.app.method.checkBox("ON", Take_all_power_device_click, Take_all_power_device_status)

    # Включение тумблеров Системные события прибора - сохранение
    def tumblers_instrument_system_events_save_on(self, type_control):
        self.app.method.checkBox("OFF", instrument_system_events_click, instrument_system_events_status)
        self.app.method.checkBox("ON", Opening_the_case_of_the_device_click, Opening_the_case_of_the_device_status)
        self.app.method.checkBox("ON", Closing_the_instrument_housing_click, Closing_the_instrument_housing_status)
        if type_control != 'DC09':
            self.app.method.checkBox("ON", The_device_has_been_rebooted_click, The_device_has_been_rebooted_status)
            if type_control != 'SMS Эгида':
                self.app.method.checkBox("ON", sim_card_balance_reduced_click, sim_card_balance_reduced_status)
                self.app.method.checkBox("ON", added_sensor_click, added_sensor_status)
                self.app.method.checkBox("ON", user_added_or_changed_click, user_added_or_changed_status)
                self.app.method.checkBox("ON", key_added_click, key_added_status)
                self.app.method.checkBox("ON", added_or_changed_direction_click, added_or_changed_direction_status)
                self.app.method.checkBox("ON", key_updated_click, key_updated_status)
                self.app.method.checkBox("ON", sensor_removed_click, sensor_removed_status)
                self.app.method.checkBox("ON", key_removed_click, key_removed_status)
                self.app.method.checkBox("ON", user_removed_click, user_removed_status)

    # Проверка включения тумблеров Системные события прибора - сохранение
    def assert_tumblers_instrument_system_events_save_on(self, type_control):
        self.app.method.assertCheckBox("ON", instrument_system_events_status)
        self.app.method.assertCheckBox("ON", Opening_the_case_of_the_device_status)
        self.app.method.assertCheckBox("ON", Closing_the_instrument_housing_status)
        if type_control != 'DC09':
            self.app.method.checkBox("ON", The_device_has_been_rebooted_click, The_device_has_been_rebooted_status)
            if type_control != 'SMS Эгида':
                self.app.method.assertCheckBox("ON", sim_card_balance_reduced_status)
                self.app.method.assertCheckBox("ON", added_sensor_status)
                self.app.method.assertCheckBox("ON", user_added_or_changed_status)
                self.app.method.assertCheckBox("ON", key_added_status)
                self.app.method.assertCheckBox("ON", added_or_changed_direction_status)
                self.app.method.assertCheckBox("ON", key_updated_status)
                self.app.method.assertCheckBox("ON", sensor_removed_status)
                self.app.method.assertCheckBox("ON", key_removed_status)
                self.app.method.assertCheckBox("ON", user_removed_status)

    # Выключение тумблеров Системные события прибора - сохранение
    def tumblers_instrument_system_events_save_off(self, type_control):
        self.app.method.checkBox("ON", instrument_system_events_click, instrument_system_events_status)
        self.app.method.checkBox("OFF", Opening_the_case_of_the_device_click, Opening_the_case_of_the_device_status)
        self.app.method.checkBox("OFF", Closing_the_instrument_housing_click, Closing_the_instrument_housing_status)
        if type_control != 'DC09':
            self.app.method.checkBox("OF", The_device_has_been_rebooted_click, The_device_has_been_rebooted_status)
            if type_control != 'SMS Эгида':
                self.app.method.checkBox("OFF", sim_card_balance_reduced_click, sim_card_balance_reduced_status)
                self.app.method.checkBox("OFF", added_sensor_click, added_sensor_status)
                self.app.method.checkBox("OFF", user_added_or_changed_click, user_added_or_changed_status)
                self.app.method.checkBox("OFF", key_added_click, key_added_status)
                self.app.method.checkBox("OFF", added_or_changed_direction_click, added_or_changed_direction_status)
                self.app.method.checkBox("OFF", key_updated_click, key_updated_status)
                self.app.method.checkBox("OFF", sensor_removed_click, sensor_removed_status)
                self.app.method.checkBox("OFF", key_removed_click, key_removed_status)
                self.app.method.checkBox("OFF", user_removed_click, user_removed_status)

    # Проверка выключения тумблеров Системные события прибора - сохранение
    def assert_tumblers_instrument_system_events_save_off(self, type_control):
        self.app.method.assertCheckBox("OFF", instrument_system_events_status)
        self.app.method.assertCheckBox("OFF", Opening_the_case_of_the_device_status)
        self.app.method.assertCheckBox("OFF", Closing_the_instrument_housing_status)
        if type_control != 'DC09':
            self.app.method.checkBox("OF", The_device_has_been_rebooted_click, The_device_has_been_rebooted_status)
            if type_control != 'SMS Эгида':
                self.app.method.assertCheckBox("OFF", sim_card_balance_reduced_status)
                self.app.method.assertCheckBox("OFF", added_sensor_status)
                self.app.method.assertCheckBox("OFF", user_added_or_changed_status)
                self.app.method.assertCheckBox("OFF", key_added_status)
                self.app.method.assertCheckBox("OFF", added_or_changed_direction_status)
                self.app.method.assertCheckBox("OFF", key_updated_status)
                self.app.method.assertCheckBox("OFF", sensor_removed_status)
                self.app.method.assertCheckBox("OFF", key_removed_status)
                self.app.method.assertCheckBox("OFF", user_removed_status)

    # Частичное включение тумблеров Системные события прибора - сохранение
    def tumblers_instrument_system_events_save_on_some_1(self, type_control):
        self.app.method.checkBox("OFF", instrument_system_events_click, instrument_system_events_status)
        self.app.method.checkBox("ON", Opening_the_case_of_the_device_click, Opening_the_case_of_the_device_status)
        self.app.method.checkBox("OFF", Closing_the_instrument_housing_click, Closing_the_instrument_housing_status)
        if type_control != 'DC09':
            self.app.method.checkBox("ON", The_device_has_been_rebooted_click, The_device_has_been_rebooted_status)
            if type_control != 'SMS Эгида':
                self.app.method.checkBox("ON", sim_card_balance_reduced_click, sim_card_balance_reduced_status)
                self.app.method.checkBox("OFF", added_sensor_click, added_sensor_status)
                self.app.method.checkBox("ON", user_added_or_changed_click, user_added_or_changed_status)
                self.app.method.checkBox("OFF", key_added_click, key_added_status)
                self.app.method.checkBox("ON", added_or_changed_direction_click, added_or_changed_direction_status)
                self.app.method.checkBox("OFF", key_updated_click, key_updated_status)
                self.app.method.checkBox("ON", sensor_removed_click, sensor_removed_status)
                self.app.method.checkBox("OFF", key_removed_click, key_removed_status)
                self.app.method.checkBox("ON", user_removed_click, user_removed_status)

    # Проверка Частичного включения тумблеров Системные события прибора - сохранение
    def assert_tumblers_instrument_system_events_save_on_some_1(self, type_control):
        self.app.method.assertCheckBox("OFF", instrument_system_events_status)
        self.app.method.assertCheckBox("ON", Opening_the_case_of_the_device_status)
        self.app.method.assertCheckBox("OFF", Closing_the_instrument_housing_status)
        if type_control != 'DC09':
            self.app.method.checkBox("ON", The_device_has_been_rebooted_click, The_device_has_been_rebooted_status)
            if type_control != 'SMS Эгида':
                self.app.method.assertCheckBox("ON", sim_card_balance_reduced_status)
                self.app.method.assertCheckBox("OFF", added_sensor_status)
                self.app.method.assertCheckBox("ON", user_added_or_changed_status)
                self.app.method.assertCheckBox("OFF", key_added_status)
                self.app.method.assertCheckBox("ON", added_or_changed_direction_status)
                self.app.method.assertCheckBox("OFF", key_updated_status)
                self.app.method.assertCheckBox("ON", sensor_removed_status)
                self.app.method.assertCheckBox("OFF", key_removed_status)
                self.app.method.assertCheckBox("ON", user_removed_status)

    # Частичное включение тумблеров Системные события прибора - сохранение
    def tumblers_instrument_system_events_save_on_some_2(self, type_control):
        self.app.method.checkBox("OFF", instrument_system_events_click, instrument_system_events_status)
        self.app.method.checkBox("ON", Opening_the_case_of_the_device_click, Opening_the_case_of_the_device_status)
        self.app.method.checkBox("OFF", Closing_the_instrument_housing_click, Closing_the_instrument_housing_status)
        if type_control != 'DC09':
            self.app.method.checkBox("ON", The_device_has_been_rebooted_click, The_device_has_been_rebooted_status)
            if type_control != 'SMS Эгида':
                self.app.method.checkBox("ON", sim_card_balance_reduced_click, sim_card_balance_reduced_status)
                self.app.method.checkBox("OFF", added_sensor_click, added_sensor_status)
                self.app.method.checkBox("ON", user_added_or_changed_click, user_added_or_changed_status)
                self.app.method.checkBox("OFF", key_added_click, key_added_status)
                self.app.method.checkBox("ON", added_or_changed_direction_click, added_or_changed_direction_status)
                self.app.method.checkBox("OFF", key_updated_click, key_updated_status)
                self.app.method.checkBox("ON", sensor_removed_click, sensor_removed_status)
                self.app.method.checkBox("OFF", key_removed_click, key_removed_status)
                self.app.method.checkBox("ON", user_removed_click, user_removed_status)

    # Проверка Частичного включения тумблеров Системные события прибора - сохранение
    def assert_tumblers_instrument_system_events_save_on_some_2(self, type_control):
        self.app.method.assertCheckBox("OFF", instrument_system_events_status)
        self.app.method.assertCheckBox("ON", Opening_the_case_of_the_device_status)
        self.app.method.assertCheckBox("OFF", Closing_the_instrument_housing_status)
        if type_control != 'DC09':
            self.app.method.checkBox("ON", The_device_has_been_rebooted_click, The_device_has_been_rebooted_status)
            if type_control != 'SMS Эгида':
                self.app.method.assertCheckBox("ON", sim_card_balance_reduced_status)
                self.app.method.assertCheckBox("OFF", added_sensor_status)
                self.app.method.assertCheckBox("ON", user_added_or_changed_status)
                self.app.method.assertCheckBox("OFF", key_added_status)
                self.app.method.assertCheckBox("ON", added_or_changed_direction_status)
                self.app.method.assertCheckBox("OFF", key_updated_status)
                self.app.method.assertCheckBox("ON", sensor_removed_status)
                self.app.method.assertCheckBox("OFF", key_removed_status)
                self.app.method.assertCheckBox("ON", user_removed_status)

    # Включение основного тумблера Системные события прибора - сохранение
    def tumblers_instrument_system_events_save_main(self):
        self.app.method.checkBox("ON", instrument_system_events_click, instrument_system_events_status)

    # Ввод данных для сохранения поле Название
    def input_destination_name_for_save(self, locator=destination_name):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        self.app.method.inputValues(_directions['Name_direction'], locator)

    # Проверка сохранения поле Название
    def assert_input_destination_name_for_save(self, locator=destination_name):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        self.app.method.assertValues(_directions['Name_direction'], locator)

    # Выбор из выпадающего списка наименования для сохранения
    def path_select(self):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
            path = _directions['pathList']
            self.app.method.close_cross(path_main)
            self.app.method.click((By.XPATH, f'/html/body//div[@class="b-multiselect-item"]/span[.="{path}"]'))
            self.app.method.click((By.XPATH, path_main))

    # Проверка выбора из выпадающего списка для сохранения
    def assert_path_select_save(self):
        wd = self.app.wd
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        x = _directions['pathList']
        element = wd.find_element(By.XPATH, path_main).get_property("textContent")
        assert str(x) in str(element), f"\nОжидаемое значение в выпадающем списке: '{x}'\nФактическое: '{element}'"

    # Метод сохранения SMS пользователю - ОСНОВНОЙ
    def save_sms_user_main(self):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Ввод значений в поле Номер телефона - код"):
            self.app.method.inputValues(_directions['Phone_cod'], TEL_COD_main)
        with allure.step("Ввод значений в поле Номер телефона - номер"):
            self.app.method.inputValues(_directions['Phone_number'], TEL_NUM_main)
        with allure.step("Выбор из выпадающего списка Язык"):
            self.app.method.selectDropdownListByName(lang_main, _directions['Lang'])
        with allure.step("Выбор чекбокса Отправлять время события"):
            self.app.method.checkBox(_directions['Send_event_time'], main_Send_event_time_click,
                                     main_Send_event_time_status)
        with allure.step("Выбор чекбокса Отправлять дату события"):
            self.app.method.checkBox(_directions['Send_event_date'], main_Send_event_data_click,
                                     main_Send_event_data_status)
        with allure.step("Ввод значений в поле Таймаут при ошибке"):
            self.app.method.inputValues(_directions['Timeout_on_error'], Timeout_on_error_main)
        with allure.step("Выбор из выпадающего списка Тестировать если"):
            self.app.method.selectDropdownListByName(test_IF_main, _directions['Test_if'])
        with allure.step("Выбор из выпадающего списка Метод тестирования"):
            self.app.method.selectDropdownListByName(test_method_main, _directions['Test_method'])
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(testing_main, 'С интервалом')
        with allure.step("Ввод значений в поле Интервал тестирования"):
            self.app.method.inputValues(_directions['Test_interval'], Test_interval_main)

    # Метод сохранения SMS Эгида - ОСНОВНОЙ
    def save_sms_egida_main(self):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Ввод значений в поле Номер телефона - код"):
            self.app.method.inputValues(_directions['Phone_cod'], TEL_COD_main)
        with allure.step("Ввод значений в поле Номер телефона - номер"):
            self.app.method.inputValues(_directions['Phone_number'], TEL_NUM_main)
        with allure.step("Ввод значений в поле Таймаут при ошибке"):
            self.app.method.inputValues(_directions['Timeout_on_error'], Timeout_on_error_main)
        with allure.step("Выбор из выпадающего списка Тестировать если"):
            self.app.method.selectDropdownListByName(test_IF_sms_egida_main, _directions['Test_if'])
        with allure.step("Выбор из выпадающего списка Метод тестирования"):
            self.app.method.selectDropdownListByName(test_method_sms_egida_main, _directions['Test_method'])
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(testing_sms_egida_main, 'С интервалом')
        with allure.step("Ввод значений в поле Интервал тестирования"):
            self.app.method.inputValues(_directions['Test_interval'], Test_interval_main)

    # Метод сохранения Звонок - ОСНОВНОЙ
    def save_call_main(self):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Ввод значений в поле Номер телефона - код"):
            self.app.method.inputValues(_directions['Phone_cod'], TEL_COD_main)
        with allure.step("Ввод значений в поле Номер телефона - номер"):
            self.app.method.inputValues(_directions['Phone_number'], TEL_NUM_main)
        with allure.step("Ввод значений в поле Количество повторов"):
            self.app.method.inputValues(_directions['Count_rep'], count_reset_main)
        with allure.step("Ввод значений в поле Таймаут при ошибке"):
            self.app.method.inputValues(_directions['Timeout_on_error'], Timeout_on_error_main)
        with allure.step("Выбор из выпадающего списка Тестировать если"):
            self.app.method.selectDropdownListByName(test_IF_sms_egida_main, _directions['Test_if'])
        with allure.step("Выбор из выпадающего списка Метод тестирования"):
            self.app.method.selectDropdownListByName(test_method_sms_egida_main, _directions['Test_method'])
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(testing_sms_egida_main, 'С интервалом')
        with allure.step("Ввод значений в поле Интервал тестирования"):
            self.app.method.inputValues(_directions['Test_interval'], Test_interval_main)

    # Метод сохранения DC09 - ОСНОВНОЙ
    def save_DC09_main(self):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Ввод значений в поле Адрес "):
            self.app.method.inputValues(_directions['DC09_address'], address_DC09_main)
        with allure.step("Ввод значений в поле Порт "):
            self.app.method.inputValues(_directions['DC09_port'], port_DC09_main)
        with allure.step("Выбор из выпадающего списка Канал соединения"):
            self.app.method.selectDropdownListByName(connection_main, _directions['Connection_channel'])
        with allure.step("Ввод значений в поле Таймаут подтверждения, сек"):
            self.app.method.inputValues(_directions['Confirmation_timeout_sec'], confirmation_timeout_DC09_main)
        with allure.step("Ввод значений в поле Количество повторов"):
            self.app.method.inputValues(_directions['Count_rep'], count_reset_main)
        with allure.step("Ввод значений в поле Ключ шифрования"):
            self.app.method.inputValues(_directions['Encryption_key'], encryption_key_DC09_main)
        with allure.step("Ввод значений в поле Таймаут при ошибке"):
            self.app.method.inputValues(_directions['Timeout_on_error'], Timeout_on_error_main)
        with allure.step("Выбор из выпадающего списка Тестировать если"):
            self.app.method.selectDropdownListByName(dc09_test_IF_main, _directions['Test_if'])
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(dc09_testing_main, 'С интервалом')
        with allure.step("Ввод значений в поле Интервал тестирования"):
            self.app.method.inputValues(_directions['Test_interval'], Test_interval_main)

    # Метод сохранения DC09 - Резерв 1
    def save_DC09_rezerv_1(self):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Ввод значений в поле Адрес "):
            self.app.method.inputValues(_directions['DC09_address'], address_DC09_reserv_1)
        with allure.step("Ввод значений в поле Порт "):
            self.app.method.inputValues(_directions['DC09_port'], port_DC09_reserv_1)
        with allure.step("Выбор из выпадающего списка Канал соединения"):
            self.app.method.selectDropdownListByName(connection_rezerv_1, _directions['Connection_channel'])
        with allure.step("Ввод значений в поле Таймаут подтверждения, сек"):
            self.app.method.inputValues(_directions['Confirmation_timeout_sec'], confirmation_timeout_DC09_reserv_1)
        with allure.step("Ввод значений в поле Количество повторов"):
            self.app.method.inputValues(_directions['Count_rep'], count_reset_rezerv_1)
        with allure.step("Ввод значений в поле Ключ шифрования"):
            self.app.method.inputValues(_directions['Encryption_key'], encryption_key_DC09_reserv_1)
        with allure.step("Ввод значений в поле Таймаут при ошибке"):
            self.app.method.inputValues(_directions['Timeout_on_error'], Timeout_on_error_rezerv_1)
        with allure.step("Выбор из выпадающего списка Тестировать если"):
            self.app.method.selectDropdownListByName(dc09_test_IF_rezerv_1, _directions['Test_if'])
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(dc09_testing_rezerv_1, 'С интервалом')
        with allure.step("Ввод значений в поле Интервал тестирования"):
            self.app.method.inputValues(_directions['Test_interval'], Test_interval_rezerv_1)

    # Метод сохранения DC09 - Резерв 2
    def save_DC09_rezerv_2(self):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Ввод значений в поле Адрес "):
            self.app.method.inputValues(_directions['DC09_address'], address_DC09_reserv_2)
        with allure.step("Ввод значений в поле Порт "):
            self.app.method.inputValues(_directions['DC09_port'], port_DC09_reserv_2)
        with allure.step("Выбор из выпадающего списка Канал соединения"):
            self.app.method.selectDropdownListByName(connection_rezerv_2, _directions['Connection_channel'])
        with allure.step("Ввод значений в поле Таймаут подтверждения, сек"):
            self.app.method.inputValues(_directions['Confirmation_timeout_sec'], confirmation_timeout_DC09_reserv_2)
        with allure.step("Ввод значений в поле Количество повторов"):
            self.app.method.inputValues(_directions['Count_rep'], count_reset_rezerv_2)
        with allure.step("Ввод значений в поле Ключ шифрования"):
            self.app.method.inputValues(_directions['Encryption_key'], encryption_key_DC09_reserv_2)
        with allure.step("Ввод значений в поле Таймаут при ошибке"):
            self.app.method.inputValues(_directions['Timeout_on_error'], Timeout_on_error_rezerv_2)
        with allure.step("Выбор из выпадающего списка Тестировать если"):
            self.app.method.selectDropdownListByName(dc09_test_IF_rezerv_1, _directions['Test_if'])
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(dc09_testing_rezerv_1, 'С интервалом')
        with allure.step("Ввод значений в поле Интервал тестирования"):
            self.app.method.inputValues(_directions['Test_interval'], Test_interval_main)

    # Метод сохранения DC09 - ОСНОВНОЙ
    def save_DC09_time_table_main(self):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Ввод значений в поле Адрес "):
            self.app.method.inputValues(_directions['DC09_address'], address_DC09_main)
        with allure.step("Ввод значений в поле Порт "):
            self.app.method.inputValues(_directions['DC09_port'], port_DC09_main)
        with allure.step("Выбор из выпадающего списка Канал соединения"):
            self.app.method.selectDropdownListByName(connection_main, _directions['Connection_channel'])
        with allure.step("Ввод значений в поле Таймаут подтверждения, сек"):
            self.app.method.inputValues(_directions['Confirmation_timeout_sec'], confirmation_timeout_DC09_main)
        with allure.step("Ввод значений в поле Количество повторов"):
            self.app.method.inputValues(_directions['Count_rep'], count_reset_main)
        with allure.step("Ввод значений в поле Ключ шифрования"):
            self.app.method.inputValues(_directions['Encryption_key'], encryption_key_DC09_main)
        with allure.step("Ввод значений в поле Таймаут при ошибке"):
            self.app.method.inputValues(_directions['Timeout_on_error'], Timeout_on_error_main)
        with allure.step("Выбор из выпадающего списка Тестировать если"):
            self.app.method.selectDropdownListByName(dc09_test_IF_main, _directions['Test_if'])
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(dc09_testing_main, 'По расписанию')
        with allure.step("Выбор из выпадающего списка Дни недели"):
            day = _directions['Days_of_the_week']
            self.app.method.close_cross(days_of_the_week_main)
            self.app.method.go_to_element(f'/html/body//div[@class="b-multiselect-item"]/span[.="{day}"]', 'true')
            self.app.method.click((By.XPATH, f'/html/body//div[@class="b-multiselect-item"]/span[.="{day}"]'))
            self.app.method.click((By.XPATH, days_of_the_week_main))
        with allure.step("Выбор времени"):
            time_off = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00',
                        '10:00',
                        '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00',
                        '21:00',
                        '22:00', '23:00']
            for i in time_off:
                self.app.method.TimeBox("OFF", i, '1')
            self.app.method.TimeBox("ON", _directions['Time'], '1')

    # Метод сохранения DC09 - Резерв 1
    def save_DC09_time_table_rezerv_1(self):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Ввод значений в поле Адрес "):
            self.app.method.inputValues(_directions['DC09_address'], address_DC09_reserv_1)
        with allure.step("Ввод значений в поле Порт "):
            self.app.method.inputValues(_directions['DC09_port'], port_DC09_reserv_1)
        with allure.step("Выбор из выпадающего списка Канал соединения"):
            self.app.method.selectDropdownListByName(connection_rezerv_1, _directions['Connection_channel'])
        with allure.step("Ввод значений в поле Таймаут подтверждения, сек"):
            self.app.method.inputValues(_directions['Confirmation_timeout_sec'], confirmation_timeout_DC09_reserv_1)
        with allure.step("Ввод значений в поле Количество повторов"):
            self.app.method.inputValues(_directions['Count_rep'], count_reset_rezerv_1)
        with allure.step("Ввод значений в поле Ключ шифрования"):
            self.app.method.inputValues(_directions['Encryption_key'], encryption_key_DC09_reserv_1)
        with allure.step("Ввод значений в поле Таймаут при ошибке"):
            self.app.method.inputValues(_directions['Timeout_on_error'], Timeout_on_error_rezerv_1)
        with allure.step("Выбор из выпадающего списка Тестировать если"):
            self.app.method.selectDropdownListByName(dc09_test_IF_rezerv_1, _directions['Test_if'])
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(dc09_testing_main, 'С интервалом')
            self.app.method.selectDropdownListByName(dc09_testing_rezerv_1, 'По расписанию')
        with allure.step("Выбор из выпадающего списка Дни недели"):
            day = _directions['Days_of_the_week']
            self.app.method.close_cross(days_of_the_week_main)
            self.app.method.go_to_element(f'/html/body//div[@class="b-multiselect-item"]/span[.="{day}"]', 'true')
            self.app.method.click((By.XPATH, f'/html/body//div[@class="b-multiselect-item"]/span[.="{day}"]'))
            self.app.method.click((By.XPATH, days_of_the_week_main))
        with allure.step("Выбор времени"):
            time_off = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00',
                        '10:00',
                        '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00',
                        '21:00',
                        '22:00', '23:00']
            for i in time_off:
                self.app.method.TimeBox("OFF", i, '1')
            self.app.method.TimeBox("ON", _directions['Time'], '1')

    # Метод сохранения DC09 - Резерв 2
    def save_DC09_time_table_rezerv_2(self):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Ввод значений в поле Адрес "):
            self.app.method.inputValues(_directions['DC09_address'], address_DC09_reserv_2)
        with allure.step("Ввод значений в поле Порт "):
            self.app.method.inputValues(_directions['DC09_port'], port_DC09_reserv_2)
        with allure.step("Выбор из выпадающего списка Канал соединения"):
            self.app.method.selectDropdownListByName(connection_rezerv_2, _directions['Connection_channel'])
        with allure.step("Ввод значений в поле Таймаут подтверждения, сек"):
            self.app.method.inputValues(_directions['Confirmation_timeout_sec'], confirmation_timeout_DC09_reserv_2)
        with allure.step("Ввод значений в поле Количество повторов"):
            self.app.method.inputValues(_directions['Count_rep'], count_reset_rezerv_2)
        with allure.step("Ввод значений в поле Ключ шифрования"):
            self.app.method.inputValues(_directions['Encryption_key'], encryption_key_DC09_reserv_2)
        with allure.step("Ввод значений в поле Таймаут при ошибке"):
            self.app.method.inputValues(_directions['Timeout_on_error'], Timeout_on_error_rezerv_2)
        with allure.step("Выбор из выпадающего списка Тестировать если"):
            self.app.method.selectDropdownListByName(dc09_test_IF_rezerv_1, _directions['Test_if'])
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(dc09_testing_rezerv_1, 'По расписанию')
        with allure.step("Выбор из выпадающего списка Дни недели"):
            day = _directions['Days_of_the_week']
            self.app.method.close_cross(days_of_the_week_main)
            self.app.method.go_to_element(f'/html/body//div[@class="b-multiselect-item"]/span[.="{day}"]', 'true')
            self.app.method.click((By.XPATH, f'/html/body//div[@class="b-multiselect-item"]/span[.="{day}"]'))
            self.app.method.click((By.XPATH, days_of_the_week_main))
        with allure.step("Выбор времени"):
            time_off = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00',
                        '10:00',
                        '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00',
                        '21:00',
                        '22:00', '23:00']
            for i in time_off:
                self.app.method.TimeBox("OFF", i, '1')
            self.app.method.TimeBox("ON", _directions['Time'], '1')

    # Метод сохранения SMS Эгида - Резерв 1
    def save_sms_egida_rezerv_1(self):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Ввод значений в поле Номер телефона - код"):
            self.app.method.inputValues(_directions['Phone_cod'], TEL_COD_rezerv_1)
        with allure.step("Ввод значений в поле Номер телефона - номер"):
            self.app.method.inputValues(_directions['Phone_number'], TEL_NUM_rezerv_1)
        with allure.step("Ввод значений в поле Таймаут при ошибке"):
            self.app.method.inputValues(_directions['Timeout_on_error'], Timeout_on_error_rezerv_1)
        with allure.step("Выбор из выпадающего списка Тестировать если"):
            self.app.method.selectDropdownListByName(test_IF_sms_egidrezerv_1, _directions['Test_if'])
        with allure.step("Выбор из выпадающего списка Метод тестирования"):
            self.app.method.selectDropdownListByName(test_method_sms_egida_rezerv_1, _directions['Test_method'])
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(testing_sms_egida_main, 'С интервалом')
            self.app.method.selectDropdownListByName(testing_sms_egida_rezerv_1, 'С интервалом')
        with allure.step("Ввод значений в поле Интервал тестирования"):
            self.app.method.inputValues(_directions['Test_interval'], Test_interval_rezerv_1)

    # Метод сохранения ЗВОНОК - Резерв 1
    def save_call_rezerv_1(self):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Ввод значений в поле Номер телефона - код"):
            self.app.method.inputValues(_directions['Phone_cod'], TEL_COD_rezerv_1)
        with allure.step("Ввод значений в поле Номер телефона - номер"):
            self.app.method.inputValues(_directions['Phone_number'], TEL_NUM_rezerv_1)
        with allure.step("Ввод значений в поле Количество повторов"):
            self.app.method.inputValues(_directions['Count_rep'], count_reset_rezerv_1)
        with allure.step("Ввод значений в поле Таймаут при ошибке"):
            self.app.method.inputValues(_directions['Timeout_on_error'], Timeout_on_error_rezerv_1)
        with allure.step("Выбор из выпадающего списка Тестировать если"):
            self.app.method.selectDropdownListByName(test_IF_sms_egidrezerv_1, _directions['Test_if'])
        with allure.step("Выбор из выпадающего списка Метод тестирования"):
            self.app.method.selectDropdownListByName(test_method_sms_egida_rezerv_1, _directions['Test_method'])
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(testing_sms_egida_main, 'С интервалом')
            self.app.method.selectDropdownListByName(testing_sms_egida_rezerv_1, 'С интервалом')
        with allure.step("Ввод значений в поле Интервал тестирования"):
            self.app.method.inputValues(_directions['Test_interval'], Test_interval_rezerv_1)

    # Метод сохранения SMS Эгида - Резерв 2
    def save_sms_egida_rezerv_2(self):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Ввод значений в поле Номер телефона - код"):
            self.app.method.inputValues(_directions['Phone_cod'], TEL_COD_rezerv_2)
        with allure.step("Ввод значений в поле Номер телефона - номер"):
            self.app.method.inputValues(_directions['Phone_number'], TEL_NUM_rezerv_2)
        with allure.step("Ввод значений в поле Таймаут при ошибке"):
            self.app.method.inputValues(_directions['Timeout_on_error'], Timeout_on_error_rezerv_2)
        with allure.step("Выбор из выпадающего списка Тестировать если"):
            self.app.method.selectDropdownListByName(test_IF_sms_egidrezerv_2, _directions['Test_if'])
        with allure.step("Выбор из выпадающего списка Метод тестирования"):
            self.app.method.selectDropdownListByName(test_method_sms_egida_rezerv_2, _directions['Test_method'])
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(testing_sms_egida_main, 'С интервалом')
            self.app.method.selectDropdownListByName(testing_sms_egida_rezerv_1, 'С интервалом')
            self.app.method.selectDropdownListByName(testing_sms_egida_rezerv_2, 'С интервалом')
        with allure.step("Ввод значений в поле Интервал тестирования"):
            self.app.method.inputValues(_directions['Test_interval'], Test_interval_rezerv_2)

    # Метод сохранения SMS Эгида - Резерв 2
    def save_call_rezerv_2(self):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Ввод значений в поле Номер телефона - код"):
            self.app.method.inputValues(_directions['Phone_cod'], TEL_COD_rezerv_2)
        with allure.step("Ввод значений в поле Номер телефона - номер"):
            self.app.method.inputValues(_directions['Phone_number'], TEL_NUM_rezerv_2)
        with allure.step("Ввод значений в поле Таймаут при ошибке"):
            self.app.method.inputValues(_directions['Timeout_on_error'], Timeout_on_error_rezerv_2)
        with allure.step("Ввод значений в поле Количество повторов"):
            self.app.method.inputValues(_directions['Count_rep'], count_reset_rezerv_2)
        with allure.step("Выбор из выпадающего списка Тестировать если"):
            self.app.method.selectDropdownListByName(test_IF_sms_egidrezerv_2, _directions['Test_if'])
        with allure.step("Выбор из выпадающего списка Метод тестирования"):
            self.app.method.selectDropdownListByName(test_method_sms_egida_rezerv_2, _directions['Test_method'])
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(testing_sms_egida_main, 'С интервалом')
            self.app.method.selectDropdownListByName(testing_sms_egida_rezerv_1, 'С интервалом')
            self.app.method.selectDropdownListByName(testing_sms_egida_rezerv_2, 'С интервалом')
        with allure.step("Ввод значений в поле Интервал тестирования"):
            self.app.method.inputValues(_directions['Test_interval'], Test_interval_rezerv_2)

    # Метод проверки сохранения SMS пользователю - ОСНОВНОЙ
    def assert_save_sms_user_main(self):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Проверка ввода значений в поле Номер телефона - код"):
            self.app.method.assertValues(_directions['Phone_cod'], TEL_COD_main)
        with allure.step("Проверка ввода значений в поле Номер телефона - номер"):
            self.app.method.assertValuesPhoneNum(_directions['Phone_number'], TEL_NUM_main)
        with allure.step("Проверка выбора из выпадающего списка Язык"):
            self.app.method.assertSelectionDropdownList(_directions['Lang'], lang_main)
        with allure.step("Проверка выбора чек-бокса Отправлять время события"):
            self.app.method.assertCheckBox(_directions['Send_event_time'], main_Send_event_time_status)
        with allure.step("Проверка выбора чек-бокса Отправлять дату события"):
            self.app.method.assertCheckBox(_directions['Send_event_date'], main_Send_event_data_status)
        with allure.step("Проверка ввода значений в поле Таймаут при ошибке"):
            self.app.method.assertValues(_directions['Timeout_on_error'], Timeout_on_error_main)
        with allure.step("Проверка выбора из выпадающего списка Тестировать если"):
            self.app.method.assertSelectionDropdownList(_directions['Test_if'], test_IF_main)
        with allure.step("Проверка выбора из выпадающего списка Метод тестирования"):
            self.app.method.assertSelectionDropdownList(_directions['Test_method'], test_method_main)
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(testing_main, 'С интервалом')
        with allure.step("Проверка ввода значений в поле Интервал тестирования"):
            self.app.method.assertValues(_directions['Test_interval'], Test_interval_main)

    # Метод проверки сохранения SMS Эгида - ОСНОВНОЙ
    def assert_save_sms_egida_main(self):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Проверка ввода значений в поле Номер телефона - код"):
            self.app.method.assertValues(_directions['Phone_cod'], TEL_COD_main)
        with allure.step("Проверка ввода значений в поле Номер телефона - номер"):
            self.app.method.assertValuesPhoneNum(_directions['Phone_number'], TEL_NUM_main)
        with allure.step("Проверка ввода значений в поле Таймаут при ошибке"):
            self.app.method.assertValues(_directions['Timeout_on_error'], Timeout_on_error_main)
        with allure.step("Проверка выбора из выпадающего списка Тестировать если"):
            self.app.method.assertSelectionDropdownList(_directions['Test_if'], test_IF_sms_egida_main)
        with allure.step("Проверка выбора из выпадающего списка Метод тестирования"):
            self.app.method.assertSelectionDropdownList(_directions['Test_method'], test_method_sms_egida_main)
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(testing_sms_egida_main, 'С интервалом')
        with allure.step("Проверка ввода значений в поле Интервал тестирования"):
            self.app.method.assertValues(_directions['Test_interval'], Test_interval_main)

    # Метод проверки сохранения ЗВОНОК - ОСНОВНОЙ
    def assert_save_call_main(self):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Проверка ввода значений в поле Номер телефона - код"):
            self.app.method.assertValues(_directions['Phone_cod'], TEL_COD_main)
        with allure.step("Проверка ввода значений в поле Номер телефона - номер"):
            self.app.method.assertValuesPhoneNum(_directions['Phone_number'], TEL_NUM_main)
        with allure.step("Проверка ввода значений в поле Количество повторов"):
            self.app.method.assertValues(_directions['Count_rep'], count_reset_main)
        with allure.step("Проверка ввода значений в поле Таймаут при ошибке"):
            self.app.method.assertValues(_directions['Timeout_on_error'], Timeout_on_error_main)
        with allure.step("Проверка выбора из выпадающего списка Тестировать если"):
            self.app.method.assertSelectionDropdownList(_directions['Test_if'], test_IF_sms_egida_main)
        with allure.step("Проверка выбора из выпадающего списка Метод тестирования"):
            self.app.method.assertSelectionDropdownList(_directions['Test_method'], test_method_sms_egida_main)
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(testing_sms_egida_main, 'С интервалом')
        with allure.step("Проверка ввода значений в поле Интервал тестирования"):
            self.app.method.assertValues(_directions['Test_interval'], Test_interval_main)

    # Метод проверки сохранения DC09 - ОСНОВНОЙ
    def assert_save_dc09_main(self):
        time.sleep(1)
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Проверка ввода значений в поле Адрес "):
            self.app.method.assertValues(_directions['DC09_address'], address_DC09_main)
        with allure.step("Проверка ввода значений в поле Порт "):
            self.app.method.assertValues(_directions['DC09_port'], port_DC09_main)
        with allure.step("Проверка выбора из выпадающего списка Канал соединения"):
            self.app.method.assertSelectionDropdownList(_directions['Connection_channel'], connection_main)
        with allure.step("Проверка ввода значений в поле Таймаут подтверждения, сек"):
            self.app.method.assertValues(_directions['Confirmation_timeout_sec'], confirmation_timeout_DC09_main)
        with allure.step("Проверка ввода значений в поле Количество повторов"):
            self.app.method.assertValues(_directions['Count_rep'], count_reset_main)
        with allure.step("Проверка ввода значений в поле Ключ шифрования"):
            self.app.method.assertValues(_directions['Encryption_key'], encryption_key_DC09_main)
        with allure.step("Проверка ввода значений в поле Таймаут при ошибке"):
            self.app.method.assertValues(_directions['Timeout_on_error'], Timeout_on_error_main)
        with allure.step("Проверка выбора из выпадающего списка Тестировать если"):
            self.app.method.assertSelectionDropdownList(_directions['Test_if'], dc09_test_IF_main)
        with allure.step("Проверка выбора из выпадающего списка Тестировать"):
            self.app.method.assertSelectionDropdownList('С интервалом', dc09_testing_main)
        with allure.step("Проверка ввода значений в поле Интервал тестирования"):
            self.app.method.assertValues(_directions['Test_interval'], Test_interval_main)

    # Метод проверки сохранения DC09 - Резерв 1
    def assert_save_dc09_rezerv_1(self):
        time.sleep(1)
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Проверка ввода значений в поле Адрес "):
            self.app.method.assertValues(_directions['DC09_address'], address_DC09_reserv_1)
        with allure.step("Проверка ввода значений в поле Порт "):
            self.app.method.assertValues(_directions['DC09_port'], port_DC09_reserv_1)
        with allure.step("Проверка выбора из выпадающего списка Канал соединения"):
            self.app.method.assertSelectionDropdownList(_directions['Connection_channel'], connection_rezerv_1)
        with allure.step("Проверка ввода значений в поле Таймаут подтверждения, сек"):
            self.app.method.assertValues(_directions['Confirmation_timeout_sec'], confirmation_timeout_DC09_reserv_1)
        with allure.step("Проверка ввода значений в поле Количество повторов"):
            self.app.method.assertValues(_directions['Count_rep'], count_reset_rezerv_1)
        with allure.step("Проверка ввода значений в поле Ключ шифрования"):
            self.app.method.assertValues(_directions['Encryption_key'], encryption_key_DC09_reserv_1)
        with allure.step("Проверка ввода значений в поле Таймаут при ошибке"):
            self.app.method.assertValues(_directions['Timeout_on_error'], Timeout_on_error_rezerv_1)
        with allure.step("Проверка выбора из выпадающего списка Тестировать если"):
            self.app.method.assertSelectionDropdownList(_directions['Test_if'], dc09_test_IF_rezerv_1)
        with allure.step("Проверка выбора из выпадающего списка Тестировать"):
            self.app.method.assertSelectionDropdownList('С интервалом', dc09_testing_rezerv_1)
        with allure.step("Проверка ввода значений в поле Интервал тестирования"):
            self.app.method.assertValues(_directions['Test_interval'], Test_interval_rezerv_1)

    # Метод проверки сохранения DC09 - Резерв 2
    def assert_save_dc09_rezerv_2(self):
        time.sleep(1)
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Проверка ввода значений в поле Адрес "):
            self.app.method.assertValues(_directions['DC09_address'], address_DC09_reserv_2)
        with allure.step("Проверка ввода значений в поле Порт "):
            self.app.method.assertValues(_directions['DC09_port'], port_DC09_reserv_2)
        with allure.step("Проверка выбора из выпадающего списка Канал соединения"):
            self.app.method.assertSelectionDropdownList(_directions['Connection_channel'], connection_rezerv_2)
        with allure.step("Проверка ввода значений в поле Таймаут подтверждения, сек"):
            self.app.method.assertValues(_directions['Confirmation_timeout_sec'], confirmation_timeout_DC09_reserv_2)
        with allure.step("Проверка ввода значений в поле Количество повторов"):
            self.app.method.assertValues(_directions['Count_rep'], count_reset_rezerv_2)
        with allure.step("Проверка ввода значений в поле Ключ шифрования"):
            self.app.method.assertValues(_directions['Encryption_key'], encryption_key_DC09_reserv_2)
        with allure.step("Проверка ввода значений в поле Таймаут при ошибке"):
            self.app.method.assertValues(_directions['Timeout_on_error'], Timeout_on_error_rezerv_2)
        with allure.step("Проверка выбора из выпадающего списка Тестировать если"):
            self.app.method.assertSelectionDropdownList(_directions['Test_if'], dc09_test_IF_rezerv_1)
        with allure.step("Проверка выбора из выпадающего списка Тестировать"):
            self.app.method.assertSelectionDropdownList('С интервалом', dc09_testing_rezerv_1)
        with allure.step("Проверка ввода значений в поле Интервал тестирования"):
            self.app.method.assertValues(_directions['Test_interval'], Test_interval_main)

    # Метод проверки сохранения DC09 - ОСНОВНОЙ
    def assert_save_dc09_time_table_main(self):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Проверка ввода значений в поле Адрес "):
            self.app.method.assertValues(_directions['DC09_address'], address_DC09_main)
        with allure.step("Проверка ввода значений в поле Порт "):
            self.app.method.assertValues(_directions['DC09_port'], port_DC09_main)
        with allure.step("Проверка выбора из выпадающего списка Канал соединения"):
            self.app.method.assertSelectionDropdownList(_directions['Connection_channel'], connection_main)
        with allure.step("Проверка ввода значений в поле Таймаут подтверждения, сек"):
            self.app.method.assertValues(_directions['Confirmation_timeout_sec'], confirmation_timeout_DC09_main)
        with allure.step("Проверка ввода значений в поле Количество повторов"):
            self.app.method.assertValues(_directions['Count_rep'], count_reset_main)
        with allure.step("Проверка ввода значений в поле Ключ шифрования"):
            self.app.method.assertValues(_directions['Encryption_key'], encryption_key_DC09_main)
        with allure.step("Проверка ввода значений в поле Таймаут при ошибке"):
            self.app.method.assertValues(_directions['Timeout_on_error'], Timeout_on_error_main)
        with allure.step("Проверка выбора из выпадающего списка Тестировать если"):
            self.app.method.assertSelectionDropdownList(_directions['Test_if'], dc09_test_IF_main)
        with allure.step("Проверка выбора из выпадающего списка Тестировать"):
            self.app.method.assertSelectionDropdownList('По расписанию', dc09_testing_main)
        with allure.step("Проверка выбора из выпадающего списка Дни недели"):
            day = _directions['Days_of_the_week']
            wd = self.app.wd
            element = wd.find_element(By.XPATH, days_of_the_week_main).get_property("textContent")
            assert str(day) in str(
                element), f"\nОжидаемое значение в выпадающем списке: '{day}'\nФактическое: '{element}'"
        with allure.step("Проверка выбора времени"):
            self.app.method.assertTimeBox("ON", _directions['Time'], '1')

    # Метод проверки сохранения DC09 - Резерв 1
    def assert_save_dc09_time_table_rezerv_1(self):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Проверка ввода значений в поле Адрес "):
            self.app.method.assertValues(_directions['DC09_address'], address_DC09_reserv_1)
        with allure.step("Проверка ввода значений в поле Порт "):
            self.app.method.assertValues(_directions['DC09_port'], port_DC09_reserv_1)
        with allure.step("Проверка выбора из выпадающего списка Канал соединения"):
            self.app.method.assertSelectionDropdownList(_directions['Connection_channel'], connection_rezerv_1)
        with allure.step("Проверка ввода значений в поле Таймаут подтверждения, сек"):
            self.app.method.assertValues(_directions['Confirmation_timeout_sec'], confirmation_timeout_DC09_reserv_1)
        with allure.step("Проверка ввода значений в поле Количество повторов"):
            self.app.method.assertValues(_directions['Count_rep'], count_reset_rezerv_1)
        with allure.step("Проверка ввода значений в поле Ключ шифрования"):
            self.app.method.assertValues(_directions['Encryption_key'], encryption_key_DC09_reserv_1)
        with allure.step("Проверка ввода значений в поле Таймаут при ошибке"):
            self.app.method.assertValues(_directions['Timeout_on_error'], Timeout_on_error_rezerv_1)
        with allure.step("Проверка выбора из выпадающего списка Тестировать если"):
            self.app.method.assertSelectionDropdownList(_directions['Test_if'], dc09_test_IF_rezerv_1)
        with allure.step("Проверка выбора из выпадающего списка Тестировать"):
            self.app.method.assertSelectionDropdownList('По расписанию', dc09_testing_rezerv_1)
        with allure.step("Проверка выбора из выпадающего списка Дни недели"):
            day = _directions['Days_of_the_week']
            wd = self.app.wd
            element = wd.find_element(By.XPATH, days_of_the_week_main).get_property("textContent")
            assert str(day) in str(
                element), f"\nОжидаемое значение в выпадающем списке: '{day}'\nФактическое: '{element}'"
        with allure.step("Проверка выбора времени"):
            self.app.method.assertTimeBox("ON", _directions['Time'], '1')

    # Метод проверки сохранения DC09 - Резерв 2
    def assert_save_dc09_time_table_rezerv_2(self):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Проверка ввода значений в поле Адрес "):
            self.app.method.assertValues(_directions['DC09_address'], address_DC09_reserv_2)
        with allure.step("Проверка ввода значений в поле Порт "):
            self.app.method.assertValues(_directions['DC09_port'], port_DC09_reserv_2)
        with allure.step("Проверка выбора из выпадающего списка Канал соединения"):
            self.app.method.assertSelectionDropdownList(_directions['Connection_channel'], connection_rezerv_2)
        with allure.step("Проверка ввода значений в поле Таймаут подтверждения, сек"):
            self.app.method.assertValues(_directions['Confirmation_timeout_sec'], confirmation_timeout_DC09_reserv_2)
        with allure.step("Проверка ввода значений в поле Количество повторов"):
            self.app.method.assertValues(_directions['Count_rep'], count_reset_rezerv_2)
        with allure.step("Проверка ввода значений в поле Ключ шифрования"):
            self.app.method.assertValues(_directions['Encryption_key'], encryption_key_DC09_reserv_2)
        with allure.step("Проверка ввода значений в поле Таймаут при ошибке"):
            self.app.method.assertValues(_directions['Timeout_on_error'], Timeout_on_error_rezerv_2)
        with allure.step("Проверка выбора из выпадающего списка Тестировать если"):
            self.app.method.assertSelectionDropdownList(_directions['Test_if'], dc09_test_IF_rezerv_1)
        with allure.step("Проверка выбора из выпадающего списка Тестировать"):
            self.app.method.assertSelectionDropdownList('По расписанию', dc09_testing_rezerv_1)
        with allure.step("Проверка выбора из выпадающего списка Дни недели"):
            day = _directions['Days_of_the_week']
            wd = self.app.wd
            element = wd.find_element(By.XPATH, days_of_the_week_main).get_property("textContent")
            assert str(day) in str(
                element), f"\nОжидаемое значение в выпадающем списке: '{day}'\nФактическое: '{element}'"
        with allure.step("Проверка выбора времени"):
            self.app.method.assertTimeBox("ON", _directions['Time'], '1')

    # Метод проверки сохранения SMS Эгида - Резерв 1
    def assert_save_sms_egida_rezerv_1(self):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Проверка ввода значений в поле Номер телефона - код"):
            self.app.method.assertValues(_directions['Phone_cod'], TEL_COD_rezerv_1)
        with allure.step("Проверка ввода значений в поле Номер телефона - номер"):
            self.app.method.assertValuesPhoneNum(_directions['Phone_number'], TEL_NUM_rezerv_1)
        with allure.step("Проверка ввода значений в поле Таймаут при ошибке"):
            self.app.method.assertValues(_directions['Timeout_on_error'], Timeout_on_error_rezerv_1)
        with allure.step("Проверка выбора из выпадающего списка Тестировать если"):
            self.app.method.assertSelectionDropdownList(_directions['Test_if'], test_IF_sms_egidrezerv_1)
        with allure.step("Проверка выбора из выпадающего списка Метод тестирования"):
            self.app.method.assertSelectionDropdownList(_directions['Test_method'], test_method_sms_egida_rezerv_1)
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(testing_sms_egida_rezerv_1, 'С интервалом')
        with allure.step("Проверка ввода значений в поле Интервал тестирования"):
            self.app.method.assertValues(_directions['Test_interval'], Test_interval_rezerv_1)

    # Метод проверки сохранения ЗВОНОК - Резерв 1
    def assert_save_call_rezerv_1(self):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Проверка ввода значений в поле Номер телефона - код"):
            self.app.method.assertValues(_directions['Phone_cod'], TEL_COD_rezerv_1)
        with allure.step("Проверка ввода значений в поле Номер телефона - номер"):
            self.app.method.assertValuesPhoneNum(_directions['Phone_number'], TEL_NUM_rezerv_1)
        with allure.step("Проверка ввода значений в поле Количество повторов"):
            self.app.method.assertValues(_directions['Count_rep'], count_reset_rezerv_1)
        with allure.step("Проверка ввода значений в поле Таймаут при ошибке"):
            self.app.method.assertValues(_directions['Timeout_on_error'], Timeout_on_error_rezerv_1)
        with allure.step("Проверка выбора из выпадающего списка Тестировать если"):
            self.app.method.assertSelectionDropdownList(_directions['Test_if'], test_IF_sms_egidrezerv_1)
        with allure.step("Проверка выбора из выпадающего списка Метод тестирования"):
            self.app.method.assertSelectionDropdownList(_directions['Test_method'], test_method_sms_egida_rezerv_1)
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(testing_sms_egida_rezerv_1, 'С интервалом')
        with allure.step("Проверка ввода значений в поле Интервал тестирования"):
            self.app.method.assertValues(_directions['Test_interval'], Test_interval_rezerv_1)

    # Метод проверки сохранения SMS Эгида - Резерв 2
    def assert_save_sms_egida_rezerv_2(self):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Проверка ввода значений в поле Номер телефона - код"):
            self.app.method.assertValues(_directions['Phone_cod'], TEL_COD_rezerv_2)
        with allure.step("Проверка ввода значений в поле Номер телефона - номер"):
            self.app.method.assertValuesPhoneNum(_directions['Phone_number'], TEL_NUM_rezerv_2)
        with allure.step("Проверка ввода значений в поле Таймаут при ошибке"):
            self.app.method.assertValues(_directions['Timeout_on_error'], Timeout_on_error_rezerv_2)
        with allure.step("Проверка выбора из выпадающего списка Тестировать если"):
            self.app.method.assertSelectionDropdownList(_directions['Test_if'], test_IF_sms_egidrezerv_2)
        with allure.step("Проверка выбора из выпадающего списка Метод тестирования"):
            self.app.method.assertSelectionDropdownList(_directions['Test_method'], test_method_sms_egida_rezerv_2)
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(testing_sms_egida_rezerv_2, 'С интервалом')
        with allure.step("Проверка ввода значений в поле Интервал тестирования"):
            self.app.method.assertValues(_directions['Test_interval'], Test_interval_rezerv_2)

    # Метод проверки сохранения SMS Эгида - Резерв 2
    def assert_save_call_rezerv_2(self):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Проверка ввода значений в поле Номер телефона - код"):
            self.app.method.assertValues(_directions['Phone_cod'], TEL_COD_rezerv_2)
        with allure.step("Проверка ввода значений в поле Номер телефона - номер"):
            self.app.method.assertValuesPhoneNum(_directions['Phone_number'], TEL_NUM_rezerv_2)
        with allure.step("Проверка ввода значений в поле Количество повторов"):
            self.app.method.assertValues(_directions['Count_rep'], count_reset_rezerv_2)
        with allure.step("Проверка ввода значений в поле Таймаут при ошибке"):
            self.app.method.assertValues(_directions['Timeout_on_error'], Timeout_on_error_rezerv_2)
        with allure.step("Проверка выбора из выпадающего списка Тестировать если"):
            self.app.method.assertSelectionDropdownList(_directions['Test_if'], test_IF_sms_egidrezerv_2)
        with allure.step("Проверка выбора из выпадающего списка Метод тестирования"):
            self.app.method.assertSelectionDropdownList(_directions['Test_method'], test_method_sms_egida_rezerv_2)
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(testing_sms_egida_rezerv_2, 'С интервалом')
        with allure.step("Проверка ввода значений в поле Интервал тестирования"):
            self.app.method.assertValues(_directions['Test_interval'], Test_interval_rezerv_2)

    # Метод сохранения SMS пользователю - ОСНОВНОЙ
    def save_sms_user_timetable_main(self):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Ввод значений в поле Номер телефона - код"):
            self.app.method.inputValues(_directions['Phone_cod'], TEL_COD_main)
        with allure.step("Ввод значений в поле Номер телефона - номер"):
            self.app.method.inputValues(_directions['Phone_number'], TEL_NUM_main)
        with allure.step("Выбор из выпадающего списка Язык"):
            self.app.method.selectDropdownListByName(lang_main, _directions['Lang'])
        with allure.step("Выбор чекбокса Отправлять время события"):
            self.app.method.checkBox(_directions['Send_event_time'], main_Send_event_time_click,
                                     main_Send_event_time_status)
        with allure.step("Выбор чекбокса Отправлять дату события"):
            self.app.method.checkBox(_directions['Send_event_date'], main_Send_event_data_click,
                                     main_Send_event_data_status)
        with allure.step("Ввод значений в поле Таймаут при ошибке"):
            self.app.method.inputValues(_directions['Timeout_on_error'], Timeout_on_error_main)
        with allure.step("Выбор из выпадающего списка Тестировать если"):
            self.app.method.selectDropdownListByName(test_IF_main, _directions['Test_if'])
        with allure.step("Выбор из выпадающего списка Метод тестирования"):
            self.app.method.selectDropdownListByName(test_method_main, _directions['Test_method'])
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(testing_main, 'По расписанию')
        with allure.step("Выбор из выпадающего списка Дни недели"):
            day = _directions['Days_of_the_week']
            self.app.method.close_cross(days_of_the_week_main)
            self.app.method.go_to_element(f'/html/body//div[@class="b-multiselect-item"]/span[.="{day}"]', 'true')
            self.app.method.click((By.XPATH, f'/html/body//div[@class="b-multiselect-item"]/span[.="{day}"]'))
            self.app.method.click((By.XPATH, days_of_the_week_main))
        with allure.step("Выбор времени"):
            time_off = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00',
                        '10:00',
                        '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00',
                        '21:00',
                        '22:00', '23:00']
            for i in time_off:
                self.app.method.TimeBox("OFF", i, '1')
            self.app.method.TimeBox("ON", _directions['Time'], '1')

    # Метод сохранения SMS Эгида - ОСНОВНОЙ
    def save_sms_egida_timetable_main(self):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Ввод значений в поле Номер телефона - код"):
            self.app.method.inputValues(_directions['Phone_cod'], TEL_COD_main)
        with allure.step("Ввод значений в поле Номер телефона - номер"):
            self.app.method.inputValues(_directions['Phone_number'], TEL_NUM_main)
        with allure.step("Ввод значений в поле Таймаут при ошибке"):
            self.app.method.inputValues(_directions['Timeout_on_error'], Timeout_on_error_main)
        with allure.step("Выбор из выпадающего списка Тестировать если"):
            self.app.method.selectDropdownListByName(test_IF_sms_egida_main, _directions['Test_if'])
        with allure.step("Выбор из выпадающего списка Метод тестирования"):
            self.app.method.selectDropdownListByName(test_method_sms_egida_main, _directions['Test_method'])
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(testing_sms_egida_main, 'По расписанию')
        with allure.step("Выбор из выпадающего списка Дни недели"):
            day = _directions['Days_of_the_week']
            self.app.method.close_cross(days_of_the_week_main)
            self.app.method.go_to_element(f'/html/body//div[@class="b-multiselect-item"]/span[.="{day}"]', 'true')
            self.app.method.click((By.XPATH, f'/html/body//div[@class="b-multiselect-item"]/span[.="{day}"]'))
            self.app.method.click((By.XPATH, days_of_the_week_main))
        with allure.step("Выбор времени"):
            time_off = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00',
                        '10:00',
                        '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00',
                        '21:00',
                        '22:00', '23:00']
            for i in time_off:
                self.app.method.TimeBox("OFF", i, '1')
            self.app.method.TimeBox("ON", _directions['Time'], '1')

    # Метод сохранения ЗВОНОК- ОСНОВНОЙ
    def save_call_timetable_main(self):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Ввод значений в поле Номер телефона - код"):
            self.app.method.inputValues(_directions['Phone_cod'], TEL_COD_main)
        with allure.step("Ввод значений в поле Номер телефона - номер"):
            self.app.method.inputValues(_directions['Phone_number'], TEL_NUM_main)
        with allure.step("Ввод значений в поле Количество повторов"):
            self.app.method.inputValues(_directions['Count_rep'], count_reset_main)
        with allure.step("Ввод значений в поле Таймаут при ошибке"):
            self.app.method.inputValues(_directions['Timeout_on_error'], Timeout_on_error_main)
        with allure.step("Выбор из выпадающего списка Тестировать если"):
            self.app.method.selectDropdownListByName(test_IF_sms_egida_main, _directions['Test_if'])
        with allure.step("Выбор из выпадающего списка Метод тестирования"):
            self.app.method.selectDropdownListByName(test_method_sms_egida_main, _directions['Test_method'])
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(testing_sms_egida_main, 'По расписанию')
        with allure.step("Выбор из выпадающего списка Дни недели"):
            day = _directions['Days_of_the_week']
            self.app.method.close_cross(days_of_the_week_main)
            self.app.method.go_to_element(f'/html/body//div[@class="b-multiselect-item"]/span[.="{day}"]', 'true')
            self.app.method.click((By.XPATH, f'/html/body//div[@class="b-multiselect-item"]/span[.="{day}"]'))
            self.app.method.click((By.XPATH, days_of_the_week_main))
        with allure.step("Выбор времени"):
            time_off = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00',
                        '10:00',
                        '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00',
                        '21:00',
                        '22:00', '23:00']
            for i in time_off:
                self.app.method.TimeBox("OFF", i, '1')
            self.app.method.TimeBox("ON", _directions['Time'], '1')

    # Метод сохранения SMS Эгида - РЕЗЕРВ 1
    def save_sms_egida_timetable_rezerv_1(self):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Ввод значений в поле Номер телефона - код"):
            self.app.method.inputValues(_directions['Phone_cod'], TEL_COD_rezerv_1)
        with allure.step("Ввод значений в поле Номер телефона - номер"):
            self.app.method.inputValues(_directions['Phone_number'], TEL_NUM_rezerv_1)
        with allure.step("Ввод значений в поле Таймаут при ошибке"):
            self.app.method.inputValues(_directions['Timeout_on_error'], Timeout_on_error_rezerv_1)
        with allure.step("Выбор из выпадающего списка Тестировать если"):
            self.app.method.selectDropdownListByName(test_IF_sms_egidrezerv_1, _directions['Test_if'])
        with allure.step("Выбор из выпадающего списка Метод тестирования"):
            self.app.method.selectDropdownListByName(test_method_sms_egida_rezerv_1, _directions['Test_method'])
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(testing_sms_egida_main, 'С интервалом')
            self.app.method.selectDropdownListByName(testing_sms_egida_rezerv_1, 'По расписанию')
        with allure.step("Выбор из выпадающего списка Дни недели"):
            day = _directions['Days_of_the_week']
            self.app.method.close_cross(days_of_the_week_main)
            self.app.method.go_to_element(f'/html/body//div[@class="b-multiselect-item"]/span[.="{day}"]', 'true')
            self.app.method.click((By.XPATH, f'/html/body//div[@class="b-multiselect-item"]/span[.="{day}"]'))
            self.app.method.click((By.XPATH, days_of_the_week_main))
        with allure.step("Выбор времени"):
            time_off = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00',
                        '10:00',
                        '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00',
                        '21:00',
                        '22:00', '23:00']
            for i in time_off:
                self.app.method.TimeBox("OFF", i, '1')
            self.app.method.TimeBox("ON", _directions['Time'], '1')

    # Метод сохранения SMS Эгида - РЕЗЕРВ 1
    def save_call_timetable_rezerv_1(self):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Ввод значений в поле Номер телефона - код"):
            self.app.method.inputValues(_directions['Phone_cod'], TEL_COD_rezerv_1)
        with allure.step("Ввод значений в поле Номер телефона - номер"):
            self.app.method.inputValues(_directions['Phone_number'], TEL_NUM_rezerv_1)
        with allure.step("Ввод значений в поле Таймаут при ошибке"):
            self.app.method.inputValues(_directions['Timeout_on_error'], Timeout_on_error_rezerv_1)
        with allure.step("Ввод значений в поле Количество повторов"):
            self.app.method.inputValues(_directions['Count_rep'], count_reset_rezerv_1)
        with allure.step("Выбор из выпадающего списка Тестировать если"):
            self.app.method.selectDropdownListByName(test_IF_sms_egidrezerv_1, _directions['Test_if'])
        with allure.step("Выбор из выпадающего списка Метод тестирования"):
            self.app.method.selectDropdownListByName(test_method_sms_egida_rezerv_1, _directions['Test_method'])
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(testing_sms_egida_main, 'С интервалом')
            self.app.method.selectDropdownListByName(testing_sms_egida_rezerv_1, 'По расписанию')
        with allure.step("Выбор из выпадающего списка Дни недели"):
            day = _directions['Days_of_the_week']
            self.app.method.close_cross(days_of_the_week_main)
            self.app.method.go_to_element(f'/html/body//div[@class="b-multiselect-item"]/span[.="{day}"]', 'true')
            self.app.method.click((By.XPATH, f'/html/body//div[@class="b-multiselect-item"]/span[.="{day}"]'))
            self.app.method.click((By.XPATH, days_of_the_week_main))
        with allure.step("Выбор времени"):
            time_off = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00',
                        '10:00',
                        '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00',
                        '21:00',
                        '22:00', '23:00']
            for i in time_off:
                self.app.method.TimeBox("OFF", i, '1')
            self.app.method.TimeBox("ON", _directions['Time'], '1')

    # Метод сохранения SMS Эгида - РЕЗЕРВ 2
    def save_sms_egida_timetable_rezerv_2(self):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Ввод значений в поле Номер телефона - код"):
            self.app.method.inputValues(_directions['Phone_cod'], TEL_COD_rezerv_2)
        with allure.step("Ввод значений в поле Номер телефона - номер"):
            self.app.method.inputValues(_directions['Phone_number'], TEL_NUM_rezerv_2)
        with allure.step("Ввод значений в поле Таймаут при ошибке"):
            self.app.method.inputValues(_directions['Timeout_on_error'], Timeout_on_error_rezerv_2)
        with allure.step("Выбор из выпадающего списка Тестировать если"):
            self.app.method.selectDropdownListByName(test_IF_sms_egidrezerv_2, _directions['Test_if'])
        with allure.step("Выбор из выпадающего списка Метод тестирования"):
            self.app.method.selectDropdownListByName(test_method_sms_egida_rezerv_2, _directions['Test_method'])
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(testing_sms_egida_main, 'С интервалом')
            self.app.method.selectDropdownListByName(testing_sms_egida_rezerv_1, 'С интервалом')
            self.app.method.selectDropdownListByName(testing_sms_egida_rezerv_2, 'По расписанию')
        with allure.step("Выбор из выпадающего списка Дни недели"):
            day = _directions['Days_of_the_week']
            self.app.method.close_cross(days_of_the_week_main)
            self.app.method.go_to_element(f'/html/body//div[@class="b-multiselect-item"]/span[.="{day}"]', 'true')
            self.app.method.click((By.XPATH, f'/html/body//div[@class="b-multiselect-item"]/span[.="{day}"]'))
            self.app.method.click((By.XPATH, days_of_the_week_main))
        with allure.step("Выбор времени"):
            time_off = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00',
                        '10:00',
                        '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00',
                        '21:00',
                        '22:00', '23:00']
            for i in time_off:
                self.app.method.TimeBox("OFF", i, '1')
            self.app.method.TimeBox("ON", _directions['Time'], '1')

    # Метод сохранения ЗВОНОК - РЕЗЕРВ 2
    def save_call_timetable_rezerv_2(self):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Ввод значений в поле Номер телефона - код"):
            self.app.method.inputValues(_directions['Phone_cod'], TEL_COD_rezerv_2)
        with allure.step("Ввод значений в поле Номер телефона - номер"):
            self.app.method.inputValues(_directions['Phone_number'], TEL_NUM_rezerv_2)
        with allure.step("Ввод значений в поле Таймаут при ошибке"):
            self.app.method.inputValues(_directions['Timeout_on_error'], Timeout_on_error_rezerv_2)
        with allure.step("Ввод значений в поле Количество повторов"):
            self.app.method.inputValues(_directions['Count_rep'], count_reset_rezerv_2)
        with allure.step("Выбор из выпадающего списка Тестировать если"):
            self.app.method.selectDropdownListByName(test_IF_sms_egidrezerv_2, _directions['Test_if'])
        with allure.step("Выбор из выпадающего списка Метод тестирования"):
            self.app.method.selectDropdownListByName(test_method_sms_egida_rezerv_2, _directions['Test_method'])
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(testing_sms_egida_main, 'С интервалом')
            self.app.method.selectDropdownListByName(testing_sms_egida_rezerv_1, 'С интервалом')
            self.app.method.selectDropdownListByName(testing_sms_egida_rezerv_2, 'По расписанию')
        with allure.step("Выбор из выпадающего списка Дни недели"):
            day = _directions['Days_of_the_week']
            self.app.method.close_cross(days_of_the_week_main)
            self.app.method.go_to_element(f'/html/body//div[@class="b-multiselect-item"]/span[.="{day}"]', 'true')
            self.app.method.click((By.XPATH, f'/html/body//div[@class="b-multiselect-item"]/span[.="{day}"]'))
            self.app.method.click((By.XPATH, days_of_the_week_main))
        with allure.step("Выбор времени"):
            time_off = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00',
                        '10:00',
                        '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00',
                        '21:00',
                        '22:00', '23:00']
            for i in time_off:
                self.app.method.TimeBox("OFF", i, '1')
            self.app.method.TimeBox("ON", _directions['Time'], '1')

    # Метод сохранения SMS пользователю - ОСНОВНОЙ - максимальное заполнение
    def save_sms_user_timetable_main_max_size(self):
        with allure.step("Ввод значений в поле Номер телефона - код"):
            self.app.method.inputValues('+7777', TEL_COD_main)
        with allure.step("Ввод значений в поле Номер телефона - номер"):
            self.app.method.inputValues('(999)999-99-99', TEL_NUM_main)
        with allure.step("Выбор из выпадающего списка Язык"):
            self.app.method.selectDropdownListByName(lang_main, "Английский")
        with allure.step("Выбор чекбокса Отправлять время события"):
            self.app.method.checkBox("ON", main_Send_event_time_click, main_Send_event_time_status)
        with allure.step("Выбор чекбокса Отправлять дату события"):
            self.app.method.checkBox("ON", main_Send_event_data_click, main_Send_event_data_status)
        with allure.step("Ввод значений в поле Таймаут при ошибке"):
            self.app.method.inputValues('23:59', Timeout_on_error_main)
        with allure.step("Выбор из выпадающего списка Тестировать если"):
            self.app.method.selectDropdownListByName(test_IF_main, "Канал активен")
        with allure.step("Выбор из выпадающего списка Метод тестирования"):
            self.app.method.selectDropdownListByName(test_method_main, "Звонок")
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(testing_main, 'По расписанию')
        with allure.step("Выбор из выпадающего списка Дни недели"):
            self.choice_all_days(days_of_the_week_main)
        with allure.step("Выбор времени"):
            time1 = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00',
                     '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00',
                     '22:00', '23:00']
            for i in time1:
                self.app.method.TimeBox("OFF", i, '1')
            time2 = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00']
            for i in time2:
                self.app.method.TimeBox("ON", i, '1')

    # Метод сохранения SMS Эгида - ОСНОВНОЙ - максимальное заполнение
    def save_sms_egida_timetable_main_max_size(self):
        with allure.step("Ввод значений в поле Номер телефона - код"):
            self.app.method.inputValues('+7777', TEL_COD_main)
        with allure.step("Ввод значений в поле Номер телефона - номер"):
            self.app.method.inputValues('(999)999-99-99', TEL_NUM_main)
        with allure.step("Ввод значений в поле Таймаут при ошибке"):
            self.app.method.inputValues('23:59', Timeout_on_error_main)
        with allure.step("Выбор из выпадающего списка Тестировать если"):
            self.app.method.selectDropdownListByName(test_IF_sms_egida_main, "Канал активен")
        with allure.step("Выбор из выпадающего списка Метод тестирования"):
            self.app.method.selectDropdownListByName(test_method_sms_egida_main, "Звонок")
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(testing_sms_egida_main, 'По расписанию')
        with allure.step("Выбор из выпадающего списка Дни недели"):
            self.choice_all_days(days_of_the_week_main)
        with allure.step("Выбор времени"):
            time1 = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00',
                     '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00',
                     '22:00', '23:00']
            for i in time1:
                self.app.method.TimeBox("OFF", i, '1')
            time2 = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00']
            for i in time2:
                self.app.method.TimeBox("ON", i, '1')

    # Метод сохранения SMS Эгида - РЕЗЕРВ 1 - максимальное заполнение
    def save_sms_egida_timetable_rezerv_1_max_size(self):
        with allure.step("Ввод значений в поле Номер телефона - код"):
            self.app.method.inputValues('+7777', TEL_COD_rezerv_1)
        with allure.step("Ввод значений в поле Номер телефона - номер"):
            self.app.method.inputValues('(999)999-99-99', TEL_NUM_rezerv_1)
        with allure.step("Ввод значений в поле Таймаут при ошибке"):
            self.app.method.inputValues('23:59', Timeout_on_error_rezerv_1)
        with allure.step("Выбор из выпадающего списка Тестировать если"):
            self.app.method.selectDropdownListByName(test_IF_sms_egidrezerv_1, "Канал активен")
        with allure.step("Выбор из выпадающего списка Метод тестирования"):
            self.app.method.selectDropdownListByName(test_method_sms_egida_rezerv_1, "Звонок")
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(testing_sms_egida_main, 'С интервалом')
            self.app.method.selectDropdownListByName(testing_sms_egida_rezerv_1, 'По расписанию')
        with allure.step("Выбор из выпадающего списка Дни недели"):
            self.choice_all_days(days_of_the_week_main)
        with allure.step("Выбор времени"):
            time1 = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00',
                     '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00',
                     '22:00', '23:00']
            for i in time1:
                self.app.method.TimeBox("OFF", i, '1')
            time2 = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00']
            for i in time2:
                self.app.method.TimeBox("ON", i, '1')

    # Метод проверки сохранения SMS пользователю - ОСНОВНОЙ - ля проверки сохранения максимального значения
    def assert_save_sms_user_timetable_main_max(self):
        with allure.step("Проверка ввода значений в поле Номер телефона - код"):
            self.app.method.assertValues('7777', TEL_COD_main)
        with allure.step("Проверка ввода значений в поле Номер телефона - номер"):
            self.app.method.assertValuesPhoneNum('(999)999-99-99', TEL_NUM_main)
        with allure.step("Проверка ввода значений в поле Таймаут при ошибке"):
            self.app.method.assertValues('23:59', Timeout_on_error_main)
        with allure.step("Проверка выбора из выпадающего списка Тестировать если"):
            self.app.method.assertSelectionDropdownList("Канал активен", test_IF_sms_egida_main)
        with allure.step("Проверка выбора из выпадающего списка Метод тестирования"):
            self.app.method.assertSelectionDropdownList("Звонок", test_method_sms_egida_main)
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(testing_sms_egida_main, 'По расписанию')
        with allure.step("Проверка выбора из выпадающего списка Дни недели"):
            days = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
            wd = self.app.wd
            for i in days:
                element = wd.find_element(By.XPATH, days_of_the_week_main).get_property("textContent")
                assert str(i) in str(
                    element), f"\nОжидаемое значение в выпадающем списке: '{i}'\nФактическое: '{element}'"
        with allure.step("Проверка выбора времени"):
            time1 = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00']
            for i in time1:
                self.app.method.assertTimeBox("ON", i, '1')

        # Метод проверки сохранения SMS пользователю - ОСНОВНОЙ - ля проверки сохранения максимального значения

    def assert_save_sms_user_timetable_rezerv_1_max(self):
        with allure.step("Проверка ввода значений в поле Номер телефона - код"):
            self.app.method.assertValues('7777', TEL_COD_rezerv_1)
        with allure.step("Проверка ввода значений в поле Номер телефона - номер"):
            self.app.method.assertValuesPhoneNum('(999)999-99-99', TEL_NUM_rezerv_1)
        with allure.step("Проверка ввода значений в поле Таймаут при ошибке"):
            self.app.method.assertValues('23:59', Timeout_on_error_rezerv_1)
        with allure.step("Проверка выбора из выпадающего списка Тестировать если"):
            self.app.method.assertSelectionDropdownList("Канал активен", test_IF_sms_egidrezerv_1)
        with allure.step("Проверка выбора из выпадающего списка Метод тестирования"):
            self.app.method.assertSelectionDropdownList("Звонок", test_method_sms_egida_rezerv_1)
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(testing_sms_egida_main, 'С интервалом')
            self.app.method.selectDropdownListByName(testing_sms_egida_rezerv_1, 'По расписанию')
        with allure.step("Проверка выбора из выпадающего списка Дни недели"):
            days = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
            wd = self.app.wd
            for i in days:
                element = wd.find_element(By.XPATH, days_of_the_week_rezerv_1).get_property("textContent")
                assert str(i) in str(
                    element), f"\nОжидаемое значение в выпадающем списке: '{i}'\nФактическое: '{element}'"
        with allure.step("Проверка выбора времени"):
            time1 = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00']
            for i in time1:
                self.app.method.assertTimeBox("ON", i, '1')

    def choice_all_days(self, locator):
        self.app.method.close_cross(locator)
        self.app.method.click((By.XPATH, f'/html/body/div[3]/div[1]/label/span'))
        self.app.method.click((By.XPATH, locator))

    # Метод проверки сохранения SMS пользователю - ОСНОВНОЙ
    def assert_save_sms_user_timetable_main(self):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Проверка ввода значений в поле Номер телефона - код"):
            self.app.method.assertValues(_directions['Phone_cod'], TEL_COD_main)
        with allure.step("Проверка ввода значений в поле Номер телефона - номер"):
            self.app.method.assertValuesPhoneNum(_directions['Phone_number'], TEL_NUM_main)
        with allure.step("Проверка выбора из выпадающего списка Язык"):
            self.app.method.assertSelectionDropdownList(_directions['Lang'], lang_main)
        with allure.step("Проверка выбора чек-бокса Отправлять время события"):
            self.app.method.assertCheckBox(_directions['Send_event_time'], main_Send_event_time_status)
        with allure.step("Проверка выбора чек-бокса Отправлять дату события"):
            self.app.method.assertCheckBox(_directions['Send_event_date'], main_Send_event_data_status)
        with allure.step("Проверка ввода значений в поле Таймаут при ошибке"):
            self.app.method.assertValues(_directions['Timeout_on_error'], Timeout_on_error_main)
        with allure.step("Проверка выбора из выпадающего списка Тестировать если"):
            self.app.method.assertSelectionDropdownList(_directions['Test_if'], test_IF_main)
        with allure.step("Проверка выбора из выпадающего списка Метод тестирования"):
            self.app.method.assertSelectionDropdownList(_directions['Test_method'], test_method_main)
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(testing_main, 'По расписанию')
        with allure.step("Проверка выбора из выпадающего списка Дни недели"):
            day = _directions['Days_of_the_week']
            wd = self.app.wd
            element = wd.find_element(By.XPATH, days_of_the_week_main).get_property("textContent")
            assert str(day) in str(
                element), f"\nОжидаемое значение в выпадающем списке: '{day}'\nФактическое: '{element}'"
        with allure.step("Проверка выбора времени"):
            self.app.method.assertTimeBox("ON", _directions['Time'], '1')

    # Метод проверки сохранения SMS пользователю - ОСНОВНОЙ
    def assert_save_sms_egida_timetable_main(self):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Проверка ввода значений в поле Номер телефона - код"):
            self.app.method.assertValues(_directions['Phone_cod'], TEL_COD_main)
        with allure.step("Проверка ввода значений в поле Номер телефона - номер"):
            self.app.method.assertValuesPhoneNum(_directions['Phone_number'], TEL_NUM_main)
        with allure.step("Проверка ввода значений в поле Таймаут при ошибке"):
            self.app.method.assertValues(_directions['Timeout_on_error'], Timeout_on_error_main)
        with allure.step("Проверка выбора из выпадающего списка Тестировать если"):
            self.app.method.assertSelectionDropdownList(_directions['Test_if'], test_IF_sms_egida_main)
        with allure.step("Проверка выбора из выпадающего списка Метод тестирования"):
            self.app.method.assertSelectionDropdownList(_directions['Test_method'], test_method_sms_egida_main)
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(testing_sms_egida_main, 'По расписанию')
        with allure.step("Проверка выбора из выпадающего списка Дни недели"):
            day = _directions['Days_of_the_week']
            wd = self.app.wd
            element = wd.find_element(By.XPATH, days_of_the_week_main).get_property("textContent")
            assert str(day) in str(
                element), f"\nОжидаемое значение в выпадающем списке: '{day}'\nФактическое: '{element}'"
        with allure.step("Проверка выбора времени"):
            self.app.method.assertTimeBox("ON", _directions['Time'], '1')

    # Метод проверки сохранения ЗВОНОК - ОСНОВНОЙ
    def assert_save_call_timetable_main(self):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Проверка ввода значений в поле Номер телефона - код"):
            self.app.method.assertValues(_directions['Phone_cod'], TEL_COD_main)
        with allure.step("Проверка ввода значений в поле Номер телефона - номер"):
            self.app.method.assertValuesPhoneNum(_directions['Phone_number'], TEL_NUM_main)
        with allure.step("Проверка ввода значений в поле Количество повторов"):
            self.app.method.assertValues(_directions['Count_rep'], count_reset_main)
        with allure.step("Проверка ввода значений в поле Таймаут при ошибке"):
            self.app.method.assertValues(_directions['Timeout_on_error'], Timeout_on_error_main)
        with allure.step("Проверка выбора из выпадающего списка Тестировать если"):
            self.app.method.assertSelectionDropdownList(_directions['Test_if'], test_IF_sms_egida_main)
        with allure.step("Проверка выбора из выпадающего списка Метод тестирования"):
            self.app.method.assertSelectionDropdownList(_directions['Test_method'], test_method_sms_egida_main)
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(testing_sms_egida_main, 'По расписанию')
        with allure.step("Проверка выбора из выпадающего списка Дни недели"):
            day = _directions['Days_of_the_week']
            wd = self.app.wd
            element = wd.find_element(By.XPATH, days_of_the_week_main).get_property("textContent")
            assert str(day) in str(
                element), f"\nОжидаемое значение в выпадающем списке: '{day}'\nФактическое: '{element}'"
        with allure.step("Проверка выбора времени"):
            self.app.method.assertTimeBox("ON", _directions['Time'], '1')

    # Метод проверки сохранения SMS пользователю - РЕЗЕРВ 1
    def assert_save_sms_egida_timetable_rezerv_1(self):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Проверка ввода значений в поле Номер телефона - код"):
            self.app.method.assertValues(_directions['Phone_cod'], TEL_COD_rezerv_1)
        with allure.step("Проверка ввода значений в поле Номер телефона - номер"):
            self.app.method.assertValuesPhoneNum(_directions['Phone_number'], TEL_NUM_rezerv_1)
        with allure.step("Проверка ввода значений в поле Таймаут при ошибке"):
            self.app.method.assertValues(_directions['Timeout_on_error'], Timeout_on_error_rezerv_1)
        with allure.step("Проверка выбора из выпадающего списка Тестировать если"):
            self.app.method.assertSelectionDropdownList(_directions['Test_if'], test_IF_sms_egidrezerv_1)
        with allure.step("Проверка выбора из выпадающего списка Метод тестирования"):
            self.app.method.assertSelectionDropdownList(_directions['Test_method'], test_method_sms_egida_rezerv_1)
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(testing_sms_egida_main, 'С интервалом')
            self.app.method.selectDropdownListByName(testing_sms_egida_rezerv_1, 'По расписанию')
        with allure.step("Проверка выбора из выпадающего списка Дни недели"):
            day = _directions['Days_of_the_week']
            wd = self.app.wd
            element = wd.find_element(By.XPATH, days_of_the_week_main).get_property("textContent")
            assert str(day) in str(
                element), f"\nОжидаемое значение в выпадающем списке: '{day}'\nФактическое: '{element}'"
        with allure.step("Проверка выбора времени"):
            self.app.method.assertTimeBox("ON", _directions['Time'], '1')

    # Метод проверки сохранения ЗВОНОК - РЕЗЕРВ 1
    def assert_save_call_timetable_rezerv_1(self):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Проверка ввода значений в поле Номер телефона - код"):
            self.app.method.assertValues(_directions['Phone_cod'], TEL_COD_rezerv_1)
        with allure.step("Проверка ввода значений в поле Номер телефона - номер"):
            self.app.method.assertValuesPhoneNum(_directions['Phone_number'], TEL_NUM_rezerv_1)
        with allure.step("Проверка ввода значений в поле Таймаут при ошибке"):
            self.app.method.assertValues(_directions['Timeout_on_error'], Timeout_on_error_rezerv_1)
        with allure.step("Проверка ввода значений в поле Количество повторов"):
            self.app.method.assertValues(_directions['Count_rep'], count_reset_rezerv_1)
        with allure.step("Проверка выбора из выпадающего списка Тестировать если"):
            self.app.method.assertSelectionDropdownList(_directions['Test_if'], test_IF_sms_egidrezerv_1)
        with allure.step("Проверка выбора из выпадающего списка Метод тестирования"):
            self.app.method.assertSelectionDropdownList(_directions['Test_method'], test_method_sms_egida_rezerv_1)
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(testing_sms_egida_main, 'С интервалом')
            self.app.method.selectDropdownListByName(testing_sms_egida_rezerv_1, 'По расписанию')
        with allure.step("Проверка выбора из выпадающего списка Дни недели"):
            day = _directions['Days_of_the_week']
            wd = self.app.wd
            element = wd.find_element(By.XPATH, days_of_the_week_main).get_property("textContent")
            assert str(day) in str(
                element), f"\nОжидаемое значение в выпадающем списке: '{day}'\nФактическое: '{element}'"
        with allure.step("Проверка выбора времени"):
            self.app.method.assertTimeBox("ON", _directions['Time'], '1')

    # Метод проверки сохранения SMS пользователю - РЕЗЕРВ 1
    def assert_save_sms_egida_timetable_rezerv_2(self):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Проверка ввода значений в поле Номер телефона - код"):
            self.app.method.assertValues(_directions['Phone_cod'], TEL_COD_rezerv_2)
        with allure.step("Проверка ввода значений в поле Номер телефона - номер"):
            self.app.method.assertValuesPhoneNum(_directions['Phone_number'], TEL_NUM_rezerv_2)
        with allure.step("Проверка ввода значений в поле Таймаут при ошибке"):
            self.app.method.assertValues(_directions['Timeout_on_error'], Timeout_on_error_rezerv_2)
        with allure.step("Проверка выбора из выпадающего списка Тестировать если"):
            self.app.method.assertSelectionDropdownList(_directions['Test_if'], test_IF_sms_egidrezerv_2)
        with allure.step("Проверка выбора из выпадающего списка Метод тестирования"):
            self.app.method.assertSelectionDropdownList(_directions['Test_method'], test_method_sms_egida_rezerv_2)
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(testing_sms_egida_main, 'С интервалом')
            self.app.method.selectDropdownListByName(testing_sms_egida_rezerv_1, 'С интервалом')
            self.app.method.selectDropdownListByName(testing_sms_egida_rezerv_2, 'По расписанию')
        with allure.step("Проверка выбора из выпадающего списка Дни недели"):
            day = _directions['Days_of_the_week']
            wd = self.app.wd
            element = wd.find_element(By.XPATH, days_of_the_week_main).get_property("textContent")
            assert str(day) in str(
                element), f"\nОжидаемое значение в выпадающем списке: '{day}'\nФактическое: '{element}'"
        with allure.step("Проверка выбора времени"):
            self.app.method.assertTimeBox("ON", _directions['Time'], '1')

    # Метод проверки сохранения ЗВОНОК- РЕЗЕРВ 1
    def assert_save_call_timetable_rezerv_2(self):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Проверка ввода значений в поле Номер телефона - код"):
            self.app.method.assertValues(_directions['Phone_cod'], TEL_COD_rezerv_2)
        with allure.step("Проверка ввода значений в поле Номер телефона - номер"):
            self.app.method.assertValuesPhoneNum(_directions['Phone_number'], TEL_NUM_rezerv_2)
        with allure.step("Проверка ввода значений в поле Количество повторов"):
            self.app.method.assertValues(_directions['Count_rep'], count_reset_rezerv_2)
        with allure.step("Проверка ввода значений в поле Таймаут при ошибке"):
            self.app.method.assertValues(_directions['Timeout_on_error'], Timeout_on_error_rezerv_2)
        with allure.step("Проверка выбора из выпадающего списка Тестировать если"):
            self.app.method.assertSelectionDropdownList(_directions['Test_if'], test_IF_sms_egidrezerv_2)
        with allure.step("Проверка выбора из выпадающего списка Метод тестирования"):
            self.app.method.assertSelectionDropdownList(_directions['Test_method'], test_method_sms_egida_rezerv_2)
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(testing_sms_egida_main, 'С интервалом')
            self.app.method.selectDropdownListByName(testing_sms_egida_rezerv_1, 'С интервалом')
            self.app.method.selectDropdownListByName(testing_sms_egida_rezerv_2, 'По расписанию')
        with allure.step("Проверка выбора из выпадающего списка Дни недели"):
            day = _directions['Days_of_the_week']
            wd = self.app.wd
            element = wd.find_element(By.XPATH, days_of_the_week_main).get_property("textContent")
            assert str(day) in str(
                element), f"\nОжидаемое значение в выпадающем списке: '{day}'\nФактическое: '{element}'"
        with allure.step("Проверка выбора времени"):
            self.app.method.assertTimeBox("ON", _directions['Time'], '1')

    # Метод сохранения SMS пользователю - РЕЗЕРВ 1
    def save_sms_user_rezerv_1(self):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Ввод значений в поле Номер телефона - код"):
            self.app.method.inputValues(_directions['Phone_cod'], TEL_COD_rezerv_1)
        with allure.step("Ввод значений в поле Номер телефона - номер"):
            self.app.method.inputValues(_directions['Phone_number'], TEL_NUM_rezerv_1)
        with allure.step("Выбор из выпадающего списка Язык"):
            self.app.method.selectDropdownListByName(lang_rezerv_1, _directions['Lang'])
        with allure.step("Выбор чекбокса Отправлять время события"):
            self.app.method.checkBox(_directions['Send_event_time'], rezerv_1_Send_event_time_click,
                                     rezerv_1_Send_event_time_status)
        with allure.step("Выбор чекбокса Отправлять дату события"):
            self.app.method.checkBox(_directions['Send_event_date'], rezerv_1_Send_event_data_click,
                                     rezerv_1_Send_event_data_status)
        with allure.step("Ввод значений в поле Таймаут при ошибке"):
            self.app.method.inputValues(_directions['Timeout_on_error'], Timeout_on_error_rezerv_1)
        with allure.step("Выбор из выпадающего списка Тестировать если"):
            self.app.method.selectDropdownListByName(test_IF_rezerv_1, _directions['Test_if'])
        with allure.step("Выбор из выпадающего списка Метод тестирования"):
            self.app.method.selectDropdownListByName(test_method_rezerv_1, _directions['Test_method'])
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(testing_main, 'С интервалом')
            self.app.method.selectDropdownListByName(testing_rezerv_1, 'С интервалом')
        with allure.step("Ввод значений в поле Интервал тестирования"):
            self.app.method.inputValues(_directions['Test_interval'], Test_interval_rezerv_1)

    # Метод проверки сохранения SMS пользователю - РЕЗЕРВ 1
    def assert_save_sms_user_rezerv_1(self):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Проверка ввода значений в поле Номер телефона - код"):
            self.app.method.assertValues(_directions['Phone_cod'], TEL_COD_rezerv_1)
        with allure.step("Проверка ввода значений в поле Номер телефона - номер"):
            self.app.method.assertValuesPhoneNum(_directions['Phone_number'], TEL_NUM_rezerv_1)
        with allure.step("Проверка выбора из выпадающего списка Язык"):
            self.app.method.assertSelectionDropdownList(_directions['Lang'], lang_rezerv_1)
        with allure.step("Проверка выбора чек-бокса Отправлять время события"):
            self.app.method.assertCheckBox(_directions['Send_event_time'], rezerv_1_Send_event_time_status)
        with allure.step("Проверка выбора чек-бокса Отправлять дату события"):
            self.app.method.assertCheckBox(_directions['Send_event_date'], rezerv_1_Send_event_data_status)
        with allure.step("Проверка ввода значений в поле Таймаут при ошибке"):
            self.app.method.assertValues(_directions['Timeout_on_error'], Timeout_on_error_rezerv_1)
        with allure.step("Проверка выбора из выпадающего списка Тестировать если"):
            self.app.method.assertSelectionDropdownList(_directions['Test_if'], test_IF_rezerv_1)
        with allure.step("Проверка выбора из выпадающего списка Метод тестирования"):
            self.app.method.assertSelectionDropdownList(_directions['Test_method'], test_method_rezerv_1)
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(testing_main, 'С интервалом')
            self.app.method.selectDropdownListByName(testing_rezerv_1, 'С интервалом')
        with allure.step("Проверка ввода значений в поле Интервал тестирования"):
            self.app.method.assertValues(_directions['Test_interval'], Test_interval_rezerv_1)

    # Метод сохранения SMS пользователю - РЕЗЕРВ 1
    def save_sms_user_timetable_rezerv_1(self):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Ввод значений в поле Номер телефона - код"):
            self.app.method.inputValues(_directions['Phone_cod'], TEL_COD_rezerv_1)
        with allure.step("Ввод значений в поле Номер телефона - номер"):
            self.app.method.inputValues(_directions['Phone_number'], TEL_NUM_rezerv_1)
        with allure.step("Выбор из выпадающего списка Язык"):
            self.app.method.selectDropdownListByName(lang_rezerv_1, _directions['Lang'])
        with allure.step("Выбор чекбокса Отправлять время события"):
            self.app.method.checkBox(_directions['Send_event_time'], rezerv_1_Send_event_time_click,
                                     rezerv_1_Send_event_time_status)
        with allure.step("Выбор чекбокса Отправлять дату события"):
            self.app.method.checkBox(_directions['Send_event_date'], rezerv_1_Send_event_data_click,
                                     rezerv_1_Send_event_data_status)
        with allure.step("Ввод значений в поле Таймаут при ошибке"):
            self.app.method.inputValues(_directions['Timeout_on_error'], Timeout_on_error_rezerv_1)
        with allure.step("Выбор из выпадающего списка Тестировать если"):
            self.app.method.selectDropdownListByName(test_IF_rezerv_1, _directions['Test_if'])
        with allure.step("Выбор из выпадающего списка Метод тестирования"):
            self.app.method.selectDropdownListByName(test_method_rezerv_1, _directions['Test_method'])
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(testing_main, 'По расписанию')
            self.app.method.selectDropdownListByName(testing_rezerv_1, 'По расписанию')
        with allure.step("Выбор из выпадающего списка Дни недели"):
            day = _directions['Days_of_the_week']
            self.app.method.close_cross(days_of_the_week_rezerv_1)
            self.app.method.go_to_element(f'/html/body//div[@class="b-multiselect-item"]/span[.="{day}"]', 'true')
            self.app.method.click((By.XPATH, f'/html/body//div[@class="b-multiselect-item"]/span[.="{day}"]'))
            self.app.method.click((By.XPATH, days_of_the_week_rezerv_1))
        with allure.step("Выбор времени"):
            time_off = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00',
                        '10:00',
                        '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00',
                        '21:00',
                        '22:00', '23:00']
            for i in time_off:
                self.app.method.TimeBox("OFF", i, '2')
            self.app.method.TimeBox("ON", _directions['Time'], '2')

    # Метод сохранения SMS пользователю - РЕЗЕРВ 1 - максимальное значение
    def save_sms_user_timetable_rezerv_1_max(self):
        with allure.step("Ввод значений в поле Номер телефона - код"):
            self.app.method.inputValues('+7777', TEL_COD_rezerv_1)
        with allure.step("Ввод значений в поле Номер телефона - номер"):
            self.app.method.inputValues('(999)999-99-99', TEL_NUM_rezerv_1)
        with allure.step("Выбор из выпадающего списка Язык"):
            self.app.method.selectDropdownListByName(lang_rezerv_1, "Английский")
        with allure.step("Выбор чекбокса Отправлять время события"):
            self.app.method.checkBox("ON", rezerv_1_Send_event_time_click, rezerv_1_Send_event_time_status)
        with allure.step("Выбор чекбокса Отправлять дату события"):
            self.app.method.checkBox("ON", rezerv_1_Send_event_data_click, rezerv_1_Send_event_data_status)
        with allure.step("Ввод значений в поле Таймаут при ошибке"):
            self.app.method.inputValues('23:59', Timeout_on_error_rezerv_1)
        with allure.step("Выбор из выпадающего списка Тестировать если"):
            self.app.method.selectDropdownListByName(test_IF_rezerv_1, "Канал активен")
        with allure.step("Выбор из выпадающего списка Метод тестирования"):
            self.app.method.selectDropdownListByName(test_method_rezerv_1, "Звонок")
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(testing_rezerv_1, 'По расписанию')
        with allure.step("Выбор из выпадающего списка Дни недели"):
            self.choice_all_days(days_of_the_week_rezerv_1)
        with allure.step("Выбор времени"):
            time1 = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00',
                     '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00',
                     '22:00', '23:00']
            for i in time1:
                self.app.method.TimeBox("OFF", i, '2')
            time2 = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00']
            for i in time2:
                self.app.method.TimeBox("ON", i, '2')

    # Метод проверки сохранения SMS пользователю - РЕЗЕРВ 1 - максимальное значение
    def assert_save_sms_egida_timetable_rezerv_1_max(self):
        with allure.step("Проверка ввода значений в поле Номер телефона - код"):
            self.app.method.assertValues('7777', TEL_COD_rezerv_1)
        with allure.step("Проверка ввода значений в поле Номер телефона - номер"):
            self.app.method.assertValuesPhoneNum('(999)999-99-99', TEL_NUM_rezerv_1)
        with allure.step("Проверка ввода значений в поле Таймаут при ошибке"):
            self.app.method.assertValues('23:59', Timeout_on_error_rezerv_1)
        with allure.step("Проверка выбора из выпадающего списка Тестировать если"):
            self.app.method.assertSelectionDropdownList("Канал активен", test_IF_sms_egidrezerv_1)
        with allure.step("Проверка выбора из выпадающего списка Метод тестирования"):
            self.app.method.assertSelectionDropdownList("Звонок", test_method_sms_egida_rezerv_1)
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(testing_sms_egida_main, 'С интервалом')
            self.app.method.selectDropdownListByName(testing_sms_egida_rezerv_1, 'По расписанию')
        with allure.step("Проверка выбора из выпадающего списка Дни недели"):
            days = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
            wd = self.app.wd
            for i in days:
                element = wd.find_element(By.XPATH, days_of_the_week_main).get_property("textContent")
                assert str(i) in str(
                    element), f"\nОжидаемое значение в выпадающем списке: '{i}'\nФактическое: '{element}'"
        with allure.step("Проверка выбора времени"):
            time1 = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00']
            for i in time1:
                self.app.method.assertTimeBox("ON", i, '2')

    # Метод сохранения SMS пользователю - РЕЗЕРВ 2 - максимальное значение
    def save_sms_user_timetable_rezerv_2_max(self):
        with allure.step("Ввод значений в поле Номер телефона - код"):
            self.app.method.inputValues('+7777', TEL_COD_rezerv_2)
        with allure.step("Ввод значений в поле Номер телефона - номер"):
            self.app.method.inputValues('(999)999-99-99', TEL_NUM_rezerv_2)
        with allure.step("Выбор из выпадающего списка Язык"):
            self.app.method.selectDropdownListByName(lang_rezerv_2, "Английский")
        with allure.step("Выбор чекбокса Отправлять время события"):
            self.app.method.checkBox("ON", rezerv_2_Send_event_time_click, rezerv_2_Send_event_time_status)
        with allure.step("Выбор чекбокса Отправлять дату события"):
            self.app.method.checkBox("ON", rezerv_2_Send_event_data_click, rezerv_2_Send_event_data_status)
        with allure.step("Ввод значений в поле Таймаут при ошибке"):
            self.app.method.inputValues('23:59', Timeout_on_error_rezerv_2)
        with allure.step("Выбор из выпадающего списка Тестировать если"):
            self.app.method.selectDropdownListByName(test_IF_rezerv_2, "Канал активен")
        with allure.step("Выбор из выпадающего списка Метод тестирования"):
            self.app.method.selectDropdownListByName(test_method_rezerv_2, "Звонок")
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(testing_rezerv_2, 'По расписанию')
        with allure.step("Выбор из выпадающего списка Дни недели"):
            self.choice_all_days(days_of_the_week_rezerv_2)
        with allure.step("Выбор времени"):
            time_off = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00',
                        '10:00',
                        '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00',
                        '21:00',
                        '22:00', '23:00']
            for i in time_off:
                self.app.method.TimeBox("OFF", i, '3')
            time2 = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00']
            for i in time2:
                self.app.method.TimeBox("ON", i, '3')

    # Метод проверки сохранения SMS пользователю - РЕЗЕРВ 2 - максимальное значение
    def assert_save_sms_user_timetable_rezerv_2_max(self):
        with allure.step("Проверка ввода значений в поле Номер телефона - код"):
            self.app.method.assertValues('7777', TEL_COD_rezerv_2)
        with allure.step("Проверка ввода значений в поле Номер телефона - номер"):
            self.app.method.assertValuesPhoneNum('(999)999-99-99', TEL_NUM_rezerv_2)
        with allure.step("Проверка выбора из выпадающего списка Язык"):
            self.app.method.assertSelectionDropdownList("Английский", lang_rezerv_2)
        with allure.step("Проверка выбора чек-бокса Отправлять время события"):
            self.app.method.assertCheckBox("ON", rezerv_2_Send_event_time_status)
        with allure.step("Проверка выбора чек-бокса Отправлять дату события"):
            self.app.method.assertCheckBox("ON", rezerv_2_Send_event_data_status)
        with allure.step("Проверка ввода значений в поле Таймаут при ошибке"):
            self.app.method.assertValues('23:59', Timeout_on_error_rezerv_2)
        with allure.step("Проверка выбора из выпадающего списка Тестировать если"):
            self.app.method.assertSelectionDropdownList("Канал активен", test_IF_rezerv_2)
        with allure.step("Проверка выбора из выпадающего списка Метод тестирования"):
            self.app.method.assertSelectionDropdownList("Звонок", test_method_rezerv_2)
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(testing_rezerv_2, 'По расписанию')
        with allure.step("Проверка выбора из выпадающего списка Дни недели"):
            days = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
            wd = self.app.wd
            for i in days:
                element = wd.find_element(By.XPATH, days_of_the_week_rezerv_2).get_property("textContent")
                assert str(i) in str(
                    element), f"\nОжидаемое значение в выпадающем списке: '{i}'\nФактическое: '{element}'"
        with allure.step("Проверка выбора времени"):
            time1 = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00']
            for i in time1:
                self.app.method.assertTimeBox("ON", i, '3')

    # Метод проверки сохранения SMS пользователю - РЕЗЕРВ 1
    def assert_save_sms_user_timetable_rezerv_1(self):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Проверка ввода значений в поле Номер телефона - код"):
            self.app.method.assertValues(_directions['Phone_cod'], TEL_COD_rezerv_1)
        with allure.step("Проверка ввода значений в поле Номер телефона - номер"):
            self.app.method.assertValuesPhoneNum(_directions['Phone_number'], TEL_NUM_rezerv_1)
        with allure.step("Проверка выбора из выпадающего списка Язык"):
            self.app.method.assertSelectionDropdownList(_directions['Lang'], lang_rezerv_1)
        with allure.step("Проверка выбора чек-бокса Отправлять время события"):
            self.app.method.assertCheckBox(_directions['Send_event_time'], rezerv_1_Send_event_time_status)
        with allure.step("Проверка выбора чек-бокса Отправлять дату события"):
            self.app.method.assertCheckBox(_directions['Send_event_date'], rezerv_1_Send_event_data_status)
        with allure.step("Проверка ввода значений в поле Таймаут при ошибке"):
            self.app.method.assertValues(_directions['Timeout_on_error'], Timeout_on_error_rezerv_1)
        with allure.step("Проверка выбора из выпадающего списка Тестировать если"):
            self.app.method.assertSelectionDropdownList(_directions['Test_if'], test_IF_rezerv_1)
        with allure.step("Проверка выбора из выпадающего списка Метод тестирования"):
            self.app.method.assertSelectionDropdownList(_directions['Test_method'], test_method_rezerv_1)
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(testing_main, 'По расписанию')
            self.app.method.selectDropdownListByName(testing_rezerv_1, 'По расписанию')
        with allure.step("Проверка выбора из выпадающего списка Дни недели"):
            day = _directions['Days_of_the_week']
            wd = self.app.wd
            element = wd.find_element(By.XPATH, days_of_the_week_rezerv_1).get_property("textContent")
            assert str(day) in str(
                element), f"\nОжидаемое значение в выпадающем списке: '{day}'\nФактическое: '{element}'"
        with allure.step("Проверка выбора времени"):
            self.app.method.assertTimeBox("ON", _directions['Time'], '2')

    # Метод сохранения SMS пользователю - РЕЗЕРВ 2
    def save_sms_user_rezerv_2(self):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Ввод значений в поле Номер телефона - код"):
            self.app.method.inputValues(_directions['Phone_cod'], TEL_COD_rezerv_2)
        with allure.step("Ввод значений в поле Номер телефона - номер"):
            self.app.method.inputValues(_directions['Phone_number'], TEL_NUM_rezerv_2)
        with allure.step("Выбор из выпадающего списка Язык"):
            self.app.method.selectDropdownListByName(lang_rezerv_2, _directions['Lang'])
        with allure.step("Выбор чекбокса Отправлять время события"):
            self.app.method.checkBox(_directions['Send_event_time'], rezerv_2_Send_event_time_click,
                                     rezerv_2_Send_event_time_status)
        with allure.step("Выбор чекбокса Отправлять дату события"):
            self.app.method.checkBox(_directions['Send_event_date'], rezerv_2_Send_event_data_click,
                                     rezerv_2_Send_event_data_status)
        with allure.step("Ввод значений в поле Таймаут при ошибке"):
            self.app.method.inputValues(_directions['Timeout_on_error'], Timeout_on_error_rezerv_2)
        with allure.step("Выбор из выпадающего списка Тестировать если"):
            self.app.method.selectDropdownListByName(test_IF_rezerv_2, _directions['Test_if'])
        with allure.step("Выбор из выпадающего списка Метод тестирования"):
            self.app.method.selectDropdownListByName(test_method_rezerv_2, _directions['Test_method'])
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(testing_main, 'С интервалом')
            self.app.method.selectDropdownListByName(testing_rezerv_1, 'С интервалом')
            self.app.method.selectDropdownListByName(testing_rezerv_2, 'С интервалом')
        with allure.step("Ввод значений в поле Интервал тестирования"):
            self.app.method.inputValues(_directions['Test_interval'], Test_interval_rezerv_2)

    # Метод проверки сохранения SMS пользователю - РЕЗЕРВ 2
    def assert_save_sms_user_rezerv_2(self):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Проверка ввода значений в поле Номер телефона - код"):
            self.app.method.assertValues(_directions['Phone_cod'], TEL_COD_rezerv_2)
        with allure.step("Проверка ввода значений в поле Номер телефона - номер"):
            self.app.method.assertValuesPhoneNum(_directions['Phone_number'], TEL_NUM_rezerv_2)
        with allure.step("Проверка выбора из выпадающего списка Язык"):
            self.app.method.assertSelectionDropdownList(_directions['Lang'], lang_rezerv_2)
        with allure.step("Проверка выбора чек-бокса Отправлять время события"):
            self.app.method.assertCheckBox(_directions['Send_event_time'], rezerv_2_Send_event_time_status)
        with allure.step("Проверка выбора чек-бокса Отправлять дату события"):
            self.app.method.assertCheckBox(_directions['Send_event_date'], rezerv_2_Send_event_data_status)
        with allure.step("Проверка ввода значений в поле Таймаут при ошибке"):
            self.app.method.assertValues(_directions['Timeout_on_error'], Timeout_on_error_rezerv_2)
        with allure.step("Проверка выбора из выпадающего списка Тестировать если"):
            self.app.method.assertSelectionDropdownList(_directions['Test_if'], test_IF_rezerv_2)
        with allure.step("Проверка выбора из выпадающего списка Метод тестирования"):
            self.app.method.assertSelectionDropdownList(_directions['Test_method'], test_method_rezerv_2)
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(testing_main, 'С интервалом')
            self.app.method.selectDropdownListByName(testing_rezerv_1, 'С интервалом')
            self.app.method.selectDropdownListByName(testing_rezerv_2, 'С интервалом')
        with allure.step("Проверка ввода значений в поле Интервал тестирования"):
            self.app.method.assertValues(_directions['Test_interval'], Test_interval_rezerv_2)

    # Метод сохранения SMS пользователю - РЕЗЕРВ 2
    def save_sms_user_timetable_rezerv_2(self):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Ввод значений в поле Номер телефона - код"):
            self.app.method.inputValues(_directions['Phone_cod'], TEL_COD_rezerv_2)
        with allure.step("Ввод значений в поле Номер телефона - номер"):
            self.app.method.inputValues(_directions['Phone_number'], TEL_NUM_rezerv_2)
        with allure.step("Выбор из выпадающего списка Язык"):
            self.app.method.selectDropdownListByName(lang_rezerv_2, _directions['Lang'])
        with allure.step("Выбор чекбокса Отправлять время события"):
            self.app.method.checkBox(_directions['Send_event_time'], rezerv_2_Send_event_time_click,
                                     rezerv_2_Send_event_time_status)
        with allure.step("Выбор чекбокса Отправлять дату события"):
            self.app.method.checkBox(_directions['Send_event_date'], rezerv_2_Send_event_data_click,
                                     rezerv_2_Send_event_data_status)
        with allure.step("Ввод значений в поле Таймаут при ошибке"):
            self.app.method.inputValues(_directions['Timeout_on_error'], Timeout_on_error_rezerv_2)
        with allure.step("Выбор из выпадающего списка Тестировать если"):
            self.app.method.selectDropdownListByName(test_IF_rezerv_2, _directions['Test_if'])
        with allure.step("Выбор из выпадающего списка Метод тестирования"):
            self.app.method.selectDropdownListByName(test_method_rezerv_2, _directions['Test_method'])
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(testing_main, 'По расписанию')
            self.app.method.selectDropdownListByName(testing_rezerv_1, 'По расписанию')
            self.app.method.selectDropdownListByName(testing_rezerv_2, 'По расписанию')
        with allure.step("Выбор из выпадающего списка Дни недели"):
            day = _directions['Days_of_the_week']
            self.app.method.close_cross(days_of_the_week_rezerv_2)
            self.app.method.go_to_element(f'/html/body//div[@class="b-multiselect-item"]/span[.="{day}"]', 'true')
            self.app.method.click((By.XPATH, f'/html/body//div[@class="b-multiselect-item"]/span[.="{day}"]'))
            self.app.method.click((By.XPATH, days_of_the_week_rezerv_2))
        with allure.step("Выбор времени"):
            time_off = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00',
                        '10:00',
                        '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00',
                        '21:00',
                        '22:00', '23:00']
            for i in time_off:
                self.app.method.TimeBox("OFF", i, '3')
            self.app.method.TimeBox("ON", _directions['Time'], '3')

    # Метод проверки сохранения SMS пользователю - РЕЗЕРВ 2
    def assert_save_sms_user_timetable_rezerv_2(self):
        with allure.step("Парсинг сгенерированных данных"):
            _directions = self.app.read_data.data_directions()
        with allure.step("Проверка ввода значений в поле Номер телефона - код"):
            self.app.method.assertValues(_directions['Phone_cod'], TEL_COD_rezerv_2)
        with allure.step("Проверка ввода значений в поле Номер телефона - номер"):
            self.app.method.assertValuesPhoneNum(_directions['Phone_number'], TEL_NUM_rezerv_2)
        with allure.step("Проверка выбора из выпадающего списка Язык"):
            self.app.method.assertSelectionDropdownList(_directions['Lang'], lang_rezerv_2)
        with allure.step("Проверка выбора чек-бокса Отправлять время события"):
            self.app.method.assertCheckBox(_directions['Send_event_time'], rezerv_2_Send_event_time_status)
        with allure.step("Проверка выбора чек-бокса Отправлять дату события"):
            self.app.method.assertCheckBox(_directions['Send_event_date'], rezerv_2_Send_event_data_status)
        with allure.step("Проверка ввода значений в поле Таймаут при ошибке"):
            self.app.method.assertValues(_directions['Timeout_on_error'], Timeout_on_error_rezerv_2)
        with allure.step("Проверка выбора из выпадающего списка Тестировать если"):
            self.app.method.assertSelectionDropdownList(_directions['Test_if'], test_IF_rezerv_2)
        with allure.step("Проверка выбора из выпадающего списка Метод тестирования"):
            self.app.method.assertSelectionDropdownList(_directions['Test_method'], test_method_rezerv_2)
        with allure.step("Выбор из выпадающего списка Тестировать"):
            self.app.method.selectDropdownListByName(testing_main, 'По расписанию')
            self.app.method.selectDropdownListByName(testing_rezerv_1, 'По расписанию')
            self.app.method.selectDropdownListByName(testing_rezerv_2, 'По расписанию')
        with allure.step("Проверка выбора из выпадающего списка Дни недели"):
            day = _directions['Days_of_the_week']
            wd = self.app.wd
            element = wd.find_element(By.XPATH, days_of_the_week_rezerv_2).get_property("textContent")
            assert str(day) in str(
                element), f"\nОжидаемое значение в выпадающем списке: '{day}'\nФактическое: '{element}'"
        with allure.step("Проверка выбора времени"):
            self.app.method.assertTimeBox("ON", _directions['Time'], '3')

    def choose_type_of_control_and_fill_form(self, type_control):
        self.app.PO_Directions.openType_main(type_control)
        if type_control != 'DC09':
            self.app.method.inputValues('+7', TEL_COD_main)
            self.app.method.inputValues('(111)111-11-11', TEL_NUM_main)
            if type_control == 'Звонок':
                self.app.method.inputValues('15', count_reset_main)
        else:
            self.app.method.inputValues('http//ya.ru', address_DC09_main)
            self.app.method.inputValues('5566', port_DC09_main)
            self.app.method.inputValues('22', confirmation_timeout_DC09_main)

