from locators.tariff_selection_locators import TariffSelectionLocators
from pages.base_page import BasePage
from test_data import TestData


class TariffSelector(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = TariffSelectionLocators()

    def any_tariff_selected(self):
        tariffs = [
            self.locators.BUSINESS_TARIFF,
            self.locators.SLEEPY_TARIFF,
            self.locators.HOLIDAY_TARIFF,
            self.locators.CHATTY_TARIFF,
            self.locators.COZY_TARIFF,
            self.locators.GLAMOUR_TARIFF,
        ]
        return any("active" in self.get_element_classes(t) for t in tariffs)

    def get_business_tariff_price(self):
        return self.read_text(self.locators.BUSINESS_TARIFF_PRICE)

    def _verify_hint(self, tariff_locator, hint_btn_locator, hint_text_locator, expected):
        self.tap(tariff_locator)
        self.mouse_over(hint_btn_locator)
        return expected == self.read_text(hint_text_locator)

    def verify_business_tariff_hint(self):
        return self._verify_hint(
            self.locators.BUSINESS_TARIFF,
            self.locators.BUSINESS_TARIFF_HINT_BTN,
            self.locators.BUSINESS_TARIFF_HINT_TEXT,
            TestData.BUSINESS_TARIFF_HINT,
        )

    def verify_sleepy_tariff_hint(self):
        return self._verify_hint(
            self.locators.SLEEPY_TARIFF,
            self.locators.SLEEPY_TARIFF_HINT_BTN,
            self.locators.SLEEPY_TARIFF_HINT_TEXT,
            TestData.SLEEPY_TARIFF_HINT,
        )

    def verify_holiday_tariff_hint(self):
        return self._verify_hint(
            self.locators.HOLIDAY_TARIFF,
            self.locators.HOLIDAY_TARIFF_HINT_BTN,
            self.locators.HOLIDAY_TARIFF_HINT_TEXT,
            TestData.HOLIDAY_TARIFF_HINT,
        )

    def verify_chatty_tariff_hint(self):
        return self._verify_hint(
            self.locators.CHATTY_TARIFF,
            self.locators.CHATTY_TARIFF_HINT_BTN,
            self.locators.CHATTY_TARIFF_HINT_TEXT,
            TestData.CHATTY_TARIFF_HINT,
        )

    def verify_cozy_tariff_hint(self):
        return self._verify_hint(
            self.locators.COZY_TARIFF,
            self.locators.COZY_TARIFF_HINT_BTN,
            self.locators.COZY_TARIFF_HINT_TEXT,
            TestData.COZY_TARIFF_HINT,
        )

    def verify_glamour_tariff_hint(self):
        return self._verify_hint(
            self.locators.GLAMOUR_TARIFF,
            self.locators.GLAMOUR_TARIFF_HINT_BTN,
            self.locators.GLAMOUR_TARIFF_HINT_TEXT,
            TestData.GLAMOUR_TARIFF_HINT,
        )

    def select_business(self):
        self.tap(self.locators.BUSINESS_TARIFF)

    def select_sleepy(self):
        self.tap(self.locators.SLEEPY_TARIFF)

    def select_holiday(self):
        self.tap(self.locators.HOLIDAY_TARIFF)

    def select_chatty(self):
        self.tap(self.locators.CHATTY_TARIFF)

    def select_cozy(self):
        self.tap(self.locators.COZY_TARIFF)

    def select_glamour(self):
        self.tap(self.locators.GLAMOUR_TARIFF)

    def expand_requirements(self):
        self.tap(self.locators.ORDER_REQUIREMENTS)

    def submit_order(self):
        self.tap(self.locators.CONFIRM_ORDER_BTN)

    def comment_field_visible(self):
        return self.element_exists(self.locators.RIDE_COMMENT)

    def phone_field_visible(self):
        return self.element_exists(self.locators.PHONE_DISPLAY)

    def payment_field_visible(self):
        return self.element_exists(self.locators.PAYMENT_BUTTON)

    def requirements_visible(self):
        return self.element_exists(self.locators.ORDER_REQUIREMENTS)
