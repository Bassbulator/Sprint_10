from selenium.webdriver.common.by import By


class TariffSelectionLocators:
    BUSINESS_TARIFF = [By.XPATH, "//div[@class='tcard-title' and text()='Рабочий']/.."]
    BUSINESS_TARIFF_PRICE = [
        By.XPATH,
        "//div[text()='Рабочий']//following-sibling::div[@class='tcard-price']",
    ]
    SLEEPY_TARIFF = [By.XPATH, "//div[@class='tcard-title' and text()='Сонный']/.."]
    HOLIDAY_TARIFF = [
        By.XPATH,
        "//div[@class='tcard-title' and text()='Отпускной']/..",
    ]
    CHATTY_TARIFF = [
        By.XPATH,
        "//div[@class='tcard-title' and text()='Разговорчивый']/..",
    ]
    COZY_TARIFF = [
        By.XPATH,
        "//div[@class='tcard-title' and text()='Утешительный']/..",
    ]
    GLAMOUR_TARIFF = [By.XPATH, "//div[@class='tcard-title' and text()='Глянцевый']/.."]

    PHONE_DISPLAY = [By.CSS_SELECTOR, "div.np-text"]
    PAYMENT_BUTTON = [By.CSS_SELECTOR, "div.pp-button.filled"]
    RIDE_COMMENT = [By.XPATH, "//input[@id='comment']"]
    ORDER_REQUIREMENTS = [By.XPATH, "//div[@class='reqs-header']"]
    CONFIRM_ORDER_BTN = [By.CSS_SELECTOR, "button.smart-button"]

    BUSINESS_TARIFF_HINT_TEXT = [
        By.XPATH,
        "//div[@id='tariff-card-0']//div[@class='i-dPrefix']",
    ]
    SLEEPY_TARIFF_HINT_TEXT = [
        By.XPATH,
        "//div[@id='tariff-card-1']//div[@class='i-dPrefix']",
    ]
    HOLIDAY_TARIFF_HINT_TEXT = [
        By.XPATH,
        "//div[@id='tariff-card-2']//div[@class='i-dPrefix']",
    ]
    CHATTY_TARIFF_HINT_TEXT = [
        By.XPATH,
        "//div[@id='tariff-card-3']//div[@class='i-dPrefix']",
    ]
    COZY_TARIFF_HINT_TEXT = [
        By.XPATH,
        "//div[@id='tariff-card-4']//div[@class='i-dPrefix']",
    ]
    GLAMOUR_TARIFF_HINT_TEXT = [
        By.XPATH,
        "//div[@id='tariff-card-5']//div[@class='i-dPrefix']",
    ]

    BUSINESS_TARIFF_HINT_BTN = [By.XPATH, "//button[@data-for='tariff-card-0']"]
    SLEEPY_TARIFF_HINT_BTN = [By.XPATH, "//button[@data-for='tariff-card-1']"]
    HOLIDAY_TARIFF_HINT_BTN = [By.XPATH, "//button[@data-for='tariff-card-2']"]
    CHATTY_TARIFF_HINT_BTN = [By.XPATH, "//button[@data-for='tariff-card-3']"]
    COZY_TARIFF_HINT_BTN = [By.XPATH, "//button[@data-for='tariff-card-4']"]
    GLAMOUR_TARIFF_HINT_BTN = [By.XPATH, "//button[@data-for='tariff-card-5']"]
