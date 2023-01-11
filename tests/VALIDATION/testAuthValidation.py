# -*- coding: utf-8 -*-

import allure
import pytest

reruns = 2


@pytest.fixture(scope="class")
def go_to_auth_page(app):
    with allure.step("переход на страницу авторизации"):
        app.session.logout()


@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты АВТОРИЗАЦИЯ")
@allure.feature("Валидация полей ввода")
@pytest.mark.flaky(reruns=reruns)
class TestAuthValidation:

    @allure.title("Позитивные проверки: Проверка ввода значений в поле 'Логин'")
    def test_input_login(self, app, go_to_auth_page):
        with allure.step("Проверка валидации поля"):
            app.PO_Auth.input_login()

    @allure.title("Негитивные проверки: Проверка ввода значений в поле 'Логин'")
    def test_input_login_negativ(self, app, go_to_auth_page):
        with allure.step("Проверка валидации поля"):
            app.PO_Auth.input_login_negativ()

    @allure.title("Позитивные проверки: Проверка ввода значений в поле 'Пароль'")
    def test_input_password(self, app, go_to_auth_page):
        with allure.step("Проверка валидации поля"):
            app.PO_Auth.input_password()

    @allure.title("Негитивные проверки: Проверка ввода значений в поле 'Пароль'")
    def test_input_password_negativ(self, app, go_to_auth_page):
        with allure.step("Проверка валидации поля"):
            app.PO_Auth.input_password_negativ()
