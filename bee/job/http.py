"""
    http task
"""
from .. import net
from .task import Task


class _HttpGetTask(Task):
    def __init__(self, url, params=None, **kwargs):
        self._url = url
        self._params = params
        self._kwargs = kwargs

    def run(self):
        return net.http.client.get(self._url, self._params, **self._kwargs)


class _HttpPostTask(Task):
    def __init__(self, url, data=None, json=None, **kwargs):
        self._url = url
        self._data = data
        self._json = json
        self._kwargs = kwargs

    def run(self):
        return net.http.client.post(self._url, self._data, self._json, **self._kwargs)


class _DefaultPlatform:
    @staticmethod
    def get(url, params=None, **kwargs):
        return _HttpGetTask(url, params, **kwargs)

    @staticmethod
    def post(url, data=None, json=None, **kwargs):
        return _HttpPostTask(url, data, json, **kwargs)


class _MobilePlatform:
    @staticmethod
    def get(url, params=None, **kwargs):
        return _HttpGetTask(url, params, **kwargs)

    @staticmethod
    def post(url, data=None, json=None, **kwargs):
        return _HttpPostTask(url, data, json, **kwargs)
