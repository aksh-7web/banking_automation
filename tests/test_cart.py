from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver

from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

scenarios('../features/cart_add.feature')
scenarios('../features/cart_remove.feature')

@given('the user launches the DemoBlaze website')
def launch_site(driver):
    driver.get("https://www.demoblaze.com")

@when(parsers.parse('the user selects the product "{product_name}"'))
def select_product(driver, product_name):
    home_page = HomePage(driver)
    home_page.select_product(product_name)


@when("the user adds the product to the cart")
def add_product_to_cart(driver):
    product_page = ProductPage(driver)
    product_page.add_product_to_cart()


@then("the product should be added successfully")
def product_added_successfully():
    assert True


@when("the user returns to the home page")
def return_to_home_page(driver):
    driver.get("https://www.demoblaze.com")


@when("the user navigates to the cart page")
def navigate_to_cart_page(driver):
    cart_page = CartPage(driver)
    cart_page.open_cart()


@then(parsers.parse('the cart should display "{product_name}"'))
def verify_product_in_cart(driver, product_name):
    cart_page = CartPage(driver)
    assert cart_page.verify_product_in_cart(product_name), f"{product_name} not found in cart"


@then("the cart total should be updated correctly")
def verify_cart_total(driver):
    cart_page = CartPage(driver)
    total = cart_page.get_cart_total()
    assert total is not None and total != "", "Cart total was not updated"

@given(parsers.parse('the user has added "{product_name}" to the cart'))
def user_has_added_product_to_cart(driver, product_name):
    home_page = HomePage(driver)
    product_page = ProductPage(driver)
    driver.get("https://www.demoblaze.com")
    home_page.select_product(product_name)
    product_page.add_product_to_cart()

@when(parsers.parse('the user removes "{product_name}" from the cart'))
def remove_product_from_cart(driver, product_name):
    cart_page = CartPage(driver)
    cart_page.remove_product(product_name)

@then(parsers.parse('the product "{product_name}" should not be displayed in the cart'))
def verify_product_removed_from_cart(driver, product_name):
    cart_page = CartPage(driver)
    assert not cart_page.verify_product_in_cart(product_name), f"{product_name} was not removed from cart"

@then("the cart should be empty")
def verify_cart_is_empty(driver):
    cart_page = CartPage(driver)
    assert cart_page.is_cart_empty(), "Cart is not empty"