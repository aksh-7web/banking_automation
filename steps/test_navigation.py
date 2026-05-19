from pytest_bdd import given, when, then, parsers
from pages.navigation_home import NavigationPage

@given('the user is on the Demoblaze website homepage', target_fixture='nav_page')
def step_impl(driver):
    nav_page = NavigationPage(driver)
    nav_page.navigate_to_homepage()
    return nav_page

@when(parsers.parse('the user clicks on "{category}" in the categories menu'))
def step_impl(nav_page, category):
    nav_page.click_category_menu(category)

