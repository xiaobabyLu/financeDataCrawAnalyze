import requests
import requests.utils
from bs4 import BeautifulSoup as bs
from tqdm import tqdm

import dataScripy

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
}


def get_url(code):
    if (code[0] == '6' or code[0] == '9'):
        code_url = 'SHSE:' + code
    else:
        code_url = 'SZSE:' + code

    url =  f'https://www.gurufocus.cn/stock/{code_url}/term/gf_value'
    print(url)

    return url

def get_dashi_evaluate(code):
    url = get_url(code)

    req = requests.get(url,headers,verify=False)

    req.encoding = 'utf-8'

    soup = bs(req.text,'lxml')

    valueOBJ = soup.findAll(name="div", attrs={"class" :"text-body1 q-mt-md"})

    return valueOBJ[0].text


if __name__ == '__main__':

    url = 'https://cn.investing.com/equities/yili-company-consensus-estimates'

    url1 = 'https://cn.investing.com/equities/wangfujing-consensus-estimates'
    url2 = 'https://cn.investing.com/equities/fujian-torch-electron-tech-consensus-estimates'



    req = requests.get(url,headers,verify=False)
    req.encoding = 'utf-8'

    print(req.text)

    # print(get_dashi_evaluate('600887'))


    # code_pes = dataScripy.get_code_pe(1,350)

    # for codes in tqdm(code_pes):
    #     code = codes[0].strip('"')
    #
    #     try:
    #
    #         print(get_dashi_evaluate(code))
    #     except:
    #         print("错误：" + codes[1])
    #         continue
