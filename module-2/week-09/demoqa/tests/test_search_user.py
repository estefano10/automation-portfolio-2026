from playwright.sync_api import Page, expect
from pages.webtables_page import WebTablesPage

def test_search_user(page: Page):
    web_tables = WebTablesPage(page)
    web_tables.open()
    web_tables.add_record("Estefano", "Gigena", "example@gmail.com", "29", "5000", "Testing")
    web_tables.search("example@gmail.com")
    row = web_tables.get_row("example@gmail.com")
    expect(row).to_have_count(1)
    another_row = web_tables.get_row("cierra@example.com")
    expect(another_row).to_have_count(0)