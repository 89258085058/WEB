==============================

Документация к проекту тестирования SIGNAL-GSM!
==============================

.. toctree::
   :maxdepth: 4

   reference
   changes
   Переход на страницу проекта gitlab  <http://gitlab.bolid.ru/gorelov/signalgsmweb>

   reference
   changes
   Скачать проект zipfile <http://gitlab.bolid.ru/gorelov/signalgsmweb/-/archive/master/signalgsmweb-master.zip>

   reference
   changes
   Переход на сервер непрерывной интеграции TeamCity  <http://192.168.22.130:8112/viewType.html?buildTypeId=Signal_SeleniumTests>


.. glossary::
        Архитектура проекта:

            * data - директория для хранения сгенерированных данных
            * docs - директория c документацией к коду проекта
            * fixture - директория c ключевыми файлами архитектуры проекта
            * generator - директория c методом генерирования случайных тестовых данных
            * locators - директория в которой находятся локаторы элементов
            * pages - методы о работе с страницами приложения согласно Page object
            * tests - автотесты
            * фаил "conftest.py" - основные настройки фремворка
            * фаил "target.json" - данные приложения (адрес/авторизация)
            * фаил "requirements.txt" - зависимости проекта



CONFTEST.PY
==============================
.. code-block:: python

   Фикстура APP передается в качестве аргумента принудительно для запуска авто-теста

    @pytest.fixture
    def app(request):
        global fixture
        browser = request.config.getoption("--browser")
        web_config = load_config(request.config.getoption("--target"))["web"]
        logAndPas = load_config(request.config.getoption("--target"))["webadmin"]

        if fixture is None or not fixture.is_valid():
            fixture = Application(browser=browser, base_url=web_config["baseUrl"])
        fixture.session.ensure_login(username=logAndPas["username"], password=logAndPas["password"])
        return fixture

==============================

.. code-block:: python

   Фикстура STOP вызывается автоматически после каждого теста

    @pytest.fixture(scope="session", autouse=True)
    def stop(request):
        def fin():
            fixture.destroy()

        request.addfinalizer(fin)
        return fixture

==============================

.. code-block:: python

   Хук: pytest_runtest_makereport используется
   для получения скриншота приложения в период падения теста

    @pytest.hookimpl(hookwrapper=True)
    def pytest_runtest_makereport(item, call):
        result = yield
        report = result.get_result()
        if report.longrepr:
            logging.error('FAILED: %s', report.longrepr)
        else:
            logging.info('Did not fail...')
        if report.outcome == 'failed':
            with allure.step('Скриншот браузера при падении теста'):
                fixture.get_screen()
                logging.error('FAILED: %s', report.longrepr)
        elif report.outcome == 'skipped':
            logging.info('Skipped')
        else:
            logging.info('Passed')

==============================

APPLICATION.PY
==============================
.. code-block:: python

   Настройка браузеров и взаимодействие с классами помошниками

    class Application:

        def __init__(self, browser, base_url):
            browser == 'exapmle_browser':
                self.wd = webdriver.exapmle_browser()
            self.wd.implicitly_wait(10)
            self.wd.set_window_size(1920, 1080)
            self.exapmle_helper = exapmle_Helper(self)


==============================

.. code-block:: python

   Открытие домашней страницы

    def open_home_page(self):
        wd = self.wd
        if wd.current_url is not self.base_url:
            wd.get(self.base_url)


==============================

.. code-block:: python

    Скриншот для отчета Allure

     def get_screen(self):
         wd = self.wd
         allure.attach(wd.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)



==============================

.. code-block:: python

    Завершение сессии

     def destroy(self):
        wd = self.wd
        self.wd.quit()



==============================


METHOD.PY
==============================
.. code-block:: python

    Проверка перехода на нужную ручку

    def pageEndpoint(self, host: str, endpoint: str, locator: str):
        wd = self.app.wd
        if wd.current_url == host + endpoint:
            pass
        else:
            self.click((By.XPATH, locator))
            time.sleep(0.1)
            assert str(wd.current_url) == str(host + endpoint), f" \nОшибка перехода на сраницу! " \
                                                                f"\nОжидаемый адрес:'{host + endpoint}'" \
                                                                f"\nФактический адрес:'{wd.current_url}'"
.. code-block:: python

    Метод проверки ввода вывода

    def verification_value_xpath(self, input_value, assert_value, locator):
        self.Input_values_xpath(input_value, locator)
        self.Assert_values_xpath(assert_value, locator)

.. code-block:: python

    Ввод значений в поле

    def Input_values(self, value, locator):
        try:
            wd = self.app.wd
            element = WebDriverWait(wd, 10).until(
                EC.element_to_be_clickable((By.ID, ('%s' % locator))))
            element.clear()
            element.send_keys(value)
        except Exception as e:
            assert e == TimeoutException, f"Ошибка локатор поля ввода '{locator}' - не найден"

