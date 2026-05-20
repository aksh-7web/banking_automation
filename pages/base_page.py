from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):

        self.driver = driver

    def click_element(self, locator, timeout=10):

        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def enter_text(self, locator, text, timeout=10):

        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)

    def get_text(self, locator, timeout=10):

        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).text