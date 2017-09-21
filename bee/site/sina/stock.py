"""
    get stock data
"""
import re
from . import sites


def get_stock_count(market="hs_a"):
    """

    :return:
    """
    resp = sites.uri_stock_count.format(params=market).get()

    regex_count = re.compile(r'\"(?P<count>\d+)\"')
    result = regex_count.search(resp.text)
    count = int(result.group(1))

    return count