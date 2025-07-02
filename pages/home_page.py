from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page: Page):
        self.page = page

    def verify_home_loaded(self):
        expect(self.page.get_by_text("Best Sellers Books")).to_be_visible()
        expect(self.page.get_by_role("button", name="Vol")).to_be_visible()
