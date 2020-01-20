from selene.support.jquery_style_selectors import s

from src.shared.ui.base_page import BasePage
from variables import way2automation


class DroppablePage(BasePage):
    def __init__(self):
        super().__init__(f'{way2automation["hostname"]}{way2automation["droppable_page"]}')
        self._page_content = '//h1[contains(text(), "Droppable")]'

    default_functionality_tab = s('//li[a[@href="#example-1-tab-1"]]')
    accept_tab = s('//li[a[@href="#example-1-tab-2"]]')
