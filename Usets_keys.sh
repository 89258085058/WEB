#!/bin/bash

python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_users_keys tests/VALIDATION/testUsersKeysValidation.py
python3 -m pytest --device=remote --browser=selenoid --alluredir=allure_users_keys tests/SAVE/testUsersKeysSave.py