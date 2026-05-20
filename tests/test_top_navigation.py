from pytest_bdd import scenarios, given, when, then, parsers
from pages.navigation_home import NavigationPage

scenarios('../features/top_navigation_bar.feature')

@given('the user is on the Demoblaze website homepage')
def launch_site(driver):
    nav_page = NavigationPage(driver)
    nav_page.navigate_to_homepage()

@when(parsers.parse('the user clicks on the "{nav_link}" link in the top header'))
def click_header_link(driver, nav_link):
    nav_page = NavigationPage(driver)
    nav_page.click_nav_link(nav_link)

@then(parsers.parse('a modal window titled "{expected_title}" should appear on the screen'))
def verify_modal_title(driver, expected_title):
    nav_page = NavigationPage(driver)
    actual_title = nav_page.get_modal_title()
    assert actual_title == expected_title, f"Expected modal title '{expected_title}' but got '{actual_title}'"

@then('the user closes the modal window')
def close_active_modal(driver):
    nav_page = NavigationPage(driver)
    nav_page.close_modal()

@then(parsers.parse('the user should be redirected to the page URL containing "{url_snippet}"'))
def verify_url_redirection(driver, url_snippet):
    nav_page = NavigationPage(driver)
    current_url = nav_page.get_current_url()
    assert url_snippet in current_url, f"Expected URL to contain '{url_snippet}' but got '{current_url}'"

@then('the user should see the main product display grid reset or refreshed with all products visible')
def verify_grid_refresh(driver):
    nav_page = NavigationPage(driver)
    nav_page.verify_product_is_visible("Samsung galaxy s6")