.. code-block:: python

    Ввод значений в поле xpath

    def Input_values_xpath(self, value, locator):
        try:
            wd = self.app.wd
            element = WebDriverWait(wd, 10).until(
                EC.element_to_be_clickable((By.XPATH, ('%s' % locator))))
            element.clear()
            element.send_keys(value)
            # element.click()
        except Exception as e:
            assert e == TimeoutException, f"Ошибка локатор поля ввода '{locator}' - не найден"

.. code-block:: python

    Проверка введенных значений в поле xpath

    def Assert_values_xpath(self, value, locator):
        try:
            wd = self.app.wd
            element = WebDriverWait(wd, 10).until(
                EC.element_to_be_clickable((By.XPATH, ('%s' % locator))))
            values = element.get_attribute('value')
            assert str(value) == str(
                values), f"Ожидаемый результат ввода = '{value}' Фактическое значение в поле = '{values}'"
        except TimeoutException:
            print(f"Ошибка при проверке локатор поля ввода '{locator}' - не найден")

.. code-block:: python

    Получить текст

    def get_text(self, locator):
        wd = self.app.wd
        return WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.XPATH, ('%s' % locator)))).text

.. code-block:: python

    Проверить текст на странице

    def assert_text_on_page(self, locator, list_text):
        info_element = self.get_text(locator)
        for x in list_text:
            assert x in info_element, \
                f"\n----------------------\n" \
                f"Ошибка!\nОжидаемый текст: ***{x}*** - отсутствует на странице!\n" \
                f"\n----------------------\n" \
                f"Фактический текст на странице:\n{info_element}" \
                f"\n----------------------"

.. code-block:: python

    Проверить отсутствие текста на странице

    def assert_not_text_on_page(self, locator, list_text):
        info_element = self.get_text(locator)
        for x in list_text:
            assert x not in info_element, \
                f"\n----------------------\n" \
                f"Ошибка!\nОжидаемый текст: ***{x}*** - отсутствует на странице!\n" \
                f"\n----------------------\n" \
                f"Фактический текст на странице:\n{info_element}" \
                f"\n----------------------"

.. code-block:: python

    Клик по элементу

    def click(self, locator):
        try:
            wd = self.app.wd
            element = WebDriverWait(wd, 10).until(
                EC.element_to_be_clickable((locator)))
            element.click()
        except Exception as e:
            assert e == TimeoutException, f"Ошибка! Нет возможности кликнуть по локатору: '{locator}'"

.. code-block:: python

    Выбор чекбокса

    def check_box(self, position, click, status):
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

.. code-block:: python

    Проверка выбора чекбокса

    def assert_check_box(self, position, status):
        try:
            wd = self.app.wd
            selected = wd.find_element(By.XPATH, status)
            if position == "ON":
                status_check_box = True
            if position == "OFF":
                status_check_box = False
            assert status_check_box == selected.is_selected(),
             f"Ошибка! несоответствия статуса чекбокса, фактический статус: {selected.is_selected()}"
        except Exception as exc:
            assert exc == TimeoutException, f"Ошибка! локатор чекбокса: '{status}' не найден"

.. code-block:: python

    Проверка статуса кнопки

    def status_button(self, locator):
        wd = self.app.wd
        selected = wd.find_element(By.XPATH, locator)
        return selected.get_attribute('disabled')

.. code-block:: python

    Выбор из выпадающего списка

    def Select_from_the_dropdown_list(self, button, position):
        try:
            self.app.method.click((By.XPATH, button))
            self.app.method.click((By.XPATH, position))
        except TimeoutException as exc:
            assert exc == TimeoutException, f"Ошибка!!! Локатор выпадающего списка не найден"

.. code-block:: python

    Проверка значения в выпадающем списке

    def assert_Selection_from_the_dropdown_list(self, values, identifier):
        try:
            wd = self.app.wd
            element = wd.find_element(By.XPATH, identifier).get_property("textContent")
            assert str(element) == str(values), f"Ожидаемое значение='{values}', Фактическое '{element}'"
        except TimeoutException as exc:
            assert exc == TimeoutException, f"Ошибка локатор выпадающего списка '{identifier}' - не найден"

.. code-block:: python

    Виджет ползунок

    def slider_widget(self, volum, identifier):
        try:
            wd = self.app.wd
            slider = wd.find_element(By.XPATH, identifier)
            wd.execute_script("arguments[0].value = arguments[1]", slider, "%s" % volum)
        except Exception as exc:
            assert exc == TimeoutException, f"Ошибка локатор виджета {identifier} ползунка не найден"

.. code-block:: python

    Проверка виджета ползунка ID

    def assert_slider_widget(self, volum, identifier):
        wd = self.app.wd
        element = wd.find_element(By.XPATH, identifier).get_property("value")
        assert int(element) == int(
            volum), f"\n***Неверное положение виджета ползунка!***\nОжидаемое:'{volum}'\nФактическое:'{element}'"

.. code-block:: python

    Проверка текста всплывающей подсказки

    def assert_tooltip_text(self, text, locator):
        actual_text = self.get_text(locator)
        assert str(text) == str(actual_text),
           f"\nОшибка при проверке всплывающей подсказки!\nОжидаемый текст:
            '{text}' Фактический текст: '{actual_text}'"

==============================








