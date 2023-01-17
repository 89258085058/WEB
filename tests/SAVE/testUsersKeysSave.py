# -*- coding: utf-8 -*-
import time

import allure
import pytest
from selenium.webdriver.common.by import By

reruns = 0

@pytest.fixture
def goToUsers(app):
    with allure.step("Переход на страницу Пользователи и ключи"):
        app.PO_Navigations.goToUsersKeysPage()
    with allure.step("Переход на вкладку 'Пользователи'"):
        app.PO_Navigations.goToUsersPage()


@pytest.fixture
def goToKeys(app):
    with allure.step("Переход на страницу Пользователи и ключи"):
        app.PO_Navigations.goToUsersKeysPage()
    with allure.step("Переход на вкладку 'Ключи'"):
        app.PO_Navigations.goToKeysPage()


@pytest.fixture()
def close_modal(request, app):
    def fin():
        app.method.click((By.XPATH, '(//*[.=" Отменить "]//div)[last()]'))

    request.addfinalizer(fin)


@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты ПОЛЬЗОВАТЕЛИ И КЛЮЧИ")
@allure.feature("Сохранение данных")
@pytest.mark.flaky(reruns=reruns)
class TestSaveKeys:

    @allure.story("КЛЮЧИ")
    @allure.title("Проверка сохранения добавления ключа")
    def test_01_users_keys_save_data_key(self, app, goToKeys, close_modal):
        with allure.step("Генерирование тестовых данных"):
            app.ganerate_data.createData()
        with allure.step("Предусловия добавления ключа"):
            count = app.PO_Users_Keys.count_key()
            if count == 64:
                app.PO_Users_Keys.delete_key()
        with allure.step("Добавления ключа"):
            app.PO_Users_Keys.data_key_for_save()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToUsersKeysPage()
            app.PO_Navigations.goToKeysPage()
        with allure.step("Проверка сохраненной информации"):
            app.PO_Users_Keys.assert_data_key_for_save()

    @allure.story("КЛЮЧИ")
    @allure.title("Проверка добавления ключа")
    def test_02_users_keys_add_save_key(self, app, goToKeys):
        with allure.step("Удаление ключа при условии отображения 64х ключей"):
            count = app.PO_Users_Keys.count_key()
            if count == 64:
                app.PO_Users_Keys.delete_key()
        with allure.step("Подсчет списка ключей до добавления"):
            old_keys_list: int = app.PO_Users_Keys.count_key()
        with allure.step("Добавления ключа"):
            app.PO_Users_Keys.add_key()
        with allure.step("Подсчет списка ключей после добавления"):
            new_keys_list: int = app.PO_Users_Keys.count_key()
        with allure.step("Проверка на добавления ключа"):
            assert old_keys_list + 1 == new_keys_list, f'Ошибка добавления ключа!\n' \
                                                       f'Список ключей до добавления="{old_keys_list}"\n' \
                                                       f'Список ключей после добавления="{new_keys_list}"'

    @allure.story("КЛЮЧИ")
    @allure.title("Проверка удаления ключа")
    def test_03_users_keys_delete_save_key(self, app, goToKeys):
        with allure.step("Добавления ключа при его отсутствии"):
            count = app.PO_Users_Keys.count_key()
            if count == 0:
                app.PO_Users_Keys.add_key()
        with allure.step("Подсчет списка ключей до удаления"):
            old_keys_list: int = app.PO_Users_Keys.count_key()
        with allure.step("Удаление ключа"):
            app.PO_Users_Keys.delete_key()
        with allure.step("Подсчет списка ключей после удаления"):
            new_keys_list: int = app.PO_Users_Keys.count_key()
        with allure.step("Проверка на удаление ключа"):
            assert old_keys_list - 1 == new_keys_list, f'Ошибка удаления ключа!\n' \
                                                       f'Список ключей до удаления="{old_keys_list}"\n' \
                                                       f'Список ключей после удаления="{new_keys_list}"'

    @pytest.mark.skip("Длинный тест")
    @allure.story("КЛЮЧИ")
    @allure.title("Проверка добавления максимального количества ключей")
    def test_04_users_keys_add_save_key_64(self, app, goToKeys):
        with allure.step("Добавления максимального количества ключей"):
            count = app.PO_Users_Keys.count_key()
            for i in range(count, 64):
                app.PO_Users_Keys.add_key()
        with allure.step("Проверка списка ключей после добавления"):
            keys_list: int = app.PO_Users_Keys.count_key()
            assert keys_list == 64, f'Ошибка создания 64х ключей,' \
                                    f' фактически список ключей = {app.PO_Users_Keys.count_key()}'
        with allure.step("Выполнение пост условий - удаление ключей"):
            for i in range(64):
                app.PO_Users_Keys.delete_key()

    @pytest.mark.skip("Длинный тест")
    @allure.story("КЛЮЧИ")
    @allure.title("Проверка всплывающей подсказки при добавлении максимального количества ключей")
    def test_05_users_keys_add_save_key_64_tooltip(self, app, goToKeys):
        with allure.step("Добавления максимального количества ключей"):
            count = app.PO_Users_Keys.count_key()
            for i in range(count, 64):
                app.PO_Users_Keys.add_key()
            time.sleep(5)
        with allure.step("Проверка всплывающей подсказки"):
            app.PO_Users_Keys.add_key_for_tooltip()
            text = 'Максимально допустимое количество ключей: 64.'
            actual_text = app.method.getText('//*[@class="toast-message-detail"]')
            assert text == actual_text, f"\nОшибка при проверке всплывающей подсказки!" \
                                        f"\nОжидаемый текст: '{text}'" \
                                        f"\nФактический текст: '{actual_text}'"


