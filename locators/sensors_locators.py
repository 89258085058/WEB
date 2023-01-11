# -*- coding: utf-8 -*-

# выбор первого пункта настроек
settings_button_first = '(//button[@class="BTN-secondary block BTN-auto-icon"])[1]'

"""Сирена"""
# ------------ПОЛЯ ВВОДА------------
name = '//*[.="Название"]//input'
# Код настройки
code_setting_light = '(//*[.="Код настройки"]//input[1])[1]'
code_setting_volum = '(//*[.="Код настройки"]//input[1])[2]'
code_setting_out_mask_2_on = '(//*[.="Код настройки"]//input[1])[3]'
code_setting_out_mask_2_off = '(//*[.="Код настройки"]//input[1])[4]'

# ------------ВЫПАДАЮЩИЕ СПИСКИ------------
options = '(/html/body//div[@class="option"])'
# Режим светодиодов для охранных датчиков
indication_mode = '(/html/body//span[@class="label"])[1]'
# Номер группы выходов
num_group_outs_1 = '(/html/body//span[@class="label"])[3]'
num_group_outs_2 = '(/html/body//span[@class="label"])[5]'

# Кнопка выпадающего списка Режим работы
Working_mode_out_1 = '(//*[.="Режим работы"]/following::span[1])[1]'
Working_mode_out_2 = '(//*[.="Режим работы"]/following::span[1])[2]'

# ------------Текст на странице------------
locator_out_1_text = '(/html/body//div[@class="out-section"])[1]'
locator_out_2_text = '(/html/body//div[@class="out-section"])[2]'

# ------------КНОПКИ------------
# Настройки
settings_button = '(//*[.="Настройки"])[last()]'
# Список событий Выходы - 1/2
list_of_events_1 = '(//*[.="Список событий"]/i)[1]'
list_of_events_2 = '(//*[.="Список событий"]/i)[2]'
# Маска включения Выходы - 1/2
mask_on_settings_light = '(//*[.="Маска включения"]/i)[1]'
mask_on_settings_volum = '(//*[.="Маска включения"]/i)[2]'
# Маска включения Выходы - 1/2
mask_off_settings_light = '(//*[.="Маска выключения"]/i)[1]'
mask_off_settings_volum = '(//*[.="Маска выключения"]/i)[2]'
# Взятие
light_take_on_button = '(//*[.="Взятие"]//button)[1]'
volum_take_on_button = '(//*[.="Взятие"]//button)[2]'
# Снятие
light_take_off_button = '(//*[.="Снятие"]//button)[1]'
volum_take_off_button = '(//*[.="Снятие"]//button)[2]'
# Принудительное взятие
light_forced_take_button = '(//*[.="Принудительное взятие"]//button)[1]'
volum_forced_take_button = '(//*[.="Принудительное взятие"]//button)[2]'
# Невзятие
light_not_taking_button = '(//*[.="Невзятие"]//button)[1]'
volum_not_taking_button = '(//*[.="Невзятие"]//button)[2]'
# Пожар
light_fire_button = '(//*[.="Пожар"]//button)[1]'
volum_fire_button = '(//*[.="Пожар"]//button)[2]'
# Тревога
light_alarm_button = '(//*[.="Тревога"]//button)[1]'
volum_alarm_button = '(//*[.="Тревога"]//button)[2]'

