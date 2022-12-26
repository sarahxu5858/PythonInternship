from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import when, given, then
from time import sleep

from tests.environment import MyContext

QUALITY = (By.CSS_SELECTOR, 'input[name="quantity"]')
   
@given('Go to {product_name}')
def open_home_page(context: MyContext, product_name: str):
    context.app.home_page.open_url(f"products/{product_name.replace(' ', '-')}")


@when('Input a {number} to the quantity field')
def input_negative_number(context: MyContext, number):
    context.app.detail.input_quantity(number)


@when('Click on Buy it now button')
def click_buy_now_button(context: MyContext):
    context.app.detail.click_buynow_btn()


@then('Show order summary display')
def verify_order_summary_display(context: MyContext):
    context.app.info.verify_show_order_summary_display() 