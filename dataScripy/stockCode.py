import requests
import re

'''
参考文章：https://zhuanlan.zhihu.com/p/159200115
'''


"""获取网页源码"""
def get_page(url):
    try:
        response = requests.get(url)
        return response.text
    except requests.ConnectionError as e:
        print('',e.args)

"""获取股票代码、名称、PE,最高价，最小价，市净率，市盈率"""

def get_stock_data(text):
   # .* ?"f9": (?P < pe >.+?) 匹配市盈率  .*?"f23":(?P<pb>.+?) 匹配市净率 ，注意需要按照f1,f2...这样的顺序
    com = re.compile('"f2":(?P<end>.+?),.*?"f6":(?P<volume>.+?),.*?"f9":(?P<pe>.+?),.*?"f12":(?P<number>.+?),.*?"f14":(?P<name>.+?)'
                     ',.*?"f15":(?P<max>.+?),.*?"f16":(?P<min>.+?),.*?"f17":(?P<start>.+?),.*?"f23":(?P<pb>.+?),.*?"f24":(?P<a>.+?)', re.S)

    ret = com.finditer(text)
    for i in ret:
        yield {
            'number': i.group('number'),
            'name': i.group('name'),
            'start': i.group('start'),
            'max': i.group('max'),
            'min': i.group('min'),
            'end': i.group('end'),

            'pe':i.group('pe'),#解析获取市盈率
            'pb':i.group('pb'),#解析市净率

            'a' :i.group('a'),
            'volume': i.group('volume')

        }


#开始页码，和结束解码
def get_code_pe(start=1, end=1):
    #将所有的股票代码放入列表中
    b = []
    for i in range(start, end+1):
        url = 'http://60.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112408744624686429123_1578798932591&pn=' \
              '%d&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:13,m:' \
              '0+t:80,m:1+t:2,m:1+t:23&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,' \
              'f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1586266306109' % i
        content = get_page(url=url)
        data = get_stock_data(text=content)

        for j in data:
            #定义获取股票代码，名字列表
            a =[]
            number = j.get('number')
            #加入股票代码
            a.append(number)
            name = j.get('name')
            #加入股票名字
            a.append(name)
            start = j.get('start')
            max_price = j.get('max')
            min_price = j.get('min')
            end = j.get('end')
            volume = j.get('volume')
            pe = j.get('pe')
            #加入市盈率
            a.append(pe)
            pb = j.get('pb')
            #加入市盈率
            a.append(pb)
            if start == '"-"':
                start, max_price, min_price, end, volume,pe,pb = '0', '0', '0', '0', '0','0','0'

            b.append(a)
    print(len(b))
    return b

def get_stock_codes():
    stock_codes = []
    lt = get_code_pe(1,380)
    for i in lt:
        stock_codes.append(i[0].strip('"'))
    print(stock_codes)
    return stock_codes


if __name__ == '__main__':
    get_stock_codes()