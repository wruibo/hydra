from . import sites


_china_all_index = sites.ApiNode("getHQNodeStockCount", "getHQNodeData", "hs_s")
_hongkong_hengsheng_index = sites.ApiNode("getNameCount", "getNameList", "zs_hk")


def get_china_index_count_all():
    return sites.get_market_center_count(_china_all_index)


def get_china_index_quote_all(interval = sites.default_interval):
    return sites.get_market_center_data(_china_all_index, interval)


def get_hongkong_index_count_hengsheng():
    return sites.get_market_center_count(_hongkong_hengsheng_index)


def get_hongkong_index_quote_hengsheng(interval = sites.default_interval):
    return sites.get_market_center_data(_hongkong_hengsheng_index, interval)
