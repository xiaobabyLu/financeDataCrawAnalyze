import pandas as pd
import xlrd
from openpyxl import *
import os

'''
文章分析上市公司的成长能力，也就是获利营收能力

参考文章：https://www.cnblogs.com/lgyxta/p/13266964.html 读取文件报错解决
'''

#所有的列或者行
pd.set_option('display.max_columns', 500)
pd.set_option('max_colwidth',500)
pd.set_option('display.max_rows', 500)		# 显示行数

pd.set_option('display.width', 1000)       # 显示宽度




'''读取从同花顺下载的财务数据文件,转换为df'''
def read_excel(path= r'D:\develop\1.Python\item\test\financeDataCrawAnalyze\dataScripy\growth_power\000003.xlsx'):
    pd.set_option('display.notebook_repr_html',False)
    # 读取xls（绝对路径）
    df = pd.read_excel(path,header=1)
    return df

'''获取对应的扣非净利润和营收增长率'''
def get_rate(df):
    a = df.iloc[3].iat[1]
    b = df.iloc[5].iat[1]
    return a,b

if __name__ == '__main__':

    df = read_excel()
    get_rate(df)

    g = os.walk(r"D:\develop\1.Python\item\test\financeDataCrawAnalyze\dataScripy\growth_power")

    for path, dir_list, file_list in g:
        for file_name in file_list:
            filename = os.path.join(path, file_name)
            try:
                df = read_excel(filename)
                a,b = get_rate(df)
                if a == '--':
                    continue
                if b == '--':
                    continue
                a = float(a.strip("%"))
                b =  float(b.strip("%"))
                if a>50 and b> 70:
                    code = file_name.split('.')[0]
                    print(f'http://basic.10jqka.com.cn/144/{code}/finance.html')


            except:
                print('没有获取到数据：'+file_name)
                continue





