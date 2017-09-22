"""
    bound data
"""
import re
from . import sites


def get_china_bonds_count(market):
    """
        get bond count in specified market("hs_z"|"sh_z"|"sz_z"|"hskzz_z")
    :param market:
    :return:
    """
    resp = sites.uri_china_bonds_count.format(params=market).get()

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
