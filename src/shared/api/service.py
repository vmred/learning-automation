from src.shared.api.api import API


class Service(API):
    def __init__(self, hostname, port):
        super().__init__(hostname, port)