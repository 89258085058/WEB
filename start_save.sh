#!/bin/bash

python3 -m pytest --device=remote --browser=selenoid --alluredir=allure_save_3 tests/SAVE/testSettingsSave.py
python3 -m pytest --device=remote --browser=selenoid --alluredir=allure_save_3 tests/SAVE/testUsersKeysSave.py
python3 -m pytest --device=remote --browser=selenoid --alluredir=allure_save_3 tests/SAVE/testZonePathSave.py
python3 -m pytest --device=remote --browser=selenoid --alluredir=allure_save_3 tests/SAVE/testDirectionsSave.py -k TestSaveDestinationTumblers
python3 -m pytest --device=remote --browser=selenoid --alluredir=allure_save_3 tests/SAVE/testDirectionsSave.py -k TestSaveDestinationChanels


