from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
import re

def test_valid_login(page: Page, credentials):
    login = LoginPage(page)
    login.open()
    email, password = credentials
    login.login(email, password)
    url_pattern = re.compile(r".*automationexercise\.com.*")
    expect(page).to_have_url(url_pattern)
