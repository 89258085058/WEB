#!/bin/bash

python3 -m pytest --device=remote --browser=selenoid --alluredir=allure_zone_path_01 tests/SAVE/testZonePathSave.py
python3 -m pytest --device=remote --browser=selenoid --alluredir=allure_zone_path_01 tests/SAVE/testZonePathSave.py



