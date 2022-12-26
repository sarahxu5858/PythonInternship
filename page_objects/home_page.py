from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from .base_page import Page

class HomePage(Page):

    COLLECTION_TITLE = (By.CSS_SELECTOR, 'h1.collection-hero__title')
   
    def open_main(self):
        self.open_url()

    def assert_title_text(self, expected_text):
        self.verify_partial_text(expected_text, *self.COLLECTION_TITLE)
    
    