from pages.base_page import BasePage
from playwright.sync_api import Page

class CheckoutPage(BasePage):
    PATH = "/checkout"
    def __init__(self, page: Page):
        super().__init__(page)
        self.comment_box = page.locator("[name='message']")
        self.place_order_button = page.locator(".check_out")