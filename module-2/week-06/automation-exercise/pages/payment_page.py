from pages.base_page import BasePage
from playwright.sync_api import Page

class PaymentPage(BasePage):
    PATH = "/payment"
    def __init__(self, page: Page):
        super().__init__(page)
        self.name_on_card_input = page.locator("[data-qa='name-on-card']")
        self.card_number_input = page.locator("[data-qa='card-number']")
        self.cvc_input = page.locator("[data-qa='cvc']")
        self.card_expiration_input = page.locator("[data-qa='expiry-month']")
        self.card_year_expiration_input = page.locator("[data-qa='expiry-year']")
        self.pay_and_confirm_order_button = page.locator("[data-qa='pay-button']")

    def fill_payment(self):
        self.name_on_card_input.fill("Estefano")
        self.card_number_input.fill("4111111111111111")
        self.cvc_input.fill("311")
        self.card_expiration_input.fill("09")
        self.card_year_expiration_input.fill("2030")
        self.pay_and_confirm_order_button.click()
