# Sample UI test
from configs.config import BASE_URL

def test_login(page):
    page.goto(BASE_URL)
    page.fill('#username', 'user')
    page.fill('#password', 'pass')
    page.click('button[type=submit]')
    assert page.url == f'{BASE_URL}/dashboard'
