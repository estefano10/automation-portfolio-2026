from playwright.sync_api import Page
from pages.base_page import BasePage

class ProductsPage(BasePage):
    PATH = "/products"
    def __init__(self, page: Page):
        super().__init__(page)
        self.search_box = page.locator("#search_product")
        self.search_button = page.locator("#submit_search")
        self.search_results = page.locator(".features_items")
        self.products = page.locator(".single-products")
        self.added_msg_confirmation = page.locator(".modal-content")
        self.continue_shopping_button= page.get_by_role("button", name="Continue Shopping")
        self.view_cart_modal_button = page.locator(".modal-body a[href='/view_cart']")

    def search(self, term: str):
        self.search_box.fill(term)
        self.search_button.click()

    def add_to_cart(self, product: str):
        card = self.products.filter(has_text=product)
        card.hover()
        card.locator(".overlay-content .add-to-cart").click()
