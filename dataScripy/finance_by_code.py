import requests
import requests as req
from bs4 import BeautifulSoup as bs
from lxml import etree


'''
参考文章：
https://zhuanlan.zhihu.com/p/159200115
'''
url = 'http://quotes.money.163.com/f10/lrb_688237.html'
# 模仿浏览器的headers
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
}

resp = req.get(url,headers)
resp.encoding = 'utf-8'
html = resp.text


#解析html
def get_table_from_html(html):
    tree = etree.HTML(html)
    # 寻找所有的table标签
    table_lst = tree.xpath("//table")
    table_data_lst = []
    for table in table_lst:
        table_data_lst.append(get_table(table))

    return table_data_lst

def get_table(table_ele):
    """
    获取table数据
    :param table_ele:
    :return:
    """
    tr_lst = table_ele.xpath(".//tr")
    # 第一行通常来说都是标题
    title_data = get_title(tr_lst[0])
    # 第一行后面都是数据
    data = get_data(tr_lst[1:])

    return {
        'title': title_data,
        'data': data
    }


def get_title(tr_ele):
    """
    获取标题
    标题可能用th 标签，也可能用td标签
    :param tr_ele:
    :return:
    """
    # 先寻找th标签
    title_lst = get_tr_data_by_tag(tr_ele, 'th')
    if not title_lst:
        title_lst = get_tr_data_by_tag(tr_ele, 'td')

    return title_lst

def get_tr_data_by_tag(tr, tag):
    """
    获取一行数据
    :param tr:
    :param tag:
    :return:
    """
    datas = []
    nodes = tr.xpath(".//{tag}".format(tag=tag))
    for node in nodes:
        text = node.xpath('string(.)').strip()
        datas.append(text)

    return datas


def get_data(tr_lst):
    """
    获取数据
    :param tr_lst:
    :return:
    """
    datas = []
    for tr in tr_lst:
        tr_data = get_tr_data_by_tag(tr, 'td')
        datas.append(tr_data)

    return datas

if __name__ == '__main__':
    tree = etree.HTML(html)
    table_list = tree.xpath("//table")
    for table in table_list:
        print(get_table(table))
    print(get_table(table_list[4]).get('data')[32])
    print(get_table(table_list[4]).get('data')[32][4])



