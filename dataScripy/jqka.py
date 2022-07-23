import urllib
from urllib import request
import pandas as pd
import dataScripy as ds
from bs4 import BeautifulSoup
import csv
import time
import datetime
import requests



'''
文章参考：https://zhuanlan.zhihu.com/p/91490234
'''



url = 'http://basic.10jqka.com.cn/144/600859/finance.html'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b20',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'spversion=20130314; historystock=300059%7C*%7C300033; userid=502126315; u_name=yufeijason; escapename=yufeijason; user=MDp5dWZlaWphc29uOjpOb25lOjUwMDo1MTIxMjYzMTU6NywxMTExMTExMTExMSw0MDs0NCwxMSw0MDs2LDEsNDA7NSwxLDQwOzEsMSw0MDsyLDEsNDA7MywxLDQwOzUsMSw0MDs4LDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAxLDQwOjE6Ojo1MDIxMjYzMTU6MTU3MzQ3MjYyNzo6OjE1NzM0NzI1MjA6NjA0ODAwOjA6MTc0NjVlMTY1NDVlNTMwY2JjYTU2YzgyY2U4NzkwMTAwOmRlZmF1bHRfMzow; ticket=29857a3a991e61c22242191bc7208932; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1572181059,1572196044,1572266592,1573472630; v=AiaG-hXJR3ghIRPcFWzSShOYd5erB2rHPEueJRDPEskkk8hBeJe60Qzb7-fj',
    'Host': 'q.10jqka.com.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
}

codes = ds.get_stock_codes()
for code in codes:
    Download_url = f'http://basic.10jqka.com.cn/api/stock/export.php?export=main&type=report&code={code}'
    print(Download_url)
    try:
        r = requests.get(Download_url,headers = headers,timeout = 400)
        r.encoding = 'gbk'
        path = f'.//growth_power/{code}.xlsx'
        f = open(path, "wb") # 项目路径下新增一个教师.xls文件
        f.write(r.content)
    except:
        print('错误码' + code)
        continue

f.close()




req = requests.get(url, headers=headers, timeout=15)
html = req.text

soup = BeautifulSoup(html, features='lxml')

trs = soup.find_all('td')
print(trs)


with open('codeinfo.csv', 'w', encoding='UTF-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(
        ["date", "code", "name", "price", "pct_chg", "shuangshou", "liangbi", "zhenfu", "amount", "liutonggu",
         "liutongshizhi", "shiyinglv"])
    urls = (['http://q.10jqka.com.cn/index/index/board/all/field/zdf/order/desc/page/{}/ajax/1/'.format(str(i)) for i in
             range(1, 20)])

    for url in urls:
        print(url)
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b20',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'spversion=20130314; historystock=300059%7C*%7C300033; userid=502126315; u_name=yufeijason; escapename=yufeijason; user=MDp5dWZlaWphc29uOjpOb25lOjUwMDo1MTIxMjYzMTU6NywxMTExMTExMTExMSw0MDs0NCwxMSw0MDs2LDEsNDA7NSwxLDQwOzEsMSw0MDsyLDEsNDA7MywxLDQwOzUsMSw0MDs4LDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAxLDQwOjE6Ojo1MDIxMjYzMTU6MTU3MzQ3MjYyNzo6OjE1NzM0NzI1MjA6NjA0ODAwOjA6MTc0NjVlMTY1NDVlNTMwY2JjYTU2YzgyY2U4NzkwMTAwOmRlZmF1bHRfMzow; ticket=29857a3a991e61c22242191bc7208932; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1572181059,1572196044,1572266592,1573472630; v=AiaG-hXJR3ghIRPcFWzSShOYd5erB2rHPEueJRDPEskkk8hBeJe60Qzb7-fj',
            'Host': 'q.10jqka.com.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        }
        html = requests.get(url, headers=headers, timeout=15).content
        soup = BeautifulSoup(html, features='lxml')
        time.sleep(3)
        for tr in soup.find_all("tr")[1:]:
            item = []
            tds = tr.find_all("td")
            date = datetime.date.today()
            code = tds[1].string
            name = tds[2].string
            price = tds[3].string
            change = tds[4].string
            pct_chg = tds[5].string
            shuangshou = tds[7].string
            liangbi = tds[8].string
            zhenfu = tds[9].string
            amount = tds[10].string
            liutonggu = tds[11].string
            liutongshizhi = tds[12].string
            shiyinglv = tds[13].string
            item.append(
                [date, code, name, price, pct_chg, shuangshou, liangbi, zhenfu, amount, liutonggu, liutongshizhi,
                 shiyinglv])

            for row in item:
                writer.writerow(row)
                print(item)

f.close

