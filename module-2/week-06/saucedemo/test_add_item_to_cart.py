from playwright.sync_api import Page, expect
from pages.inventory_page import InventoryPage

def test_add_item_to_cart(logged_in_page: Page):
    expect(logged_in_page).to_have_url("https://www.saucedemo.com/inventory.html")
    inventory = InventoryPage(logged_in_page)
    inventory.add_backpack()
    expect(inventory.cart_badge).to_have_text("1")