from page_object.base_page import Page


class HomePage(Page):
    def open_main(self):
        self.open_url()
