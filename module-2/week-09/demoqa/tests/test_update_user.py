from playwright.sync_api import Page, expect
from pages.webtables_page import WebTablesPage

def test_update_user(page: Page):
    web_tables = WebTablesPage(page)
    web_tables.open()
    web_tables.add_record("Estefano", "Gigena", "example@gmail.com", "29", "5000", "Testing")
    web_tables.edit_record("example@gmail.com", "Morita","Gigena", "example@gmail.com", "5", "5000", "Testing" )
    row = web_tables.get_row("example@gmail.com")
    cells = row.locator("td")
    expect(cells.nth(0)).to_have_text("Morita")
    expect(cells.nth(2)).to_have_text("5")