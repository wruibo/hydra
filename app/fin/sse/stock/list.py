import bee


class ListSpider(bee.Spider):
    """
        get the stock list
    """
    def prepare(self):
        """

        :return:
        """
        url = "http://query.sse.com.cn/security/stock/downloadStockListFile.do?csrcCode=&stockCode=&areaName=&stockType=1"

        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Mobile Safari/537.36",
            "Host": "www.sse.com.cn",
            "Referer": "http://www.sse.com.cn/",
        }

        self.feed(bee.job.http.get(url, None, headers=headers))

    def process(self, resp):
        """

        :param resp:
        :return:
        """
        pass


if __name__ == "__main__":
    s = ListSpider()

    s.start()

    s.stop()

