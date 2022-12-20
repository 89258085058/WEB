#!/bin/bash

python3 -m pytest --browser=selenoid --alluredir=allure_validation tests/VALIDATION/testZonePathValidation.py
python3 -m pytest --browser=selenoid --alluredir=allure_validation tests/VALIDATION/testUsersKeysValidation.py