# ------------ЧЕК-БОКСЫ------------
# Включение датчика
sirena_main_click = '(//*[.="Включение датчика"]//span[@class="checkmark-container"][1])[1]'
sirena_main_status = '(//*[.="Включение датчика"]//label/input)[1]'
# Взятие
light_take_on_click = '(//*[.="Взятие"]//span[@class="checkmark-container"][1])[1]'
light_take_on_status = '(//*[.="Взятие"]//label/input)[1]'
volum_take_on_click = '(//*[.="Взятие"]//span[@class="checkmark-container"][1])[2]'
volum_take_on_status = '(//*[.="Взятие"]//label/input)[2]'
# Снятие
light_take_off_click = '(//*[.="Снятие"]//span[@class="checkmark-container"][1])[1]'
light_take_off_status = '(//*[.="Снятие"]//label/input)[1]'
volum_take_off_click = '(//*[.="Снятие"]//span[@class="checkmark-container"][1])[2]'
volum_take_off_status = '(//*[.="Снятие"]//label/input)[2]'
# Принудительное взятие
light_forced_take_click = '(//*[.="Принудительное взятие"]//span[@class="checkmark-container"][1])[1]'
light_forced_take_status = '(//*[.="Принудительное взятие"]//label/input)[1]'
volum_forced_take_click = '(//*[.="Принудительное взятие"]//span[@class="checkmark-container"][1])[2]'
volum_forced_take_status = '(//*[.="Принудительное взятие"]//label/input)[2]'
# Невзятие
light_not_taking_click = '(//*[.="Невзятие"]//span[@class="checkmark-container"][1])[1]'
light_not_taking_status = '(//*[.="Невзятие"]//label/input)[1]'
volum_not_taking_click = '(//*[.="Невзятие"]//span[@class="checkmark-container"][1])[2]'
volum_not_taking_status = '(//*[.="Невзятие"]//label/input)[2]'
# Пожар
light_fire_click = '(//*[.="Пожар"]//span[@class="checkmark-container"][1])[1]'
light_fire_status = '(//*[.="Пожар"]//label/input)[1]'
volum_fire_click = '(//*[.="Пожар"]//span[@class="checkmark-container"][1])[2]'
volum_fire_status = '(//*[.="Пожар"]//label/input)[2]'
# Тревога
light_alarm_click = '(//*[.="Тревога"]//span[@class="checkmark-container"][1])[1]'
light_alarm_status = '(//*[.="Тревога"]//label/input)[1]'
volum_alarm_click = '(//*[.="Тревога"]//span[@class="checkmark-container"][1])[2]'
volum_alarm_status = '(//*[.="Тревога"]//label/input)[2]'

# ------------Тумблер------------
# Включить по окончанию
off_end_tumbler_light = '(//*[@id="app"]/main//label[@class="switch"]/input)[1]'
off_end_tumbler_volum = '(//*[@id="app"]/main//label[@class="switch"]/input)[2]'
off_end_tumbler_light_click = '(//*[.="Включить по окончанию"]//label/span)[1]'
off_end_tumbler_light_status = '(//*[.="Включить по окончанию"]//label/input)[1]'
off_end_tumbler_volum_click = '(//*[.="Включить по окончанию"]//label/span)[2]'
off_end_tumbler_volum_status = '(//*[.="Включить по окончанию"]//label/input)[2]'
off_end_tumbler_volum_click_mask_on = '(//*[.="Включить по окончанию"]//label/span)[3]'
off_end_tumbler_volum_status_mask_on = '(//*[.="Включить по окончанию"]//label/input)[3]'

modulation_tumbler_light_click = '(//*[.="Модуляция"]//label/span)[1]'
modulation_tumbler_light_status = '(//*[.="Модуляция"]//label/input)[1]'
modulation_tumbler_volum_click = '//*[.="Модуляция"]//label/span'
modulation_tumbler_volum_status = '//*[.="Модуляция"]//label/input'
mask_settings_tumbler_light_click_on = '(//*[.="Включить по окончанию"]//label/span)[3]'
mask_settings_tumbler_light_status_on = '(//*[.="Включить по окончанию"]//label/input)[3]'
mask_settings_tumbler_volum_click_off = '(//*[.="Включить по окончанию"]//label/span)[4]'
mask_settings_tumbler_volum_status_off = '(//*[.="Включить по окончанию"]//label/input)[4]'
# Включить по окончанию
Inversion_of_control_tumbler_light_click = '(//*[.="Инверсия управления"]//label/span)[1]'
Inversion_of_control_tumbler_light_status = '(//*[.="Инверсия управления"]//label/input)[1]'
Inversion_of_control_tumbler_volum_click = '(//*[.="Инверсия управления"]//label/span)[2]'
Inversion_of_control_tumbler_volum_status = '(//*[.="Инверсия управления"]//label/input)[2]'

# Световая индикация тумблеры Разрешить управление по SMS
Allow_control_by_SMS_1_click = '(//*[.="Разрешить управление по SMS"]//label/span)[1]'
Allow_control_by_SMS_1_status = '(//*[.="Разрешить управление по SMS"]//label/input)[1]'
Allow_control_by_SMS_2_click = '(//*[.="Разрешить управление по SMS"]//label/span)[2]'
Allow_control_by_SMS_2_status = '(//*[.="Разрешить управление по SMS"]//label/input)[2]'
# Световая индикация тумблеры Разрешить управление звонком
Allow_call_control_1_click = '(//*[.="Разрешить управление звонком"]//label/span)[1]'
Allow_call_control_1_status = '(//*[.="Разрешить управление звонком"]//label/input)[1]'
Allow_call_control_2_click = '(//*[.="Разрешить управление звонком"]//label/span)[2]'
Allow_call_control_2_status = '(//*[.="Разрешить управление звонком"]//label/input)[2]'
# Световая индикация тумблеры Разрешить управление брелоком
Allow_key_control_1_click = '(//*[.="Разрешить управление брелоком"]//label/span)[1]'
Allow_key_control_1_status = '(//*[.="Разрешить управление брелоком"]//label/input)[1]'
Allow_key_control_2_click = '(//*[.="Разрешить управление брелоком"]//label/span)[2]'
Allow_key_control_2_status = '(//*[.="Разрешить управление брелоком"]//label/input)[2]'

