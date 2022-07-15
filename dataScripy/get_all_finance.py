import pprint
import requests
from lxml import etree
from bs4 import BeautifulSoup

'''
参考文章：https://developer.51cto.com/article/645408.html
'''


if __name__ == '__main__':
    # url = 'https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/xjllbAjaxNew?companyType=4&reportDateType=0&reportType=1&dates=2022-03-31%2C2021-12-31%2C2021-09-30%2C2021-06-30%2C2021-03-31%2C2020-12-31%&code=SH600887'

    url = 'https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/ZYZBAjaxNew?type=0&code=SZ002475'
    html = requests.get(url)

    print(html.json())