from selenium.webdriver.common.by import By


class ActiveRideLocators:
    RIDE_PANEL = [By.XPATH, "//div[@class='order-body']"]
    RIDE_PANEL_TITLE = [By.XPATH, "//div[contains(@class, 'order-header-title')]"]
    VEHICLE_IMAGE = [By.XPATH, "//img[@alt='Car']"]
    LICENSE_PLATE = [By.XPATH, "//div[@class='number']"]
    DRIVER_PHOTO = [
        By.XPATH,
        "//div[@class='order-btn-rating']/following-sibling::img",
    ]
    DRIVER_NAME = [
        By.XPATH,
        "//div[@class='order-btn-rating']/parent::div/following-sibling::div",
    ]
    DRIVER_SCORE = [By.XPATH, "//div[@class='order-btn-rating']"]