# ------------Маска------------
mask = '(//*//label[@class="checkbox small"]/input)'
mask_settings_click = '(//*[.="Маска"]//label/span)'
mask_settings_status = '(//*[.="Маска"]//label/input)'

# ------------Виджет ползунок------------
# Время
time_widget_light = '(//*//div[@class="time-control"]/div)[1]'
time_widget_volum = '(//*//div[@class="time-control"]/div)[3]'
widget_light = '(//*[.="Время"]/following::input[1])[1]'
widget_volum = '(//*[.="Время"]/following::input[1])[2]'
widget_light_mask = '(//*[.="Время"]/following::input[1])[3]'
widget_light_mask_2 = '(//*[.="Время"]/following::input[1])[4]'
# Громкость
volum_widget_light = '(//*//div[@class="slot-container"]/div)[4]'
volum_widget_volum = '(//*//div[@class="slot-container"]/div)[8]'
widget_volum_light = '(//*[.="Громкость"]/following::input[1])[1]'
widget_volum_volum = '(//*[@id="modalSettings"]//div[@class="b-range-slider"]/input)[2]'

"""Брелоки"""
# Модальное окно
modal_window = '//*[@id="modalSettings"]//div[@class="control-wrappper"]'

# ------------ЧЕКБОКСЫ-------------
# Включение датчика
brelock_senser_on_click = '//*[.="Включение датчика"]//label/span'
brelock_senser_on_status = '//*[.="Включение датчика"]//label/input'
# Снятие
brelock_senser_off_click = '//*[.="Снятие"]//label/span'
brelock_senser_off_status = '//*[.="Снятие"]//label/input'
# Взятие
brelock_senser_take_click = '//*[.="Взятие"]//label/span'
brelock_senser_take_status = '//*[.="Взятие"]//label/input'
# Отключить сирену
brelock_senser_off_sirena_click = '//*[.="Отключить сирену"]//label/span'
brelock_senser_off_sirena_status = '//*[.="Отключить сирену"]//label/input'

# ------------ВЫПАДАЮЩИЕ СПИСКИ------------
# Название
brelok_DL_user = '(//*[@id="modalSettings"]//span[@class="label"])[1]'
# Раздел
brelok_DL_path = '(//*[@id="modalSettings"]//span[@class="label"])[2]'
# Способ вызова тихой тревоги
brelok_DL_silent_alarm_method = '(//*[@id="modalSettings"]//span[@class="label"])[3]'
# Группа выходов кнопки 1
brelok_DL_button_output_group_1 = '(//*[@id="modalSettings"]//span[@class="label"])[4]'
# Группа выходов кнопки 2
brelok_DL_button_output_group_2 = '(//*[@id="modalSettings"]//span[@class="label"])[5]'

# Кнопка выпадающего списка Управляемые разделы
brelok_controlled_sections = '(/html/body//div[@class="b-multiselect-label"])[1]'
positions_check_box = '(/html/body//div[@class="b-multiselect-items"]//label[@class="checkbox"])'
status_drop_list_check_box = '(//*[@class="b-multiselect-items-wrapper scrollable"]//label/input)'

"""С2000р-ИК"""
# ------------ЧЕКБОКСЫ-------------
# Включение датчика
c_2000p_senser_on_click = '//*[.="Включение датчика"]//label/span'
c_2000p_senser_on_status = '//*[.="Включение датчика"]//label/input'
# Режим "Колокольчик"
c_2000p_bell_mode_click = '//*[.=\'Режим "Колокольчик"\']//label/span'
c_2000p_bell_mode_status = '//*[.=\'Режим "Колокольчик"\']//label/input'
# Режим Энергосберегающий режим
c_2000p_energy_saving_mode_click = '//*[.="Энергосберегающий режим"]//label/span'
c_2000p_energy_saving_mode_status = '//*[.="Энергосберегающий режим"]//label/input'
# Режим тестирования
c_2000p_power_mode_click = '//*[.="Режим тестирования"]//label/span'
c_2000p_power_mode_status = '//*[.="Режим тестирования"]//label/input'
# ------------ВЫПАДАЮЩИЕ СПИСКИ------------
# Раздел
c_2000p_DL_path = '(//*[@id="modalSettings"]//span[@class="label"])[1]'
# Режим индикации
c_2000p_DL_indication_mod = '(//*[@id="modalSettings"]//span[@class="label"])[2]'
# ------------ВИДЖЕТ ПОЛЗУНОК-----------
c_2000p_widget_sensitivity = '(//*[.="Чувствительность"]/following::input[1])[1]'

