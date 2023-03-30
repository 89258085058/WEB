# -*- coding: utf-8 -*-

import allure
import pytest

reruns = 1


@pytest.fixture(scope="class")
def go_to_auth_page(app):
    with allure.step("переход на страницу авторизации"):
        app.session.logout()


@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты АВТОРИЗАЦИЯ")
@allure.feature("Проверки UI")
@pytest.mark.flaky(reruns=reruns)
class TestAuthUI:

    @allure.title("Проверка названий полей на странице")
    def test_auth_title(self, app, go_to_auth_page):
        with allure.step("Проверка названий полей"):
            app.PO_Auth.text_auth_page()

    @allure.story("Проверка подсказок АВТОРИЗАЦИЯ")
    @allure.title("Проверка всплывающей подсказки поля 'Логин'")
    def test_tooltip_login(self, app, go_to_auth_page):
        with allure.step("Проверка текста подсказки"):
            app.PO_Tooltips.tooltip_login()

    @allure.story("Проверка подсказок АВТОРИЗАЦИЯ")
    @allure.title("Проверка всплывающей подсказки поля 'Пароль'")
    def test_tooltip_password(self, app, go_to_auth_page):
        with allure.step("Проверка текста подсказки"):
            app.PO_Tooltips.tooltip_password()
