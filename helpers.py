from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


class DriverFactory:
    @staticmethod
    def create(browser: str, headless: bool = False):
        if browser.lower() == "chrome":
            options = ChromeOptions()
            options.page_load_strategy = "none"
            if headless:
                options.add_argument("--headless")
            options.add_argument("--disable-save-password-bubble")
            options.add_experimental_option(
                "prefs",
                {
                    "credentials_enable_service": False,
                    "profile.password_manager_enabled": False,
                },
            )
            return webdriver.Chrome(options=options)
