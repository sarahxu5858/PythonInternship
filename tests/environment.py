from behave.runner import Context
from selenium.webdriver import Chrome, ChromeOptions, Firefox, FirefoxOptions, Remote
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.remote.webdriver import WebDriver
from behave.model import Scenario
from app.application import Application
from chromedriver_py import binary_path


class MyContext(Context):
    driver: WebDriver
    app: Application


def browser_init(context: MyContext, test_name: str):
    # options = FirefoxOptions()
    options = ChromeOptions()
    # options.headless = True
    # context.driver = Firefox(options=options, firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    context.driver = Chrome(executable_path=binary_path)

    bstack_options = {
        "osVersion": cap["osVersion"],
        "buildName": cap["buildName"],
        "sessionName": cap["sessionName"],
        "userName": BROWSERSTACK_USERNAME,
        "accessKey": BROWSERSTACK_ACCESS_KEY
    }
    if "os" in cap:
        bstack_options["os"] = cap["os"]
    if "deviceName" in cap:
        bstack_options['deviceName'] = cap["deviceName"]
    if "deviceOrientation" in cap:
        bstack_options["deviceOrientation"] = cap["deviceOrientation"]
    if cap['browserName'] in ['ios']:
        cap['browserName'] = 'safari'
    options = get_browser_option(cap["browserName"].lower())
    if "browserVersion" in cap:
        options.browser_version = cap["browserVersion"]
    options.set_capability('bstack:options', bstack_options)
    if cap['browserName'].lower() == 'samsung':
        options.set_capability('browserName', 'samsung')
    context.driver = Remote(
        command_executor=URL,
        options=options)

    # context.driver = Remote(URL, desired_cap=desired_cap)
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
    context.driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "' + scenario.name + '"}}')

    context.driver.delete_all_cookies()
    context.driver.quit()

# BrowswerStack setting


BROWSERSTACK_USERNAME = "sarahxu_jpz3PN"
BROWSERSTACK_ACCESS_KEY = "LbPLYyFk14z4B7fR52iv"
URL = "https://hub.browserstack.com/wd/hub"
BUILD_NAME = "browserstack-build-1"
capabilities = [
    {
        "browserName": "Chrome",
        "browserVersion": "103.0",
        "os": "Windows",
        "osVersion": "11",
        "sessionName": "BStack Python sample parallel",  # test name
        "buildName": BUILD_NAME,  # Your tests will be organized within this build
    },
    {
        "browserName": "Firefox",
        "browserVersion": "102.0",
        "os": "Windows",
        "osVersion": "10",
        "sessionName": "BStack Python sample parallel",
        "buildName": BUILD_NAME,
    },
    {
        "browserName": "Safari",
        "browserVersion": "14.1",
        "os": "OS X",
        "osVersion": "Big Sur",
        "sessionName": "BStack Python sample parallel",
        "buildName": BUILD_NAME,
    },
]
cap = capabilities[1]


def get_browser_option(browser):
    switcher = {
        "chrome": ChromeOptions(),
        "firefox": FirefoxOptions(),
        # "edge": EdgeOptions(),
        "safari": SafariOptions(),
    }
    return switcher.get(browser, ChromeOptions())
