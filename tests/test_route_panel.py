import allure

from pages.address_form import AddressForm
from pages.transport_picker import TransportPicker
from test_data import TestData


class TestRoutePanelDisplay:

    @allure.title("Панель выбора транспорта отображается при разных адресах")
    @allure.description(
        "Проверяет появление панели с вариантами транспорта после ввода двух различных адресов"
    )
    def test_transport_panel_shown_for_different_addresses(self, driver, app_ready):
        form = AddressForm(driver)

        with allure.step("Ввести начальный адрес"):
            form.set_origin(TestData.ADDRESS_FROM)

        with allure.step("Ввести конечный адрес"):
            form.set_destination(TestData.ADDRESS_TO)

        picker = TransportPicker(driver)

        with allure.step("Убедиться, что панель выбора транспорта появилась"):
            assert picker.panel_visible()

    @allure.title("Панель транспорта при совпадающих адресах показывает нулевое время")
    @allure.description(
        "Проверяет, что при вводе одного адреса в оба поля маршрут отображается "
        "с нулевым временем в пути и нулевой стоимостью"
    )
    def test_transport_panel_for_identical_addresses(self, driver, app_ready):
        form = AddressForm(driver)

        with allure.step("Ввести одинаковый адрес в поле «Откуда»"):
            form.set_origin(TestData.ADDRESS_TO)

        with allure.step("Ввести тот же адрес в поле «Куда»"):
            form.set_destination(TestData.ADDRESS_TO)

        picker = TransportPicker(driver)

        with allure.step("Убедиться, что маршрут показывает нулевое время и бесплатный проезд"):
            lines = picker.get_route_summary().split("\n")
            assert lines[0] == "Авто Бесплатно"
            assert lines[1] == "В пути 0 мин."
