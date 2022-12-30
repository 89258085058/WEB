# -*- coding: utf-8 -*-
import time

import allure
from selenium.webdriver.common.by import By

from locators.navigations_locators import *


class NavigationsHelper:

    def __init__(self, app):
        self.app = app

    def goToZonePathPage(self):
        self.app.method.pageEndpoint(self.app.base_url_for_check, f'/zones-and-parts/partitions', ZonePathButton)

    def goToSettingsPage(self):
        self.app.method.pageEndpoint(self.app.base_url_for_check, f'/device-settings/object', SettingsButton)

    def goToUsersKeysPage(self):
        self.app.method.pageEndpoint(self.app.base_url_for_check, f'/users-and-keys/users', UsersKeysButton)

    def goToDirectionsPage(self):
        self.app.method.pageEndpoint(self.app.base_url_for_check, f'/destinations', DirectionsButton)

    def goToStatusPage(self):
        self.app.method.pageEndpoint(self.app.base_url_for_check, f'/status', StatusButton)

    def goToUpdatePage(self):
        self.app.method.pageEndpoint(self.app.base_url_for_check, f'/update', UpdateButton)

    def goToJournalPage(self):
        self.app.method.pageEndpoint(self.app.base_url_for_check, f'/journal', JournalButton)

    def goToObjectPage(self):
        self.app.method.pageEndpoint(self.app.base_url_for_check, f'/device-settings/object', ObjectButton)

    def goToDateTimePage(self):
        self.app.method.pageEndpoint(self.app.base_url_for_check, f'/device-settings/date-time', DateTimeButton)

    def goToDevicePage(self):
        self.app.method.pageEndpoint(self.app.base_url_for_check, f'/device-settings/device', DeviceButton)

    def goToLightIndicationPage(self):
        self.app.method.pageEndpoint(self.app.base_url_for_check, f'/device-settings/led', LightIbdicationBautton)

    def goToVolumIndicationPage(self):
        self.app.method.pageEndpoint(self.app.base_url_for_check, f'/device-settings/beeper', VolumIndicationButton)

    def goToRadioPage(self):
        self.app.method.pageEndpoint(self.app.base_url_for_check, f'/device-settings/wirelles', RadioButton)

    def goToGSMPage(self):
        self.app.method.pageEndpoint(self.app.base_url_for_check, f'/device-settings/gsm', GSMButton)

    def goToEthernetPage(self):
        self.app.method.pageEndpoint(self.app.base_url_for_check, f'/device-settings/ethernet', EthernetButton)

    def goToUsersPage(self):
        self.app.method.pageEndpoint(self.app.base_url_for_check, f'/users-and-keys/users', UsersButton)

    def goToKeysPage(self):
        self.app.method.pageEndpoint(self.app.base_url_for_check, f'/users-and-keys/keys', KeysButton)

    def goToPathPage(self):
        self.app.method.pageEndpoint(self.app.base_url_for_check, f'/zones-and-parts/partitions', PathButton)

    def goToZonePathOuts(self):
        self.app.method.pageEndpoint(self.app.base_url_for_check, f'/zones-and-parts/outs', ZonePathOutsButton)

    def goToZonePathSensorsZone(self):
        self.app.method.pageEndpoint(self.app.base_url_for_check, f'/zones-and-parts/sensors-and-zones',
                                     ZonePathSensorsZoneButton)

    def goToZonePathRelaySiren(self):
        self.app.method.pageEndpoint(self.app.base_url_for_check, f'/zones-and-parts/sirens', ZonePathRelaySirensButton)

    def goToZonePathKeyring(self):
        self.app.method.pageEndpoint(self.app.base_url_for_check, f'/zones-and-parts/keychains', ZonePathKeyringButton)

    def assert_main_page_journal(self):
        wd = self.app.wd
        time.sleep(1)
        assert str(wd.current_url) == str(
            self.app.base_url_for_check + f'/journal'), f" \n***Ошибка перехода на сраницу! " \
                                                        f"Ожидаемый эндпоинт:{str(self.app.base_url + '/journal')}" \
                                                        f" фактический адрес:'{wd.current_url}'***"

    def ExitAndEnter(self):
        self.app.session.logout()
        self.app.session.login_enter("admin", "admin")

    def ExitAndEnter_no_admin(self):
        self.app.session.logout()
        self.app.session.login_enter("test", "test")

    def edit_button_click(self):
        with allure.step("Клик по кнопке Редактировать"):
            try:
                time.sleep(0.3)
                self.app.method.click((By.XPATH, '//*[@id="app"]//button[.=" Редактировать "]'))
                time.sleep(0.1)
            except:
                time.sleep(0.3)
                self.reset_button_click()
                time.sleep(0.1)
                self.app.method.click((By.XPATH, '//*[@id="app"]//button[.=" Редактировать "]'))
                time.sleep(0.1)

    def reset_button_click(self):
        with allure.step("Клик по кнопке Редактировать"):
            time.sleep(0.1)
            self.app.method.click((By.XPATH, '//*[@id="app"]//button[.=" Сбросить "]'))
            time.sleep(0.1)
