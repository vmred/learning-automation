from selene.support.jquery_style_selectors import s

from src.shared.ui.base_page import BasePage
from variables import way2automation


class HomePage(BasePage):
    def __init__(self):
        # TODO change url format passing
        super().__init__(f'{way2automation["hostname"]}{way2automation["base_url"]}')
        self._page_content = 'div[class="container margin-top-20"]'

    droppable_page_link = s('div[class*="linkbox"] > ul>  li > a[href*="droppable"]')
