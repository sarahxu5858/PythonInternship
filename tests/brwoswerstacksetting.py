from selenium import webdriver

BROWSERSTACK_USERNAME = ""
BROWSERSTACK_ACCESS_KEY = ""
    
caps = [{
    "os": "Windows",
    "osVersion": "11",
},
    {
    'deviceName': 'Google Pixel 5',
    'osVersion': '11.0',
    'realMobile': 'true',
},
    {
    'deviceName': 'iPhone 12',
    'osVersion': '14',
    "realMobile": "true",
}]

windows_chrome = caps[0]
android_chrome = caps[1]
iphone_chrome = caps[2]

def return_drvier_mob(desired_cap):
    cap = {'bstack:options': desired_cap, "browserName": "Chrome", }
    return webdriver.Remote(
        command_executor=f'https://{BROWSERSTACK_USERNAME}:{BROWSERSTACK_ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub',
        desired_capabilities=cap)



