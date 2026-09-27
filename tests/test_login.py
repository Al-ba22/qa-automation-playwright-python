import pytest
from playwright.sync_api import Page, expect
def test_successful_login(login_page: Page):
    login_page.get_by_placeholder("Username").fill("standard_user")
    login_page.get_by_placeholder("Password").fill("secret_sauce")
    login_page.get_by_role("button", name="Login").click()

    expect(login_page).to_have_url("https://www.saucedemo.com/inventory.html")

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

def test_login_error(login_page: Page, username, password, expected_error):
    login_page.get_by_placeholder("Username").fill(username)
    login_page.get_by_placeholder("Password").fill(password)
    login_page.get_by_role("button", name="Login").click()
    expect(login_page.get_by_role("alert")).to_contain_text(expected_error)
