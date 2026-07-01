from selenium.webdriver.common.by import By


class SearchingTaxiLocators:
    COUNTDOWN_TIMER = [By.CSS_SELECTOR, "div.order-header-time"]
    SEARCHING_WINDOW = [By.XPATH, "//div[contains(text(),'Поиск машины')]"]
