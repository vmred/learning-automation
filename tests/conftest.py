import pytest


class TestCase:
    def __init__(self):
        self._fail = ''

    @property
    def fail(self):
        return self._fail

    def verify(self, actual, expected):
        if actual != expected:
            self._fail += f'Fail! Actual result: {actual} not equal to expected: {expected}'

    def is_failed(self):
        if self.fail:
            pytest.fail(self.fail)


@pytest.fixture
def test_case():
    tc = TestCase()
    yield tc
    tc.is_failed()
