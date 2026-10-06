import pytest

@pytest.fixture(autouse=True)
def block_ads(page: Page):
    # acá registrás tus page.route(...)