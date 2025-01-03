import pytest
from playwright.sync_api import Playwright

# rajesh
@pytest.mark.parametrize("uname",[("student"),
                                       # pytest.param("studentt",marks=pytest.mark.xfail),
                                       # pytest.param("studenttt", marks=pytest.mark.xfail)
                                  ] )
@pytest.mark.parametrize("passw",[("Password123"),
                                       # pytest.param("Password123335",marks=pytest.mark.xfail),
                                       # pytest.param("Password12334", marks=pytest.mark.xfail)
                                  ] )
def test_run(playwright: Playwright, uname,passw) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # page.set_default_timeout(15000)
    page.goto("https://practicetestautomation.com/")
    #page.wait_for_load_state("networkidle")
    page.get_by_role("link", name="Practice", exact=True).click()
    page.get_by_role("link", name="Test Login Page").click()
    page.get_by_label("Username").click()
    # page.fill("Username",uname)
    page.get_by_label("Username").fill(uname)
    page.get_by_label("Username").press("Tab")
    page.get_by_label("Password").fill(passw)
    page.get_by_role("button", name="Submit").click()
    page.get_by_role("link", name="Log out").click()
    #page.pause()
    print("shallow")
    # page.set_default_timeout(15000)

    # ---------------------
    context.close()
    browser.close()



# with sync_playwright() as playwright:
#     run(playwright)