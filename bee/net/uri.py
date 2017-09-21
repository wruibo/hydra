"""
    uri
"""
import urllib

from . import http


class _Uri:
    def __init__(self, url):
        p = urllib.parse.urlsplit(url)
        self._scheme = p.scheme
        self._netloc = p.netloc
        self._path = p.path
        self._params = p.query
        self._fragment = p.fragment

    @property
    def scheme(self):
        return self._scheme

    @property
    def netloc(self):
        return self._netloc

    @property
    def path(self):
        return self._path

    @property
    def params(self):
        return self._params

    @property
    def fragment(self):
        return self._fragment

    def format(self, **kwargs):
        netloc_values = kwargs.get("netloc")
        if netloc_values is not None:
            self._netloc = self.netloc % netloc_values

        path_values = kwargs.get("path")
        if path_values is not None:
            self._path = self.path % path_values

        params_values = kwargs.get("params")
        if params_values is not None:
            self._params = self.params % params_values

        fragment_values = kwargs.get("fragment")
        if fragment_values is not None:
            self._fragment = self.fragment % fragment_values

        return self


class _HttpUri(_Uri):
    def __init__(self, url, host=None, referer=None, cookie=None):
        _Uri.__init__(self, url)

        self._headers = http.header.empty()
        if host is not None: self._headers.host(host)
        if referer is not None: self._headers.referer(referer)
        if cookie is not None: self._headers.cookie(cookie)

    @property
    def get_url(self):
        return urllib.parse.urlunsplit((self.scheme, self.netloc, self.path, self.params, self.fragment))

    @property
    def post_url(self):
        return urllib.parse.urlunsplit((self.scheme, self.netloc, self.path, "", ""))

    @property
    def post_params(self):
        return "%s#%s" % (self.params, self.fragment) if self.fragment != "" else self.params

    def get(self, **kwargs):
        return http.get(self.get_url, headers=self._headers, **kwargs)

    def post(self, **kwargs):
        return http.post(self.post_url, params=self.post_params, headers=self._headers, **kwargs)


httpuri = _HttpUri


if __name__ == "__main__":
    resp = httpuri("http://www.baidu.com/").get()
    print(resp.text)