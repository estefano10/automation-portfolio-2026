from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_box = page.locator("[data-qa='login-email']")
        self.password_box = page.locator("[data-qa='login-password']")
        self.login_button = page.locator("[data-qa='login-button']")

    def open(self):
        self.page.goto("https://automationexercise.com/login")

    def login(self, email: str, password: str):
        self.email_box.fill(email)
        self.password_box.fill(password)
        self.login_button.click()