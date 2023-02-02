#!/bin/bash

python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_ui tests/UI/testAuthUI.py
python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_ui tests/UI/testNavigationsUI.py
python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_ui tests/UI/testSettingsUI.py
python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_ui tests/UI/testTooltipsUI.py
python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_ui tests/UI/testUsersKeysUI.py
python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_ui tests/UI/testZonePathUI.py
python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_ui tests/UI/testStatusUI.py
python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_ui tests/UI/testUpdate.py
python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_ui tests/UI/testDirectionsUI.py
