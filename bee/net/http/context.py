# request headers for sse
default_header = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Mobile Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    'Connection': 'keep-alive',
    "Host": "www.cninfo.com.cn",
    "Referer": "http://www.cninfo.com.cn/cninfo-new/index",
}


class Header(dict):
    @staticmethod
    def default():
        return Header({
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Mobile Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
        }
        )

    @property
    def accept(self):
        return self.get("Accept", None)

    @accept.setter
    def accept(self, accept):
        self["Accept"] = accept

    @property
    def cookie(self):
        return self.get("Cookie", None)

    @cookie.setter
    def cookie(self, cookie):
        self["Cookie"] = cookie
