import requests
from requests import RequestException
import urllib

'''
参考文章: https://blog.csdn.net/qq_29027865/article/details/84000942
微博文章 ： https://developer.51cto.com/article/665031.html
'''

def format_url(url, params: dict=None) -> str:
    query_str = urllib.parse.urlencode(params)
    return f'{ url }?{ query_str }'

def get_url(keyword):
    params = {
        'wd': str(keyword)
    }
    url = "https://www.baidu.com/s"
    url = format_url(url, params)
    print(url)

    return url


def get_page(url):
    try:
        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'max-age=0',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
        }
        response = requests.get(url=url,headers=headers)
        # 更改编码方式，否则会出现乱码的情况
        response.encoding = "utf-8"
        print(response.status_code)
        print(response.text)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None



if __name__ == '__main__':
    url = get_url("奖金")
    get_page(url)



