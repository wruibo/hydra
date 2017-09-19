"""
    task for spider
"""
from . import net


class Task:
    def run(self):
        """
            run the task
        :return:
        """
        pass


class HttpGetTask(Task):
    def __init__(self, url, params=None, cookie=None):
        """

        :param url:
        :param params:
        """
        self._request = rqst.HttpRequest("GET", url, params)

    def run(self):
        """

        :return:
        """
        r = net.http.client.get(self.url)


class HttpPostTask(Task):
    def __init__(self, url, params=None, cookie=None):
        """

        :param url:
        :param params:
        :param cookie:
        """
        pass

    def run(self):
        pass