"""С2000р-СМК"""
# ------------ЧЕКБОКСЫ-------------
# Включение режима "Антисаботаж"
c_2000p_smk_enabling_the_anti_sabotage_click = '//*[.=\'Включение режима "Антисаботаж"\']//label/span'
c_2000p_smk_enabling_the_anti_sabotage_status = '//*[.=\'Включение режима "Антисаботаж"\']//label/input'
# ------------ВЫПАДАЮЩИЕ СПИСКИ------------
# Включаемые модули
c_2000p_DL_included_modules = '(//*[@id="modalSettings"]//span[@class="label"])[3]'

"""КЦ"""
# ------------ВЫПАДАЮЩИЕ СПИСКИ------------
# Включаемые модули
kc_DL_type_zone = '(//*[@id="modalSettings"]//span[@class="label"])[1]'
# Раздел
kc_DL_path = '(//*[@id="modalSettings"]//span[@class="label"])[2]'

"""С2000р-СДВИГ"""
# ------------ЧЕКБОКСЫ-------------
# Контроль сдвига
c_2000p_sdvig_shear_control_click = '//*[.="Контроль сдвига"]//label/span'
c_2000p_sdvig_shear_control_status = '//*[.="Контроль сдвига"]//label/input'
# Контроль наклона
c_2000p_sdvig_tilt_control_click = '//*[.="Контроль наклона"]//label/span'
c_2000p_sdvig_tilt_control_status = '//*[.="Контроль наклона"]//label/input'
# Фиксирование датчика наклона
c_2000p_sdvig_fixing_the_tilt_sensor_click = '//*[.="Фиксирование датчика наклона"]//label/span'
c_2000p_sdvig_fixing_the_tilt_sensor_status = '//*[.="Фиксирование датчика наклона"]//label/input'
# Энергосберегающий режим
c_2000p_sdvig_energy_saving_mode_click = '//*[.="Энергосберегающий режим"]//label/span'
c_2000p_sdvig_energy_saving_mode_status = '//*[.="Энергосберегающий режим"]//label/input'
# Зафиксировать текущее положение
c_2000p_sdvig_lock_current_position_click = '//*[.="Зафиксировать текущее положение"]//label/span'
c_2000p_sdvig_lock_current_position_status = '//*[.="Зафиксировать текущее положение"]//label/input'
# Контроль геркона
c_2000p_sdvig_reed_switch_control_click = '//*[.="Контроль геркона"]//label/span'
c_2000p_sdvig_reed_switch_control_status = '//*[.="Контроль геркона"]//label/input'
# ------------ВЫПАДАЮЩИЕ СПИСКИ------------
# Порог тревоги по наклону
c_2000p_sdvig_DL_tilt_alarm_threshold = '(//*[@id="modalSettings"]//span[@class="label"])[3]'
# Порог тревоги по перемещению
c_2000p_sdvig_DL_movement_alarm_threshold = '(//*[@id="modalSettings"]//span[@class="label"])[4]'

"""С2000р-ИП"""
# ------------ЧЕКБОКСЫ-------------
# Вскрытие корпуса
c_2000p_ip_senser_open_click = '//*[.="Вскрытие корпуса"]//label/span'
c_2000p_ip_senser_open_status = '//*[.="Вскрытие корпуса"]//label/input'
# ------------ВЫПАДАЮЩИЕ СПИСКИ------------
# Режим уведомлений
c_2000p_DL_notification_mod = '(//*[@id="modalSettings"]//span[@class="label"])[3]'
# ------------ПОЛЯ ВВОДА------------
c_2000p_ip_gisteresis = '//*[.="Гистерезис"]//input'
c_2000p_ip_temp_min = '//*[.="Верхний порог по температуре"]//input'
c_2000p_ip_temp_max = '//*[.="Нижний порог по температуре"]//input'
