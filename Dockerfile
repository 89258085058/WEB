FROM python:3.8
COPY . .
RUN pip install --proxy http://gorelov:911@proxy.bolid.ru:3128 -r requirements.txt
#CMD python -m pytest tests/
CMD python -m pytest --alluredir=allure_reports_docker/ --browser=chrome_100 tests/test_users_keys.py -k test_user_input_search_user








