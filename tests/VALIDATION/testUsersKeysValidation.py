# -*- coding: utf-8 -*-

import allure
import pytest
from selenium.webdriver.common.by import By

reruns = 2


@pytest.fixture
def users(app):
    with allure.step("Переход на страницу Пользователи и ключи"):
        app.PO_Navigations.goToUsersKeysPage()
    with allure.step("Переход на вкладку 'Пользователи'"):
        app.PO_Navigations.goToUsersPage()
    with allure.step("Нажать на кнопку 'Добавить пользователя'"):
        app.PO_Users_Keys.PushAddUserButton()


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
        app.method.check_hide_element('modal-title', '(//*[.=" Отменить "]//div)[last()]')

    request.addfinalizer(fin)

@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты ПОЛЬЗОВАТЕЛИ И КЛЮЧИ")
@allure.feature("Валидация полей ввода")
@pytest.mark.flaky(reruns=reruns)
class Test01UsersKeysValidation():

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Поиск'")
    def test_user_input_search_user(self, app, extend_time):
        with allure.step("Переход на страницу Пользователи и ключи"):
            app.PO_Navigations.goToUsersKeysPage()
        with allure.step("Проверка валидации поля"):
            app.PO_Users_Keys.input_seach()

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Имя пользователя'(Добавить пользователя)")
    def test_user_input_name_user(self, app, extend_time, users, close_modal):
        with allure.step("Проверка валидации поля"):
            app.PO_Users_Keys.input_name_user()

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Имя пользователя'(Добавить пользователя)")
    def test_user_input_name_user_negativ(self, app, extend_time, users, close_modal):
        with allure.step("Проверка валидации поля"):
            app.PO_Users_Keys.input_name_user_negativ()

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Логин'(Добавить пользователя)")
    def test_user_input_login_user(self, app, extend_time, users, close_modal):
        with allure.step("Проверка валидации поля"):
            app.PO_Users_Keys.input_login_user()

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Логин'(Добавить пользователя)")
    def test_user_input_login_user_negativ(self, app, extend_time, users, close_modal):
        with allure.step("Проверка валидации поля"):
            app.PO_Users_Keys.input_login_user_negativ()

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Пароль'(Добавить пользователя)")
    def test_user_input_password_user(self, app, extend_time, users, close_modal):
        with allure.step("Проверка валидации поля"):
            app.PO_Users_Keys.input_password_user()

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Пароль'(Добавить пользователя)")
    def test_user_input_password_user_negativ(self, app, extend_time, users, close_modal):
        with allure.step("Проверка валидации поля"):
            app.PO_Users_Keys.input_password_user_negativ()

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Повторите пароль'(Добавить пользователя)")
    def test_user_input_re_password_user(self, app, extend_time, users, close_modal):
        with allure.step("Проверка валидации поля"):
            app.PO_Users_Keys.input_re_password_user()

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Повторите пароль'(Добавить пользователя)")
    def test_user_input_re_password_user_negativ(self, app, extend_time, users, close_modal):
        with allure.step("Проверка валидации поля"):
            app.PO_Users_Keys.input_re_password_user_negativ()

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Телефон (КОД)'(Добавить пользователя)")
    def test_user_input_phone_cod_user(self, app, extend_time, users, close_modal):
        with allure.step("Проверка валидации поля"):
            app.PO_Users_Keys.input_phone_cod_user()

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Телефон (КОД)'(Добавить пользователя)")
    def test_user_input_phone_cod_user_negativ(self, app, extend_time, users, close_modal):
        with allure.step("Проверка валидации поля"):
            app.PO_Users_Keys.input_phone_cod_user_negativ()

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Телефон (номер)'(Добавить пользователя)")
    def test_user_input_phone_number_user(self, app, extend_time, users, close_modal):
        with allure.step("Проверка валидации поля"):
            app.PO_Users_Keys.input_phone_number_user()

@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты ПОЛЬЗОВАТЕЛИ И КЛЮЧИ")
@allure.feature("Валидация полей ввода")
@pytest.mark.flaky(reruns=reruns)
class Test02UsersKeysValidation():

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Телефон (номер)'(Добавить пользователя)")
    def test_user_input_phone_number_user_negativ(self, app, extend_time, users, close_modal):
        with allure.step("Проверка валидации поля"):
            app.PO_Users_Keys.input_phone_number_user_negativ()

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Пароль SMS'(Добавить пользователя)")
    def test_user_input_password_sms_user(self, app, extend_time, users, close_modal):
        with allure.step("Проверка валидации поля"):
            app.PO_Users_Keys.input_password_sms_user()

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Пароль SMS'(Добавить пользователя)")
    def test_user_input_phone_password_sms_negativ(self, app, extend_time, users, close_modal):
        with allure.step("Проверка валидации поля"):
            app.PO_Users_Keys.input_password_sms_user_negativ()

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Повторите пароль'(Добавить пользователя)")
    def test_user_input_re_password_sms_user(self, app, extend_time, users, close_modal):
        with allure.step("Проверка валидации поля"):
            app.PO_Users_Keys.input_re_password_sms_user()

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Повторите пароль'(Добавить пользователя)")
    def test_user_input_phone_re_password_sms_negativ(self, app, extend_time, users, close_modal):
        with allure.step("Проверка валидации поля"):
            app.PO_Users_Keys.input_re_password_sms_user_negativ()

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Имя пользователя'(Настройки)")
    def test_user_input_name_user_settings(self, app, extend_time, users_settings, close_modal):
        with allure.step("Проверка валидации поля"):
            app.PO_Users_Keys.input_name_user()

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Имя пользователя'(Настройки)")
    def test_user_input_name_user_negativ_settings(self, app, extend_time, users_settings, close_modal):
        with allure.step("Проверка валидации поля"):
            app.PO_Users_Keys.input_name_user_negativ()

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Логин'(Настройки)")
    def test_user_input_login_user_settings(self, app, extend_time, users_settings, close_modal):
        with allure.step("Проверка валидации поля"):
            app.PO_Users_Keys.input_login_user()

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Логин'(Настройки)")
    def test_user_input_login_user_negativ_settings(self, app, extend_time, users_settings, close_modal):
        with allure.step("Проверка валидации поля"):
            app.PO_Users_Keys.input_login_user_negativ()

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Пароль'(Настройки)")
    def test_user_input_password_user_settings(self, app, extend_time, users_settings, close_modal):
        with allure.step("Проверка валидации поля"):
            app.PO_Users_Keys.input_password_user()

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Пароль'(Настройки)")
    def test_user_input_password_user_negativ_settings(self, app, extend_time, users_settings, close_modal):
        with allure.step("Проверка валидации поля"):
            app.PO_Users_Keys.input_password_user_negativ()

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Повторите пароль'(Настройки)")
    def test_user_input_re_password_user_settings(self, app, extend_time, users_settings, close_modal):
        with allure.step("Проверка валидации поля"):
            app.PO_Users_Keys.input_re_password_user()

