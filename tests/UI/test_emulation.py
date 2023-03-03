# -*- coding: utf-8 -*-
import time

import allure
import pytest

reruns = 1


@pytest.fixture(scope='class')
def open_tab_sensors(app):
    with allure.step("Открытие вкладки 'Датчики/Зоны'"):
        app.PO_Navigations.goToZonePathPage()
        app.PO_Navigations.goToZonePathSensorsZone()
    yield
    with allure.step("Удаление добавленного датчика"):
        app.PO_Status.delete_fake_sensor()


@pytest.fixture()
def open_tab_status(app):
    with allure.step("Открытие вкладки 'Статус'"):
        app.PO_Navigations.goToStatusPage()


@pytest.fixture(scope='class')
def delete_fake_partition(app):
    yield
    with allure.step("Удаление добавленного раздела"):
        app.PO_Status.delete_fake_partition()


@pytest.fixture(scope='class')
def precondition_for_device(app):
    with allure.step("Добавление прибора и логаут"):
        app.PO_Status.add_fake_device()
    yield
    with allure.step("Удаление прибора"):
        app.PO_Status.delete_fake_device()


@allure.label("owner", 'Александр Санталов')
@allure.epic("Тесты эмуляция статусов")
@allure.feature("Проверки UI")
@pytest.mark.flaky(reruns=reruns)
class TestEmulation:

    @allure.story("Проверка статуса раздела")
    @pytest.mark.parametrize("value_status, description_status",
                             [
                                 (0, 'События нет'),
                                 (1, 'Раздел не используется'),
                                 (2, 'Невзятие'),
                                 (3, 'Ожидание квитанции'),
                                 (4, 'Раздел снят'),
                                 (5, 'Автовзятие'),
                                 (6, 'Задержка взятия'),
                                 (7, 'Принудительное взятие раздела'),
                                 (8, 'Квитанция получена'),
                                 (9, 'Раздел взят'),
                                 (10, 'Тревога входа'),
                                 (11, 'Тревога'),
                                 (12, 'Пожара нет'),
                                 (13, 'Пожар'),
                                 (14, 'Пожар по ручному извещателю'),
                                 (15, 'Тихая тревога'),
                                 (16, 'Включение выхода'),
                                 (17, 'Выключение выхода'),
                                 (18, 'Отметка наряда'),
                                 (19, 'Протечка воды'),
                                 (20, 'Сброс оповещателей тревоги и пожара'),
                                 (21, 'Свободное событие'),
                                 (22, 'Переключение выхода')
                             ])
    def test_assert_status_partition(self, app, open_tab_status, delete_fake_partition, value_status, description_status):
        with allure.step("Проверка статуса"):
            app.PO_Status.assert_status_partition(value_status, description_status)

    @allure.story("Проверка статуса датчика")
    @pytest.mark.parametrize("z_event, description",
                             [
                                 (0, 'Неизвестно'),
                                 (1, 'Не присвоен раздел'),
                                 (2, 'Готов'),
                                 (3, 'Тревога'),
                                 (4, 'Тревога входа'),
                                 (5, 'Нападение'),
                                 (6, 'Пожар!'),
                                 (7, 'Пожар! Ручной извещатель.'),
                                 (8, 'ШС замкнут'),
                                 (9, 'ШС оборван'),
                                 (10, 'ШС низкое сопротивление'),
                                 (11, 'ШС высокое сопротивление'),
                                 (12, 'ШС в норме'),
                                 (13, 'Корпус открыт'),
                                 (14, 'Корпус закрыт'),
                                 (15, 'Потерян'),
                                 (16, 'Связь восстановлена'),
                                 (17, 'Основная батарея в норме'),
                                 (18, 'Низкий заряд батареи'),
                                 (19, 'Резервная батарея в норме'),
                                 (20, 'Ошибка резервной батареи'),
                                 (21, 'Ошибка устройства'),
                                 (22, 'Проверка связи'),
                                 (23, 'Обрыв шлейфа датчика воды'),
                                 (24, 'Протечка'),
                                 (25, 'Датчик выключен'),
                                 (26, 'Отметка наряда'),
                                 (27, 'Взятие разделов на охрану'),
                                 (28, 'Снятие разделов с охраны'),
                                 (29, 'Перезагрузка датчика'),
                                 (30, 'Принудительное взятие разделов на охрану'),
                                 (31, 'Событие по температуре'),
                                 (32, 'Событие по влажности'),
                                 (33, 'Событие по датчику CO'),
                                 (34, 'Событие саботажа по СМК'),
                                 (35, 'Событие \"Колокольчик\"'),
                                 (36, 'Количество событий по зоне')
                             ])
    def test_assert_status_sensor(self, app, open_tab_sensors, z_event, description):
        with allure.step("Проверка статуса"):
            app.PO_Status.assert_status_sensor(z_event, description)

    @allure.story("Проверка статуса устройства")
    @pytest.mark.parametrize("status, description",
                             [
                                 (1, 'НЕИЗВЕСТНО'),
                                 (2, 'НОРМА'),
                                 (3, 'ТРЕВОГА'),
                                 (4, 'ПОЖАР'),
                                 (5, 'НЕИСПРАВНОСТЬ'),
                                 (6, 'ПУСК'),
                                 (7, 'ОСТАНОВ'),
                                 (8, 'ОТКЛЮЧЕНИЕ АВТОМАТИКИ'),
                                 (9, 'ОТКЛЮЧЕНИЕ'),
                                 (10, 'ПОЛЬЗОВАТЕЛЬ НЕ АВТОРИЗОВАН'),
                                 (11, 'ПОЛЬЗОВАТЕЛЬ АВТОРИЗОВАН')
                             ])
    def test_assert_status_device(self, app, precondition_for_device, status, description):
        with allure.step("Проверка статуса"):
            app.PO_Status.assert_status_device(status, description)