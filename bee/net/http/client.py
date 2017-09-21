"""
    http based remote data access
"""
import requests as _requests

from . import model


class _Client:
    def __init__(self, headers):
        self._headers = headers

    def request(self, method, url, **kwargs):
        self._update_headers(**kwargs)
        resp = _requests.request(method, url, **kwargs)
        return model.response(resp)

    def get(self, url, params=None, **kwargs):
        self._update_headers(**kwargs)
        resp = _requests.get(url, params, **kwargs)
        return model.response(resp)

    def post(self, url, params=None, **kwargs):
        self._update_headers(**kwargs)
        resp = _requests.post(url, params, None, **kwargs)
        return model.response(resp)

    def _update_headers(self, **kwargs):
        if kwargs.get("headers") is None:
            kwargs["headers"] = self._headers
        else:
            kwargs["headers"].merge(self._headers)


class _ChromeClient:
    pc = _Client(model.header.default().agent("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"))
    mobile = _Client(model.header.default().agent("Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Mobile Safari/537.36"))

# default client
default = _ChromeClient
# chrome client
chrome = _ChromeClient

# global client
_global_http_client = default.pc


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
