#!/bin/bash

python3 -m pytest --browser=selenoid --alluredir=allure_validation tests/VALIDATION/testAuthValidation.py
python3 -m pytest --browser=selenoid --alluredir=allure_validation tests/VALIDATION/testUsersKeysValidation.py
