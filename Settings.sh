#!/bin/bash


python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_settings tests/VALIDATION/testSettingsValidation.py
python3 -m pytest --device=remote --browser=selenoid --alluredir=allure_settings tests/SAVE/testSettingsSave.py