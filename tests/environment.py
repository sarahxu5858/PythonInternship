from behave.runner import Context
from selenium import webdriver
from behave.model import Scenario
from app.application import Application


class MyContext(Context):
    driver: webdriver.Chrome
    app: Application


def browser_init(context: Context, test_name: str) -> None:
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.app = Application(context.driver)


def before_scenario(context, scenario: Scenario):
    browser_init(context, scenario.name)


def before_step(context, step):
    pass


def after_step(context, step):
    pass


def after_scenario(context: MyContext, scenario: Scenario):
    context.driver.delete_all_cookies()
    context.driver.quit()
