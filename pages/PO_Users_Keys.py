import random
import time

import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from data.pages_text import *
from locators.users_keys_locators import *


class UsersKeysHelper:

    def __init__(self, app):
        self.app = app

    # Клик по кнопке Добавить пользователя
    def PushAddUserButton(self, locator=add_user):
        self.app.method.click((By.XPATH, locator))

    # Клик по кнопке раскрыть настройки пользователя
    def OpenLastUserButton(self, locator=open_last_user):
        time.sleep(0.3)
        self.app.method.click((By.XPATH, locator))

    # Клик по кнопке Добавить ключ
    def PushAddKeyButton(self, locator=add_key):
        self.app.method.click((By.XPATH, locator))

    # Клик по кнопке Пользователь/Настройки
    def PushUserSettingsButton(self, locator=user_settings_button):
        time.sleep(1)
        self.app.method.click((By.XPATH, locator))
        time.sleep(1)

    # Клик по кнопке Ключи/Настройки
    def PushKeysSettingsButton(self, locator=user_settings_button):
        self.app.method.click((By.XPATH, locator))

    # Добавить ключ если его нет
    def Add_key_if_not(self):
        with allure.step("Получение списка ключей"):
            key = self.app.method.getElementsLen(key_row)
            if key < 3:
                with allure.step("Добавление ключа"):
                    self.app.method.click((By.XPATH, add_key))
                    time.sleep(1)
                    self.app.method.inputValues((random.randint(11111, 99999)), key_id)
                    self.app.method.click((By.XPATH, save_button_key))

    # Клик по кнопке Отменить
    def Cancel_button(self, locator=Cancel_button):
        self.app.method.click((By.XPATH, locator))

    # Проверка ввода поле принимает все символы
    def input_all(self, locator):
        with allure.step("Проверка ввода цифр"):
            for i in range(10):
                self.app.method.assertEqual(i, i, locator)
        with allure.step("Проверка ввода латинских букв в нижнем регистре"):
            self.app.method.assertEqual('abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz', locator)
        with allure.step("Проверка ввода латинских букв в врхнем регистре"):
            self.app.method.assertEqual('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', locator)
        with allure.step("Проверка ввода Русских букв в нижнем регистре"):
            self.app.method.assertEqual("ёйцукенгшщзхъфыв", "ёйцукенгшщзхъфыв", locator)
            self.app.method.assertEqual("апролджэячсмитьбю", "апролджэячсмитьбю", locator)
        with allure.step("Проверка ввода Русских букв в верхнем регистре"):
            self.app.method.assertEqual("АПРОЛДЖЭЯЧСМИТЬБЮ", "АПРОЛДЖЭЯЧСМИТЬБЮ", locator)
            self.app.method.assertEqual("ЁЙЦУКЕНГШЩЗХЪФЫВ", "ЁЙЦУКЕНГШЩЗХЪФЫВ", locator)
        with allure.step("Проверка ввода спецсимполов"):
            self.app.method.assertEqual("!#$%&'()*+,-./:;<=>?@[]^_`{|}~", "!#$%&'()*+,-./:;<=>?@[]^_`{|}~", locator)
        with allure.step("Проверка ввода совместных значений"):
            self.app.method.assertEqual('123  АБВABC!@#', '123  АБВABC!@#', locator)
        with allure.step("Проверка ввода пробелов"):
            self.app.method.assertEqual('   ', '   ', locator)
            self.app.method.assertEqual('123     ', '123     ', locator)
            self.app.method.assertEqual('   123', '   123', locator)
            self.app.method.assertEqual('1 2 3', '1 2 3', locator)
        with allure.step("Проверка ввода дробного числа "):
            self.app.method.assertEqual('11.11', '11.11', locator)
            self.app.method.assertEqual('000.1', '000.1', locator)
            self.app.method.assertEqual('11,11', '11,11', locator)
            self.app.method.assertEqual('000,1', '000,1', locator)
        with allure.step("Проверка ввода пустого значения"):
            self.app.method.assertEqual('', '', locator)
        with allure.step("Проверка ввода отрицательного числа"):
            self.app.method.assertEqual('-1', '-1', locator)

    # Проверка Поиск
    def input_seach(self, locator=Search):
        try:
            self.input_all(locator)
            with allure.step("Проверка ввода очень большого числа"):
                self.app.method.assertEqual(9999 * 1000000, 9999 * 1000000, locator)
        finally:
            self.app.method.click((By.XPATH, cross_close_button))

    # Проверка Идентификатор позитивные проверки
    def input_key_id(self, locator=key_id):
        self.input_key_posutiv(locator)

    # Проверка Идентификатор негативные проверки
    def input_key_id_negativ(self, locator=key_id):
        self.input_key_negativ(locator)

    # Проверка имя пользователя позитивные тесты
    def input_name_user(self, locator=name_user):
        self.input_all(locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual('0', '0', locator)
            self.app.method.assertEqual('1', '1', locator)
            self.app.method.assertEqual('1' * 62, '1' * 62, locator)
            self.app.method.assertEqual('1' * 63, '1' * 63, locator)

    # Проверка имя пользователя негативные тесты
    def input_name_user_negativ(self, locator=name_user):
        with allure.step("Проверка ввода очень большого числа"):
            self.app.method.assertEqual('1' * 10000, '1' * 63, locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual('1' * 64, '1' * 63, locator)


    # Проверка ЛОГИН/ПАРОЛЬ/ПОДТВЕРЖДЕНИЕ ПАРОЛЯ
    def input_data_63(self, locator):
        with allure.step("Проверка ввода цифр"):
            for i in range(10):
                self.app.method.assertEqual(i, i, locator)
        with allure.step("Проверка ввода латинских букв в нижнем регистре"):
            self.app.method.assertEqual('abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz', locator)
        with allure.step("Проверка ввода латинских букв в врхнем регистре"):
            self.app.method.assertEqual('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', locator)
        with allure.step("Проверка ввода спецсимполов"):
            self.app.method.assertEqual("№_~!@#$%^&*-+=|(){}[]:;<>,.?", "№_~!@#$%^&*-+=|(){}[]:;<>,.?", locator)
        with allure.step("Проверка ввода дробного числа "):
            self.app.method.assertEqual('11.11', '11.11', locator)
            self.app.method.assertEqual('000.1', '000.1', locator)
            self.app.method.assertEqual('11,11', '11,11', locator)
            self.app.method.assertEqual('000,1', '000,1', locator)
        with allure.step("Проверка ввода пустого значения"):
            self.app.method.assertEqual('', '', locator)
        with allure.step("Проверка ввода отрицательного числа"):
            self.app.method.assertEqual('-1', '-1', locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual('0', '0', locator)
            self.app.method.assertEqual('1', '1', locator)
            self.app.method.assertEqual('1' * 62, '1' * 62, locator)
            self.app.method.assertEqual('1' * 63, '1' * 63, locator)

    # Проверка ЛОГИН/ПАРОЛЬ/ПОДТВЕРЖДЕНИЕ ПАРОЛЯ
    def input_data_63_negativ(self, locator):
        with allure.step("Проверка ввода Русских букв в нижнем регистре"):
            self.app.method.assertEqual("ёйцукенгшщзхъфыв", "", locator)
            self.app.method.assertEqual("апролджэячсмитьбю", "", locator)
        with allure.step("Проверка ввода Русских букв в верхнем регистре"):
            self.app.method.assertEqual("АПРОЛДЖЭЯЧСМИТЬБЮ", "", locator)
            self.app.method.assertEqual("ЁЙЦУКЕНГШЩЗХЪФЫВ", "", locator)
        with allure.step("Проверка ввода спецсимполов"):
            self.app.method.assertEqual("!#$%&'()*+,-./:;<=>?@[]^_`{|}~", "!#$%&()*+,-.:;<=>?@[]^_{|}~", locator)
        with allure.step("Проверка ввода совместных значений"):
            self.app.method.assertEqual('123  АБВABC!@#', '123ABC!@#', locator)
        with allure.step("Проверка ввода пробелов"):
            self.app.method.assertEqual('   ', '', locator)
            self.app.method.assertEqual('123     ', '123', locator)
            self.app.method.assertEqual('   123', '123', locator)
            self.app.method.assertEqual('1 2 3', '123', locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual('1' * 64, '1' * 63, locator)

    # Проверка поля ЛОГИН позитив
    def input_login_user(self, locator=login_user):
        self.input_data_63(locator)

    # Проверка поля ЛОГИН негатив
    def input_login_user_negativ(self, locator=login_user):
        self.input_data_63_negativ(locator)

    # Проверка поля пароль позитив
    def input_password_user(self, locator=password):
        self.input_data_63(locator)

    # Проверка поля пароль негатив
    def input_password_user_negativ(self, locator=password):
        self.input_data_63_negativ(locator)

    # Проверка поля подтвердите пароль позитив
    def input_re_password_user(self, locator=re_password):
        self.input_data_63(locator)

    # Проверка поля подтвердите пароль негатив
    def input_re_password_user_negativ(self, locator=re_password):
        self.input_data_63_negativ(locator)

    # Проверка поля Телефон КОД
    def input_phone_cod_user(self, locator=phone_cod):
        with allure.step("Проверка ввода цифр"):
            for i in range(10):
                self.app.method.assertEqual(i, i, locator)
        with allure.step("Проверка ввода спецсимполов"):
            self.app.method.assertEqual("+", "+", locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual('0', '0', locator)
            self.app.method.assertEqual('1', '1', locator)
            self.app.method.assertEqual('1' * 4, '1' * 4, locator)
            self.app.method.assertEqual('1' * 5, '1' * 5, locator)

    # Проверка поля Телефон КОД
    def input_phone_cod_user_negativ(self, locator=phone_cod):
        with allure.step("Проверка ввода латинских букв в нижнем регистре"):
            self.app.method.assertEqual('abcdefghijklmnopqrstuvwxyz', '', locator)
        with allure.step("Проверка ввода латинских букв в врхнем регистре"):
            self.app.method.assertEqual('ABCDEFGHIJKLMNOPQRSTUVWXYZ', '', locator)
        with allure.step("Проверка ввода Русских букв в нижнем регистре"):
            self.app.method.assertEqual("ёйцукенгшщзхъфыв", "", locator)
            self.app.method.assertEqual("апролджэячсмитьбю", "", locator)
        with allure.step("Проверка ввода Русских букв в верхнем регистре"):
            self.app.method.assertEqual("АПРОЛДЖЭЯЧСМИТЬБЮ", "", locator)
            self.app.method.assertEqual("ЁЙЦУКЕНГШЩЗХЪФЫВ", "", locator)
        with allure.step("Проверка ввода спецсимполов"):
            self.app.method.assertEqual("!#$%&'()*+,-./:;<=>?@[]^_`{|}~", "+", locator)
        with allure.step("Проверка ввода совместных значений"):
            self.app.method.assertEqual('+123  АБВABC!@#', '+123', locator)
        with allure.step("Проверка ввода пробелов"):
            self.app.method.assertEqual('   ', '', locator)
            self.app.method.assertEqual('123     ', '123', locator)
            self.app.method.assertEqual('   123', '123', locator)
            self.app.method.assertEqual('1 2 3', '123', locator)
        with allure.step("Проверка ввода дробного числа "):
            self.app.method.assertEqual('11.11', '1111', locator)
            self.app.method.assertEqual('000.1', '0001', locator)
            self.app.method.assertEqual('11,11', '1111', locator)
            self.app.method.assertEqual('000,1', '0001', locator)
        with allure.step("Проверка ввода пустого значения"):
            self.app.method.assertEqual('', '', locator)
        with allure.step("Проверка ввода отрицательного числа"):
            self.app.method.assertEqual('-1', '1', locator)
        with allure.step("Проверка ввода очень большого числа"):
            self.app.method.assertEqual('1' * 1000, '11111', locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual('1' * 6, '1' * 5, locator)

    # Проверка поля Телефон НОМЕР
    def input_phone_number_user(self, locator=phone_number):
        with allure.step("Проверка ввода цифр"):
            for i in range(10):
                self.app.method.assertEqual(i, '(' + str(i), locator)
        with allure.step("Проверка ввода спецсимполов"):
            self.app.method.assertEqual("()- ", "()- ", locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual('0', '(0', locator)
            self.app.method.assertEqual('1', '(1', locator)
            self.app.method.assertEqual('1' * 9, '(111) 111-11-1', locator)
            self.app.method.assertEqual('1' * 10, '(111) 111-11-11', locator)

    # Проверка поля Телефон НОМЕР
    def input_phone_number_user_negativ(self, locator=phone_number):
        with allure.step("Проверка ввода латинских букв в нижнем регистре"):
            self.app.method.assertEqual('abcdefghijklmnopqrstuvwxyz', '', locator)
        with allure.step("Проверка ввода латинских букв в врхнем регистре"):
            self.app.method.assertEqual('ABCDEFGHIJKLMNOPQRSTUVWXYZ', '', locator)
        with allure.step("Проверка ввода Русских букв в нижнем регистре"):
            self.app.method.assertEqual("ёйцукенгшщзхъфыв", "", locator)
            self.app.method.assertEqual("апролджэячсмитьбю", "", locator)
        with allure.step("Проверка ввода Русских букв в верхнем регистре"):
            self.app.method.assertEqual("АПРОЛДЖЭЯЧСМИТЬБЮ", "", locator)
            self.app.method.assertEqual("ЁЙЦУКЕНГШЩЗХЪФЫВ", "", locator)
        with allure.step("Проверка ввода спецсимполов"):
            self.app.method.assertEqual("!#$%&'()*+,-./:;<=>?@[]^_`{|}~", "()-", locator)
        with allure.step("Проверка ввода совместных значений"):
            self.app.method.assertEqual('(123  АБВABC!@#', '(123  ', locator)
        with allure.step("Проверка ввода пробелов"):
            self.app.method.assertEqual('   ', '   ', locator)
            self.app.method.assertEqual('123   ', '(123   ', locator)
            self.app.method.assertEqual('   123', '   123', locator)
            self.app.method.assertEqual('1 2 3', '(1 2 3', locator)
        with allure.step("Проверка ввода дробного числа "):
            self.app.method.assertEqual('11.1', '(111', locator)
            self.app.method.assertEqual('00.1', '(001', locator)
            self.app.method.assertEqual('11,1', '(111', locator)
            self.app.method.assertEqual('00,1', '(001', locator)
        with allure.step("Проверка ввода пустого значения"):
            self.app.method.assertEqual('', '', locator)
        with allure.step("Проверка ввода отрицательного числа"):
            self.app.method.assertEqual('-1', '-1', locator)
        with allure.step("Проверка ввода очень большого числа"):
            self.app.method.assertEqual('1' * 1000, '(111) 111-11-11', locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual('1' * 11, '(111) 111-11-11', locator)

    # Пароль SMS Позитивные проверки
    def input_sms_password_positiv(self, locator):
        with allure.step("Проверка ввода цифр"):
            for i in range(10):
                self.app.method.assertEqual(i, i, locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual('0', '0', locator)
            self.app.method.assertEqual('1', '1', locator)
            self.app.method.assertEqual('1' * 4, '1' * 4, locator)
            self.app.method.assertEqual('1' * 5, '1' * 5, locator)

    # Пароль SMS Негативные проверки
    def input_sms_password_negativ(self, locator):
        with allure.step("Проверка ввода латинских букв в нижнем регистре"):
            self.app.method.assertEqual('abcdefghijklmnopqrstuvwxyz', '', locator)
        with allure.step("Проверка ввода латинских букв в врхнем регистре"):
            self.app.method.assertEqual('ABCDEFGHIJKLMNOPQRSTUVWXYZ', '', locator)
        with allure.step("Проверка ввода Русских букв в нижнем регистре"):
            self.app.method.assertEqual("ёйцукенгшщзхъфыв", "", locator)
            self.app.method.assertEqual("апролджэячсмитьбю", "", locator)
        with allure.step("Проверка ввода Русских букв в верхнем регистре"):
            self.app.method.assertEqual("АПРОЛДЖЭЯЧСМИТЬБЮ", "", locator)
            self.app.method.assertEqual("ЁЙЦУКЕНГШЩЗХЪФЫВ", "", locator)
        with allure.step("Проверка ввода спецсимполов"):
            self.app.method.assertEqual("!#$%&'()*+,-./:;<=>?@[]^_`{|}~", "", locator)
        with allure.step("Проверка ввода совместных значений"):
            self.app.method.assertEqual('123  АБВABC!@#', '123', locator)
        with allure.step("Проверка ввода пробелов"):
            self.app.method.assertEqual('   ', '', locator)
            self.app.method.assertEqual('123     ', '123', locator)
            self.app.method.assertEqual('   123', '123', locator)
            self.app.method.assertEqual('1 2 3', '123', locator)
        with allure.step("Проверка ввода дробного числа "):
            self.app.method.assertEqual('11.11', '1111', locator)
            self.app.method.assertEqual('000.1', '0001', locator)
            self.app.method.assertEqual('11,11', '1111', locator)
            self.app.method.assertEqual('000,1', '0001', locator)
        with allure.step("Проверка ввода пустого значения"):
            self.app.method.assertEqual('', '', locator)
        with allure.step("Проверка ввода отрицательного числа"):
            self.app.method.assertEqual('-1', '1', locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual('1' * 5, '1' * 5, locator)

    # Проверка вволда в поле Пароль SMS
    def input_password_sms_user(self, locator=password_sms_user):
        self.input_sms_password_positiv(locator)

    # Проверка вволда в поле Пароль SMS
    def input_password_sms_user_negativ(self, locator=password_sms_user):
        self.input_sms_password_negativ(locator)

    # Проверка вволда в поле Повторите пароль
    def input_re_password_sms_user(self, locator=re_password_sms_user):
        self.input_sms_password_positiv(locator)

    # Проверка вволда в поле Повторите пароль
    def input_re_password_sms_user_negativ(self, locator=re_password_sms_user):
        self.input_sms_password_negativ(locator)



    # Проверка ввода поле принимает все символы
    def input_key_posutiv(self, locator):
        with allure.step("Проверка ввода цифр"):
            for i in range(10):
                self.app.method.assertEqual(i, i, locator)
        with allure.step("Проверка ввода латинских букв в нижнем регистре"):
            self.app.method.assertEqual('abcdef', 'abcdef', locator)
        with allure.step("Проверка ввода латинских букв в врхнем регистре"):
            self.app.method.assertEqual('ABCDEF', 'ABCDEF', locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual('0', '0', locator)
            self.app.method.assertEqual('1', '1', locator)
            self.app.method.assertEqual('1' * 11, '1' * 11, locator)
            self.app.method.assertEqual('1' * 12, '1' * 12, locator)

    def input_key_negativ(self, locator):
        with allure.step("Проверка ввода цифр"):
            for i in range(10):
                self.app.method.assertEqual(i, i, locator)
        with allure.step("Проверка ввода латинских букв в нижнем регистре"):
            self.app.method.assertEqual('abcdefghijklmnopqrstuvwxyz', 'abcdef', locator)
        with allure.step("Проверка ввода латинских букв в врхнем регистре"):
            self.app.method.assertEqual('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ABCDEF', locator)
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
        with allure.step("Проверка ввода пробелов"):
            self.app.method.assertEqual('   ', '', locator)
            self.app.method.assertEqual('123     ', '123', locator)
            self.app.method.assertEqual('   123', '123', locator)
            self.app.method.assertEqual('1 2 3', '123', locator)
        with allure.step("Проверка ввода дробного числа "):
            self.app.method.assertEqual('11.11', '1111', locator)
            self.app.method.assertEqual('000.1', '0001', locator)
            self.app.method.assertEqual('11,11', '1111', locator)
            self.app.method.assertEqual('000,1', '0001', locator)
        with allure.step("Проверка ввода пустого значения"):
            self.app.method.assertEqual('', '', locator)
        with allure.step("Проверка ввода отрицательного числа"):
            self.app.method.assertEqual('-1', '1', locator)
        with allure.step("Проверка ввода очень большого числа"):
            self.app.method.assertEqual('1' * 1000, '1' * 12, locator)
        with allure.step("Проверка ввода граничных значений"):
            self.app.method.assertEqual('1' * 13, '1' * 12, locator)

    # Включение чекбоксов добавить пользователя
    def check_box_users_add_on(self):
        self.app.method.checkBox("ON", Administrator_click, Administrator_status)
        self.app.method.assertCheckBox("ON", Administrator_status)
        self.app.method.checkBox("ON", Egida3_Mode_click, Egida3_Mode_status)
        self.app.method.assertCheckBox("ON", Egida3_Mode_status)
        self.app.method.checkBox("ON", Operator_message_forwarding_click, Operator_message_forwarding_status)
        self.app.method.assertCheckBox("ON", Operator_message_forwarding_status)
        self.app.method.checkBox("ON", CB_Sending_out_of_broadcast, Sending_outside_broadcasts_status)
        self.app.method.assertCheckBox("ON", Sending_outside_broadcasts_status)
        self.app.method.checkBox("ON", Allow_take_off_by_SMS_click, Allow_take_off_by_SMS_status)
        self.app.method.assertCheckBox("ON", Allow_take_off_by_SMS_status)
        self.app.method.checkBox("ON", Allow_take_by_SMS_click, Allow_take_by_SMS_status)
        self.app.method.assertCheckBox("ON", Allow_take_by_SMS_status)

    # Выключение чекбоксов добавить пользователя
    def check_box_users_add_off(self):
        self.app.method.checkBox("OFF", Administrator_click, Administrator_status)
        self.app.method.assertCheckBox("OFF", Administrator_status)
        self.app.method.checkBox("OFF", Egida3_Mode_click, Egida3_Mode_status)
        self.app.method.assertCheckBox("OFF", Egida3_Mode_status)
        self.app.method.checkBox("OFF", Operator_message_forwarding_click, Operator_message_forwarding_status)
        self.app.method.assertCheckBox("OFF", Operator_message_forwarding_status)
        self.app.method.checkBox("OFF", CB_Sending_out_of_broadcast, Sending_outside_broadcasts_status)
        self.app.method.assertCheckBox("OFF", Sending_outside_broadcasts_status)
        self.app.method.checkBox("OFF", Allow_take_off_by_SMS_click, Allow_take_off_by_SMS_status)
        self.app.method.assertCheckBox("OFF", Allow_take_off_by_SMS_status)
        self.app.method.checkBox("OFF", Allow_take_by_SMS_click, Allow_take_by_SMS_status)
        self.app.method.assertCheckBox("OFF", Allow_take_by_SMS_status)

    # Включение чекбоксов выборочно
    def check_box_users_add_some(self):
        self.app.method.checkBox("ON", Administrator_click, Administrator_status)
        self.app.method.assertCheckBox("ON", Administrator_status)
        self.app.method.checkBox("OFF", Egida3_Mode_click, Egida3_Mode_status)
        self.app.method.assertCheckBox("OFF", Egida3_Mode_status)
        self.app.method.checkBox("ON", Operator_message_forwarding_click, Operator_message_forwarding_status)
        self.app.method.assertCheckBox("ON", Operator_message_forwarding_status)
        self.app.method.checkBox("OFF", CB_Sending_out_of_broadcast, Sending_outside_broadcasts_status)
        self.app.method.assertCheckBox("OFF", Sending_outside_broadcasts_status)
        self.app.method.checkBox("ON", Allow_take_off_by_SMS_click, Allow_take_off_by_SMS_status)
        self.app.method.assertCheckBox("ON", Allow_take_off_by_SMS_status)
        self.app.method.checkBox("OFF", Allow_take_by_SMS_click, Allow_take_by_SMS_status)
        self.app.method.assertCheckBox("OFF", Allow_take_by_SMS_status)
        self.app.method.checkBox("OFF", Administrator_click, Administrator_status)
        self.app.method.assertCheckBox("OFF", Administrator_status)
        self.app.method.checkBox("ON", Egida3_Mode_click, Egida3_Mode_status)
        self.app.method.assertCheckBox("ON", Egida3_Mode_status)
        self.app.method.checkBox("OFF", Operator_message_forwarding_click, Operator_message_forwarding_status)
        self.app.method.assertCheckBox("OFF", Operator_message_forwarding_status)
        self.app.method.checkBox("ON", CB_Sending_out_of_broadcast, Sending_outside_broadcasts_status)
        self.app.method.assertCheckBox("ON", Sending_outside_broadcasts_status)
        self.app.method.checkBox("OFF", Allow_take_off_by_SMS_click, Allow_take_off_by_SMS_status)
        self.app.method.assertCheckBox("OFF", Allow_take_off_by_SMS_status)
        self.app.method.checkBox("ON", Allow_take_by_SMS_click, Allow_take_by_SMS_status)
        self.app.method.assertCheckBox("ON", Allow_take_by_SMS_status)

    # Проверка полей на странице Добавить пользователя
    def text_add_users(self):
        self.app.method.assertTextOnPage(data_users_and_keys_modal_text, data_users)

    # Проверка полей на странице Настройки пользователя
    def text_settings_users(self):
        self.app.method.assertTextOnPage(data_users_and_keys_modal_text, data_users)

    # Проверка полей на странице Добавить ключ
    def text_add_keys(self):
        self.app.method.assertTextOnPage(data_users_and_keys_modal_text, data_keys)

    # Проверка полей на странице Настройки ключа
    def text_settings_keys(self):
        self.app.method.assertTextOnPage(data_users_and_keys_modal_text, data_keys)

    # Выпадающий список: Группа выходов с управлением звонком
    def drop_list_group_of_outputs_with_call_control(self, button=Group_of_outputs_with_call_control,
                                                     possition=positions):
        self.app.method.selectDropdownList(button, possition + '[1]')
        self.app.method.assertSelectionDropdownList('Выкл', button)
        for i in range(1, 17):
            self.app.method.selectDropdownList(button, possition + f'[{i + 1}]')
            self.app.method.assertSelectionDropdownList(i, button)

    # Выпадающий список: Группа выходов с управлением по SMS
    def drop_list_group_of_outputs_controlled_by_SMS(self, button=Group_of_outputs_controlled_by_SMS,
                                                     possition=positions_check_box):
        for i in range(16):
            self.app.method.selectDropdownListCheckBox(button, possition + f'[{i + 1}]',
                                                       status_drop_list_check_box + f'[{i + 1}]')
            self.app.method.assertSelectionDropdownListCheckBox(i + 1, button)

    # Выпадающий список: Группа выходов с управлением по SMS
    def drop_list_SMS_controlled_sections(self, button=SMS_controlled_sections, possition=positions_check_box):
        for i in range(16):
            self.app.method.selectDropdownListCheckBox(button, possition + f'[{i + 1}]',
                                                       status_drop_list_check_box + f'[{i + 1}]')
            self.app.method.assertSelectionDropdownListCheckBox(str(i + 1), button)

    # Выпадающий список: Разрешения - Ключи
    def dropdown_list_permissions_keys(self, button=permissions_dropdown):
        self.app.method.selectDropdownList(button, option_key + '[1]')
        self.app.method.assertSelectionDropdownList('Не настроен', button)

        self.app.method.selectDropdownList(button, option_key + '[2]')
        self.app.method.assertSelectionDropdownList('Взятие/снятие разделов', button)

        self.app.method.selectDropdownList(button, option_key + '[3]')
        self.app.method.assertSelectionDropdownList('Взятие разделов', button)

        self.app.method.selectDropdownList(button, option_key + '[4]')
        self.app.method.assertSelectionDropdownList('Снятие разделов', button)

        self.app.method.selectDropdownList(button, option_key + '[5]')
        self.app.method.assertSelectionDropdownList('Отметка наряда', button)

    # Выпадающий список: Разделы - Ключи
    def dropdown_list_path_keys(self, button=path_key_dropdown, possition=positions_check_box):
        for i in range(9):
            self.app.method.selectDropdownListCheckBox(button, possition + f'[{i + 1}]',
                                                       status_drop_list_check_box + f'[{i + 1}]')
            self.app.method.assertSelectionDropdownListCheckBox('Раздел № 0' + str(i + 1), button)
        for x in range(9, 16):
            self.app.method.selectDropdownListCheckBox(button, possition + f'[{x + 1}]',
                                                       status_drop_list_check_box + f'[{x + 1}]')
            self.app.method.assertSelectionDropdownListCheckBox('Раздел № ' + str(x + 1), button)
            print(x)


    # Форма настроек ключа
    def key_form(self, ids=None, user="Администратор", permissions=None, path=None):
        self.app.method.inputValues(value=ids, locator=key_id)
        self.app.method.dropdown_select(button=user_list_dropdown, name=user)
        self.app.method.dropdown_select(button=permissions_dropdown, name=permissions)
        self.app.method.path_select(button=path_key_dropdown, name=path)

    # Форма настроек пользователя
    def user_form(self, input_user_name=None, input_user_login=None, input_user_password=None,
                  input_user_password_rep=None,
                  input_phone_cod=None, input_phone_number=None, input_sms_password=None, input_sms_password_rep=None):
        self.app.method.inputValues(value=input_user_name, locator=name_user)
        self.app.method.inputValues(value=input_user_login, locator=login_user)
        self.app.method.inputValues(value=input_user_password, locator=password)
        self.app.method.inputValues(value=input_user_password_rep, locator=re_password)
        self.app.method.inputValues(value=input_phone_cod, locator=phone_cod)
        self.app.method.inputValues(value=input_phone_number, locator=phone_number)
        self.app.method.inputValues(value=input_sms_password, locator=password_sms_user)
        self.app.method.inputValues(value=input_sms_password_rep, locator=re_password_sms_user)

    # скрытие высплвающего окна сохранить
    def assert_save_text(self):
        count = self.app.method.elements_count('/html/body/div[2]/div/div/button')
        if count > 0:
            self.app.method.click((By.XPATH, '/html/body/div[2]/div/div/button'))

    # Удоление ключa
    def delete_key(self):
        self.app.method.click((By.XPATH, delete_button_key))
        self.assert_save_text()
        time.sleep(1)

    # Удоление пользователя
    def delete_user(self):
        self.app.method.click((By.XPATH, delete_button_user))
        self.assert_save_text()
        time.sleep(1)

    # Подсчет ключей
    def count_key(self):
        wd = self.app.wd
        return len(wd.find_elements_by_xpath(key))

    # Подсчет пользователей
    def count_user(self):
        wd = self.app.wd
        return len(wd.find_elements_by_xpath(user))

    # Добавление ключa
    def add_key(self):
        list_permissions = ['Не настроен', 'Взятие/снятие разделов', 'Взятие разделов', 'Снятие разделов', ]
        # list_path = ['Раздел № 01', 'Раздел № 02', 'Раздел № 03', 'Раздел № 04', 'Раздел № 05', 'Раздел № 06',
        #              'Раздел № 07', 'Раздел № 08', 'Раздел № 09', 'Раздел № 10', 'Раздел № 11', 'Раздел № 12',
        #              'Раздел № 13', 'Раздел № 14', 'Раздел № 15', 'Раздел № 16']
        list_path = ['Раздел № 01']
        self.PushAddKeyButton()
        self.key_form(
            ids=random.randint(11111, 99999),
            permissions=random.choice(list_permissions),
            path=random.choice(list_path)
        )
        self.app.method.click((By.XPATH, save_button_key))
        self.assert_save_text()
        time.sleep(1)

    # Добавление пользователя
    def add_user(self):
        random_data = random.randint(1111, 9999)
        random_data_phone = random.randint(1111111111, 9999999999)

        self.PushAddUserButton()
        self.user_form(input_user_name=random_data,
                       input_user_login=random_data,
                       input_user_password=random_data,
                       input_user_password_rep=random_data,
                       input_phone_cod='+7',
                       input_phone_number=random_data_phone,
                       input_sms_password=random_data,
                       input_sms_password_rep=random_data
                       )
        self.app.method.click((By.XPATH, save_button_key))
        self.assert_save_text()
        time.sleep(1)

    # Добавление ключа для проверки подсказки
    def add_key_for_tooltip(self):
        self.PushAddKeyButton()
        self.key_form(
            ids=random.randint(11111, 99999),
            permissions='Взятие разделов',
            path=r'Раздел № 01'
        )
        self.app.method.click((By.XPATH, save_button_key))
        time.sleep(1)

    # Добавление пользователя для проверки подсказки
    def add_user_tooltip(self):
        random_data = random.randint(1111, 9999)
        random_data_phone = random.randint(1111111111, 9999999999)
        self.PushAddUserButton()
        self.user_form(input_user_name=random_data,
                       input_user_login=random_data,
                       input_user_password=random_data,
                       input_user_password_rep=random_data,
                       input_phone_cod='+7',
                       input_phone_number=random_data_phone,
                       input_sms_password=random_data,
                       input_sms_password_rep=random_data
                       )
        self.app.method.click((By.XPATH, save_button_key))
        time.sleep(1)

    # Кнопка сохранить пользователя
    def User_save_button(self):
        self.app.method.click((By.XPATH, save_button_key))
        self.assert_save_text()
        time.sleep(1)

    # Кнопка сохранить пользователя проверка сообщения
    def User_save_button_messege(self):
        self.app.method.click((By.XPATH, save_button_key))
        text = self.app.method.getText('//div[@class="toast-message-text"]')
        assert str(text) == 'Сохранено.', f"Ожидаемый текст всплввающего окна = 'Сохранено.', фактический = '{text}'"
        time.sleep(1)

    # Добавление пользователя для сохранения
    def data_user_for_save(self):
        with allure.step("Клик по кнопке добавить пользователя"):
            self.PushAddUserButton()
        with allure.step("Парсинг сгенерированных данных"):
            _user = self.app.read_data.data_user()
        with allure.step("Выбор чекбокса Режим Эгида3"):
            self.app.method.checkBox(_user['CB_egida'], Egida3_Mode_click, Egida3_Mode_status)
        with allure.step("Ввод значений в поле Имя пользователя"):
            self.app.method.inputValues(_user['user_name'], name_user)
        with allure.step("Ввод значений в поле Логин"):
            self.app.method.inputValues(_user['user_login'], login_user)
        with allure.step("Ввод значений в поле Пароль "):
            self.app.method.inputValues(_user['user_password'], password)
        with allure.step("Ввод значений в поле Повторите пароль  "):
            self.app.method.inputValues(_user['user_password'], re_password)
        with allure.step("Выбор чекбокса Перенаправление сообщений оператора"):
            self.app.method.checkBox(_user['CB_Operator_message_forwarding'], Operator_message_forwarding_click,
                                     Operator_message_forwarding_status)
        with allure.step("Выбор чекбокса Отправка вне трансляции"):
            self.app.method.checkBox(_user['CB_Sending_out_of_broadcast'], CB_Sending_out_of_broadcast,
                                     Sending_outside_broadcasts_status)
        with allure.step("Выбор из выпадающего списка Группа выходов с управлением по SMS"):
            path = _user['DL_Group_of_outputs_controlled_by_SMS']
            self.app.method.close_cross(Group_of_outputs_controlled_by_SMS)
            self.app.method.click((By.XPATH, f'/html/body//div[@class="b-multiselect-item"]/span[.="{path}"]'))
            self.app.method.click((By.XPATH, Group_of_outputs_controlled_by_SMS))
        with allure.step("Выбор из выпадающего списка Группа выходов с управлением звонком"):
            self.app.method.selectDropdownListByName(Group_of_outputs_with_call_control,
                                                     _user['DL_Group_of_outputs_with_call_control'])
        with allure.step("Выбор чекбокса Разрешить снятие по SMS"):
            self.app.method.checkBox(_user['CB_Allow_withdrawal_by_SMS'], Allow_take_off_by_SMS_click,
                                     Allow_take_off_by_SMS_status)
        with allure.step("Выбор чекбокса Разрешить взятие по SMS"):
            self.app.method.checkBox(_user['CB_Allow_Pickup_by_SMS'], Allow_take_by_SMS_click,
                                     Allow_take_by_SMS_status)
        with allure.step("Ввод значений в поле Телефон - код"):
            self.app.method.inputValues(_user['user_phone_cod'], phone_cod)
        with allure.step("Ввод значений в поле Телефон - номер"):
            self.app.method.inputValues(_user['user_phone_number'], phone_number)
        with allure.step("Ввод значений в поле Пароль SMS"):
            self.app.method.inputValues(_user['user_sms_password'], password_sms_user)
        with allure.step("Ввод значений в поле Повторите пароль SMS"):
            self.app.method.inputValues(_user['user_sms_password'], re_password_sms_user)
        with allure.step("Выбор из выпадающего списка Группа выходов с управлением по SMS"):
            path = _user['pathList']
            self.app.method.close_cross(DL_SMS_controlled_sections)
            self.app.method.click((By.XPATH, f'/html/body//div[@class="b-multiselect-item"]/span[.="{path}"]'))
            self.app.method.click((By.XPATH, DL_SMS_controlled_sections))
        with allure.step("Клик по кнопке сохранить"):
            self.User_save_button()

    # проверка сохранения данных пользователя
    def assert_data_user_for_save(self):
        with allure.step("Клик по кнопке настройки последнего пользователя"):
            self.OpenLastUserButton()
        with allure.step("Парсинг сгенерированных данных"):
            _user = self.app.read_data.data_user()
        with allure.step("Проверка выбора чекбокса Режим Эгида3"):
            self.app.method.assertCheckBox(_user['CB_egida'], Egida3_Mode_status)
        with allure.step("Проверка ввода значений в поле Имя пользователя"):
            self.app.method.assertValues(_user['user_name'], name_user)
        with allure.step("Проверка ввода значений в поле Логин"):
            self.app.method.assertValues(_user['user_login'], login_user)
        with allure.step("Проверка ввода значений в поле Пароль "):
            self.app.method.assertValues('', password)
        with allure.step("Проверка ввода значений в поле Повторите пароль  "):
            self.app.method.assertValues('', re_password)
        with allure.step("Проверка выбора чекбокса Перенаправление сообщений оператора"):
            self.app.method.assertCheckBox(_user['CB_Operator_message_forwarding'], Operator_message_forwarding_status)
        with allure.step("Проверка выбора чекбокса Отправка вне трансляции"):
            self.app.method.assertCheckBox(_user['CB_Sending_out_of_broadcast'], Sending_outside_broadcasts_status)
        with allure.step("Проверка выбора из выпадающего списка Группа выходов с управлением по SMS"):
            el = _user['DL_Group_of_outputs_controlled_by_SMS']
            wd = self.app.wd
            element = wd.find_element(By.XPATH, Group_of_outputs_controlled_by_SMS).get_property("textContent")
            assert str(el) in str(
                element), f"\nОжидаемое значение в выпадающем списке: '{el}'\nФактическое: '{element}'"
            time.sleep(2)
        with allure.step("Проверка выбора из выпадающего списка Группа выходов с управлением звонком"):
            self.app.method.assertSelectionDropdownList(_user['DL_Group_of_outputs_with_call_control'],
                                                        Group_of_outputs_with_call_control)
        with allure.step("Проверка выбора чекбокса Разрешить снятие по SMS"):
            self.app.method.assertCheckBox(_user['CB_Allow_withdrawal_by_SMS'], Allow_take_off_by_SMS_status)
        with allure.step("Проверка выбора чекбокса Разрешить взятие по SMS"):
            self.app.method.assertCheckBox(_user['CB_Allow_Pickup_by_SMS'], Allow_take_by_SMS_status)
        with allure.step("Проверка ввода значений в поле Телефон - код"):
            self.app.method.assertValues(_user['user_phone_cod'], phone_cod)
        with allure.step("Проверка ввода значений в поле Телефон - номер"):
            self.app.method.assertValuesPhoneNum(_user['user_phone_number'], phone_number)
        with allure.step("Проверка ввода значений в поле Пароль SMS"):
            self.app.method.assertValues('', password_sms_user)
        with allure.step("Проверка ввода значений в поле Повторите пароль SMS"):
            self.app.method.assertValues('', re_password_sms_user)
        with allure.step("Проверка выбора из выпадающего списка Группа выходов с управлением по SMS"):
            path = _user['pathList']
            wd = self.app.wd
            element = wd.find_element(By.XPATH, DL_SMS_controlled_sections).get_property("textContent")
            assert str(path) in str(
                element), f"\nОжидаемое значение в выпадающем списке: '{path}'\nФактическое: '{element}'"

    # изменение настроек пользователя
    def data_user_for_save_same_login(self):
        with allure.step("Клик по кнопке настройки последнего пользователя"):
            self.OpenLastUserButton()
        with allure.step("Парсинг сгенерированных данных"):
            _user = self.app.read_data.data_user()
        with allure.step("Выбор чекбокса Режим Эгида3"):
            self.app.method.checkBox(_user['CB_egida_2'], Egida3_Mode_click, Egida3_Mode_status)
        with allure.step("Ввод значений в поле Имя пользователя"):
            self.app.method.inputValues(_user['user_name_2'], name_user)
        with allure.step("Ввод значений в поле Логин"):
            self.app.method.inputValues(_user['user_login'], login_user)
        with allure.step("Ввод значений в поле Пароль "):
            self.app.method.inputValues(_user['user_password_2'], password)
        with allure.step("Ввод значений в поле Повторите пароль  "):
            self.app.method.inputValues(_user['user_password_2'], re_password)
        with allure.step("Выбор чекбокса Перенаправление сообщений оператора"):
            self.app.method.checkBox(_user['CB_Operator_message_forwarding_2'], Operator_message_forwarding_click,
                                     Operator_message_forwarding_status)
        with allure.step("Выбор чекбокса Отправка вне трансляции"):
            self.app.method.checkBox(_user['CB_Sending_out_of_broadcast_2'], CB_Sending_out_of_broadcast,
                                     Sending_outside_broadcasts_status)
        with allure.step("Выбор из выпадающего списка Группа выходов с управлением по SMS"):
            path = _user['DL_Group_of_outputs_controlled_by_SMS_2']
            self.app.method.close_cross(Group_of_outputs_controlled_by_SMS)
            self.app.method.click((By.XPATH, f'/html/body//div[@class="b-multiselect-item"]/span[.="{path}"]'))
            self.app.method.click((By.XPATH, Group_of_outputs_controlled_by_SMS))
        with allure.step("Выбор из выпадающего списка Группа выходов с управлением звонком"):
            self.app.method.selectDropdownListByName(Group_of_outputs_with_call_control,
                                                     _user['DL_Group_of_outputs_with_call_control_2'])
        with allure.step("Выбор чекбокса Разрешить снятие по SMS"):
            self.app.method.checkBox(_user['CB_Allow_withdrawal_by_SMS_2'], Allow_take_off_by_SMS_click,
                                     Allow_take_off_by_SMS_status)
        with allure.step("Выбор чекбокса Разрешить взятие по SMS"):
            self.app.method.checkBox(_user['CB_Allow_Pickup_by_SMS_2'], Allow_take_by_SMS_click,
                                     Allow_take_by_SMS_status)
        with allure.step("Ввод значений в поле Телефон - код"):
            self.app.method.inputValues(_user['user_phone_cod_2'], phone_cod)
        with allure.step("Ввод значений в поле Телефон - номер"):
            self.app.method.inputValues(_user['user_phone_number_2'], phone_number)
        with allure.step("Ввод значений в поле Пароль SMS"):
            self.app.method.inputValues(_user['user_sms_password_2'], password_sms_user)
        with allure.step("Ввод значений в поле Повторите пароль SMS"):
            self.app.method.inputValues(_user['user_sms_password_2'], re_password_sms_user)
        with allure.step("Выбор из выпадающего списка Группа выходов с управлением по SMS"):
            path = _user['pathList_2']
            self.app.method.close_cross(DL_SMS_controlled_sections)
            self.app.method.click((By.XPATH, f'/html/body//div[@class="b-multiselect-item"]/span[.="{path}"]'))
            self.app.method.click((By.XPATH, DL_SMS_controlled_sections))
        with allure.step("Клик по кнопке сохранить"):
            self.User_save_button_messege()

    # Проверка измененря данных пользователя
    def assert_data_user_for_save_same_login(self):
        with allure.step("Клик по кнопке настройки последнего пользователя"):
            self.OpenLastUserButton()
        with allure.step("Парсинг сгенерированных данных"):
            _user = self.app.read_data.data_user()
        with allure.step("Проверка выбора чекбокса Режим Эгида3"):
            self.app.method.assertCheckBox(_user['CB_egida_2'], Egida3_Mode_status)
        with allure.step("Проверка ввода значений в поле Имя пользователя"):
            self.app.method.assertValues(_user['user_name_2'], name_user)
        with allure.step("Проверка ввода значений в поле Логин"):
            self.app.method.assertValues(_user['user_login'], login_user)
        with allure.step("Проверка ввода значений в поле Пароль "):
            self.app.method.assertValues('', password)
        with allure.step("Проверка ввода значений в поле Повторите пароль  "):
            self.app.method.assertValues('', re_password)
        with allure.step("Проверка выбора чекбокса Перенаправление сообщений оператора"):
            self.app.method.assertCheckBox(_user['CB_Operator_message_forwarding_2'],
                                           Operator_message_forwarding_status)
        with allure.step("Проверка выбора чекбокса Отправка вне трансляции"):
            self.app.method.assertCheckBox(_user['CB_Sending_out_of_broadcast_2'], Sending_outside_broadcasts_status)
        with allure.step("Проверка выбора из выпадающего списка Группа выходов с управлением по SMS"):
            el = _user['DL_Group_of_outputs_controlled_by_SMS_2']
            wd = self.app.wd
            element = wd.find_element(By.XPATH, Group_of_outputs_controlled_by_SMS).get_property("textContent")
            assert str(el) in str(
                element), f"\nОжидаемое значение в выпадающем списке: '{el}'\nФактическое: '{element}'"
            time.sleep(2)
        with allure.step("Проверка выбора из выпадающего списка Группа выходов с управлением звонком"):
            self.app.method.assertSelectionDropdownList(_user['DL_Group_of_outputs_with_call_control_2'],
                                                        Group_of_outputs_with_call_control)
        with allure.step("Проверка выбора чекбокса Разрешить снятие по SMS"):
            self.app.method.assertCheckBox(_user['CB_Allow_withdrawal_by_SMS_2'], Allow_take_off_by_SMS_status)
        with allure.step("Проверка выбора чекбокса Разрешить взятие по SMS"):
            self.app.method.assertCheckBox(_user['CB_Allow_Pickup_by_SMS_2'], Allow_take_by_SMS_status)
        with allure.step("Проверка ввода значений в поле Телефон - код"):
            self.app.method.assertValues(_user['user_phone_cod_2'], phone_cod)
        with allure.step("Проверка ввода значений в поле Телефон - номер"):
            self.app.method.assertValuesPhoneNum(_user['user_phone_number_2'], phone_number)
        with allure.step("Проверка ввода значений в поле Пароль SMS"):
            self.app.method.assertValues('', password_sms_user)
        with allure.step("Проверка ввода значений в поле Повторите пароль SMS"):
            self.app.method.assertValues('', re_password_sms_user)
        with allure.step("Проверка выбора из выпадающего списка Группа выходов с управлением по SMS"):
            path = _user['pathList_2']
            wd = self.app.wd
            element = wd.find_element(By.XPATH, DL_SMS_controlled_sections).get_property("textContent")
            assert str(path) in str(
                element), f"\nОжидаемое значение в выпадающем списке: '{path}'\nФактическое: '{element}'"

    # Добавление ключа для сохранения
    def data_key_for_save(self):
        with allure.step("Клик по кнопке добавить пользователя"):
            self.PushAddKeyButton()
        with allure.step("Парсинг сгенерированных данных"):
            _key = self.app.read_data.data_key()
        with allure.step("Ввод значений в поле Идентификатор "):
            self.app.method.inputValues(_key['key_id'], key_id)
        with allure.step("Выбор из выпадающего списка Разрешения"):
            self.app.method.selectDropdownListByName(permissions_dropdown, _key['Permissions'])
        with allure.step("Выбор из выпадающего списка Разделы"):
            path = _key['pathList']
            self.app.method.close_cross(path_key_dropdown)
            self.app.method.click((By.XPATH, f'/html/body//div[@class="b-multiselect-item"]/span[.="{path}"]'))
            self.app.method.click((By.XPATH, path_key_dropdown))
        with allure.step("Клик по кнопке сохранить"):
            self.User_save_button()

    # проверка сохранения данных ключа
    def assert_data_key_for_save(self):
        with allure.step("Клик по кнопке настройки последнего ключа"):
            self.OpenLastUserButton()
        with allure.step("Парсинг сгенерированных данных"):
            _key = self.app.read_data.data_key()
        with allure.step("Проверка ввода в поле Идентификатор "):
            self.app.method.assertValues(_key['key_id'], key_id)
        with allure.step("Проверка выбора из выпадающего списка Разрешения"):
            self.app.method.assertSelectionDropdownList(_key['Permissions'], permissions_dropdown)
        with allure.step("Выбор из выпадающего списка Разделы"):
            path = _key['pathList']
            wd = self.app.wd
            element = wd.find_element(By.XPATH, path_key_dropdown).get_property("textContent")
            assert str(path) in str(
                element), f"\nОжидаемое значение в выпадающем списке: '{path}'\nФактическое: '{element}'"
