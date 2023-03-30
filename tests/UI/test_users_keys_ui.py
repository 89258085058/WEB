# -*- coding: utf-8 -*-

import allure
import pytest
from selenium.webdriver.common.by import By

reruns = 1


@pytest.fixture
def users(app):
    with allure.step("Переход на страницу Пользователи и ключи"):
        app.PO_Navigations.goToUsersKeysPage()
    with allure.step("Переход на вкладку 'Пользователи'"):
        app.PO_Navigations.goToUsersPage()
    with allure.step("Нажать на кнопку 'Добавить пользователя'"):
        app.PO_Users_Keys.PushAddKeyButton()


@pytest.fixture
def users_settings(app):
    with allure.step("Переход на страницу Пользователи и ключи"):
        app.PO_Navigations.goToUsersKeysPage()
    with allure.step("Переход на вкладку 'Пользователи'"):
        app.PO_Navigations.goToUsersPage()
    with allure.step("Нажать на кнопку 'Настройки'"):
        app.PO_Users_Keys.PushUserSettingsButton()


@pytest.fixture
def keys(app):
    with allure.step("Переход на страницу Пользователи и ключи"):
        app.PO_Navigations.goToUsersKeysPage()
    with allure.step("Переход на вкладку 'Ключи'"):
        app.PO_Navigations.goToKeysPage()
    with allure.step("Нажать на кнопку 'Добавить ключ'"):
        app.PO_Users_Keys.PushAddKeyButton()


@pytest.fixture
def keys_settings(app):
    with allure.step("Переход на страницу Пользователи и ключи"):
        app.PO_Navigations.goToUsersKeysPage()
    with allure.step("Переход на вкладку 'Ключи'"):
        app.PO_Navigations.goToKeysPage()
    with allure.step("Добавление ключа при его отсутствии"):
        app.PO_Users_Keys.Add_key_if_not()
    with allure.step("Нажать на кнопку 'Настройки'"):
        app.PO_Users_Keys.PushKeysSettingsButton()


@pytest.fixture()
def close_modal(request, app):
    def fin():
        app.method.click((By.XPATH, '(//*[.=" Отменить "]//div)[last()]'))

    request.addfinalizer(fin)

