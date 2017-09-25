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
            resp = sites.uri_securities_broker_servers.join("%s.htm" % name).get()

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
