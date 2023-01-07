from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

from .base_page import Page


class Info(Page):
    
    # SHOWORDERSUMMARY = (By.XPATH, '//span[contains(text(),"Show order summary")]')
    SHOWORDERSUMMARY = (By.ID, 'primary-header')
    def verify_show_order_summary_display(self):
        # try: 
        self.verify_partial_text('Contact information', *self.SHOWORDERSUMMARY)
        # except NoSuchElementException:
        #     print(f'Expected "Show order summary", but got {actual_text}')
        # except Exception as e:
        #     print(e)
        