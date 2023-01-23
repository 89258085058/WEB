#!/bin/bash

python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_users tests/VALIDATION/testUsersKeysValidation.py
python3 -m pytest --device=remote --browser=selenoid --alluredir=allure_users tests/SAVE/testUsersKeysSave.py