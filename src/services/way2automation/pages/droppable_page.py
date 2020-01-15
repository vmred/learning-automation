from src.shared.ui.base_page import BasePage
from variables import way2automation


class DroppablePage(BasePage):
    def __init__(self):
        super().__init__(f'{way2automation["hostname"]}{way2automation["droppable_page"]}')
        self._page_content = 'div[class="container margin-top-20"]'
