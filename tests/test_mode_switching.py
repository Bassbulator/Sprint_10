import allure

from pages.address_form_page import AddressForm
from pages.transport_picker_page import TransportPicker
from test_data import TestData


class TestModeSwitching:

    @allure.title("Переключение между режимами Оптимальный и Быстрый")
    @allure.description(
        "Проверяет, что при смене режима маршрута между Оптимальным и Быстрым "
        "меняется активный таб, доступные виды транспорта и пересчитывается маршрут"
    )
    def test_switching_optimal_and_express_modes_recalculates_route(
        self, driver, app_ready
    ):
        form = AddressForm(driver)

        with allure.step("Ввести начальный адрес"):
            form.set_origin(TestData.ADDRESS_FROM)

        with allure.step("Ввести конечный адрес"):
            form.set_destination(TestData.ADDRESS_TO)

        picker = TransportPicker(driver)

        with allure.step("Сохранить данные маршрута до переключения режима"):
            summary_before = picker.get_route_summary().split("\n")

        with allure.step("Активировать режим Оптимальный"):
            picker.select_optimal_mode()

        with allure.step("Считать классы кнопки Оптимальный"):
            classes_optimal_active = picker.optimal_mode_classes()

        with allure.step("Считать классы кнопки Быстрый"):
            classes_express_inactive = picker.express_mode_classes()

        with allure.step("Сохранить данные маршрута после активации Оптимального"):
            summary_optimal = picker.get_route_summary().split("\n")

        with allure.step("Считать классы Такси в режиме Оптимальный"):
            classes_taxi_in_optimal = picker.taxi_type_classes()

        with allure.step("Считать классы Авто в режиме Оптимальный"):
            classes_auto_in_optimal = picker.auto_type_classes()

        with allure.step("Активировать режим Быстрый"):
            picker.select_express_mode()
            picker.await_summon_taxi_btn()

        with allure.step("Считать классы кнопки Оптимальный после переключения"):
            classes_optimal_inactive = picker.optimal_mode_classes()

        with allure.step("Считать классы кнопки Быстрый после переключения"):
            classes_express_active = picker.express_mode_classes()

        with allure.step("Считать классы Такси в режиме Быстрый"):
            classes_taxi_in_express = picker.taxi_type_classes()

        with allure.step("Убедиться, что данные маршрута изменились"):
            assert summary_before != summary_optimal

        with allure.step("Убедиться, что кнопка Оптимальный активна"):
            assert "active" in classes_optimal_active

        with allure.step("Убедиться, что кнопка Быстрый неактивна в режиме Оптимальный"):
            assert "active" not in classes_express_inactive

        with allure.step("Убедиться, что Такси недоступно в режиме Оптимальный"):
            assert "disabled" in classes_taxi_in_optimal

        with allure.step("Убедиться, что Авто активно в режиме Оптимальный"):
            assert "active" in classes_auto_in_optimal

        with allure.step("Убедиться, что кнопка Быстрый активна"):
            assert "active" in classes_express_active

        with allure.step("Убедиться, что кнопка Оптимальный неактивна в режиме Быстрый"):
            assert "active" not in classes_optimal_inactive

        with allure.step("Убедиться, что Такси доступно в режиме Быстрый"):
            assert "active" in classes_taxi_in_express

        with allure.step("Убедиться, что кнопка вызова такси отображается"):
            assert picker.summon_taxi_visible()

    @allure.title("Режим Свой делает доступными все виды транспорта")
    @allure.description(
        "Проверяет, что при выборе режима «Свой» становятся доступны все шесть видов транспорта"
    )
    def test_custom_mode_enables_all_transport_types(self, driver, app_ready):
        form = AddressForm(driver)

        with allure.step("Ввести начальный адрес"):
            form.set_origin(TestData.ADDRESS_FROM)

        with allure.step("Ввести конечный адрес"):
            form.set_destination(TestData.ADDRESS_TO)

        picker = TransportPicker(driver)

        with allure.step("Активировать режим Свой"):
            picker.select_custom_mode()
            picker.await_summon_taxi_btn()

        with allure.step("Убедиться, что режим Быстрый стал неактивным"):
            assert "active" not in picker.express_mode_classes()

        with allure.step("Убедиться, что режим Свой стал активным"):
            assert "active" in picker.custom_mode_classes()

        with allure.step("Убедиться, что Такси доступно"):
            assert "disabled" not in picker.taxi_type_classes()

        with allure.step("Убедиться, что Авто доступно"):
            assert "disabled" not in picker.auto_type_classes()

        with allure.step("Убедиться, что Пешком доступно"):
            assert "disabled" not in picker.walking_type_classes()

        with allure.step("Убедиться, что Мото доступно"):
            assert "disabled" not in picker.moto_type_classes()

        with allure.step("Убедиться, что Самокат доступен"):
            assert "disabled" not in picker.scooter_type_classes()

        with allure.step("Убедиться, что Драйв доступен"):
            assert "disabled" not in picker.drive_type_classes()
