from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

from locators.common_locators import CommonLocators
from constants import AppConfig


class BasePage:
    def __init__(self, driver, timeout=90):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.common = CommonLocators()

    def navigate_to(self, url):
        self.driver.get(url)

    def go_home(self):
        self.navigate_to(AppConfig.APP_URL)

    def type_text(self, locator, value):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(value)

    def tap(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def toggle_switch(self):
        self.wait.until(EC.element_to_be_clickable(self.common.TOGGLE_SWITCH)).click()

    def find_visible(self, locator, timeout=None):
        wait = WebDriverWait(self.driver, timeout) if timeout is not None else self.wait
        return wait.until(EC.visibility_of_element_located(locator))

    def await_clickable(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))

    def element_exists(self, locator, timeout=5):
        try:
            self.find_visible(locator, timeout)
            return True
        except TimeoutException:
            return False

    def read_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def get_element_classes(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element.get_attribute("class").split()

    def mouse_over(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        ActionChains(self.driver).move_to_element(element).perform()

    def wait_until_hidden(self, locator, timeout=30):
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )
