from pytest_bdd import scenarios, given, when, then
from pages.home_page import HomePage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


scenarios("../features/categories.feature")


@given("user opens DemoBlaze website",target_fixture="home_page")
def open_website(driver):
    driver.get("https://www.demoblaze.com")
    return HomePage(driver)


@when("user clicks Phones category")
def click_phones(home_page):
    home_page.select_category("Phones")


@then("phones category products should display")
def verify_phones(driver):
    
    WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,"//a[contains(text(),'Samsung galaxy s6')]")))
    assert True

@when("user clicks Laptops category")
def click_laptops(home_page):
    home_page.select_category("Laptops")


@then("laptops category products should display")
def verify_laptops(driver):

    WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,"//a[contains(text(),'Sony vaio i5')]")))
    assert True


@when("user clicks Monitors category")
def click_monitors(home_page):

    home_page.select_category("Monitors")

#  This test will fail Because i have asserted False (False failure for report)
@then("monitors category products should display")
def verify_monitors(driver):

    WebDriverWait(driver,20).until(lambda d:("Apple monitor" in d.page_source or"ASUS Full HD"in d.page_source))

#  Take Screenshot
    driver.save_screenshot("screenshots/false_failure.png")
    assert False
