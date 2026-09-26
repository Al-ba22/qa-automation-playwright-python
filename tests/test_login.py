from playwright.sync_api import Page, expect
def test_successful_login(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_invalid_login(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("wrong_user")
    page.get_by_placeholder("Password").fill("wrong_password")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("alert")).to_contain_text(
        "Username and password do not match"
            )