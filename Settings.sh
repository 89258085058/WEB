#!/bin/bash


python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_settings_01 tests/VALIDATION/testSettingsValidation.py
python3 -m pytest --device=remote --browser=selenoid --alluredir=allure_settings_01 tests/SAVE/testSettingsSave.py