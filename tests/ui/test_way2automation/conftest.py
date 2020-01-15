import pytest

from src.services.way2automation.pages.home_page import HomePage


@pytest.fixture
def home_page():
    return HomePage().open()
