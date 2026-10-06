from playwright.sync_api import Page, expect
from pages.webtables_page import WebTablesPage

def test_create_user(page: Page):
    web_tables = WebTablesPage(page)
    web_tables.open()
    web_tables.add_record("Estefano", "Gigena", "example@gmail.com", "29", "5000", "Testing")
    row = web_tables.get_row("example@gmail.com")
    cells = row.locator("td")
    expect(cells.nth(0)).to_contain_text("Estefano")
    expect(cells.nth(1)).to_contain_text("Gigena")
    expect(cells.nth(2)).to_contain_text("29")
    expect(cells.nth(3)).to_contain_text("example@gmail.com")
    expect(cells.nth(4)).to_contain_text("5000")
    expect(cells.nth(5)).to_contain_text("Testing")
