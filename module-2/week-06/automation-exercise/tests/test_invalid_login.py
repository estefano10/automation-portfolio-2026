from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_invalid_login(page: Page):
    login = LoginPage(page)
    login.open()
    login.login("falseemail@gmail.com", "false")
    expect(login.error_message).to_be_visible()