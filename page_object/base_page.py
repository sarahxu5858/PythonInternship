from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumpagefactory import PageFactory


class Page(PageFactory):

    def __init__(self, driver: webdriver):
        self.driver = driver
        self.base_url = 'https://shop.cureskin.com/'
        self.wait = WebDriverWait(self.driver, 15)

    def open_url(self, end_url=''):
        self.driver.get(f'{self.base_url}{end_url}')

    def find_element(self, *locator: str):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)

    def verify_element_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text in actual_text, f'Expected {expected_text} is not in {actual_text}'

    def verify_url_contains_query(self, query):
        self.wait.until(EC.url_contains(query))


