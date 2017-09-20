"""
    sites of sse
"""
from bee import net

uri_stock_list_listed_a = net.uri.httpuri(
    url = "http://query.sse.com.cn/security/stock/downloadStockListFile.do?csrcCode=&stockCode=&areaName=&stockType=1",
    host = "query.sse.com.cn",
    referer="http://www.sse.com.cn/assortment/stock/list/share/"
)

uri_stock_list_listed_b = net.uri.httpuri(
    url = "http://query.sse.com.cn/security/stock/downloadStockListFile.do?csrcCode=&stockCode=&areaName=&stockType=2",
    host = "query.sse.com.cn",
    referer="http://www.sse.com.cn/assortment/stock/list/share/"
)

uri_stock_list_waiting = net.uri.httpuri(
    url = "http://query.sse.com.cn/security/stock/downloadStockListFile.do?csrcCode=&stockCode=&areaName=&stockType=3",
    host = "query.sse.com.cn",
    referer="http://www.sse.com.cn/assortment/stock/list/firstissue/"
)

uri_stock_list_paused = net.uri.httpuri(
    url = "http://query.sse.com.cn/security/stock/downloadStockListFile.do?csrcCode=&stockCode=&areaName=&stockType=4",
    host = "query.sse.com.cn",
    referer="http://www.sse.com.cn/assortment/stock/list/delisting/"
)

uri_stock_list_terminated = net.uri.httpuri(
    url = "http://query.sse.com.cn/security/stock/downloadStockListFile.do?csrcCode=&stockCode=&areaName=&stockType=5",
    host = "query.sse.com.cn",
    referer="http://www.sse.com.cn/assortment/stock/list/delisting/"
)
