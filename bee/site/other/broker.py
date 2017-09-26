"""
    broker data
"""
import re, time, pandas
from . import sites


def get_securities_broker_servers(interval=sites.interval):
    """
        get broker servers
    :return:
    """
    # get all securities
    resp = sites.uri_securities_broker_servers.get()
    regex_names = re.compile(r'href=\"(?P<name>\w+)\.htm\"')
    names = regex_names.findall(resp.content.decode("gb2312"))

    # get servers for each broker
    all_servers = []
    for name in names:
        try:
            # get servers for current broker
            path = "%s.htm" % name if name != "中信建投" else "%s.files/sheet001.htm" % name
            resp = sites.uri_securities_broker_servers.join(path).get()

            # parse server address
            regex_servers = re.compile(r'(?P<server>[^>]+):(?P<ip>[.\d]+):(?P<port>\d+)')
            servers = regex_servers.findall(resp.content.decode("gb2312"))
            for server, ip, port in servers:
                all_servers.append([name, server, ip, port])
        except:
            pass
        # sleep for a while
        time.sleep(interval)

    return pandas.DataFrame(all_servers, columns=["券商名称", "服务器名", "IP", "Port"])


def get_securities_broker_departments(interval=sites.interval):
    """
        get broker departments
    :param interval:
    :return:
    """
    resp = sites.uri_securities_broker_servers.get()
    regex_names = re.compile(r'href=\"(?P<name>\w+)\.htm\"')
    names = regex_names.findall(resp.content.decode("gb2312"))

    # get departments for each broker
    all_depts = []
    for name in names:
        try:
            # get departments for current broker
            path = "%s.htm" % name if name != "中信建投" else "%s.files/sheet001.htm" % name
            resp = sites.uri_securities_broker_servers.join(path).get()

            # parse departments
            regex_depts = re.compile(r'>(?P<code>\d+)\s+(?P<dept>[^<]+)<')
            depts = regex_depts.findall(resp.content.decode("gb2312"))
            for code, dept in depts:
                all_depts.append([name, dept, code])
        except:
            pass
        # sleep for a while
        time.sleep(interval)

    return pandas.DataFrame(all_depts, columns=["券商名称", "营业部名称", "营业部代码"])
