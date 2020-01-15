import pytest

from src.shared.ui.cfg import browser

driver = browser.driver()


@pytest.fixture(scope='session', autouse=True)
def setup(request):
    def teardown():
        driver.quit()

    request.addfinalizer(teardown)
