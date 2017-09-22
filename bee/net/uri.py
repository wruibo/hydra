"""
    uri
"""
import urllib

from . import http


class _HttpUri:
    def __init__(self, url, params=None, **headers):
        self._url = url
        self._params = params
        self._headers = http.header().merge(**headers)


    @property
    def url(self):
        return self._url

    @property
    def params(self):
        return self._params

    @property
    def headers(self):
        return self._headers

    def get(self, **kwargs):
        url_format_values, params_format_values = kwargs.get('url'), kwargs.get('params')

        url = self.url if url_format_values is None else self.url % url_format_values
        params = self.params if params_format_values is None else self.params % params_format_values

        return http.get(url, params=params, headers=self.headers)

    def post(self, **kwargs):
        url_format_values, params_format_values = kwargs.get('url'), kwargs.get('params')

        url = self.url if url_format_values is None else self.url % url_format_values
        params = self.params if params_format_values is None else self.params % params_format_values

        return http.post(url, params=params, headers=self.headers)

httpuri = _HttpUri
