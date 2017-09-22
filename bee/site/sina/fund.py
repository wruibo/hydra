"""
    fund data
"""
import re
from . import sites


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


