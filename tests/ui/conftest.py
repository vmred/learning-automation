import allure
import pytest
from allure.constants import AttachmentType

from src.shared.ui.cfg import browser

driver = browser.driver()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, 'rep_' + rep.when, rep)


@pytest.fixture(scope='function', autouse=True)
def capture_fail(request):
    yield

    if request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            allure.attach(request.function.__name__, driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        elif request.node.rep_call.passed:
            allure.attach(request.function.__name__, driver.get_screenshot_as_png(), type=AttachmentType.PNG)
    elif request.node.rep_setup.failed:
        allure.attach(request.function.__name__, driver.get_screenshot_as_png(), type=AttachmentType.PNG)


@pytest.fixture(scope='session', autouse=True)
def setup(request):
    def teardown():
        driver.quit()

    request.addfinalizer(teardown)
