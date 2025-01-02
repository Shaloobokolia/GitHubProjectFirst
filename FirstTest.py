import re
from playwright.sync_api import Playwright, sync_playwright, expect

# rajesh
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://practicetestautomation.com/")
    page.get_by_role("link", name="Practice", exact=True).click()
    page.get_by_role("link", name="Test Login Page").click()
    page.get_by_label("Username").click()
    page.get_by_label("Username").fill("student")
    page.get_by_label("Username").press("Tab")
    page.get_by_label("Password").fill("Password123")
    page.get_by_role("button", name="Submit").click()
    page.get_by_role("link", name="Log out").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
