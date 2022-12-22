#!/bin/bash

python3 -m pytest --device=remote --browser=selenoid --alluredir=allure_ui tests/VALIDATION/testAuthValidation.py
python3 -m pytest --device=remote --browser=selenoid --alluredir=allure_ui tests/VALIDATION/testDirectionsValidation.py
python3 -m pytest --device=remote --browser=selenoid --alluredir=allure_ui tests/VALIDATION/testSettingsValidation.py
python3 -m pytest --device=remote --browser=selenoid --alluredir=allure_ui tests/VALIDATION/testUsersKeysValidation.py
python3 -m pytest --device=remote --browser=selenoid --alluredir=allure_ui tests/VALIDATION/testZonePathValidation.py


