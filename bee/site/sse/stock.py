"""
    stock relate data from sse
"""
import re, io, pandas
from . import sites


########### stock list #############
def get_stocks():
    """

    :return:
    """
    resp = sites.uri_stocks.get()

    regex_bonds = re.compile(r'val:\"(?P<code>\d+)\",val2:\"(?P<name>\w+)\",val3:\"(?P<spell>\w+)\"')
    bonds = regex_bonds.findall(resp.text)

    return pandas.DataFrame(bonds, columns=("股票代码", "股票名称", "名称简写"))


def get_stocks_listed_a():
    """
        get A stock list of shanghai stock exchange
    :return:
    """
    resp = sites.uri_stocks_listed_a.get()
    return pandas.read_csv(io.StringIO(resp.text), sep="\s+")


def get_stocks_listed_b():
    """
        get B stock list of shanghai stock exchange
    :return:
    """
    resp = sites.uri_stocks_listed_b.get()
    return pandas.read_csv(io.StringIO(resp.text), sep="\s+")


def get_stocks_waiting():
    """
        get stock list waiting for ipo of shanghai stock exchange
    :return:
    """
    resp = sites.uri_stocks_waiting.get()
    return pandas.read_csv(io.StringIO(resp.text), sep="\s+")


def get_stocks_paused():
    """
        get stock list paused of shanghai stock exchange
    :return:
    """
    resp = sites.uri_stocks_paused.get()
    return pandas.read_csv(io.StringIO(resp.text), sep="\s+")


def get_stocks_terminated():
    """
        get stock list terminated of shanghai stock exchange
    :return:
    """
    resp = sites.uri_stocks_terminated.get()
    return pandas.read_csv(io.StringIO(resp.text), sep="\s+")


########### stock detail #############
def get_stock_detail(code):
    """
        get stock de
    :param code:
    :return:
    """