from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def load(self, base_url):
        self.page.goto(base_url)

    def login(self, email, password):
        self.page.get_by_role("textbox", name="Email").fill(email)
        self.page.get_by_role("textbox", name="Password").fill(password)
        self.page.wait_for_timeout(500)  # Instead of time.sleep(0.5)
        sign_in_button = self.page.get_by_role("button", name="Sign in")
        expect(sign_in_button).to_be_enabled()
        expect(sign_in_button).to_be_enabled(timeout=5000)
        sign_in_button.click()
