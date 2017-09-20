"""
    stock relate data from sse
"""
import io, sites, pandas


def get_stock_list_listed_a():
    """
        get stock list of shanghai stock exchange
    :return:
    """
    resp = sites.uri_stock_list_listed_a.get()
    return pandas.read_csv(io.StringIO(resp.text), sep="\s+")


def get_stock_list_listed_b():
    """
        get stock list of shanghai stock exchange
    :return:
    """
    resp = sites.uri_stock_list_listed_b.get()
    return pandas.read_csv(io.StringIO(resp.text), sep="\s+")


def get_stock_list_waiting():
    """
        get ipo stock list of shanghai stock exchange
    :return:
    """
    resp = sites.uri_stock_list_waiting.get()
    return pandas.read_csv(io.StringIO(resp.text), sep="\s+")


def get_stock_list_paused():
    """
        get ipo stock list of shanghai stock exchange
    :return:
    """
    resp = sites.uri_stock_list_paused.get()
    return pandas.read_csv(io.StringIO(resp.text), sep="\s+")


def get_stock_list_terminated():
    """
        get ipo stock list of shanghai stock exchange
    :return:
    """
    resp = sites.uri_stock_list_terminated.get()
    return pandas.read_csv(io.StringIO(resp.text), sep="\s+")

if __name__ == "__main__":
    print(get_stock_list_listed_a())
    print(get_stock_list_listed_b())
    print(get_stock_list_waiting())
    print(get_stock_list_paused())
    print(get_stock_list_terminated())