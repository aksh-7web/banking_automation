from selenium.webdriver.common.by import By
import time

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    cart_button = (By.ID, "cartur")

    def open_cart(self):
        self.driver.find_element(*self.cart_button).click()
        time.sleep(10)
    
    def verify_product_in_cart(self, product_name):
        return product_name in self.driver.page_source
    
    def get_cart_total(self):
        return self.driver.find_element(By.ID, "totalp").text
    
    def remove_product(self):
        self.driver.find_element(By.LINK_TEXT, "Delete").click()
        time.sleep(10)
    
    def remove_product(self, product_name):
        delete_button_xpath = f"//td[text()='{product_name}']/following-sibling::td/a[text()='Delete']"
        self.driver.find_element(By.XPATH, delete_button_xpath).click()
        time.sleep(10)
    
    def is_cart_empty(self):
        products = self.driver.find_elements(By.XPATH, "//tbody[@id='tbodyid']/tr")
        return len(products) == 0