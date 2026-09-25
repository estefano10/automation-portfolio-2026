import pytest
from pages.login_page import LoginPage
from dotenv import load_dotenv
import os

load_dotenv()

@pytest.fixture
def credentials():
    email = os.environ['AE_EMAIL']
    password = os.environ['AE_PASSWORD']
    return (email, password)

@pytest.fixture
def logged_in_page(page, credentials):
    login = LoginPage(page)
    login.open()
    email, password = credentials
    login.login(email, password)
    yield page
