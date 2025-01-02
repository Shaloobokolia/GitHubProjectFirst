import re
from playwright.sync_api import Playwright, sync_playwright, expect

# rajesh
def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(15000)
    page.goto("https://practicetestautomation.com/")
    #page.wait_for_load_state("networkidle")
    page.get_by_role("link", name="Practice", exact=True).click()
    page.get_by_role("link", name="Test Login Page").click()
    page.get_by_label("Username").click()
    page.get_by_label("Username").fill("student")
    page.get_by_label("Username").press("Tab")
    page.get_by_label("Password").fill("Password123")
    page.get_by_role("button", name="Submit").click()
    page.get_by_role("link", name="Log out").click()
    #page.pause()
    print("shaloo")
    page.set_default_timeout(15000)

    # ---------------------
    context.close()
    browser.close()


