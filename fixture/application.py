# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as CHROME
from selenium.webdriver.firefox.options import Options as FIREFOX

from fixture.attach import Attachments
from fixture.method import MethodsHelper
from fixture.session import SessionHelper
from generator.generate_data import Ganerate
from generator.read_data import DataHelper
from pages.PO_Auth import AuthHelper
from pages.PO_Directions import DirectionsHelper
from pages.PO_Journal import JournalHelper
from pages.PO_Navigations import NavigationsHelper
from pages.PO_Sensors import SensorsHelper
from pages.PO_Settings import SettingsHelper
from pages.PO_Status import StatusHelper
from pages.PO_Tooltips import TooltipsHelper
from pages.PO_Update import UpdateHelper
from pages.PO_Users_Keys import UsersKeysHelper
from pages.PO_Zone_Path import ZonePathHelper
from api.endpoint import EndpointHelper


class Application:

    # Настройка браузеров и взаимодействие с классами помошниками
    def __init__(self, browser, base_url, base_url_for_check):
        if browser == 'firefox':
            self.wd = webdriver.Firefox()
        elif browser == 'chrome':
            self.wd = webdriver.Chrome()
        elif browser == 'chrome_headless':
            options = CHROME()
            options.headless = True
            self.wd = webdriver.Chrome(options=options)
        elif browser == 'chrome_no_logs':
            options = CHROME()
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            self.wd = webdriver.Chrome(options=options)
        elif browser == 'firefox_headless':
            options = FIREFOX()
            options.headless = True
            self.wd = webdriver.Firefox(options=options)
        elif browser == 'chrome_latest':
            capabilities = {"browserName": 'chrome', "browserVersion": "105.0", "platformName": "Linux"}
            self.wd = webdriver.Remote(command_executor=f"http://192.168.22.130:4444/wd/hub",
                                       desired_capabilities=capabilities)
        elif browser == 'selenoid':
            capabilities = {
                "browserName": "chrome",
                "browserVersion": "108.0",
                "selenoid:options": {
                    "enableVNC": True,
                    "enableVideo": False
                }
            }
            self.wd = webdriver.Remote(
                command_executor="http://134.0.115.66:4444/wd/hub",
                desired_capabilities=capabilities,
            )
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.set_window_size(1920, 1080)
        self.wd.implicitly_wait(5)
        self.PO_Auth = AuthHelper(self)
        self.PO_Directions = DirectionsHelper(self)
        self.PO_Journal = JournalHelper(self)
        self.PO_Navigations = NavigationsHelper(self)
        self.PO_Settings = SettingsHelper(self)
        self.PO_Users_Keys = UsersKeysHelper(self)
        self.PO_Zone_Path = ZonePathHelper(self)
        self.PO_Tooltips = TooltipsHelper(self)
        self.PO_Sensors = SensorsHelper(self)
        self.PO_Status = StatusHelper(self)
        self.PO_Update = UpdateHelper(self)
        self.endpoint = EndpointHelper(self)
        self.method = MethodsHelper(self)
        self.session = SessionHelper(self)
        self.read_data = DataHelper(self)
        self.ganerate_data = Ganerate(self)
        self.attach = Attachments(self)
        self.base_url = base_url
        self.base_url_for_check = base_url_for_check

    # Проверка на валидный URL
    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    # Открытие домашней страницы
    def open_home_page(self):
        wd = self.wd
        if wd.current_url is not self.base_url:
            wd.get(self.base_url)

    # Выход из браузера
    def destroy(self):
        self.wd.quit()

    # Выполнение скриншота для отчета Allure
    def get_attach(self):
        self.attach.add_screenshot()

    # # Выполнение скриншота для отчета Allure c скролом в самый низ
    # def get_attach(self):
    #     wd = self.wd
    #     target = wd.find_element(By.XPATH, '//*[@id="modalSettings"]/div/div[2]/div[2]/button[1]')
    #     actions = ActionChains(wd)
    #     actions.move_to_element(target)
    #     actions.perform()
    #     allure.attach(wd.get_screenshot_as_png(), name="↓ СКРИНШОТ ↓", attachment_type=AttachmentType.PNG)
