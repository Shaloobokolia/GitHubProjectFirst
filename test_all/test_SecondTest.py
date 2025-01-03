from playwright.sync_api import Playwright
import pytest

# rajesh

def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # page.set_default_timeout(15000)
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

    # page.set_default_timeout(15000)

    # ---------------------
    context.close()
    browser.close()

@pytest.mark.skip(reason='not ready')
def test_runagain(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
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
    print("shallow")
    page.set_default_timeout(15000)

    # ---------------------
    context.close()
    browser.close()


# with sync_playwright() as playwright:
#     run(playwright)