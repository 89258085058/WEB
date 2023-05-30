# -*- coding: utf-8 -*-
import re
from dataclasses import dataclass

from data.pages_text import *
from locators.update_locators import *


@dataclass
class UpdateHelper:
    app: any

    def display_items_update(self):
        self.app.method.assert_element_text(text_version_device, 'Версия устройства')
        self.app.method.assert_element_text(text_version_device_name, 'Сигнал GSM Р')
        self.app.method.assert_element_text(text_version_po, 'Текущая версия ПО')
        self.app.method.assert_element_text(text_version_web, 'Версия Веб-интерфейса')
        self.app.method.assert_element_text(text_form, update_louder_text_content)
        value_device_version = self.app.method.getText(text_device_version)
        assert re.match(r'\d+\.\d+', value_device_version) is not None, f'Формат версии отображается некоррекнтно'
        value_po_version = self.app.method.getText(text_device_version)
        assert re.match(r'\d+\.\d+', value_po_version) is not None, f'Формат версии отображается некоррекнтно'
        value_web_version = self.app.method.getText(text_device_version)
        assert re.match(r'\d+\.\d+', value_web_version) is not None, f'Формат версии отображается некоррекнтно'
        value_version_po_date = self.app.method.getText(text_version_po_date)
        assert re.match(r'(0[1-9]|[12][0-9]|3[01])\s[а-яА-Я]{3}\s(202)\d', value_version_po_date) is not None, \
            f'Формат даты неверный'
        value_version_web_date = self.app.method.getText(text_version_web_date)
        assert re.match(r'(0[1-9]|[12][0-9]|3[01])\s[а-яА-Я]{3}\s(202)\d', value_version_web_date) is not None, \
            f'Формат даты неверный'
        self.app.method.click_element_locate(text_version_device_button)
        try:
            self.app.method.assertTextOnPage(modal_info_version_device, update_device_text_content)
        finally:
            self.app.method.click_element_locate(btn_modal_close)