@pytest.mark.skip("Неактуальные тесты по UI запускать при появлении свободного времени")
@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты ПОЛЬЗОВАТЕЛИ И КЛЮЧИ")
@allure.feature("Проверки UI")
@pytest.mark.flaky(reruns=reruns)
class TestUsersKeysUI:

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Проверка чек-боксов добавления пользователя (Добавить пользователя)")
    def test_user_checkbox_user_add(self, app, users, close_modal):
        with allure.step("Проверка включения чекбоксов"):
            app.PO_Users_Keys.check_box_users_add_on()
        with allure.step("Проверка выключения чекбоксов"):
            app.PO_Users_Keys.check_box_users_add_off()
        with allure.step("Проверка частичного выбора чекбоксов"):
            app.PO_Users_Keys.check_box_users_add_some()

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Проверка названий полей на странице")
    def test_main_title_users_add(self, app, users, close_modal):
        with allure.step("Проверка названий полей Добавить пользователя (Добавить пользователя)"):
            app.PO_Users_Keys.text_add_users()

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Проверка выпадающего списка: Группа выходов с управлением звонком (Добавить пользователя)")
    def test_dropdown_list_group_of_outputs_with_call_control(self, app, users, close_modal):
        with allure.step("Проверка выбора позиций из выпадающего списка"):
            app.PO_Users_Keys.drop_list_group_of_outputs_with_call_control()

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Проверка выпадающего списка: Группа выходов с управлением по SMS (Добавить пользователя)")
    def test_dropdown_list_group_of_outputs_controlled_by_SMS(self, app, users, close_modal):
        with allure.step("Проверка выбора позиций из выпадающего списка"):
            app.PO_Users_Keys.drop_list_group_of_outputs_controlled_by_SMS()

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Проверка выпадающего списка: Управляемые по SMS разделы (Добавить пользователя)")
    def test_dropdown_list_SMS_controlled_sections(self, app, users, close_modal):
        with allure.step("Проверка выбора позиций из выпадающего списка"):
            app.PO_Users_Keys.drop_list_SMS_controlled_sections()

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Проверка чек-боксов добавления пользователя (Настройки пользователя)")
    def test_user_checkbox_user_add_user_settings(self, app, users_settings, close_modal):
        with allure.step("Проверка включения чекбоксов"):
            app.PO_Users_Keys.check_box_users_add_on()
        with allure.step("Проверка выключения чекбоксов"):
            app.PO_Users_Keys.check_box_users_add_off()
        with allure.step("Проверка частичного выбора чекбоксов"):
            app.PO_Users_Keys.check_box_users_add_some()

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Проверка названий полей на странице (Настройки пользователя)")
    def test_main_title_users_add_user_settings(self, app, users_settings, close_modal):
        with allure.step("Проверка названий полей Добавить пользователя "):
            app.PO_Users_Keys.text_add_users()

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Проверка выпадающего списка: Группа выходов с управлением звонком (Настройки пользователя)")
    def test_dropdown_list_group_of_outputs_with_call_control_user_settings(self, app, users_settings, close_modal):
        with allure.step("Проверка выбора позиций из выпадающего списка"):
            app.PO_Users_Keys.drop_list_group_of_outputs_with_call_control()

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Проверка выпадающего списка: Группа выходов с управлением по SMS (Настройки пользователя)")
    def test_dropdown_list_group_of_outputs_controlled_by_SMS_user_settings(self, app, users_settings, close_modal):
        with allure.step("Проверка выбора позиций из выпадающего списка"):
            app.PO_Users_Keys.drop_list_group_of_outputs_controlled_by_SMS()

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Проверка выпадающего списка: Управляемые по SMS разделы (Настройки пользователя)")
    def test_dropdown_list_SMS_controlled_sections_user_settings(self, app, users_settings, close_modal):
        with allure.step("Проверка выбора позиций из выпадающего списка"):
            app.PO_Users_Keys.drop_list_SMS_controlled_sections()

    @allure.story("КЛЮЧИ")
    @allure.title("Проверка названий полей на странице (Добавить ключ)")
    def test_main_title_keys(self, app, keys, close_modal):
        with allure.step("Проверка названий полей Добавить ключ"):
            app.PO_Users_Keys.text_add_keys()

    @allure.story("КЛЮЧИ")
    @allure.title("Проверка выпадающего списка: Разрешения (Добавить ключ)")
    def test_dropdown_list_permissions_keys(self, app, keys, close_modal):
        with allure.step("Проверка выбора позиций из выпадающего списка"):
            app.PO_Users_Keys.dropdown_list_permissions_keys()

    @allure.story("КЛЮЧИ")
    @allure.title("Проверка выпадающего списка: Разделы (Добавить ключ)")
    def test_dropdown_list_path_keys(self, app, keys, close_modal):
        with allure.step("Проверка выбора позиций из выпадающего списка"):
            app.PO_Users_Keys.dropdown_list_path_keys()

    @allure.story("КЛЮЧИ")
    @allure.title("Проверка названий полей на странице (Настройки ключа)")
    def test_main_title_keys_settings(self, app, keys_settings, close_modal):
        with allure.step("Проверка названий полей Настройки ключа"):
            app.PO_Users_Keys.text_settings_keys()

    @allure.story("КЛЮЧИ")
    @allure.title("Проверка выпадающего списка: Разрешения (Настройки ключа)")
    def test_dropdown_list_permissions_keys_settings(self, app, keys_settings, close_modal):
        with allure.step("Проверка выбора позиций из выпадающего списка"):
            app.PO_Users_Keys.dropdown_list_permissions_keys()

    @allure.story("КЛЮЧИ")
    @allure.title("Проверка выпадающего списка: Разделы (Настройки ключа)")
    def test_dropdown_list_path_keys_settings(self, app, keys_settings, close_modal):
        with allure.step("Проверка выбора позиций из выпадающего списка"):
            app.PO_Users_Keys.dropdown_list_path_keys()
