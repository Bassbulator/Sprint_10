import allure

from pages.address_form import AddressForm
from pages.transport_picker import TransportPicker
from test_data import TestData


class TestRouteDisplay:

    @allure.title("Построение маршрута по двум адресам")
    @allure.description(
        "Проверяет, что после ввода начального и конечного адреса на карте появляются точки маршрута"
    )
    def test_route_points_appear_on_map(self, driver, app_ready):
        form = AddressForm(driver)

        with allure.step("Ввести начальный адрес"):
            form.set_origin(TestData.ADDRESS_FROM)

        with allure.step("Ввести конечный адрес"):
            form.set_destination(TestData.ADDRESS_TO)

        picker = TransportPicker(driver)

        with allure.step("Убедиться, что на карте появились точки маршрута"):
            assert picker.waypoints_visible()
