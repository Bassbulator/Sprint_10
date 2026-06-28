from selenium.webdriver.common.by import By


class AddressFormLocators:
    ORIGIN_LABEL = [By.XPATH, "//label[contains(text(), 'Откуда')]"]
    DESTINATION_LABEL = [By.XPATH, "//label[contains(text(), 'Куда')]"]
    ORIGIN_INPUT = [By.CSS_SELECTOR, "input#from.input"]
    DESTINATION_INPUT = [By.CSS_SELECTOR, "input#to.input"]
