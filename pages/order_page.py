from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class OrderPage(BasePage):

    def select_product(self, product_name):

        locator = (By.LINK_TEXT, product_name)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )

        self.click_element(locator)

    def add_product_to_cart(self):

        locator = (By.LINK_TEXT, "Add to cart")

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )

        self.click_element(locator)

        WebDriverWait(self.driver, 10).until(
            EC.alert_is_present()
        )

        self.driver.switch_to.alert.accept()

    def open_cart(self):

        locator = (By.ID, "cartur")

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )

        self.click_element(locator)

    def click_place_order(self):

        locator = (By.XPATH, "//button[text()='Place Order']")

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )

        self.click_element(locator)

    def enter_order_details(
        self,
        name,
        country,
        city,
        card,
        month,
        year
    ):

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "name"))
        )

        self.driver.find_element(By.ID, "name").send_keys(name)
        self.driver.find_element(By.ID, "country").send_keys(country)
        self.driver.find_element(By.ID, "city").send_keys(city)
        self.driver.find_element(By.ID, "card").send_keys(card)
        self.driver.find_element(By.ID, "month").send_keys(month)
        self.driver.find_element(By.ID, "year").send_keys(year)

    def click_purchase(self):

        locator = (By.XPATH, "//button[text()='Purchase']")

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )

        self.click_element(locator)

    def is_order_successful(self):

        return "Thank you for your purchase!" in self.driver.page_source

    def is_order_id_generated(self):

        return "Id" in self.driver.page_source