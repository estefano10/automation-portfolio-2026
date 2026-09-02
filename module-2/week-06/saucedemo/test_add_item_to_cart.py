from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_item_to_cart(page: Page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    inventory = InventoryPage(page)
    inventory.add_backpack()
    expect(inventory.cart_badge).to_have_text("1")


    # page.goto("https://www.saucedemo.com/")
    # page.get_by_placeholder("Username").fill("standard_user")
    # page.get_by_placeholder("Password").fill("secret_sauce")
    # page.get_by_role("button", name="Login").click()
    # expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    # page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()

    # cart_counter = page.locator("[data-test='shopping-cart-badge']")
    # expect(cart_counter).to_have_text("1")

    # page.locator("[data-test='add-to-cart-sauce-labs-bike-light']").click()
    # expect(cart_counter).to_have_text("2")