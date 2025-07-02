# Sample UI test
import time
from playwright.sync_api import expect
from configs.config import BASE_URL


def test_login(context):
    page = context
    page.goto(BASE_URL)
    page.get_by_role("textbox", name="Email").fill("test@123.com")
    page.get_by_role("textbox", name="Password").fill("123456")
    page.wait_for_timeout(500)  # Instead of time.sleep(0.5)
    sign_in_button =page.get_by_role("button", name="Sign in")
    expect(sign_in_button).to_be_enabled()
    expect(sign_in_button).to_be_enabled(timeout=5000)
    sign_in_button.click()

    heading = page.get_by_text("Best Sellers Books")
    username = page.get_by_role("button", name="Vol")
    expect(heading).to_be_visible()
    expect(username).to_be_visible()
    # ---------------------
    page.close()
