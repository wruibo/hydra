"""
    fund data from sse
"""
import re, pandas
from . import sites


### fund list ###
def get_funds():
    """

    :return:
    """
    resp = sites.uri_funds.get()

    regex_bonds = re.compile(r'val:\"(?P<code>\d+)\",val2:\"(?P<name>\w+)\",val3:\"(?P<spell>\w+)\"')
    bonds = regex_bonds.findall(resp.text)

    return pandas.DataFrame(bonds, columns=("基金代码", "基金名称", "名称简写"))