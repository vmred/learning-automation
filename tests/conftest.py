import pytest


class TestCase:
    def __init__(self):
        self._fail = ''

    @property
    def fail(self):
        return self._fail

    def verify(self, *args, reason=''):
        # expects that args[0] == actual value
        # args[1] == expected value

        if len(args) == 1:
            if not args[0]:
                self._fail += 'condition mismatch'
                if reason:
                    self._fail += f', reason: {reason}\n'

        elif args[0] != args[1]:
            self._fail += f'actual value: {args[0]} is not equal to expected: {args[1]}'
            if reason:
                self._fail += f', reason: {reason}\n'

        return self

    def is_failed(self):
        if self.fail:
            pytest.fail(self.fail)


@pytest.fixture
def test_case():
    tc = TestCase()
    yield tc
    tc.is_failed()
