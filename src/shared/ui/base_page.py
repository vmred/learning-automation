from selene.conditions import visible
from selene.support.jquery_style_selectors import s

from src.shared.ui import cfg
from src.shared.ui.utils import wait_until_element_not_visible, log, is_element_displayed


class BasePage:

    def __init__(self, url):
        self._url = url
        self.browser = cfg.browser
        self.driver = self.browser.driver()
        self._page_content = None
        self._page_loader = None

    @property
    def page_content(self):
        return s(self._page_content)

    @property
    def page_loader(self):
        return s(self._page_loader)

    def open(self):
        self.browser.open_url(self._url)
        self.wait_until_page_loaded()
        return self

    def wait_until_page_loaded(self):
        self.wait_until_loader_completed()
        if self._page_content:
            self.page_content.should_be(visible)
            log.info(f'{self.__class__.__name__} was loaded')

    def wait_until_loader_completed(self):
        if self._page_loader:
            wait_until_element_not_visible(self.page_loader)

    def is_current_page(self):
        return is_element_displayed(self.page_content, timeout=0.4)
