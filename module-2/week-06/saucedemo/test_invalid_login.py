from playwright.sync_api import Page, expect

def test_invalid_credentials(page: Page):
    # 1. ir a la página
    page.goto("https://www.saucedemo.com/")
    # 2. llenar usuario y password con basura que no existe
    page.get_by_placeholder("Username").fill("Estefano")
    page.get_by_placeholder("Password").fill("ADMIN123")
    # 3. click en login
    page.get_by_role("button", name="Login").click()
    # 4. afirmar que aparece el mensaje de error correcto
    error_container = page.locator("[data-test='error']")
    expect(error_container).to_contain_text("Epic sadface: Username and password do not match any user in this service")


def test_locked_out_user(page: Page):
    # 1. ir a la página
    page.goto("https://www.saucedemo.com/")
    # 2. llenar con locked_out_user / secret_sauce
    page.get_by_placeholder("Username").fill("locked_out_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    # 3. click en login
    page.get_by_role("button", name="Login").click()
    # 4. afirmar que aparece el mensaje de bloqueo
    error_container = page.locator("[data-test='error']")
    expect(error_container).to_contain_text("Epic sadface: Sorry, this user has been locked out.")
