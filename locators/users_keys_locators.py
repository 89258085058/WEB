# -*- coding: utf-8 -*-
"""ПОЛЬЗОВАТЕЛИ И КЛЮЧИ"""
# ------------Текст на странице------------
data_users_and_keys_modal_text = '//div[@class="modal card"]'

# Выпадающий спосок - опция
positions = '(/html/body//div[@class="option"])'
# Выпадающий спосок - опция
positions_check_box = '(/html/body//div[@class="b-multiselect-items"]//label[@class="checkbox"])'
status_drop_list_check_box = '(//*[@class="b-multiselect-items-wrapper scrollable"]//label/input)'

"""ПОЛЬЗОВАТЕЛИ"""
# ------------ПОЛЯ ВВОДА------------
# Поиск
Search = '//*[@id="app"]/main//div/input'
# Имя пользователя
name_user = '//*[.="Имя пользователя"]/following::input[1]'
# Логин
login_user = '//*[.="Логин"]/following::input[1]'
# Пароль
password = '//*[.="Пароль"]/following::input[1]'
# Подтвердите пароль
re_password = '//*[.="Повторите пароль"]/following::input[1]'
# Телефон (код)
phone_cod_add = '//*[.="Телефон"]//input[1]'
phone_cod = '//*[.="Телефон"]/following::input[1]'

# Телефон (номер)
phone_number_add = '//*[.="Телефон"]//input[2]'
phone_number = '//*[.="Телефон"]/following::input[2]'
# Пароль SMS
password_sms_user_add = '//*[.="Пароль SMS"]//input[1]'
password_sms_user = '//*[.="Пароль SMS"]/following::input[1]'
# Повторите пароль
re_password_sms_user = '//*[.="Повторите пароль SMS"]/following::input[1]'
# ------------ВЫПАДАЮЩИЙ СПИСОК-----
# Кнопка выпадающего списка Группа выходов с управлением звонком
Group_of_outputs_with_call_control = '/html/body//span[@class="label"]'
# Кнопка выпадающего списка Группа выходов с управлением по SMS
Group_of_outputs_controlled_by_SMS = '(/html/body//div[@class="b-multiselect-label"])[1]'
# Кнопка выпадающего списка Управляемые по SMS разделы
SMS_controlled_sections = '(/html/body//div[@class="b-multiselect-label"])[1]'
DL_SMS_controlled_sections = '(/html/body//div[@class="b-multiselect-label"])[2]'

"""Ключи"""
# список ключей
key_row = '//*[@id="app"]/main//div[@class="row-item"]'
# ------------ПОЛЯ ВВОДА------------
# Идентификатор
key_id = '//*[.="Идентификатор"]/following::input[1]'

# ------------Кнопки------------
# Добавить пользователя
add_user = '//*[@id="app"]//div[@class="control-container"]'
# Добавить ключ
add_key = '//*[@id="app"]//div[@class="control-container"]'
# Настройки пользователя
user_settings_button = '(//*[@id="app"]//button[@class="BTN-secondary block BTN-auto-icon"])[1]'
# Настройки ключа
key_settings_button = '(//*[@id="app"]//button[@class="BTN-secondary block BTN-auto-icon"])[1]'
# Отменить
Cancel_button = '(//*[.=" Отменить "])[last()]'
# кнопка очистить поле поиска
cross_close_button = '//*[@id="app"]/main//div[@class="reset-icon"]'
# кнопка сохранить
save_button_key = '//*[.="Сохранить"]/div'
save_text = '(//*[.="Сохранено."])[1]'
delete_button_key = '(//*[.="Удалить"])[1]'
delete_button_user = '(//*[.="Удалить"])[6]'
# Добавить пользователя
open_last_user = '(//*[@id="app"]//button//*[.="Настройки"])[last()]'

# ------------ЧЕКБОКСЫ-------------
# Администратор
Administrator_click = '(/html/body//label/span)[1]'
Administrator_status = '(/html/body//label/input)[1]'
# Режим Эгида3
Egida3_Mode_click = '(/html/body//label/span)[2]'
Egida3_Mode_status = '(/html/body//label/input)[2]'
# Перенаправление сообщений оператора
Operator_message_forwarding_click = '(/html/body//label/span)[3]'
Operator_message_forwarding_status = '(/html/body//label/input)[3]'
# Отправка вне трансляций
CB_Sending_out_of_broadcast = '(/html/body//label/span)[4]'
Sending_outside_broadcasts_status = '(/html/body//label/input)[4]'
# Разрешить снятие по SMS
Allow_take_off_by_SMS_click = '(/html/body//label/span)[5]'
Allow_take_off_by_SMS_status = '(/html/body//label/input)[5]'
# Разрешить взятие по SMS
Allow_take_by_SMS_click = '(/html/body//label/span)[6]'
Allow_take_by_SMS_status = '(/html/body//label/input)[6]'

# ------------ВЫПАДАЮЩИЙ СПИСОК-----
# Выбор опции
option_key = '(/html/body//div[@class="option"])'
# Кнопка выпадающего списка Разрешения
permissions_dropdown = '//*[.="Разрешения"]/following::span[1]'
# Кнопка выпадающего списка Разделы
path_key_dropdown = '(/html/body//div[@class="b-multiselect-label"])[1]'
# Кнопка выпадающего списка Пользователь
user_list_dropdown = '//*[.="Пользователь"]/following::span[1]'

# ------------ЭЛЕМЕНТЫ НА СТРТАНИЦЕ-----
# локатор описания ключа
key = '//*[@id="app"]//div[@class="main-info"]'
# локатор описания пользователя
user = '//*[@id="app"]//div[@class="main-info"]'
