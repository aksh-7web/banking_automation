from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

@given('the user launches the DemoBlaze website')
def step_launch_site(context):
    context.driver.get("https://www.demoblaze.com/")
    context.home_page = HomePage(context.driver)