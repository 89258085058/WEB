#!/bin/bash


python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_test tests/VALIDATION/testSettingsValidation.py -k test_input_data_name_object
python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_test tests/VALIDATION/testSettingsValidation.py -k test_input_data_name_object_negativ
python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_test tests/VALIDATION/testSettingsValidation.py -k test_input_data_number_object
