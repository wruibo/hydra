"""
    http based remote data access
"""
import requests as _requests

from . import model
from . import vendor


class _Client:
    def __init__(self, headers):
        self._headers = headers

    def get(self, url, params=None, headers=None):
        r = _requests.get(url, params, headers=self._headers.merge(headers))
        return model.response(r.status_code, r.reason, r.content)

    def post(self, url, params=None, headers=None):
        r = _requests.post(url, params, None, headers=self._headers.merge(headers))
        return model.response(r.status_code, r.reason, r.content)


class _Chrome:
    @staticmethod
    def default():
        return _Client(vendor.chrome.pc.header())

    @staticmethod
    def mobile():
        return _Client(vendor.chrome.mobile.header())

# chrome client
chrome = _Chrome

# global client
_global_http_client = chrome.default()


def use(client):
    """
        set the global http client
    :param client:
    :return:
    """
    _global_http_client = client


def get(url, params=None, headers=None):
    return _global_http_client.get(url, params, headers)


def post(url, params=None, headers=None):
    return _global_http_client.post(url, params, headers)
