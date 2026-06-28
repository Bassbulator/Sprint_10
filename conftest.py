import pytest

from constants import AppConfig
from helpers import DriverFactory
from pages.base_page import BasePage
from pages.address_form import AddressForm


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
