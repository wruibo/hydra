"""
    model for http
"""
import collections
from bee import util

hkey = collections.namedtuple('hkey',['agent', 'accept', 'encoding', 'connection', 'host', 'referer', 'cookie']) \
                             ('User-Agent', 'Accept', 'Accept-Encoding', 'Connection', 'Host', 'Referer', 'Cookie')


class _Header(util.dict.CaseInsensitiveDict):

    def __init__(self):
        super(_Header, self).__init__(
            {
                hkey.agent: "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Mobile Safari/537.36",
                hkey.accept: "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                hkey.encoding: "gzip, deflate",
                hkey.connection: "keep-alive"
            }
        )

    def agent(self, agent):
        if agent is None:
            return self.get(hkey.agent)
        else:
            self[hkey.agent] = agent
        return self

    def accept(self, accept):
        if accept is None:
            return self.get(hkey.accept, None)
        else:
            self[hkey.accept] = accept
        return self

    def cookie(self, cookie):
        if cookie is None:
            return self.get(hkey.cookie, None)
        else:
            self[hkey.cookie] = cookie
        return self

    def host(self, host):
        if host is None:
            return self.get(hkey.host)
        else:
            self[hkey.host] = host
        return self

    def referer(self, referer):
        if referer is None:
            return self.get(hkey.referer)
        else:
            self[hkey.referer] = referer
        return self

    def merge(self, seq={}, **kwargs):
        self.update(seq, **kwargs)
        return self


class _Request:
    def __init__(self, url, params=None):
        self._url = url
        self._params = params

    @staticmethod
    def create(url, params=None):
        """
            create a new request object
        :param url:
        :param params:
        :return:
        """
        return _Request(url, params)

    @property
    def url(self):
        return self._url

    @property
    def params(self):
        return self._params


class _Response:
    def __init__(self, resp):
        self._resp = resp

    @property
    def ok(self):
        return self._resp.ok

    @property
    def code(self):
        return self._resp.status_code

    @property
    def message(self):
        return self._resp.reason

    @property
    def content(self):
        return self._resp.content

    @property
    def text(self):
        return self._resp.text

    @property
    def json(self):
        return self._resp.json()

header = _Header
request = _Request
response = _Response
