#!/bin/bash

python3 -m pytest --device=remote --browser=selenoid --alluredir=allure_zone_path tests/SAVE/testZonePathSave.py
python3 -m pytest --device=remote --browser=selenoid --alluredir=allure_zone_path tests/SAVE/testZonePathSave.py



