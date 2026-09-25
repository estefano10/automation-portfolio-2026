from playwright.sync_api import Page, expect
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

def test_add_multiple_products_to_cart(page: Page):
    products = ProductsPage(page)
    products.open()
    products.add_to_cart("Blue Top")
    products.continue_shopping_button.click()
    products.add_to_cart("Men Tshirt")
    products.view_cart_modal_button.click()
    cart = CartPage(page)
    expect(cart.product_names).to_have_text(["Blue Top", "Men Tshirt"])