"""
    http based remote data access
"""
import requests as _requests

from . import model


class _Client:
    def __init__(self, headers):
        self._headers = headers

    def request(self, method, url, **kwargs):
        if kwargs.get("headers") is None:
            kwargs["headers"] = self._headers
        resp = _requests.request(method, url, **kwargs)
        return model.response(resp)

    def get(self, url, params=None, **kwargs):
        if kwargs.get("headers") is None:
            kwargs["headers"] = self._headers
        resp = _requests.get(url, params, **kwargs)
        return model.response(resp)

    def post(self, url, params=None, **kwargs):
        if kwargs.get("headers") is None:
            kwargs["headers"] = self._headers
        resp = _requests.post(url, params, None, **kwargs)
        return model.response(resp)


class _ChromeClient:
    pc = _Client(model.header.chrome.pc)
    mobile = _Client(model.header.chrome.mobile)

# chrome client
chrome = _ChromeClient

# global client
_global_http_client = chrome.pc


def use(client):
    """
        set the global http client
    :param client:
    :return:
    """
    if not isinstance(client, _Client):
        raise ValueError("input client must be an instance of _Client")
    global _global_http_client
    _global_http_client = client


def request(method, url, **kwargs):
    return _global_http_client.request(method, url, **kwargs)


def get(url, params=None, **kwargs):
    return _global_http_client.get(url, params, **kwargs)


def post(url, params=None, **kwargs):
    return _global_http_client.post(url, params, **kwargs)
