#!/bin/bash

python3 -m pytest --device=remote --browser=selenoid --alluredir=allure_validation_1 tests/VALIDATION/testAuthValidation.py
python3 -m pytest --device=remote --browser=selenoid --alluredir=allure_validation_1 tests/VALIDATION/testDirectionsValidation.py
python3 -m pytest --device=remote --browser=selenoid --alluredir=allure_validation_1 tests/VALIDATION/testSettingsValidation.py
python3 -m pytest --device=remote --browser=selenoid --alluredir=allure_validation_1 tests/VALIDATION/testUsersKeysValidation.py
python3 -m pytest --device=remote --browser=selenoid --alluredir=allure_validation_1 tests/VALIDATION/testZonePathValidation.py


