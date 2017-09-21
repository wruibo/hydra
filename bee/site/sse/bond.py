"""
    bond data from sse
"""
import re, pandas
from . import sites


### bond list ###
def get_national_bonds():
    """

    :return:
    """
    resp = sites.uri_bonds_national.get()

    regex_bonds = re.compile(r'val:\"(?P<code>\d+)\",val2:\"(?P<name>\w+)\",val3:\"(?P<spell>\w+)\"')
    bonds = regex_bonds.findall(resp.text)

    return pandas.DataFrame(bonds, columns=("债券代码", "债券名称", "拼音简写"))


def get_enterprise_bonds():
    """

    :return:
    """
    resp = sites.uri_bonds_enterprise.get()

    regex_bonds = re.compile(r'val:\"(?P<code>\d+)\",val2:\"(?P<name>\w+)\",val3:\"(?P<spell>\w+)\"')
    bonds = regex_bonds.findall(resp.text)

    return pandas.DataFrame(bonds, columns=("债券代码", "债券名称", "拼音简写"))

