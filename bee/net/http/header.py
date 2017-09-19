"""
    http header model
"""


class CaseInsensitiveDict(dict):
    def __init__(self, seq=None, **kwargs):
        super(CaseInsensitiveDict, self).__init__(seq, **kwargs)

    def __setitem__(self, key, value):
        pkey = key
        if isinstance(key, str):
            pkey = key.lower()

        super(CaseInsensitiveDict, self).__setitem__(pkey, (key, value))

    def __getitem__(self, key):
        pkey = key
        if isinstance(key, str):
            pkey = key.lower()
        return super(CaseInsensitiveDict, self).__getitem__(pkey)[1]


class _Header(CaseInsensitiveDict):
    def __init__(self):
        self["User-Agent"] = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Mobile Safari/537.36"
        self["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
        self["Accept-Encoding"] = "gzip, deflate"
        self["Connection"] = "keep-alive"

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

    def refer(self, refer):
        if refer is None:
            return self.get("Refer")
        else:
            self["Refer"] = refer
        return self

    def merge(self, headers):
        pass


def create():
    return _Header()


if __name__ == "__main__":
    h = create()
    h["Cookie"] = "abc"
    print(h)
    print(h["cOOkie"])