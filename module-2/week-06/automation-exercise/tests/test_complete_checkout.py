from playwright.sync_api import Page, expect
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage
from pages.payment_done_page import PaymentDone

def test_complete_checkout(logged_in_page: Page, credentials):
    products = ProductsPage(logged_in_page)
    products.open()
    products.add_to_cart("Blue Top")
    products.continue_shopping_button.click()
    products.add_to_cart("Men Tshirt")
    products.view_cart_modal_button.click()
    cart = CartPage(logged_in_page)
    expect(cart.product_names).to_have_text(["Blue Top", "Men Tshirt"])
    cart.checkout_button.click()
    checkout = CheckoutPage(logged_in_page)
    checkout.place_order_button.click()
    payment = PaymentPage(logged_in_page)
    payment.fill_payment()
    payment_done = PaymentDone(logged_in_page)
    expect(payment_done.confirmed_order_message).to_have_text("Order Placed!")
