from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.signup_page import SignupPage

scenarios('../features/invalid_login.feature')
scenarios('../features/signup_duplicate.feature')


@given('the user is on the Demoblaze home page')
def open_home_page(driver):
    driver.get("https://www.demoblaze.com")


@when('the user clicks on the login link')
def click_login(driver):
    login_page = LoginPage(driver)
    login_page.click_login_link()


@when(parsers.parse('enters invalid username "{username}" and password "{password}"'))
def enter_invalid_login_credentials(driver, username, password):
    login_page = LoginPage(driver)
    login_page.enter_username(username)
    login_page.enter_password(password)


@when('clicks login button')
def click_login_button(driver):
    login_page = LoginPage(driver)
    login_page.click_login_button()


@when('the user clicks on the signup link')
def click_signup(driver):
    signup_page = SignupPage(driver)
    signup_page.click_signup_link()


@when(parsers.parse('enters existing username "{username}" and password "{password}"'))
def enter_duplicate_signup_credentials(driver, username, password):
    signup_page = SignupPage(driver)
    signup_page.enter_username(username)
    signup_page.enter_password(password)


@when('clicks signup button')
def click_signup_button(driver):
    signup_page = SignupPage(driver)
    signup_page.click_signup_button()


@then(parsers.parse('an alert should be displayed with message "{message}"'))
def verify_alert_message(driver, message):

    WebDriverWait(driver, 10).until(EC.alert_is_present())

    alert = driver.switch_to.alert

    alert_text = alert.text

    assert message in alert_text

    alert.accept()