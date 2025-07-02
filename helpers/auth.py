import time

def login(page, base_url, email, password):
    page.goto(base_url)
    page.get_by_role("textbox", name="Email").fill(email)
    page.get_by_role("textbox", name="Password").fill(password)
    time.sleep(.6)
    page.get_by_role("button", name="Sign in").click()
    page.wait_for_url("**/books-store/**")
