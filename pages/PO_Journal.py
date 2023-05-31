# -*- coding: utf-8 -*-
import time

import allure
from selenium.webdriver.common.by import By
from locators.zone_path_locators import name_out_2
from locators.journal_locators import *
from dataclasses import dataclass


@dataclass
class JournalHelper:
    app: any

    def event_evt_from_sensor(self, z_event, description):
        with allure.step("Эмуляция события по api"):
            data = self.app.endpoint.generate_json(0, z_event, 1)
            self.app.endpoint.create_event(data)
        with allure.step("Проверка отображения события"):
            self.assert_event_evt_from_sensor(z_event, description)

    def event_evt_from_sensor_climate(self, z_event, description, type_evt, value_type_evt):
        with allure.step("Эмуляция события по api"):
            data = self.app.endpoint.generate_json_climate(0, z_event, 1, value_type_evt)
            self.app.endpoint.create_event(data)
        with allure.step("Проверка отображения события"):
            self.assert_event_evt_from_sensor_climate(description, type_evt)

    def assert_event_evt_from_sensor_climate(self, description, type_evt):
        self.assert_equal_event_and_value_date(event_warning)
        self.app.method.assert_element_text(event_warning + '//p', f'15:04:50 | {description}: '
                                                                   f'{type_evt} Раздел № 01, Датчик №1')
        text_body = \
            f'Событие: {description}\nРаздел(ы): №1 «Раздел № 01»\nДатчик: Датчик №1\nДата и время: 01.01.2022 15:04:50'
        self.open_event(event_warning)
        self.app.method.assert_element_text(event_warning + '//div[@class="card-body"]', text_body)

    def assert_event_evt_from_sensor(self, z_event, description):
        locator = self.get_locator_for_sensor(z_event)
        self.assert_equal_event_and_value_date(locator)
        self.app.method.assert_element_text(locator + '//p', f'15:04:50 | {description}: Раздел № 01, Датчик №1')
        text_body = \
            f'Событие: {description}\nРаздел(ы): №1 «Раздел № 01»\nДатчик: Датчик №1\nДата и время: 01.01.2022 15:04:50'
        self.open_event(locator)
        self.app.method.assert_element_text(locator + '//div[@class="card-body"]', text_body)

    def open_event(self, locator):
        self.app.method.click_element_locate(locator)
        self.app.method.element_wait_to_be_text(last_item_body, 'Дата и время:')

    def assert_equal_event_and_value_date(self, locator):
        assert 1 == self.app.method.elements_count(locator), \
            f"Фактический результат {self.app.method.elements_count(locator)}"
        self.app.method.assert_element_text(title_date, '1 Января 2022, Суббота')

    @staticmethod
    def get_locator_for_sensor(z_event):
        if z_event in [0, 1, 15]:
            return event_secondary
        elif z_event in [2, 12]:
            return event_success
        elif z_event in [3, 4, 5, 6, 7, 8, 9, 10, 11, 24, 34, 35]:
            return event_danger
        elif z_event in [13, 18, 20, 21, 23, 29, 31, 32, 33]:
            return event_warning
        elif z_event in [14, 16, 17, 19, 22, 25, 26, 27, 28, 30, 36]:
            return event_status

    @staticmethod
    def get_locator_for_section(param):
        if param == 16:
            return event_success
        elif param in [8, 15, 22, 23, 30, 31, 32, 41]:
            return event_primary
        elif param in [0, 5]:
            return event_secondary
        elif param in [1, 6, 7, 9, 10, 11, 33, 40]:
            return event_warning
        elif param in [17, 21, 24, 25, 29]:
            return event_danger

    def event_evt_from_key(self, p_event, description):
        with allure.step("Эмуляция события по api"):
            data = self.app.endpoint.generate_json_for_evt_from_key(p_event)
            self.app.endpoint.create_event(data)
        with allure.step("Проверка отображения события"):
            self.assert_evt_from_key(p_event, description)

    def assert_evt_from_key(self, key_id, description):
        locator = self.get_locator_for_section(key_id)
        self.assert_equal_event_and_value_date(locator)
        self.app.method.assert_element_text(locator + '//p', f'15:04:50 | {description}: Раздел № 01, Test')
        if key_id == 6:
            text_body = f'Событие: {description}\nРаздел(ы): №1 «Раздел № 01»\nПользователь: Test\nКлюч: 1' \
                        f'\nИсточник: Ключ\nНевзятые датчики: Датчик №4\nДата и время: 01.01.2022 15:04:50'
        elif key_id == 11:
            text_body = f'Событие: {description}\nРаздел(ы): №1 «Раздел № 01»\nПользователь: Test\nКлюч: 1' \
                        f'\nИсточник: Ключ\nВременно отключенные датчики: Датчик №4\nДата и время: 01.01.2022 15:04:50'
        else:
            text_body = f'Событие: {description}\nРаздел(ы): №1 «Раздел № 01»\nПользователь: Test\nКлюч: 1' \
                        f'\nИсточник: Ключ\nДата и время: 01.01.2022 15:04:50'

        self.open_event(locator)
        self.app.method.assert_element_text(locator + '//div[@class="card-body"]', text_body)

    def event_evt_from_matrix(self, p_event, description, type_evt, value_type_evt):
        self.app.PO_Navigations.goToJournalPage()
        with allure.step("Эмуляция события по api"):
            data = self.app.endpoint.generate_json(p_event, 0, value_type_evt)
            self.app.endpoint.create_event(data)
        with allure.step(f"Проверка отображения события {type_evt} при статусе раздела {description}"):
            self.assert_evt_from_matrix(p_event, description, type_evt)

    def assert_evt_from_matrix(self, p_event, description, type_evt):
        locator = self.get_locator_for_section(p_event)
        self.assert_equal_event_and_value_date(locator)
        if type_evt == 'Брелок':
            self.app.method.assert_element_text(locator + '//p', f'15:04:50 | {description}: Раздел № 01, Брелок №1, Test')
            if p_event == 6:
                text_body = f'Событие: {description}\nРаздел(ы): №1 «Раздел № 01»\nПользователь: Test\nБрелок: Брелок №1' \
                            f'\nНевзятые датчики: Датчик №4\nДата и время: 01.01.2022 15:04:50'
            elif p_event == 11:
                text_body = f'Событие: {description}\nРаздел(ы): №1 «Раздел № 01»\nПользователь: Test\nБрелок: Брелок №1' \
                            f'\nВременно отключенные датчики: Датчик №4\nДата и время: 01.01.2022 15:04:50'
            else:
                text_body = f'Событие: {description}\nРаздел(ы): №1 «Раздел № 01»\nПользователь: Test\nБрелок: Брелок №1' \
                            f'\nДата и время: 01.01.2022 15:04:50'
        else:
            self.app.method.assert_element_text(locator + '//p', f'15:04:50 | {description}: Раздел № 01, Test')
            if p_event == 6:
                text_body = f'Событие: {description}\nРаздел(ы): №1 «Раздел № 01»\nПользователь: Test\nИсточник: {type_evt}' \
                            f'\nНевзятые датчики: Датчик №4\nДата и время: 01.01.2022 15:04:50'
            elif p_event == 11:
                text_body = f'Событие: {description}\nРаздел(ы): №1 «Раздел № 01»\nПользователь: Test\nИсточник: {type_evt}' \
                            f'\nВременно отключенные датчики: Датчик №4\nДата и время: 01.01.2022 15:04:50'
            else:
                text_body = f'Событие: {description}\nРаздел(ы): №1 «Раздел № 01»\nПользователь: Test\nИсточник: {type_evt}' \
                            f'\nДата и время: 01.01.2022 15:04:50'
        self.open_event(locator)
        self.app.method.assert_element_text(locator + '//div[@class="card-body"]', text_body)

    '''События для приборов'''

    def event_evt_from_bl(self, value_bievent, description):
        with allure.step("Эмуляция события по api"):
            data = self.app.endpoint.generate_json_for_bl(value_bievent)
            self.app.endpoint.create_event(data)
        with allure.step(f"Проверка отображения события"):
            self.assert_evt_from_bl_or_fw(description, 9)

    def assert_evt_from_bl_or_fw(self, description, event_type):
        self.assert_equal_event_and_value_date(event_info)
        if event_type == 9:
            source = 'Загрузчик'
        else:
            source = 'Изменение версии ПО'
        self.app.method.assert_element_text(event_info + '//p', f'15:04:50 | {description}')
        text_body = f'Событие: {description}\nИсточник: {source}\nТекущая версия: 1.28\nПредыдущая версия: 1.0' \
                    f'\nДата и время: 01.01.2022 15:04:50'
        self.open_event(event_info)
        self.app.method.assert_element_text(event_info + '//div[@class="card-body"]', text_body)

    def event_evt_from_fw(self, value_bievent, description):
        with allure.step("Эмуляция события по api"):
            data = self.app.endpoint.generate_json_for_fw(value_bievent)
            self.app.endpoint.create_event(data)
        with allure.step(f"Проверка отображения события"):
            self.assert_evt_from_bl_or_fw(description, 11)

    def event_evt_from_time_sync(self, value_event, description):
        with allure.step("Эмуляция события по api"):
            data = self.app.endpoint.generate_json_for_time_sync(value_event)
            self.app.endpoint.create_event(data)
        with allure.step(f"Проверка отображения события"):
            self.assert_evt_from_time_sync_or_ps(description, 'Синхронизация времени')

    def assert_evt_from_time_sync_or_ps(self, description, source):
        self.assert_equal_event_and_value_date(event_info)
        self.app.method.assert_element_text(event_info + '//p', f'15:04:50 | {description}')
        text_body = f'Событие: {description}\nИсточник: {source}\nДата и время: 01.01.2022 15:04:50'
        self.open_event(event_info)
        self.app.method.assert_element_text(event_info + '//div[@class="card-body"]', text_body)

    def event_evt_from_ps(self, value_event, description):
        with allure.step("Эмуляция события по api"):
            data = self.app.endpoint.generate_json_for_ps(value_event)
            self.app.endpoint.create_event(data)
        with allure.step(f"Проверка отображения события"):
            self.assert_evt_from_time_sync_or_ps(description, 'Электропитание')

    def event_evt_from_login(self, value_login_status, description, type_auth, value_type_auth):
        with allure.step("Эмуляция события по api"):
            data = self.app.endpoint.generate_json_for_login(value_login_status, value_type_auth)
            self.app.endpoint.create_event(data)
        with allure.step(f"Проверка отображения события"):
            self.assert_evt_from_time_login(description, type_auth)

    def assert_evt_from_time_login(self, description, type_auth):
        self.assert_equal_event_and_value_date(event_info)
        self.app.method.assert_element_text(event_info + '//p', f'15:04:50 | {description}, Test')
        text_body = f'Событие: {description}\nИсточник: Аутентификация\nТип авторизации: {type_auth}' \
                    f'\nДата и время: 01.01.2022 15:04:50'
        self.open_event(event_info)
        self.app.method.assert_element_text(event_info + '//div[@class="card-body"]', text_body)

    def event_evt_from_gsm_module(self, value_event, description):
        with allure.step("Эмуляция события по api"):
            data = self.app.endpoint.generate_json_for_gsm_module(value_event)
            self.app.endpoint.create_event(data)
        with allure.step(f"Проверка отображения события"):
            self.assert_evt_from_gsm_module(description, value_event)

    def assert_evt_from_gsm_module(self, description, value_event):
        self.assert_equal_event_and_value_date(event_info)
        self.app.method.assert_element_text(event_info + '//p', f'15:04:50 | {description}')
        if value_event in [5, 10]:
            text_body = f'Событие: {description}\nSIM-карта: SIM 2\nИсточник: События модуля GSM' \
                        f'\nИмя оператора: Megafon\nДата и время: 01.01.2022 15:04:50'
        elif value_event in [12, 13]:
            text_body = f'Событие: {description}\nSIM-карта: SIM 2\nИсточник: События модуля GSM' \
                        f'\nКол-во попыток: 2\nДата и время: 01.01.2022 15:04:50'
        else:
            text_body = f'Событие: {description}\nSIM-карта: SIM 2\nИсточник: События модуля GSM' \
                        f'\nДата и время: 01.01.2022 15:04:50'
        self.open_event(event_info)
        self.app.method.assert_element_text(event_info + '//div[@class="card-body"]', text_body)

    def event_evt_from_channel(self, value_status, description):
        with allure.step("Эмуляция события по api"):
            data = self.app.endpoint.generate_json_for_channel(value_status)
            self.app.endpoint.create_event(data)
        with allure.step(f"Проверка отображения события"):
            self.assert_evt_from_channel(description)

    def assert_evt_from_channel(self, description):
        self.assert_equal_event_and_value_date(event_info)
        self.app.method.assert_element_text(event_info + '//p', f'15:04:50 | {description}')
        text_body = f'Количество попыток передачи: 1\nНомер направления: 1\nНомер канала: 1' \
                    f'\nДата и время: 01.01.2022 15:04:50'
        self.open_event(event_info)
        self.app.method.assert_element_text(event_info + '//div[@class="card-body"]', text_body)

    def event_evt_from_test(self, value_test_type, description, state, value_state, channel, value_channel):
        with allure.step("Эмуляция события по api"):
            data = self.app.endpoint.generate_json_for_test(value_test_type, value_state, value_channel)
            self.app.endpoint.create_event(data)
        with allure.step(f"Проверка отображения события"):
            self.assert_evt_from_test(description, state, channel)

    def assert_evt_from_test(self, description, state, channel):
        self.assert_equal_event_and_value_date(event_info)
        self.app.method.assert_element_text(event_info + '//p', f'15:04:50 | Тестирование направления: {state}')
        text_body = f'Дата и время проведения тестирования: 20.01.1970 08:27:01\nНаправление: 1\nКанал: {channel}' \
                    f'\nТип события: {description}\nДата и время: 01.01.2022 15:04:50'
        self.open_event(event_info)
        self.app.method.assert_element_text(event_info + '//div[@class="card-body"]', text_body)

    def event_evt_from_text_string(self, value_source, description):
        with allure.step("Эмуляция события по api"):
            data = self.app.endpoint.generate_json_for_text_string(value_source)
            self.app.endpoint.create_event(data)
        with allure.step(f"Проверка отображения события"):
            self.assert_evt_from_text_string(description)

    def assert_evt_from_text_string(self, description):
        self.assert_equal_event_and_value_date(event_info)
        self.app.method.assert_element_text(event_info + '//p', f'15:04:50 | Текстовая строка: {description}, Test')
        text_body = f'Содержание смс: Text SMS - Hello world\nДата и время: 01.01.2022 15:04:50'
        self.open_event(event_info)
        self.app.method.assert_element_text(event_info + '//div[@class="card-body"]', text_body)

    def event_evt_from_output(self, value_out_event_type, description_out_event_type, value, description):
        with allure.step("Эмуляция события по api"):
            data = self.app.endpoint.generate_json_for_output(value_out_event_type, value)
            self.app.endpoint.create_event(data)
        with allure.step(f"Проверка отображения события"):
            self.assert_evt_from_output(value_out_event_type, description_out_event_type,  value, description)

    def assert_evt_from_output(self, value_out_event_type, description_out_event_type,  value, description):
        if value_out_event_type == 3:
            param = 'Неисправность: '
            locator = event_warning
        elif value_out_event_type == 1:
            param = 'Событие по маске: '
            locator = self.get_locator_for_section(value)
        elif value_out_event_type == 0:
            locator = event_info
            param = 'Состояние: '
        else:
            param = 'Состояние: '
            locator = event_warning
        self.assert_equal_event_and_value_date(locator)
        self.app.method.assert_element_text(
            locator + '//p', f'15:04:50 | {description_out_event_type}: output_second, 100')

        text_body = f'Событие: {description_out_event_type}\nВыход: № 2, «0», 100\nИсточник: Выход' \
                    f'\n{param}{description}\nДата и время: 01.01.2022 15:04:50'
        self.open_event(locator)
        self.app.method.assert_element_text(locator + '//div[@class="card-body"]', text_body)

    def event_evt_from_system_action_sensor(self, value_sys_evt_type,
                                            description_sys_evt_type, value_sensor_type, description_sensor_type):
        with allure.step("Эмуляция события по api"):
            data = self.app.endpoint.generate_json_for_system(value_sys_evt_type, value_sensor_type)
            self.app.endpoint.create_event(data)
        with allure.step(f"Проверка отображения события"):
            self.assert_evt_from_system_action_sensor(description_sys_evt_type, description_sensor_type)

    def assert_evt_from_system_action_sensor(self, description_sys_evt_type, description_sensor_type):
        self.assert_equal_event_and_value_date(event_info)
        self.app.method.assert_element_text(event_info + '//p', f'15:04:50 | {description_sys_evt_type}, Датчик №5')
        text_body = f'Событие: {description_sys_evt_type}\nИсточник: Система\nТип датчика: {description_sensor_type}' \
                    f'\nДата и время: 01.01.2022 15:04:50'
        self.open_event(event_info)
        self.app.method.assert_element_text(event_info + '//div[@class="card-body"]', text_body)

    def event_evt_from_system_action_key(self, value_sys_evt_type, description_sys_evt_type,
                                         value_access_law, description_access_law):
        with allure.step("Эмуляция события по api"):
            data = self.app.endpoint.generate_json_for_system(value_sys_evt_type, value_access_law)
            self.app.endpoint.create_event(data)
        with allure.step(f"Проверка отображения события"):
            self.assert_evt_from_system_action_key(description_sys_evt_type, description_access_law)

    def assert_evt_from_system_action_key(self, description_sys_evt_type, description_access_law):
        self.assert_equal_event_and_value_date(event_info)
        self.app.method.assert_element_text(event_info + '//p', f'15:04:50 | {description_sys_evt_type} №bc6148')
        text_body = f'Событие: {description_sys_evt_type}\nИсточник: Система\nКлюч: bc6148' \
                    f'\nУправляемые разделы: Раздел №5, Раздел №9, Раздел №11, Раздел №12, Раздел №13, Раздел №14, ' \
                    f'Раздел №19\nПрава: {description_access_law}\nДата и время: 01.01.2022 15:04:50'
        self.open_event(event_info)
        self.app.method.assert_element_text(event_info + '//div[@class="card-body"]', text_body)

    def event_evt_from_system(self, value_sys_evt_type, description_sys_evt_type):
        with allure.step("Эмуляция события по api"):
            data = self.app.endpoint.generate_json_for_system_standard(value_sys_evt_type)
            self.app.endpoint.create_event(data)
        with allure.step(f"Проверка отображения события"):
            self.assert_evt_from_system(value_sys_evt_type, description_sys_evt_type)

    def assert_evt_from_system(self, value_sys_evt_type, description_sys_evt_type):
        locator = event_warning if value_sys_evt_type in [10, 11, 13, 14, 16] else event_info
        self.assert_equal_event_and_value_date(locator)
        if value_sys_evt_type == 1:
            self.app.method.assert_element_text(locator + '//p', f'15:04:50 | {description_sys_evt_type}, Датчик №5')
        else:
            self.app.method.assert_element_text(locator + '//p', f'15:04:50 | {description_sys_evt_type}')
        if value_sys_evt_type in [8, 9]:
            text_body = f'Событие: {description_sys_evt_type}\nИсточник: Система\nОсновной канал: Выключен' \
                        f'\nПервый резеврный канал: СМС Эгида 3\nВторой резервный канал: СМС пользователю' \
                        f'\nДата и время: 01.01.2022 15:04:50'
        elif value_sys_evt_type == 14:
            text_body = f'Событие: {description_sys_evt_type}\nИсточник: Система\nБаланс: 100' \
                        f'\nНомер телефона: 89167115555\nДата и время: 01.01.2022 15:04:50'
        else:
            text_body = f'Событие: {description_sys_evt_type}\nИсточник: Система\nДата и время: 01.01.2022 15:04:50'
        self.open_event(locator)
        self.app.method.assert_element_text(locator + '//div[@class="card-body"]', text_body)

    def event_evt_from_system_add_and_delete_user(
            self, value_sys_evt_type, description_sys_evt_type, value_settings_changes):
        with allure.step("Эмуляция события по api"):
            data = self.app.endpoint.generate_json_for_system_add_delete_user(value_sys_evt_type, value_settings_changes)
            self.app.endpoint.create_event(data)
        with allure.step(f"Проверка отображения события"):
            self.assert_evt_from_system_add_delete_user(description_sys_evt_type, value_settings_changes)

    def assert_evt_from_system_add_delete_user(self, description_sys_evt_type, value_settings_changes):
        self.assert_equal_event_and_value_date(event_info)
        self.app.method.assert_element_text(event_info + '//p', f'15:04:50 | {description_sys_evt_type}')
        settings_description = 'Изменилось имя, Изменился логин, Изменился пароль, Изменился номер телефона, ' \
                               'Изменилась маска разделов, Изменилась структура настроек, Изменился пароль ' \
                               'управления по телефону'
        if value_settings_changes == 0:
            text_body = f'Событие: {description_sys_evt_type}\nИсточник: Система\nДата и время: 01.01.2022 15:04:50'
        else:
            text_body = f'Событие: {description_sys_evt_type}\nИсточник: Система\nНастройки пользователя: ' \
                        f'{settings_description}\nДата и время: 01.01.2022 15:04:50'
        self.open_event(event_info)
        self.app.method.assert_element_text(event_info + '//div[@class="card-body"]', text_body)

    def event_evt_from_system_case_state(self, value_sys_evt_type, description_sys_evt_type,
                                         value_state, value_description, p_event, description):
        with allure.step("Эмуляция события по api"):
            data = self.app.endpoint.generate_json_for_system_case_state(
                value_sys_evt_type, value_state, p_event)
            self.app.endpoint.create_event(data)
        with allure.step(f"Проверка отображения события"):
            locator = event_warning if value_sys_evt_type == 11 else event_info
            self.assert_evt_from_system_case_state(description_sys_evt_type, value_description, description, locator)

    def assert_evt_from_system_case_state(self, description_sys_evt_type, value_description, description, locator):
        self.assert_equal_event_and_value_date(locator)
        self.app.method.assert_element_text(locator + '//p', f'15:04:50 | {description_sys_evt_type}')
        text_body = f'Событие: {description_sys_evt_type}\nИсточник: Система' \
                    f'\nДата и время: 01.01.2022 15:04:50'
        self.open_event(locator)
        self.app.method.assert_element_text(locator + '//div[@class="card-body"]', text_body)

    def display_items_on_journal_page(self):
        with allure.step("Проверка уведомления загрузки журнала и отсутсвия событий в нём"):
            self.app.method.element_wait_to_be_text("span.toast-message-summary", 'Идёт загрузка журнала.')
            # self.app.method.assert_element_text(
            #     toast_error, 'Не удалось получить данные от устройства.\nПопробуйте перезагрузить страницу.')
            self.app.method.assert_element_text(toast_info, 'Идёт загрузка журнала.\nПожалуйста, подождите...')
        with allure.step("Проверка заглушки журнала на отсутствие событий"):
            self.app.method.assert_element_text(text_empty_result, 'Не найдено подходящих событий')
        with allure.step("Проверка элементов и их статусов"):
            self.app.method.assert_count_elements(field_search, 1)
            self.app.method.assert_count_elements(btn_date_picker, 1)
            self.app.method.assert_count_elements(btn_apply, 1)
            self.app.method.assert_count_elements(btn_reset, 1)
            self.app.method.assert_count_elements(btn_reread, 1)
            self.app.method.assertValues('', field_search)
            status = self.app.method.attributeStatusButton(btn_reset)
            assert 'true' == status, f'\nОжидаемый результа {"true"},\nактический результат {status}'

    def assert_result_filters_for_fields(self):
        wd = self.app.wd
        with allure.step("Генерация тестовых событий"):
            self.generate_events()
        with allure.step("Проверка фильтрации по полю 'Поиск' по заголовку события"):
            self.app.method.inputValues('User', field_search)
            self.app.method.click_element_locate(btn_apply)
            self.assert_equal_badges_and_events('1', 1)
            self.app.method.assertTextOnPage(event_header_text, ['TestUser'])
        with allure.step("Проверка фильтрации по полю 'Поиск' по телу события"):
            self.app.method.inputValues('Управление по SMS', field_search)
            self.app.method.click_element_locate(btn_apply)
            self.assert_equal_badges_and_events('1', 2)
            self.assert_body_event('Источник: Управление по SMS')
        with allure.step("Проверка фильтрации по полю 'Поиск' и по дате"):
            self.app.method.inputValues('Раздел', field_search)
            self.set_filter_for_date('2023', 'Февраль', '14', '2023', 'Февраль', '15')
            self.assert_equal_badges_and_events('2', 2)
            self.assert_header_event('Раздел')
            self.assert_body_event('Дата и время: 14.02.2023')
        with allure.step("Проверка фильтрации по полю 'Поиск', по дате и по времени"):
            self.set_filter_for_time('13', '40', '13', '30')
            self.assert_equal_badges_and_events('3', 1)
            self.assert_header_event('Раздел')
            self.app.method.assertTextOnPage(event_body, ['Дата и время: 14.02.2023 13:38:52'])
        with allure.step("Проверка фильтрации по полю 'Поиск' и по времени"):
            self.app.method.click_element_locate(btn_date_picker)
            self.app.method.click_element_locate(field_date + '//button')
            self.set_time_range('16', '00', '13', '00')
            self.app.method.click_element_locate(btn_apply)
            self.assert_equal_badges_and_events('2', 3)
            self.assert_header_event('Раздел')
            min_value = 13*3600
            max_value = 16*3600
            for element in wd.find_elements(By.XPATH, event_header_text):
                text = element.text
                hour, minute, seconds = map(int, text.split(' |')[0].split(":", 2))
                value = hour*3600 + minute*60 + seconds
                assert min_value < value, f"Выход времени за нижнюю границу"
                assert max_value > value, f"Выход времени за верхнюю границу"
        with allure.step("Проверка фильтрации по времени"):
            self.app.method.click_element_locate(btn_reset)
            self.set_filter_for_time('15', '05', '15', '00')
            self.assert_equal_badges_and_events('1', 1)
            self.assert_body_event('Дата и время: 01.01.2022 15:04:50')
        with allure.step("Проверка фильтрации по дате и времени"):
            self.app.method.click_element_locate(btn_date_picker)
            self.set_date_range('2020', 'Август', '3', '2022', 'Январь', '1')
            self.set_time_range('19', '00', '18', '00')
            self.app.method.click_element_locate(btn_apply)
            self.assert_equal_badges_and_events('2', 1)
            self.assert_body_event('Дата и время: 03.08.2020 18:15:52')
        with allure.step("Проверка фильтрации по дате"):
            self.app.method.click_element_locate(btn_reset)
            self.set_filter_for_date('2023', 'Февраль', '14', '2023', 'Февраль', '15')
            self.assert_equal_badges_and_events('1', 2)
            self.assert_body_event('Дата и время: 14.02.2023')
        with allure.step("Проверка пустого результата фильтрации"):
            self.app.method.click_element_locate(btn_reset)
            self.app.method.inputValues('w' * 55, field_search)
            self.app.method.click_element_locate(btn_apply)
            self.assert_equal_badges_and_events('1', 0)
            self.app.method.assert_element_text(text_empty_result, 'Не найдено подходящих событий')

    def assert_body_event(self, expected_text):
        wd = self.app.wd
        for element in wd.find_elements(By.XPATH, event_header):
            element.click()
        time.sleep(0.5)
        for element in wd.find_elements(By.XPATH, event_body):
            assert expected_text in element.text, \
                f"Фактический результат '{element.text}' не содерит подстроку '{expected_text}'"

    def assert_header_event(self, expected_text):
        wd = self.app.wd
        for element in wd.find_elements(By.XPATH, event_header_text):
            assert expected_text in element.text, \
                f"Фактический результат '{element.text}' не содерит подстроку '{expected_text}'"

    def assert_equal_badges_and_events(self, text, equal):
        self.app.method.element_wait_to_be_text(item_badge, text)
        self.app.method.assert_count_elements(event_header_text, equal)

    def set_filter_for_date(self, year_1, month_1, day_1, year_2, month_2, day_2):
        self.app.method.click_element_locate(btn_date_picker)
        self.set_date_range(year_1, month_1, day_1, year_2, month_2, day_2)
        self.app.method.click_element_locate(btn_apply)

    def set_filter_for_time(self, value_h_1, value_m_1, value_h_2, value_m_2):
        self.app.method.click_element_locate(btn_date_picker)
        self.set_time_range(value_h_1, value_m_1, value_h_2, value_m_2)
        self.app.method.click_element_locate(btn_apply)

    def generate_events(self):
        wd = self.app.wd
        self.app.endpoint.create_event_for_filters(0, 6, 1, 1641038690, 'Администратор')
        self.app.endpoint.create_event_for_filters(0, 7, 1, 1676369343, 'Админ')
        self.app.endpoint.create_event_for_filters(16, 0, 4, 1596467752, 'Test')
        self.app.endpoint.create_event_for_filters(17, 0, 4, 1676371132, 'TestUser')
        self.app.endpoint.create_event_for_filters(0, 25, 1, 1642518952, 'User')
        wd.refresh()
        self.app.method.element_wait_to_be_text("span.toast-message-summary", 'Идёт загрузка журнала.')
        self.app.method.click_element_locate('//button[contains(@class, "toast-message-btn-close")]')

    def set_date_range(self, year_1, month_1, day_1, year_2, month_2, day_2):
        self.app.method.click_element_locate(field_date)
        self.chose_date(year_1, month_1, day_1)
        self.chose_date(year_2, month_2, day_2)
        self.app.method.click_element_locate(field_search)

    def chose_date(self, year, month, day):
        self.app.method.click_element_locate(item_year)
        self.app.method.click_element_locate(f"//div[contains(@class, 'years-list')]//div[.='{year}']")
        self.app.method.click_element_locate(f"//div[@class='calendar-wrapper']//div[.='{month}']")
        self.app.method.click_element_locate(f"//button[@class='BTN-text calendar-button']//div[.='{day}']")

    def set_time_range(self, value_h_1, value_m_1, value_h_2, value_m_2):
        self.app.method.click_element_locate(field_time)
        self.set_field_time('00', '00', '1')
        self.set_field_time(value_h_1, value_m_1, '2')
        self.set_field_time(value_h_2, value_m_2, '1')
        self.app.method.click_element_locate(btn_date_picker_apply)

    def set_field_time(self, value_h, value_m, index):
        wd = self.app.wd
        self.app.method.click_element_locate(f'(// div[@ aria-label="Open hours overlay"])[{index}]')
        if int(value_h) > 14:
            element = wd.find_element(By.CSS_SELECTOR, 'div:nth-child(9) > div:nth-child(3) > div')
            wd.execute_script("arguments[0].scrollIntoView();", element)
        self.app.method.click_element_locate(f"//div[@class='dp__overlay_col']/div[.={value_h}]")
        self.app.method.click_element_locate(f'(//div[@aria-label="Open minutes overlay"])[{index}]')
        self.app.method.click_element_locate(f"//div[@class='dp__overlay_col']/div[.={value_m}]")

    def assert_reset_result_filters(self):
        self.generate_events()
        self.app.method.inputValues('Раздел', field_search)
        self.app.method.click_element_locate(btn_date_picker)
        self.set_date_range('2020', 'Август', '3', '2022', 'Январь', '1')
        self.set_time_range('19', '00', '18', '00')
        self.app.method.click_element_locate(btn_apply)
        self.app.method.check_hide_element(item_badge, btn_reset)
        self.app.method.assertValues('', field_search)
        self.app.method.click_element_locate(btn_date_picker)
        self.app.method.assertValues(None, field_time)
        self.app.method.assertValues(None, field_date)

    def set_name_for_exit_two(self):
        self.app.PO_Navigations.goToZonePathPage()
        self.app.PO_Navigations.goToZonePathOuts()
        self.app.PO_Settings.edit_button_click()
        self.app.method.inputValues("output_second", name_out_2)
        self.app.PO_Zone_Path.save_button_click()

    def set_name_partition(self):
        self.app.PO_Navigations.goToZonePathPage()
        self.app.PO_Navigations.goToPathPage()
        self.app.PO_Zone_Path.settings_first_path_button()
        self.app.method.inputValues('Раздел № 01', '//*[.="Название"]//input[1]')
        self.app.PO_Zone_Path.save_button_settings_click()
