from page_objects import *

class Application:
    def __init__(self, driver):
        self.driver = driver
        self.home_page = HomePage(self.driver)
        self.header = Header(self.driver)
        self.detail = Detail(self.driver)
        self.info = Info(self.driver)
