from retrying import retry

from tests.experimental.conftest import execute_on_retry


@retry(retry_on_exception=execute_on_retry, stop_max_attempt_number=1)
def test_one():
    assert False
