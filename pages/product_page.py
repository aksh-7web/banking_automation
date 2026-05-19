from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductPage(BasePage):

    CART = (
        By.LINK_TEXT,
        "Add to cart"
    )

    def select_product(
        self,
        product
    ):

        self.click(
            (
                By.LINK_TEXT,
                product
            )
        )

    def add_cart(self):

        self.click(
            self.CART
        )