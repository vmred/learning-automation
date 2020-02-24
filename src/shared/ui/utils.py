import logging
import string
from random import random
import time

from selene.support.conditions import be, have
from selene.support.jquery_style_selectors import s, ss
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains

from src.shared.ui.cfg import browser
from src.shared.ui.cfg import timeout as tm
from tests.ui.conftest import driver

log = logging.getLogger()

not_clickable_overlays = [
    'break-all gray-hover'
]


def wait(seconds):
    time.sleep(seconds)


def remove_focus_from_element(element):
    browser.execute_script(f'document.querySelector("{element}").blur();')


def js_ready():
    return browser.wait_to(have.js_returned_true('return document.readyState == "complete"'))


def _is_element_or_locator(element_or_locator, is_collection=False):
    if type(element_or_locator) is str:
        func = ss if is_collection else s
        return func(element_or_locator)
    return element_or_locator


def is_element_displayed(element, timeout=4):
    try:
        element.should(be.visible, timeout=timeout)
        return True
    except (NoSuchElementException, TimeoutException):
        return False


def _is_selene_element_or_webelement(element):
    if 'SeleneElement' in str(type(element)):
        element = element.get_actual_webelement()
    return element


def wait_until_element_not_visible(element, is_collection=False, timeout=tm):
    _is_element_or_locator(element, is_collection).should_not(be.visible, timeout)


def wait_until_element_is_visible(element, is_collection=False, timeout=tm):
    _is_element_or_locator(element, is_collection).should(be.visible, timeout)


def is_element_is_present(element, is_collection=False, timeout=tm):
    return _is_element_or_locator(element, is_collection).assure(be.in_dom, timeout)


def scroll_to_element_to_be_in_view(element):
    browser.execute_script('arguments[0].scrollIntoView({"block":"center"});',
                           _is_selene_element_or_webelement(element))


def get_element_attributes(element):
    return browser.execute_script(
        'var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) {'
        ' items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value '
        '}; '
        'return items;', _is_selene_element_or_webelement(element))


def switch_to_frame(frame):
    driver.switch_to_frame(frame.get_actual_webelement())


def drag_n_drop(element, drag_to):
    actions = ActionChains(driver)
    if type(drag_to) == list:
        actions.drag_and_drop_by_offset(element.get_actual_webelement(), drag_to[0], drag_to[1]).perform()
    else:
        actions.drag_and_drop(element.get_actual_webelement(), drag_to.get_actual_webelement()).perform()


def element_is_clickable(element):
    attrs = get_element_attributes(element)
    return not any(x in not_clickable_overlays for x in attrs.values())


def random_string(string_size=20):
    return ''.join(random.choice(string.ascii_letters) for _ in range(string_size))