@allure.epic("Тесты ПОЛЬЗОВАТЕЛИ И КЛЮЧИ")
@allure.feature("Сохранение данных")
@pytest.mark.flaky(reruns=reruns)
class TestSaveUsers:

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Проверка сохранения изменения данных пользователя")
    def test_users_keys_save_data_user(self, app, goToUsers, close_modal):
        with allure.step("Генерирование тестовых данных"):
            app.ganerate_data.createData()
        with allure.step("Предусловия добавления пользователя"):
            count = app.PO_Users_Keys.count_user()
            if count == 64:
                app.PO_Users_Keys.delete_user()
        with allure.step("Создание пользователя"):
            app.PO_Users_Keys.data_user_for_save()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToUsersKeysPage()
            app.PO_Navigations.goToUsersPage()
        with allure.step("Проверка сохраненной информации"):
            app.PO_Users_Keys.assert_data_user_for_save()

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Проверка сохранения изменения данных пользователя без изменения логина")
    def test_users_keys_save_data_user_same_login(self, app, goToUsers, close_modal):
        with allure.step("Генерирование тестовых данных"):
            app.ganerate_data.createData()
        with allure.step("Предусловия добавления пользователя"):
            count = app.PO_Users_Keys.count_user()
            if count == 64:
                app.PO_Users_Keys.delete_user()
        with allure.step("Создание пользователя"):
            app.PO_Users_Keys.data_user_for_save()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToUsersKeysPage()
            app.PO_Navigations.goToUsersPage()
        with allure.step("Изменение данных"):
            app.PO_Users_Keys.data_user_for_save_same_login()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToUsersKeysPage()
            app.PO_Navigations.goToUsersPage()
        with allure.step("Проверка сохраненной информации"):
            app.PO_Users_Keys.assert_data_user_for_save_same_login()

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Проверка добавления пользователя")
    def test_users_keys_add_save_user(self, app, goToUsers):
        with allure.step("Удаление пользователя при условии отображения 64х пользователей"):
            count = app.PO_Users_Keys.count_user()
            if count == 64:
                app.PO_Users_Keys.delete_user()
            if count < 1:
                app.PO_Users_Keys.add_user()
        with allure.step("Подсчет списка пользователей до добавления"):
            old_user_list: int = app.PO_Users_Keys.count_user()
        with allure.step("Добавления пользователя"):
            app.PO_Users_Keys.add_user()
        with allure.step("Подсчет списка пользователей после добавления"):
            new_user_list: int = app.PO_Users_Keys.count_user()
        with allure.step("Проверка на добавления пользователя"):
            assert old_user_list + 1 == new_user_list, f'Ошибка добавления пользователя!\n' \
                                                       f'Список пользователей до добавления="{old_user_list}"\n' \
                                                       f'Список пользователей после добавления="{new_user_list}"'

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Проверка удаления пользователя")

    def test_users_keys_delete_save_user(self, app, goToUsers):
        with allure.step("Добавления пользователя при его отсутствии"):
            count = app.PO_Users_Keys.count_user()
            if count == 1:
                app.PO_Users_Keys.add_user()
        with allure.step("Подсчет списка пользователей до удаления"):
            old_user_list: int = app.PO_Users_Keys.count_user()
        with allure.step("Удаление пользователя"):
            app.PO_Users_Keys.delete_user()
        with allure.step("Подсчет списка пользователей после удаления"):
            new_user_list: int = app.PO_Users_Keys.count_user()
        with allure.step("Проверка на удаление пользователя"):
            assert old_user_list - 1 == new_user_list, f'Ошибка удаления пользователя!\n' \
                                                       f'Список пользователей до удаления="{old_user_list}"\n' \
                                                       f'Список пользователей после удаления="{new_user_list}"'

    @pytest.mark.skip("Длинный тест")
    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Проверка добавления максимального количества пользователей")
    def test_users_keys_add_save_user_64(self, app, goToUsers):
        with allure.step("Добавления максимального количества пользователей"):
            count = app.PO_Users_Keys.count_user()
            for i in range(count, 64):
                app.PO_Users_Keys.add_user()
        with allure.step("Проверка списка пользователей после добавления"):
            user_list: int = app.PO_Users_Keys.count_user()
            assert user_list == 64, f'Ошибка создания 64х пользователей,' \
                                    f' фактически список пользователей = {app.PO_Users_Keys.count_user()}'
        with allure.step("Выполнение пост условий - удаление пользователей"):
            for i in range(62):
                app.PO_Users_Keys.delete_user()

    @pytest.mark.skip("Длинный тест")
    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Проверка всплывающей подсказки при добавлении максимального количества пользователей")
    def test_users_keys_add_save_user_64_tooltip(self, app, goToUsers):
        with allure.step("Добавления максимального количества пользователей"):
            count = app.PO_Users_Keys.count_user()
            for i in range(count, 64):
                app.PO_Users_Keys.add_user()
            time.sleep(5)
        with allure.step("Проверка всплывающей подсказки"):
            app.PO_Users_Keys.add_user_tooltip()
            text = 'Максимально допустимое количество пользователей: 64.'
            actual_text = app.method.getText('//*[@class="toast-message-detail"]')
            assert text == actual_text, f"\nОшибка при проверке всплывающей подсказки!" \
                                        f"\nОжидаемый текст: '{text}'" \
                                        f"\nФактический текст: '{actual_text}'"

    @allure.story("ПОЛЬЗОВАТЕЛИ")
    @allure.title("Проверка отображения вкладок при входе не под администратором")
    def test_users_keys_not_admin_user(self, app, goToUsers):
        with allure.step("Добавления нового пользователя"):
            count = app.PO_Users_Keys.count_user()
            if count == 64:
                app.PO_Users_Keys.delete_user()
            app.PO_Users_Keys.add_user_for_test()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter_no_admin()
        with allure.step("Проверка отображения вкладок"):
            app.PO_Users_Keys.assert_header()
        with allure.step("Удаление пользователя"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToUsersKeysPage()
            app.PO_Navigations.goToUsersPage()
            app.PO_Users_Keys.delete_user()
