from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
import re

def test_valid_login(page: Page):
    login = LoginPage(page)
    login.open()
    login.login("gemelosaramiel15@gmail.com", "morita")
    url_pattern = re.compile(r".*automationexercise\.com.*")
    expect(page).to_have_url(url_pattern)
