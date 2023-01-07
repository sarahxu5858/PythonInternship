from behave.runner import Context
from selenium.webdriver import Chrome, ChromeOptions, Firefox, FirefoxOptions, Remote
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.remote.webdriver import WebDriver
from behave.model import Scenario
from app.application import Application
from chromedriver_py import binary_path
from brwoswerstacksetting import return_drvier_mob, windows_chrome, iphone_chrome, android_chrome


class MyContext(Context):
    driver: WebDriver
    app: Application
    ismobile: bool

# Allure
    # behave -f allure_behave.formatter:AllureFormatter -o test_results/ tests/features/shop_by_facewash.feature


def browser_init(context: MyContext, tags: list):
    context.ismobile = "mobile" in tags
    # options = FirefoxOptions()
    options = ChromeOptions()
    # # options.headless = True
    # context.driver = Firefox(options=options, firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    # context.driver = Chrome(executable_path=binary_path, options=options)
    context.driver = return_drvier_mob(
        android_chrome if context.ismobile else windows_chrome)

    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.app = Application(context.driver)


def before_scenario(context, scenario: Scenario):
    browser_init(context, scenario.tags)


def before_step(context, step):
    pass


def after_step(context, step):
    pass


def after_scenario(context: MyContext, scenario: Scenario):
    # context.driver.execute_script(
    # 'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "' + scenario.name + '"}}')

    context.driver.delete_all_cookies()
    context.driver.quit()


def get_browser_option(browser):
    switcher = {
        "chrome": ChromeOptions(),
        "firefox": FirefoxOptions(),
        # "edge": EdgeOptions(),
        "safari": SafariOptions(),
    }
    return switcher.get(browser, ChromeOptions())
