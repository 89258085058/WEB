# -*- coding: utf-8 -*-

from dataclasses import dataclass

from data.pages_text import *
from locators.update_locators import *


@dataclass
class UpdateHelper:
    app: any

    # Проверка полей на странице блок: Сигнал GSM Р исп. 0 изм.7
    def text_update_device(self):
        self.app.method.assertTextOnPage(update_page_text_update_device, update_device_text_content)

    # Проверка полей на странице блок: Обновление прошивки
    def text_update(self):
        self.app.method.assertTextOnPage(update_page_text_update, update_louder_text_content)
