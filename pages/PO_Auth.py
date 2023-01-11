# -*- coding: utf-8 -*-

from dataclasses import dataclass

import allure

from data.pages_text import data_auth
from locators.auth_locators import *


@dataclass
class AuthHelper:
    app: any

    # Проверка полей на странице Авторизации
    def text_auth_page(self):
        self.app.method.assertTextOnPage(auth_text, data_auth)

    # Проверка ввода поле Логин
    def input_login(self, locator=login_input):
        with allure.step("Проверка ввода цифр"):
            for i in range(10):
                self.app.method.assertEqual(i, i, locator)
        with allure.step("Проверка ввода латинских букв в нижнем регистре"):
            self.app.method.assertEqual('abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz',
                                        locator)
        with allure.step("Проверка ввода латинских букв в врхнем регистре"):
            self.app.method.assertEqual('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                                        locator)
        with allure.step("Проверка ввода граничных значений внутри диапазона"):
            self.app.method.assertEqual(0, 0, locator)
            self.app.method.assertEqual(1, 1, locator)
            self.app.method.assertEqual('1' * 62, '1' * 62, locator)
            self.app.method.assertEqual('1' * 63, '1' * 63, locator)

    # Проверка ввода поле Логин
    def input_login_negativ(self, locator=login_input):
        with allure.step("Проверка ввода граничных значений внутри диапазона"):
            with allure.step("Проверка ввода Русских букв в нижнем регистре"):
                self.app.method.assertEqual("ёйцукенгшщзхъфыв", "", locator)
                self.app.method.assertEqual("апролджэячсмитьбю", "", locator)
            with allure.step("Проверка ввода Русских букв в верхнем регистре"):
                self.app.method.assertEqual("АПРОЛДЖЭЯЧСМИТЬБЮ", "", locator)
                self.app.method.assertEqual("ЁЙЦУКЕНГШЩЗХЪФЫВ", "", locator)
            with allure.step("Проверка ввода спецсимполов"):
                self.app.method.assertEqual("!#$%&'()*+,-./:;<=>?@[]^_`{|}~", "", locator)
            with allure.step("Проверка ввода совместных значений"):
                self.app.method.assertEqual('123  АБВABC!@#', '123ABC', locator)
            with allure.step("Проверка ввода пустого значения"):
                self.app.method.assertEqual('', '', locator)
            with allure.step("Проверка ввода пробелов"):
                self.app.method.assertEqual('   ', '', locator)
                self.app.method.assertEqual('123     ', '123', locator)
                self.app.method.assertEqual('   123', '123', locator)
                self.app.method.assertEqual('1 2 3', '123', locator)
            with allure.step("Проверка ввода граничных значений внутри диапазона"):
                self.app.method.assertEqual('1' * 64, '1' * 63, locator)

    # Проверка ввода поле Пароль
    def input_password(self, locator=password_input):
        with allure.step("Проверка ввода цифр"):
            for i in range(10):
                self.app.method.assertEqual(i, i, locator)
        with allure.step("Проверка ввода латинских букв в нижнем регистре"):
            self.app.method.assertEqual('abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz',
                                        locator)
        with allure.step("Проверка ввода латинских букв в врхнем регистре"):
            self.app.method.assertEqual('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                                        locator)
        with allure.step("Проверка ввода спецсимполов"):
            self.app.method.assertEqual("!#$%&()*+,-.:;<=>?@[]^_{|}~",
                                        "!#$%&()*+,-.:;<=>?@[]^_{|}~", locator)
        with allure.step("Проверка ввода граничных значений внутри диапазона"):
            self.app.method.assertEqual(0, 0, locator)
            self.app.method.assertEqual(1, 1, locator)
            self.app.method.assertEqual('1' * 62, '1' * 62, locator)
            self.app.method.assertEqual('1' * 63, '1' * 63, locator)

    # Проверка ввода поле Логин
    def input_password_negativ(self, locator=password_input):
        with allure.step("Проверка ввода граничных значений внутри диапазона"):
            with allure.step("Проверка ввода Русских букв в нижнем регистре"):
                self.app.method.assertEqual("ёйцукенгшщзхъфыв", "", locator)
                self.app.method.assertEqual("апролджэячсмитьбю", "", locator)
            with allure.step("Проверка ввода Русских букв в верхнем регистре"):
                self.app.method.assertEqual("АПРОЛДЖЭЯЧСМИТЬБЮ", "", locator)
                self.app.method.assertEqual("ЁЙЦУКЕНГШЩЗХЪФЫВ", "", locator)
            with allure.step("Проверка ввода спецсимполов"):
                self.app.method.assertEqual("!#$%&'()*+,-./:;<=>?@[]^_`{|}~",
                                            "!#$%&()*+,-.:;<=>?@[]^_{|}~", locator)
            with allure.step("Проверка ввода совместных значений"):
                self.app.method.assertEqual('123  АБВABC!@#', '123ABC!@#', locator)
            with allure.step("Проверка ввода пустого значения"):
                self.app.method.assertEqual('', '', locator)
            with allure.step("Проверка ввода пробелов"):
                self.app.method.assertEqual('   ', '', locator)
                self.app.method.assertEqual('123     ', '123', locator)
                self.app.method.assertEqual('   123', '123', locator)
                self.app.method.assertEqual('1 2 3', '123', locator)
            with allure.step("Проверка ввода граничных значений внутри диапазона"):
                self.app.method.assertEqual('1' * 64, '1' * 63, locator)
