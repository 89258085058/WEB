# -*- coding: utf-8 -*-
import time
from dataclasses import dataclass

from selenium.common.exceptions import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@dataclass
class MethodsHelper:
    app: any

    # Проверка перехода на нудную ручку
    def pageEndpoint(self, host: str, endpoint: str, locator: str):
        wd = self.app.wd
        if wd.current_url == host + endpoint:
            pass
        else:
            self.click((By.XPATH, locator))
            time.sleep(0.5)
            assert str(wd.current_url) == str(host + endpoint), f" \nОшибка перехода на сраницу! " \
                                                                f"\nОжидаемый адрес:'{host + endpoint}'" \
                                                                f"\nФактический адрес:'{wd.current_url}'"

    # Метод проверки ввода вывода
    def assertEqual(self, input, expected, locator):
        self.inputValues(input, locator)
        self.assertValues(expected, locator)

    # Ввод значений в поле xpath
    def inputValues(self, value, locator):
        try:
            wd = self.app.wd
            element = WebDriverWait(wd, 10).until(
                EC.element_to_be_clickable((By.XPATH, ('%s' % locator))))
            element.clear()
            element.clear()
            element.send_keys(value)
        except Exception as e:
            assert e == TimeoutException, f"Ошибка локатор поля ввода '{locator}' - не найден"

    # Проверка введенных значений в поле xpath
    # def assertValues(self, value, locator):
    #     try:
    #         wd = self.app.wd
    #         element = WebDriverWait(wd, 10).until(
    #             EC.element_to_be_clickable((By.XPATH, ('%s' % locator))))
    #         values = element.get_attribute('value')
    #         # check.equal(str(values), str(value))
    #         assert str(value) == str(
    #             values), f"\nОжидаемый результат ввода = '{value}'\nФактическое значение в поле = '{values}'"
    #     except Exception as e:
    #         assert e == TimeoutException, f"Ошибка локатор поля ввода '{locator}' - не найден"


    # Проверка введенных значений в поле xpath
    def assertValues(self, value, locator):
        wd = self.app.wd
        element = WebDriverWait(wd, 10).until(
            EC.element_to_be_clickable((By.XPATH, ('%s' % locator))))
        values = element.get_attribute('value')
        assert str(value) == str(
            values), f"\nОжидаемый результат ввода = '{value}'\nФактическое значение в поле = '{values}'"

    # Проверка введенных значений в поле xpath
    def assertValuesPhoneNum(self, value, locator):
        try:
            wd = self.app.wd
            element = WebDriverWait(wd, 10).until(
                EC.element_to_be_clickable((By.XPATH, ('%s' % locator))))
            val = element.get_attribute('value')
            values = val.replace(' ', '')
            # check.equal(str(values), str(value))

            assert str(value) == str(
                values), f"\nОжидаемый результат ввода = '{value}'\nФактическое значение в поле = '{values}'"
        except Exception as e:
            assert e == TimeoutException, f"Ошибка локатор поля ввода '{locator}' - не найден"

    # Проверка значений на странице
    def assertValuesOnPage(self, value, locator):
        try:
            values = self.getText(locator)
            assert str(value) == str(
                values), f"\nОжидаемый результат ввода = '{value}'\nФактическое значение в поле = '{values}'"
        except Exception as e:
            assert e == TimeoutException, f"Ошибка локатор поля ввода '{locator}' - не найден"

    # Получить текст
    def getText(self, locator):
        wd = self.app.wd
        return WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.XPATH, ('%s' % locator)))).text

    # Проверить текст на странице
    def assertTextOnPage(self, locator, list_text):
        info_element = self.getText(locator)
        for x in list_text:
            assert x in info_element, \
                f"\n----------------------\n" \
                f"Ошибка!\nОжидаемый текст: ***{x}*** - отсутствует на странице!\n" \
                f"\n----------------------\n" \
                f"Фактический текст на странице:\n{info_element}" \
                f"\n----------------------"

    # Проверить отсутствие текста на странице
    def assertotMissingTextOnPage(self, locator, list_text):
        info_element = self.getText(locator)
        for x in list_text:
            assert x not in info_element, \
                f"\n----------------------\n" \
                f"Ошибка!\nОжидаемый текст: ***{x}*** - отсутствует на странице!\n" \
                f"\n----------------------\n" \
                f"Фактический текст на странице:\n{info_element}" \
                f"\n----------------------"

    # Клик по элементу
    def click(self, locator):
        try:
            wd = self.app.wd
            element = WebDriverWait(wd, 10).until(
                EC.element_to_be_clickable((locator)))
            element.click()
        except Exception as e:
            assert e == TimeoutException, f"Ошибка! Нет возможности кликнуть по локатору: '{locator}'"

    # Клик по элементу
    def click_element_locate(self, locator):
        try:
            wd = self.app.wd
            time.sleep(0.3)
            element = wd.find_element(By.XPATH, locator)
            element.click()
        except Exception as e:
            assert e == TimeoutException, f"Ошибка! Нет возможности кликнуть по локатору: '{locator}'"

    # Получение длинны списка элементов
    def getElementsLen(self, locator):
        wd = self.app.wd
        return len(wd.find_elements(By.XPATH, locator))

    # Проверка статуса кнопок в выходах
    def status_outs_button(self, locator):
        wd = self.app.wd
        element = WebDriverWait(wd, 20).until(
            EC.element_to_be_clickable((locator)))
        class_button = element.get_property("className")
        assert str(
            class_button) == "BTN-primary-text content-left block active", f"Ошибка активации кнопки!\nФактический класс кнопки: '{class_button}'\nОжидаемый: 'BTN-primary-text content-left block active'"

    # Получение property
    def getProperty(self, locator):
        try:
            wd = self.app.wd
            element = WebDriverWait(wd, 10).until(
                EC.element_to_be_clickable((locator)))
            return element.get_property('checked')
        except Exception as e:
            assert e == TimeoutException, f"Ошибка! Нет возможности кликнуть по локатору: '{locator}'"

    # Выбор чекбокса
    def checkBox(self, position: str, click: str, status: str):
        try:
            wd = self.app.wd
            element = WebDriverWait(wd, 10).until(
                EC.element_to_be_clickable((By.XPATH, click)))
            selected = wd.find_element(By.XPATH, status)
            if position == "ON":
                if selected.is_selected() == True:
                    pass
                else:
                    element.click()
            elif position == "OFF":
                if selected.is_selected() == False:
                    pass
                else:
                    element.click()
        except Exception as exc:
            assert exc == TimeoutException, f"Ошибка! локатор чекбокса: '{click}' не найден"

    # Проверка выбора чекбокса
    def assertCheckBox(self, position: str, status: str):
        wd = self.app.wd
        selected = wd.find_element(By.XPATH, status)
        if position == "ON":
            status_check_box = True
        if position == "OFF":
            status_check_box = False
        if selected.is_selected() == False:
            result = 'Не включается'
        if selected.is_selected() == True:
            result = 'Не выключается'
        assert status_check_box == selected.is_selected(), f"Ошибка! Чекбокс: {result}"

    def attributeStatusButton(self, locator):
        wd = self.app.wd
        selected = wd.find_element(By.XPATH, locator)
        return selected.get_attribute('disabled')

    # Выбор из выпадающего списка
    def selectDropdownList(self, button, position):
        try:
            self.app.method.click((By.XPATH, button))
            self.app.method.click((By.XPATH, position))
        except TimeoutException as exc:
            assert exc == TimeoutException, f"Ошибка!!! Локатор выпадающего списка не найден"

    # Выбор из выпадающего списка с чекбоксом
    def selectDropdownListCheckBox(self, button, position, status):
        try:
            wd = self.app.wd
            try:
                time.sleep(0.2)
                self.app.method.click((By.XPATH, button))
                selected = wd.find_element(By.XPATH, status)
                if selected.is_selected() == False:
                    self.app.method.click((By.XPATH, position))
            except TimeoutException as exc:
                assert exc == TimeoutException, f"Ошибка!!! Локатор выпадающего списка не найден"
            except:
                time.sleep(0.2)
            self.app.method.click((By.XPATH, button))
            selected = wd.find_element(By.XPATH, status)
            if selected.is_selected() == False:
                self.app.method.click((By.XPATH, position))
        except TimeoutException as exc:
            assert exc == TimeoutException, f"Ошибка!!! Локатор выпадающего списка не найден"

    # Выбор из выпадающего списка с чекбоксом
    def selectDropdownListCheckBoxByName(self, button, name):
        try:
            self.app.method.click((By.XPATH, button))
            self.app.method.click((By.XPATH, f'/html/body//span[.="{name}"]'))
        except TimeoutException as exc:
            assert exc == TimeoutException, f"Ошибка!!! Локатор выпадающего списка не найден"

    # Выбор из выпадающего списка для сохранения
    def selectDropdownListByName(self, button, name):
        try:
            time.sleep(0.3)
            self.app.method.click((By.XPATH, button))
            time.sleep(0.3)
            self.app.method.click((By.XPATH, f'/html/body//div[@class="option"][.="{name}"]'))
            time.sleep(0.3)
        except TimeoutException as exc:
            assert exc == TimeoutException, f"Ошибка!!! Локатор выпадающего списка не найден"

    # Проверка значения в выпадающем списке
    def assertSelectionDropdownList(self, values, identifier):
        try:
            wd = self.app.wd
            element = wd.find_element(By.XPATH, identifier).get_property("textContent")
            assert str(element) == str(
                values), f"\nОжидаемое значение в выпадающем списке: '{values}'\nФактическое: '{element}'"
        except TimeoutException as exc:
            assert exc == TimeoutException, f"Ошибка локатор выпадающего списка '{identifier}' - не найден"

    # Проверка значения в выпадающем списке
    def assertSelectionDropdownListCheckBox(self, values, identifier):
        try:
            wd = self.app.wd
            element = wd.find_element(By.XPATH, identifier).get_property("outerText")
            assert str(values) in str(
                element), f"\nОжидаемое значение в выпадающем списке: '{values}'\nФактическое: '{element}'"
        except TimeoutException as exc:
            assert exc == TimeoutException, f"Ошибка локатор выпадающего списка '{identifier}' - не найден"

    # Виджет ползунок
    def sliderWidgetExit(self, volum, identifier):
        from selenium.webdriver import ActionChains, Keys
        wd = self.app.wd
        slider = wd.find_element(By.XPATH, identifier)
        actions = ActionChains(wd)
        actions.move_to_element(slider)
        actions.click(slider)
        for i in range(1000):
            actions.key_down(Keys.LEFT)
        for i in range(int(volum)):
            actions.key_down(Keys.RIGHT)
        actions.perform()

    # Виджет ползунок
    def sliderWidget(self, volum, identifier):
        from selenium.webdriver import ActionChains, Keys
        wd = self.app.wd
        slider = wd.find_element(By.XPATH, identifier)
        actions = ActionChains(wd)
        actions.move_to_element(slider)
        actions.click(slider)
        for i in range(1024):
            actions.key_down(Keys.LEFT)
        for i in range(int(volum)):
            actions.key_down(Keys.RIGHT)
        actions.perform()

        # Проверка виджета ползунка

    def assertSliderWidget(self, volum, identifier):
        wd = self.app.wd
        element = wd.find_element(By.XPATH, identifier).get_property("value")
        assert int(element) == int(
            volum), f"\n***Неверное положение виджета ползунка!***\nОжидаемое:'{volum}'\nФактическое:'{element}'"

    # Проверка текста всплывающей подсказки
    def assertTooltipText(self, text):
        locator = '//*[@class="b-tooltip-text"]'
        actual_text = self.getText(locator)
        assert str(text) == str(
            actual_text), f"\nОшибка при проверке всплывающей подсказки!\nОжидаемый текст: '{text}'\n\nФактический текст: '{actual_text}'"

    # Выбор из выпадающего списка по названию
    def Select_from_the_dropdown_list_by_name(self, button, position):
        try:
            self.app.method.click((By.XPATH, button))
            time.sleep(0.5)
            self.app.method.click((By.XPATH, f'/html/body//div[@class="option"][.="{position}"]'))
        except TimeoutException as exc:
            assert exc == TimeoutException, f"Ошибка!!! Локатор выпадающего списка не найден"

    # Ввод значений в поле xpath
    def elementFocus(self, locator):
        try:
            wd = self.app.wd
            element = WebDriverWait(wd, 10).until(
                EC.element_to_be_clickable((By.XPATH, ('%s' % locator))))
            action = ActionChains(wd)
            action.move_to_element(element).perform()
        except TimeoutException as exc:
            assert exc == TimeoutException, f"Ошибка!!! Локатор '{locator}' не найден"

    # Проверка выпадающего списка
    def check_dropdown_list(self, button: str, name: str):
        for x in name:
            self.app.method.selectDropdownListByName(button, x)
            self.app.method.assertSelectionDropdownList(x, button)

    # Проверка выпадающего списка с чек боксом
    def check_dropdown_list_with_check_box(self, button: str, name: str):
        try:
            wd = self.app.wd
            for x in name:
                self.close_cross(button)
                self.app.method.click((By.XPATH, f'/html/body//span[.="{x}"]'))
                self.app.method.click((By.XPATH, button))
                element = wd.find_element(By.XPATH, button).get_property("textContent")
                assert str(element) == str(
                    x), f"\nОжидаемое значение в выпадающем списке: '{x}'\nФактическое: '{element}'"
        except TimeoutException as exc:
            assert exc == TimeoutException, f"Ошибка выбора из выпадающего списка"

    def check_dropdown_list_with_check_box_double_click(self, button: str, name: str):
        try:
            wd = self.app.wd
            for x in name:
                self.close_cross(button)
                self.app.method.click((By.XPATH, f'/html/body//span[.="{x}"]'))
                self.app.method.click((By.XPATH, button))
                element = wd.find_element(By.XPATH, button).get_property("textContent")
                assert str(element) == str(
                    x), f"\nОжидаемое значение в выпадающем списке: '{x}'\nФактическое: '{element}'"
        except TimeoutException as exc:
            assert exc == TimeoutException, f"Ошибка выбора из выпадающего списка"

    # Сброс выпадающего списка при нажатии крестика
    def close_cross(self, locator):
        try:
            time.sleep(0.3)
            self.app.method.click((By.XPATH, locator))
            time.sleep(0.5)
            self.app.method.click((By.XPATH, f'(/html/body//*[@class="b-close-icon"])[1]'))
        except:
            time.sleep(0.3)
            self.app.method.click((By.XPATH, locator))
            time.sleep(0.5)
            self.app.method.click((By.XPATH, f'(/html/body//*[@class="b-close-icon"])[1]'))

    # Проверка черкбокса отображающего списком в поле
    def assert_drop_wown_list_with_check_box(self, button, main_CB, list):
        wd = self.app.wd
        self.app.method.close_cross(button)
        self.app.method.click((By.XPATH, main_CB))
        self.app.method.click((By.XPATH, button))
        element = wd.find_element(By.XPATH, button).get_property("textContent")
        for x in list:
            assert str(x) in str(element), f"\nОжидаемое значение в выпадающем списке: '{x}'\nФактическое: '{element}'"

    # Метод проверки позиции чекбокса
    def check_box_verification(self, position, click, status):
        self.checkBox(position, click, status)
        self.assertCheckBox(position, status)

    # Подсчет элементов
    def elements_count(self, locator):
        wd = self.app.wd
        return len(wd.find_elements(By.XPATH, locator))

    # Выбор из выпадающего списка без проверки
    def dropdown_select(self, button, name):
        self.app.method.click((By.XPATH, button))
        self.app.method.click((By.XPATH, f'/html/body//div[@class="option"][.="{name}"]'))

    # Выбор из выпадающего списка разделов
    def path_select(self, button, name):
        self.app.method.click((By.XPATH, button))
        self.app.method.click((By.XPATH, f'/html/body//div[@class="b-multiselect-item"]/span[.="{name}"]'))
        self.app.method.click((By.XPATH, button))

    # Выбор времени
    def TimeBox(self, position, time, chanel):
        wd = self.app.wd
        status = f'(// *[ @ id = "modalSettings"] // button[. = "{time}"])[{chanel}]'
        click_on = f'(//*[.="{time}"]/span)[{chanel}]'
        element = WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, click_on)))
        selected = wd.find_element(By.XPATH, status)
        if position == "ON":
            if selected.get_attribute("class") == 'BTN-primary-text block active':
                pass
            else:
                element.click()
        elif position == "OFF":
            if selected.get_attribute("class") == 'BTN-primary-text block':
                pass
            else:
                element.click()

    # Проверка выбора времени
    def assertTimeBox(self, position, time, chanel):
        wd = self.app.wd
        status = f'(// *[ @ id = "modalSettings"] // button[. = "{time}"])[{chanel}]'
        selected = wd.find_element(By.XPATH, status)
        if position == "ON":
            status_check_box = 'BTN-primary-text block active'
        if position == "OFF":
            status_check_box = 'BTN-primary-text block'
        if selected.get_attribute("class") == 'BTN-primary-text block':
            result = 'Не включается'
        if selected.get_attribute("class") == 'BTN-primary-text block active':
            result = 'Не выключается'
        assert status_check_box == selected.get_attribute("class"), f"Ошибка! Время: '{time}' - {result}"

    # Проверка присутствия элемента на странице
    def is_element_present(self, locator):
        wd = self.app.wd
        wd.implicitly_wait(0.1)
        try:
            wd.find_element(By.CSS_SELECTOR, locator)
        except NoSuchElementException:
            wd.implicitly_wait(5)
            return False
        wd.implicitly_wait(5)
        return True