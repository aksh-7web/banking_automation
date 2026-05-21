from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException
from pages.base_page import BasePage


class LoginPage(BasePage):

    LOGIN_LINK = (By.ID, "login2")
    USERNAME_FIELD = (By.ID, "loginusername")
    PASSWORD_FIELD = (By.ID, "loginpassword")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Log in']")
    USER_WELCOME = (By.ID, "nameofuser")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)

    def click_login_link(self):
        self.click_element(self.LOGIN_LINK)
        # Wait for username field to appear (indicates modal is ready)
        self.wait.until(EC.visibility_of_element_located(self.USERNAME_FIELD))

    def enter_username(self, username):
        self.wait.until(
            EC.visibility_of_element_located(self.USERNAME_FIELD)
        ).send_keys(username)

    def enter_password(self, password):
        self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD_FIELD)
        ).send_keys(password)

    def click_login_button(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()

    def login(self, username, password):
        self.click_login_link()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def verify_login(self):
        try:
            # Wait for welcome message
            welcome_text = self.wait.until(
                EC.visibility_of_element_located(self.USER_WELCOME)
            ).text
            print(f"Login successful. Welcome text: {welcome_text}")
            return "Welcome" in welcome_text
        except TimeoutException:
            # Check for login error alert
            try:
                alert = self.driver.switch_to.alert
                alert_text = alert.text
                print(f"Login failed with alert: {alert_text}")
                alert.accept()
            except:
                print("Login failed - welcome element not found and no alert")
            return False
        except UnexpectedAlertPresentException as e:
            # Handle unexpected alert
            try:
                alert = self.driver.switch_to.alert
                alert_text = alert.text
                print(f"Login error: {alert_text}")
                alert.accept()
            except:
                pass
            return False
        except Exception as e:
            print(f"Login verification error: {str(e)}")
            return False
