# -*- coding: utf-8 -*-
import json
import logging
import os.path

import pytest

from fixture.application import Application

fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


@pytest.fixture(scope="session")
def config(request):
    return load_config(request.config.getoption("--target"))


@pytest.fixture(scope='class')
def app(request):
    global fixture

    if request.config.getoption("--device") == 'remote':
        browser = request.config.getoption("--browser")
        web_config = load_config(request.config.getoption("--target"))["web_remote"]
        logAndPas = load_config(request.config.getoption("--target"))["webadmin"]

        fixture = Application(browser=browser, base_url=web_config["baseUrl_remote"],
                              base_url_for_check=web_config["baseUrl_remote_signal"])
        fixture.session.ensure_login_remote(username=logAndPas["username"], password=logAndPas["password"])
        return fixture

    if request.config.getoption("--device") == 'local':
        browser = request.config.getoption("--browser")
        web_config = load_config(request.config.getoption("--target"))["web"]
        logAndPas = load_config(request.config.getoption("--target"))["webadmin"]
        if fixture is None or not fixture.is_valid():
            fixture = Application(browser=browser, base_url=web_config["baseUrl"],
                                  base_url_for_check=web_config["baseUrl"])
        fixture.session.ensure_login(username=logAndPas["username"], password=logAndPas["password"])
        return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.destroy()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    # parser.addoption("--browser", action='store', default="selenoid")
    parser.addoption("--browser", action='store', default="chrome")
    # parser.addoption("--browser", action='store', default="Firefox")
    parser.addoption("--target", action='store', default="target.json")
    parser.addoption("--device", action='store', default="local")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    result = yield
    report = result.get_result()
    if report.longrepr:
        logging.error('FAILED: %s', report.longrepr)
    else:
        logging.info('Did not fail...')
    if report.outcome == 'failed':
        fixture.get_screen()
        logging.error('FAILED: %s', report.longrepr)
        # with allure.step('Скриншот браузера при падении теста'):
        #     fixture.get_screen()
        #     logging.error('FAILED: %s', report.longrepr)
    elif report.outcome == 'skipped':
        logging.info('Skipped')
    else:
        logging.info('Passed')
