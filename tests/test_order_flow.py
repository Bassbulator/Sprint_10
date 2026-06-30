import allure
import pytest

from pages.address_form_page import AddressForm
from pages.transport_picker_page import TransportPicker
from pages.tariff_selector_page import TariffSelector
from pages.searching_taxi_page import SearchingTaxi
from pages.active_ride_page import ActiveRide
from pages.ride_details_page import RideDetails
from test_data import TestData


class TestOrderFlow:

    @allure.title("Блок выбора тарифа появляется после нажатия «Вызвать такси»")
    @allure.description(
        "Проверяет, что после нажатия на кнопку вызова такси открывается блок с тарифами "
        "и один из них оказывается выбранным по умолчанию"
    )
    def test_tariff_block_shown_and_default_tariff_selected(self, driver, app_ready):
        form = AddressForm(driver)

        with allure.step("Ввести начальный адрес"):
            form.set_origin(TestData.ADDRESS_FROM)

        with allure.step("Ввести конечный адрес"):
            form.set_destination(TestData.ADDRESS_TO)

        picker = TransportPicker(driver)

        with allure.step("Нажать кнопку вызова такси"):
            picker.await_summon_taxi_btn()
            picker.click_summon_taxi()

        tariff = TariffSelector(driver)

        with allure.step("Убедиться, что один из тарифов выбран"):
            assert tariff.any_tariff_selected()

    @allure.title("Подсказки тарифов соответствуют ожидаемым описаниям")
    @allure.description(
        "Проверяет, что при наведении на кнопку информации у каждого тарифа "
        "отображается верный текст подсказки, а все поля блока заказа присутствуют"
    )
    @pytest.mark.xfail(
        reason="Известный дефект: описания тарифов «Сонный» и «Разговорчивый» перепутаны местами"
    )
    def test_tariff_hints_match_expected_descriptions(self, driver, app_ready):
        form = AddressForm(driver)

        with allure.step("Ввести начальный адрес"):
            form.set_origin(TestData.ADDRESS_FROM)

        with allure.step("Ввести конечный адрес"):
            form.set_destination(TestData.ADDRESS_TO)

        picker = TransportPicker(driver)

        with allure.step("Нажать кнопку вызова такси"):
            picker.await_summon_taxi_btn()
            picker.click_summon_taxi()

        tariff = TariffSelector(driver)

        with allure.step("Проверить подсказки всех тарифов и наличие полей формы"):
            assert tariff.verify_business_tariff_hint()
            assert tariff.verify_holiday_tariff_hint()
            assert tariff.verify_cozy_tariff_hint()
            assert tariff.verify_glamour_tariff_hint()
            assert tariff.comment_field_visible()
            assert tariff.phone_field_visible()
            assert tariff.payment_field_visible()
            assert tariff.requirements_visible()
            assert tariff.verify_chatty_tariff_hint()
            assert tariff.verify_sleepy_tariff_hint()

    @allure.title("Полный сценарий бронирования такси с последующей отменой")
    @allure.description(
        "Проверяет полный цикл заказа: выбор тарифа, дополнительных опций, оформление заказа, "
        "ожидание машины, просмотр деталей и отмена поездки"
    )
    @pytest.mark.xfail(reason="Известный дефект: кнопка «Отменить» не завершает заказ")
    def test_complete_booking_flow_with_business_tariff_and_cancel(
        self, driver, app_ready
    ):
        form = AddressForm(driver)
        tariff = TariffSelector(driver)
        searching = SearchingTaxi(driver)
        ride = ActiveRide(driver)
        details = RideDetails(driver)

        with allure.step("Ввести начальный адрес"):
            form.set_origin(TestData.ADDRESS_FROM)

        with allure.step("Ввести конечный адрес"):
            form.set_destination(TestData.ADDRESS_TO)

        picker = TransportPicker(driver)

        with allure.step("Нажать кнопку вызова такси"):
            picker.await_summon_taxi_btn()
            picker.click_summon_taxi()

        with allure.step("Выбрать тариф «Рабочий»"):
            tariff.select_business()

        with allure.step("Открыть требования к заказу"):
            tariff.expand_requirements()

        with allure.step("Включить опцию «Столик для ноутбука»"):
            tariff.toggle_switch()

        with allure.step("Сохранить стоимость тарифа до оформления заказа"):
            price_before = tariff.get_business_tariff_price().split("\n")

        with allure.step("Нажать «Ввести номер и заказать»"):
            tariff.submit_order()

        with allure.step("Зафиксировать состояние окна поиска машины"):
            title_searching = searching.get_window_title()
            has_dismiss_in_search = searching.dismiss_btn_visible()
            has_countdown = searching.countdown_visible()

        with allure.step("Дождаться завершения поиска машины"):
            searching.wait_search_complete()

        with allure.step("Зафиксировать состояние окна активной поездки"):
            title_ride = ride.get_title()
            has_plate = ride.license_plate_visible()
            has_vehicle = ride.vehicle_image_visible()
            has_photo = ride.driver_photo_visible()
            has_name = ride.driver_name_visible()
            has_score = ride.driver_score_visible()
            has_dismiss_in_ride = ride.dismiss_btn_visible()
            has_info_in_ride = ride.info_btn_visible()

        with allure.step("Открыть детали поездки"):
            ride.open_details()
            details.await_pickup_address()

        with allure.step("Считать итоговую стоимость из деталей поездки"):
            price_after = details.get_fare_text().split("\n")

        with allure.step("Отменить поездку"):
            ride.dismiss()

        with allure.step("Дождаться закрытия панели активной поездки"):
            ride.wait_panel_closed()

        with allure.step("Убедиться, что стоимость в деталях совпадает с выбранным тарифом"):
            assert price_before[0] == price_after[1]

        with allure.step("Проверить все элементы и заголовки окон"):
            assert title_searching == TestData.SEARCHING_TAXI_TITLE
            assert title_ride == TestData.CAR_ARRIVING_TITLE
            assert has_dismiss_in_search
            assert has_countdown
            assert has_plate
            assert has_vehicle
            assert has_photo
            assert has_name
            assert has_score
            assert has_dismiss_in_ride
            assert has_info_in_ride
