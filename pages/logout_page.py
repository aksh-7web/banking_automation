from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LogoutPage(BasePage):

    LOGIN = (By.ID,"login2")
    USERNAME = (By.ID,"loginusername")
    PASSWORD = (By.ID,"loginpassword")
    LOGIN_BUTTON = (By.XPATH,"//button[text()='Log in']")
    LOGOUT = (By.ID,"logout2")

    def open_site(self):
        self.driver.get("https://www.demoblaze.com")

    def login(self,username,password):
        self.click_element(self.LOGIN)
        self.enter_text(self.USERNAME,username)
        self.enter_text(self.PASSWORD,password)
        self.click_element(self.LOGIN_BUTTON)
    def logout(self):
        self.click_element(self.LOGOUT)

    def verify_logout(self):
        return ("Log in" in self.driver.page_source)