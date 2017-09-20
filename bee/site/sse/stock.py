"""
    stock relate data from sse
"""
import bee, pandas


def get_stock_list():
    """
        get stock list of shanghai stock exchange
    :return:
    """
    # url address for stock list
    url = "http://query.sse.com.cn/security/stock/downloadStockListFile.do?csrcCode=&stockCode=&areaName=&stockType=1"

