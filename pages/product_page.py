from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ProductPage(BasePage):
    PRODUCT = (By.LINK_TEXT,"Samsung galaxy s6")
    PRODUCT_TITLE = (By.CLASS_NAME,"name")
    PRODUCT_PRICE = (By.CLASS_NAME,"price-container")
    ADD_TO_CART = (By.LINK_TEXT,"Add to cart")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def select_product(self,product):
        self.click((By.LINK_TEXT,product))

    def add_product_to_cart(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Add to cart']"))).click()
        alert = self.wait.until(EC.alert_is_present())
        alert.accept()

    def open_website(self):
        self.driver.get("https://www.demoblaze.com")

    def select_product(self):

        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.PRODUCT)).click()

    def verify_product_details(self):

        title = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.PRODUCT_TITLE)).text

        price = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.PRODUCT_PRICE)).text

        return (
            title != ""
            and price != ""
        )