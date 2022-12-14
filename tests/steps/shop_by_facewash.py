from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import when, given, then
from time import sleep

from tests.environment import MyContext


@given('Open Home Page')
def open_home_page(context: MyContext):
    context.app.home_page.open_main()

@when('Click Shop by product')
def open_home_page(context: MyContext):
    context.app.header.click_by_product()

@when('Select Face Washes option')
def click_face_washes(context: MyContext):
    context.app.header.click_select_face_wash()

@then('{expected_result} products display')
def verify_wash_products_display(context: MyContext, expected_result):
    context.app.home_page.assert_title_text(expected_result)
