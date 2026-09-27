import pytest
from pages.login_page import LoginPage
from playwright.sync_api import expect
def test_successful_login(login_page: LoginPage):
    login_page.login("standard_user", "secret_sauce")

    expect(login_page.page).to_have_url("https://www.saucedemo.com/inventory.html")

@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        (
            "wrong_user",
            "wrong_password",
            "Username and password do not match",
        ),
        (
            "locked_out_user",
            "secret_sauce",
            "Sorry, this user has been locked out.",
        ),
    ],
)

def test_login_error(
    login_page: LoginPage, 
    username, 
    password, 
    expected_error
    ):
    login_page.login(username, password)

    expect(login_page.error_message).to_contain_text(expected_error)
