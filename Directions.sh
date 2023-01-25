#!/bin/bash

python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_directions_01 tests/VALIDATION/testDirectionsValidation.py -k TestValidationDestinationMainChanel
python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_directions_01 tests/VALIDATION/testDirectionsValidation.py -k TestValidationDestinationRezerv1Chanel
python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_directions_01 tests/VALIDATION/testDirectionsValidation.py -k TestValidationDestinationRezerv2Chanel
python3 -m pytest --device=remote --browser=selenoid --alluredir=allure_directions_01 tests/SAVE/testDirectionsSave.py -k TestSaveDestinationTumblers
python3 -m pytest --device=remote --browser=selenoid --alluredir=allure_directions_01 tests/SAVE/testDirectionsSave.py -k TestSaveDestinationChanels
