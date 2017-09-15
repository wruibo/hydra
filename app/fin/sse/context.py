"""
    context for sse web site
"""

# request headers for sse
_access_headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Mobile Safari/537.36",
    "Host": "www.cninfo.com.cn",
    "Referer": "http://www.cninfo.com.cn/cninfo-new/index",
}


def headers():
    return _access_headers
