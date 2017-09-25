"""
    get stock data
"""
import re, pandas
from . import sites


def get_china_stocks_count(type="hs_a"):
    """
        get stock count by specified type("hs_a"|"hs_b"|"sh_a"|"sh_b"|"sz_a"|"sz_b")
    hs_a: A stock count listed in ShangHai and ShenZhen exchange
    hs_b: B stock count listed in ShangHai and ShenZhen exchange
    sh_a: A stock count listed in ShangHai exchange
    sh_b: B stock count listed in ShangHai exchange
    sz_a: A stock count listed in ShenZhen exchange
    sz_b: B stock count listed in ShenZhen exchange
    :param type: str, type code
    :return: int
    """
    resp = sites.uri_stocks_count.get(url=(type))

    regex_count = re.compile(r'\"(?P<count>\d+)\"')
    result = regex_count.search(resp.text)
    count = int(result.group(1))

    return count


def get_china_stocks_count_total():
    """
        stock count of hushen A
    :return:
    """
    return get_china_stocks_count("hs_a")


def get_china_stocks_count_hushen_b():
    """
        stock count of huhen B
    :return:
    """
    return get_china_stocks_count("hs_b")


def get_china_stocks_count_shanghai_a():
    """
        stock count of shangzheng A
    :return:
    """
    return get_china_stocks_count("sh_a")


def get_china_stocks_count_shanghai_b():
    """
        stock count of shangzheng B
    :return:
    """
    return get_china_stocks_count("sh_b")


def get_china_stocks_count_shenzhen_a():
    """
        stock count of shenzheng A
    :return:
    """
    return get_china_stocks_count("sz_a")


def get_china_stocks_count_shenzhen_b():
    """
        stock count of shenzheng B
    :return:
    """
    return get_china_stocks_count("sz_b")


def get_china_stocks_count_cyb():
    """
        stock count of shenzheng growth enterprises market
    :return:
    """
    return get_china_stocks_count("cyb")


def get_china_stocks_quote_current(type="hs_a", interval=sites.interval):
    """
        get stock
    :param type:
    :return:
    """
    import bee, math, time

    # how many data pages
    record_per_page = 80
    total_record = get_china_stocks_count_total()
    total_page = math.ceil(total_record/record_per_page)

    # get data of each page
    record_key = ['code', 'name', 'trade', 'pricechange', 'changepercent', 'buy', 'sell', 'settlement', 'open', 'high', 'low', 'volume', 'amount', 'turnoverratio', 'per', 'pb', 'mktcap', 'nmc','ticktime']
    quotes_key = ["证券代码", "证券名称", "当前价", "涨跌额", "涨跌幅", "买入价", "卖出价", "收盘价", "开盘价", "最高价", "最低价", "成交量", "成交额", "换手率", "市盈率", "市净率", "总市值", "流通市值", "当前时间"]
    quotes = [quotes_key]
    for page in range(1, total_page+1):
        resp = sites.uri_china_stocks_quote_current.get(url=(record_per_page, page, type))
        records = bee.util.jsexpr.parse(resp.text)
        for record in records:
            quote = [record[key] for key in record_key]
            quotes.append(quote)

        time.sleep(interval)

    # quotes result
    return pandas.DataFrame(quotes, columns=quotes_key)


def get_hongkong_stocks_count(type="qbgg_hk"):
    """
        get stock count by specified type("hs_a"|"hs_b"|"sh_a"|"sh_b"|"sz_a"|"sz_b")
    hs_a: A stock count listed in ShangHai and ShenZhen exchange
    hs_b: B stock count listed in ShangHai and ShenZhen exchange
    sh_a: A stock count listed in ShangHai exchange
    sh_b: B stock count listed in ShangHai exchange
    sz_a: A stock count listed in ShenZhen exchange
    sz_b: B stock count listed in ShenZhen exchange
    :param type: str, type code
    :return: int
    """
    resp = sites.uri_hongkong_stocks_count.get(url=(type))

    regex_count = re.compile(r'\"(?P<count>\d+)\"')
    result = regex_count.search(resp.text)
    count = int(result.group(1))

    return count


def get_hongkong_stocks_count_total():
    return get_hongkong_stocks_count("qbgg_hk")


def get_hongkong_stocks_quote_current(type="qbgg_hk", interval=sites.interval):
    """
        get stock
    :param type:
    :return:
    """
    import bee, math, time

    # how many data pages
    record_per_page = 80
    total_record = get_hongkong_stocks_count_total()
    total_page = math.ceil(total_record/record_per_page)

    # get data of each page
    record_key = ['symbol', 'name', 'lasttrade', 'pricechange', 'changepercent', 'buy', 'sell', 'prevclose', 'open', 'high', 'low', 'volume', 'amount', 'eps', 'dividend', 'stocks_sum', 'ticktime']
    quotes_key = ["证券代码", "证券名称", "当前价", "涨跌额", "涨跌幅", "买入价", "卖出价", "收盘价", "开盘价", "最高价", "最低价", "成交量", "成交额", "每股盈利", "股息", "总股本", "当前时间"]
    quotes = [quotes_key]
    for page in range(1, total_page+1):
        resp = sites.uri_hongkong_stocks_quote_current.get(url=(record_per_page, page, type))
        records = bee.util.jsexpr.parse(resp.text)
        for record in records:
            quote = [record[key] for key in record_key]
            quotes.append(quote)

        time.sleep(interval)

    # quotes result
    return pandas.DataFrame(quotes, columns=quotes_key)
