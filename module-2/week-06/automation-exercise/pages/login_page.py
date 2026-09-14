from playwright.sync_api import Page
from pages.base_page import BasePage

class LoginPage(BasePage):
    PATH = "/login"
    def __init__(self, page: Page):
        super().__init__(page)
        self.email_box = page.locator("[data-qa='login-email']")
        self.password_box = page.locator("[data-qa='login-password']")
        self.login_button = page.locator("[data-qa='login-button']")

    def login(self, email: str, password: str):
        self.email_box.fill(email)
        self.password_box.fill(password)
        self.login_button.click()