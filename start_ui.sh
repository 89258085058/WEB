#!/bin/bash

python3 -m pytest --device=remote --browser=selenoid --alluredir=allure_ui_1 tests/UI/testAuthUI.py
python3 -m pytest --device=remote --browser=selenoid --alluredir=allure_ui_1 tests/UI/testDirectionsUI.py
python3 -m pytest --device=remote --browser=selenoid --alluredir=allure_ui_1 tests/UI/testNavigationsUI.py
python3 -m pytest --device=remote --browser=selenoid --alluredir=allure_ui_1 tests/UI/testSettingsUI.py
python3 -m pytest --device=remote --browser=selenoid --alluredir=allure_ui_1 tests/UI/testStatusUI.py
python3 -m pytest --device=remote --browser=selenoid --alluredir=allure_ui_1 tests/UI/testTooltipsUI.py
python3 -m pytest --device=remote --browser=selenoid --alluredir=allure_ui_1 tests/UI/testUpdate.py
python3 -m pytest --device=remote --browser=selenoid --alluredir=allure_ui_1 tests/UI/testUsersKeysUI.py
python3 -m pytest --device=remote --browser=selenoid --alluredir=allure_ui_1 tests/UI/testZonePathUI.py



