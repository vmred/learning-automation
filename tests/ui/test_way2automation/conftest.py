import pytest

from src.services.way2automation.forms.registration import RegistrationForm
from src.services.way2automation.pages.droppable_page import DroppablePage
from src.services.way2automation.pages.home_page import HomePage
from src.shared.ui.utils import wait_until_element_is_visible, log, get_element_attributes


@pytest.fixture
def home_page():
    return HomePage().open()


@pytest.fixture(scope='session', autouse=True)
def login():
    HomePage().open()
    rf = RegistrationForm()
    log.info('waiting until registration form is opened')
    wait_until_element_is_visible(rf.form)
    log.info('registration form is opened')
    rf.login()


@pytest.fixture
def droppable_page(home_page):
    home_page.droppable_page_link.click()
    return DroppablePage()


@pytest.fixture
def accept_tab_droppable_page(droppable_page):
    droppable_page.driver.refresh()
    droppable_page.accept_tab.click()

    return DroppablePage()
