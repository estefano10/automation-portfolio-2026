from playwright.sync_api import Page

class SignupPage:
    def __init__(self, page: Page):
        self.page = page
        self.name_box = page.locator("[data-qa='signup-name']")
        self.signup_email_box = page.locator("[data-qa='signup-email']")
        self.signup_button = page.locator("[data-qa='signup-button']")
        self.error_message = page.get_by_text("Email Address already exist!")

    def open(self):
        self.page.goto("https://automationexercise.com/login")

    def signup(self, name, email):
        self.name_box.fill(name)
        self.signup_email_box.fill(email)
        self.signup_button.click()