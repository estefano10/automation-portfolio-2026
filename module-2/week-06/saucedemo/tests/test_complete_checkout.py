from playwright.sync_api import Page, expect
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_complete_checkout(logged_in_page: Page):
    expect(logged_in_page).to_have_url("https://www.saucedemo.com/inventory.html")
    inventory = InventoryPage(logged_in_page)
    inventory.add_backpack()
    expect(inventory.cart_badge).to_have_text("1")
    cart = CartPage(logged_in_page)
    cart.go_to_cart()
    expect(logged_in_page).to_have_url("https://www.saucedemo.com/cart.html")
    expect(cart.total_price).to_have_text("$29.99")
    cart.click_checkout()
    expect(logged_in_page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")
    checkout = CheckoutPage(logged_in_page)
    checkout.submit_information("Estefano", "Gigena", "5152")
    expect(logged_in_page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")
    checkout.finish_checkout()
    expect(checkout.success_message).to_have_text("Thank you for your order!")