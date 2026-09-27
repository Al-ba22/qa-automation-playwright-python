import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.fixture
def login_page(page: Page):
    page.goto("https://www.saucedemo.com/")
    return LoginPage(page)

@pytest.fixture
def inventory_page(page: Page):
    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
    
    return InventoryPage(page)
