from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginModal:
    def __init__(self, driver):
        self.driver = driver
        
        # Locators on the Homepage to open the modal
        self.login_nav_button = (By.ID, "login2")
        
        # Locators inside the Login Modal
        self.username_input = (By.ID, "loginusername")
        self.password_input = (By.ID, "loginpassword")
        self.login_submit_button = (By.XPATH, "//button[contains(text(), 'Log in')]")

    def open_modal(self):
        self.driver.find_element(*self.login_nav_button).click()
        # Wait until the modal username field is visible before interacting
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_locator(self.username_input)
        )

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_submit_button).click()

    def get_alert_text(self):
        """Waits for the browser error alert pop-up to appear and returns its text."""
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()  # Clicks 'OK' on the alert to close it
        return alert_text