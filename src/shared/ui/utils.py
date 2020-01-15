import logging
import string
from random import random
import time

from selene.support.conditions import be
from selene.support.conditions.be import visible
from selene.support.jquery_style_selectors import s, ss

from src.shared.ui.cfg import browser
from src.shared.ui.cfg import timeout as tm

log = logging.getLogger()

not_clickable_overlays = [
    'break-all gray-hover'
]


def wait(seconds):
    time.sleep(seconds)


def remove_focus_from_element(element):
    browser.execute_script(f'document.querySelector("{element}").blur();')


def js_ready():
    return browser.execute_script('return document.readyState == "complete"')


def _is_element_or_locator(element_or_locator, is_collection=False):
    if type(element_or_locator) is str:
        return s(element_or_locator) if not is_collection else ss(element_or_locator)


def _is_selene_element_or_webelement(element):
    if 'SeleneElement' in str(type(element)):
        element = element.get_actual_webelement()
    return element


def wait_until_element_not_visible(element, is_collection=False, timeout=tm):
    _is_element_or_locator(element, is_collection).should_not_be(visible, timeout)


def wait_until_element_is_visible(element, is_collection=False, timeout=tm):
    _is_element_or_locator(element, is_collection).should_be(visible, timeout)


def is_element_is_present(element, is_collection=False, timeout=tm):
    return _is_element_or_locator(element, is_collection).assure(be.in_dom, timeout)


def scroll_to_element_to_be_in_view(element):
    browser.execute_script('arguments[0].scrollIntoView({"block":"center"});',
                           _is_selene_element_or_webelement(element))


def get_all_element_attributes(element):
    return browser.execute_script(
        'var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) {'
        ' items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value '
        '}; '
        'return items;', _is_selene_element_or_webelement(element))


def element_is_clickable(element):
    attrs = get_all_element_attributes(element)
    return not any(x in not_clickable_overlays for x in attrs.values())


def random_string(string_size=20):
    return ''.join(random.choice(string.ascii_letters) for _ in range(string_size))
