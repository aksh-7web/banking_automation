from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignupModal:
    def __init__(self, driver):
        self.driver = driver
        
        # Locators on the Homepage to open the modal
        self.signup_nav_button = (By.ID, "signin2")
        
        # Locators inside the Signup Modal
        self.username_input = (By.ID, "sign-username")
        self.password_input = (By.ID, "sign-password")
        self.signup_submit_button = (By.XPATH, "//button[contains(text(), 'Sign up')]")

    def open_modal(self):
        self.driver.find_element(*self.signup_nav_button).click()
        # Wait until the modal username field is visible before interacting
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_locator(self.username_input)
        )

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_signup(self):
        self.driver.find_element(*self.signup_submit_button).click()

    def get_alert_text(self):
        """Waits for the browser signup conflict alert and returns its text."""
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()  # Clicks 'OK' on the alert to close it
        return alert_text