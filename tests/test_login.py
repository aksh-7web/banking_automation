from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage

scenarios("../features/login.feature")

@given("the user is on the Demoblaze home page")
def open_home(driver):
    driver.get("https://www.demoblaze.com")

@when("the user clicks on the login link")
def click_login(driver):
    page = LoginPage(driver)
    page.click_login_link()

@when(parsers.cfparse('enters username "{username}"  and password "{password}"'))

def enter_credentials(driver, username, password):
    page = LoginPage(driver)
    page.enter_username(username)
    page.enter_password(password)

@when("clicks login button")
def click_login_button(driver):
    page = LoginPage(driver)
    page.click_login_button()

@then("user should see products page")
def verify_products_page(driver):
    page = LoginPage(driver)
    assert page.verify_login()
