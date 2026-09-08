from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_invalid_credentials(page: Page):
    login = LoginPage(page)
    login.open()
    login.login("Estefano", "ADMIN123")
    expect(login.error_container).to_contain_text("Epic sadface: Username and password do not match any user in this service")


def test_locked_out_user(page: Page):
    login = LoginPage(page)
    login.open()
    login.login("locked_out_user", "secret_sauce")
    expect(login.error_container).to_contain_text("Epic sadface: Sorry, this user has been locked out.")