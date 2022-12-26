from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from .base_page import Page


class Detail(Page):

    QUALITY_FIELD = (By.CSS_SELECTOR, 'input[name="quantity"]')
    RIGHT_ARROW = (By.CSS_SELECTOR, 'button[name=plus]')
    BUY_IT_NOW_BTN = (By.CSS_SELECTOR, 'button[data-testid=Checkout-button]')
    ADDTOCART_BTN = (By.NAME, 'add')

    def input_quantity(self, text):
        self.input_text(text, *self.QUALITY_FIELD)

    def click_buynow_btn(self):
        self.click(*self.BUY_IT_NOW_BTN)