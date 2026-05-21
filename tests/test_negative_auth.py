from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.signup_page import SignupPage

scenarios('../features/invalid_login.feature')
scenarios('../features/signup_duplicate.feature')


@given("the user is on the Demoblaze website homepage",target_fixture="home")
def open_home(driver):
    driver.get("https://www.demoblaze.com")
    return driver


@when(parsers.cfparse('the user clicks on "{button}"'))
def click_button(driver, button):
    if button == "Log in":
        LoginPage(driver).click_login_link()
    elif button == "Sign up":
        SignupPage(driver).click_signup_link()
    else:
        raise ValueError(f'Unexpected button "{button}"')


@when(parsers.cfparse('the user enters username "{username}" and password "{password}"'))
def enter_login_credentials(driver, username, password):
    page = LoginPage(driver)
    page.enter_username(username)
    page.enter_password(password)


@when(parsers.cfparse('the user enters an already registered username "{username}" and password "{password}"'))
def enter_duplicate_signup_credentials(driver, username, password):
    signup_page = SignupPage(driver)
    signup_page.enter_username(username)
    signup_page.enter_password(password)


@when(parsers.cfparse('the user clicks the "{button}" button in the modal'))
def click_modal_button(driver, button):
    if button == "Log in":
        LoginPage(driver).click_login_button()
    elif button == "Sign up":
        SignupPage(driver).click_signup_button()
    else:
        raise ValueError(f'Unexpected modal button "{button}"')


@then(parsers.cfparse('a browser alert pop-up should appear with the message "{message}"'))
def verify_alert_message(driver, message):

    WebDriverWait(driver, 10).until(EC.alert_is_present())

    alert = driver.switch_to.alert

    alert_text = alert.text

    assert message in alert_text

    alert.accept()