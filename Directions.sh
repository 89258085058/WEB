#!/bin/bash

python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_directions_02 tests/VALIDATION/testDirectionsValidation.py
python3 -m pytest --device=remote --browser=selenoid --alluredir=allure_directions_02 tests/SAVE/testDirectionsSave.py -k TestSaveDestinationTumblers
python3 -m pytest --device=remote --browser=selenoid --alluredir=allure_directions_02 tests/SAVE/testDirectionsSave.py -k TestSaveDestinationChanels
