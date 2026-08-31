from playwright.sync_api import Page, expect

def test_complete_checkout(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()

    page.locator("[data-test='shopping-cart-link']").click()

    page.locator("[data-test='checkout']").click()

    page.get_by_placeholder("First Name").fill("Estefano")
    page.get_by_placeholder("Last Name").fill("Gigena")
    page.get_by_placeholder("Zip/Postal Code").fill("5152")

    page.locator("[data-test='continue']").click()
    page.locator("[data-test='finish']").click()
   
    successful_message = page.locator("[data-test='complete-text']")
    expect(successful_message).to_have_text("Your order has been dispatched, and will arrive just as fast as the pony can get there!")