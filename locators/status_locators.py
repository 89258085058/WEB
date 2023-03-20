# -*- coding: utf-8 -*-
"""СТАТУС"""
# ------------Текст на странице------------
path_data_status_text = '//*[@id="app"]//div[@class="partitions-block card"]'
batteries_data_status_text = '//*[@id="app"]//div[@class="batteries-block card"]'
gsm_data_status_text = '//*[@id="app"]//div[@class="gsm-block card"]'
gsm_data_status_text_sim_1 = '(//*[@id="app"]//div[@class="accordion accordion--open"])[1]'
gsm_data_status_text_sim_2 = '(//*[@id="app"]//div[@class="accordion accordion--open"])[2]'
power_data_status_text = '//*[@id="app"]//div[@class="power-block card"]'
ethernet_data_status_text = '//*[@id="app"]//div[@class="ethernet-block card"]'
device_option_data_status_text = '(//*[@id="app"]//div[@class="device-state-block card"])[1]'
device_data_status_text = '(//*[@id="app"]//div[@class="device-state-block card"])[2]'
others_data_status_text = '//*[@id="app"]//div[@class="others-block card"]'
# ------------Кнопки------------
sim_1_button = '(//*[@id="app"]//i[@class="b-panel__header-icon"])[1]'
sim_2_button = '(//*[@id="app"]//i[@class="b-panel__header-icon"])[2]'
# ---Статусы
status_primary = "//div[.='fake_part']/..//span[contains(@class, 'primary')]"
status_success = "//div[.='fake_part']/..//span[contains(@class, 'success')]"
status_secondary = "//div[.='fake_part']/..//span[contains(@class, 'secondary')]"
status_warning = "//div[.='fake_part']/..//span[contains(@class, 'warning')]"
status_danger = "//div[.='fake_part']/..//span[contains(@class, 'error')]"
