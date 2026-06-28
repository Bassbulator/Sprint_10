from selenium.webdriver.common.by import By


class RideDetailsLocators:
    PICKUP_ADDRESS = [
        By.XPATH,
        "//div[text()='Адрес подачи']/preceding-sibling::div",
    ]
    DROPOFF_ADDRESS = [
        By.XPATH,
        "//div[text()='Адрес назначения']/preceding-sibling::div",
    ]
    PAYMENT_TYPE = [By.XPATH, "//div[text()='Способ оплаты']/preceding-sibling::div"]
    RIDE_COST = [By.XPATH, "//div[contains(text(), 'Стоимость')]"]
