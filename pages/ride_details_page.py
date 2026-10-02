from locators.ride_details_locators import RideDetailsLocators
from pages.base_page import BasePage


class RideDetails(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = RideDetailsLocators()

    def await_pickup_address(self):
        return self.find_visible(self.locators.PICKUP_ADDRESS)

    def dropoff_visible(self):
        return self.element_exists(self.locators.DROPOFF_ADDRESS)

    def pickup_visible(self):
        return self.element_exists(self.locators.PICKUP_ADDRESS)

    def payment_type_visible(self):
        return self.element_exists(self.locators.PAYMENT_TYPE)

    def get_fare_text(self):
        return self.read_text(self.locators.RIDE_COST)
