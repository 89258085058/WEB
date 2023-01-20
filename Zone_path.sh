#!/bin/bash

python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_validation_6 tests/VALIDATION/testZonePathValidation.py -k test_path_input_search
#python3 -m pytest --device=remote --browser=selenoid --alluredir=allure_zone_path tests/SAVE/testZonePathSave.py



