from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def load(self, base_url):
        self.page.goto(base_url)

    def login(self, email, password):
        self.page.get_by_role("textbox", name="Email").fill(email)
        self.page.get_by_role("textbox", name="Password").fill(password)
        self.page.locator("body").click()  # blur trigger
        button = self.page.get_by_role("button", name="Sign in")
        expect(button).to_be_enabled(timeout=5000)
        button.click()
