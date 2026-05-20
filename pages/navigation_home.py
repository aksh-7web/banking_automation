import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class NavigationPage(BasePage):
    
    logo = (By.ID, "nava")
    product_grid = (By.ID, "tbodyid")
    active_modal_title = (By.CSS_SELECTOR, ".modal.show .modal-title")
    active_modal_close_btn = (By.CSS_SELECTOR, ".modal.show .btn-secondary")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(self.driver, 10)

    def navigate_to_homepage(self):
        self.driver.get("https://www.demoblaze.com/")
        self.wait.until(EC.visibility_of_element_located(self.logo))

    def get_logo_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.logo)).text

    def click_nav_link(self, link_name):
        link = self.wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, link_name)))
        link.click()
        time.sleep(1)

    def click_category_menu(self, category_name):
        category = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, category_name)))
        category.click()
        time.sleep(1)

    def verify_product_is_visible(self, product_name):
        grid_element = self.wait.until(EC.visibility_of_element_located(self.product_grid))
        grid_text = grid_element.text
        assert product_name in grid_text, f"Product '{product_name}' was not found on the display grid."

    def get_modal_title(self):
        return self.wait.until(EC.visibility_of_element_located(self.active_modal_title)).text

    def close_modal(self):
        close_btn = self.wait.until(EC.element_to_be_clickable(self.active_modal_close_btn))
        close_btn.click()
        time.sleep(1)

    def get_current_url(self):
        return self.driver.current_url