"""
    http based remote data access
"""
import requests as _requests


class Core:
    def __init__(self):
        self._headers = {
            "Accept":"text/html, application/xhtml+xml, application/xml; q=0.9, image/webp, */*; q=0.8",
            "Accept-Encoding":"gzip, deflate"
        }

    def get(self, url, params=None, **kwargs):
        return _requests.get(url, params, **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        return _requests.post(url, data, json, **kwargs)


class Chrome(Core):
    def __init__(self):
        self._context = None

    @staticmethod
    def mobile():
        pass

    @staticmethod
    def default():
        pass

    def get(self, url, params=None, **kwargs):
        return _requests.get(url, params, **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        return _requests.post(url, data, json, **kwargs)




def get(url, params=None, **kwargs):
    return _requests.get(url, params, **kwargs)


def post(url, data=None, json=None, **kwargs):
    return _requests.post(url, data, json, **kwargs)

