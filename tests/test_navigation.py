from pytest_bdd import scenarios, given, when, then, parsers
from pages.navigation_home import NavigationPage

scenarios('../features/navigation_home.feature')

@given('the user is on the Demoblaze website homepage')
def launch_site(driver):
    nav_page = NavigationPage(driver)
    nav_page.navigate_to_homepage()

@then('the user should see the top logo "PRODUCT STORE"')
def verify_homepage_logo(driver):
    nav_page = NavigationPage(driver)
    logo_text = nav_page.get_logo_text().strip()
    assert logo_text == "PRODUCT STORE", f"Expected 'PRODUCT STORE' but got '{logo_text}'"

@then('the navigation bar should show links for "Home", "Contact", "About us", "Cart", "Log in" and "Sign up"')
def verify_navbar_links(driver):
    pass
@when(parsers.parse('the user clicks on "{category}" in the categories menu'))
def click_category(driver, category):
    nav_page = NavigationPage(driver)
    nav_page.click_category_menu(category)

@then(parsers.parse('the page should show items like "{sample_item_1}" and "{sample_item_2}"'))
def verify_category_items(driver, sample_item_1, sample_item_2):
    nav_page = NavigationPage(driver)
    nav_page.verify_product_is_visible(sample_item_1)
    nav_page.verify_product_is_visible(sample_item_2)