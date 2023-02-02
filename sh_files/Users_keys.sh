#!/bin/bash

python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_users_02 tests/VALIDATION/testUsersKeysValidation.py
python3 -m pytest --device=remote --browser=selenoid --alluredir=allure_users_02 tests/SAVE/testUsersKeysSave.py