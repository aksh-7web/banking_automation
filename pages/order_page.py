from selenium.webdriver.common.by import By

class OrderPage:

    PRODUCT = (By.LINK_TEXT, "Samsung galaxy s6")
    ADD_TO_CART = (By.LINK_TEXT, "Add to cart")
    CART = (By.ID, "cartur")
    PLACE_ORDER = (By.XPATH, "//button[text()='Place Order']")
    NAME = (By.ID, "name")
    COUNTRY = (By.ID, "country")
    CITY = (By.ID, "city")
    CARD = (By.ID, "card")
    MONTH = (By.ID, "month")
    YEAR = (By.ID, "year")
    PURCHASE = (By.XPATH, "//button[text()='Purchase']")