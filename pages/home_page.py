from selenium.webdriver.common.by import By
from pages.base_page import BasePage

import time

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def select_product(self, product_name):
        self.driver.find_element(By.LINK_TEXT, product_name).click()
        time.sleep(2)
class HomePage(BasePage):

    def select_category(self, category_name):

        locator = (
            By.LINK_TEXT,
            category_name
        )

        self.click_element(locator)