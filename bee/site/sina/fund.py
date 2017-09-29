"""
    fund data
"""
from . import sites


_china_open_fund_nav = sites.MarketCenterApiNode("getFundNetCount", "getFundNetData", "open_fund")
_china_money_fund_nav = sites.MarketCenterApiNode("getFundNetCount", "getFundNetData", "money_fund")
_china_etf_fund_nav = sites.MarketCenterApiNode("getFundNetCount", "getFundNetData", "etf_jz_fund")

_china_close_fund_quote = sites.MarketCenterApiNode("getHQNodeStockCountSimple", "getHQNodeDataSimple", "close_fund")
_china_etf_fund_quote = sites.MarketCenterApiNode("getHQNodeStockCountSimple", "getHQNodeDataSimple", "etf_hq_fund")
_china_lof_fund_quote = sites.MarketCenterApiNode("getHQNodeStockCountSimple", "getHQNodeDataSimple", "lof_hq_fund")


def get_china_funds_count_open():
    return sites.get_market_center_count(_china_open_fund_nav)


def get_china_funds_count_money():
    return sites.get_market_center_count(_china_money_fund_nav)


def get_china_funds_count_close():
    return sites.get_market_center_count(_china_close_fund_quote)


def get_china_funds_count_etf():
    return sites.get_market_center_count(_china_etf_fund_quote)


def get_china_funds_count_lof():
    return sites.get_market_center_count(_china_lof_fund_quote)


def get_china_funds_nav_open(interval = sites.default_interval):
    return sites.get_market_center_data(_china_open_fund_nav, interval)


def get_china_funds_nav_money(interval = sites.default_interval):
    return sites.get_market_center_data(_china_money_fund_nav, interval)


def get_china_funds_nav_etf(interval = sites.default_interval):
    return sites.get_market_center_data(_china_etf_fund_nav, interval)


def get_china_funds_quote_etf(interval = sites.default_interval):
    return sites.get_market_center_data(_china_etf_fund_quote, interval)


def get_china_funds_quote_lof(interval = sites.default_interval):
    return sites.get_market_center_data(_china_lof_fund_quote, interval)


def get_china_funds_quote_close(interval = sites.default_interval):
    return sites.get_market_center_data(_china_close_fund_quote, interval)
