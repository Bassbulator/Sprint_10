from locators.searching_taxi_locators import SearchingTaxiLocators
from pages.base_page import BasePage


class SearchingTaxi(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = SearchingTaxiLocators()

    def wait_search_complete(self):
        self.wait_until_hidden(self.locators.SEARCHING_WINDOW)

    def dismiss_btn_visible(self):
        return self.element_exists(self.common.DISMISS_BTN)

    def info_btn_visible(self):
        return self.element_exists(self.common.INFO_BTN)

    def countdown_visible(self):
        return self.element_exists(self.locators.COUNTDOWN_TIMER)

    def get_window_title(self):
        return self.read_text(self.locators.SEARCHING_WINDOW)
