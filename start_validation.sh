#!/bin/bash

python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure-results tests/VALIDATION/testAuthValidation.py
