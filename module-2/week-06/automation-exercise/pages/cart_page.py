from playwright.sync_api import Page
from pages.base_page import BasePage

class CartPage(BasePage):
    PATH = "/view_cart"
    def __init__(self, page: Page):
        super().__init__(page)
        self.product_names = page.locator(".cart_description h4 a")
        self.checkout_button = page.locator(".check_out")
        self.go_to_login_link = page.locator(".modal-body a[href='/login']")