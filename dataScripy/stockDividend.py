import requests
import json

'''
https://eniu.com/gu/sh600887/dv
'''

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
    "Cookie": "gnKGLBelr6HN92kGkV2kGHpOPMXNIy1mLRhGWhWgAZp2DuVxr9zgdvwhx92aItYl; Hm_lvt_eac4547169afd7579f80d05491ed45ef=1657526727; Hm_lpvt_eac4547169afd7579f80d05491ed45ef=1657527267",
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Host": "wglh.com"
}

'''
根据要查询的code，获取需要的url
'''
def get_url(code):
    if (code[0] == '6' or code[0] == '9'):
        code_url = 'sh' + code
    else:
        code_url = 'sz' + code

    url = f'https://eniu.com/chart/dva/{code_url}/t/all'

    return url



def get_recent_dv(code):
    url = get_url(code)

    reqs = requests.get(url, headers)
    j = reqs.json()

    dvs = j.get('dv')
    last_dv = dvs[len(dvs) - 1]

    return float(last_dv)



if __name__ == '__main__':

    dv = get_recent_dv('601390')
    print(dv)


    url1 = 'https://eniu.com/table/gxba/sh600887'
    reqs1 = requests.get(url1,headers)
    js = reqs1.json()
    print(js)

