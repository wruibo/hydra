"""
    model for http
"""


class _Request:
    def __init__(self, url, params=None):
        self._url = url
        self._params = params

    @property
    def url(self):
        return self._url

    @property
    def params(self):
        return self._params


class _Response:
    def __init__(self, code, message, content):
        self._code = code
        self._message = message
        self._content = content

    @property
    def code(self):
        return self._code

    @property
    def message(self):
        return self._message

    @property
    def content(self):
        return self._content


def request(url, params=None):
    """
        create a new request object
    :param url:
    :param params:
    :return:
    """
    return _Request(url, params)


def response(code, message, content):
    """
        create a new response object
    :param code:
    :param message:
    :param content:
    :return:
    """
    return _Response(code, message, content)
