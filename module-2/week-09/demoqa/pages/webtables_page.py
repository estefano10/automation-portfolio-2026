from pages.base_page import BasePage
from playwright.sync_api import Page

class WebTablesPage(BasePage):
    PATH = "/webtables"
    def __init__(self, page: Page):
        super().__init__(page)
        self.add_button = page.locator("#addNewRecordButton")
        self.first_name = page.locator("#firstName")
        self.last_name = page.locator("#lastName")
        self.user_email = page.locator("#userEmail")
        self.user_age = page.locator("#age")
        self.user_salary = page.locator("#salary")
        self.department = page.locator("#department")
        self.form_submit_button = page.locator("#submit")
        self.search_box = page.locator("#searchBox")
        self.table_content = page.locator(".table")

    def _fill_and_submit_form(self, name: str, lastname: str, email: str, age: str, salary: str, department: str):
        self.first_name.fill(name)
        self.last_name.fill(lastname)
        self.user_email.fill(email)
        self.user_age.fill(age)
        self.user_salary.fill(salary)
        self.department.fill(department)
        self.form_submit_button.click()


    def add_record(self, name: str, lastname: str, email: str, age: str, salary: str, department: str):
        self.add_button.click()
        self._fill_and_submit_form(name, lastname, email, age, salary, department)


    def search(self, text: str):
        self.search_box.fill(text)

    def get_row(self, email: str):
        return self.page.locator("tr").filter(has_text=email)

    def edit_record(self, email: str, name: str, lastname: str, edited_email: str, age: str, salary: str, department: str):
        row = self.get_row(email)
        row.locator("[title='Edit']").click()
        self._fill_and_submit_form(name, lastname, edited_email, age, salary, department)


    def delete_record(self, email: str):
        row = self.get_row(email)
        row.locator("[title='Delete']").click()