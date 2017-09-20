import bee, pandas, io


class ListSpider(bee.Spider):
    """
        get the stock list
    """
    def prepare(self):
        """

        :return:
        """
        url = "http://query.sse.com.cn/security/stock/downloadStockListFile.do?csrcCode=&stockCode=&areaName=&stockType=1"

        host = "query.sse.com.cn"
        referer = "http://www.sse.com.cn/assortment/stock/list/share/"

        headers = bee.net.http.header.default.pc.host(host).referer(referer)

        self.feed(bee.task.http_get(url, None, headers=headers))

    def process(self, resp):
        """

        :param resp:
        :return:
        """
        stocks = pandas.read_csv(io.StringIO(resp.text), sep="\s+")
        print(stocks)


if __name__ == "__main__":
    s = ListSpider()

    s.start()

    s.stop()
