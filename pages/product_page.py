from selenium.webdriver.common.by import By
import time

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    add_to_cart_link = (By.LINK_TEXT, "Add to cart")

    def add_product_to_cart(self):
        self.driver.find_element(*self.add_to_cart_link).click()
        time.sleep(2)

        alert = self.driver.switch_to.alert
        alert.accept()