from selenium.webdriver.common.by import By


class TransportPickerLocators:
    MAP_WAYPOINT = [
        By.XPATH,
        "//ymaps[contains(@class, 'ymaps-2-1-79-route-pin__label-a')]",
    ]
    TRANSPORT_PICKER_PANEL = [By.CSS_SELECTOR, "div.type-picker.shown"]
    TYPE_DRIVE = [By.XPATH, "//div[contains(@class, 'drive')]"]
    TYPE_SCOOTER = [By.XPATH, "//div[@class='types-container']/div[5]"]
    TYPE_MOTO = [By.XPATH, "//div[@class='types-container']/div[4]"]
    TYPE_TAXI = [By.XPATH, "//div[@class='types-container']/div[3]"]
    TYPE_WALKING = [By.XPATH, "//div[@class='types-container']/div[2]"]
    TYPE_AUTO = [By.XPATH, "//div[@class='types-container']/div[1]"]
    CUSTOM_MODE = [By.XPATH, "//div[text()='Свой']"]
    EXPRESS_MODE = [By.XPATH, "//div[text()='Быстрый']"]
    OPTIMAL_MODE = [By.XPATH, "//div[text()='Оптимальный']"]
    RESERVE_BTN = [By.XPATH, "//button[text()='Забронировать']"]
    SUMMON_TAXI_BTN = [By.XPATH, "//button[text()='Вызвать такси']"]
    ROUTE_SUMMARY = (
        By.XPATH,
        "//div[contains(@class, 'results-container')]//div[contains(@class, 'text')]",
    )
