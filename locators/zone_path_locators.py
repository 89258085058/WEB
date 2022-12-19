# -*- coding: utf-8 -*-

"""РАЗДЕЛЫ"""
# ------------Текст на странице------------
data_add_path_modal_text = '//div[@class="modal card"]'
# ------------Список разделов------------
path_row = '//*[@id="app"]/main//div[@class="main-info"]'

# ------------КНОПКИ------------
add_path_button = '//*[@id="app"]//button[@class="BTN-indigo control-btn-desktop"]'
settings_first_path_button = '(//*[@id="app"]//button[@class="BTN-secondary block BTN-auto-icon"][.="Настройки"])[1]'
settings_2_path_button = '(//*[@id="app"]//button[@class="BTN-secondary block BTN-auto-icon"][.="Настройки"])[2]'
cancel_button = '(//*[.=" Отменить "]//div)[last()]'
cross_close_button = '//*[@id="app"]/main//div[@class="reset-icon"]'
save_button = '(//*[.=" Сохранить "]/div)[1]'
save_button_path = '(//*[.="Сохранить"]/div)[1]'

# ------------ПОЛЯ ВВОДА------------
Search = '//*[@id="app"]/main//div/input'
namber_path = '//*[.="Номер АРМ Орион"]//input[1]'
name_path = '//*[.="Название"]//input[1]'

namber_path_on_page = '(//*[@id="app"]//div[@class="number"]/span)[2]'
name_path_on_page = '//*[@id="app"]//div[@class="name"]/span'

# ------------ВЫПАДАЮЩИЙ СПИСОК-----
# Выпадающий спосок - опция
positions_check_box = '(/html/body//div[@class="b-multiselect-items"]//label[@class="checkbox"])'
status_drop_list_check_box = '(//*[@class="b-multiselect-items-wrapper scrollable"]//label/input)'
# Кнопка выпадающего списка Управляющие разделы
controlled_sections_button = '(/html/body//div[@class="b-multiselect-label"])[1]'

# ------------ЧЕКБОКСЫ-------------
# Задержка взятия
Take_Delay_click = '(/html/body//label/span)[1]'
Take_Delay_status = '(/html/body//label/input)[1]'
# Автовзятие из невзятия
Auto_pickup_from_non_pickup_click = '(/html/body//label/span)[2]'
Auto_pickup_from_non_pickup_status = '(/html/body//label/input)[2]'
# Автовзятие из невзятия
Auto_arm_from_alarm_click = '(/html/body//label/span)[3]'
Auto_arm_from_alarm_status = '(/html/body//label/input)[3]'

"""ВЫХОДЫ"""
# ------------Текст на странице------------
locator_out_1_text = '(//*[@id="app"]/main//div[@class="main-section"])[1]'
locator_out_2_text = '(//*[@id="app"]/main//div[@class="main-section"])[2]'

# ------------ВЫПАДАЮЩИЕ СПИСКИ------------
# Кнопка выпадающего списка Режим работы
Working_mode_out_1 = '(//*[.="Режим работы"]/following::span[1])[1]'
Working_mode_out_2 = '(//*[.="Режим работы"]/following::span[1])[2]'
Output_group_number = '(//*[.="Номер группы выходов"]/following::span[1])[1]'
# Выбор опции
option_key = '(/html/body//div[@class="option"])'

# ------------ПОЛЯ ВВОДА------------
name_out_1 = '(//*[.="Название"]//input[1])[1]'
name_out_2 = '(//*[.="Название"]//input[1])[2]'
hysteresis_out = '//*[.="Гистерезис"]/following::input[1]'
control_sensor_out = '(//*[.="Внутренний сигнал задания *"]//input[1])[1]'

# Код настройки
code_setting_out_1 = '(//*[.="Код настройки"]//input[1])[1]'
code_setting_out_2 = '(//*[.="Код настройки"]//input[1])[2]'
code_setting_out_mask_2_on = '(//*[.="Код настройки"]//input[1])[3]'
code_setting_out_mask_2_off = '(//*[.="Код настройки"]//input[1])[4]'


