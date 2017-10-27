import time, lxml.html.soupparser
import webbrowser as wb

from . import sites


def get_dom_text(dom, path):
    tmpdom = dom.xpath(path)
    if len(tmpdom) > 0:
        return tmpdom[0].text.strip()
    return None


def get_dom_property(dom, path, property):
    tmpdom = dom.xpath(path)
    if len(tmpdom) > 0:
        return tmpdom[0].attrib.get(property)
    return None


def get_p2p_list():
    """
        get all p2p product list
    :return:
    """
    # remove <textarea> content for html parse problem
    chtml = sites.uri_p2p_list.get().text

    # get dom nodes of product items
    itemdoms = lxml.html.soupparser.fromstring(chtml, features="lxml").xpath('//li[@class="product-rows-item"]')

    products = []
    # parse each product
    for dom in itemdoms:
        product = {}
        product['产品名称'] = get_dom_text(dom, 'a[@class="product-title"]')

        key = get_dom_text(dom, 'ul/li[@class="interest-rate"]/span[@class="product-property-name"]')
        value = get_dom_text(dom, 'ul/li[@class="interest-rate"]/p')
        product[key] = value

        key = get_dom_text(dom, 'ul/li[@class="invest-period"]/span[@class="product-property-name"]')
        value = get_dom_text(dom, 'ul/li[@class="invest-period"]/p')
        product[key] = value

        key = get_dom_text(dom, 'ul/li[@class="collection-mode"]/span[@class="product-property-name"]')
        value = get_dom_text(dom, 'ul/li[@class="collection-mode"]/p')
        product[key] = value

        key = get_dom_text(dom, 'ul/li[@class="investment-amount"]/span[@class="product-property-name"]')
        value = get_dom_text(dom, 'ul/li[@class="investment-amount"]/p/span')
        product[key] = value

        product['进度'] = get_dom_text(dom, 'ul//span[@class="progress-txt"]')
        product['状态'] = get_dom_text(dom, 'ul/div/span')

        path = get_dom_property(dom, 'ul//a', 'href')
        product['url'] = "https://www.lup2p.com%s" % path if path is not None else None

        products.append(product)

    return products


def get_transfer_p2p_list():
    """
        get transfer p2p list
    :return:
    """
    # get html content
    chtml = sites.uri_transfer_p2p_list.get().text

    # get dom nodes of product items
    itemdoms = lxml.html.soupparser.fromstring(chtml, features="lxml").xpath('//ul[@data-sk="p2p-transfer-list"]')

    products = []
    #parse each product
    for dom in itemdoms:
        product = {}
        product['产品名称'] = get_dom_text(dom, 'li/dl/dt[@class="product-name"]/a')

        key = get_dom_text(dom, 'li/dl/dd//li[@class="interest-rate"]/span[@class="product-property-name"]')
        value = get_dom_text(dom, 'li/dl/dd//li[@class="interest-rate"]/p')
        product[key] = value

        key = get_dom_text(dom, 'li/dl/dd//li[@class="invest-period"]/span[@class="product-property-name"]')
        value = get_dom_text(dom, 'li/dl/dd//li[@class="invest-period"]/p')
        product[key] = value

        key = get_dom_text(dom, 'li/dl/dd//li[@class="product-value"]/span[@class="product-property-name"]')
        value = get_dom_text(dom, 'li/dl/dd//li[@class="product-value"]/p/span')
        product[key] = value

        key = get_dom_text(dom, 'li/dl/dd//li[@class="product-depreciation"]/span[@class="product-property-name"]')
        value = get_dom_text(dom, 'li/dl/dd//li[@class="product-depreciation"]/p')
        product[key] = value

        key = get_dom_text(dom, 'li/div[@class="product-amount"]/span')
        value = get_dom_text(dom, 'li/div[@class="product-amount"]/p/em')
        product[key] = value

        product['状态'] = get_dom_text(dom, 'li/div[@class="product-status"]/a')

        path = get_dom_property(dom, 'li/div[@class="product-status"]/a', 'href')
        product['url'] = "https://www.lup2p.com%s" % path if path is not None else None

        products.append(product)

    return products


def open_p2p_invest_page():
    """
        open page if there is an invest p2p project
    :return:
    """
    histories = []
    while True:
        products = get_p2p_list()
        for product in products:
            url = product['url']
            if product['状态'] == '投资' and url not in histories:
                print(url)
                wb.open(url)
                histories.append(url)

        print("next trip...")
        time.sleep(2)


def open_transfer_p2p_invest_page():
    """
        open page if there is an transfer p2p project
    :return:
    """
    histories = []
    while True:
        products = get_transfer_p2p_list()
        for product in products:
            url = product['url']
            if product['状态'] == '投资' and url not in histories:
                print(url)
                wb.open(url)
                histories.append(url)

        print("next trip...")
        time.sleep(1)
