import json

import requests

from src.shared.logger import log


def log_call(func):
    def wrapper(url, *args, **kwargs):
        response = func(url, *args, **kwargs)
        log.info(f'sending {func.__name__.upper()}, url: {response.url}')
        if 'json' in kwargs.keys():
            log.info(f'sending data: {kwargs["json"]}')
        log.info(f'status code: {response.status_code}')
        response_data = format_response_data(response)
        log.info(f'response data: {response_data}')
        return response, response_data

    return wrapper


def format_response_data(response):
    if response.headers and 'content-type' in response.headers.keys():
        content_type = response.headers['content-type']

        if 'text' in content_type:
            return response.content

        if 'application/json' in content_type:
            return json.loads(response.content)

    # unknown response data format, returning as is
    return response.content


class API:
    def __init__(self, hostname, port):
        self._hostname = hostname
        self._port = port
        self._cookies = {}
        self._headers = {}

    def _get_api_url(self):
        return f'{self.hostname}:{self._port}/api'

    @property
    def hostname(self):
        return self._hostname

    def add_headers(self, header, value):
        self._headers[header] = value

    @property
    def headers(self):
        return self._headers

    def set_cookies(self, cookies):
        self._cookies = cookies

    def add_cookies(self, cookie, value):
        self._cookies[cookie] = value

    @property
    def cookies(self):
        return self._cookies

    @staticmethod
    def _update_kwargs(kwargs, key, value):
        if key in kwargs.keys():
            kwargs[key].update(value)
        else:
            kwargs[key] = value
        return kwargs

    @log_call
    def post(self, url, *args, **kwargs):
        kwargs = self._update_kwargs(kwargs, 'headers', self.headers)
        return requests.post(f'{self._get_api_url()}{url}', *args, **kwargs)

    @log_call
    def get(self, url, *args, **kwargs):
        kwargs = self._update_kwargs(kwargs, 'headers', self.headers)
        return requests.get(f'{self._get_api_url()}{url}', *args, **kwargs)
