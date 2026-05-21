from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):

    def select_category(self, category_name):
        locator = (By.LINK_TEXT, category_name)
        self.click_element(locator)

    def select_product(self, product_name):
        locator = (By.LINK_TEXT, product_name)
        self.click_element(locator)