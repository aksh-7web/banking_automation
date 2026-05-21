from pytest_bdd import scenarios, given, when, then, parsers
from pages.order_page import OrderPage

scenarios("../features/place_order.feature")
scenarios("../features/order_confirmation.feature")


@given("the user is on the Demoblaze home page")
def open_home(driver):

    driver.get("https://www.demoblaze.com")


@when(parsers.cfparse('the user selects product "{product_name}"'))
def select_product(driver, product_name):

    page = OrderPage(driver)
    page.select_product(product_name)


@when("the user adds product to cart")
def add_to_cart(driver):

    page = OrderPage(driver)
    page.add_product_to_cart()


@when("the user opens cart")
def open_cart(driver):

    page = OrderPage(driver)
    page.open_cart()


@when("the user clicks place order button")
def place_order(driver):

    page = OrderPage(driver)
    page.click_place_order()


@when(parsers.cfparse(
    'the user enters name "{name}", country "{country}", city "{city}", '
    'card "{card}", month "{month}", year "{year}"'
))
def enter_order_details(driver, name, country, city, card, month, year):

    page = OrderPage(driver)

    page.enter_order_details(
        name,
        country,
        city,
        card,
        month,
        year
    )


@when("the user clicks purchase button")
def click_purchase(driver):

    page = OrderPage(driver)
    page.click_purchase()


@then("order should be placed successfully")
def verify_order(driver):

    page = OrderPage(driver)
    assert page.is_order_successful()


@then("order id should be generated")
def verify_order_id(driver):

    page = OrderPage(driver)
    assert page.is_order_id_generated()