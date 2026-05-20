import pytest
import random
import string
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Link to feature file
scenarios("../features/signup.feature")

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.wait = WebDriverWait(driver, 10)
    yield driver
    driver.quit()

def random_string(length=8):
    """Generate a random alphanumeric string."""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

@given("the user is on the Demoblaze home page")
def open_home(browser):
    browser.get("https://www.demoblaze.com")

@when("the user clicks on the signup link")
def click_signup(browser):
    signup_link = browser.wait.until(EC.element_to_be_clickable((By.ID, "signin2")))
    signup_link.click()

@when(parsers.cfparse('enters a unique "{username}" and "{password}"'))
def enter_credentials(browser, username, password):
    # If placeholders are <random>, generate new values
    if username == "<random>":
        username = "user_" + random_string(6)
    if password == "<random>":
        password = "pass_" + random_string(8)

    username_field = browser.wait.until(EC.visibility_of_element_located((By.ID, "sign-username")))
    password_field = browser.wait.until(EC.visibility_of_element_located((By.ID, "sign-password")))
    username_field.send_keys(username)
    password_field.send_keys(password)

@when("clicks signup button")
def click_signup_button(browser):
    signup_button = browser.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Sign up']")))
    signup_button.click()

@then("an alert should be displayed with message Sign up successful")
def verify_alert(browser):
    alert = browser.wait.until(EC.alert_is_present())
    assert alert.text == "Sign up successful."
    alert.accept()
