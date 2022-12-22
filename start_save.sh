#!/bin/bash

python3 -m pytest --device=local --browser=selenoid --alluredir=allure_save tests/SAVE/testDirectionsSave.py
python3 -m pytest --device=local --browser=selenoid --alluredir=allure_save tests/SAVE/testSettingsSave.py
python3 -m pytest --device=local --browser=selenoid --alluredir=allure_save tests/SAVE/testUsersKeysSave.py
python3 -m pytest --device=local --browser=selenoid --alluredir=allure_save tests/SAVE/testZonePathSave.py



