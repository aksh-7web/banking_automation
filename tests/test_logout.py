from pytest_bdd import (scenarios,given,when,then)
from pages.logout_page import LogoutPage


scenarios("../features/logout.feature")


@given("user opens DemoBlaze website",target_fixture="logout_page")
def open_site(driver):
    page = LogoutPage(driver)
    page.open_site()
    return page


@when("user logs into application")
def login(logout_page):
    logout_page.login("alok087","tintin")


@when("user clicks logout button")
def logout(logout_page):
    logout_page.logout()


@then("login option should appear")
def verify(logout_page):
    assert (logout_page.verify_logout())