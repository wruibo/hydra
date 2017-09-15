"""
    http based remote data access
"""
import requests as _requests


def get(url, params=None, **kwargs):
    return _requests.get(url, params, kwargs)


def options(url, **kwargs):
    return _requests.options(url, kwargs)


def head(url, **kwargs):
    return _requests.head(url, kwargs)


def post(url, data=None, json=None, **kwargs):
    return _requests.post(url, data, json, kwargs)


def put(url, data=None, **kwargs):
    return _requests.put(url, data, kwargs)


def patch(url, data=None, **kwargs):
    return _requests.patch(url, data, kwargs)


def delete(url, **kwargs):
    return _requests.delete(url, kwargs)
