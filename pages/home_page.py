from playwright.sync_api import expect

class HomePage:
    def __init__(self, page):
        self.page = page
        self.heading = page.get_by_text("Best Sellers Books")
        self.user_button = page.get_by_role("button", name="Vol")

    def verify_home_loaded(self):
        expect(self.heading).to_be_visible()
        expect(self.user_button).to_be_visible()