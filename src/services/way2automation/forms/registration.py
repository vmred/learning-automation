from selene.support.jquery_style_selectors import s

from variables import way2automation


class RegistrationForm:
    def __init__(self):
        self._form = 'div[id="load_box"]'

    @property
    def form(self):
        return self._form

    login_link = s('a[href="#login"]')
    login_form = s('div[id="login"]')
    username_field = s('div[id="login"] > form input[name="username"]')
    password_field = s('div[id="login"] > form input[name="password"]')
    submit_button = s('div[id="login"] > form input[type="submit"]')

    def login(self):
        self.login_link.click()
        self.username_field.type(way2automation['username'])
        self.password_field.type(way2automation['password'])
        self.submit_button.click()
