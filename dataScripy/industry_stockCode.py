import pandas as pd
from bs4 import BeautifulSoup as bs
import requests



'''
参考文章：https://www.igiftidea.com/article/13214288162.html

'''

'''
新浪获取同行业code ，是申万三级分类
'''
def get_sw_industry_stock_code (code):
    url = f'http://money.finance.sina.com.cn/corp/go.php/vCI_CorpOtherInfo/stockid/{code}.phtml'
    req = requests.get(url)
    html = req.text

    soup = bs(html, 'html')

    id = soup.find(id = 'con02-0')
    tds = id.findAll('td')
    industry_name = tds[1].text
    industry_url = 'http://money.finance.sina.com.cn'+tds[2].find('a').get('href')

    industry_req = requests.get(industry_url)
    industry_html = industry_req.text
    # print(industry_html)

    industry_soup = bs(industry_html,'html')
    industry_id = industry_soup.find(id = 'CirculateShareholderTable')
    trs = industry_id.findAll('tr')
    industry_stock_name = []
    industry_stock_code = []
    i = 0
    for tr in trs:
        if i >1:
            tds = tr.findAll('td')
            industry_stock_name.append(tds[0].text)
            industry_stock_code.append(tds[3].text)
        i = i+1
    industry_stock_dict = {}
    industry_stock_dict['industry_stock_name'] = industry_stock_name
    industry_stock_dict['industry_stock_code'] = industry_stock_code
    return industry_stock_dict



if __name__ == '__main__':
    url = 'http://money.finance.sina.com.cn/corp/go.php/vCI_CorpOtherInfo/stockid/002340.phtml'
    req = requests.get(url)
    html = req.text

    soup = bs(html, 'html')

    id = soup.find(id = 'con02-0')
    tds = id.findAll('td')
    industry_name = tds[1].text
    print(industry_name)
    industry_url = 'http://money.finance.sina.com.cn'+tds[2].find('a').get('href')

    industry_req = requests.get(industry_url)
    industry_html = industry_req.text

    industry_soup = bs(industry_html,'html')
    industry_id = industry_soup.find(id = 'CirculateShareholderTable')
    trs = industry_id.findAll('tr')
    industry_stock_name = []
    industry_stock_code = []
    i = 0
    for tr in trs:
        if i >1:
            tds = tr.findAll('td')
            industry_stock_name.append(tds[0].text)
            industry_stock_code.append(tds[3].text)
        i = i+1
    industry_stock_dict = {}
    industry_stock_dict['industry_stock_name'] = industry_stock_name
    industry_stock_dict['industry_stock_code'] = industry_stock_code
    print(industry_stock_dict)
