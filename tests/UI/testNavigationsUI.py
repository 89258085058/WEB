# -*- coding: utf-8 -*-
import allure
import pytest

reruns = 2


@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты НАВИГАЦИЯ")
@pytest.mark.flaky(reruns=reruns)
class TestNavigations:

    @allure.title("Вкладка Журнал по умолчанию")
    def test_main_endppoint(self, app):
        with allure.step("Проверка перехода на вкладку Журнал при входе в приложение"):
            app.PO_Navigations.assert_main_page_journal()

    @allure.title("Главные вкладки")
    def test_navigate_main_pages(self, app):
        with allure.step("Переход на страницу Зоны Разделы"):
            app.PO_Navigations.goToZonePathPage()
        with allure.step("Переход на страницу Настройки"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на страницу Пользователи и ключи"):
            app.PO_Navigations.goToUsersKeysPage()
        with allure.step("Переход на страницу Направления"):
            app.PO_Navigations.goToDirectionsPage()
        with allure.step("Переход на страницу Статус"):
            app.PO_Navigations.goToStatusPage()
        with allure.step("Переход на страницу Обновления"):
            app.PO_Navigations.goToUpdatePage()
        with allure.step("Переход на страницу Журнал"):
            app.PO_Navigations.goToJournalPage()

    @allure.title("Проверка навигации: вкадака 'Настройки'")
    def test_navigate_settings_page(self, app):
        with allure.step("Переход на страницу 'Настройки'"):
            app.PO_Navigations.goToSettingsPage()
        with allure.step("Переход на вкладку 'Объект'"):
            app.PO_Navigations.goToObjectPage()
        with allure.step("Переход на вкладку 'Дата и Время'"):
            app.PO_Navigations.goToDateTimePage()
        with allure.step("Переход на вкладку 'Прибор'"):
            app.PO_Navigations.goToDevicePage()
        with allure.step("Переход на вкладку 'Световая индикация'"):
            app.PO_Navigations.goToLightIndicationPage()
        with allure.step("Переход на вкладку 'Звуковая индикация'"):
            app.PO_Navigations.goToVolumIndicationPage()
        with allure.step("Переход на вкладку 'Радио'"):
            app.PO_Navigations.goToRadioPage()
        with allure.step("Переход на вкладку 'GSM'"):
            app.PO_Navigations.goToGSMPage()
        with allure.step("Переход на вкладку 'ETHERNET'"):
            app.PO_Navigations.goToEthernetPage()
