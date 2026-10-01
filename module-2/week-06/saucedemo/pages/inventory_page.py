from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.backpack_button = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")

    def add_backpack(self):
        self.backpack_button.click()