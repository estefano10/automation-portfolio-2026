from playwright.sync_api import Page
from pages.login_page import LoginPage

class InventoryPage:
    def __init__(self, page: Page):
        self.backpack_button = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")

    def add_backpack(self):
        self.backpack_button.click()