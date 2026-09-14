from playwright.sync_api import Page
class BasePage:
    BASE_URL = "https://automationexercise.com"
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(self.BASE_URL + self.PATH)