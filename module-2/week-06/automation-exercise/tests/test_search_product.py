from playwright.sync_api import Page, expect
from pages.products_page import ProductsPage

def test_search_product(page: Page):
    products = ProductsPage(page)
    products.open()
    products.search("dress")
    expect(products.search_results.first).to_be_visible()
    expect(products.search_results.first).to_contain_text("Dress")