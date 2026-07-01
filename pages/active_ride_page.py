from locators.active_ride_locators import ActiveRideLocators
from pages.base_page import BasePage


class ActiveRide(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ActiveRideLocators()

    def get_title(self):
        return self.read_text(self.locators.RIDE_PANEL_TITLE)

    def vehicle_image_visible(self):
        return self.element_exists(self.locators.VEHICLE_IMAGE)

    def dismiss_btn_visible(self):
        return self.element_exists(self.common.DISMISS_BTN)

    def info_btn_visible(self):
        return self.element_exists(self.common.INFO_BTN)

    def driver_photo_visible(self):
        return self.element_exists(self.locators.DRIVER_PHOTO)

    def driver_name_visible(self):
        return self.element_exists(self.locators.DRIVER_NAME)

    def driver_score_visible(self):
        return self.element_exists(self.locators.DRIVER_SCORE)

    def license_plate_visible(self):
        return self.element_exists(self.locators.LICENSE_PLATE)

    def open_details(self):
        self.tap(self.common.INFO_BTN)

    def dismiss(self):
        self.tap(self.common.DISMISS_BTN)

    def wait_panel_closed(self):
        self.wait_until_hidden(self.locators.RIDE_PANEL)
