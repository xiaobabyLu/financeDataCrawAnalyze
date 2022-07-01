import requests
import re

"""获取网页源码"""
def get_page(url):
    try:
        response = requests.get(url)
        return response.text
    except requests.ConnectionError as e:
        print('',e.args)

"""获取股票代码、名称、PE"""
def get_stock_data(text):
    com = re.compile('"f2":(?P<end>.+?),.*?"f6":(?P<volume>.+?),.*?"f12":"(?P<number>.+?)",.*?"f14":"(?P<name>.+?)"'
                     ',.*?"f15":(?P<max>.+?),.*?"f16":(?P<min>.+?),.*?"f17":(?P<start>.+?),', re.S)

    ret = com.finditer(text)
    for i in ret:
        yield {
            'number': i.group('number'),
            'name': i.group('name'),
            'start': i.group('start'),
            'max': i.group('max'),
            'min': i.group('min'),
            'end': i.group('end'),
            'volume': i.group('volume')
        }



def main(start=1, end=1):
    for i in range(start, end+1):
        url = 'http://60.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112408744624686429123_1578798932591&pn=' \
              '%d&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:13,m:' \
              '0+t:80,m:1+t:2,m:1+t:23&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,' \
              'f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1586266306109' % i
        content = get_page(url=url)
        data = get_stock_data(text=content)

        for j in data:
            a =[]
            number = j.get('number')
            a.append(number)
            name = j.get('name')
            a.append(name)
            start = j.get('start')
            max_price = j.get('max')
            min_price = j.get('min')
            end = j.get('end')
            volume = j.get('volume')
            if start == '"-"':
                start, max_price, min_price, end, volume = '0', '0', '0', '0', '0'

            print(a)

if __name__ == '__main__':
    main(1,1000)