"""
    task for spider
"""


class Task:
    def __init__(self):
        pass

    def run(self):
        pass


class HttpTask(Task):
    def __init__(self, method, url, data, json, params=None, platform=None):
        self._method = method

        self._url = url
        self._params = params

        self._data = data
        self._json = json

        self._platform = platform


class HttpGetTask(HttpTask):
    def run(self):
        pass


class HttpPostTask(HttpTask):
    def run(self):
        pass