# ------------КНОПКИ------------
# Список событий Выходы - 1/2
list_of_events_1 = '(//*[.="Список событий"]/i)[1]'
list_of_events_2 = '(//*[.="Список событий"]/i)[2]'
# Маска включения Выходы - 1/2
mask_on_settings_out_1 = '(//*[.="Маска включения"]/i)[1]'
mask_on_settings_out_2 = '(//*[.="Маска включения"]/i)[2]'
# Маска выключения Выходы - 1/2
mask_off_settings_out_1 = '(//*[.="Маска выключения"]/i)[1]'
mask_off_settings_out_2 = '(//*[.="Маска выключения"]/i)[2]'
# Взятие
out_1_take_on_button = '(//*[.="Взятие"]//button)[1]'
out_2_take_on_button = '(//*[.="Взятие"]//button)[2]'
# Снятие
out_1_take_off_button = '(//*[.="Снятие"]//button)[1]'
out_2_take_off_button = '(//*[.="Снятие"]//button)[2]'
# Принудительное взятие
out_1_forced_take_button = '(//*[.="Принудительное взятие"]//button)[1]'
out_2_forced_take_button = '(//*[.="Принудительное взятие"]//button)[2]'
# Невзятие
out_1_not_taking_button = '(//*[.="Невзятие"]//button)[1]'
out_2_not_taking_button = '(//*[.="Невзятие"]//button)[2]'
# Пожар
out_1_fire_button = '(//*[.="Пожар"]//button)[1]'
out_2_fire_button = '(//*[.="Пожар"]//button)[2]'
# Тревога
out_1_alarm_button = '(//*[.="Тревога"]//button)[1]'
out_2_alarm_button = '(//*[.="Тревога"]//button)[2]'

# ------------ЧЕКБОКСЫ-------------
# Взятие
out_1_take_on_click = '(//*[.="Взятие"]//span[@class="checkmark-container"][1])[1]'
out_1_take_on_status = '(//*[.="Взятие"]//label/input)[1]'
out_2_take_on_click = '(//*[.="Взятие"]//span[@class="checkmark-container"][1])[2]'
out_2_take_on_status = '(//*[.="Взятие"]//label/input)[2]'
# Снятие
out_1_take_off_click = '(//*[.="Снятие"]//span[@class="checkmark-container"][1])[1]'
out_1_take_off_status = '(//*[.="Снятие"]//label/input)[1]'
out_2_take_off_click = '(//*[.="Снятие"]//span[@class="checkmark-container"][1])[2]'
out_2_take_off_status = '(//*[.="Снятие"]//label/input)[2]'
# Принудительное взятие
out_1_forced_take_click = '(//*[.="Принудительное взятие"]//span[@class="checkmark-container"][1])[1]'
out_1_forced_take_status = '(//*[.="Принудительное взятие"]//label/input)[1]'
out_2_forced_take_click = '(//*[.="Принудительное взятие"]//span[@class="checkmark-container"][1])[2]'
out_2_forced_take_status = '(//*[.="Принудительное взятие"]//label/input)[2]'
# Невзятие
out_1_not_taking_click = '(//*[.="Невзятие"]//span[@class="checkmark-container"][1])[1]'
out_1_not_taking_status = '(//*[.="Невзятие"]//label/input)[1]'
out_2_not_taking_click = '(//*[.="Невзятие"]//span[@class="checkmark-container"][1])[2]'
out_2_not_taking_status = '(//*[.="Невзятие"]//label/input)[2]'
# Пожар
out_1_fire_click = '(//*[.="Пожар"]//span[@class="checkmark-container"][1])[1]'
out_1_fire_status = '(//*[.="Пожар"]//label/input)[1]'
out_2_fire_click = '(//*[.="Пожар"]//span[@class="checkmark-container"][1])[2]'
out_2_fire_status = '(//*[.="Пожар"]//label/input)[2]'
# Тревога
out_1_alarm_click = '(//*[.="Тревога"]//span[@class="checkmark-container"][1])[1]'
out_1_alarm_status = '(//*[.="Тревога"]//label/input)[1]'
out_2_alarm_click = '(//*[.="Тревога"]//span[@class="checkmark-container"][1])[2]'
out_2_alarm_status = '(//*[.="Тревога"]//label/input)[2]'

