"""
    model for http
"""
from bee import util


_default_header = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Mobile Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive"
}


class _Header(util.dict.CaseInsensitiveDict):
    def __init__(self, seq={}, **kwargs):
        super(_Header, self).__init__(seq, **kwargs)

    @staticmethod
    def empty():
        return _Header()

    @staticmethod
    def default():
        return _Header(_default_header)

    def is_empty(self):
        return len(self) == 0

    def agent(self, agent):
        if agent is None:
            return self.get("User-Agent")
        else:
            self["User-Agent"] = agent
        return self

    def accept(self, accept):
        if accept is None:
            return self.get("Accept", None)
        else:
            self["Accept"] = accept
        return self

    def cookie(self, cookie):
        if cookie is None:
            return self.get("Cookie", None)
        else:
            self["Cookie"] = cookie
        return self

    def host(self, host):
        if host is None:
            return self.get("Host")
        else:
            self["Host"] = host
        return self

    def referer(self, referer):
        if referer is None:
            return self.get("Referer")
        else:
            self["Referer"] = referer
        return self

    def merge(self, seq=None, **kwargs):
        if seq is None:
            seq = {}

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


class _HeaderVendor:
    empty = _Header.empty()

    default_pc = _Header.default().agent("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36")
    default_mobile = _Header.default().agent("Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Mobile Safari/537.36")

    chrome_pc = _Header.default().agent("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36")
    chrome_mobile = _Header.default().agent("Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Mobile Safari/537.36")

header =_HeaderVendor
request = _Request
response = _Response
