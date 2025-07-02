from pages.home_page import HomePage

def test_user_lands_on_home(auth_page):
    page = auth_page
    home = HomePage(page)
    home.verify_home_loaded()
