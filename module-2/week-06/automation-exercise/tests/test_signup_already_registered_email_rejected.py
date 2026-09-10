from playwright.sync_api import Page, expect
from pages.signup_page import SignupPage

def test_signup_already_registered_email_rejected(page: Page):
    signup = SignupPage(page)
    signup.open()
    signup.signup("Estefano", "gemelosaramiel15@gmail.com")
    expect(signup.error_message).to_be_visible()