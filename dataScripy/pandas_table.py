import pandas as pd
import json
import dataScripy as ds
from tqdm import tqdm
'''
参考文章：https://zhuanlan.zhihu.com/p/351603761
'''

def get_profit_by_code(code,num =0):

#url = https://q.stock.sohu.com/cn/600597/index.shtml

    url = f'https://q.stock.sohu.com/cn/{code}/index.shtml'
    print(url)
    # index:0 代表利润 2 代表业务构成
    tb = pd.read_html(url)[num]  # 经观察发现所需表格是网页中第4个表格，故为[3]

    # tb.to_csv(r'C:\Users\xxx\Desktop\1.csv', mode='a', encoding='utf_8_sig', header=1, index=0)
    # print('第' + str(i) + '页抓取完成')

    # print(tb)
    return tb

def get_finace_all(code,num):

    url = f'https://emweb.securities.eastmoney.com/PC_HSF10/FinanceAnalysis/Index?type=web&code=SZ002475'
    # html= requests.get(url).content
    #
    # bsObj = bs(html, "lxml")
    # #
    # tables = bsObj.find_all(id = 'report_zyzb')
    # print(str(tables[0]))
    # # index:0 代表利润 2 代表业务构成
    tb = pd.read_html(url)  # 经观察发现所需表格是网页中第4个表格，故为[3]

    print(len(tb))
    #
    # # tb.to_csv(r'C:\Users\xxx\Desktop\1.csv', mode='a', encoding='utf_8_sig', header=1, index=0)
    # # print('第' + str(i) + '页抓取完成')
    #
    # # print(tb)
    # return tb
    #
    # headers = {
    #     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
    # }
    #
    # html = requests.get(url, headers=headers)
    # html = html.text
    # soup = bs(html, 'html', from_encoding='utf-8')  # html
    #
    # # 谷歌浏览器 -> 审查元素 -> copy selector  如果截取不到，截取一部分前半部分
    # # body > div.content > div.right_frame > div:nth-child(2) > div.public_table_box.mg_tone
    # # content = soup.select('body > div.content > div.right_frame > div:nth-child(2) > div.public_table_box.mg_tone > div:nth-child(1) > div.public_ta_b_l_com.mg_tone > table')[0]
    # content = soup.select('#report_zcfzb_table')[0]
    # tf = pd.read_html(content.prettify(), header=0)  # prettify():页面美化（整理成有格式的） #myTable04
    # print(tf)


if __name__ == '__main__':

    df = get_profit_by_code(600859,0)
    print(df)
    all_code = dict()

    print(df.iat[3, 2])
    print(df.iat[2, 2])

    df = pd.read_html('http://www.dashiyetouzi.com/tools/stock.php?stock_id=600660',encoding='utf8')
    print(df)


    a = ds.get_code_pe(1, 400)
    for code in tqdm(a):
        sigle_code = dict()

        cod = code[0].strip('"')
        print(cod)
        try:
            df = ds.get_profit_by_code(cod, 0)
            s = df.iat[3, 2]
            p = df.iat[2, 2]
            if s == '-':
                s = '0'
            if p == '-':
                p = '0'

            sigle_code['s'] = s
            sigle_code['p'] = p
            all_code[cod] = sigle_code
            print(sigle_code)
        except:
            print("""aa""")
            continue

    json_str = json.dumps(all_code)
    print(json_str)
    with open('test_data.json', 'w') as json_file:
        json_file.write(json_str)