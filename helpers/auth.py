from pages.login_page import LoginPage
from pages.home_page import HomePage

def login(page, base_url, email, password):
    login_page = LoginPage(page)
    home_page = HomePage(page)

    login_page.load(base_url)
    login_page.login(email, password)
    home_page.verify_home_loaded()
