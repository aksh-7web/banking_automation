from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_cart(self):
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "cartur"))).click()
        self.wait.until(EC.visibility_of_element_located((By.ID, "tbodyid")))
    
    def verify_product_in_cart(self, product_name):
        product_xpath = f"//td[text()='{product_name}']"
        try:
            element = self.wait.until(EC.visibility_of_element_located((By.XPATH, product_xpath)))
            return element.is_displayed()
        except TimeoutException:
            return False
    
    def get_cart_total(self):
        total_element = self.wait.until(EC.visibility_of_element_located((By.ID, "totalp")))
        return total_element.text
    
    def remove_product(self, product_name):
        delete_button_xpath = (f"//td[text()='{product_name}']/following-sibling::td/a[text()='Delete']")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, delete_button_xpath))).click()
        self.wait.until(EC.invisibility_of_element_located((By.XPATH, f"//td[text()='{product_name}']")))
    
    def is_cart_empty(self):
        products = self.driver.find_elements(By.XPATH, "//tbody[@id='tbodyid']/tr")
        return len(products) == 0