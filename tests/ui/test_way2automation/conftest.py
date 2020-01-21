import pytest

from src.services.way2automation.forms.registration import RegistrationForm
from src.services.way2automation.pages.droppable_page import DroppablePage
from src.services.way2automation.pages.home_page import HomePage
from src.shared.ui.utils import wait_until_element_is_visible, log, wait_until_element_not_visible, \
    is_element_displayed


@pytest.fixture
def home_page():
    return HomePage()


@pytest.fixture(scope='session', autouse=True)
def login():
    HomePage().open()
    rf = RegistrationForm()
    log.info('waiting until registration form is opened')
    wait_until_element_is_visible(rf.form)
    log.info('registration form is opened')
    rf.login()
    wait_until_element_not_visible(rf.login_form, timeout=4)


@pytest.fixture
def droppable_page(home_page):
    dp = DroppablePage()

    if not is_element_displayed(dp.page_content, timeout=0):
        home_page.droppable_page_link.click()

    return dp
