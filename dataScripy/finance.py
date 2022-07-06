import time
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup as bs


import requests
'''
参考文章 ：get_finance_report： https://cloud.tencent.com/developer/article/1358519

get_search_theche: https://blog.csdn.net/u011541946/article/details/70140812
                   https://blog.csdn.net/shenyuan12/article/details/108033287
                   https://blog.csdn.net/qq_39844123/article/details/96884789
                   https://blog.51cto.com/aoian/4893246
'''

def get_finance_report():
    # 当测试好能够顺利爬取后，为加快爬取速度可设置无头模式，即不弹出浏览器
    # 添加无头headlesss 1使用chrome headless,2使用PhantomJS
    # 使用 PhantomJS 会警告高不建议使用phantomjs，建议chrome headless
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    # browser = webdriver.Chrome(chrome_options=chrome_options)
    # browser = webdriver.PhantomJS()
    # browser.maximize_window()  # 最大化窗口,可以选择设置

    # 加载启动项，这里设置headless，表示不启动浏览器，只开一个监听接口获取返回值
    browser = webdriver.Chrome("E:\\software\chromedriver.exe",80,chrome_options)


    browser.get('http://data.eastmoney.com/bbsj/201806/lrb.html')
    element = browser.find_element_by_css_selector('tbody')  # 定位表格，element是WebElement类型
    # 提取表格内容td
    td_content = element.find_elements_by_tag_name("td") # 进一步定位到表格内容所在的td节点
    lst = []  # 存储为list
    for td in td_content:
        lst.append(td.text)
    print(lst) # 输出表格内容

    col = len(element.find_elements_by_css_selector('tr:nth-child(1) td'))
    print(col)

    browser.quit()


def get_search_theche():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')

    browser = webdriver.Chrome("E:\\software\chromedriver.exe",80,chrome_options)


    browser.get('https://cn.investing.com/equities/yili-company-technical')

    browser.find_elements_by_class_name("searchText")[0].send_keys('300181')

    time.sleep(5)
    # browser.find_elements_by_class_name('row')[0].click()
    a = browser.find_element_by_css_selector("[class='row js-quote-row-template js-quote-item']")



    time.sleep(5)
    browser.get(a.get_attribute('href') + '-technical')


#https://cn.investing.com/equities/zhejiang-jolly-pharma-technical

    print(browser.current_url)
    return browser.current_url

    # browser.quit()
if __name__ == '__main__':
    url = get_search_theche()
    rep = requests.get('https://cn.investing.com/equities/zhejiang-jolly-pharma-technical')
    bsObj = bs(rep.text)
    tables = bsObj.findAll('table',{'id':'curr_table'})
    print(len(tables))

    for table in tables:
        table = str(table)
        print(table)
        tb = pd.read_html(str(table), encoding='utf-8',header=0)[0]
        print(tb)