#!/bin/bash

python3 -m pytest --browser=selenoid --alluredir=allure_validation tests/VALIDATION/testAuthValidation.py
python3 -m pytest --browser=selenoid --alluredir=allure_validation tests/VALIDATION/testDirectionsValidation.py
python3 -m pytest --browser=selenoid --alluredir=allure_validation tests/VALIDATION/testSettingsValidation.py
python3 -m pytest --browser=selenoid --alluredir=allure_validation tests/VALIDATION/testUsersKeysValidation.py
python3 -m pytest --browser=selenoid --alluredir=allure_validation tests/VALIDATION/testZonePathValidation.py


