"""
    fund data
"""
import re, pandas
from . import sites


class SinaMarketCenterNodes:
    open_fund = "open_fund"
    close_fund = "close_fund"
    money_fund = "money_fund"
    etf_jz_fund = "etf_jz_fund"
    etf_hq_fund = "etf_hq_fund"
    lof_hq_fund = "lof_hq_fund"
    jjycjz = "jjycjz"


class SinaMarketApiMethods:
    pass


def get_china_funds_count(type):
    """
        get fund count by it's type("open_fund|close_fund|money_fund|")
    :param type: str, fund's type code
    :return: int
    """
    resp = sites.uri_china_funds_count.format(params=type).get()

    regex_count = re.compile(r'\"(?P<count>\d+)\"')
    result = regex_count.search(resp.text)
    count = int(result.group(1))

    return count


def get_china_funds_count_open():
    return get_china_funds_count("open_fund")


def get_china_funds_count_close():
    return get_china_funds_count("close_fund")


def get_china_funds_count_money():
    return get_china_funds_count("money_fund")


def get_china_funds_nav_current(type, interval=sites.interval):
    import bee, math, time

    # how many data pages
    record_per_page = 80
    total_record = get_china_funds_count(type)
    total_page = math.ceil(total_record/record_per_page)

    # get data of each page
    navs, columns = [], None
    for page in range(1, total_page+1):
        resp = sites.uri_china_funds_nav.get(url=(record_per_page, page, type))
        records = bee.util.jsexpr.parse(resp.text)
        for record in records:
            if columns is None:
                columns = list(record.keys())
            nav = [record[key] for key in columns]
            navs.append(nav)

        time.sleep(interval)

    # quotes result
    return pandas.DataFrame(navs, columns=columns)


def get_china_funds_nav_current_open(interval = sites.interval):
    return get_china_funds_nav_current("open_fund", interval)


def get_china_funds_nav_current_money(interval = sites.interval):
    return get_china_funds_nav_current("money_fund", interval)


def get_china_funds_nav_current_etf(interval = sites.interval):
    return get_china_funds_nav_current("etf_jz_fund", interval)


def get_china_funds_nav_current_lof(interval = sites.interval):
    return get_china_funds_nav_current("lof_hq_fund", interval)