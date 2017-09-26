"""
    bound data
"""
import re, pandas
from . import sites


def get_china_bonds_count(type):
    """
        get bond count in specified type("hs_z"|"sh_z"|"sz_z"|"hskzz_z")
    :param type:
    :return:
    """
    resp = sites.uri_china_bonds_count.format(params=type).get()

    regex_count = re.compile(r'\"(?P<count>\d+)\"')
    result = regex_count.search(resp.text)
    count = int(result.group(1))

    return count


def get_china_bonds_count_hushen():
    return get_china_bonds_count("hs_z")


def get_china_bonds_count_shanghai():
    return get_china_bonds_count("sh_z")


def get_china_bonds_count_shenzhen():
    return get_china_bonds_count("sz_z")


def get_china_bonds_count_hushen_kzz():
    return get_china_bonds_count("hskzz_z")


def get_china_bounds_quote_current(type="hs_z", interval=sites.interval):
    """
        get china bounds current quote
    :param type:
    :param interval:
    :return:
    """
    import bee, math, time

    # how many data pages
    record_per_page = 80
    total_record = get_china_bonds_count(type)
    total_page = math.ceil(total_record/record_per_page)

    # get data of each page
    record_key = ['code', 'name', 'trade', 'pricechange', 'changepercent', 'buy', 'sell', 'settlement', 'open', 'high', 'low', 'volume', 'amount', 'ticktime']
    quotes_key = ["债券代码", "债券名称", "当前价", "涨跌额", "涨跌幅", "买入价", "卖出价", "收盘价", "开盘价", "最高价", "最低价", "成交量", "成交额", "当前时间"]
    quotes = [quotes_key]
    for page in range(1, total_page+1):
        resp = sites.uri_china_bonds_quote_current.get(url=(record_per_page, page, type))
        records = bee.util.jsexpr.parse(resp.text)
        for record in records:
            quote = [record[key] for key in record_key]
            quotes.append(quote)

        time.sleep(interval)

    # quotes result
    return pandas.DataFrame(quotes, columns=quotes_key)


def get_china_bonds_quote_current_hushen(interval=sites.interval):
    return get_china_bounds_quote_current("hs_z", interval)


def get_china_bonds_quote_current_shanghai(interval=sites.interval):
    return get_china_bounds_quote_current("sh_z", interval)


def get_china_bonds_quote_current_shenzhen(interval=sites.interval):
    return get_china_bounds_quote_current("sz_z", interval)


def get_china_bonds_quote_current_hushen_kzz(interval=sites.interval):
    return get_china_bounds_quote_current("hskzz_z", interval)