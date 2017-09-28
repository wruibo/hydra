"""
    get stock data
"""
from . import sites

_china_hushen_stock_a = sites.ApiNode("getHQNodeStockCount", "getHQNodeData", "hs_a")
_china_hushen_stock_b = sites.ApiNode("getHQNodeStockCount", "getHQNodeData", "hs_b")
_china_shanghai_stock_a = sites.ApiNode("getHQNodeStockCount", "getHQNodeData", "sh_a")
_china_shanghai_stock_b = sites.ApiNode("getHQNodeStockCount", "getHQNodeData", "sh_b")
_china_shenzhen_stock_a = sites.ApiNode("getHQNodeStockCount", "getHQNodeData", "sz_a")
_china_shenzhen_stock_b = sites.ApiNode("getHQNodeStockCount", "getHQNodeData", "sz_b")
_china_cyb_stock = sites.ApiNode("getHQNodeStockCount", "getHQNodeData", "cyb")

_hongkong_all_stock = sites.ApiNode("getHKStockCount", "getHKStockData", "qbgg_hk")


def get_china_stocks_count_hushen_a():
    return sites.get_market_center_count(_china_hushen_stock_a)


def get_china_stocks_count_hushen_b():
    return sites.get_market_center_count(_china_hushen_stock_b)


def get_china_stocks_count_shanghai_a():
    return sites.get_market_center_count(_china_shanghai_stock_a)


def get_china_stocks_count_shanghai_b():
    return sites.get_market_center_count(_china_shanghai_stock_b)


def get_china_stocks_count_shenzhen_a():
    return sites.get_market_center_count(_china_shenzhen_stock_a)


def get_china_stocks_count_shenzhen_b():
    return sites.get_market_center_count(_china_shenzhen_stock_b)


def get_china_stocks_count_cyb():
    return sites.get_market_center_count(_china_cyb_stock)


def get_china_stocks_quote_hushen_a():
    return sites.get_market_center_data(_china_hushen_stock_a)


def get_china_stocks_quote_hushen_b():
    return sites.get_market_center_data(_china_hushen_stock_b)


def get_china_stocks_quote_shanghai_a():
    return sites.get_market_center_data(_china_shanghai_stock_a)


def get_china_stocks_quote_shanghai_b():
    return sites.get_market_center_data(_china_shanghai_stock_b)


def get_china_stocks_quote_shenzhen_a():
    return sites.get_market_center_data(_china_shenzhen_stock_a)


def get_china_stocks_quote_shenzhen_b():
    return sites.get_market_center_data(_china_shenzhen_stock_b)


def get_china_stocks_quote_cyb():
    return sites.get_market_center_data(_china_cyb_stock)


def get_hongkong_stocks_count_all():
    return sites.get_market_center_count(_hongkong_all_stock)


def get_hongkong_stocks_quote_all():
    return sites.get_market_center_data(_hongkong_all_stock)
