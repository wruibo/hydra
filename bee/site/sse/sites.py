"""
    sites of sse
"""
from bee import net


### all securities ###
uri_securities = net.uri.httpuri(
    url = "http://www.sse.com.cn/js/common/ssesuggestdataAll.js",
)


### bond sites ###
uri_bonds_enterprise = net.uri.httpuri(
    url = "http://www.sse.com.cn/js/common/ssesuggestEbonddata.js",
)

uri_bonds_national = net.uri.httpuri(
    url = "http://www.sse.com.cn/js/common/ssesuggestTbonddata.js"
)

### fund sites ###
uri_funds = net.uri.httpuri(
    url = "http://www.sse.com.cn/js/common/ssesuggestfunddata.js"
)


### stock sites ###
uri_stocks = net.uri.httpuri(
    url = "http://www.sse.com.cn/js/common/ssesuggestdata.js"
)

uri_stocks_listed_a = net.uri.httpuri(
    url = "http://query.sse.com.cn/security/stock/downloadStockListFile.do?csrcCode=&stockCode=&areaName=&stockType=1",
    host = "query.sse.com.cn",
    referer="http://www.sse.com.cn/assortment/stock/list/share/"
)

uri_stocks_listed_b = net.uri.httpuri(
    url = "http://query.sse.com.cn/security/stock/downloadStockListFile.do?csrcCode=&stockCode=&areaName=&stockType=2",
    host = "query.sse.com.cn",
    referer="http://www.sse.com.cn/assortment/stock/list/share/"
)

uri_stocks_waiting = net.uri.httpuri(
    url = "http://query.sse.com.cn/security/stock/downloadStockListFile.do?csrcCode=&stockCode=&areaName=&stockType=3",
    host = "query.sse.com.cn",
    referer="http://www.sse.com.cn/assortment/stock/list/firstissue/"
)

uri_stocks_paused = net.uri.httpuri(
    url = "http://query.sse.com.cn/security/stock/downloadStockListFile.do?csrcCode=&stockCode=&areaName=&stockType=4",
    host = "query.sse.com.cn",
    referer="http://www.sse.com.cn/assortment/stock/list/delisting/"
)

uri_stocks_terminated = net.uri.httpuri(
    url = "http://query.sse.com.cn/security/stock/downloadStockListFile.do?csrcCode=&stockCode=&areaName=&stockType=5",
    host = "query.sse.com.cn",
    referer="http://www.sse.com.cn/assortment/stock/list/delisting/"
)

