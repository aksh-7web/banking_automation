from pytest_bdd import (scenarios,given,when,then)
from pages.product_page import ProductPage

scenarios("../features/product_details.feature")

@given("user opens DemoBlaze website",target_fixture="product_page")
def open_website(driver):

    page = ProductPage(driver)
    page.open_website()

    return page


@when("user selects a product")
def select_product(product_page):

    product_page.select_product()


@then("product details should display successfully")
def verify_product(product_page):
    assert (product_page.verify_product_details())