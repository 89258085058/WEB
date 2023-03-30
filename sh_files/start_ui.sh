#!/bin/bash

python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_ui tests/UI/test_auth_ui.py
python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_ui tests/UI/test_directions_ui.py
python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_ui tests/UI/test_navigations_ui.py
python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_ui tests/UI/test_settings_ui.py
python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_ui tests/UI/test_tooltips_ui.py
python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_ui tests/UI/test_users_keys_ui.py
python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_ui tests/UI/test_zone_path_ui.py
python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_ui tests/UI/test_status_ui.py
python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_ui tests/UI/test_update.py
python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_ui tests/UI/test_directions_ui.py
