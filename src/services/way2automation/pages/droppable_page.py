from selene.support.jquery_style_selectors import s, ss

from src.shared.ui.base_page import BasePage
from variables import way2automation


class DroppablePage(BasePage):
    def __init__(self):
        super().__init__(f'{way2automation["hostname"]}{way2automation["droppable_page"]}')
        self._page_content = '//h1[contains(text(), "Droppable")]'

    tabs = ss('.responsive-tabs > li')

    draggable_elements = ss('div[id="draggable"]')
    droppable_elements = ss('div[id="droppable"]')

    default_tab = tabs[0]
    default_functionality_frame = s('iframe[src="droppable/default.html"]')
    default_tab_draggable = draggable_elements[0]
    default_tab_droppable = droppable_elements[0]
    accept_tab_draggable = draggable_elements[1]
    accept_tab_draggable_invalid = s('div[id="draggable-nonvalid"]')
    accept_tab_droppable = droppable_elements[1]
    accept_tab = tabs[1]
