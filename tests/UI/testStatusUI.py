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
    @allure.title("Разделы")
    def test_title_status_path(self, app, StatusPage):
        with allure.step("Проверка названий полей"):
            app.PO_Status.text_status_path()

    @allure.story("Проверка названий полей на странице")
    @allure.title("Батареи")
    def test_title_status_batteries(self, app, StatusPage):
        with allure.step("Проверка названий полей"):
            app.PO_Status.text_status_batteries()

    @allure.story("Проверка названий полей на странице")
    @allure.title("Состояние GSM модуля")
    def test_title_status_gsm(self, app, StatusPage):
        with allure.step("Проверка названий полей"):
            app.PO_Status.text_status_gsm()

    @allure.story("Проверка названий полей на странице")
    @allure.title("Источник питания")
    def test_title_status_power(self, app, StatusPage):
        with allure.step("Проверка названий полей"):
            app.PO_Status.text_status_power()

    @allure.story("Проверка названий полей на странице")
    @allure.title("Сеть")
    def test_title_status_ethernet(self, app, StatusPage):
        with allure.step("Проверка названий полей"):
            app.PO_Status.text_status_ethernet()

    @allure.story("Проверка названий полей на странице")
    @allure.title("Состояние прибора")
    def test_title_status_device(self, app, StatusPage):
        with allure.step("Проверка названий полей"):
            app.PO_Status.text_status_device()

    @allure.story("Проверка названий полей на странице")
    @allure.title("Прочее")
    def test_title_status_others(self, app, StatusPage):
        with allure.step("Проверка названий полей"):
            app.PO_Status.text_status_others()

    @allure.story("Проверка названий полей на странице")
    @allure.title("Прибор")
    def test_title_status_device_option(self, app, StatusPage):
        with allure.step("Проверка названий полей"):
            app.PO_Status.text_status_device_option()

