import os

from selene.support.jquery_style_selectors import s
from selenium.webdriver.common.by import By

from tests.ui.conftest import driver


def get_shadow_root(element):
    return driver.execute_script('return arguments[0].shadowRoot', element.get_actual_webelement())


def get_shadow_element(shadow_root, by, locator):
    return shadow_root.find_element(by, locator)


class TestShadowRoot:
    def test_one(self):
        driver.get(f'file://{os.path.dirname(os.path.abspath(__file__))}/shadow_dom_sample.html')
        shadow_input = 'input#shadowInput'
        shadow_h1 = 'h1#inside'

        shadow_root = get_shadow_root(s('div#element'))

        assert get_shadow_element(shadow_root, By.CSS_SELECTOR, shadow_h1).text == 'Inside Shadow DOM'
        inp = shadow_root.find_element_by_css_selector(shadow_input)
        inp.send_keys(123)
