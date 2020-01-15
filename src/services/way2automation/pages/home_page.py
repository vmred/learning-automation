from src.shared.ui.base_page import BasePage
from variables import way2automation


class HomePage(BasePage):
    def __init__(self):
        super().__init__(way2automation['base_url'])
        self._page_content = 'div[class="container margin-top-20"]'
