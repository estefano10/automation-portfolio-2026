from pages.base_page import BasePage
from playwright.sync_api import Page

class PaymentDone(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.confirmed_order_message = page.locator("[data-qa='order-placed']")