import pytest

from constants import AppConfig
from helpers import DriverFactory
from pages.base_page import BasePage
from pages.address_form_page import AddressForm
from pages.transport_picker_page import TransportPicker
from pages.tariff_selector_page import TariffSelector
from pages.searching_taxi_page import SearchingTaxi
from pages.active_ride_page import ActiveRide
from pages.ride_details_page import RideDetails
from test_data import TestData


@pytest.fixture(params=["chrome"])
def driver(request):
    browser = DriverFactory.create(request.param, headless=False)
    browser.maximize_window()
    browser.delete_all_cookies()
    yield browser
    browser.quit()


@pytest.fixture()
def app_ready(driver):
    page = BasePage(driver)
    page.navigate_to(AppConfig.APP_URL)
    form = AddressForm(driver)
    form.await_origin_field()


@pytest.fixture()
def tariff_screen_ready(app_ready, driver):
    form = AddressForm(driver)
    form.set_origin(TestData.ADDRESS_FROM)
    form.set_destination(TestData.ADDRESS_TO)
    picker = TransportPicker(driver)
    picker.await_summon_taxi_btn()
    picker.click_summon_taxi()
    return TariffSelector(driver)


@pytest.fixture()
def business_tariff_ready(tariff_screen_ready):
    tariff_screen_ready.select_business()
    return tariff_screen_ready


@pytest.fixture()
def order_placed(business_tariff_ready, driver):
    business_tariff_ready.submit_order()
    return {
        "tariff": business_tariff_ready,
        "searching": SearchingTaxi(driver),
        "ride": ActiveRide(driver),
        "details": RideDetails(driver),
    }


@pytest.fixture()
def order_placed_with_price(tariff_screen_ready, driver):
    tariff = tariff_screen_ready
    tariff.select_business()
    price = tariff.get_business_tariff_price().split("\n")
    tariff.submit_order()
    return {
        "price": price,
        "searching": SearchingTaxi(driver),
        "ride": ActiveRide(driver),
        "details": RideDetails(driver),
    }


@pytest.fixture()
def active_ride_screen(order_placed):
    order_placed["searching"].wait_search_complete()
    return order_placed
