from locators.transport_picker_locators import TransportPickerLocators
from pages.base_page import BasePage


class TransportPicker(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = TransportPickerLocators()

    def waypoints_visible(self):
        return self.element_exists(self.locators.MAP_WAYPOINT)

    def panel_visible(self):
        return self.element_exists(self.locators.TRANSPORT_PICKER_PANEL)

    def get_route_summary(self):
        return self.read_text(self.locators.ROUTE_SUMMARY)

    def auto_type_classes(self):
        return self.get_element_classes(self.locators.TYPE_AUTO)

    def taxi_type_classes(self):
        return self.get_element_classes(self.locators.TYPE_TAXI)

    def drive_type_classes(self):
        return self.get_element_classes(self.locators.TYPE_DRIVE)

    def scooter_type_classes(self):
        return self.get_element_classes(self.locators.TYPE_SCOOTER)

    def moto_type_classes(self):
        return self.get_element_classes(self.locators.TYPE_MOTO)

    def walking_type_classes(self):
        return self.get_element_classes(self.locators.TYPE_WALKING)

    def optimal_mode_classes(self):
        return self.get_element_classes(self.locators.OPTIMAL_MODE)

    def custom_mode_classes(self):
        return self.get_element_classes(self.locators.CUSTOM_MODE)

    def express_mode_classes(self):
        return self.get_element_classes(self.locators.EXPRESS_MODE)

    def summon_taxi_visible(self):
        return self.element_exists(self.locators.SUMMON_TAXI_BTN)

    def select_optimal_mode(self):
        self.tap(self.locators.OPTIMAL_MODE)

    def select_custom_mode(self):
        self.tap(self.locators.CUSTOM_MODE)

    def select_express_mode(self):
        self.tap(self.locators.EXPRESS_MODE)

    def click_summon_taxi(self):
        self.tap(self.locators.SUMMON_TAXI_BTN)

    def await_summon_taxi_btn(self):
        self.await_clickable(self.locators.SUMMON_TAXI_BTN)

    def await_reserve_btn(self):
        self.await_clickable(self.locators.RESERVE_BTN)
