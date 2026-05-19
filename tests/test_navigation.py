from pytest_bdd import scenarios, given, when, then, parsers
from pages.navigation_home import NavigationPage

scenarios('../features/navigation_home.feature')

@given('the user is on the Demoblaze website homepage')
def launch_site(driver):
    nav_page = NavigationPage(driver)
    nav_page.navigate_to_homepage()

@then(parsers.parse('the user should see the top logo "PRODUCT STORE" "{logo}"'))
def verify_logo(driver, logo):
    assert logo in driver.page_source
    
@when(parsers.parse('the user clicks on "{category}" in the categories menu'))
def click_category(driver, category):
    nav_page = NavigationPage(driver)
    nav_page.click_category_menu(category)