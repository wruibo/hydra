"""
    bound data
"""
from . import sites


_china_hushen_bond = sites.ApiNode("getHQNodeStockCount", "getHQNodeData", "hs_z")
_china_shanghai_bond = sites.ApiNode("getHQNodeStockCount", "getHQNodeData", "sh_z")
_china_shenzhen_bond = sites.ApiNode("getHQNodeStockCount", "getHQNodeData", "sz_z")
_china_hushen_cbond = sites.ApiNode("getHQNodeStockCount", "getHQNodeData", "hskzz_z")


def get_china_bonds_count_hushen():
    return sites.get_market_center_count(_china_hushen_bond)


def get_china_bonds_count_shanghai():
    return sites.get_market_center_count(_china_shanghai_bond)


def get_china_bonds_count_shenzhen():
    return sites.get_market_center_count(_china_shenzhen_bond)


def get_china_cbonds_count_hushen():
    return sites.get_market_center_count(_china_hushen_cbond)


def get_china_bonds_quote_current_hushen(interval=sites.default_interval):
    return sites.get_market_center_data(_china_hushen_cbond, interval)


def get_china_bonds_quote_current_shanghai(interval=sites.default_interval):
    return sites.get_market_center_data(_china_shanghai_bond, interval)


def get_china_bonds_quote_current_shenzhen(interval=sites.default_interval):
    return sites.get_market_center_data(_china_shenzhen_bond, interval)


def get_china_cbonds_quote_current_hushen(interval=sites.default_interval):
    return sites.get_market_center_data(_china_hushen_cbond, interval)
