#!/bin/bash

python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_validation_5 tests/VALIDATION/testAuthValidation.py
python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_validation_5 tests/VALIDATION/testSettingsValidation.py
python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_validation_5 tests/VALIDATION/testUsersKeysValidation.py
python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_validation_5 tests/VALIDATION/testZonePathValidation.py
python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_validation_5 tests/VALIDATION/testDirectionsValidation.py -k TestValidationDestinationMainChanel
python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_validation_5 tests/VALIDATION/testDirectionsValidation.py -k TestValidationDestinationRezerv1Chanel
python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_validation_5 tests/VALIDATION/testDirectionsValidation.py -k TestValidationDestinationRezerv2Chanel