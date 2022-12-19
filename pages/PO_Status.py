# -*- coding: utf-8 -*-
import time

from selenium.webdriver.common.by import By

from data.pages_text import *
from locators.status_locators import *


class StatusHelper:

    def __init__(self, app):
        self.app = app

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

