from selene.elements import SeleneElement
from selene.support import by
from selene.support.jquery_style_selectors import s


class ChildElement:
    def __init__(self, element):
        self.element = element

    def __call__(self, *args, **kwargs) -> SeleneElement:
        return self.element


class ParentElement:
    def __init__(self, locator):
        self._locator = locator

    @property
    def locator(self):
        return self._locator

    def __call__(self, *args, **kwargs):
        return [s(self._locator), s(by.xpath(self._locator))][self._locator.startswith('(')]
