from playwright.sync_api import Page, expect
from pages.webtables_page import WebTablesPage

def test_delete_user(page: Page):
    web_tables = WebTablesPage(page)
    web_tables.open()
    web_tables.add_record("Estefano", "Gigena", "example@gmail.com", "29", "5000", "Testing")
    row = web_tables.get_row("example@gmail.com")
    expect(row).to_have_count(1)
    web_tables.delete_record("example@gmail.com")
    expect(row).to_have_count(0)