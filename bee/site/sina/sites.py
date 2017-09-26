"""
    sites of sina
"""
from bee import net


interval = 1

### china bond data uri ###
uri_china_bonds_count = net.uri.httpuri(
    url = "http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeStockCount?node=%s"
)


uri_china_bonds_quote_current = net.uri.httpuri(
    url = "http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?sort=symbol&asc=1&symbol=&_s_r_a=page&num=%d&page=%d&node=%s#"
)

### china fund data uri ###
uri_china_funds_count = net.uri.httpuri(
    url = "http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getNameCount?node=%s"
)


uri_china_funds_nav = net.uri.httpuri(
    url = "http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getFundNetData?sort=symbol&asc=1&symbol=&_s_r_a=page&num=%d&page=%d&node=%s#"
)


### china stock data uri ###
uri_china_stocks_count = net.uri.httpuri(
    url = "http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeStockCount?node=%s"
)


uri_china_stocks_quote_current = net.uri.httpuri(
    url = "http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?sort=symbol&asc=1&symbol=&_s_r_a=page&num=%d&page=%d&node=%s#"
)

### hongkong stock data uri ###
uri_hongkong_stocks_count = net.uri.httpuri(
    url = "http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHKStockCount?node=%s"
)

uri_hongkong_stocks_quote_current = net.uri.httpuri(
    url = "http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHKStockData?sort=symbol&asc=1&symbol=&_s_r_a=page&num=%d&page=%d&node=%s#"
)
