#!/bin/bash

python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_ui_6 tests/UI/testAuthUI.py
python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_ui_6 tests/UI/testNavigationsUI.py
python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_ui_6 tests/UI/testSettingsUI.py
python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_ui_6 tests/UI/testTooltipsUI.py
python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_ui_6 tests/UI/testUsersKeysUI.py
python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_ui_6 tests/UI/testZonePathUI.py
python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_ui_6 tests/UI/testStatusUI.py
python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_ui_6 tests/UI/testUpdate.py
python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_ui_6 tests/UI/testDirectionsUI.py -k TestUIDestinationMainChanel
python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_ui_6 tests/UI/testDirectionsUI.py -k TestUIDestinationRezerv1Chanel
python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_ui_6 tests/UI/testDirectionsUI.py -k TestUIDestinationRezerv2Chanel