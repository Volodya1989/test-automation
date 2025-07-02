from pages.home_page import HomePage
from configs.config import BASE_URL

def test_user_lands_on_home(auth_page):
    home = HomePage(auth_page)
    home.verify_home_loaded()

