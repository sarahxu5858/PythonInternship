from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import when, given, then
from time import sleep

from tests.environment import MyContext


@given('Open Home Page')
def open_home_page(context: MyContext):
    context.app.home_page.open_main()

# @when()
#
# @and()
#
# @then
