from selenium.webdriver.common.by import By


class CommonLocators:
    DISMISS_BTN = [By.XPATH, "//div[text()='Отменить']/preceding-sibling::button"]
    INFO_BTN = [By.XPATH, "//div[text()='Детали']/preceding-sibling::button"]
    ORDER_PANEL = [By.XPATH, "//div[@class='order-body']"]
    ORDER_PANEL_TITLE = [By.XPATH, "//div[@class='order-header-title']"]
    TOGGLE_SWITCH = [By.XPATH, "//span[@class='slider round']"]
