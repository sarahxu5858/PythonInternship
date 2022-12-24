from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import when, given, then
from time import sleep

from tests.environment import MyContext

QUALITY = (By.CSS_SELECTOR, 'input[name="quantity"]')
   
@given('Go to {product_name}')
def open_home_page(context: MyContext, product_name: str):
    context.app.home_page.open_url(f"products/{product_name.replace(' ', '-')}")