@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты ПОЛЬЗОВАТЕЛИ И КЛЮЧИ")
@allure.feature("Валидация полей ввода")
@pytest.mark.flaky(reruns=reruns)
class Test03UsersKeysValidation():

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Повторите пароль'(Настройки)")
    def test_user_input_re_password_user_negativ_settings(self, app, extend_time, users_settings, close_modal):
        with allure.step("Проверка валидации поля"):
            app.PO_Users_Keys.input_re_password_user_negativ()

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Телефон (КОД)'(Настройки)")
    def test_user_input_phone_cod_user_settings(self, app, extend_time, users_settings, close_modal):
        with allure.step("Проверка валидации поля"):
            app.PO_Users_Keys.input_phone_cod_user()

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Телефон (КОД)'(Настройки)")
    def test_user_input_phone_cod_user_negativ_settings(self, app, extend_time, users_settings, close_modal):
        with allure.step("Проверка валидации поля"):
            app.PO_Users_Keys.input_phone_cod_user_negativ()

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Телефон (номер)'(Настройки)")
    def test_user_input_phone_number_user_settings(self, app, extend_time, users_settings, close_modal):
        with allure.step("Проверка валидации поля"):
            app.PO_Users_Keys.input_phone_number_user()

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Телефон (номер)'(Настройки)")
    def test_user_input_phone_number_user_negativ_settings(self, app, extend_time, users_settings, close_modal):
        with allure.step("Проверка валидации поля"):
            app.PO_Users_Keys.input_phone_number_user_negativ()

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Пароль SMS'(Настройки)")
    def test_user_input_password_sms_user_settings(self, app, extend_time, users_settings, close_modal):
        with allure.step("Проверка валидации поля"):
            app.PO_Users_Keys.input_password_sms_user()

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Пароль SMS'(Настройки)")
    def test_user_input_phone_password_sms_negativ_settings(self, app, extend_time, users_settings, close_modal):
        with allure.step("Проверка валидации поля"):
            app.PO_Users_Keys.input_password_sms_user_negativ()

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Повторите пароль'(Настройки)")
    def test_user_input_re_password_sms_user_settings(self, app, extend_time, users_settings, close_modal):
        with allure.step("Проверка валидации поля"):
            app.PO_Users_Keys.input_re_password_sms_user()

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Повторите пароль'(Настройки)")
    def test_user_input_phone_re_password_sms_negativ_settings(self, app, extend_time, users_settings, close_modal):
        with allure.step("Проверка валидации поля"):
            app.PO_Users_Keys.input_re_password_sms_user_negativ()

@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты ПОЛЬЗОВАТЕЛИ И КЛЮЧИ")
@allure.feature("Валидация полей ввода")
@pytest.mark.flaky(reruns=reruns)
class Test04UsersKeysValidation():

    @allure.story("КЛЮЧИ")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Поиск'")
    def test_input_search_keys(self, app, extend_time):
        with allure.step("Переход на страницу Пользователи и ключи"):
            app.PO_Navigations.goToUsersKeysPage()
        with allure.step("Переход на вкладку 'Ключи'"):
            app.PO_Navigations.goToKeysPage()
        with allure.step("Проверка валидации поля"):
            app.PO_Users_Keys.input_seach()

    @allure.story("КЛЮЧИ")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Идентификатор'(Добавить ключ)")
    def test_input_keys_id(self, app, extend_time, keys, close_modal):
        with allure.step("Проверка валидации поля"):
            app.PO_Users_Keys.input_key_id()

    @allure.story("КЛЮЧИ")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Идентификатор'(Добавить ключ)")
    def test_input_keys_id_negativ(self, app, extend_time, keys, close_modal):
        with allure.step("Проверка валидации поля"):
            app.PO_Users_Keys.input_key_id_negativ()

    @allure.story("КЛЮЧИ")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Идентификатор'(Настройки ключа)")
    def test_input_keys_id_settings(self, app, extend_time, keys_settings, close_modal):
        with allure.step("Проверка валидации поля"):
            app.PO_Users_Keys.input_key_id()

    @allure.story("КЛЮЧИ")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Идентификатор'(Настройки ключа)")
    def test_input_keys_id_negativ_settings(self, app, extend_time, keys_settings, close_modal):
        with allure.step("Проверка валидации поля"):
            app.PO_Users_Keys.input_key_id_negativ()
