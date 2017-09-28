"""
    sites of sina
"""
import re, collections
from bee import net


uri_market_center_count = net.uri.httpuri(
    url="http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.%s?node=%s"
)


uri_market_center_data = net.uri.httpuri(
    url = "http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.%s?sort=symbol&asc=1&symbol=&_s_r_a=page&num=%d&page=%d&node=%s#"
)


ApiNode = collections.namedtuple("ApiNode", ("count", "data", "node"))


def get_market_center_count(api_node):
    """
        get records count of data in market center with specified <api> and <node>
    :param api: str, api name
    :param node: str, node name
    :return: int, records count
    """
    resp = uri_market_center_count.get(url=(api_node.count, api_node.node))

    regex_count = re.compile(r'\"(?P<count>\d+)\"')
    result = regex_count.search(resp.text)
    count = int(result.group(1))

    return count


default_interval = 0.5 # default interval for access next page for data


def get_market_center_data(api_node, interval=default_interval):
    """
        get records of data in market center with specified <api> and <node>
    :param api_node: ApiNode, api node in market center
    :param interval: float, interval for access next page for data
    :return: array
    """
    import bee, math, time

    # how many data pages
    record_per_page = 80
    total_record = get_market_center_count(api_node)
    total_page = math.ceil(total_record / record_per_page)

    # get data of each page
    data, columns = [], None
    for page in range(1, total_page + 1):
        resp = uri_market_center_data.get(url=(api_node.data, record_per_page, page, api_node.node))
        records = bee.util.jsexpr.parse(resp.text)
        for record in records:
            if columns is None:
                columns = list(record.keys())
                data.append(columns)
            else:
                data.append([record[key] for key in columns])

        time.sleep(interval)

    # quotes result
    return data


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
