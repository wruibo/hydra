"""
    securities data
"""
import re, pandas
from . import sites


### securities list ###
def get_securities():
    """

    :return:
    """
    resp = sites.uri_securities.get()

    regex_bonds = re.compile(r'val:\"(?P<code>\d+)\",val2:\"(?P<name>\w+)\",val3:\"(?P<spell>\w+)\"')
    bonds = regex_bonds.findall(resp.text)

    return pandas.DataFrame(bonds, columns=("证券代码", "证券名称", "证券简写"))