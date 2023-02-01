#!/bin/bash


python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_settings_02 tests/VALIDATION/testSettingsValidation.py -k test_input_data_name_object
