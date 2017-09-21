"""
    sites of sina
"""
from bee import net


### bond data uri ###
uri_bond_count = net.uri.httpuri(
    url = "http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeStockCount?node=%s"
)


### fund data uri ###
uri_fund_count = net.uri.httpuri(
    url = "http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getFundNetCount?node=%s"
)


### stock data uri ###
uri_stock_count = net.uri.httpuri(
    url = "http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeStockCount?node=%s"
)


uri_stock_count_shangzheng_a = net.uri.httpuri(
    url = "http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeStockCount?node=sh_a"
)


uri_stock_count_shangzheng_b = net.uri.httpuri(
    url = "http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeStockCount?node=sh_b"
)


uri_stock_count_shenzheng_a = net.uri.httpuri(
    url = "http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeStockCount?node=sz_a"
)


uri_stock_count_shenzheng_b = net.uri.httpuri(
    url = "http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeStockCount?node=sz_b"
)


uri_stock_count_hushen_a = net.uri.httpuri(
    url = "http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeStockCount?node=hs_a"
)


uri_stock_count_hushen_b = net.uri.httpuri(
    url = "http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeStockCount?node=hs_b"
)


uri_stock_quotes_today_all = net.uri.httpuri(
    url="http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?page=4&num=80&sort=symbol&asc=1&node=hs_a&symbol=&_s_r_a=page#"
)