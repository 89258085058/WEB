# -*- coding: utf-8 -*-

import allure
import pytest

reruns = 1


@pytest.fixture
def StatusPage(app):
    with allure.step("Переход на страницу Статус"):
        app.PO_Navigations.goToStatusPage()


@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты СТАТУС")
@allure.feature("Проверки UI")
@pytest.mark.flaky(reruns=reruns)
class TestStatusUI:

    @allure.story("Проверка названий полей на странице")
    @allure.title("Радио устройства")
    def test_title_status_radio_device(self, app, StatusPage):
        with allure.step("Проверка названий полей"):
            app.PO_Status.text_status_radio_device()

    @allure.story("Проверка названий полей на странице")
    @allure.title("Прибор")
    def test_title_status_device_option(self, app, StatusPage):
        with allure.step("Проверка названий полей"):
            app.PO_Status.text_status_device_option()

    @allure.story("Проверка названий полей на странице")
    @allure.title("Прочее")
    def test_title_cloud_server(self, app, StatusPage):
        with allure.step("Проверка названий полей"):
            app.PO_Status.text_status_cloud_server()

    @allure.story("Проверка названий полей на странице")
    @allure.title("Сеть")
    def test_title_status_ethernet(self, app, StatusPage):
        with allure.step("Проверка названий полей"):
            app.PO_Status.text_status_ethernet()

    @allure.story("Проверка названий полей на странице")
    @allure.title("Состояние GSM модуля")
    def test_title_status_gsm(self, app, StatusPage):
        with allure.step("Проверка названий полей"):
            app.PO_Status.text_status_gsm()








