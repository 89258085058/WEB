# -*- coding: utf-8 -*-

"""ОБНОВЛЕНИЯ"""

# Элементы блока версия устройства
card_version_device = '//div[contains(@class, "current-info__item--secondary")]'
text_version_device = f'{card_version_device}/div/h5'
text_version_device_name = f'{card_version_device}/div/p'
text_version_device_button = f'{card_version_device}/button'
text_device_version = f'{card_version_device}/h4'
modal_info_version_device = '//div[@class="b-dialog"]'
btn_modal_close = '//div[@class="b-dialog"]//button'

# Элементы блока текущая версия ПО
card_version_po = '//div[contains(@class, "current-info__item--primary")]'
text_version_po = f'{card_version_po}/div/h5'
text_version_po_date = f'{card_version_po}/div/p'
text_po_version = f'{card_version_po}/h4'

# Элементы блока версия Веб-интерфейса
card_version_web = '//div[contains(@class, "current-info__item--base")]'
text_version_web = f'{card_version_web}/div/h5'
text_version_web_date = f'{card_version_web}/div/p'
text_web_version = f'{card_version_web}/h4'

# Форма загрузки
text_form = '//form/label'


