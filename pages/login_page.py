class LoginPage:
    def __init__(self, page):
        self.page = page
        self.email_input = page.get_by_role("textbox", name="Email")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.signin_button = page.get_by_role("button", name="Sign in")

    def load(self, base_url):
        self.page.goto(base_url)

    def login(self, email, password):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.signin_button.click()