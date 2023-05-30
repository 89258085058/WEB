# -*- coding: utf-8 -*-

import allure
import pytest

reruns = 1


@pytest.fixture
def update_page(app):
    with allure.step("Переход на страницу Обновления"):
        app.PO_Navigations.goToUpdatePage()


@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты ОБНОВЛЕНИЯ")
@allure.feature("Проверки UI")
@pytest.mark.flaky(reruns=reruns)
class TestUpdateUI:

    @allure.story("Проверка отображения текста и элементов на странице")
    def test_display_items_update(self, app, update_page):
        app.PO_Update.display_items_update()
