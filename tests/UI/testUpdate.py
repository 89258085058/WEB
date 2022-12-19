# -*- coding: utf-8 -*-

import allure
import pytest

reruns = 1


@pytest.fixture
def updatePage(app):
    with allure.step("Переход на страницу Обновления"):
        app.PO_Navigations.goToUpdatePage()

@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты ОБНОВЛЕНИЯ")
@allure.feature("Проверки UI")
@pytest.mark.flaky(reruns=reruns)
class TestUpdateUI:

    @allure.story("Проверка названий полей на странице")
    @allure.title("Сигнал GSM Р исп. 0 изм.7")
    def test_title_update_device(self, app, updatePage):
        with allure.step("Проверка названий полей"):
            app.PO_Update.text_update_device()

    @allure.story("Проверка названий полей на странице")
    @allure.title("Обновление прошивки")
    def test_title_update(self, app, updatePage):
        with allure.step("Проверка названий полей"):
            app.PO_Update.text_update()