# ------------Виджет ползунок------------
# Время
time_widget_out_1 = '(//*[@id="app"]/main//div[@class="time-control"]/div)[1]'
time_widget_out_2 = '(//*[@id="app"]/main//div[@class="time-control"]/div)[3]'
time_widget_out_1_class = '(//*[@class="time-control"]/div)[1]'
time_widget_out_2_class = '(//*[@class="time-control"]/div)[3]'
widget_out_1 = '(//*[.="Время"]/following::input[1])[1]'
widget_out_2 = '(//*[.="Время"]/following::input[1])[2]'

widget_out_2_mask_settings_on = '(//*[.="Время"]/following::input[1])[3]'
widget_out_2_mask_settings_off = '(//*[.="Время"]/following::input[1])[4]'

# ------------Тумблер------------
# Включить по окончанию
off_end_tumbler_out_1 = '(//*[@id="app"]/main//label[@class="switch"]/input)[1]'
off_end_tumbler_out_2 = '(//*[@id="app"]/main//label[@class="switch"]/input)[2]'
off_end_tumbler_out_1_click = '(//*[.="Включить по окончанию"]//label/span)[1]'
off_end_tumbler_out_1_status = '(//*[.="Включить по окончанию"]//label/input)[1]'
off_end_tumbler_out_2_click = '(//*[.="Включить по окончанию"]//label/span)[2]'
off_end_tumbler_out_2_status = '(//*[.="Включить по окончанию"]//label/input)[2]'
mask_settings_tumbler_out_1_click_on = '(//*[.="Включить по окончанию"]//label/span)[3]'
mask_settings_tumbler_out_1_status_on = '(//*[.="Включить по окончанию"]//label/input)[3]'
mask_settings_tumbler_out_1_click_off = '(//*[.="Включить по окончанию"]//label/span)[4]'
mask_settings_tumbler_out_1_status_off = '(//*[.="Включить по окончанию"]//label/input)[4]'
# Инверсия управления
Inversion_of_control_tumbler_out_1_click = '(//*[.="Инверсия управления"]//label/span)[1]'
Inversion_of_control_tumbler_out_1_status = '(//*[.="Инверсия управления"]//label/input)[1]'
Inversion_of_control_tumbler_out_2_click = '(//*[.="Инверсия управления"]//label/span)[1]'
Inversion_of_control_tumbler_out_2_status = '(//*[.="Инверсия управления"]//label/input)[1]'
# Разрешить управление по SMS
Allow_control_by_SMS_1_click = '(//*[.="Разрешить управление по SMS"]//label/span)[1]'
Allow_control_by_SMS_1_status = '(//*[.="Разрешить управление по SMS"]//label/input)[1]'
Allow_control_by_SMS_2_click = '(//*[.="Разрешить управление по SMS"]//label/span)[2]'
Allow_control_by_SMS_2_status = '(//*[.="Разрешить управление по SMS"]//label/input)[2]'
# Разрешить управление звонком
Allow_call_control_1_click = '(//*[.="Разрешить управление звонком"]//label/span)[1]'
Allow_call_control_1_status = '(//*[.="Разрешить управление звонком"]//label/input)[1]'
Allow_call_control_2_click = '(//*[.="Разрешить управление звонком"]//label/span)[2]'
Allow_call_control_2_status = '(//*[.="Разрешить управление звонком"]//label/input)[2]'
# Разрешить управление брелоком
Allow_key_control_1_click = '(//*[.="Разрешить управление брелоком"]//label/span)[1]'
Allow_key_control_1_status = '(//*[.="Разрешить управление брелоком"]//label/input)[1]'
Allow_key_control_2_click = '(//*[.="Разрешить управление брелоком"]//label/span)[2]'
Allow_key_control_2_status = '(//*[.="Разрешить управление брелоком"]//label/input)[2]'


# ------------Маска------------
mask_out = '(//*[@id="app"]/main//label[@class="checkbox small"]/input)'
mask_settings_click = '(//*[.="Маска"]//label/span)'
mask_settings_status = '(//*[.="Маска"]//label/input)'



