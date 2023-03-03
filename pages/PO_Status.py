# -*- coding: utf-8 -*-
import time
from dataclasses import dataclass

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *
from data.pages_text import *
from locators.status_locators import *


@dataclass
class StatusHelper:
    app: any

    # Проверка полей на странице Разделы
    def text_status_path(self):
        self.app.method.assertTextOnPage(path_data_status_text, path_status_text_content)

    # Проверка полей на странице Батареи
    def text_status_batteries(self):
        self.app.method.assertTextOnPage(batteries_data_status_text, batteries_status_text_content)

    # Проверка полей на странице gsm
    def text_status_gsm(self):
        self.app.method.assertTextOnPage(gsm_data_status_text, gsm_status_text_content)

    # Проверка полей на странице Источник питания
    def text_status_power(self):
        self.app.method.assertTextOnPage(power_data_status_text, power_status_text_content)

    # Проверка полей на странице Источник Сеть
    def text_status_ethernet(self):
        self.app.method.assertTextOnPage(ethernet_data_status_text, ethernet_status_text_content)

    # Проверка полей на странице Источник Состояние прибора
    def text_status_device(self):
        self.app.method.assertTextOnPage(device_data_status_text, device_status_text_content)

    # Проверка полей на странице Прочее
    def text_status_others(self):
        self.app.method.assertTextOnPage(others_data_status_text, others_status_text_content)

    # Проверка полей на странице gsm sim1
    def text_status_gsm_sim_1(self):
        self.app.method.assertTextOnPage(gsm_data_status_text_sim_1, gsm_status_text_content_SIM)

    # Проверка полей на странице gsm sim2
    def text_status_gsm_sim_2(self):
        self.app.method.assertTextOnPage(gsm_data_status_text_sim_2, gsm_status_text_content_SIM)

    # Раскрытие настроек сим 1
    def open_sim_1(self):
        time.sleep(0.5)
        self.app.method.click((By.XPATH, sim_1_button))

    # Раскрытие настроек сим 2
    def open_sim_2(self):
        time.sleep(0.5)
        self.app.method.click((By.XPATH, sim_2_button))

    #Блок проверки эмулируемых статусов разделов
    def assert_status_partition(self, value_status, description_status):
        with allure.step("Эмуляция статуса раздела"):
            self.app.endpoint.add_partition_status(self.app.endpoint.add_partition_with_status(value_status))
        with allure.step("Проверка отображения статуса раздела {description_status} на вкладке 'Статус'"):
            status = self.get_locator_for_tab_status(value_status)
            locator = f"//div[.='fake_part']/..//span[contains(@class, '{status}')]"
            assert 1 == self.app.method.elements_count(locator), \
                f"\nОжидаемый результат {1}\nФактический результат {self.app.method.elements_count(locator)}"
            self.app.method.assert_element_text(locator, description_status)
        with allure.step("Проверка отображения статуса раздела {description_status} на вкладке 'Зоны/Разделы'"):
            self.app.PO_Navigations.goToZonePathPage()
            status = 'successful' if value_status == 9 else status
            locator = f"//div[.='fake_part']/..//span[@class ='status {status}']"
            assert 1 == self.app.method.elements_count(locator), \
                f"\nОжидаемый результат {1}\nФактический результат {self.app.method.elements_count(locator)}"
            self.app.method.assert_element_text(locator, description_status)

    def get_locator_for_tab_status(self, param):
        if param == 9:
            return 'success'
        elif param in [4, 8, 12, 16, 17, 18, 21, 22]:
            return 'primary'
        elif param in [0, 1]:
            return 'secondary'
        elif param in [2, 3, 5, 6, 7, 19, 20]:
            return 'warning'
        elif param in [10, 11, 13, 14, 15]:
            return 'error'

    def delete_fake_partition(self):
        self.app.endpoint.add_partition_status(self.app.endpoint.add_partition_with_status(1))
        self.app.PO_Navigations.ExitAndEnter()


    def assert_status_sensor(self, z_event, description):
        with allure.step("Эмуляция статуса датчика"):
            self.app.endpoint.add_sensor_status(self.app.endpoint.add_sensor_with_status(z_event))
        with allure.step("Проверка отображения статуса датчика"):
            status = self.get_locator_for_sensor(z_event)
            locator = f"//div[.='FAKE']/..//span[contains(@class, '{status}')]"
            assert 1 == self.app.method.elements_count(locator), \
                f"\nОжидаемый результат {1}\nФактический результат {self.app.method.elements_count(locator)}"
            self.app.method.assert_element_text(locator, description)

    def delete_fake_sensor(self):
        with allure.step("Удаление дачтика"):
            self.app.method.click_element_locate("//div[.='FAKE']/../..//button[contains(@class, 'BTN-error')]")

    def get_locator_for_sensor(self, z_event):
        if z_event in [0, 1, 15]:
            return 'secondary'
        elif z_event in [2, 12]:
            return 'success'
        elif z_event in [3, 4, 5, 6, 7, 8, 9, 10, 11, 24, 34, 35]:
            return 'error'
        elif z_event in [13, 18, 20, 21, 23, 29, 31, 32, 33]:
            return 'warning'
        elif z_event in [14, 16, 17, 19, 22, 25, 26, 27, 28, 30, 36]:
            return 'primary'

    def assert_status_device(self, status, description):
        with allure.step("Эмуляция статуса устроуства"):
            self.app.endpoint.change_status_device(status)
        with allure.step("Проверка отображения статуса датчика"):
            if description == 'НЕИЗВЕСТНО':
                locator = "(//div[.='fake_signal']/../..//span[@class])[1]"
            else:
                status_device = self.get_locator_for_device(status)
                locator = f"//div[.='fake_signal']/../..//span[@class='{status_device}']"
            assert 1 == self.app.method.elements_count(locator), \
                f"\nОжидаемый результат {1}\nФактический результат {self.app.method.elements_count(locator)}"
            self.wait_text_status(locator)
            self.app.method.assert_element_text(locator, description)

    def add_fake_device(self):
        wd = self.app.wd
        cookies = wd.get_cookies()[1].get('value')
        self.app.endpoint.add_device(cookies)
        self.app.session.logout()
        wd.switch_to.window(wd.window_handles[0])

    def get_locator_for_device(self, status_device):
        if status_device in [2, 11]:
            return 'success'
        elif status_device in [3, 5, 7, 8, 9]:
            return 'warning'
        elif status_device in [4, 6]:
            return 'error'
        elif status_device in [10]:
            return 'second'

    @staticmethod
    def element_text_is_not_empty(selector):
        def call(webdriver):
            return webdriver.find_element(By.XPATH, selector).text != ""

        return call

    def wait_text_status(self, locator):
        try:
            wd = self.app.wd
            WebDriverWait(wd, 3).until(self.element_text_is_not_empty(locator))
        except Exception as e:
            assert e == TimeoutException, f"Ожидаемый текст статуса не отобразился"

    def delete_fake_device(self):
        wd = self.app.wd
        self.app.method.click_element_locate("//div[.='fake_signal']/../..//button[1]")
        self.app.method.click_element_locate("//span[.='Удалить']")
        self.app.method.click_element_locate("//div[.=' Удалить ']")
        wd.switch_to.window(wd.window_handles[1])
        self.app.session.login_enter("admin", "admin")
