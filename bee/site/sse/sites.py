"""
    sites of sse
"""

class _Protocol:
    http = "http"
    ftp = "ftp"

class _Domain:
    www = "www.sse.com.cn"
    query = "query.sse.com.cn"

class _Path:


class _URI:
    def __init__(self, proto, host, path, params):
        self._proto = proto
        self._host = host
        self._path = path
        self._params = params


sse = {
    "http":{
        "www":{
            "www.sse.com.cn",
        }
        "query":""
    }
}

proto = _Protocol
domain = _Domain
uri = _URI


uri_stock_list = uri(
    proto.http,
    domain.query,
    path.stock
)
