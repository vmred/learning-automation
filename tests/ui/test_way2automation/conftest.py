import pytest

from src.services.way2automation.forms.registration import RegistrationForm
from src.services.way2automation.pages.home_page import HomePage
from src.shared.ui.utils import wait_until_element_is_visible, log, wait, wait_until_element_not_visible


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
