#!/bin/bash

python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_users tests/VALIDATION/testUsersKeysValidation.py -k test_input_keys_id_settings
#python3 -m pytest --device=remote --browser=selenoid --alluredir=allure_users tests/SAVE/testUsersKeysSave.py