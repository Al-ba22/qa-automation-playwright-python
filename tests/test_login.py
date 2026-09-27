import pytest
from playwright.sync_api import Page, expect
def test_successful_login(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

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

def test_login_error(page: Page, username, password, expected_error):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill(username)
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("alert")).to_contain_text(expected_error)
