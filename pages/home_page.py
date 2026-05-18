from selenium.webdriver.common.by import By
import time

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def select_product(self, product_name):
        self.driver.find_element(By.LINK_TEXT, product_name).click()
        time.sleep(2)