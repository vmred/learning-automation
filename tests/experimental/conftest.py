from src.shared.logger import log


def execute_on_retry(exc):
    log.info('executing on retry here')
    return isinstance(exc, Exception)
