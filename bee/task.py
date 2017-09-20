"""
    task for spider
"""
from . import net


class _Task:
    def run(self):
        """
            run the task
        :return:
        """
        pass


class _HttpTask(_Task):
    def __init__(self, url, params=None, **kwargs):
        self._url = url
        self._params = params
        self._kwargs = kwargs

    @property
    def url(self):
        return self._url

    @property
    def params(self):
        return self._params

    @property
    def kwargs(self):
        return self._kwargs


class _HttpGetTask(_HttpTask):
    def __init__(self, url, params=None, **kwargs):
        super(_HttpGetTask, self).__init__(url, params, **kwargs)

    def run(self):
        return net.http.client.get(self.url, self.params, **self.kwargs)


class _HttpPostTask(_HttpTask):
    def __init__(self, url, params=None, **kwargs):
        super(_HttpPostTask, self).__init__(url, params, **kwargs)

    def run(self):
        return net.http.client.post(self.url, self.params, **self.kwargs)


def http_get(url, params, **kwargs):
    return _HttpGetTask(url, params, **kwargs)


def http_post(url, params, **kwargs):
    return _HttpPostTask(url, params, **kwargs)
