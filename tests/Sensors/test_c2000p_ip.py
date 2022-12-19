import allure
import pytest
from selenium.webdriver.common.by import By

reruns = 1


@pytest.fixture()
def close_modal_sensor(request, app):
    def fin():
        app.method.click((By.XPATH, '(//*[.=" Отменить "]//div)[last()]'))

    request.addfinalizer(fin)


@pytest.fixture
def c_2000p_ip(app):
    with allure.step("Переход на страницу Зоны Разделы"):
        app.PO_Navigations.goToZonePathPage()
    with allure.step("Переход на вкладку 'Датчики'"):
        app.PO_Navigations.goToZonePathSensorsZone()
    with allure.step("Раскрытие настроек"):
        app.PO_Sensors.sensor_settings_button()


@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты ДАТЧИКИ")
@pytest.mark.flaky(reruns=reruns)
class TestSensorC_2000P_IP:

    @allure.story("С2000Р_ИП")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Название'")
    def test_c_2000p_ip_name_input_positiv(self, app, c_2000p_ip, close_modal_sensor):
        with allure.step("Проверка валидации поля"):
            app.PO_Sensors.input_name_positiv()

    @allure.story("С2000Р_ИП")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Название")
    def test_c_2000p_ip_name_input_negativ(self, app, c_2000p_ip, close_modal_sensor):
        with allure.step("Проверка валидации поля"):
            app.PO_Sensors.input_name_negativ()

    # @allure.story("С2000Р_ИП")
    # @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Гистерезис'")
    # def test_c_2000p_ip_gisteresis_input_positiv(self, app, c_2000p_ip, close_modal_sensor):
    #     with allure.step("Проверка валидации поля"):
    #         app.PO_Zone_Path.input_hysteresis_positiv()
    #
    # @allure.story("С2000Р_ИП")
    # @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Гистерезис")
    # def test_c_2000p_ip_gisteresis_input_negativ(self, app, c_2000p_ip, close_modal_sensor):
    #     with allure.step("Проверка валидации поля"):
    #         app.PO_Zone_Path.input_hysteresis_negativ()

    # @allure.story("С2000Р_ИП")
    # @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Нижний порог по температуре'")
    # def test_c_2000p_ip_temp_min_input_positiv(self, app, c_2000p_ip, close_modal_sensor):
    #     with allure.step("Проверка валидации поля"):
    #         app.PO_Zone_Path.input_hysteresis_positiv()
    #
    # @allure.story("С2000Р_ИП")
    # @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Нижний порог по температуре'")
    # def test_c_2000p_ip_temp_min_input_negativ(self, app, c_2000p_ip, close_modal_sensor):
    #     with allure.step("Проверка валидации поля"):
    #         app.PO_Zone_Path.input_hysteresis_negativ()

    # @allure.story("С2000Р_ИП")
    # @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Верхний порог по температуре'")
    # def test_c_2000p_ip_temp_max_input_positiv(self, app, c_2000p_ip, close_modal_sensor):
    #     with allure.step("Проверка валидации поля"):
    #         app.PO_Zone_Path.input_hysteresis_positiv()
    #
    # @allure.story("С2000Р_ИП")
    # @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Верхний порог по температуре'")
    # def test_c_2000p_ip_temp_max_input_negativ(self, app, c_2000p_ip, close_modal_sensor):
    #     app.PO_Zone_Path.input_hysteresis_negativ()

    @allure.story("С2000Р_ИП")
    @allure.title("Проверка названий полей")
    def test_c_2000p_ip_titles(self, app, c_2000p_ip, close_modal_sensor):
        with allure.step("Проверка названий полей"):
            app.PO_Sensors.text_c2000p_ip_title()

    @allure.story("С2000Р_ИП")
    @allure.title("Проверка переключения чек-боксов")
    def test_c_2000p_ip_check_box(self, app, c_2000p_ip, close_modal_sensor):
        with allure.step("Проверка включения чекбоксов"):
            app.PO_Sensors.check_box_c_2000p_ip_on()
        with allure.step("Проверка выключения чекбоксов"):
            app.PO_Sensors.check_box_c_2000p_ip_off()
        with allure.step("Проверка частичного выбора чекбоксов"):
            app.PO_Sensors.check_box_c_2000p_ip_some()

    @allure.story("С2000Р_ИП")
    @allure.title("Проверка выпадающего списка: Раздел")
    def test_c_2000p_ip_drop_list_path(self, app, c_2000p_ip, close_modal_sensor):
        with allure.step("Проверка выбора позиций из выпадающего списка"):
            app.PO_Sensors.drop_list_path_c_2000p_ip()

    @allure.story("С2000Р_ИП")
    @allure.title("Проверка выпадающего списка: Режим индикации")
    def test_c_2000p_ip_drop_list_indication_mode(self, app, c_2000p_ip, close_modal_sensor):
        with allure.step("Проверка выбора позиций из выпадающего списка"):
            app.PO_Sensors.drop_list_indication_mode_c_2000p_ip()

    @allure.story("С2000Р_ИП")
    @allure.title("Проверка выпадающего списка: Режим уведомлений")
    def test_c_2000p_ip_drop_list_notification_mode(self, app, c_2000p_ip, close_modal_sensor):
        with allure.step("Проверка выбора позиций из выпадающего списка"):
            app.PO_Sensors.drop_list_notification_mode_c_2000p_ip()

    @allure.story("С2000Р_ИП")
    @allure.title("Проверка сохранения данных")
    def test_c_2000p_ip_save_data(self, app, c_2000p_ip, close_modal_sensor):
        with allure.step("Генерирование тестовых данных"):
            app.ganerate_data.createData()
        with allure.step("Заполнение полей данными"):
            app.PO_Sensors.save_data_c_2000p_ip()
        with allure.step("Сохранение данных"):
            app.PO_Directions.save_button_click()
        with allure.step("Выход и повторный вход"):
            app.PO_Navigations.ExitAndEnter()
            app.PO_Navigations.goToZonePathPage()
            app.PO_Navigations.goToZonePathSensorsZone()
            app.PO_Sensors.sensor_settings_button()
        with allure.step("Проверка сохранения"):
            app.PO_Sensors.assert_save_data_c_2000p_ip()
