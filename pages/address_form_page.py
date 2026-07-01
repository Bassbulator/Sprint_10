from locators.address_form_locators import AddressFormLocators
from pages.base_page import BasePage


class AddressForm(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = AddressFormLocators()

    def await_origin_field(self):
        self.find_visible(self.locators.ORIGIN_INPUT)

    def set_origin(self, address):
        self.tap(self.locators.ORIGIN_LABEL)
        self.type_text(self.locators.ORIGIN_INPUT, address)

    def set_destination(self, address):
        self.tap(self.locators.DESTINATION_LABEL)
        self.type_text(self.locators.DESTINATION_INPUT, address)
