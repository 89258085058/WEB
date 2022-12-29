#!/bin/bash

python3 -m pytest --device=remote --browser=selenoid --alluredir=allure_save_2 tests/SAVE/testDirectionsSave.py
python3 -m pytest --device=remote --browser=selenoid --alluredir=allure_save_2 tests/SAVE/testSettingsSave.py
python3 -m pytest --device=remote --browser=selenoid --alluredir=allure_save_2 tests/SAVE/testUsersKeysSave.py
python3 -m pytest --device=remote --browser=selenoid --alluredir=allure_save_2 tests/SAVE/testZonePathSave.py


