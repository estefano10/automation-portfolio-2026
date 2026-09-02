from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.cart_link = page.locator("[data-test='shopping-cart-link']")
        self.checkout_button = page.locator("[data-test='checkout']")
        self.total_price = page.locator("[data-test='inventory-item-price']")

    def go_to_cart(self):
        self.cart_link.click()

    def click_checkout(self):
        self.checkout_button.click()